#functons in python proramming
#create afuction

#invok functon created

#1. possitional function ==> Indexbased Arguments
def satya(u,y,x):
    print(u+y)
    print(u+x)
satya("satya","deepu", "mandapati")

#keyword arguments
def satya(name3,name2,name1):
    print("who is the best actor in wrld?"+ name1 + "" + name2 + "" + name3)
    select=int(input("1.sachin te \n 2.alien \n 3.brianlara"))
    if(select==1):
        print("best cricketer in worls is"+name1)
    elif(select==2):
        print("est cricketer in world is"+name2)
    elif(select==3):
        print("best cricjter in world is"+name3)
   satya(name1="sachin te",name2="alien",name3="brianlara")

 #arbitary keywor adrguments
 #when we doesnt know how many arguments are needed

def white(**sachin):
     print(" india is acilture nation"+sachin["name1"]+sachin["name2"])

white(name1="and clourful",name2="with rich heritage")

def evenodd(num):
    num=int(input("enter a number"))
    if(num%2==0):
        print("this is even number")
    else:
        print("this is a odd number")
evenodd(100)

#inovoke functions
def green(favplace="bhimavaram"):
    print("my fav place is " + favplace)
green("bondada")
green("goa")

#index operator [start,end,step]

st=["msd","mdk"]
print(st[0],st[1],st[-1],st[-2],st[0:2])



