from datetime import date
from abc import ABC, abstractmethod
import ast
from tabulate import tabulate
class Books(ABC): # Feature no 1.Abstract Class
    allbooks={}
    BooksTrack=[]
    requestedbooks=[]
    totalearn=0
    @staticmethod
    #To initialize the previously added books information in database as dictionary
    def initialize_books():
        f = open("books.txt", "r")
        bookinfoline = f.read().split("\n")
        for i in bookinfoline:
            j = i.split('-')
            key = j[0]
            value = eval(j[1])
            Books.allbooks[key] = value
        f.close()
    #To initialize total earn of your library till now
    @staticmethod
    def initialize_earn():
        with open("earn.txt",'r') as f:
            localearn=f.read()
            localearn=int(localearn)
            Books.totalearn=localearn
    #To initialize the history of already taken books from library.
    @staticmethod
    def initialize_books_track():
        f = open("bookstrack.txt", "r")
        Books.BooksTrack=[]
        for line in f:
            line = line.replace("\n", "")
            locallst1 = line.split("--")
            locallst1 = locallst1[1:]
            locallst1 = ast.literal_eval(locallst1[0:][0])
            locallst1.insert(0, len(Books.BooksTrack) + 1)
            Books.BooksTrack.append(locallst1)
        f.close()
    @staticmethod
    #To initialize the the already requested books by students
    def initialize_req_books():
        f = open("requestedbooks.txt", "r")
        Books.requestedbooks = []
        for line in f:
            line = line.replace("\n", "")
            line = ast.literal_eval(line)
            Books.requestedbooks.append(line)
        f.close()
    @abstractmethod
    #To display all the books
    def display_books(self):
        pass
class Admin(Books):#Feature no:2.Inheritance
    def display_books(self):#Implementing in the abstract method as it inherits the Books (abstract class) OOP Feature no:3.Method Overriding
        displaybooks = []
        Books.initialize_books()
        print("\033[1m *******ALL BOOKS AVAILABLE******* \033[0m")
        for k, val in Books.allbooks.items():
            locallist = list(val)
            locallist.insert(0, len(displaybooks) + 1)
            displaybooks.append(locallist)
        print(tabulate(displaybooks, headers=['S.no', 'Book name', 'Author name', 'Edition', 'Type', 'Rate per day'],
                       tablefmt='pretty'))
    @staticmethod
    #To show all the students involved in library
    def show_all_students():
        allstudents = []
        with open("students.txt", "r") as f:
            for line in f:
                line = line.replace("\n", "")
                locallist4 = line.split(" ")
                allstudents.append(locallist4)
            f.close()
        print("\033[1m All Students Information \033[0m")
        print(tabulate(allstudents, headers=['Student Roll Number', 'Student Password'], tablefmt='pretty'))
    #To add new student in library by admin
    def add_new_student(self):
        student_add = True
        while student_add:
            Roll_no = input("Roll no(Format CS-XXXXX):")
            Password = input("Password:")
            studentcheck = {}
            add=True
            with open("students.txt","a+") as f:
                f.seek(0)
                for line in f:
                    (key, value) = line.split()
                    studentcheck[str(key)] = str(value)
                for k, val in studentcheck.items():
                    if k == Roll_no:
                        print("Two students with same roll number can not exist!")
                        add = False
                        student_add = False
                if add == True:
                    f.write(f"\n{Roll_no} {Password}")
                    f.close()
                    student_add = False

    # To add new book in the library
    def add_a_book(self):
        print("\033[1m ***********YOUR ARE NOW ADDING A BOOK********\033[0m")
        book_add = True
        while book_add:
            f = open("books.txt", "a+")
            books = {}
            bookeligible = True
            bookname = input("Enter the name of the book:")
            author = input("Enter the name Author of book:")
            edition = input("Enter the edition of book:")
            type = input("Enter the type of book:")
            rate = int(input("Enter the rate of book for one month:"))
            for l in Books.requestedbooks:
                if l[1]==bookname and l[2]==author and l[3]==edition:
                    print("You are now adding the requested book.")
                    Books.requestedbooks.remove(l)
                    break
            with open("requestedbooks.txt", "w") as file:
                for i in Books.requestedbooks:
                    file.write(f"{i}\n")

            Books.initialize_req_books()
            bookinfo = (bookname, author, edition, type, rate)
            f.seek(0)
            fileline = f.read().split("\n")
            for i in fileline:
                j = i.split('-')
                key = j[0]
                value = j[1]
                books[key] = value
            Books.initialize_req_books()
            for k in books:
                val = eval(books[k])
                if val[0] == bookname and val[1] == author and val[2] == edition:
                    print("Book exist already!")
                    bookeligible = False
            if bookeligible == True:
                f.write(f"\n{len(books) + 1}-{bookinfo}")
                book_add = False
            Books.initialize_books()
            f.close()

    #Tracking the books that which student lend the book
    @staticmethod
    def Books_Track():
        Books.initialize_books_track()
        if len(Books.BooksTrack)>0:
            print("\033[1m ******ALL BOOKS RECORD*****\033[0m")
            print(tabulate(Books.BooksTrack, headers=['S.no', 'Roll no', 'Book name', 'Author name', 'Edition', 'Type',
                                                  'Rate per day(Rs)', 'Lend Date', 'No. of Months',
                                                  'Total Amount Due(Rs)'], tablefmt='pretty'))
        if len(Books.BooksTrack)==0:
            print("\033[1m Nothing to show here! \033[0m")

    # To show all the requested book by the students which is not in library
    @staticmethod
    def show_req_books():
        Books.initialize_req_books()
        if len(Books.requestedbooks) > 0:
            print(tabulate(Books.requestedbooks, headers=['S.no', 'Book name', 'Author name', 'Edition'],tablefmt='pretty'))
        else:
            print("\033[1m Nothing to show here! \033[0m")
