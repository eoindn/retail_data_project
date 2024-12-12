

from Load_Data import data



def average():
    store_location = input("Enter a Location")

    revenue = []

    for row in data:
        if row['StoreLocation'] == store_location:
            price = float(row['TotalPrice'])
            revenue.append(price)

    total_sum = sum(revenue)
    average_sum = total_sum / len(revenue)

    return average_sum

    # –--------------------#


def quantity():
    store_location = input("Enter a Location")

    amount_sold = []

    for row in data:
        if row['StoreLocation'] == store_location:
            amount = float(row['Quantity'])
            amount_sold.append(amount)

    total_quantity = sum(amount_sold)
    return total_quantity

    # ------------------------------#


def average_satisfaction():
    store_location = input("Enter a Location")

    cus_sat = []

    for row in data:
        if row['StoreLocation'] == store_location:
            satisfaction_score = float(row['CustomerSatisfaction'])
            cus_sat.append(satisfaction_score)

    average_sat = sum(cus_sat) / len(cus_sat)
    return average_sat


# ------------------------------------------------------------------------------------------#


def payment_method():

    debit = 0
    credit = 0
    cash = 0
    mobile = 0

    store_location = input("Enter a Location")
    for row in data:
        if row['StoreLocation'] == store_location:
            payment_type = str(row["PaymentMethod"])

            if payment_type == "Cash":
                cash += 1
            elif payment_type == "Credit Card":
                credit += 1
            elif payment_type == "Debit Card":
                debit += 1
            elif payment_type == "Mobile Payment":
                mobile += 1

    total = (credit+debit+mobile+cash)

    if total > 0:
        deb_perc = 100 * debit / total
        credit_perc = 100 * credit / total
        cash_perc = 100 * cash / total
        mobile_perc = 100 * mobile / total

        print(
            f"Debit Payments : %{deb_perc}\nCredit Payments: %{credit_perc}\nCash Payments: %{cash_perc}\nMobile Payments: %{mobile_perc}")
    else: print("Sorry, no data was returned, please check location")


# ------------------------------------------------------------------------------------------#

def total_rev_by_store():

    store_location = input("Enter a Location")

    revenue_by_location = []

    for row in data:
        if row['StoreLocation'] == store_location:
            price = float(row['TotalPrice'])
            revenue_by_location.append(price)


    if '' not in revenue_by_location:
        print(f"The total revenue gained by {store_location} is £{sum(revenue_by_location)}")
    else: print(f"{store_location} is not a valid location")






