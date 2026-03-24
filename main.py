import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def convert_to_kg(qty, unit):
    if unit.lower() == 'g':
        return qty / 1000
    return qty

def add_food():
    item = input("Food item: ")
    qty = float(input("Quantity: "))
    unit = input("Unit (kg/g): ")
    location = input("Location: ")
    address = input("Address: ")
    source = input("Source (Home/Hotel/Restaurant): ")
    expiry = int(input("Expiry time (hours): "))
    
    status = "Donated" if expiry > 5 else "Wasted"
    date = datetime.now().strftime("%Y-%m-%d")
    
    df = pd.read_csv("food_data.csv")
    
    new_row = pd.DataFrame([[date, item, qty, unit, location, address, source, expiry, status]],
                           columns=df.columns)
    
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("food_data.csv", index=False)
    
    print("✅ Entry added successfully!")
    print(f"📌 Status: {status}")

def generate_report():
    df = pd.read_csv("food_data.csv")
    
    df["Quantity_kg"] = df.apply(lambda x: convert_to_kg(x["Quantity"], x["Unit"]), axis=1)
    
    total = df["Quantity_kg"].sum()
    wasted = df[df["Status"] == "Wasted"]["Quantity_kg"].sum()
    donated = df[df["Status"] == "Donated"]["Quantity_kg"].sum()
    
    print("\n📊 REPORT")
    print(f"Total Food: {round(total,2)} kg")
    print(f"Wasted: {round(wasted,2)} kg")
    print(f"Donated: {round(donated,2)} kg")
    
    efficiency = (donated / total) * 100
    print(f"Donation Efficiency: {round(efficiency,2)}%")
    
    print("\n📍 Location-wise:")
    print(df.groupby("Location")["Quantity_kg"].sum())
    
    print("\n🍱 Top Food Items:")
    print(df.groupby("Food_Item")["Quantity_kg"].sum().sort_values(ascending=False))
    
    df.groupby("Date")["Quantity_kg"].sum().plot(kind='bar', title="Daily Food Waste")
    plt.show()

def menu():
    while True:
        print("\n🌱 FOOD WASTE MANAGEMENT SYSTEM")
        print("1. Add Entry")
        print("2. Generate Report")
        print("3. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            add_food()
        elif choice == '2':
            generate_report()
        elif choice == '3':
            break
        else:
            print("Invalid choice")

menu()