from Load_Data import data




def total_transactions():
    return len(data)


#----------------------------------------------------------------------------------–––––––––––#


def all_rev():

    prices = [float(row['TotalPrice']) for row in data] # Collect integers directly into a list

    total_prof = sum(prices)
    return f"£{total_prof}"  # Sum the list of prices


#--------------------------------------------------------------------------------------------#


def locations_category():


    location = {row['StoreLocation'] for row in data}
    categories = {row['ProductCategory'] for row in data}
    return location,categories

#-------------------------------------------------------------------------------------------#

def transactions_for_store():
    store_location = input("What store location are you looking for?").title()
    transactions = [row for row in data if row['StoreLocation'] == store_location]
    return transactions

#------------------------------------------------------------------------------------------#


def transaction_by_id():


    identify = input("Enter a Store ID")

    for row in data:
        if row['TransactionID'] == identify:
            print("Transaction Found", f"Details: {row}")
        else:pass
#------------------------------------------------------------------------------------------#


def rev_for_location():

    revenue = {}

    loc = input("Enter a Location").title()

    for row in data:
        price = float(row['TotalPrice'])
        location = row['StoreLocation']
        if loc == location:
            revenue[location] = revenue.get(location, 0) + price


    for location in revenue:
        revenue[location] = round(revenue[location],2)




    return f"£{revenue}"

#------------------------------------------------------------------------------------------#
