greeting = "Hello"
name = "Python"
fullText = greeting + " " +name +" !"
languages = ["Python", "Java", "C++", "JavaScript", "C#"]
numbers = [1,2,3,4,5]

# Concatenation :
print(f"{greeting} + {name} = {fullText}")
    # From list to string
print(" Liste ow languages : ",languages)
print("Joined string (Separator is ,) : ",", ".join(languages) )
print("Joined string (Separator is *) : ","* ".join(languages) )
print("Joined string (Separator is ' ') : "," ".join(languages) )
    # Using for
result = ""
for num in numbers:
    result += str(num)
print("Liste Numbers : ",numbers)
print("Concatened result : ",result)

# Upper, Lower, Strip functions
print(f"Upper case : {fullText.upper()}")
print(f"Lower case : {fullText.lower()}")
print(f"Title case : {fullText.title()}")
print(f"Stripped text : {fullText.strip()}")

#Author functions for string
print("Find world in sentence :","Python" in fullText)
print("Length of text : ",len(fullText))

# Slicing string
print("Original text : ", fullText)
print("Sliced text : ",fullText[6:12])
print("Substring 1 : ",fullText[0:5])
print("Substring 2 : ",fullText[:5])
print("Substring 3 : ",fullText[6:])
print("Last three characters : ",fullText[-3:])

# Modify string 
modiedText = fullText.replace("Python","World")
print("Original Taxt : ",fullText)
print("Modified Text : ",modiedText)
