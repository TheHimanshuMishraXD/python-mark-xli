# Write a Library class with no_of_books and books as two instance variables.
#  Write a program to create a library object using this Library class and show how you can print all books,
#   add a book and get the number of books using different methods. 
#   Show that your program doesn’t persist the books after the program is stopped!



class Library:
    def __init__ (self , no_books,books1):
        self.nobooks = no_books
        self.book = books1


    def showbooks(self):
            print(self.book)


    def addbook(self):

            s = int(input("how many books you wants to add:  "))
            for i in range(s):
                 book = input(f"enter the books {i+1}:")
                 
                 self.book.append(book)
                 self.nobooks +=1


    def countbook(self):
            print((self.nobooks))


a = Library(0,[])

a.addbook()


print(f"the books you want to know {a}")
a.showbooks()





#code is end succesfully








# class Library:
#     def __init__(self):
#         self.num_of_books = 0
#         self.books = []

#     def add(self):
#         s = int(input("How many books do you want to store? "))
#         for v in range(1, s + 1):
#             book = input(f"Enter book {v}: ")
#             self.num_of_books += 1
#             self.books.append(book)

#     def check(self):
#         if self.num_of_books == len(self.books):
#             print("Ok")
#         else:
#             print("Error")

# a = Library()
# a.add()
# a.check()
# print(f"Your books: {a.books}")

    




        