
# Tax according to criteria 1 - Total income (salary + business) = (salary income) + (Profits from F&O trading) + (Intraday equity trading)
# 0 – Rs.250,000 : 0% – Nil
# 250,000 – Rs.500,000 : 5% 
# 500,000 – Rs.1,000,000 : 20% 
# 1,000,000 – 1,200,000: 30% 

# Tax according to criteria 2 - Additional income classified under short term capital gains from delivery based equity. The tax rate on this is flat 15%.

class taxCalculator:
    def __init__(self, Salary_income, FO_trading, Intraday_Trading, Short_Term_Capital_Gain, intrest_income, loss_Gain):
        self.Salary_income = Salary_income
        self.FO_trading = FO_trading
        self.Intraday_Trading = Intraday_Trading
        self.Short_Term_Capital_Gain = Short_Term_Capital_Gain
        self.intrest_income = intrest_income
        self.loss_Gain = loss_Gain

    def calculateTax(self):
        total_Income = self.Salary_income + self.FO_trading + self.Intraday_Trading + self.intrest_income - self.loss_Gain
        Criteria1_Tax = 0
        Criteria2_Tax = 0
        if total_Income<250000:
            Criteria1_Tax = 0
        else:
            if total_Income<=500000:
                slab1_tax = ((total_Income-250000)/100)*5
                Criteria1_Tax = slab1_tax
            elif total_Income<=1000000:
                slab1_tax = ((250000)/100)*5
                slab2_tax = ((total_Income-500000)/100)*20
                Criteria1_Tax = slab1_tax+slab2_tax
            elif total_Income>1000000:
                slab1_tax = ((250000)/100)*5
                slab2_tax = ((500000)/100)*20
                slab3_tax = ((total_Income-1000000)/100)*30
                Criteria1_Tax = slab1_tax+slab2_tax+slab3_tax
        Criteria2_Tax = (self.Short_Term_Capital_Gain/100)*15

        return Criteria1_Tax + Criteria2_Tax

# if __name__ == "__main__":
#     Salary_income = int(input("Enter Salary: "))
#     FO_trading = int(input("Enter income from F&O Trading: "))
#     Intraday_Trading = int(input("Enter income from Intra Trading: "))
#     Short_Term_Capital_Gain = int(input("Enter income from short term capital gain: "))
#     intrest_income = int(input("Enter income on intrest: "))
#     loss_Gain = int(input("Enter Annual loss: "))
    
#     totaltax = taxCalculator(Salary_income, FO_trading, Intraday_Trading, Short_Term_Capital_Gain, intrest_income, loss_Gain)
#     print(totaltax.calculateTax())