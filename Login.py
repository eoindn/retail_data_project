from tkinter import Image
from tkinter import messagebox
from customtkinter import CTk, CTkFrame, CTkImage, CTkLabel, CTkEntry, CTkButton
from PIL import Image
#-----------Own Module---------#
from Dash import create_dashboard


def login_window():

    app = CTk()
    app.geometry("700x600")

    image = CTkImage(dark_image = Image.open("wave.jpg"),
                     size = (300,600))

    image2 = CTkImage(dark_image=Image.open("Donnaz.png"),size = (200,200))


    nice_blue = "#1e90ff"
    white = "#ffffff"



    frame1 = CTkFrame(app,fg_color = "#d3d3d3" , width = 400, height=600, border_width = 2)
    frame1.place(x = 300 , y = 0)
    frame2 = CTkFrame(app, width=300, height=600)
    frame2.place(x = 0, y = 0)
    image_label = CTkLabel(frame2, image = image, text = '')
    image_label.place(x = 0 , y = 0 )

    # ---------------------------------------------------------------------------------------------------

    def file_entry_ctk():

        file_entered = entry.get()
        if file_entered == "sales_data.csv":
            app.destroy()

            new_enter_button = CTkButton(frame1, corner_radius=32, text="Enter DashBoard", text_color=white,
                                     fg_color=f"{nice_blue}",command=create_dashboard()
                                     )
            new_enter_button.place(x=141, y=500)


        elif file_entered != "retail_sales.csv":
            warning_mes = messagebox.showerror("Invalid File", "Please Enter a Valid File")

#---------------------------------------------------------------------------------------------------------------------#


    entry = CTkEntry(frame1,width = 200, fg_color="transparent",border_color=f"{nice_blue}", corner_radius=20, placeholder_text="eg, sales.csv",
                     text_color='black')
    entry.bind("<Return>", lambda event: file_entry_ctk())
    entry.place(x = 110 , y = 400)

    welcome_label = CTkLabel(frame1, text = "Welcome Back", font = ("Arial",20,"bold"),text_color="black",  )
    welcome_label.place(x = 140, y = 100)

    enter_button = CTkButton(frame1,corner_radius = 32, text = "Press Enter To View", text_color=white, fg_color = f"{nice_blue}",
                             )
    enter_button.place(x = 140 , y = 500)

    image_label2 = CTkLabel(frame1, image = image2, text = '')
    image_label2.place(y = 180,  x = 115)

    enter_label = CTkLabel(frame1, text = "Confirm File Name", font = ("",12),text_color=nice_blue)
    enter_label.place(x = 158 , y = 440)



    app.mainloop()

login_window()