import itertools

print(
    *itertools.accumulate(
        [1] + list(range(int(input()) + 1))[1:],
        lambda x, y: x * y
    )
)
