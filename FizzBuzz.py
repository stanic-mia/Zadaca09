
broj = int(input("Molim Vas unesite jedan broj od 1 do 100: "))

i = 1

while i <= broj:
    if (i % 3) == 0 and (i % 5) == 0:
        print("fizzbuzz")
    elif (i % 3) == 0:
        print("fizz")
    elif (i % 5) == 0:
        print("buzz")
    else:
        print(i)
    i += 1


