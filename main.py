#startup and instructions 
print("\nGreetings dear user,") 
print("\nHere are some tips that may be useful:-")
print("\n1.If you want to change the sequence of the password elements, just fill the questions according to your preferences and promptly ignore what the question states to enter (IMPORTANT)")
print("\n2.Please do not violate any terms of service, rules or any other policies of any website,application. This program is not liable for any violation of policies. ")

import random
import sys
print("\nn = number\nstr = string or alphabet(s)\nchar = character(s)")
#PASSFORMAT = str(input("\nEnter the format of your password eg n+a+c:")
STR1 = input("\nEnter Letter or Word:")
STR2 = input("\nSame letter or Word with first word or last or middle word capital or small else enter same word as before: ")

INT1 = input("\nenter a no:")
INT2 = input("\nenter another no.if no change enter the same previous no")
INT3 = input("\nenter another no.if no change enter the same previous no.")
INT4 = input("\nenter another no.if no change enter the same previous no.")
CHR1 = input("\nenter first character:")
CHR2 = input("\nenter second character.if no change, enter the same previous character:")
CHR3 = input("\nenter third character.if no change enter the same previous character:")
CHR4 = input("\nenter fourth character. if no change enter same previous character:")
Range = int(input("\n enter the number of passwords to be generated:"))

#forgotten characters/numbers
forgot1 = INT1 + CHR1
forgot2 = INT2 + CHR2
forgot3 = INT3 + CHR3
forgot4 = INT4 + CHR4

# length of the password 
#the number counts as one and sign counts as one and the word counts as one  so length = 3
length = 3

#display output with the remembered parts of the password.
for i in range (0,Range):
 password1 ="".join(random.sample(forgot1,length))
 password2 ="".join(random.sample(forgot2,length))
 password3 ="".join(random.sample(forgot3,length))
 password4 = "".join(random.sample(forgot4,length))
 print(STR1+password1)
 print(STR2+password1)
 print(STR1+password2)
 print(STR2+password2)
 print(STR1+password3)
 print(STR2+password3)
 print(STR1+password4)
 print(STR2+password4)
 print("------------")