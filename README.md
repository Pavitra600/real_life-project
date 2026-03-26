# Bank Management System (Python)

## Project Description

This is a simple **Bank Management System** written in Python.
The program allows users to perform basic banking operations such as creating an account, depositing money, withdrawing money, and viewing account details.

## Files in the Project

* **pavitra_bank.py** – Main Python program that runs the bank application.
* **pavitra_bank_system.txt** – Stores account data such as account number, name, and balance.

## Features

* Create a new bank account
* Deposit money
* Withdraw money
* View account details
* Transfering money within accounts
* Store account data in a text file

## Requirements

* Python 3 installed on your system

## How to Run the Program

1. Download or clone the repository.
2. Open the project folder.
3. Run the following command:

```
python pavitra_bank.py

import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "pavitra_bank_system.txt"

class Bank:
    def __init__(self):
        if not os.path.exists(FILE_NAME):
            open(FILE_NAME, "w").close()

    def create_account(self, acc_no, name, balance):
        if self.account_exists(acc_no):
            return False

        with open(FILE_NAME, "a") as file:
            file.write(f"{acc_no},{name},{balance}\n")
        return True

    def account_exists(self, acc_no):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    return True
        return False

    def get_balance(self, acc_no):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    return float(data[2])
        return None

    def update_balance(self, acc_no, new_balance):
        lines = []
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    lines.append(f"{acc_no},{data[1]},{new_balance}\n")
                else:
                    lines.append(line)

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

    def deposit(self, acc_no, amount):
        balance = self.get_balance(acc_no)
        if balance is not None:
            balance += amount
            self.update_balance(acc_no, balance)
            return True
        return False

    def withdraw(self, acc_no, amount):
        balance = self.get_balance(acc_no)
        if balance is not None and balance >= amount:
            balance -= amount
            self.update_balance(acc_no, balance)
            return True
        return False

    def transfer(self, from_acc, to_acc, amount):
        if not self.account_exists(from_acc) or not self.account_exists(to_acc):
            return "Account not found"

        from_balance = self.get_balance(from_acc)

        if from_balance < amount:
            return "Insufficient balance"

        to_balance = self.get_balance(to_acc)

        self.update_balance(from_acc, from_balance - amount)
        self.update_balance(to_acc, to_balance + amount)

        return "Success"


class BankApp:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Pavitra Banking System 💙")
        self.root.geometry("420x500")
        self.root.configure(bg="#d9f2ff")

        tk.Label(root, text="Pavitra Banking System", 
                 font=("Arial", 16, "bold"), bg="#d9f2ff").pack(pady=10)

        tk.Label(root, text="Account Number", bg="#d9f2ff").pack()
        self.acc_entry = tk.Entry(root)
        self.acc_entry.pack()

        tk.Label(root, text="Receiver Account", bg="#d9f2ff").pack()
        self.to_acc_entry = tk.Entry(root)
        self.to_acc_entry.pack()

        tk.Label(root, text="Name", bg="#d9f2ff").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Amount", bg="#d9f2ff").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Button(root, text="Create Account", bg="green", fg="white",
                  command=self.create_account).pack(pady=5)

        tk.Button(root, text="Deposit", bg="blue", fg="white",
                  command=self.deposit).pack(pady=5)

        tk.Button(root, text="Withdraw", bg="orange", fg="white",
                  command=self.withdraw).pack(pady=5)

        tk.Button(root, text="Transfer", bg="red", fg="white",
                  command=self.transfer).pack(pady=5)

        tk.Button(root, text="Check Balance", bg="purple", fg="white",
                  command=self.check_balance).pack(pady=5)

    def create_account(self):
        acc = self.acc_entry.get()
        name = self.name_entry.get()
        amount = self.amount_entry.get()

        if not acc or not name or not amount:
            messagebox.showwarning("Warning", "All fields required")
            return

        try:
            amount = float(amount)
        except:
            messagebox.showerror("Error", "Enter valid amount")
            return

        if self.bank.create_account(acc, name, amount):
            messagebox.showinfo("Success", "Account created successfully")
        else:
            messagebox.showerror("Error", "Account already exists")

    def deposit(self):
        acc = self.acc_entry.get()
        amount = self.amount_entry.get()

        try:
            amount = float(amount)
        except:
            messagebox.showerror("Error", "Enter valid amount")
            return

        if self.bank.deposit(acc, amount):
            messagebox.showinfo("Success", "Amount deposited")
        else:
            messagebox.showerror("Error", "Account not found")

    def withdraw(self):
        acc = self.acc_entry.get()
        amount = self.amount_entry.get()

        try:
            amount = float(amount)
        except:
            messagebox.showerror("Error", "Enter valid amount")
            return

        if self.bank.withdraw(acc, amount):
            messagebox.showinfo("Success", "Amount withdrawn")
        else:
            messagebox.showerror("Error", "Insufficient balance or account not found")

    def transfer(self):
        from_acc = self.acc_entry.get()
        to_acc = self.to_acc_entry.get()
        amount = self.amount_entry.get()

        try:
            amount = float(amount)
        except:
            messagebox.showerror("Error", "Enter valid amount")
            return

        result = self.bank.transfer(from_acc, to_acc, amount)

        if result == "Success":
            messagebox.showinfo("Success", "Amount transferred successfully")
        else:
            messagebox.showerror("Error", result)

    def check_balance(self):
        acc = self.acc_entry.get()
        balance = self.bank.get_balance(acc)

        if balance is not None:
            messagebox.showinfo("Balance", f"Current Balance: {balance}")
        else:
            messagebox.showerror("Error", "Account not found")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()

```

## Example

The program will display a menu like:

1. Create Account
2. Deposit Money
3. Withdraw Money
4. View Account
5. Tranfer
6. Exit
## Output
## CREATE ACCOUNT

<img width="509" height="648" alt="image" src="https://github.com/user-attachments/assets/c08ed760-0acf-430f-828c-8a26e5c33557" />
<img width="301" height="190" alt="image" src="https://github.com/user-attachments/assets/915f4501-e3ee-477e-8d7c-58404a8beacb" />
<img width="331" height="174" alt="image" src="https://github.com/user-attachments/assets/f4ae466b-67e1-45de-8f13-166eb01af5cf" />


## DEPOSIT
<img width="507" height="634" alt="image" src="https://github.com/user-attachments/assets/f4d3db13-e695-4b9a-9e96-66d890d17712" />

<img width="336" height="156" alt="image" src="https://github.com/user-attachments/assets/ec2e0b87-55c7-468a-9020-f5518dae8dab" />

## TRANSFER
<img width="519" height="650" alt="image" src="https://github.com/user-attachments/assets/c6e8349c-8768-4444-8ed1-a36c79abda89" />

<img width="350" height="120" alt="image" src="https://github.com/user-attachments/assets/b1590a6d-08df-4f97-be51-44ccdc477800" />

## WITHDRAW
<img width="501" height="632" alt="image" src="https://github.com/user-attachments/assets/a67d010c-ef71-474d-b9ab-45c2cdddbc55" />

<img width="354" height="145" alt="image" src="https://github.com/user-attachments/assets/bf53cf26-df52-4efb-aaf6-811457f08e53" />

## CHECK BALANCE
<img width="513" height="663" alt="image" src="https://github.com/user-attachments/assets/6d95b953-2672-45d9-8161-81212a131cf8" />

<img width="267" height="181" alt="image" src="https://github.com/user-attachments/assets/26215ba4-8a9f-4fe9-a937-bdad782473b0" />

## Author

Pavitra J
212224110043
