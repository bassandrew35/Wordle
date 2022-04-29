# Andrew Bass
# 4/19/22

five_file = open("five_letter_words.txt", "r")

bad_chars = ""
yellow_chars = [[],[],[],[],[]]
exact_chars = ["","","","",""]

keep_going = "y"

lines = five_file.readlines()

while keep_going == "y":
    print(" --------------------------- ")
    print("Grey Characters: ")
    for a in bad_chars:
        print(a, end=" ")
    print("")
    print("Enter Characters that are not included:")
    print("Ex. qwer\n-> ", end= "")
    user_in = input()
    if user_in:
        bad_chars = bad_chars + user_in
    
    print(" --------------------------- ")
    print("Yellow Characters: ")
    for a in yellow_chars:
        print(a, end=" ")
    print("")
    print("For yellow characters enter character then number then space then the next")
    print("Ex. s0 r2 a3")
    print("First character is 0 and last is 4\n-> ", end= "")
    user_in = input()
    if user_in:
        for a in user_in.split(' '):
            yellow_chars[int(a[1])].append(a[0])

    print(" --------------------------- ")
    print("Green Characters: ")
    for a in range(len(exact_chars)):
        print(a, ":", exact_chars[a], end="     ")
    print("")
    print("For exact match enter character then number then space then the next")
    print("Ex. s0 r2 a3")
    print("First character is 0 and last is 4\n-> ", end= "")
    user_in = input()
    if user_in:
        for a in user_in.split(' '):
            exact_chars[int(a[1])] = a[0]

    for a in lines:
        temp = a.strip()
        found = True
        for b in bad_chars:
            if b in temp:
                found = False
        for c in range(len(yellow_chars)):
            if yellow_chars[c] != []:
                for x in yellow_chars[c]:
                    if x not in temp or x == temp[c]:
                        found = False
        for d in range(len(exact_chars)):
            if exact_chars[d] != "":
                if exact_chars[d] != temp[d]:
                    found = False
        if found:
            print(temp)

    print(" --------------------------- ")
    print("Enter y to continue or anything else to quit:\n-> ", end= "")
    keep_going = input()
