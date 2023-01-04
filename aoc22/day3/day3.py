from collections import Counter
import string

if __name__== "__main__":

    letters = string.ascii_letters
    vals = [i for i in range(1, len(letters)+1)]
    priorities = dict(zip(letters, vals))

       
    sum_priorities = 0
    with open("input.txt", "r") as f:

        for line in f:

            l = len(line)

            c1 = line[:l//2]
            c2 = line[l//2:]

            searched = []
            for char in c1: 
                if (char not in searched and char in c2):
                    sum_priorities+= priorities[char]

                searched.append(char)

    f.close()

    with open("input.txt", "r") as f:
        all_lines = f.readlines()

    f.close()

    all_lines = [x.strip() for x in all_lines]
    sp2 = 0
    for i in range(0, len(all_lines)-2, 3):

        one = ''.join(set(all_lines[i]))
        two = ''.join(set(all_lines[i+1]))
        three = ''.join(set(all_lines[i+2]))
        
        triad = one + two + three
        count_dict = Counter(triad)

        for key, val in count_dict.items():
            if (val == 3):
                sp2+= priorities[key]
        #print(f"count_dict: {dict(count_dict)} ")

    print(f"part one answer: {sum_priorities} ")
    print(f"part two answer: {sp2} ")


