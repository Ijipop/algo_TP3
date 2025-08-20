import datetime
from TP3.loan import Loan
from TP3.user import User
from TP3.book import Book

class Overdue():
    nb_overdues: int = 0
    
    def __init__(self, loan: Loan, user: User, book: Book, current_date: datetime):
        Overdue.nb_overdues += 1
        self.id: int = Overdue.nb_overdues
        self.loan = loan
        self.user = user
        self.book = book
        self.days_overdue = (current_date - loan.getDueDate()).days

    def getId(self): return self.id
    def getLoan(self): return self.loan
    def getUser(self): return self.user
    def getBook(self): return self.book
    def getDaysOverdue(self): return self.days_overdue
    
    def __str__(self):
        return f"ID: {self.id}\nLoan: {self.loan.getId}User: {self.user.getId}\nBook: {self.book.getId}\nDays Overdue: {self.days_overdue}"
