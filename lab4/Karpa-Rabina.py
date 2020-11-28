alpha = "ABCDE"


def h(values):
    r = len(alpha)
    q = 19
    result = 0
    m = len(values)
    for i in range(0, len(values)):
        m -= 1
        weight = alpha.index(values[i])
        result += weight * pow(r, m)
    result %= q
    # print("wqe", result)
    return result


def karpa_rabina(input, pattern):

    hp = h(pattern)
    r = len(alpha)
    len_pat = len(pattern)
    end_char = len_pat

    for i in range(0, len(input)-len_pat+1):

        ti = input[i:end_char]
        end_char += 1

        hi = h(ti)
        if hi == hp:
            is_pattern = True
            for j in range(0, len_pat):
                if pattern[j] != ti[j]:
                    is_pattern = False
                    break
            if is_pattern:
                print("patter:", ti, "from char", i, "to", end_char-1)


karpa_rabina("AEDBACA", "BACA")


