from sys import argv

script, filename = argv

input_file = open(filename)
input_text = input_file.read()

#create an empty list
alpha_list = []

#initialize all elements of the list to 0
for i in range(0, 26):
    alpha_list[i:i] = [0]

for char in input_text:
    if char.isupper():      #convert Uppercase letters to lowercase and add to list
        char_lower = char.lower()
        alpha_list[ord(char_lower) - 97] += 1
    elif ord(char) >= 97 and ord(char) <= 122:  #if input char is between 'a' and 'z'
        alpha_list[ord(char) - 97] += 1
    else:                   #for all characters other than letters, pass on and move to next char
        pass

for i in range(0, 26):
    print alpha_list[i]




