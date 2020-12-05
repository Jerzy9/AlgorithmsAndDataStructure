alpha = ['c', 'b', 'e', 'a', 'd'], [0.4, 0.2, 0.2, 0.1, 0.1]
result = [], []


def shan(a, value):
    length = len(a[1])

    if length == 1:
        result[0].append(a[0])
        result[1].append(value)
        print(a[0], value, "test")
        pass
    else:

        half = int(length / 2)

        tab0 = a[0][:half], a[1][:half]
        tab1 = a[0][half:], a[1][half:]

        # print(tab0, tab1)
        str0 = str(value+ '0')
        shan(tab0, str(value + '0'))
        shan(tab1, str(value + '1'))


shan(alpha, "")
print(result)