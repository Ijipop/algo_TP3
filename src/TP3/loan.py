from abc import ABC, abstractmethod
import datetime

class Loan():
    nb_loans: int = 0
    
    def __init__(self, user_id: int, book_id: int):
        self.nb_loans += 1
        self.id: int = self.nb_loans
        self.user_id: int = user_id
        self.book_id: int = book_id
        self.loan_date: datetime = datetime.datetime.now().isoformat()
        self.due_date: datetime
        self.returned: bool
        self.return_date: datetime

    def getId(self): return self.id
    def getUserId(self): return self.user_id
    def getBookId(self): return self.book_id
    def getLoanDate(self): return self.loan_date
    def getDueDate(self): return self.due_date
    def getReturned(self): return self.returned
    def getReturnDate(self): return self.return_date
    
    def __str__(self):
        return f"ID: {self.id}\nUser ID: {self.user_id}\nBook ID: {self.book_id}\nLoan Date: {self.loan_date}\nDue Date: {self.due_date}\nReturned: {self.returned}\nReturn Date: {self.return_date}"
        