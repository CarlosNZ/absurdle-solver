from helpers import fewest_greens, fewest_yellows, latest_clue, getTimeString
from solver import sort_buckets, get_response

# Not a proper test suite, just some crude checks I used while developing.

# print(fewest_greens("⬜⬜⬜⬜🟩", "⬜🟨⬜🟨⬜"))

# print(fewest_yellows("⬜⬜⬜⬜🟩", "⬜🟨⬜🟨⬜"))

# print(latest_clue("⬜🟨🟨⬜⬜", "⬜⬜🟨🟨⬜"))

print(get_response("beech", "jetty"))  # ⬛🟩⬛⬛⬛
print(get_response("beech", "plane"))  # ⬛🟨⬛⬛⬛
print(get_response("beech", "theft"))  # ⬛⬛🟩⬛🟨
print(get_response("beech", "theme"))  # ⬛🟨🟩⬛🟨
print(get_response("plied", "bevel"))  # ⬛🟨⬛🟩⬛
print(get_response("foray", "chump"))  # ⬛⬛⬛⬛⬛

# fmt: off
# print(sort_buckets({'⬛🟨⬛🟨⬛': ['glint', 'guilt', 'ingot', 'input', 'joint', 'joist', 'moist', 'point', 'posit', 'quilt', 'spilt', 'split', 'still', 'stilt', 'sting', 'stink', 'stint', 'toxin', 'tulip', 'unlit', 'until', 'vomit'], '⬛⬛⬛⬛🟩': ['golly', 'gully', 'gummy', 'guppy', 'jolly', 'jumpy', 'loopy', 'lousy', 'lumpy', 'mossy', 'mummy', 'musky', 'poppy', 'pulpy', 'puppy', 'pygmy', 'slyly', 'smoky', 'soggy', 'sulky', 'sully', 'sunny']}))
# fmt: on

# print(getTimeString(1000))
# print(getTimeString(1))
# print(getTimeString(60))
# print(getTimeString(61))
# print(getTimeString(120))
# print(getTimeString(654))
