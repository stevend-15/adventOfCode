if __name__== "__main__":

    part = input("To which part would you like the answer? (1 or 2): ")

    with open("input.txt", "r") as f:
        s = f.read()

    f.close()
    
    counter = 4
    if (part == '2'):
        counter = 14

    for i in range(counter, len(s)):
        sliced = s[i-counter:i]

        if (len(sliced)==len(set(sliced))):
            print(f"found marker at position {i}. Val: {s[i]} ")
            break

    

