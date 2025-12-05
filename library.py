### Creating two file named users.txt and books.txt to store user information and books information permanently inside the file
        
import os

if not os.path.exists('users.txt'):
    with open('users.txt', 'w') as f:
        pass
if not os.path.exists('books.txt'):
    with open('books.txt', 'w') as f:
        pass

### load data from the file
def load_user():
    """Load all the users from user.txt into dictionary"""
    users_dict = {}

    try:
        with open('users.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(',')
                    users_dict[username] = password
    except FileNotFoundError:
        print("File not found!")
    
    return users_dict

# book_id,title,author,quantity

def load_books():
    books_list = []
    try:
        with open("books.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    book_id, title, author, quantity = line.split(',')

                    book = {
                        'id': book_id,
                        'title': title,
                        'author': author,
                        'quantity': int(quantity)
                    }
                    books_list.append(book)

    except FileNotFoundError:
        print("file not found!")
    return books_list

                    
def get_existing_books_id(books_list):
    """Create a set to store all the ids of the books"""
    book_ids = set()
    for book in books_list:
        # dictionary
        book_ids.add(book['id'])
    return book_ids

#### User registration
def register_user(users_dict):
    """Register a new user"""
    print("\n---- Register a New user ----")
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()
    if username in users_dict:
        print(f"username alrealy exists!")
        return False
    if not username or not password:
        print("Username and password cannot be empty")
        return False
    users_dict[username] = password

    # save the registered user to the file 'users.txt'
    with open('users.txt', 'a') as f:
        f.write(f"{username},{password}\n")

    print("registration successfull!")
    return True

users_dict = load_user()
print(users_dict)
register_user(users_dict)

def login_user(users_dict):
    print("\n----login user----")
    username = input("enter username: ").strip()
    password = input("enter password: ").strip()
    
    if username in users_dict and users_dict[username] == password:
       print(f"Welcome! {username.capitalize()}")
       return username
    else:
        print("invalid username or password")
        return None

login_user(users_dict) 


## Now book operation start 

### main menu function
def main_menu():
    """Display  main menu options"""
    print("="*55)
    print("\n library management system")
    print("="*55)
    print("1. Add book")
    print("2.view all books")
    print("3.Search book")
    print("4.Issue book")
    print("5.Return book")
    print("6.Logout")
    print("="*55)
  
    
#main_menu()


#add book 
def add_book(books_list, book_ids):
    """add a new book to the laibrary"""
    print("\n-----Add New book------")
    book_id = input("enter the book id: ").strip()
    
    if book_id in book_ids:
        print("Book id already exist !!")
        return
    
    title = input("enter the book title: ").strip()
    author = input("enter the  author: ").strip()
    quantity = int(input("enter the quantity: ").strip())
    
    
    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'quantity': quantity
    }
    
    books_list.append(new_book)
    book_ids.add(book_id)
    
    with open('books.txt', 'a') as f:
        f.write(f"{book_id},{title},{author},{quantity}\n")
    
    print("Book added successfuly")


books_list = load_books()
book_ids = get_existing_books_id(books_list)
print(books_list)
print(book_ids)
add_book(books_list, book_ids)



#Function to view  all the book in library

def view_books(books_list):
    """display all the books in the library """
    print("\n ------All book in library-----")
    if not books_list:
        print("no books found in library!!")
        return
    for book in books_list:
        print(f"{book['id']}| {book['title']}| {book['author']}|{book['quantity']}")
view_books(books_list)

## search a book using title or author
def search_book(books_list):
    """search book by book title or author name"""
    found_items = []
    search_term=input("search here: ").strip().lower()
    
    
    for book in books_list:
        if search_term in book['title']or search_term in book['author']:
            found_items.append(book)
    if not found_items:
        print(f"found{len(found_items)} books")
        view_books(found_items)
        
    else:
        print("no bboks found matching your search")
        
#search_book(books_list)

#save books to the file

"""save all the books to the file"""
def save_books(books_list):
    """write all books back to books.txt file """
    with open('books.txt', 'w') as f:
        for book in books_list:
            f.write(f"{book['id']},{book['title']},{book['author']},{book['quantity']}\n")


## issue book--> user le library bata book lanu
def issue_book(books_list):
    book_id = input("enter the book id to issue: ").strip()
     
    for book in books_list:
        if book['id']== book_id:
            if book['quantity']>0:
                book['quantity']-=1
                
                save_books(books_list)
                print(f"book{book['title']} issued successfully!!")
                print(f"remaining quantity:{book['quantity']}")
            else:
                print("book is currently  out of stock!!")
                return
        print("book id not found!!!")
        
def return_book(books_list):
    """Return a book to a user"""
    book_id=input("enter the book id to return: ").strip()
    for book in books_list:
        if book['id']==book_id:
            book['quantity'] +=1
            
            save_books(books_list)
            
            print(f"book{book['title']} returned successfully!!") 
            print(f"current quantity: {book['quantity']}")
            return
    print("book id not found")
add_book(books_list,book_ids)
issue_book(books_list)
return_book(books_list)   

## MAIN FUNCTION --> CONTROL OVERALL PROGRAM FLOW

def main():
    "MAIN PROGRAM LOOP"
    users_dict = load_user
    
    print("-"*50)
    print("-----Welcomr to library management system-----")
    print("="*50)
    
    while True:
        print ( "\n 1.register")
        print ( "\n 2.Login")
        print ( "\n 3.EXIT")
        
        choice =input("\n Enter choice(1,2,3): ").strip()
        
        if choice =='1':
            register_user(users_dict)
            
        elif choice =='2':
            username = login_user(users_dict)
            
            if username:
                books_list = load_books
                book_ids =get_existing_books_id(books_list)
                 
                while True:
                    main_menu()
                    menu_choice = input("\n Enter choice (1-6): ")
                    if menu_choice == '1':
                        add_book(books_list,book_ids)
                    elif menu_choice == '2':
                        view_books(books_list)
                    elif menu_choice == '3':
                        search_book(books_list)
                    elif menu_choice == '4':
                        issue_book (books_list)
                    elif menu_choice == '5':
                        return_book(books_list,book_ids)
                    elif menu_choice == '6' :
                        print(f"bye{username.capitalize()}!")
                        break
                    else:
                        print("invalid choice!!")
                           
        elif  choice =='3':
            print("exiting the program!!")
            break
                           