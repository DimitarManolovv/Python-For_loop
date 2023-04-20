groups_count = int(input())
musala_count = 0
monblan_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0

for i in range(groups_count):
    group_size = int(input())
    if group_size <= 5:
        musala_count += group_size
    elif group_size <= 12:
        monblan_count += group_size
    elif group_size <= 25:
        kilimandjaro_count += group_size
    elif group_size <= 40:
        k2_count += group_size
    else:
        everest_count += group_size

total_count = musala_count + monblan_count + kilimandjaro_count + k2_count + everest_count

musala_percent = (musala_count / total_count) * 100
monblan_percent = (monblan_count / total_count) * 100
kilimandjaro_percent = (kilimandjaro_count / total_count) * 100
k2_percent = (k2_count / total_count) * 100
everest_percent = (everest_count / total_count) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
