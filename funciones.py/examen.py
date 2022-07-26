'''a=1
b=0
a=a^b
b=a^b
a=a^b
print(a,b)'''


# lst=[i for i in range(-1,-2)]'
# print(lst)
'''a=1//2
print(a)'''

'''nums=[1,2,3]
vals=nums
del vals[:]'''

'''x=1//5+1/5
print(x)'''


'''lst=[[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst [r][c] %2!=0:
            print('#')'''

'''try:
    print(5/0)
    break
except:
    print('lo siento, algo salio mal...')
except (ValueError, ZeroDivisionError)
    print('mala suerte')'''


'''def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))'''

'''def func(a,b):
    return b**a
print(func(b=2,2))'''

'''def ja (a):
    return None
def jaa(a):
    return ja(a)* ja(a)
print(jaa(2))'''

'''tup=(1,2,4,8)
tup=tup[-2:-1]
tup=tup[-1]
print(tup)'''

'''i=0
while i<i+2:
    i+=1
    print('*')
else:
    print('*')'''

'''z=0
y=10
x= y<z and z>y or y>z and z<y
print(x)'''

'''x=1
y=2
x,y,z=x,x,y
z,y,z=x,y,z
print(x,y,z)'''


'''x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)'''

'''foo=(1,2,3)
#foo.index(0)
print(foo.index(0))'''

'''print('a','b','c', sep='sep')'''
y=input(3)
x=input(6)
print(x+y)

''''def fun(a,b,c=0):
    #fun()
    #fun(b=1)
    #fun(0,1,2)
    fun(b=0, a=0)'''


'''dd={'1': '0', '0': '1'}
for x in dd.vals():
    print(x,end='')'''

'''my=[x*x for x in range(5)]
def fun(lst):
    del lst [lst[2]]
    return lst
print(fun(my))'''


'''def fun(inp=2, out=3):
    return inp*out
print(fun(out=2))'''

'''def fun(x,y):
    if x==y:
        return x
    else:
        return fun(x,y-1)
print(fun(0,3))'''

'''x=float(input(2))
y=float(input(4))
print(y**(1/x))'''

'''print(!,hola,mundo!)'''


'''try:
    Value=input('Ingrese un valor:')
    print(int(value)/len(value))
except ValueError:
    print('Entrada incorrecta....')
except ZeroDivisionError:
    print('Entrada erronea....')
except TypeError:
    print('Entrada my erronea....')
except:
    print('Buuuu.....')'''

'''dct={'one':'two', 'three':'one','two': 'three' }
v=dct['three']
for k in range(len(dct)):
    v=dct[v]    
print(v)'''
'''except ( TypeErro, ValueError, ZeroDivisionError):'''
