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


class BankApp:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Pavitra Banking System 💙")
        self.root.geometry("420x420")
        self.root.configure(bg="#d9f2ff")

        tk.Label(root, text="Pavitra Banking System", 
                 font=("Arial", 16, "bold"), bg="#d9f2ff").pack(pady=10)

        tk.Label(root, text="Account Number", bg="#d9f2ff").pack()
        self.acc_entry = tk.Entry(root)
        self.acc_entry.pack()

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