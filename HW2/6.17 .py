User_pass = input()
New_pass= ''

for character in User_pass:
    if character == "i":
        New_pass+= ("!")

    elif character == "a":
        New_pass+= ("@")

    elif character == "m":
        New_pass+= ("M")

    elif character == "B":
        New_pass+= ('8')

    elif character == "o":
        New_pass+= (".")

    else:
        New_pass+= character
print(New_pass + 'q*s')
