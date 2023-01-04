if __name__== "__main__":
       
    num_subsets = 0
    num_overlaps = 0
    with open("input.txt", "r") as f:
        for line in f:

            s1, s2 = line.split(",")
            s1_split = s1.split("-")
            s2_split = s2.split("-")

            s1 = set(range(int(s1_split[0]), int(s1_split[1])+1))
            s2 = set(range(int(s2_split[0]), int(s2_split[1])+1))

            if (s1.issubset(s2) or s2.issubset(s1)):
                num_subsets+=1

            for num in s1:
                if (num in s2):
                    num_overlaps+=1
                    break
        
    print(f"part 1 answer: {num_subsets} ")
    print(f"part 2 answer: {num_overlaps} ")
