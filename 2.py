color1=input("enter the color1")
color2=input("enter the color2")

if(color1=="red" or color1=="blue" or color1=="yellow"):
    print("blue,purple,yellow")
else:
    print("blue,purple,yellow")

if(color2=="red" or color2=="blue" or color2=="yellow"):
    print("invalid color")
else:
    print("invalid color")
    if(color1==color2):
         print("invalid color")


if(color1=="red"):
    if(color2=="yellow"):
        print("orange")

        if(color1=="red"):
            print("yellow")

if(color1=="red"):
    if(color2=="yellow"):
        print("orange")

        if(color1=="red"):
            if(color2=="blue"):
             print("purple")

if(color1=="blue"):
    if(color2=="yellow"):
        print("green")
        
