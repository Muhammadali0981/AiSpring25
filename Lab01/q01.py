# Practice task 

y = int(input("Enter dividend: "))
x = int(input("Enter divisor: "))
ans = 0
while y > x:
    y -= x
    ans += 1

print(f'Answer is {ans} remainder is {y}')