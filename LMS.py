from calendar import c
import datetime
from importlib.util import set_loader
import os
from random import choice
import re
class LMS:
    """this class is used to keep records of books library.
    there are four modules: display_books,issue_books,add_books,return_books"""
    def __init__(self,list_of_books,library_name):
        self.list_of_books=r"C:\Users\ROHIT\Desktop\python projects\lms"
        self.library_name=library_name
        self.books_dict={}
        id=101
        """reading books name from txt file"""
        with open(self.list_of_books) as f:
            content=f.readlines()
        for line in content:
            self.books_dict.update({str(id):{"books_title":line.replace("\n",""),"lender_name":"","issue_date":"","status":"Available"}})
            id=id+1


    """module first add books"""
    def add_books(self):
        new_book=input("enter book title:\n")
        if new_book=="":
            return self.add_books()
        else:
            with open(self.list_of_books,'a') as f:
                f.writelines(f"{new_book}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{"books_title":new_book,"lender_name":"","issue_date":"","status":"Available"}})
                print(f"{new_book}book added successfully!!!!")

    """module second issue book """
    def issue_books(self):
        book_id=input("enter book_id:\n")
        current_date=datetime.date.today()
        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]["status"]=="Available":
                print(f"This book is already issued to {self.books_dict[book_id]['lender_name']} on {self.books_dict[book_id]['issue_date']}")
                return self.issue_books()
            elif self.books_dict[book_id]["status"]=="Available":
                your_name=input("enter your name:\n")
                self.books_dict[book_id]['lender_name']=your_name
                self.books_dict[book_id]['status']="already issued"
                self.books_dict[book_id]['issued_date']=current_date
                print("book issueded successfully!!..")
        else:
            print("book_id is wrong")
            self.issue_books()


    """module three return book"""
    def return_books(self):
        book_id=input("enter book id")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["status"]=="Available":
                print("This book id is already available in library.please check your book id")
            else:
                self.books_dict[book_id]["lender_name"]=""     
                self.books_dict[book_id]["status"]="Available"   
                self.books_dict[book_id]["issue_date"]=""                
                print("Successfully updated!!")
           
        else:
            print("book id is wrong\n")



    """module four display name of books"""
    def display_books(self):
        print("---------------------------------------------------------------------------------------")
        print("book id","\ttitle","\t\tstatus")
        print("---------------------------------------------------------------------------------------")

        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"\t\t",value.get("status"))



"""""main function start"""
l=LMS(r"C:\Users\ROHIT\Desktop\python projects\lms","python")

# for authentication we can use username=user and password=12345
user=input("enter the username:\n")
password=input("enter the password:\n")

if user=="user" and password=="12345":
    print("login successfully!!!")

    print("------------------------------------------------------------------------")
    print("                      Library Management System                         ")
    print("------------------------------------------------------------------------")
while True:
    print("1.Add Book\n")
    print("2.Issue Book\n")
    print("3.Return Book\n")
    print("4.Display Book\n")
    choice=int(input("enter your choice:\n"))

    if choice==1:
        l.add_books()
        
    elif choice==2:
        l.issue_books()
        
    elif choice==3:
        l.return_books()
        
    else :
        l.display_books()



else:
    print("login failed!!!")



