a = int(input())
b = int(input())
if a < b:

    for s in range(a , b + 1 ):
        print(s, end= ';')
else:
    for s in range(a , b - 1, -1  ):
         print(s, end= ';')
    