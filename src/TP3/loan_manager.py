from TP3.notification_manager import NotificationManager
from TP3.user_manager import UserManager
from TP3.book_manager import BookManager
from TP3.loan import *
from TP3.book import *
from TP3.user import *
from abc import ABC, abstractmethod

class LoanManager:
    def __init__(self, notification_manager: NotificationManager, user_manager: UserManager, book_manager: BookManager):
        self.notification_manager = notification_manager
        self.user_manager = user_manager
        self.book_manager = book_manager
        self.loans: list[Loan] = []
        self.rulesBorrow = [
            RuleUserAndBookFound(),
            RuleBookAvailable(),
            RuleUserActive()
        ]
        self.rulesReturn = [
            RuleLoanReturned(),
            RuleLoanFound()
        ]
    
    def borrow_book(self, user_id: int, book_id: int) -> bool:
        user = self.find_user(user_id)
        book = self.find_book(book_id)

        current_loans: list[Loan] = [loan for loan in self.loans if loan.getUserId() == user_id and not loan.getReturned()]
        
        for rule in self.rulesBorrow:
            if not rule.check(book, user, current_loans):
                print(f"Erreur: {rule.getRuleReason(user)}")
                return False

        loan = Loan(user_id, book_id)
        loan.setDueDate(user.getLoanDuration())
        
        book.setAvailable(False)

        self.loans.append(loan)

        self.notification_manager.notify(f"Emprunt effectué - Livre: {book.getTitle()}, Utilisateur: {user.getName()}")

        return True

    def find_user(self, id: int) -> User:
        for u in self.user_manager.users:
            if u.getId() == id:
                return u
        return None
    
    def find_book(self, id: int) -> Book:
        for b in self.book_manager.books:
            if b.getId() == id:
                return b
        return None
    
    def find_loan(self, id: int) -> Loan:
        for l in self.loans:
            if l.getId() == id:
                return l
        return None
    
    def calculate_due_date(self, days: int):
        if days == -1:
            days == None
        due_date = datetime.datetime.now() + datetime.timedelta(days=days)
        return due_date.isoformat()

    def return_book(self, loan_id):
        loan = self.find_loan(loan_id)
        book = self.find_book(loan.book_id())
        
        for rule in self.rulesReturn:
            if not rule.check(loan, self.loans, loan.book_id()):
                print(f"Erreur: {rule.getRuleReason()}")
                return False

        
        loan.setReturned(True)
        loan.setReturnDate(datetime.datetime.now().isoformat())

        book.setAvailable(True)

        self.notification_manager.notify(f"Retour effectué - ID Emprunt: {loan_id}")

        return True

    def generate_overdue_report(self):
        pass

class IRuleBorrow(ABC):
    @abstractmethod
    def check(self, book: Book, user: User, loans: list[Loan]) -> bool:
        pass

    @abstractmethod
    def getRuleReason(self, user: User) -> str:
        pass

class RuleUserAndBookFound(IRuleBorrow):
    def check(self, book, user, loans):
        return user and book

    def getRuleReason(self, user):
        return "Utilisateur ou livre introuvable"

class RuleUserActive(IRuleBorrow):
    def check(self, book, user, loans):
        return user.getActive()

    def getRuleReason(self, user):
        return "Utilisateur inactif"

class RuleBookAvailable(IRuleBorrow):
    def check(self, book, user, loans):
        return book.getAvailable()
    
    def getRuleReason(self, user):
        return "Livre non disponible"
    
class RuleUserMaxLoans(IRuleBorrow):
    def check(self, book, user, loans):
        if user.getMaxLoans() == -1:
            return True
        return len(loans) < user.getMaxLoans()
    
    def getRuleReason(self, user):
        return f"Limite d'emprunts atteinte pour les {user.showType()}s"
    
class IRuleReturn(ABC):
    @abstractmethod
    def check(self, loan: Loan, loans: list[Loan]) -> bool:
        pass

    @abstractmethod
    def getRuleReason(self, user: User) -> str:
        pass

class RuleLoanFound(IRuleReturn):
    def check(self, loan, loans):
        return loan

    def getRuleReason(self):
        return "Emprunt introuvable"
    
class RuleLoanReturned(IRuleReturn):
    def check(self, loan, loans, book_id):
        for loan in loans:
            if loan.getId() == book_id():
                if loan.getReturned():
                    return True

    def getRuleReason(self):
        return f"Livre déjà retourné"