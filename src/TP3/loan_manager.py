from TP3.notification_manager import NotificationManager
from TP3.user_manager import UserManager
from TP3.book_manager import BookManager
from TP3.loan import *

class LoanManager:
    def __init__(self, notification_manager: NotificationManager, user_manager: UserManager, book_manager: BookManager):
        self.notification_manager = notification_manager
        self.user_manager = user_manager
        self.book_manager = book_manager
        self.loans = []
    
    def borrow_book(self, user_id: int, book_id: int):
        user = self.find_user(user_id)
        book = self.find_book(book_id)

        pass

    def find_user(self, id: int):
        for u in self.user_manager.users:
            if u.getId == id:
                return u
        return None
    
    def find_book(self, id: int):
        for b in self.book_manager.books:
            if b.getId == id:
                return b
        return None
    
    def return_book(self, loan_id):
        pass
    
    def generate_overdue_report(self):
        pass