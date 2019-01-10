#!/usr/bin/env python
Celsius = int(raw_input("Enter a Temperature in Degrees Celsius: "))
Fahrenheit = 9.0/5.0 * Celsius + 32
print "Temperature:", Celsius, " Degree Celsius = ", Fahrenheit, " Fahrenheit"
Fahrenheit=int(raw_input("Enter the Temperature in Degrees Fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5.0/9.0
print "Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, "C"