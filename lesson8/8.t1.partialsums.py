import itertools

print(
    *itertools.accumulate(
        map(
            int,
            input().split()
        ),
        lambda x, y: x + y
    )
)
