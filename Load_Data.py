import csv

# List of key values, going to be referring to this a lot
data = []

data_loaded = False
def data_load():
    global data, data_loaded


    while data_loaded is not True:

        file_path = input("Enter the file path: ")

        try:

            with open(file_path, mode="r") as file:
                read = csv.DictReader(file)
                data = list(read)
                print("The data has been successfully loaded.")
                data_loaded = True

                break
        except FileNotFoundError:

            print(f"No file was found at '{file_path}'. Maybe double check the path and try again")

            continue
        except Exception as except_that:

            print(f"Reading error for: {except_that}")

            continue


data_load()