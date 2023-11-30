x=(input("enter the number of days:,x"))
y=(input("enter the number of month:,y"))
z=(input("enter the number of year:,z"))


if("x>30"):
    print("invalid date:x")
    if("y>12"):
        print("invalid month:y")
        if("z>99"):
            print("invalid year:z")
            if("y==2"):
                if("z%4==0"):
                    print("rsult")
                elif("x>29"):
                    print("invalid date")
                    print(x,"/",y,"/",z)
                
                    

                    
                        

