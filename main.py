# create a program that will calculate the Return on Investment (ROI) for a rental property
# user inputs - monthly_income, monthly_expenses
# monthly_cashflow variable = monthly_income - monthly_expenses
# ROI - user input -> total_investment --- figure out annual cash flow -> monthly_cashflow * 12
# (annual cash flow / total investment) * 100 to obtain property ROI 

class ReturnOnInvestment():

    def __init__(self, address):
        self.address = address.title()

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
        store_info(self.address, self.roi)
        self.print_result()

    def print_result(self):
        # print all the info 
        print(f"\nPROPERTY: {self.address}")
        print("MONTHLY".center(50, '-'))
        print(f"INCOME: ${self.monthly_income}\nEXPENSES: ${self.monthly_expenses}\nCASH FLOW: ${self.monthly_cashflow}")
        print("".center(50, '-'))
        print(f"ROI: {round(self.roi, 2)} %")
        print("".center(50, '-'))

roi_storage = {}

def store_info(address, roi):
    # will store property address and calculated ROI
    roi_storage[address] = (round(roi, 2))

def print_stored_info():
    print("")
    print("CALCULATED ROI'S".center(50, '-'))
    for key, value in roi_storage.items():
        print(f"{key} : {value} %")
    print("")



# main
print("CALCULATION OF RENTAL INCOME".center(50, '-'))
while True:
    property_address = input("Enter property address: ")
    print("".center(50, '-'))
    p = ReturnOnInvestment(property_address)
    p.run()
    run_again = input("Calculate, print ROI's, or quit? (C/P/Q): ")
    run_again = run_again.upper()
    # found out checking for membership in set is faster than checking in list especially if list is large in size
    while run_again not in {'C', 'P', 'Q'}:
        print(">>> INVALID INPUT <<<")
        run_again = input("Enter 'C', 'P', or 'Q': ")
    if run_again == 'C':
        continue
    elif run_again == 'P':
        print_stored_info()
        user_input = input("Calculate another property 'C' or quit 'Q'?: ")
        user_input = user_input.upper()
        while user_input not in {'C', 'Q'}:
            print(">>> INVALID INPUT <<<")
            user_input = input("Enter 'C' or 'Q': ")
        if user_input == 'C':
            continue
        else:
            break
    else:
        break