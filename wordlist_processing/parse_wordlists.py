import json

RAW_WORDLIST_FILE = "absurdle_allowed_guesses_raw__2022-02-16.json"

with open(RAW_WORDLIST_FILE) as json_file:
    wordsRaw = json.load(json_file)

json_file.close()

full_word_array = []
for prefix in wordsRaw.keys():
    suffixes = [wordsRaw[prefix][i : i + 3] for i in range(0, len(wordsRaw[prefix]), 3)]
    words = [prefix + suffix for suffix in suffixes]
    full_word_array = full_word_array + words

full_word_array.sort()

f = open(RAW_WORDLIST_FILE.replace("raw_", "").replace("json", "txt"), "w")

for word in full_word_array:
    f.write(word.lower() + "\n")

f.close()
