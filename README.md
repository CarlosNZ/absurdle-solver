# Absurdle Solver

A Python script to find four-word solutions to the adversarial [Wordle](https://www.nytimes.com/games/wordle/index.html) variant, [**Absurdle**](https://qntm.org/files/absurdle/absurdle.html).

Implements a depth-first search using only the valid solution list (feel free to try it with the full allowable guesses list, but it's gonna take a while!)

An exhaustive search is extremely slow, so I've added a "threshold" restriction to abandon branches if the opening word doesn't yield a largest bucket with less words than this value (see [Absurdle explanation](https://qntm.org/absurdle) for what "buckets" are). However this comes at the cost of completeness. For example, with the threshold set to 350, the script generates 31 solutions, whereas with a threshold of 400, 37 solutions are found, but takes many times longer. The threshold can be adjusted at the top of `solver.py`

To run:

```
python3 solver.py
```

Solutions will be displayed on screen as they are found, but the complete list will also be written to a text file.