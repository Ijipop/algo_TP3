from abc import ABC, abstractmethod
import datetime

class Loan():
    nb_loans: int = 0
    
    def __init__(self, user_id: int, book_id: int):
        Loan.nb_loans += 1
        self.id: int = Loan.nb_loans
        self.user_id: int = user_id
        self.book_id: int = book_id
        self.loan_date: datetime = datetime.datetime.now().isoformat()
        self.due_date: datetime = None
        self.returned: bool = False
        self.return_date: datetime = None

    def getId(self): return self.id
    def getUserId(self): return self.user_id
    def getBookId(self): return self.book_id
    def getLoanDate(self): return self.loan_date
    def getDueDate(self): return self.due_date
    def getReturned(self): return self.returned
    def getReturnDate(self): return self.return_date

    def setLoanDate(self, new_date): self.loan_date = new_date
    def setReturned(self, new_returned): self.returned = new_returned
    def setReturnDate(self, new_date): self.return_date = new_date
    
    def setDueDate(self, loan_duration):
        if loan_duration == -1:
            self.due_date == None
        else:
            self.due_date = datetime.datetime.now() + datetime.timedelta(loan_duration)
    
    def __str__(self):
        return f"-----------\nID: {self.id}\nUser ID: {self.user_id}\nBook ID: {self.book_id}\nLoan Date: {self.loan_date}\nDue Date: {self.due_date}\nReturned: {self.returned}\nReturn Date: {self.return_date}\n-----------"
