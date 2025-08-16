from abc import ABC, abstractmethod
import datetime

class User(ABC):
    nb_users: int = 0
    
    # @abstractmethod
    def __init__(self, name: str, email: str):
        self.nb_users += 1
        self.id: int = self.nb_users
        self.name: str = name
        self.email: str = email
        self.max_loans: int = 0
        self.loan_duration: int = 0 # days
        self.registration_date: datetime = datetime.datetime.now().isoformat()
        self.active: bool = True

    def getId(self): return self.id
    def getName(self): return self.name
    def getEmail(self): return self.email
    def getMaxLoans(self): return self.max_loans
    def getLoanDuration(self): return self.loan_duration
    def getRegistrationDate(self): return self.registration_date
    def getActive(self): return self.active

    def setActive(self, new_active: bool): self.active = new_active

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nE-mail: {self.email}\nMax Loans: {self.max_loans}\nLoad Duration: {self.loan_duration}\nRegistration Date: {self.registration_date}\nActive: {self.active}"
    
    # def can_burrow(self, loan: int):
    #     return loan < self.max_loans
class UserStudent(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.max_loans = 3
        self.loan_duration = 14

class UserTeacher(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.max_loans = 10
        self.loan_duration = 30

class UserAdmin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.max_loans = -1     # unlimited
        self.loan_duration = -1 # unlimited