from itertools import permutations
from functools import reduce

print(
    *next(
        filter(
            lambda elem: reduce(
                lambda stake1, stake2:
                    bool(stake1) and int(
                        elem.index(stake2[0]) < elem.index(stake2[1])
                    ) + int(
                        elem.index(stake2[2]) < elem.index(stake2[3])
                    ) % 2 == 1,
                map(
                    lambda x: list(
                        map(
                            int,
                            x.split()
                        )
                    ),
                    open('input.txt').readlines()
                )
            ),
            permutations(
                range(
                    1,
                    int(open('input.txt').readline().split()[0]) + 1
                )
            )
        ),
        [0]
    )
)
