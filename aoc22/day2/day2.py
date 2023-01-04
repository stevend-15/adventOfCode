if __name__== "__main__":

    outcome = {"AX": 3, "AY": 6, "AZ": 0, 
                "BX": 0, "BY": 3, "BZ": 6,
                "CX": 6, "CY": 0, "CZ": 3}

    my_action_score = {"X": 1, "Y": 2, "Z": 3}
    
    #pt2 rule: X means must lose, Y means must draw, Z means must win
    req_outcome = {"X": 0, "Y": 3, "Z": 6}

    s = 0
    s2 = 0

    with open("input.txt", "r") as f:
        for line in f: 

            line = line.strip()
            s+= outcome[line[0] + line[2]] + my_action_score[line[2]]

            for key, val in outcome.items():
                if (line[0] in key and outcome[key] == req_outcome[line[2]]):
                    s2+= my_action_score[key[1]] + outcome[key]
            
    f.close()

    print(f"sum: {s}\nsum2: {s2} ")
