from TP3.notification_manager import NotificationManager
from TP3.user_manager import UserManager
from TP3.book_manager import BookManager

class LoanManager:
    def __init__(self, notification_manager: NotificationManager, user_manager: UserManager, book_manager: BookManager):
        self.notification_manager = notification_manager
        self.user_manager = user_manager
        self.book_manager = book_manager
        self.loans = []
    
    def borrow_book(self, user_id, book_id):
        pass
    
    def return_book(self, loan_id):
        pass
    
    def generate_overdue_report(self):
        pass