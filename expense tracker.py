import csv
import matplotlib.pyplot as plt
import pandas as pd
def input_data():
    data = {
        "Date": ['Null'],
        "Category": ['Null'],
        "Amount": [0]

    }

    with open("C:/Users/User/Desktop/demo.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())

    with open("C:/Users/User/Desktop/demo.csv", 'a') as file:
        writer = csv.writer(file)
        while True:
            date = input("Enter the date: ")
            if date.lower() == 'exit':  # enter exit if you want to exit the application
                break
            category = input("In where you spent the money:")
            amount = input("Enter the amount you spent:")
            writer.writerow([date, category, amount])
    print("Data has been saved successfully :)")
def read_data():
    df = pd.read_csv(r"C:/Users/User/Desktop/demo.csv")
    print("the monthly data:\n", df)

def show_pie():
    df=pd.read_csv(r"C:/Users/User/Desktop/demo.csv")
    amount=df['Amount']
    categories=df['Category']
    plt.title("Expenses of this month")
    plt.pie(amount,labels=categories,autopct='%1.2f')
    plt.show() #to display the pie

print("Welcome to personal expense tracker!!")
print("Please enter your name and Age")
name=input("Name:")
Age=input("Age:")
salary=input("Salary:")
print("Choose any option from below:")
print("1.Enter today's Expense")
print("2.View my expenses")
print("3.show in graph")
option=int(input("Choose any option:"))
if option==1:
    input_data()
elif option==2:

    read_data()

else:
    show_pie()



#data












