a = int(input())
e = int(input())
if a == admin or a == user:
    if e == 1234 :
        print('success')
    else:
        print('wrong password')
if a != admin and a != user:
     print('wrong login')