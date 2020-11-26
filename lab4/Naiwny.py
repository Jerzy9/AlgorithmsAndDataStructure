def naiwny(input, patter):
    counter = 0
    found = False

    for i in range(0, len(input)):
        first_patt_char = patter[0]

        if input[i] == first_patt_char:
            index = i
            for p in patter:
                if input[index] == p:
                    found = True
                    index += 1
                    continue
                found = False

            if found:
                print("znaleziono wzorzec od", index - len(patter) + 1, "znaku")
                found = False
                counter += 1

    print("\nW sumie znaleziono", counter, "wzorców")


naiwny("pogodasd sd sdgodsadgod", "god")
