# to get 5 author with book
# display last author and book

author_books = {}

for i in range(5):
    author_name = input("Enter author name") 
    book_name = input("Enter its book name")
    author_books[author_name] = book_name

print("Last auther is "+str(list(author_books.keys())[-1]))
print("Last book is "+str(list(author_books.values())[-1]))
#print(author_books)