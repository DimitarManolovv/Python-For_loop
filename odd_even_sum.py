number = int(input())

chetna_suma=0
nechetna_suma=0

for chislo in range(1, number+1):
    current_number =int(input())
    if chislo % 2 == 0:
        chetna_suma = chetna_suma + current_number
    elif chislo % 2 != 0:
        nechetna_suma = nechetna_suma + current_number

if chetna_suma == nechetna_suma:
    print("Yes")
    print(f'Sum = {chetna_suma}')
elif chetna_suma != nechetna_suma:
    razlika = abs(chetna_suma-nechetna_suma)
    print("No")
    print(f'Diff = {razlika}')