import argparse
import json
import os
import csv
from datetime import datetime

Expenses = "expense.json"

def load_data():
    if not os.path.exists(Expenses):
        return []
    with open(Expenses,"r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(tasks):
    with open(Expenses,"w") as file:
        json.dump(tasks,file,indent=4)


def add_expenses(description,amount,category):
    datas = load_data()
    data = {
        "id":len(datas)+1,
        "description":description,
        "amount":amount,
        "category":category,
        "date":datetime.now().strftime("%Y-%m-%d")
    }
    datas.append(data)
    save_data(datas)
    print("New Expense Added!")
    return
def update_expenses(track_id,description,amount,category):
    datas = load_data()
    for task in datas:
        if task["id"] == track_id:
            task["description"]= description
            task["amount"]= amount
            task["category"]= category
            save_data(datas)
            print("Expenses Updated !")
            return

    print("No Expenses Found at this Id!")

def delete_expenses(track_id):
    datas = load_data()
    data = [exp for exp in datas if exp["id"] != track_id]
    save_data(data)
    print("Expense Deleted Successfully!")
    return
def view_expenses(filter_exp = None):
    datas = load_data()
    if filter_exp:
        datas = [data for data in datas if data["category"]== filter_exp ]

    for task in datas:
        print(f"{[task["id"]]},{task["description"]},{task["amount"]},{task["category"]}")

def summary(month=None):
    datas = load_data()
    total = 0  # Initialize total to 0

    for exp in datas:
        try:
            amount = int(exp["amount"])  # Ensure amount is an integer
        except ValueError:
            print(f"Invalid amount format for ID {exp['id']}, skipping.")
            continue

        # If month is provided, filter expenses by month
        if month:
            if exp["date"].startswith(f"{datetime.now().year}-{int(month):02d}"):
                total += amount
        else:
            total += amount  # Add all expenses if no month is given

    print(f"Total Expenses: {total}")

def export_csv():
    datas = load_data()
    with open("expenses.csv","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["id","description","amount","category","date"])
        writer.writeheader()
        writer.writerows(datas)
    print("Exported as CSV file successfully !")

praser = argparse.ArgumentParser("Expenses Tracker Application")
subpraser = praser.add_subparsers(dest="command")

add_arg = subpraser.add_parser("add")
add_arg.add_argument("description",type=str)
add_arg.add_argument("amount",type=int)
add_arg.add_argument("category",type=str)

update_arg = subpraser.add_parser("update")
update_arg.add_argument("track_id",type=int)
update_arg.add_argument("description",type=str)
update_arg.add_argument("amount",type=int)
update_arg.add_argument("category",type=str)

delete_arg = subpraser.add_parser("delete")
delete_arg.add_argument("track_id",type=int)

view_arg = subpraser.add_parser("view-expenses")
view_arg.add_argument("category", type=str, nargs="?", default=None)


summary_arg = subpraser.add_parser("summary")
summary_arg.add_argument("--month",type=str,nargs="?",default=None)

export_arg = subpraser.add_parser("export")

args = praser.parse_args()

if args.command == "add":
    add_expenses(args.description,args.amount,args.category)
elif args.command == "update":
    update_expenses(args.track_id,args.description,args.amount,args.category)
elif args.command == "delete":
    delete_expenses(args.track_id)
elif args.command == "view-expenses":
    view_expenses(args.category)

elif args.command == "summary":
    summary(args.month)
elif args.command == "export":
    export_csv()

else:
    praser.print_help()









