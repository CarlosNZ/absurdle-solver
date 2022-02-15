def fewest_greens(response1, response2):
    greens1 = len(response1.replace("🟨", "").replace("⬛", ""))
    greens2 = len(response2.replace("🟨", "").replace("⬛", ""))
    if greens1 < greens2:
        return 1
    elif greens2 < greens1:
        return -1
    else:
        return 0

def fewest_yellows(response1, response2):
        yellows1 = len(response1.replace("🟩", "").replace("⬛", ""))
        yellows2 = len(response2.replace("🟩", "").replace("⬛", ""))
        if yellows1 < yellows2:
            return 1
        elif yellows2 < yellows1:
            return -1
        else:
            return 0

def leftmost_clue(response1, response2):
    index1_green = 99
    index1_yellow = 99
    index2_green =99
    index2_yellow = 99
    try:
        index1_green = response1.index("🟩")
    except:
        pass
    try:
        index1_yellow = response1.index("🟨")
    except:
        pass
    first_clue_1 = min(index1_green, index1_yellow)
    try:
        index2_green = response1.index("🟩")
    except:
        pass
    try:
        index2_yellow = response1.index("🟨")
    except:
        pass
    first_clue_2 = min(index2_green, index2_yellow)
    if first_clue_1 < first_clue_2:
        return 1
    elif first_clue_2 < first_clue_1:
        return -1
    else:
        return 0