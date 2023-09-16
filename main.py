# create a program that will calculate the Return on Investment (ROI) for a rental property\
# user inputs - monthly_income, monthly_expenses
# monthly_cashflow variable = monthly_income - monthly_expenses
# ROI - user input -> total_investment --- figure out annual cash flow -> monthly_cashflow * 12
# (annual cash flow / total investment) * 100 to obtain property ROI 

class ReturnOnInvestment():

    def __init__(self, address):
        self.address = address

    def run(self):
        # run() will start the program and call the other functions
        print(f"CALCULATING ROI FOR ---> {self.address.upper()}\n")
        self.get_monthly_income()


    def get_monthly_income(self):
        # will ask user to input monthly income and store it in monthly_income
        self.monthly_income = input("Enter property monthly income: ")
        while self.monthly_income.isalpha():
            print(">>> INVALID INPUT <<<")
            self.monthly_income = input("Enter amount in $: ")
        self.get_monthly_expenses()

    def get_monthly_expenses(self):
        # will ask user for monthly expenses and store it in monthly_expenses
        self.monthly_expenses = input("Enter property monthly expenses: ")
        while self.monthly_expenses.isalpha():
            print(">>> INVALID INPUT <<<")
            self.monthly_expenses = input("Enter amount in $: ")
        self.monthly_cashflow()

    def monthly_cashflow(self):
        # will calculate the monthly cashflow by doing monthly_income - monthly_expenses
        self.monthly_cashflow = int(self.monthly_income) - int(self.monthly_expenses)
        self.calc_roi()

    def calc_roi(self):
        # will calculate the total ROI and print it for the user to see
        self.total_investment = input("Enter property total investment: ")
        while self.total_investment.isalpha():
            print(">>> INVALID INPUT <<<")
            self.total_investment = input("Enter amount in $: ")
        self.annual_cashflow = int(self.monthly_cashflow) * 12
        self.roi = (int(self.annual_cashflow) / int(self.total_investment)) * 100
        self.roi_storage()
        self.print_result()

    def print_result(self):
        # print all the info 
        print(f"\nPROPERTY: {self.address}")
        print("MONTHLY".center(50, '-'))
        print(f"INCOME: ${self.monthly_income}\nEXPENSES: ${self.monthly_expenses}\nCASH FLOW: ${self.monthly_cashflow}")
        print("".center(50, '-'))
        print(f"ROI: {round(self.roi, 2)} %")
        print("".center(50, '-'))

    

# main
print("CALCULATION OF RENTAL INCOME".center(50, '-'))
while True:
    property_address = input("Enter property address: ")
    print("".center(50, '-'))
    p = ReturnOnInvestment(property_address)
    p.run()
    run_again = input("Calculate another property or print stored properties? (Y/N/P): ")
    run_again = run_again.upper()
    # found out checking for membership in set is faster than checking in list especially if list is large in size
    while run_again not in {'Y', 'N', 'P'}:
        print(">>> INVALID INPUT <<<")
        run_again = input("Enter 'Y' or 'N': ")
    if run_again == 'Y':
        continue
    elif run_again == 'N':
        break
    else:
        p.print_roi_storage()

        # FINISH DICTIONARY FOR STORING ADDRESS AND ROI VALUE