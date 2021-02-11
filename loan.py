import numpy as np
import numpy_financial as npf
from datetime import datetime
import pandas as pd

class Loan():
    """A standard Loan class"""
    def __init__(self, annual_rate, num_years, principal_amt, loan_origination_date=''):
        """Initialize the loan"""
        self.annual_rate = annual_rate
        self.num_years = num_years
        self.principal_amt = principal_amt
        self.loan_origination_date = loan_origination_date
        
    def calculate_elapsed_periods(self):
        """Calculates how many periods have elapsed"""
        
        num_elapsed_periods = 0
        
        # Check that an origination date was supplied
        if self.loan_origination_date == '':
            print("Error: No origination date was supplied for this loan.\n")
        else:
            
            try:
                current_date = pd.to_datetime(datetime.now())
                origination_date = pd.to_datetime(self.loan_origination_date, format='%Y-%m-%d')
                num_elapsed_periods = pd.date_range(origination_date, current_date, freq='M').shape[0]
                
            except ValueError:
                print("Error: Origination date must be formatted as 'yyyy-mm-dd', calculated loan balance is not valid.")
            
            
        return num_elapsed_periods    
    
        
    def calculate_payment(self):
        """Calculate the loan payment"""
        payment = round(npf.pmt(self.annual_rate/12, self.num_years*12, self.principal_amt),2)
        return payment
        
    def calculate_remaining_balance(self):
        """Calculates the remaining balance"""
        # Determine the number of periods we are into the loan
        num_periods_elapsed = self.calculate_elapsed_periods()
        
        # Find out how much principal we have paid
        prin_paid_to_date = 0.0
        for current_period in range(0, num_periods_elapsed):
            prin_paid_to_date -= round(npf.ppmt(self.annual_rate/12, current_period, self.num_years*12, self.principal_amt ),2)
            
        return self.principal_amt - prin_paid_to_date    
            
        
    
# Main Program



# Current house loan
print("\nCurrent house loan: ")
myHouseLoan = Loan(.029,30,554000,'2020-10-01')

print("My monthly loan payment is: "
+ str(myHouseLoan.calculate_payment()) + ".")

print("My current loan balance is: "
+str(myHouseLoan.calculate_remaining_balance()))



print("\n---------------------------------------\n")



print("\nHouse in Texas, 200k note, 30 years: ")
print("My monthly loan payment is: "
+ str(Loan(.036, 30, 200000).calculate_payment()) + ".")

print("\nHouse in Texas, 200k note, 15 years: ")
print("My monthly loan payment is: "
+ str(Loan(.0285, 15, 200000).calculate_payment()) + ".")

print("\nHouse in Texas, 100k note, 30 years: ")
print("My monthly loan payment is: "
+ str(Loan(.036, 30, 100000).calculate_payment()) + ".")

print("\nHouse in Texas, 100k note, 15 years: ")
print("My monthly loan payment is: "
+ str(Loan(.0285, 15, 100000).calculate_payment()) + ".")

print("\n---------------------------------------\n")

print("\nLoan on a Volvo XC-90, 25k, 4 years: ")
print("My monthly loan payment is: "
+ str(Loan(.055,4,25000).calculate_payment()) + ".")




