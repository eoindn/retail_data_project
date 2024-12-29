from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk




def the_tax_window():
    tax_window = Toplevel()
    tax_window.geometry('400x400')
    tax_window.config(background="#d3d3d3")
    tax_window.title("Tax Calculator")


    for i in range(2):
        tax_window.rowconfigure(i, weight=3)
    #
    #
    for i in range(2):
        tax_window.columnconfigure(i, weight=3)
    #

    tax_logo = Image.open('tax-2.png')
    tax_test = ImageTk.PhotoImage(tax_logo)
    tax_label = Label(tax_window, image = tax_test,bg = "#d3d3d3")
    tax_label.image = tax_test
    tax_label.place(x=82, y=180)

    entry_label = Label(tax_window, text = "Enter your country ", font = ("Arial","13","bold"), background="#d3d3d3", fg='black')
    entry_label.place(x = 145, y = 100)






    def tax_income_func():

        tax_message = Label(tax_window, text = f"The Tax Bracket of {country_entry.get()} is 45%",
                            bg = "#d3d3d3", fg = "black" )
        tax_message.place(x = 100, y = 200)


        country_entry.destroy()
        entry_label.destroy()

        rev_label = Label(tax_window, text = "Enter Your Revenue", font = ("Arial","13","bold"), background = "#d3d3d3", fg = "black")
        rev_label.place(x = 145, y = 100)

        revenue_entry = Entry(tax_window, width=20, background='#ffffff', fg='black')
        revenue_entry.place(x=110, y=150)


        def calculate_tax():
            try:
                income = float(revenue_entry.get())
                income_after_tax = income * 0.65
                income_after_tax_label = messagebox.showinfo("Tax Calculated!",f"Your income after tax is £{income_after_tax}")


            except ValueError:
                messagebox.showerror("Value Error!", "Please Make sure you enter a valid number")


        revenue_entry.bind("<Return>", lambda event: calculate_tax())



    country_entry = Entry(tax_window, width=20, background='#ffffff', fg='black')
    country_entry.bind("<Return>", lambda event :tax_income_func())
    country_entry.place(x=110, y=150)

    tax_window.mainloop()