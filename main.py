# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

combine_name = lower_name1 + lower_name2

T = combine_name.count("t")
R = combine_name.count("r")
U = combine_name.count("u")
E = combine_name.count("e")

true_combine = T + R + U + E

L = combine_name.count("l")
O = combine_name.count("o")
V = combine_name.count("v")
E = combine_name.count("e")

love_combine = L + O + V + E

true_str = str(true_combine)
love_str = str(love_combine)

total_love1 = (true_str) + (love_str)
total_love = int(total_love1)

if total_love < 10 :
    print(f"Your score is {total_love}, you go together like coke and  mentos.")

elif total_love > 90 :
      print(f"Your score is{total_love}, you go together like coke and    mentos.")

elif (total_love >= 40 ) or  (total_love <= 50 ):
    print(f"Your score is {total_love}, you are alright together.")
else :
    print("Your score is {total_love}.")

print("THANK YOU FOR PARTICIPATING")


