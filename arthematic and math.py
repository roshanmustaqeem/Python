import math
steps=int(input("enter the number of steps walked: "))
dis= steps*0.0008
total=math.floor(dis*100)/100
print(f"the ditance in km is: {total}")

# rad=float(input("enter the radius of the circle"))
# cir=2*math.pi*rad
# print(f"the circumference is{round(cir,2)}")
 
# rad=float(input("enter the radius of the circle"))
# area= math.pi*pow(rad,2)
# print(f"enter the area of the circle{round(area,2)}")
 
a=float(input("enter the value of a:" ))
b=float(input("enter the value of b:" ))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"the hypotenouis is{round(c,2)}")