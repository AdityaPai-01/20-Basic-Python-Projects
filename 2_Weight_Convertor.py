#Python Weight Convertor
#Converts Kg to Lbs and vice versa
#1 Kg = 2.20462 lbs
#1 lbs = 0.45359237 kg

Weight_Value = float(input("What is the weight value?: "))
Current_unit = input("What is the current unit of your weight? (K- Kg/P- Lbs): ").capitalize()
Change_unit = input("In which unit would you like to change the weight?(K- Kg/P- Lbs): ").capitalize()

if Current_unit == 'K' and Change_unit == 'P':
    Result = Weight_Value * 2.20462
    print(f"{Weight_Value} Kilograms in pounds is {Result} Lbs")
elif Current_unit == 'P' and Change_unit == 'K':
    Result = Weight_Value * 0.45359237
    print(f"{Weight_Value} pounds in kilograms is {Result} kgs")
else:
    print("Coud not perform calculations. Units are the same.")