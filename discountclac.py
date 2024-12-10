while 1==1 :
    total1=int(input("Total amount :"))
    nbitem=int(input("Number of items :"))
    print("sunday=1,monday=2,thursday=3,wednesday=4,tuesday=5,friday=6,saturday=7")
    day=int(input("day of the week :"))
    if(nbitem>=5):
        discount=0.05
    else:
        discount=0
    if(day==1| day==6):
        discount=+0.2
    else:
        discount=+0.1

    total2=total1-discount*total1
    print("Total price after discount:", total2,"dinars")
