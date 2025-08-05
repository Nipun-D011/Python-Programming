name , age , score = "Kamal", 22 , 43.5657
#1st Method
# He is Kamal. He is 22 years old, and his score is 43.5657
"""print("He is "+name + ". He is "+str(age)+" years old, and his score is "+str(score))"""

#2nd Method
# He is Kamal. He is 22 years old, and his score is 43.5657
"""print("He is %s.He is %d years old, and his score is %.4f" %(name,age,score) )"""

#3rd Method
# He is Kamal. He is 22 years old, and his score is 43.5657
print("He is {}.He is {} years old, and his score is {}".format(name,age,score))


