#Python Temperature conversion program.
#F = (C*(9/5)) + 32
#K = 273.15 + C
#K = (F - 32) * (5/9) + 273.15

Temp_Value = float(input("Enter the value of your temperature: "))
Current_Unit = input("Enter the current unit of the temperature (F/C/K): ").capitalize()
Change_Unit = input("Enter the unit in which you want to change the temperature. (F/C/K): ").capitalize()

if Current_Unit == "C" and Change_Unit == "F":
    Result = (Temp_Value*(9/5)) + 32
    print(f"Result: {Result}")
elif Current_Unit == "C" and Change_Unit == "K":
    Result = 273.15 + Temp_Value
    print(f"Result: {Result}")

if Current_Unit == "F" and Change_Unit == "C":
    Result = (Temp_Value - 32) * (5/9)
    print(f"Result: {Result}")
elif Current_Unit == "F" and Change_Unit == "K":
    Result = (Temp_Value - 32) * (5/9) + 273.15
    print(f"Result: {Result}")

if Current_Unit == "K" and Change_Unit == "C":
    Result = Temp_Value - 273.15
    print(f"Result: {Result}")
elif Current_Unit == "K" and Change_Unit == "F":
    Result = (Temp_Value - 273.15) * (9/5) + 32 

if Current_Unit == Change_Unit:
    print(f"Result: {Temp_Value}")