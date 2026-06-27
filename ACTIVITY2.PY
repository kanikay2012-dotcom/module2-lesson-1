UNITS = int(input("PLEASE ENTER THE NUMBER OF UNITS YOU CONSUMED:"))
if(UNITS <50):
    amount = UNITS *2.60
    subcharge= 25
elif(UNITS<=100):
    amount = 130 + ((UNITS-50)*3.25)
    subcharge = 35
elif UNITS<=200:
    amount = 130 +162.50 +((UNITS-100)*5.26)
    subcharge = 45
else:
    amount = 130+162.50 +((UNITS-200)*8.45)
    subcharge = 75
TOTAL = amount+subcharge
print("/nElectricity Bill = %.2f "%TOTAL)