alpha = {'a': 0.1, 'b': 0.2, 'c': 0.4, 'd': 0.1, 'e': 0.2}
alpha2 = ['c', 'b', 'e', 'a', 'd'], [0.4, 0.2, 0.2, 0.1, 0.1]
result = [], []


def shan(a, value):
    # print(a)

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


shan(alpha2, "")
print(result)
test = [1,2,3,4,5]
l = len(test)
h = int(l/2)
# print(test[:h])