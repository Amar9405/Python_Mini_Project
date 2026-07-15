

#Expense Traceker Project

#list of all expenses in form of  dictionry expenses
expenses=[] 

print("Welcome to Expense Tracker")

while True:
    print("===Menu===")
    print("1. Add expense")
    print("2. View all Expenses")
    print("3. View Total karch")
    print("4. exit")

    try:
        choice = int(input("Please Enter Your Choice "))
    except ValueError:
        print("Invalid Choice")
        continue

    # Add expense
    if choice == 1:
        date = input("Enter the Date of Expensive: ")
        category = input("Enter category (Food, Travel, Shopping,etc): ")
        description = input("Enter The more details: ")

        try:
            amount = float(input("How much money you spend:"))
        except ValueError:
            print("Invalid Choice")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense add succesfully")

    #View all Expenses
    elif(choice==2):
        if(len(expenses)==0):
            print("No Expenses Added.Go Spend some money !")
        else:
            print(" === Total Expenses ==== ")
            count=1

        for eachexpensive in expenses:
            print(f"Expensive No : {count} -> {eachexpensive['date']}, {eachexpensive['category']}, {eachexpensive['description']}, {eachexpensive['amount']}")
            count = count + 1
    
    elif(choice == 3):
        total=0
        for eachexpensive in expenses:
            total=total+eachexpensive["amount"]

        
        print(" Total amount You spend= ",total)

    elif(choice==4):
        print("Thanks for used this app")
        break
    
    else:
        print("Invalid Choice")

    

        











    







