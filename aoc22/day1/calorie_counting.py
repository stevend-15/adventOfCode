import time

if __name__== "__main__":

    greatest = 0
    top_3 = [0,0,0]

    s = 0
    with open("input.txt", "r") as f:
        while True:

            line = f.readline()

            if (line == "\n" or not line):
                smallest = min(top_3)

                if (s > smallest):
                    index = top_3.index(smallest)

                    top_3[index] = s
                    s = 0
                    continue

                if (not line):
                    print(f"EOF ")
                    break

                s=0
                continue

            s += int(line.strip())

    f.close()
    print(f"greatest: {max(top_3)} ")
    print(f" top_3: {top_3} ")
    print(f"sum(top_3): {sum(top_3)} ")
       
