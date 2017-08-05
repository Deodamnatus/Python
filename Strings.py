
#interpolation way to do it
name=input("What is your name?\n")
welcome=f"\nNice to meet you {name}, how are you?"

#also you can do multi line comments with tripple quotes
"""format function way to do it"""
machine="Zebra"
machine=machine.lower()
feeling="great"
greet="I am {0} and I am feeling {1}!".format(machine, feeling)

"""
Some miscelanious string functions and their uses
"hello".capitalize()=="Hello"
"hello".replace("e","a")=="hallo"
"hello".isalpha() == True checks that there are no numbers
"123".isdigit()==True useful when converting strings to ints
"a,b,c,d".split(",") == ["a", "b", "c", "d"] useful when imputing lists
"""
print(welcome, greet)