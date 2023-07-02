main_tank = 5
additional_tank = 10
#A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.
#The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.
#Return the maximum distance which can be traveled.
#Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.

#bad, all-at-once solution (fails at edge cases)
burned = 0
#refuel_needed = (main_tank // 5 liters) * 1 liter
refuel_needed = (main_tank // 5)
if main_tank >= 5 and refuel_needed <= additional_tank:
    burned = main_tank + refuel_needed + 1
elif main_tank >= 5 and refuel_needed > additional_tank:
    burned = main_tank + additional_tank
else: burned = main_tank
print(burned)

#good, linear solution (aka "storytime")
mileage = 0
while main_tank:
    if main_tank >= 5:
        mileage += 5 * 10
        main_tank -= 5
        if additional_tank:
            main_tank += 1
            additional_tank -= 1
    else:
        mileage += main_tank * 10
        break
print(mileage)