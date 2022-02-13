from functools import cmp_to_key

# with open('wordle-allowed-guesses.txt') as f:
with open('testing-list.txt') as f:
    allowed_guesses = [a.strip() for a in f.readlines()]
with open('wordle-answers-alphabetical.txt') as f:
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
    return ''.join(response)


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
    def most_greens(item1, item2):
        greens1 = len(item1[0].replace("🟨", "").replace("⬛", ""))
        greens2 = len(item2[0].replace("🟨", "").replace("⬛", ""))
        if greens1 > greens2:
            return 1
        elif greens2 > greens1:
            return -1
        else:
            return 0
    
    def most_greens(item1, item2):
        yellows1 = len(item1[0].replace("🟩", "").replace("⬛", ""))
        yellows2 = len(item2[0].replace("🟩", "").replace("⬛", ""))
        if yellows1 > yellows2:
            return 1
        elif yellows2 > yellows1:
            return -1
        else:
            return 0

    def leftmost_clue(item1, item2):
        index1 = item1[0].find()
    


    # def bucket_compare(item1, item2):
    #     if len(item1[1]) > len(item2[1]):
    #         return 1
    #     elif len(item2[1]) > len(item1[1]):
    #         return -1
    #     else:
    #         # Check which has most greens
    #         if len(item1[0].replace("🟨", "").replace("⬛", "")) > len(item2[0].replace("🟨", "").replace("⬛", "")):
    #             return 1
    #         elif len(item1[0].replace("🟩", "").replace("⬛", "")) > len(item2[0].replace("🟩", "").replace("⬛", "")):
    #             return -1
    #         else:
    #             # Most yellows:

            
    return sorted(buckets.items(), key=cmp_to_key(bucket_compare), reverse=True)

def search(guess_list, answers=answers, current_chain = []):
    if len(current_chain)>=10:
        return current_chain
    for word in guess_list:
        print("Trying " + word)
        print("Current chain:", current_chain)
        # print(current_chain)
        new_answers=sort_buckets(put_answers_into_buckets(word, answers))[0]
        # print(new_answers)
        if len(new_answers[1]) == 1:
            return (word, new_answers, current_chain)
        else:
            return search(new_answers[1], new_answers[1], current_chain+[word])


# print(get_response("bless", "saner"))

# print(len(put_answers_into_buckets("terns").keys()))
# print(sort_buckets(put_answers_into_buckets("terns")))
print(search(allowed_guesses))

# for guess in allowed_guesses:
#     buckets = put_answers_into_buckets(guess.strip())

print("Done")

