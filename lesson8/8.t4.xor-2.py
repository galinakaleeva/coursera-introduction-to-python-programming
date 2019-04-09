from functools import reduce

print(
    *reduce(
        lambda list1, list2: list(
            map(
                lambda x, y: (int(x) + int(y)) % 2,
                list1,
                list2
            )
        ),
        map(
            lambda x: x.split(),
            open('input.txt').read().split('\n')[1:-1]
        )
    )
)
