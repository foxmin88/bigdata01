number = int(input())
count = 0
is_prime = True

if number >= 2:
    for i in range(2, number):
        if number % i == 0:
            count = count + 1
            is_prime = False
        print(i, end=" ")
else:
    count = 1
    is_prime = False

if count == 0:
    if is_prime:
        print(f"{number}는(은) 소수입니다.")
    else:
        print(f"{number}는(은) 소수가 아닙니다!")