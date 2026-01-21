import re
cadena = "Mi DNI es 54323495G y en minúsculas es 98723495g"
exp = r'\d{8}[A-Z]'
print(re.sub(exp, '...', cadena, flags=re.RegexFlag.I)) # Mi DNI es ... y en minúsculas es ...

exp = r'(\d{3})(\d{5})([A-Z])'
print(re.sub(exp, r'\1...\3', cadena, flags=re.RegexFlag.I)) # Mi DNI es 543...G y en minúsculas es 987...g


cadena = "Juan Pérez Martínez"
exp = r'(\w+) (\w+) (\w+)'
print(re.sub(exp, r'\2 \3, \1', cadena)) # Pérez Martínez, Juan

cadena = "Juan Pérez Martínez"
exp = r'(?P<nombre>\w+) (?P<ap1>\w+) (?P<ap2>\w+)'
print(re.sub(exp, r'\g<ap1> \g<ap2>, \g<nombre>', cadena)) # Pérez Martínez, Juan

def suma_nums(m: re.Match[str]) -> str: # funcion de reemplazo que suma los dígitos y los devuelve como cadena
    return str(sum([int(n) for n in m.group(0)]))

cadena = "3425345, 6457567, 324654, 54637345"
exp = "\d+"
res = re.sub(exp, suma_nums, cadena)
print(res) # 26, 40, 24, 37
res = re.sub(exp, lambda m: str(sum([int(n) for n in m.group(0)])), cadena)
print(res) # 26, 40, 24, 37