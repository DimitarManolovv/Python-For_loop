n = int(input())
starting_points = int(input())
total_points = starting_points
total_wins = 0

for i in range(n):
    result = input()
    if result == "W":
        total_points += 2000
        total_wins += 1
    elif result == "F":
        total_points += 1200
    elif result == "SF":
        total_points += 720

average_points = int(total_points / n)
win_percentage = total_wins / n * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")
