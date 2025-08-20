from TP3.loan import *
from TP3.book import *
from TP3.user import *
from abc import ABC, abstractmethod

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
        # print(user.getMaxLoans())
        # print(loans)
        if user.getMaxLoans() == -1:
            return True
        return len(loans) < user.getMaxLoans()
    
    def getRuleReason(self, user):
        return f"Limite d'emprunts atteinte pour les {user.showType()}s"
    
class IRuleReturn(ABC):
    @abstractmethod
    def check(self, loan: Loan, loans: list[Loan], book_id: int) -> bool:
        pass

    @abstractmethod
    def getRuleReason(self, user: User) -> str:
        pass

class RuleLoanFound(IRuleReturn):
    def check(self, loan, loans, book_id):
        return loan

    def getRuleReason(self):
        return "Emprunt introuvable"
    
class RuleLoanReturned(IRuleReturn):
    def check(self, loan, loans, book_id):
        for loan in loans:
            if loan.getId() == book_id:
                # if loan.getReturned():
                return not loan.getReturned()

    def getRuleReason(self):
        return f"Livre déjà retourné"