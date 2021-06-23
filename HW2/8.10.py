user_input = input()
normal = user_input
reverse =user_input[::-1]
if normal == reverse:
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")
