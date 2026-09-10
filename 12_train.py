def mirror(data: list) -> list:
    sorted_min_to_max = sorted(data)
    sorted_max_to_min = sorted(data, reverse=True)
    return sorted_min_to_max + sorted_max_to_min[1:]


def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    sorted_data = sorted(arr)
    return sum(sorted_data[1:-1])


def first_non_repeated(s):
    dd = {}
    for x in s:
        dd[x] = dd.setdefault(x, 0) + 1
    for x in s:
        if dd[x] == 1:
            return x
    return None

print(first_non_repeated("abacabad"))
