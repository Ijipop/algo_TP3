from TP3.notification_manager import NotificationManager
from TP3.user_manager import UserManager
from TP3.book_manager import BookManager
from TP3.loan import *
from TP3.book import *
from TP3.user import *
from TP3.rules import *

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

    def return_book(self, loan_id):
        loan = self.find_loan(loan_id)
        book = self.find_book(loan.getBookId())
        
        for rule in self.rulesReturn:
            if not rule.check(loan, self.loans, loan.getBookId()):
                print(f"Erreur: {rule.getRuleReason()}")
                return False
        
        loan.setReturned(True)
        loan.setReturnDate(datetime.datetime.now().isoformat())

        book.setAvailable(True)

        self.notification_manager.notify(f"Retour effectué - ID Emprunt: {loan_id}")

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