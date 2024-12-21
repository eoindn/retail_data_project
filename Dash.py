from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import csv
from customtkinter import *
from tkinter import messagebox
from datetime import *
from matplotlib import animation


data = []

def force_load(file_path = 'sales_data.csv'):
    global data


    if os.path.exists(file_path):

        with open(file_path, mode="r") as file:
            read = csv.DictReader(file)
            data = list(read)
            print("Data has been initialised")



    else:
        print(f"Error: the file {file_path} was not found\n Please Try Again")




def create_dashboard():

    force_load()

    # ----------------Variables------------------------#

    scrolling_canv_width = 400
    scrolling_canv_height = 50
    scrolling_canv_t_speed = 30


    ceiling_height = 60
    ceiling_width = 1750

    side_bar_height = 1000
    side_bar_width = 300

    chart_frame1_height = 350
    chart_frame1_width = 1500

    chart_frame2_height = 500
    chart_frame2_width = 310

    chart_frame3_height = 500
    chart_frame3_width = 310

    chart_frame4_height = 500
    chart_frame4_width = 310

    chart_frame5_height = 500
    chart_frame5_width = 310

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
    chart_frame1.place(x=328, y=110, width=chart_frame1_width, height=chart_frame1_height)

    chart_frame2 = Frame(window1, bg='#ffffff')
    chart_frame2.place(x=328, y=495, width=chart_frame2_width, height=chart_frame2_height)

    chart_frame3 = Frame(window1, bg='#ffffff' )
    chart_frame3.place(x=680, y=495, width=chart_frame3_width, height=chart_frame3_height)

    chart_frame4 = Frame(window1, bg='#ffffff')
    chart_frame4.place(x=1030, y=495, width=chart_frame4_width, height=chart_frame4_height)

    chart_frame5 = Frame(window1, bg="#ffffff")
    chart_frame5.place(x=1380, y=495, width=chart_frame5_width, height=chart_frame5_height)

    # Logo and Branding for the Donnaz logo, a nickname derived from my surname

    logo = Image.open('Donnaz.png')
    logo_test = ImageTk.PhotoImage(logo)
    logo_label = Label(window1, image=logo_test, bg='#d3d3d3',fg="#d3d3d3")
    logo_label.image = logo_test

    logo_label.place(x=25, y=60)

    logo = Image.open('Donnaz.png')
    logo_test = ImageTk.PhotoImage(logo)
    logo_label = Label(image=logo_test, bg="#d3d3d3")
    logo_label.image = logo_test

    logo_label.place(x=25, y=60)

    # ------------------------------------------Scrolling Bar--------------------------------------------------------#

    def scrolling_text(text, speed):
        canvas = Canvas(ceiling, bg="#1e90ff", height = scrolling_canv_height, width = scrolling_canv_width,
                        highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        the_text = canvas.create_text(1750, scrolling_canv_t_speed, text=text)

        def scrolling_motion():
            canvas.move(the_text, -speed, 0)

            if canvas.bbox(the_text)[2] < 0:
                canvas.move(the_text, 1750 - canvas.bbox(the_text)[2], 0)
            ceiling.after(30, scrolling_motion)

        scrolling_motion()

    scrolling_text(
        f"Dash Board for Retail Sales Data      Total Transactions : 500      Total Revenue : £682745.74      Common Method: Mobile Payment @ 26%      Share Price: £2398.43 (-90.04%)     ",
        speed=3)

    # --------------------------------------------------------------------------------------------------#

    def buttons():
        # ---------------Label Binding Functions-----------#
        def leave():
            window1.destroy()

        # CSV table for the csv button
        def tk_csv_table(file_path='sales_data.csv'):
            with open(file_path, mode='r') as file:
                csv_reader = csv.reader(file)
                ceilings = next(csv_reader)
                rows = [ceilings] + list(csv_reader)
                width_of_column = [max(len(cell) for cell in col) for col in zip(*rows)]

                table = []
                border = '+'.join('-' * (width + 2) for width in width_of_column)
                table.append(f"+{border}+")
                for row in rows:
                    formatted_row = "| " + " | ".join(
                        f"{cell.ljust(width)}" for cell, width in zip(row, width_of_column)) + " |"
                    # Add some nice separation
                    table.append(formatted_row)
                    table.append(f"+{border}+")
                return "\n".join(table)

        # -------------------------------------------------------------------------------------------------#

        def display_table(file_path):
            root = Tk()
            root.title("CSV Table Display")

            text = Text(root, wrap="none", font=("Courier", 12))
            text.pack(fill="both", expand=True)

            table_string = tk_csv_table(file_path)

            text.insert("1.0", table_string)
            text.config(state="disabled")
            root.mainloop()

        # ----------------------------------Side Bar Buttons-----------------------------------------–#

        # Buttons made as Labels  due to buttons not
        # -being displayed properly on Mac OS
        info_button =Label(sidebar, text="Info",  background="#1e90ff",fg = "#ffffff",
                                font=("", 13, "bold"),width = 12 )
        info_button.place(x=90, y=270)

        def info_button_win():
            messagebox.showinfo("Graph Information",
                                "This dashboard displays displays relevant information from the sales data, visualised as pie charts, line graphs, and bar charts"
                                "You can , on the scrolling text we can see key insights. If you wish to see all the transaction formatted please select display CSV")

        info_button.bind("<Button-1>", lambda event: info_button_win())

        manage_button = Label(sidebar, text="Manage", font=("", 13, "bold"), fg="#ffffff",background= "#1e90ff",
                                  cursor='hand2',width = 12)
        manage_button.bind("<Button-1>")
        manage_button.place(x=90, y=345)

        exit_button = Label(sidebar, text="Exit Dash", font=("", 13, "bold"),  background="#1e90ff", fg = "#ffffff",width = 12)
        exit_button.bind("<Button-1>", lambda event: leave())
        exit_button.place(x=90, y=420)

        dis_csv_button =Label(sidebar, text="Display CSV", font=("", 13, "bold"),
                                   background="#1e90ff",fg = "#ffffff", cursor="hand2", width = 12)

        dis_csv_button.bind("<Button-1>", lambda event: display_table(file_path='sales_data.csv'))
        dis_csv_button.place(x=90, y=495)




    buttons()
    create_da_charts(chart_frame1, chart_frame2, chart_frame3, chart_frame4, chart_frame5)
    window1.mainloop()


# -------------------------------------------------------------------------------------------------#

def create_da_charts(chart_frame1, chart_frame2, chart_frame3, chart_frame4, chart_frame5):
    revenue_by_location = {}
    for row in data:
        location = row['StoreLocation']
        price = float(row['TotalPrice'])
        revenue_by_location[location] = revenue_by_location.get(location, 0) + price

    fig_pie = plt.Figure(figsize=(4, 3), dpi=100)
    ax_pie = fig_pie.add_subplot(111)
    ax_pie.pie(list(revenue_by_location.values()),
               labels=list(revenue_by_location.keys()),
               autopct='%1.1f%%', startangle=90)
    ax_pie.set_title('Revenue by Store Location')
    placed_pie = FigureCanvasTkAgg(fig_pie, master=chart_frame1)
    placed_pie_widget = placed_pie.get_tk_widget()
    placed_pie_widget.place(x=500, y=45)
    # placed_pie_widget.pack(fill=None, expand=False)

    debit = 0
    credit = 0
    cash = 0
    mobile = 0
    for row in data:
        payment_type = str(row["PaymentMethod"])

        if payment_type == "Cash":
            cash += 1
        elif payment_type == "Credit Card":
            credit += 1
        elif payment_type == "Debit Card":
            debit += 1
        elif payment_type == "Mobile Payment":
            mobile += 1

    deb_perc = 100 * debit / 500
    credit_perc = 100 * credit / 500
    cash_perc = 100 * cash / 500
    mobile_perc = 100 * mobile / 500

    payments = {"Credit Card": int(credit_perc), "Debit Card": int(deb_perc), "Cash": int(cash_perc),
                "Mobile": int(mobile_perc)}

    #-----------------------Pie Chart 1--------------------------#

    fig_pie2 = plt.Figure(figsize=(3, 4), dpi=100)
    ax_pie2 = fig_pie2.add_subplot(111)
    ax_pie2.pie(list(payments.values()),
                labels=list(payments.keys()),
                autopct='%1.1f%%', startangle=90)
    ax_pie2.set_title('Revenue by Store Location')
    placed_pie2 = FigureCanvasTkAgg(fig_pie2, master=chart_frame1)
    placed_pie2_widget = placed_pie2.get_tk_widget()
    placed_pie2_widget.place(x=120, y=0)




    #------------------------Hista---------------------#

    transaction_values = [float(row['TotalPrice']) for row in data]
    fig_hist = plt.Figure(figsize=(4, 3), dpi=100)
    ax_hist = fig_hist.add_subplot(111)

    ax_hist.hist(transaction_values, bins=5, edgecolor='black')
    ax_hist.set_title("Transaction Values")
    ax_hist.set_xlabel("Transaction Value")
    ax_hist.set_ylabel("Frequency")

    canvas_hist = FigureCanvasTkAgg(fig_hist, master=chart_frame4)
    canvas_hist_widget = canvas_hist.get_tk_widget()
    canvas_hist_widget.pack(fill='both', expand=True)


    #-----------------------Da time, Line Graph------------------------------–#

    aggregated_data = {}
    for entry in data:
        try:
            date = datetime.strptime(entry["TransactionDate"], "%Y-%m-%d").date()
        except ValueError:
            continue

        total_price = float(entry["TotalPrice"])
        if date not in aggregated_data:
            aggregated_data[date] = 0
        aggregated_data[date] += total_price


    sorted_dates = sorted(aggregated_data.keys())
    sorted_totals = [aggregated_data[date] for date in sorted_dates]


    fig_line = plt.Figure(figsize=(4, 3), dpi=100)
    ax_line = fig_line.add_subplot(111)
    ax_line.plot(sorted_dates, sorted_totals, marker='o', color='blue', linestyle='-')
    ax_line.set_title("Total Transactions Over Time")
    ax_line.set_xlabel("Date")
    ax_line.set_ylabel("Total Sales Made")
    ax_line.tick_params(axis='x', rotation=45)

    canvas_line = FigureCanvasTkAgg(fig_line, master=chart_frame3)
    canvas_line_widget = canvas_line.get_tk_widget()
    canvas_line_widget.pack(fill='both', expand=True)

#----------------Bar chart one-------------------------–#




    locations = ["Rural", "City", "Suburban"]


    rural_quantity = [int(row['Quantity']) for row in data if row['StoreLocation'] == 'Rural']
    city_quantity = [int(row['Quantity']) for row in data if row['StoreLocation'] == 'City Centre']
    suburban_quantity = [int(row['Quantity']) for row in data if row['StoreLocation'] == 'Suburban']


    totals = [sum(rural_quantity), sum(city_quantity), sum(suburban_quantity)]


    fig, ax = plt.subplots(figsize=(6, 4))
    fig.subplots_adjust(left=0.2)
    plt.title("Quantity Sold Per Location", fontsize=6)
    ax.set_xlabel("Locations", fontweight='bold', fontsize=6)
    ax.set_ylabel("Amount Sold", fontweight='bold', fontsize=6)
    ax.tick_params(axis='both', which='major', labelsize=7)


    colors = ['tab:purple', 'tab:red', 'tab:orange']

    # Animation loop
    artists = []
    for i in range(1, 101):

        frame_totals = [total * (i / 100) for total in totals]
        ax.clear()
        ax.bar(locations, frame_totals, color=colors)

        # Set axis properties (reset due to clear())
        ax.set_title("Quantity Sold Per Location", fontsize=6)
        ax.set_xlabel("Locations", fontweight='bold', fontsize=6)
        ax.set_ylabel("Amount Sold", fontweight='bold', fontsize=6)
        ax.tick_params(axis='both', which='major', labelsize=7)
        ax.set_yticks(range(0, max(totals) + 50, 50))

    canvas_barchart = FigureCanvasTkAgg(fig, master=chart_frame2)
    canvas_barchart_widget = canvas_barchart.get_tk_widget()
    canvas_barchart_widget.pack(fill='both', expand=True)

    canvas_barchart.draw_idle()

    #------------------Bar Chart Two-----------------------------––#

    payment_methods = sorted({row['PaymentMethod'] for row in data})
    store_locations = sorted({row['StoreLocation'] for row in data})


    quant_matrix = [[0 for _ in store_locations] for _ in payment_methods]


    for row in data:
        payment_idx = payment_methods.index(row['PaymentMethod'])
        location_idx = store_locations.index(row['StoreLocation'])
        quant_matrix[payment_idx][location_idx] += int(row['Quantity'])


    fig, ax = plt.subplots(figsize=(4, 3))


    bar_width = 0.15
    x_positions = list(range(len(store_locations)))

    # For each payment method plot bars adjusting x to the right to create grouped bars per loc
    for idx, method in enumerate(payment_methods):
        adjusted_x_positions = [x + idx * bar_width for x in x_positions]
        ax.bar(adjusted_x_positions, quant_matrix[idx], bar_width, label=method)


    ax.set_title("Payment Method by Location", fontsize=6)
    ax.set_xlabel("Store Locations", fontsize=6)
    ax.set_ylabel("Quantity Sold", fontsize=6)


    centered_ticks = [x + bar_width * (len(payment_methods) - 1) / 2 for x in x_positions]
    ax.set_xticks(centered_ticks)
    ax.set_xticklabels(store_locations, rotation=45, ha='right')


    ax.legend(fontsize=6, loc="upper left")
    ax.tick_params(axis='both', which='major', labelsize=6)


    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2)


    canvas = FigureCanvasTkAgg(fig, master=chart_frame5)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill='both', expand=True)


