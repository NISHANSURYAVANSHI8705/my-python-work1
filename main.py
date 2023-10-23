# def add():
#     a = 87
#     b = 98
#     c = a+b
#     print(c)
#
# add()
#
#
# def sub():
#     s = 2
#     o = 5
#     v = s-o
#     print(v)
#
# sub()
#
# def div():-00
#     d = 4
#     g = 2
#     n = d/g
#     print(n)
#
# div()

dict = {}
def add_book():
    title = input("enter the title of books: ")
    author = input("enter the author: ")
    publication_year = int(input("enter publication year: "))
    genre = input("enter genre: ")
    dict[title] = {"Author":author ,"publication year":publication_year ,"genre":genre}
    print("dict")

add_book()