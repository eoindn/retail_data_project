from Summary import *
from Load_Data import data_load, data_loaded
from Process import *
from Login import login_window


data_load()



def terminal_menu():
    # List of menu options
    menu_options = [''
        ,"1 Load Data\n",
        "2 Visualise Data\n",
        "3 Total Transactions\n",
        "4 View Locations and Categories\n",
        "5 Transactions by Store\n",
        "6 Search Transaction by ID\n",
        "7 Calculate Revenue by Location\n",
        "8 Export Data to JSON\n",
        "9 Display Summary of Transactions\n",
        "10 Total Revenue\n",
        "11 Exit"
    ]


    menu_options = " ".join(menu_options)


    while True:  # Loop indefinitely until the user chooses to exit
        print(menu_options)
        try:
            choice = int(input("Select an Option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue  # Go back to the menu

        if choice == 1:
            data_load()
        if data_loaded:
            if choice == 1:
                pass
            elif choice == 2:
                login_window()
            elif choice == 3:
               print(total_transactions())
            elif choice == 4:
                print(locations_category())
            elif choice == 5:
                print (transactions_for_store())
            elif choice == 6:
                transaction_by_id()
            elif choice == 7:
                print(rev_for_location())

            elif choice == 8:
                pass
            elif choice == 9:
                print("1.) Store Revenue\n2.) Payment Methods\n3.) Average Satisfaction\n4.) Quantity Sold\n5.) Average Price")
                summary_choice = int(input("Select an option"))
                if summary_choice == 1:
                    total_rev_by_store()
                elif summary_choice == 2:
                    print(payment_method())
                elif summary_choice == 3:
                   print(average_satisfaction())
                elif summary_choice == 4:

                    print(quantity())
                elif summary_choice == 5:
                    average()
                else:
                    print("Please enter a valid number")

            elif choice == 10:
                print(all_rev())

            elif choice == 11:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid menu option.")

        # Ask if user wants to continue
            continue_choice = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("Goodbye!")
                break  # quit if not
            else: print("Please load the data")



terminal_menu()