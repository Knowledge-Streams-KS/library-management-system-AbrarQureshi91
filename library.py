class Book: 

    def __init__(self , title , author, ISBN ,  pages , price ):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self. pages =  pages
        self.price = price 

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Number of Pages: {self.pages}")
        print(f"Price: ${self.price}")

class ReferenceBook(Book):

    def __init__(self, title, author, ISBN, pages, price , reference_type):
        super().__init__(title, author, ISBN, pages, price)
        self.reference_type = reference_type

    def display_book(self):
        super().display_book()
        print(f"Reference Type: {self.reference_type}")

        
    

class FictionBook(Book):
    def __init__(self, title, author, ISBN, pages, price ,  genre ):
        super().__init__(title, author, ISBN, pages, price )
        self.genre = genre

    def display_book(self):
        super().display_book()
        print(f"Genre: {self.genre}")
        
        
class Library:

    def __init__(self):
        self.books = {}

    def add_book(self , book):
        self.books[book.title]= book
    
    def display_books(self  ):
        for book in self.books.values():
         book.display_book()
         print("\n")
        

    def search_book_by_title(self, title):
        if title in self.books:
            book = self.books[title]
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN: {book.ISBN}")
            print(f"Number of Pages: {book.pages}")
            print(f"Price: {book.price}")
        else:
            print("Book not found.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print("Book removed successfully.")
        else:
            print("Book not found.")
        
reference_type = ReferenceBook("Hardcover",    "Abrar"     , 100716601230 , 1400  , 6000 ," Encyclopedia" )
fictionbook  = FictionBook("Love"  ," Najeeb" , 1073686456637 , 45 ,5000 , "Romance" )

library = Library()

library.add_book(reference_type)
library.add_book(fictionbook)


library.display_books()


library.search_book_by_title("Love" )


library.remove_book("Hardcover")



