num = int(input("Enter a number  : "))

n = num 
sum = 0 


while n > 0:
    d = 0 
    d = n%10
    sum += d 
    n = n // 10 
print(f"sum of digit of {num} is {sum}")