from functools import cmp_to_key
from helpers import fewest_greens, fewest_yellows, leftmost_clue
import os

# CONSTANTS
THRESHOLD = 300  # Abandon branch if first guess returns a bucket larger than this

# with open('wordle-allowed-guesses.txt') as f:
with open("wordlists/wordle_answers.txt") as f:
    allowed_guesses = [a.strip() for a in f.readlines()]
with open("wordlists/wordle_answers.txt") as f:
    answers = [a.strip() for a in f.readlines()]


def get_response(guess, answer):
    answer = list(answer)
    response = []
    for index, char in enumerate(list(guess)):
        if char == answer[index]:
            response.append("🟩")
        elif char in answer:
            response.append("🟨")
        else:
            response.append("⬛")
    return "".join(response)


def put_answers_into_buckets(guess, answers=answers):
    buckets = {}
    for ans in answers:
        response = get_response(guess, ans)
        if response in buckets:
            buckets[response].append(ans)
        else:
            buckets[response] = [ans]
    return buckets


def sort_buckets(buckets):
    def bucket_compare(bucket1, bucket2):
        # Compare size of buckets
        if len(bucket1[1]) > len(bucket2[1]):
            return 1
        elif len(bucket2[1]) > len(bucket1[1]):
            return -1
        # Tied, so check fewest greens
        g = fewest_greens(bucket1[0], bucket2[0])
        if g == 1 or g == -1:
            return g
        # Tied still, so check fewest yellows
        y = fewest_yellows(bucket1[0], bucket2[0])
        if y == 1 or y == -1:
            return y
        # Still tied, so check left-most clue
        return leftmost_clue(bucket1[0], bucket2[0])

    return sorted(buckets.items(), key=cmp_to_key(bucket_compare), reverse=True)


def search(guess_list, answers=answers, current_chain=[]):
    if len(current_chain) > 2:
        # print("Abandoning branch:", current_chain)
        return
    # print("Starting new search...")
    # print("Current chain:", current_chain)
    # print("Possible answers", answers)
    for word in guess_list:
        if len(current_chain) < 1:
            print("Trying: ", word)
        response, new_answers = sort_buckets(put_answers_into_buckets(word, answers))[0]
        if len(new_answers) > THRESHOLD:
            continue
        # print("New answers", new_answers)
        if len(new_answers) == 1:
            print("Solved!")
            current_chain.append(word)
            current_chain.append(new_answers[0])
            solutions.append(current_chain)
            f.write(", ".join(current_chain) + "\n")
            print(current_chain)
            return current_chain
        else:
            search(new_answers, new_answers, current_chain + [word])


if __name__ == "__main__":
    # print(get_response("fifty", "gypsy"))
    # print(len(put_answers_into_buckets("terns").keys()))
    # print(sort_buckets(put_answers_into_buckets("terns")))
    solutions = []
    f = open("solutions_wip.txt", "w")
    search(allowed_guesses)
    print("Done")
    f.close()
    try:
        os.remove("solutions.txt")
    except:
        pass
    os.rename("solutions_wip.txt", "solutions.txt")
    print(solutions)
