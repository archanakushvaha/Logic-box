print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1.Generate a Pattern")
    print("2.Analyze a Range of Numbers")
    print("3.Exit")

    choice=int(input("Enter your Choice:"))

    if choice==1:

        rows=int(input("Enter the number of rows for the pattern:"))

        print("\n Pattern")

        for i in range(1,rows+1):
            for j in range(i):
                print("*",end="")
            print()

    elif choice==2:

        start=int(input("\nEnter the start of the range:"))
        end=int(input("Enter the end of the range:"))

        total=0
        
        for i in range(start,end+1):
            if i%2==0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")

            total +=i
                
        print(f"Sum of all numbers from {start} to {end} is:{total}")

    elif choice==3:
        print("Exiting the program.Goodbye!")

        break
    
    else:
        print("Invalide choice")
        



