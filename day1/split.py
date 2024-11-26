text =  "Hello/Everyone::hellou!"
splited=  text.split("/")
print(splited[1])
newtext =  splited[1].split("::")[1]
print(newtext)  # this is the program return only to display hellou!
