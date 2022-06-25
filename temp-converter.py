for tempconversions in range(3):
    inputCelsiusString = input("Enter the temperature in C: ")
    tempInc = float(inputCelsiusString)
    tempInF = 1.8 * tempInc + 32
    print( "The temperature in F is", tempInF, "degrees" )