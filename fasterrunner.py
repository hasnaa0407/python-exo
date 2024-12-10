while(1==1) :
    print("Runner 1")
    name1=input("name :")
    time1=float(input("Time (in seconds):"))
    print("Runner 2")
    name2=input("name :")
    time2=float(input("Time (in seconds):"))
    if time1<time2:
        print("The faster runner is",name1)
    else :
        if time1>time2:
            print("The faster runner is",2)
        else :
            print(name1,"and",name2,"have the same time")