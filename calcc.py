from tkinter import *
from tkcalendar import Calendar


# Graphical User Interface for a calculater
def mycal():
    root = Tk()

    root.geometry("300x300")

    cal = Calendar(root, Selectmode='day', year=2021, month=11, day=24)

    cal.pack(pady=20)

    def printdate():
        date.config(text="Selected Date is: " + cal.get_date())
        return cal.get_date()

    Button(root, text="Click here to save then close the calendar window.", command=printdate).pack(pady=20)

    date = Label(root, text="")
    date.pack(pady=20)
    # return(cal.get_date())
    # print(printdate())
    # return(printdate())
    root.mainloop()

    return cal.get_date()

# mycal()
# thedate = cal.get_date()
# print(thedate)