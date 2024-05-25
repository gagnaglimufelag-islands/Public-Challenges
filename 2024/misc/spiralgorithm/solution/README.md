# Spiralgorithm

This challenge presents us with squares of text with seemingly random letters and symbols. Inspecting the squares, we observe that they are English phrases arranged in a spiral pattern, as seen below.

```
# 3x3 spiral
012
783
654

# 4x4 spiral
abcd
lmne
kpof
jihg

# 5x5 spiral
abcde
pqrsf
oxytg
nwvuh
mlkji
```

In the cases where the length of the phrases is not a square, they are padded with `X` to the nearest square. Therefore, we need to unravel these spirals, either manually or programmatically. An example in Python is shown below.

```python
def unspiral(text):
    correct = []
    lines = text.split()
    while lines:
        if len(lines) == 1:
            correct.append(lines[0])
            break
        first, *lines, pen = lines

        # Transpose lines
        lines = list(map(''.join, zip(*lines)))
        if not lines:
            last = second = ''
        else:
            last, *lines, second = lines
            # Transpose lines
            lines = list(map(''.join, zip(*lines)))
        correct.extend([first, second, pen[::-1], last[::-1]])

    return ''.join(correct)
```
