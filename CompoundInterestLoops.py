def validateInput(sPrompt):
   fNumber = 0
   while fNumber <= 0 :
      try:   
         fNumber = float(input(sPrompt)) 
      except ValueError:
         print("Input must a numeric value")
   return fNumber

fDeposit=float(input("What is your total deposit?:"))
fInterestRate=float(input("What is your interest rate?:")) / 100 / 12
iMonths=int(input("What is your number of months?:"))
fGoal = -1
while fGoal < 0:
   try:
      fGoal = float(input("Enter Goal: "))  
      print("Input must be a numeric value")



for month in range(1, iMonths + 1):

   fInterestAmount = fDeposit * fInterestRate

   fDeposit += fInterestAmount

   print( f"Month: {month} Account balance is: ${fDeposit:,.2f}" )


if fGoal == 0: 

   iMonths = 0


while fDeposit < fGoal:

   fInterestAmount = fDeposit * fInterestRate

   fDeposit += fInterestAmount

   iMonths += 1

print(f"It will take: {iMonths} to reach the goal of ${fGoal:,.2f}")
