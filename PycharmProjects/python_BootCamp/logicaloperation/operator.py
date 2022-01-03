a = int(input("Provide the value of A"))
b = int(input("Provide the value of B"))

c = input("What you want to do with the a and B[add/sub/multiply/divide/modulas/exponent]")


if c == 'add':
    d = a + b
    print(d)
elif c == 'sub':
    d = a-b
    print(d)
elif c == 'multiply':
    d = a*b
    print(d)
elif c == 'divide':
    d = a/b
    print(d)
elif c == 'modulas':
    d = a%b
    print(d)
elif c == 'exponent':
    d = a**b
    print(d)
elif c == 'Floor':
    d = a//b
    print(d)
else:
    print('The operator provded is wrong')

