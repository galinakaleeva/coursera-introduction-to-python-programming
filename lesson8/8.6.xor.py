print(
    *map(
        lambda x, y: (x + y) % 2,
        map(
            int,
            input().split()
        ),
        map(
            int,
            input().split()
        )
    )
)
