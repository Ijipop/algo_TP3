from TP3.notification_manager import NotificationManager
from TP3.book import *
from abc import ABC, abstractmethod
# import datetime

class BookManager:
    def __init__(self, notification_manager: NotificationManager):
        self.notification_manager = notification_manager
        self.books: list[Book] = []
    
    # def add_book(self, title: str, author: str, isbn: str, category: str):
    #     book = Book(title, author, isbn, category)
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
    
    def search_books_by_title(self, search_term):
        results = [book for book in self.books if search_term.lower() in book.getTitle().lower()]
        return results
    
    def search_books_by_author(self, search_term):
        results = [book for book in self.books if search_term.lower() in book.getAuthor().lower()]
        return results
    
    def search_books_by_ISBN(self, search_term):
        results = [book for book in self.books if search_term in book.getISBN()]
        return results
    
    def search_books_by_Category(self, search_term):
        results = [book for book in self.books if search_term.lower() in book.getCategory().lower()]
        return results

    # def add_book(self, title: str, author: str, isbn: str, category: str):
    #     book = {
    #         'id': len(self.books) + 1,
    #         'title': title,
    #         'author': author,
    #         'isbn': isbn,
    #         'category': category,
    #         'available': True,
    #         'added_date': datetime.datetime.now().isoformat()
    #     }
    #     self.books.append(book)
        
    #     self.notification_manager.notify(f"Nouveau livre ajouté - {title}")
        
    #     return book