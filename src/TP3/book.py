import datetime

class Book:
    nb_books: int = 0
    
    def __init__(self, title: str, author: str, isbn: str, category: str, available: bool = True):
        Book.nb_books += 1
        self.id: int = Book.nb_books
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.category: str = category
        self.available: bool = available
        self.added_date: datetime = datetime.datetime.now().isoformat()

    def getId(self): return self.id
    def getTitle(self): return self.title
    def getAuthor(self): return self.author
    def getISBN(self): return self.isbn
    def getCategory(self): return self.category
    def getAvailable(self): return self.available
    def getAddedDate(self): return self.added_date

    def setAvailable(self, new_available: bool): self.available = new_available
    
    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nCategory: {self.category}\nAvailable: {self.available}\nAdded Date: {self.added_date}"

        # book = {
        #     'id': {self.id},
        #     'title': {self.title},
        #     'author': {self.author},
        #     'isbn': {self.isbn},
        #     'category': {self.category},
        #     'available': {self.available},
        #     'added_date': {self.added_date}
        # }
        # return str(book)