class Student(Books):#oop Feature -inheritance
    def __init__(self,Rollno):
        self.Rollno=Rollno
        self.mybooks=[]
    def display_books(self):#Implementing in the abstract method as it inherits the Books (abstract class) OOP Feature no:3.Method Overriding
        displaybooks=[]
        Books.initialize_books()
        print("\033[1m *******ALL BOOKS AVAILABLE******* \033[0m")
        for k,val in Books.allbooks.items():
            locallist=list(val)
            locallist.insert(0,len(displaybooks)+1)
            displaybooks.append(locallist)
        print(tabulate(displaybooks, headers=['S.no', 'Book name', 'Author name', 'Edition', 'Type', 'Rate per day'], tablefmt='pretty'))
    #Student is lending a book from the library.
    def lend_a_book(self):
        amount=0
        toddate=date.today()
        Student.display_books(self)
        while True:               #Exception for Valueerror
            try:
                seq=input("Enter the sequence number of book to be configured:")
                seq=int(seq)
                break
            except ValueError:
                print("The sequence number must be an integer. Enter again...!!")
        time=int(input("For how many months you want to the book?:"))
        for key,value in Books.allbooks.items():
            if int(key)==seq:
                locallst2=[]
                amount+=value[-1]*time
                value=list(value)
                value.insert(0,len(self.mybooks)+1)
                value.insert(1,self.Rollno)
                value.append(toddate.strftime("%B %d, %Y"))
                value.append(time)
                value.append(amount)
                locallst2.append(value)
                f=open("bookstrack.txt","a+")
                for i in locallst2:
                    f.write(f"{len(Books.BooksTrack)+1}--{i[1:]}\n")
                f.close()
                Books.initialize_books_track()
    #To show the separate record of lend books for a single student.
    def myrecord(self):
        self.mybooks=[]
        f = open("bookstrack.txt", "r")
        for line in f:
            line = line.replace("\n", "")
            locallst1 = line.split("--")
            locallst1 = locallst1[1:]
            locallst1 = ast.literal_eval(locallst1[0:][0])
            if locallst1[0] == self.Rollno:
                locallst1.insert(0,len(self.mybooks)+1)
                self.mybooks.append(locallst1)
        print("\033[1m ******YOUR RECORD*****\033[0m")
        print(tabulate(self.mybooks,headers=['S.no', 'Roll no', 'Book name', 'Author name', 'Edition', 'Type', 'Rate per day(Rs)','Lend Date', 'No. of Months', 'Total Amount Due(Rs)'], tablefmt='pretty'))
        if len(self.mybooks)==0:
            print(f"Dear {self.Rollno} You have no record here!")
    #Method so that Student can request a book which is not in library
    def request_book(self):
        reqbookavailable=False
        print("\033[1m ***********YOUR ARE NOW REQUESTING A BOOK********\033[0m")
        reqbookname = input("Enter the name of the book:")
        reqauthor = input("Enter the name Author of book:")
        reqedition = input("Enter the edition of book:")
        reqbookinfo = [len(Books.requestedbooks)+1,reqbookname, reqauthor, reqedition]
        with open("books.txt", 'r') as file:
            for line in file:
                line = line.split("-")
                line = line[1].replace("\n", "")
                line = eval(line)
                line = list(line)
                if line[0]==reqbookname and line[1]==reqauthor and line[2]==reqedition:
                    reqbookavailable=True
                    break
        Books.initialize_req_books()
        for i in Books.requestedbooks: #if the requesting book is already in the requested quenue
            if i[1]==reqbookname and i[2]==reqauthor and i[3]==reqedition:
                reqbookavailable=True
                break
        if reqbookavailable==False: #if the requesting book is already in the library
            with open("requestedbooks.txt","a+") as f:
                f.write(f"{reqbookinfo}\n")
            Books.initialize_req_books()
            print("\033[1m ***BOOK SUCCESSFULLY REQUESTED*** \033[0m")
        if reqbookavailable==True:
            print("\033[1m The book requested is already available in the library Please see all the available books in the library and if it is not in the library then it is already requested by someone please wait for some days the book will be added in the library soon! \033[0m")
    #Student returns the book in library and to update his record to remove the returned book
    def return_book(self):
        self.myrecord()
        if len(self.mybooks)>0:
            while True:          #Exception for value erro
                try:
                    seq = input("Enter the sequence number of book to be configured:")
                    seq = int(seq)
                    break
                except ValueError:
                    print("The sequence number must be an integer. Enter again...!!")
            for i in self.mybooks:
                 if i[0]==seq:
                    print(f"The amount due is \033[1m {i[-1]} Rupees \033[0m ")
                    while True:         #Exception for value erro
                        try:
                            pay=input(f"Enter the amount you want to pay {self.Rollno} Rs:")
                            pay = int(pay)
                            break
                        except ValueError:
                            print("The payment must be an integer. Enter again...!!")
                    if pay==i[-1]:
                        Books.initialize_books_track()
                        for j in Books.BooksTrack:
                             if i[1]==j[1] and i[2]==j[2] and i[3]==j[3] and i[4]==j[4]:
                                 numbering=1
                                 Books.BooksTrack.remove(j)
                                 Books.initialize_earn()
                                 Books.totalearn+=j[-1]
                                 with open ("earn.txt","w") as d:
                                     d.write(f"{Books.totalearn}")
                                 print(f"\033[1m {j[-1]} Rupees received!\033[0m ")
                                 break
                        with open ("bookstrack.txt","w") as f:
                            for k in range(0,len(Books.BooksTrack)):
                                f.write(f"{numbering}--{Books.BooksTrack[k][1:]}\n")
                                numbering+=1
                            Books.initialize_books_track()
                            print(f"\033[1m Dear {self.Rollno} Your Record Has been Updated! \033[0m")
                            self.mybooks = []
                            #Books.totalearn+=
                            f = open("bookstrack.txt", "r")
                            for line in f:
                                line = line.replace("\n", "")
                                locallst1 = line.split("--")
                                locallst1 = locallst1[1:]
                                locallst1 = ast.literal_eval(locallst1[0:][0])
                                if locallst1[0] == self.Rollno:
                                    locallst1.insert(0, len(self.mybooks) + 1)
                                    self.mybooks.append(locallst1)
                    elif pay<i[-1]:
                        print("\033[1m Not Sufficient Amount of money entered to remove the book from your record! \033[0m")
                    elif pay>i[-1]:
                        print("\033[1m You have accidentally entered the greater amount! \033[0m")
                 elif seq>len(self.mybooks)+1:
                     print("You have accidentally typed the wrong sequence numbers.")
        else:
            print("Nothing to show here!")

