# -*- coding: utf-8 -*-


#Capitalize
Introduction = "welcome to my code!"
Intro = Introduction.capitalize()
Intro.center(40)
print(Intro)


#Encoding
gibberish = "Here is some gibberish"
gibberish = gibberish.encode(encoding = 'ascii', errors="backslashreplace")
print(gibberish)

#Expand Tab
hallo = "H\te\tl\tl\to"
HELLLo =  hallo.expandtabs(7)
print(HELLLo)

#Input value for string
height = "I am a total of {price:.2f} inches tall!"
print(height.format(price = 99))

#Find index of instance
where = "Where is the first t?"
print(where.index("t"))

#Are all characters alphabets?
NotAlpha = "Are we @lphabets"
print(NotAlpha.isalpha())

#Are all characters decimals?
NotDigit = "123721732713"
print(NotDigit.isdigit())

Lowercase = "dfkjgkhsfgsdhjfghkdsgfkshgfkdshgfkhdsgfkdshgfkhdgfkhsgfkdhsgfkhdsgfkhdsgfksdhgf"
print(Lowercase.islower())


printable = "Hello!\nAre you #1?"
print(printable.isprintable())

isTitle = "Is This A Title"
print(isTitle.istitle())

Tuples = "John", "is", "great"
print(" ".join(Tuples) )

makeLower = "PLEASE MAKE ME LOWERCASE"
print(makeLower.lower())

SamisPam = "Hello Sam!"
print(SamisPam.maketrans("S", "P"))

replaceMe = "I like cats"
print(replaceMe.replace("cats", "dogs"))

WhereIsGabe = "Let me know where Gabe is"
print(WhereIsGabe.rindex("Gabe"))

eatB = "I could eat bananas all day, bananas are my favorite fruit"
print(eatB.rpartition("bananas"))

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

print(txt.upper())
print(eatB.title())



