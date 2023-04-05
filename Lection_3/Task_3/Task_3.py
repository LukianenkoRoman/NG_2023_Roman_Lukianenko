books = []

def add_book():
    author = input("Enter the author name: ")
    title = input("Enter the name of the book: ")
    genre = input("Enter genre: ")
    binding = input("Chose binding: ")
    pages = int(input("Enter the number of pages: "))
    book = {"author": author, "title": title, "pages": pages}
    books.append(book)
    print(f"The book '{title}' by {author} with {pages} pages has be added.")

def print_books():
    if len(books) == 0:
        print("The book list is empty.")
    else:
        print("Book List:")
        for book in books:
            print(f"{book['author']}: '{book['title']}', {book['pages']} pages")

def search_books_by_author():
    author = input("Enter the author name to search: ")
    author_books = []
    for book in books:
        if book['author'] == author:
            author_books.append(book)
    if len(author_books) == 0:
        print(f"No books found by {author}.")
    else:
        print(f"Books by {author}:")
        for book in author_books:
            print(f"{book['author']}: '{book['title']}', {book['pages']} pages")

def Redact_book():
    def edit_book():
     author = input("Enter the author's name: ")
    title = input("Enter the title of the book: ")

    for book in books:
        if book["title"] == title:
            pages = input("Redact the new number of pages: ")
            book["pages"] = pages
            bining = input("Redact bining")
            book["bining"] = bining
            genre = input("Redact genre")
            book["genre"] = genre
            print("Book updated successfully!")
            return

    print("Book not found.")

    

while True:
    print("nSelect the action:")
    print("1.Add book")
    print("2.Print book list")
    print("3.Search books by author")
    print("4.Redact book") 
    print("5.End")

    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        print_books()
    elif choice == "3":
        search_books_by_author()
    elif choice == "4":
        Redact_book()
    elif choice == "5":
        break
    else:
        print("Invalid comand")


