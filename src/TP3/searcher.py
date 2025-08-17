from TP3.book_manager import BookManager
from TP3.book import *
from abc import ABC, abstractmethod
    
class ISearcher(ABC):
    def __init__(self, book_manager: BookManager):
        self.books = book_manager.books

    @abstractmethod
    def search(self, search_term):
        pass

    # def displaySearchResult(self, results):
    #     if len(results)== 0:
    #         {f"Résultats de recherche: auncune resultats"}
    #     else:
    #         (f"Résultats de recherche: {len(results)} livre(s) trouvé(s)")
    #         for result in results:
    #             print(result)

class SearcherByTitle(ISearcher):
    def search(self, search_term):
        return [book for book in self.books if search_term.lower() in book.getTitle().lower()]
    
class SearcherByAuthor(ISearcher):
    def search(self, search_term):
        return [book for book in self.books if search_term.lower() in book.getAuthor().lower()]

class SearcherByISBN(ISearcher):
    def search(self, search_term):
        return [book for book in self.books if search_term in book.getISBN()]

class SearcherByCategory(ISearcher):
    def search(self, search_term):
        return [book for book in self.books if search_term.lower() in book.getCategory().lower()]