p = int(input())
d = -1
o = 0
while p != d:
    d = int(input())
    
    if p != d:
        o = o + 1
        if o == 3:
            print('Ничего страшного, все ваши деньги забрал Греф!')
            break
if  p == d:   
    print('Добро пожаловать!')
    