# Class owner :Owner can access all things
class Owner(Admin):# Multi Level inheritance Book → Admin → Owner
    def display_books(self):#Implementing in the abstract method as it inherits the Books (abstract class) OOP Feature no:3.Method Overriding
        displaybooks=[]
        Books.initialize_books()
        print("Welcome Owner!")
        print("\033[1m *******ALL BOOKS AVAILABLE******* \033[0m")
        for k,val in Books.allbooks.items():
            locallist=list(val)
            locallist.insert(0,len(displaybooks)+1)
            displaybooks.append(locallist)
        print(tabulate(displaybooks, headers=['S.no', 'Book name', 'Author name', 'Edition', 'Type', 'Rate per day'], tablefmt='pretty'))
    #Owner can see the total earn by the library
    @staticmethod
    def see_totalearn():
        print(f"Total earn of your library is \033[1m Rupees {Books.totalearn}\033[0m ")
    #Owner can add a new admin
    def make_new_admin(self):
        admin_add = True
        while admin_add:
            Username = input("Username:")
            Password = input("Password:")
            admincheck = {}
            add = True
            with open("admins.txt", "a+") as f:
                f.seek(0)
                for line in f:
                    (key, value) = line.split()
                    admincheck[str(key)] = str(value)
                for k, val in admincheck.items():
                    if k == Username:
                        print("Username exist!")
                        add = False
                if add == True:
                    f.write(f"\n{Username} {Password}")
                    f.close()
                    admin_add = False
    #Owner can see all the admin information
    def show_all_admins(self):
        alladmins=[]
        with open("admins.txt", "r") as f:
            for line in f:
                line=line.replace("\n","")
                locallist4=line.split(" ")
                alladmins.append(locallist4)
            f.close()
        print("\033[1m All Admins Information \033[0m")
        print(tabulate(alladmins, headers=['Admin Username', 'Admin Password'], tablefmt='pretty'))
    #Owner can delete any admin
    def del_an_admin(self):
        Owner.show_all_admins(self)
        Username_del=input("Enter the Username you want to delete:")
        alladmins = []
        admin_del_success = False
        with open("admins.txt", "a+") as f:
            f.seek(0)
            for line in f:
                lst= line.split(" ")
                alladmins.append(lst)
            f.close()
        for k in alladmins:
            if k[0]==Username_del:
                alladmins.remove(k)
                admin_del_success=True
                break
        if admin_del_success==False:
            print(f"There exist no such Username {Username_del}!")
        if admin_del_success==True:
            with open("admins.txt","w") as f:
                for i in alladmins:
                    f.write(f"{i[0]} {i[1]}")

