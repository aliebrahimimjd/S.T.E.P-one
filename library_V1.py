import json
books = {}
users = {}
def add_book():
    name = input("input name book ")
    author = input("enter name author")
    age = input("enter year ")
    pages = input("enter number of pages")
    if name in books:
        books[name]["count"] += 1
    else :
        books[name] = {}
        books[name]["author"] = author
        books[name]["year"] = age
        books[name]["pages"] = pages
        books[name]["rent"] = "you can rent this"
        books[name]["count"] = 1
def sing_up():
    while True:
        name = input("enter your name ")
        if name in users : 
            print("this name useed")
            continue
        users[name] = []
        break
def show():
    number = 1
    for key in books:
        print(number , key)
        number += 1
def search():
    show()
    value = input("enter name's book ")
    if value in books :
        print(value , books[value])
    else :
        print("we haven't book ")
def rent():
    usere = input("enter your name")
    if usere in users:
        book = input("enter name's book ")
        if book in books:
            if books[book]["count"] > 0 :
                users[usere].append(book)
                books[book]["rent"] = "this book isn't Available"
                books[book]["count"] -= 1
            else : 
                print("this book already have rent")
        else :
            print("this book isn't exsist")
def back():
    name = input("enter your name ")
    if name in users :
        t = 1
        for i in users[name]:
            print(t , i)
            t += 1 
        x = int (input("enter number's book"))
        q = users[name][x - 1]
        books[q]["count"] += 1
        users[name].remove(q)
        books[q]["rent"] = "you can rent this"
def use():
    name = input("enter name ")
    if name in users:
        pritn(name, users[name])
def save():
    with open("users.json" , "w") as users_file:
        json.dump(users , users_file)
    with open("books.json" , "w") as books_file:
        json.dump(books , books_file)
def load():
    try:
        with open("users.json" ,"r") as users_file:
            users.update(json.load(users_file))
    except:
        print("file isn't exsist")
    else : 
        print("load data was succsful")
    
    try :
        with open("books.json", "r") as books_file:
            books.update(json.load(books_file))
    except:
        print("file isn't exsist")
    else :
        print("load data was succsful")
                
                
                
                
                
                
                
                