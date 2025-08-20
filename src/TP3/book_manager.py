from TP3.notification_manager import NotificationManager
from TP3.book import *
# import datetime

class BookManager:
    def __init__(self, notification_manager: NotificationManager):
        self.notification_manager = notification_manager
        self.books: list[Book] = []
    
    def add_book(self, book: Book):
        self.books.append(book)
        self.notification_manager.notify(f"Nouveau livre ajouté - {book.getTitle()}")
        return book
    
    def remove_book(self, book_id: int):
        for i, book in enumerate(self.books):
            if book.getId() == book_id:
                if not book.getAvailable():
                    print("Erreur: Le livre est actuellement emprunté")
                    return False
                
                del self.books[i]
                
                self.notification_manager.notify(f"Livre supprimé - ID {book_id}")
                return True
        return False