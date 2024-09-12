class Library:
    def __init__(self,books):
        self.books = books

    def list_books(self):
        print("available books")
        for book in books:
            print(book)
    def borrow_book(self,borrowed_book):
        if borrowed_book in self.books:
            print("get ur book now ")
            self.books.remove(borrowed_book)
        else:
            print("book not available")
    def receive_book(self,receivebook):
        print("you have retunred the book")
        self.books.append(receivebook)



books = ["c","c++","Java"]
o=Library(books)

msg = """
    1.Display Book
    2.Borrow Book
    3.Return Book
"""
while True:
    print(msg)
    ch = int(input("enter ur choice:"))
    if ch == 1:
        o.list_books()
    elif ch ==2:
        book = input("Enter Book Name To Borrow : ")
        o.borrow_book(book)
    elif ch == 3:
        book = input("Enter Book Name To return : ")
        o.receive_book(book)
    else:
        print("thanks come again")




