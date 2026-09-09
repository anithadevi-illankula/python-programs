num = list(map(int, input("Enter numbers: ").split()))

even_sum = 0
odd_sum = 0

for i in num:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("even_sum =", even_sum)
print("odd_sum =", odd_sum)
