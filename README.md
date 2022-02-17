# Absurdle Solver

A Python script to find four-word solutions to the adversarial [Wordle](https://www.nytimes.com/games/wordle/index.html) variant, [**Absurdle**](https://qntm.org/files/absurdle/absurdle.html).

Implements a depth-first search using only the valid solution list (feel free to try it with the full allowable guesses list, but it's gonna take a while!)

An exhaustive search is extremely slow, so I've added a "threshold" restriction to abandon branches if the opening word doesn't yield a largest bucket with less words than this value (see [Absurdle explanation](https://qntm.org/absurdle) for what "buckets" are). However this comes at the cost of completeness. For example, with the threshold set to 300, the script generates 55 solutions in 5 minutes, whereas with a threshold of 400, 64 solutions are found, but it took over half an hour. The threshold can be adjusted at the top of `solver.py`

To run:

```
python3 solver.py
```

Solutions will be displayed on screen as they are found, but the complete list will also be written to a text file.

As mentioned above, this search only considers buckets below a certain threshold. However, you can do a full-depth search starting from a single word, by using:

```
python3 solver.py [start-word]
```

This is by no means a thorough search of the possible space. I have seen other solutions where they are using words that are not found in the largest bucket from the previous guess (which this script doesn't do), which suggests there is a lot more possible solutions to be found. Would love to hear of any optimisations that could find more solutions in less time.
