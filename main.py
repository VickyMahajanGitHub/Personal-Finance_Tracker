import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description
import matplotlib.pyplot as plt


class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMNS= ['Date', 'Amount', 'Category', 'Description']
    FORMAT= "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df= pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'Date': date,
            'Amount': amount,
            'Category': category,
            'Description': description
        }
        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully.")
        print(f"Entry added: {new_entry}")

    @classmethod
    def get_transactions(cls,start_date,end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['Date'] = pd.to_datetime(df['Date'], format=CSV.FORMAT)
        start_date = pd.to_datetime(start_date, format=CSV.FORMAT)
        end_date = pd.to_datetime(end_date, format=CSV.FORMAT)

        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the specified date range.")
            return None
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}:")
            print(filtered_df.to_string (index=False, formatters={'Date': lambda x: x.strftime(CSV.FORMAT)}))

            # Convert Amount column to numeric
            filtered_df['Amount'] = pd.to_numeric(filtered_df['Amount'], errors='coerce')
            # Calculate total income and expense

            total_income = filtered_df[filtered_df['Category'] == 'Income']['Amount'].sum()
            total_expense = filtered_df[filtered_df['Category'] == 'Expense']['Amount'].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Amount: ${(total_income - total_expense):.2f}")
        return filtered_df

            

def add():
    CSV.initialize_csv()
    date = get_date("Enter the  date of the transaction (DD-MM-YYYY) or press 'Enter' to use current date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(date, amount, category, description)



def plot_transactions(df):
    df.set_index('Date', inplace=True)
    income_df=df[df['Category'] == 'Income'].resample('D').sum().reindex(df.index, fill_value=0)

    expense_df=df[df['Category'] == 'Expense'].resample('D').sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df['Amount'], label='Income', color='green')
    plt.plot(expense_df.index, expense_df['Amount'], label='Expense', color='r')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income and Expense Over Time')
    plt.grid(True)
    plt.legend()
    plt.show()

# date = input("Enter the date (DD-MM-YYYY): ")

# amount = input("Enter the amount: ")
# category = input("Enter the category: ")
# description = input("Enter the description: ")



# add()
# CSV.get_transactions("05-05-2025", "05-06-2025")

# main function to run the program
def main():
    while True:
        print("\n Finance Tracker")
        print("1. Add a new Transaction")
        print("2. View Transactions and summary within a date range")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            add()
        elif choice == '2':
            start_date = get_date("Enter the start date (DD-MM-YYYY): ")
            end_date = get_date("Enter the end date (DD-MM-YYYY): ")
            df=CSV.get_transactions(start_date, end_date)
            if df is not None and input("Do you want to plot the transactions? (y/n): ").lower() == 'y':
                plot_transactions(df)
               
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Enter 1,2 or 3.")


if __name__ == "__main__":
    main()