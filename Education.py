Name=str(input("Your Name Please"))
Age=int(input("Age Please"))
Education=str(input("education info please"))
Education2=("primary,Middle,Highschool, Collage")

if Education not in Education2:
    print("Please give a valid education input")
elif (Age>=18) and (Education=="Highschool" or Education=="Collage"):
    print("driving lis applied")
else:
    print("driing lis not applicable")