num = list(map(int,input("enter a number:").split()))
large_num=num[0]
small_num=num[0]
for i in range(len(num)):
    if num[i]>large_num:
        large_num=num[i]
    if num[i]<small_num:
        small_num=num[i]
print("large_num=",large_num)
print("small_num=",small_num)
