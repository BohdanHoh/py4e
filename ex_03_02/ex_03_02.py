inputhours = input("How many hours per week: ")
inputrate = input("What is your rate per hour: ")

try:
    floathours = float(inputhours)
    floatrate = float(inputrate)
except:
    print('ERROR, please enter numeric input')
    quit()

if floathours <= 40:
    reg = floathours * floatrate
    print('Regular:',reg)
if floathours > 40:
    ot = (floathours - 40) * (floatrate * 1.5)
    reg = floathours * floatrate
    print('Regular:',reg)
    print('Overtime:',ot)
    print('Total:',(reg + ot))