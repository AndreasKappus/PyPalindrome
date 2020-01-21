
print("Please input text: ")
text = input()

r_test = text[::-1]

if text == r_test:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
