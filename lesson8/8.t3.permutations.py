import itertools

print(
    *map(
        ''.join,
        itertools.permutations(
            ''.join(
                list(
                    map(
                        str,
                        list(
                            range(int(input()) + 1)
                        )[1:]
                    )
                )
            )
        )
    ),
    sep='\n'
)
