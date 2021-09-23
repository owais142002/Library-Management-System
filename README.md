# Library-Management-System
Library Management system built on Python with command line interface,
See the 
PROJECT INFO:
consistS of three classes mainly i.e. Owner, Admin, Students.
Basic Assumptions:
⦁	Book added is infinite and cannot decrease if lend by any student.
⦁	Book added once cannot be deleted.
⦁	There is no salary for admins.
⦁	There is only one owner of this system i.e.(Name: MissMaria ,Pass: oop)
⦁	Student can only return the lent book if he gives the exact amount of money required.
⦁	A student have to make his account in the system by admin and his account can vacate if he returns all the books he lent but his account cannot be deleted ever.
⦁	Only Admin can add a book.
⦁	Owner can delete any admin.
⦁	Only Owner can see the financial state of library.
⦁	Distinguishing features of your project:
The main features of the program are:
⦁	All the data is always saved like a database and cannot be lost whether the program is exited or started.
⦁	I used a unique library to show all the information making the Command line program like GUI.
⦁	A Student can request for a book incase a book is not available in library.
⦁	It includes inheritance, Association, Exception handling, Method overloading and abstract class(book).
⦁	If a book being added is the requested book by students, then that book will be deleted from the requested books.
⦁	If the requested book is already requested by someone then it will give a proper message that it is already requested by someone and book info will not go into the requested books queue.
⦁	Also if the requested book is in the library already then it will print a proper message that it is available in the library and won’t go to the requested book queue again.


⦁	Flow of your project:

The program consists of 4 classes  i.e. class Books, class Owner, class Admin and class Students.
As soon as the program starts it will ask you for your identity whether Owner, Admin or Student and to close the library. If you opt for owner you will be given choices for 8 different options and can access each of them i.e. you can make a new admin, You can see all the students lending books track, you can see all the books of library, you can see all the books requested by students to include in library, you can see the financial progress of the library, you can see all the information of admins, you can delete any admin and can also see all the information of students. If you opt for admin then you will be given 6 different options i.e. you can add a student, you can add a book, you can see all the students lending book track, you can see all the books available in the library, you can see the requested books by the students that is not available and can see the information of all the students. If you opt for student then you will be given 5 choices i.e. to lend a book  from library, to see all the books in library, to request  a book if it is not available in the library, you can return a lent book and can see your record of lent books. If you opt to close the library it will close  the library and the data remains saved and unchanged.
Also at the start of program function initialize() will reload the database from text files for the credentials of Owners, Admins and Students.

NOTE:Dont try to edit or remove spaces from the txt files or the program will crash.
