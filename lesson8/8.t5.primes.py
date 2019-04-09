import math

print(
    *filter(
        lambda x: all(
            map(
                lambda y: x % y != 0,
                list(
                    range(
                        int(
                            math.sqrt(x)
                        ) + 1
                    )
                )[2:]
            )
        ),
        list(
            range(
                int(
                    input()
                ) + 1
            )
        )[2:]
    )
)
