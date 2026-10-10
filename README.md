# 2048 with Fibonacci numbers

A terminal version of the 2048 puzzle where tiles merge when they are consecutive Fibonacci numbers (1+1, 1+2, 2+3, 3+5...) instead of equal powers of two. You win by reaching 2584.

I wrote this as a programming assignment in my first years of Mathematical Engineering, using only standard Python. I'm keeping it as it was: it shows how I programmed at that point. Today I would write it differently, with less repetition between the four move directions and with tests.

## How to play

```bash
python fibonacci_2048.py
```

Moves: `l` left, `r` right, `u` up, `d` down. Type `save` to save the board to `tablero.txt`, `load` to load it again, and `end` to quit.
