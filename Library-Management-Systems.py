from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox


class Library:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management Systems")
        self.root.geometry("1490x850+0+0")
        self.root.configure(background="gray")

        MType= StringVar()
        Ref= StringVar()
        Title= StringVar()
        Firstname= StringVar()
        Surname= StringVar()
        Address1= StringVar()
        Address2= StringVar()
        PostCode= StringVar()
        MobileNo= StringVar()
        BookID= StringVar()
        BookTitle =StringVar()
        BookType= StringVar()
        Author= StringVar()
        DateBorrowed= StringVar()
        DateDue= StringVar()
        SellingPrice= StringVar()
        LateReturnFine= StringVar()
        DateOverDue= StringVar()
        DaysOnLoan= StringVar()
        Prescription= StringVar()

        def Exit():
            exit= tkinter.messagebox.askyesno("Library Management System", "Confirm if you want to Exit")

            if exit>0:
                root.destroy()
            else:
                return

        def Reset():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            PostCode.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            # self.txtFrameDetail.delete("1.0",END)
            self.txtDisplayR.delete("1.0", END)

        def Delete():
            Reset()
            self.txtDisplayR.delete("1.0",END)



        # ==================================================WIDGETS==================================================
        MainFrame = Frame(root)
        MainFrame.grid()

        # Title Frame
        TitleFrame = Frame(MainFrame, width=1920, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=39, font=('arial', 40, 'bold'), text="\t Library Management System \t",
                              padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1900, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, width=1030, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Library Membership Info:", )
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=10, width=1025, height=300, padx=20, relief=RIDGE,
                                    font=('arial', 12, 'bold'), text="Book Details:", )
        DataFrameRight.pack(side=RIGHT)

        # ==================================================WIDGETS==================================================
        self.lblMemberType = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Member Type:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)
        self.cboMemberType = ttk.Combobox(DataFrameLeft, font=('arial', 12, 'bold'), state='readonly', width=23, textvariable=MType)
        self.cboMemberType['value'] = ('', 'Student', 'Lecturer', 'Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblBookID = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Book ID:", padx=2, pady=2)
        self.lblBookID.grid(row=0, column=2, sticky=W)
        self.lblBookID = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=BookID)
        self.lblBookID.grid(row=0, column=3)

        self.lblRef = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Reference Number:", padx=2, pady=2)
        self.lblRef.grid(row=2, column=0, sticky=W)
        self.lblRef = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Ref)
        self.lblRef.grid(row=2, column=1)

        self.lblBookTitle = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Book Title:", padx=2, pady=2)
        self.lblBookTitle.grid(row=2, column=2, sticky=W)
        self.lblBookTitle = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=BookTitle)
        self.lblBookTitle.grid(row=2, column=3)
        self.lblTitle = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2)
        self.lblTitle.grid(row=3, column=0, sticky=W)

        self.cboTitle = ttk.Combobox(DataFrameLeft, font=('arial', 12, 'bold'), state='readonly', width=23, textvariable=Title)
        self.cboTitle['value'] = ('', 'Mr.', 'Mrs.', 'Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=3, column=1)

        self.lblAuthor = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Author:", padx=2, pady=2)
        self.lblAuthor.grid(row=3, column=2, sticky=W)
        self.lblAuthor = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Author)
        self.lblAuthor.grid(row=3, column=3)

        self.lblFirstname = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Firstname:", padx=2, pady=2)
        self.lblFirstname.grid(row=4, column=0, sticky=W)
        self.lblFirstname = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Firstname)
        self.lblFirstname.grid(row=4, column=1)

        self.lblDateBorrowed = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Date Borrowed:", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=4, column=2, sticky=W)
        self.lblDateBorrowed = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=DateBorrowed)
        self.lblDateBorrowed.grid(row=4, column=3)

        self.lblSurname = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Surname:", padx=2, pady=2)
        self.lblSurname.grid(row=5, column=0, sticky=W)
        self.lblSurname = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Surname)
        self.lblSurname.grid(row=5, column=1)

        self.lblDateDue = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Date Due:", padx=2, pady=2)
        self.lblDateDue.grid(row=5, column=2, sticky=W)
        self.lblDateDue = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=DateDue)
        self.lblDateDue.grid(row=5, column=3)

        self.lblAddress1 = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Address 1:", padx=2, pady=2)
        self.lblAddress1.grid(row=6, column=0, sticky=W)
        self.lblAddress1 = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Address1)
        self.lblAddress1.grid(row=6, column=1)

        self.lblDaysOnLoan = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Days On Loan:", padx=2, pady=2)
        self.lblDaysOnLoan.grid(row=6, column=2, sticky=W)
        self.lblDaysOnLoan = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=DaysOnLoan)
        self.lblDaysOnLoan.grid(row=6, column=3)

        self.lbladdress2 = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Address 2:", padx=2, pady=2)
        self.lbladdress2.grid(row=7, column=0, sticky=W)
        self.lbladdress2 = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Address2)
        self.lbladdress2.grid(row=7, column=1)

        self.lblLateReturnFine = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Days On Loan:", padx=2, pady=2)
        self.lblLateReturnFine.grid(row=7, column=2, sticky=W)
        self.lblLateReturnFine = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=LateReturnFine)
        self.lblLateReturnFine.grid(row=7, column=3)

        self.lblPostCode = Label(DataFrameLeft,font=('arial', 12, 'bold'), text="Post Code:", padx=2, pady=2)
        self.lblPostCode.grid(row=8, column=0, sticky=W)
        self.lblPostCode = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=PostCode)
        self.lblPostCode.grid(row=8, column=1)

        self.lblDateOverDue = Label(DataFrameLeft,font=('arial', 12, 'bold'), text="Date Over Due:", padx=2, pady=2)
        self.lblDateOverDue.grid(row=8, column=2, sticky=W)
        self.lblDateOverDue = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=DateOverDue)
        self.lblDateOverDue.grid(row=8, column=3)

        self.lblMobileNo = Label(DataFrameLeft,font=('arial', 12, 'bold'), text="Mobile No.:", padx=2, pady=2)
        self.lblMobileNo.grid(row=9, column=0, sticky=W)
        self.lblMobileNo = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=MobileNo)
        self.lblMobileNo.grid(row=9, column=1)

        self.lblSellingPrice = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Selling Price:", padx=2, pady=2)
        self.lblSellingPrice.grid(row=9, column=2, sticky=W)
        self.lblSellingPrice = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=SellingPrice)
        self.lblSellingPrice.grid(row=9, column=3)

        # ==================================================WIDGET==================================================

        self.txtDisplayR=Text(DataFrameRight, font=('arial', 12, 'bold'), width=32, height=13, padx=8, pady=20)
        self.txtDisplayR.grid(row=0, column=2)

        # ==================================================List Box=================================================

        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=1, sticky= "ns")

        ListOfBooks = ['Cinderella', 'Jane Eyre', 'The Stranger', 'Oliver Twist', 'Rebecca', 'Pride and Prejudice', 'To Kill a Mockingbird', 'The Great Gatsby', 'In Cold Blood', 'The Call of the Wild', 'Persuasion']
        bookList = Listbox(DataFrameRight, font=('arial', 12, 'bold'))
        bookList.bind("<<ListboxSelect>>")
        bookList.grid(row=0,  column=0, padx=8)
        scrollbar.config(command=bookList.yview())

        for items in ListOfBooks:
            bookList.insert(END, items)

        # ==================================================DETAILS==================================================

        self.lblLabel = Label(FrameDetail, font=('arial', 12, 'bold'), pady=8, text="Member Type\tReference No,\tTitle\tFirst Name\tSurname\tAddress 1\t Address 2\t Post Code\tBook Title\tDate Borrowed\tDays on Loan")
        self.lblLabel.grid(row=0,column=0)

        self.txtDisplayR = Text(FrameDetail, font=('arial', 12, 'bold'), width=141, height=4, padx=2, pady=4)
        self.txtDisplayR.grid(row=1, column=0)



        # ==================================================BUTTONS==================================================

        self.btnDisplayData = Button(ButtonFrame, text="DISPLAY DATA", font=('arial', 12, 'bold'), width=30, bd=4)
        self.btnDisplayData.grid(row=0, column=0)

        self.btnDelete = Button(ButtonFrame, text="DELETE", font=('arial', 12, 'bold'), width=30, bd=4, command=Delete)
        self.btnDelete.grid(row=0, column=1)

        self.btnReset = Button(ButtonFrame, text="RESET", font=('arial', 12, 'bold'), width=30, bd=4, command=Reset)
        self.btnReset.grid(row=0, column=2)

        self.btnExit = Button(ButtonFrame, text="EXIT", font=('arial', 12, 'bold'), width=30, bd=4, command=Exit)
        self.btnExit.grid(row=0, column=3)


if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
