number = int(input())

total_left_colum=0
total_right_colum=0

for nums in range(number):
    left_column_number=int(input())
    total_left_colum=total_left_colum+left_column_number

for rightnums in range(number):
    right_column_number=int(input())
    total_right_colum=total_right_colum+right_column_number

if total_left_colum == total_right_colum:
    print(f'Yes, sum = {total_left_colum}')
elif total_left_colum != total_right_colum:
    razlika =abs(total_left_colum - total_right_colum)
    print(f'No, diff = {razlika}')