
fCelsius = 0
fFahrenheiht = 0

fTemp = float(input("Enter Temperature: "))

sChoice = input("Fahrenheiht (F) or Celsius (C): ").upper()


if sChoice != "F" and sChoice != "C":

    exit("Enter a F or C")

if sChoice == "F":

    if fTemp > 212:

        exit("Temp can not be > 212")

    fCelsius = (5.0 / 9) * (fTemp - 32)

    print(f"The Celsius equivalent is: {fCelsius:,.1f}")

if sChoice == "C":

    if fTemp > 100:

        exit("Temp can not be > 100")

    fFahrenheiht =  ((9.0 / 5.0) * fTemp ) + 32

    print(f"The Fahrenheit equivalent is: {fFahrenheiht:,.1f}")
