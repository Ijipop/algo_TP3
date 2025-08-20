from TP3.notification_manager import NotificationManager
from TP3.book_manager import BookManager
from TP3.user_manager import UserManager
from TP3.loan_manager import LoanManager
from TP3.overdue_manager import OverdueManager

class Library:
    def __init__(self, notification_manager: NotificationManager):
        self.notification_manager = notification_manager
        self.book_manager = BookManager(notification_manager)
        self.user_manager = UserManager(notification_manager)
        self.loan_manager = LoanManager(notification_manager, self.user_manager, self.book_manager)
        self.overdue_manager = OverdueManager(notification_manager, self.user_manager, self.book_manager, self.loan_manager)