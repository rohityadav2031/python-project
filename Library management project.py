# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:28:56 2022

@author: ASUS
"""



root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500") 








from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *

mypass="root"
mydatabase="mydb"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

#enter table names here
bookTable = "books"

# create database mydb;      

# use mydb;
                                                
create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30)); 

create table books_issued(bid varchar(20) primary key, issueto varchar(30));


#Add the background Image
same = True
n = 0.28

background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
#set the new image width and height
newImageSizeWidth = int(imageSizeWidth * n)

if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)

#add an image to canva
img = ImageTk.PhotoImage(background_image)
canvas1 = Canvas(root)
canvas1.create_image(300, 340, image=img)
canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
canvas1.pack(expand=True, fill=BOTH)

#Add the buttons
btn1 = Button(root, text="Add Book Details", bg="black", fg="white", command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg="black", fg="white", command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View book list", bg="black", fg="white", command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book", bg="black", fg="white", command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg="black", fg="white", command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop() #call the mainloop to run the application

# function register book
def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into "+bookTable+" values ('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo('Error', "Can't add book to database")

    print(bid)
    print(title)
    print(author)
    print(status)

    root.destroy()
    
def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, cur, con, bookTable, root
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass="root"
    mydatabase = "mydb"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    #enter the table name here
    bookTable = "books" #book table

    #create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #book ID
    lb1 = Label(LabelFrame, text="Book Id: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for book Id
    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    #title
    lb2 = Label(LabelFrame, text="Title: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    #entry for title
    bookInfo2 = Entry(LabelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #author
    lb3 = Label(LabelFrame, text="Author: ", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    #entry for author
    bookInfo3 = Entry(LabelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    #Status
    lb4 = Label(LabelFrame, text="Status: ", bg="black", fg="white")
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
    #entry for status
    bookInfo4 = Entry(LabelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg="#d1ccc0", fg="black", command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit button
    QuitBtn = Button(root, text="Quit", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def View():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Books", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%10s %40s %30s %20s"%('BID','Title','Author','Status'),
                    bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    #addLine
    addline = Label(LabelFrame, text = "----------------------------------------------------------------------------",bg="black", fg="white")
    addline.place(relx=0.05, rely=0.2)
    
    y = 0.25 #declare var to increase the height at y-axis to print details
    #query to retrieve details from books table
    getBooks = "select * from "+ bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(LabelFrame, text="%10s %40s %30s %20s"%(i[0],i[1],i[2],i[3]),
                    bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1
            
    except:
        messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(root, text="QUIT", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
    
    
def deleteBook():
    bid = bookInfo1.get()

    deleteSql = "delete from "+ bookTable+ "where bid = '" +bid+"'"
    deleteIssue = "delete from "+issue_Table+ " where bid = '" +bid+"' "

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo("Success", "Book Deleted Successfully")

    except:
        messagebox.showinfo("Error", "Please check Book Id")

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()

def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, bookTable, cur, con, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="lightgreen")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Delete Book", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #take a book ID to delete
    lb2 = Label(LabelFrame, text="Book Id: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Submit", bg="lightblue", fg="black", command=deleteBook)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def issue():
    global issuebtn, labelFrame, inf1, inf2, lb1, quitBtn, root, Canvas1, status
    bid = inf1.get()        #take the book id with get()
    issueto = inf2.get()    #take the name to whom it is issued

    issuebtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    extractBid = "select bid from "+ bookTable
    try:
        cur.execute(extractBid)
        con.commit()

        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
            if check == 'available':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book Id not present")
    except:
        messagebox.showinfo("Error", "Can't fetch the Book Id")

    issueSql = "insert into "+issueTable+" values ('"+bid+"', '"+issueto+"')"
    show = "select * from "+issueTable
    updateStatus = "update "+ bookTable+" set status = 'issued' where bid = '"+bid+"'"

    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo("Success", "Book Issued successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo("Message", "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value insert is wrong, Try again")
    print(bid)
    print(issueto)
    allBid.clear()
    
def issueBook():
    global issuebtn, labelFrame, inf1, inf2, lb1, quitBtn, root, Canvas1, status

    root=Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="yellow")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel1 = Label(headingFrame1, text="Issue Book", bg="black", fg="white", font=('Courier',15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #Book Id
    lb1 = Label(labelFrame, text="Book Id", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    #to whom book is issued, student name
    lb2 = Label(labelFrame, text="Issue To", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    #Issue Button
    issuebtn = Button(root, text="Issue", bg="#d1ccc0", fg="black", command=issue)
    issuebtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="#aaa69d", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
    
    
def Return():
    global submitBtn, quitBtn, LabelFrame, lb1, Canvas1, bookInfo1, root, status

    bid = bookInfo1.get()
    extractBid = "select bid from "+issueTable

    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False
        
        else:
            messagebox.showinfo("Error", "Book Id is not Present")

    except:
        messagebox.showinfo("Error", "Can't Fetch the book Id")

    #remove that book from issueTable
    issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"

    print(bid in allBid)
    print(status)
    updateStatus = "update "+bookTable+" set status = 'available' where bid='"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(updateStatus)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book returned successfully")

        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book id")
            root.destroy()
            return

    except:
        messagebox.showinfo("Search Error", "the valur youentered is wrong, try again!")

    allBid.clear()
    root.destroy()
    
def returnBook():
    global root, con, cur, labelFrame, submitBtn, quitBtn, Canvas1, bookInfo1, lb1

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="pink")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg="black", fg="white", font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #book id
    lb1 = Label(labelFrame, text="Book Id", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit Button
    submitBtn = Button(root, text="Submit", bg="lightblue", fg="black", command=Return)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
    
#end 