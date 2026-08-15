# weight= int(input("enter your weight:"))
# ch=input("is it in 1)kg or 2)lbs: ")
# if ch=="kg":
#  val= weight* 2.20462
#  print(val)
# else:
#  val=weight/2.20462
#  print(val)


# print   ("welcome to calorie counter !")
# weight=int(input("plaease enter your weight in kgs: "))
# time=int(input("enter the amount of time you have workedout: "))
# if time==0:
#     print("time cant be 0mins")
# else:
#  print("enter number <3 else the result will not be printed")
#  ch=int(input("enter the choice 1.cardio 2.weight-liftng: "))
# if ch==1:
#     cal=round(0.105*weight*time,2)
#     print(f"the calories burnt are {cal}cal, in {time}mins")
# elif ch== 2:
#     cal=round(0.07875*weight*time,2)
#     print(f"the calories burnt are {cal}cal, in {time}mins")


enrg=int(input("what are your energy levels?"))
slp=int(input("how many hours did you sleep last night?"))
eat=(input("have you eaten in last 3 hrs(y/n)?"))


if slp<4 and eat=="n":
    print("dont go for intenense workout.")
elif enrg>9 or slp>6 and eat=="y":
    print("you can go for intense workout.")
else:
    print("not cleared — try a lighter workout instead")