'''if(condition):  ": - colon known for indenton default identation in 4spaces"
//statements'''
a=300
b=200
if(True):
    print(" a is true ")
    if(a>=b):
        print("nested if")
        if(a==300):
            print(a)
elif(a>b):
    print("condition is not true")
else:
    print("a is not true")
    print(a,b)
#if(condition): print("statem")
a=1
b=2
c=3
if(a<b): print(a)
if (a<b and a<c):
    print(" and comparision operator")
elif(b<c and b<a):
    printf(" and")
a=2
b=4
c=6
if(a<b or a<c):
    print(" or comp operator")
    if(a!=c or b!=c):
        print(" checkimg both operations")
else:
    print("statement")

# even and odd numbers
q=int(input("enter number:"))
if(q%2==0):
    print(q,"id a even number")
else:
    print(q,"is a odd number")


a="satyadeepu"
for i in a:
    print("for loop")
    print(a[0],a[1],a[2],a[3],a[4])

#forloop

#check=[string-"",'', integer 123]
check=["apple",48,"banana"]
print(type(check))
for i in check:
    print(check)
    if(i=="apple"):
        print(i)
    elif(i==48):
        print(i)
    elif(i=="banana"):
        print(i)
    else:
        print("not checked")

#range(0,1) ==> two paraemeters
for y in range(0,100,48):

    print(y ,end='')


#while loop
i=1
while(i<6):
    print(i,end='')
    if(i==6):
        i+=1
        break
a="satya"
while(len(a)<=6):
    print(a,end='')
    if(a<=4):
       break

#prime number without loops
