from tkinter import *
root = Tk()
root.geometry("655x333")
root.title("Register yourself to join our Dance academy")


def getvals():
    print(f"You have enter your first name as : {fnamevalue.get()}")
    print(f"You have enter middle name as : {mnamevalue.get()}")
    print(f"You have enter last name as : {lnamevalue.get()}")
    print(f"You have enter Dob as :{Dobvalue.get()}")
    print(f"You have enter email as : {emailvalue.get()}")
    print(f"You have enter password as : {passwordvalue.get()}")

    file = open("user.txt","a")
    file.write("Your first name : " + fnamevalue.get())
    file.write("\n")
    file.write("Your middle name : " + mnamevalue.get())
    file.write("\n")
    file.write("Your last name : " + lnamevalue.get())
    file.write("\n")
    file.write("Your date of birth : " + (Dobvalue.get()))
    file.write("\n")
    file.write("Your email id : " + emailvalue.get())
    file.write("\n")
    file.write("Your password : " + passwordvalue.get())
    file.close()

fname = Label(root,text="First name")
mname = Label(root,text="Middle name")
lname = Label(root,text="Last name")
Dob = Label(root,text="Date of birth")
email = Label(root,text="Email id")
password = Label(root,text="Create a password")

fname.grid()
mname.grid()
lname.grid()
Dob.grid()
email.grid()
password.grid()

fnamevalue = StringVar()
mnamevalue = StringVar()
lnamevalue = StringVar()
Dobvalue = StringVar()
emailvalue = StringVar()
passwordvalue = StringVar()


fnameentry = Entry(root,textvariable = fnamevalue)
mnameentry = Entry(root,textvariable = mnamevalue)
lnameentry = Entry(root,textvariable = lnamevalue)
Dobentry = Entry(root,textvariable = Dobvalue)
emailentry = Entry(root,textvariable = emailvalue)
passwordentry = Entry(root,textvariable = passwordvalue)

fnameentry.grid(row=0,column=1)
mnameentry.grid(row=1,column=1)
lnameentry.grid(row=2,column=1)
Dobentry.grid(row=3,column=1)
emailentry.grid(row=4,column=1)
passwordentry.grid(row=5,column=1)

# making button
Button(text = "submit",command = getvals).grid()

# # creating a file to store data
# f = open("Register_details.txt"."a") as f:



root.mainloop()