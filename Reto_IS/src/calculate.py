def calculate_patterns(distance: int) -> int:
    if distance == 0:
        return 0
    elif distance == 1:
        return 1
    elif distance == 2:
        return 2

    a, b = 1, 2
    for _ in range(3, distance + 1):
        a, b = b, a + b
    return b
