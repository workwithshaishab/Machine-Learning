

import math
x = 16
y = 7.5
z = -10

print("--- Basic Math Functions ---")
print("Ceil of y:", math.ceil(y))       # Smallest integer >= y
print("Floor of y:", math.floor(y))     # Largest integer <= y
print("Round y:", round(y))             # Normal rounding
print("Absolute of z:", math.fabs(z))   # Absolute value
print("Factorial of 5:", math.factorial(5))
print("Greatest Common Divisor (gcd):", math.gcd(24, 36))
print("Remainder (fmod):", math.fmod(20, 6))

print("\n--- Power and Roots ---")
print("Square root of x:", math.sqrt(x))
print("Power (2^3):", math.pow(2, 3))
print("Exponent (e^2):", math.exp(2))
print("Log base e of x:", math.log(x))
print("Log base 10 of x:", math.log10(x))
print("Log base 2 of x:", math.log2(x))

print("\n--- Trigonometric Functions ---")
angle = math.radians(30)   # Convert 30° to radians
print("sin(30°):", math.sin(angle))
print("cos(30°):", math.cos(angle))
print("tan(30°):", math.tan(angle))

print("\n--- Inverse Trigonometric ---")
print("asin(0.5):", math.degrees(math.asin(0.5)))  # back to degrees
print("acos(0.5):", math.degrees(math.acos(0.5)))
print("atan(1):", math.degrees(math.atan(1)))

print("\n--- Other Useful Functions ---")
print("Degrees from radians (π):", math.degrees(math.pi))
print("Radians from degrees (180):", math.radians(180))
print("Truncate y:", math.trunc(y))   # Remove decimal part
print("Modf(y):", math.modf(y))       # Splits into (fractional, integer)

print("\n--- Constants ---")
print("PI:", math.pi)
print("Euler's Number (e):", math.e)
print("Tau (2π):", math.tau)
print("Infinity:", math.inf)
print("NaN:", math.nan)
