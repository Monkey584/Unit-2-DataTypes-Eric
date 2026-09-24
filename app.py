""" x = 3
y = float(3)
print(x,y) """


""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """


""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)
 """


""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """


""" def count_words(sentance):
    words = sentance.split()
    return len(words)

user_sentance = input()
word_count = count_words(user_sentance)
print(f"{word_count}") """


""" bill = input("How much was the bill")
print(int(bill) + 20) """


""" def Number(value):
    return int(value)

user_value = input()
x = Number(user_value)
if x % 2 == 1:
    print("odd")
else:
    print("even") """
#or
""" def number(x):
 if x % 2 == 1:
     return "odd"
 else:
     return "even"

x = int(input("enter a number: "))
print(f"Your number is {number(x)}.") """


""" def service(x):
    if x == "great":
        return "25%"
    elif x == "good":
        return "20%"
    elif x == "okay":
        return "15%"
    elif x == "bad":
        return "0%"
    else:
        return "invalid"

x = input("How was the service: ")
print(f"{service(x)}") """


""" def factor(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

number = int(input("Enter a number: "))
print(factor(number)) """


def factor(x, y):
    GCF = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0:
            if y % i == 0:
                GCF.append(i)
    return GCF

numbers = input("Enter 2 numbers separated by a space: ").split()
x, y = int(numbers[0]), int(numbers[1])
print(factor(x, y))