#For logging in in the system
def initialize():
    global admins
    global owner
    global students
    admins={}
    owner={}
    students={}
    with open("admins.txt","a+") as f:
        f.seek(0)
        for line in f:
            (key, value) = line.split()
            admins[str(key)]=str(value)
    with open("owner.txt","a+") as f:
        f.seek(0)
        for line in f:
            (key, value) = line.split()
            owner[str(key)]=str(value)
    with open("students.txt","a+") as f:
        f.seek(0)
        for line in f:
            (key, value) = line.split()
            students[str(key)]=str(value)
def library():
    initialize()
    print("**Welcome to the CIS Library**")
    open_library=True
    while open_library:
        category=input("Please specify your identity \nPress 1 for Owner\nPress 2 for Admin\nPress 3 for Student \nPress 4 to close the library.\nType:")
        if category=="1":
            stay_owner_menu = True
            while stay_owner_menu:
                print("Log in")
                Ownername = input("Ownername:")
                Password = input("Password:")
                owner_names = []
                owner_passwords = []
                for i, j in owner.items():
                    owner_names.append(i)
                    owner_passwords.append(j)
                if Ownername in owner_names and Password in owner_passwords:
                    if owner_names.index(Ownername) == owner_passwords.index(Password):
                        personowner=Owner()
                        print("\033[1m Logged in successfully!\033[0m")
                        print(f"\033[1m Welcome {Ownername}!\033[0m")
                        login_stay = True
                        while login_stay:
                            owner_choice = input("If you want to log out press L.\n1.Make a new admin.\n2.All Students Track.\n3.Display all Books.\n4.Display Requested Books.\n5.See Earn Progress.\n6.All admins list.\n7.Delete an Admin.\n8.Students Information.\nEnter:").upper()
                            if owner_choice=="1":
                                personowner.make_new_admin()
                                initialize()
                            elif owner_choice=="2":
                                personowner.Books_Track()
                            elif owner_choice=="3":
                                personowner.display_books()
                            elif owner_choice=="4":
                                personowner.show_req_books()
                            elif owner_choice=="5":
                                personowner.initialize_earn()
                                personowner.see_totalearn()
                            elif owner_choice=="6":
                                personowner.show_all_admins()
                            elif owner_choice=="7":
                                personowner.del_an_admin()
                                initialize()
                            elif owner_choice == "8":
                                personowner.show_all_students()
                            elif owner_choice == "L":
                                print("Logging Out......\nLogged out successfully")
                                login_stay = False
                                stay_owner_menu = False
                            else:
                                print("Wrong Option Selected, Try Again")
                                login_stay = True
                    else:
                        print("Wrong Credentials.Try again.")
                else:
                    print("Wrong Credentials.Try again.")
        elif category=="2":
            stay_admin_menu=True
            while stay_admin_menu:
                print("Log in")
                Username=input("Username:")
                Password=input("Password:")
                all_usernames=[]
                all_passwords=[]
                for i,j in admins.items():
                    all_usernames.append(i)
                    all_passwords.append(j)
                if Username in all_usernames and Password in all_passwords:
                    if all_usernames.index(Username)== all_passwords.index(Password):
                        personadmin=Admin()
                        print("\033[1m Logged in successfully!\033[0m")
                        print(f"\033[1m Welcome {Username}!\033[0m")
                        login_stay=True
                        while login_stay:
                            admin_choice=input("If you want to log out press L.\n1.Add a student.\n2.Add a Book.\n3.All Students Track.\n4.Display all Books.\n5.Display Requested Books.\n6.All Students Information.\nEnter: ").upper()
                            if admin_choice=="1":
                                personadmin.add_new_student()
                                initialize()
                            elif admin_choice=="2":
                                personadmin.add_a_book()
                            elif admin_choice=="3":
                                personadmin.Books_Track()
                            elif admin_choice=="4":
                                personadmin.display_books()
                            elif admin_choice=="5":
                                personadmin.show_req_books()
                            elif admin_choice == "6":
                                personadmin.show_all_students()
                            elif admin_choice=="L":
                                print("Logging Out......\nLogged out successfully")
                                login_stay=False
                                stay_admin_menu=False
                            else:
                                print("Wrong Option Selected, Try Again")
                                login_stay = True
                    else:
                        print("Wrong Credentials.Try again.")
                else:
                    print("Wrong Credentials.Try again.")
        elif category=="3":
            stay_student_menu = True
            while stay_student_menu:
                print("Log in")
                Rollno= input("Enter Rollno:")
                Password= input("Password:")
                all_studentrollno = []
                all_passwords = []
                for i, j in students.items():
                    all_studentrollno.append(i)
                    all_passwords.append(j)
                if Rollno in all_studentrollno and Password in all_passwords:
                    if all_studentrollno.index(Rollno) == all_passwords.index(Password):
                        personstudent=Student(Rollno)
                        print("\033[1m Logged in successfully!\033[0m")
                        print(f"\033[1m Welcome {Rollno}!\033[0m")
                        login_stay = True
                        while login_stay:
                            student_choice =input("If you want to log out press L.\n1.Lend A book.\n2.Display all books.\n3.Request a book.\n4.Return a book.\n5.See your record.\nEnter: ").upper()
                            if student_choice=="1":
                                personstudent.lend_a_book()
                            elif student_choice=="2":
                                personstudent.display_books()
                            elif student_choice=="3":
                                personstudent.request_book()
                            elif student_choice=="4":
                                personstudent.return_book()
                            elif student_choice=="5":
                                personstudent.myrecord()
                            elif student_choice == "L":
                                print("Logging Out......\nLogged out successfully")
                                login_stay = False
                                stay_student_menu = False
                            else:
                                print("Wrong Option Selected, Try Again")
                                login_stay = True
                    else:
                        print("Wrong Credentials.Try again.")

                else:
                    print("Wrong Credentials.Try again.")
        elif category == "4":
            print("Have a great day Bye!")
            open_library=False

library()













