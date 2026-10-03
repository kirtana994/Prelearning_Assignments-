#Write a class for a library system that allows adding/removing books and searching by title.
class library:
    def __init__(self):
        self.books=[]

    def add_book(self,title):
        self.books.append(title)
        print(f"Books {title} has been added to the library.")

    def remove_book(self,title):
        if title in self.books:
             self.books.remove(title)
             print(f"Book {title} has been removed from the library.")
        else:
            print(f"Book {title} not found in the library.")
        
    def search_book(self,title):
        if title in self.books:
            print(f"Book {title} is available in the library.")
        else:
              print(f"Book {title} is not available in the library.") 

library1=library()
while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        library1.add_book(title)

    elif choice == "2":
        title = input("Enter book title to remove: ")
        library1.remove_book(title)

    elif choice == "3":
        title = input("Enter book title to search: ")
        library1.search_book(title)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")