from helpers import fewest_greens, fewest_yellows, leftmost_clue
from solver import sort_buckets

# Not a proper test suite, just some crude checks I used while developing.

print(fewest_greens("⬜⬜⬜⬜🟩", "⬜🟨⬜🟨⬜"))

print(fewest_yellows("⬜⬜⬜⬜🟩", "⬜🟨⬜🟨⬜"))

# fmt: off
print(sort_buckets({'⬛🟨⬛🟨⬛': ['glint', 'guilt', 'ingot', 'input', 'joint', 'joist', 'moist', 'point', 'posit', 'quilt', 'spilt', 'split', 'still', 'stilt', 'sting', 'stink', 'stint', 'toxin', 'tulip', 'unlit', 'until', 'vomit'], '⬛⬛⬛⬛🟩': ['golly', 'gully', 'gummy', 'guppy', 'jolly', 'jumpy', 'loopy', 'lousy', 'lumpy', 'mossy', 'mummy', 'musky', 'poppy', 'pulpy', 'puppy', 'pygmy', 'slyly', 'smoky', 'soggy', 'sulky', 'sully', 'sunny']}))
# fmt: on
