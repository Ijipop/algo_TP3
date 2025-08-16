from TP3.notification_manager import NotificationManager
from TP3.book_manager import BookManager
from TP3.user_manager import UserManager
from TP3.loan_manager import LoanManager

class Library:
    def __init__(self, notification_manager: NotificationManager):
        self.notification_manager = notification_manager
        self.book_manager = BookManager(notification_manager)
        self.user_manager = UserManager(notification_manager)
        self.loan_manager = LoanManager(notification_manager, self.user_manager, self.book_manager)

    """
    def add_book(self, book: Book):
        return self.book_manager.add_book(book)

    def remove_book(self, book_id: int):
        return self.book_manager.remove_book(book_id)

    def add_user(self, user: User):
        return self.user_manager.add_user(user)

    def borrow_book(self, user_id: int, book_id: int):
        return self.loan_manager.borrow_book(user_id, book_id)

    def return_book(self, loan_id: int):
        return self.loan_manager.return_book(loan_id)

    def search_books_by_title(self, search_term):
        return self.book_manager.search_books_by_title(search_term)
    
    def search_books_by_author(self, search_term):
        return self.book_manager.search_books_by_author(search_term)
    
    def search_books_by_ISBN(self, search_term):
        return self.book_manager.search_books_by_ISBN(search_term)
    
    def search_books_by_Category(self, search_term):
        return self.book_manager.search_books_by_Category(search_term)

    def generate_overdue_report(self):
        return self.loan_manager.generate_overdue_report()
    """