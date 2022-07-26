'''from random import randint
for i in range(2):
    print(randint(1,2), end='')'''

#from a.b import c
'''import math
result=math.e !=math.pow(2,4)
print(int(result))'''




class A:
    def _str_(self):
        return 'a'
class B:
    def _str_(self):
        return 'b'
class C(B):
    pass 
o=C()
print(o)

'''class A:
    v=2
class B(A):
    v=1
class C(B):
    pass
o=C()
print(o.v)'''