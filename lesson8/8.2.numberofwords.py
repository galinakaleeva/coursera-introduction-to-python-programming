import functools

print(
    len(
        functools.reduce(
            lambda x, y: x | y,
            map(
                lambda x: set(x.split()),
                open('input.txt', 'r', encoding='utf8').readlines()
            )
        )
    )
)
