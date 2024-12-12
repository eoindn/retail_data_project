from tkinter import *
from Load_Data import data_load,data_loaded,data
from tkinter import PhotoImage
from PIL import Image, ImageTk










def create_dashboard():
    global data
    data_load()

    # ----------------Variables------------------------#

    ceiling_height = 60
    ceiling_width = 1750

    side_bar_height = 1000
    side_bar_width = 300

    frame1_height = 350
    frame1_width = 1500

    frame2_height = 500
    frame2_width = 310

    frame3_height = 500
    frame3_width = 310

    frame4_height = 500
    frame4_width = 310

    frame5_height = 500
    frame5_width = 310

    # ---------------Window Config---------------------#

    window1 = Tk()
    window1.title("Data Manager")
    window1.geometry('1366x768')
    window1.state('zoomed')
    window1.config(background='#f4fefd')

    ceiling = Frame(window1, bg='#ffffff')
    ceiling.place(x=0, y=0, width = ceiling_width, height = ceiling_height)

    sidebar = Frame(window1, bg='#d3d3d3')
    sidebar.place(x=0, y=60, width = side_bar_width, height = side_bar_height)

    top_title = Label(window1, text='Data Dashboard', font=("", 13, "bold"), fg='#0064d3', bg='#eff5f6')
    top_title.place(x=325, y=70)

    chart_frame1 = Frame(window1, bg='#ffffff')
    chart_frame1.place(x=328, y=110, width=frame1_width, height=frame1_height)

    chart_frame2 = Frame(window1, bg='#ffffff')
    chart_frame2.place(x=328, y=495, width=frame2_width, height=frame2_height)

    chart_frame3 = Frame(window1, bg='#ffffff' )
    chart_frame3.place(x=680, y=495, width=frame3_width, height=frame3_height)

    chart_frame4 = Frame(window1, bg='#ffffff')
    chart_frame4.place(x=1030, y=495, width=frame4_width, height=frame4_height)

    chart_frame5 = Frame(window1, bg="#ffffff")
    chart_frame5.place(x=1380, y=495, width=frame5_width, height=frame5_height)

    # Logo and Branding for the Donnaz logo, a nickname derived from my surname

    logo = Image.open('Donnaz.png')
    logo_test = ImageTk.PhotoImage(logo)
    logo_label = Label(window1, image=logo_test, bg='#d3d3d3',fg="#d3d3d3")
    logo_label.image = logo_test

    logo_label.place(x=25, y=60)

    window1.mainloop()


create_dashboard()