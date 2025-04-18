#Python Compound Interest Calculator
#A = P* (1 + r/n)**n*t
#A = Final Amount 
#P = Principle Amount
#R = Rate of interest (in decimal)
#n = number of times P is compounded in a year
#t = duration of the compounding (in years)

P_Amount = float(input("Enter your principle Amount: "))
Time_Taken = int(input("Enter the duration of the investment(in years): "))
N_value = 12 #Considering the principle amount is compounded every month of the year.
Rate_of_Interest = 0.02

A_Amount = P_Amount*(1 + (Rate_of_Interest/N_value))**(N_value*Time_Taken)
print(f"Final Compounded Amount: {A_Amount:.2f}")