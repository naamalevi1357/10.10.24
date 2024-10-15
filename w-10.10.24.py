# start
import random

a: list[bool] = [True, True, False]
print(a)
ab: list[bool] = [random.choice([True, True, False])]
print(ab)
# b:
print(all(a))
# c:
print(any(a))
# d:
if not all(a):
    print("boom ")
else:
    print(" not boom")
# e:
if not any(a):
    print("good ")
else:
    print("not good")

# f:
f: list[int] = [random.randint( -2,-1,0,1,2)]
for i in f:
    f.append(random.randint(f))
print(f)
# g:
if all(f) != 0:
    print("ok")
# else:
#     print(" not ok")
# h:
if any(f) != 0:
    print("no zero")
# i:

if all(f) == 0:
    print(" all zero")
else:
    print(" any  zero ")
# j:
# if any([f == 0]):
#     print("One zero exists")
# else:
#     print("Zero does not exist")
# for x in f:
#     if any(x)==0:
#        print("exelent")
print(any([x == 0 for x in f]))
# stop


