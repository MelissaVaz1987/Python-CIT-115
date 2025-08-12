PV=float(input("Enter Principle Investment:"))
R=float(input("Enter Interest Rate:"))
t=float(input("Enter Number of Periods:"))
m=int(input("Enter Number of Compounding:"))


FV = PV * ( 1 + ( (R/100) / m ) ) ** ( m * t)
print(f"The account balance will be: {FV:,.2f}")
