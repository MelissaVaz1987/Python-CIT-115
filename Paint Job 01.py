
fPainting_Labor_charge_per_hour = getFloatInput("Painting Labor charge per hour: ")

   sState = input("Enter State: ")
   sName = input("Enter Last Name: ")

   iGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
   #print(iGallons)

   fLaborHours = getLaborHours(fLaborHoursPerGallons, iGallons)
   #print(fLaborHours)

   fLaborCost = getLaborCost(fLaborHoursPerGallons, fPainting_Labor_charge_per_hour) * iGallons
   #print(fLaborCost)

   fPaintCost = getPaintCost(iGallons, fPaintPrice)
   #print(fPaintCost)

   fTaxRate = getSalesTax(sState)
   #print(fTaxRate)

   fTaxAmount = (fPaintCost + fLaborCost) * fTaxRate
   #print(fTaxAmount)

   fTotal = fPaintCost + fLaborCost + fTaxAmount
   #print(fTotal)

   showCostEstimate(iGallons, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotal)

   with open(f"{sName}_PaintJobOutput.txt", "w") as file:

      file.write(f"Customer Name: {sName}\n")

      file.write(f"Gallons of paint: {str(iGallons)}\n")
      file.write(f"Labor hours: {str(fLaborHours)}\n")

      sPaintCost = str(f"{fPaintCost:,.2f}")
      file.write(f"Paint cost: ${sPaintCost}\n")

      sLaborCost = str(f"{fLaborCost:,.2f}")
      file.write(f"Labour cost: ${sLaborCost}\n")

      sTaxAmount = str(f"{fTaxAmount:,.2f}")
      file.write(f"Tax Amount: ${sTaxAmount}\n")

      sTotal = str(f"{fTotal:,.2f}")
      file.write(f"Total: ${sTotal}\n")

   print(f"File {sName}_PaintJobOutput.txt was created")

main()
