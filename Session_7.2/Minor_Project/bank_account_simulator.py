# Bank Account Simulator: Create an OOP-based program to simulate bank account 
# operations (deposit, withdrawal, check balance) with error handling for invalid 
# operations. Make sure to use CRUD operations with MySQL to persist data, instead of just 
# runtime.
# CREATE TABLE accounts (
#     account_no INT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     balance DECIMAL(10,2) DEFAULT 0.00
# );
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

try:
    db=mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor=db.cursor()
    print("Database connected successfully")

except mysql.connector.Error as e:
    print("Database Error:", e)
    exit()

class Bank:
    def create_account(self,account_no,name,balance):
        query="""INSERT INTO accounts (account_no,name,balance) VALUES (%s,%s,%s)"""
        cursor.execute(query,(account_no,name,balance))
        db.commit()
        print("Account created successfully")

    def deposit(self,amount,account_no):
        query = """SELECT balance FROM accounts WHERE account_no=%s"""
        cursor.execute(query, (account_no,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError("Account not found.")
    
        query="""UPDATE accounts SET balance= balance+%s WHERE account_no=%s"""
        cursor.execute(query,(amount,account_no))
        db.commit()
        print("Amount deposited successfully.")

    def withdraw(self,amount,account_no):
        query = """SELECT balance FROM accounts WHERE account_no=%s"""
        cursor.execute(query, (account_no,))
        result = cursor.fetchone()

        if not result:
            raise ValueError("Account not found.")

        balance = result[0]

        if amount > balance:
            raise ValueError("Insufficient balance.")

        query = """UPDATE accounts 
                SET balance = balance - %s 
                WHERE account_no = %s"""
        cursor.execute(query, (amount, account_no))
        db.commit()

        print("Amount withdrawn successfully.")

    def check_balance(self,account_no):
        query="""SELECT balance from accounts WHERE account_no=%s"""
        cursor.execute(query,(account_no,))
        result = cursor.fetchone()
        if result:
            print("Balance:", result[0])
        else:
            print("Account not found.")

bank=Bank()

while True:
    print("1. Create Account")
    print("2. Deposit amount")
    print("3. Withdraw amount")
    print("4. Check Balance")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Enter following details for creating account")

            account_no = int(input("Enter account number: "))
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))

            if balance < 0:
                raise ValueError("Initial balance cannot be negative.")

            bank.create_account(account_no, name, balance)

        elif choice == 2:
            account_no = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))

            if amount <= 0:
                raise ValueError("Deposit amount must be greater than 0.")

            bank.deposit(amount, account_no)

        elif choice == 3:
            account_no = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than 0.")

            bank.withdraw(amount, account_no)

        elif choice == 4:
            account_no = int(input("Enter account number: "))
            bank.check_balance(account_no)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)

    except mysql.connector.Error as e:
        print("Database Error:", e)