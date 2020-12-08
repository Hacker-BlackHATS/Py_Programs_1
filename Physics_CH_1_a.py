# CONSTANTS
G = 6.67*(10**(-11))
E = 8.85*(10**(-12))
# noinspection NonAsciiCharacters
π = 3.141592654
########################################

print("Gravitational Force")
m1 = int(input("Enter mass of object 1 (in kg) : "))
m2 = int(input("Enter mass of object 2 (in kg) : "))
r = int(input("Enter distance between their centers : "))

F = G*m1*m2/(r**2)
print(f" => {F} kg\u00b2/m\u00b2")

print("Electrostatic Force")
q1 = int(input("Enter charge of object 1 (in coulomb) : "))
q2 = int(input("Enter charge of object 2 (in coulomb) : "))
r = int(input("Enter distance between their centers : "))
C = 1/(4*π*E)
F = C*q1*q2/(r**2)
print(f" => {F} C\u00b2/m\u00b2")