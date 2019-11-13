import sys

file = open("dane.txt", "r")
data_line = file.readline()

while data_line != "":
    data_line = data_line.strip("\n")
    data = data_line.split(" ")

    amountof_mistakes = int(data[0])  # ile bledow moze byc w podciagu
    string1 = data[1]  # pierwszy ciag
    string2 = data[2]  # drugi ciag

    length1 = len(string1)
    length2 = len(string2)

    iterator1 = 0
    strings = []
    max_length = 0
    while iterator1 < length1:
        iterator2 = 0
        substrings = []
        while iterator2 < length2:
            if amountof_mistakes == 0:
                if string1[iterator1] == string2[iterator2]:
                    iterator2_inner = iterator2 + 1
                    iterator1_inner = iterator1 + 1
                    subsubstrings = [string1[iterator1], string2[iterator2]]
                    while iterator2_inner < length2 and iterator1_inner < length1 and \
                            string1[iterator1_inner] == string2[iterator2_inner]:
                        subsubstrings[0] += string1[iterator1_inner]
                        subsubstrings[1] += string2[iterator2_inner]
                        iterator2_inner += 1
                        iterator1_inner += 1
                    if len(subsubstrings) != 0:
                        substrings.append(subsubstrings[0])
                        substrings.append(subsubstrings[1])
            else:
                iterator_mistakes = 0
                iterator2_inner = iterator2
                iterator1_inner = iterator1
                subsubstrings = ['', '']
                while iterator2_inner < length2 and iterator1_inner < length1:
                    if string1[iterator1_inner] != string2[iterator2_inner]:
                        if iterator_mistakes < amountof_mistakes:
                            iterator_mistakes += 1
                        else:
                            break
                    subsubstrings[0] += string1[iterator1_inner]
                    subsubstrings[1] += string2[iterator2_inner]
                    iterator2_inner += 1
                    iterator1_inner += 1
                if len(subsubstrings) != 0:
                    substrings.append(subsubstrings[0])
                    substrings.append(subsubstrings[1])
            iterator2 += 1
        if len(substrings) > 2:
            if max_length < len(max(substrings, key=len)):
                max_length = len(max(substrings, key=len))
            for st in substrings:
                if len(st) == max_length:
                    strings.append(st)
        else:
            strings += substrings
        iterator1 += 1

    longest_strings = []
    if len(strings) != 0:
        max_length = len(max(strings, key=len))
        for st in strings:
            dlugosc = len(st)
            if dlugosc == max_length:
                longest_strings.append(st)

    data_line = file.readline()
    if len(longest_strings) == 0:
        print("Brak wspolnych podciagow spelniajacych kryteria dla ciagow wyrazowych", string1, "i", string2)
        continue
    print("Najdluzszymi wspolnymi podciagami ciagow wyrazowych", string1,
          "i", string2, "o maksymalnej ilosci rozniacych sie znakow rownej", amountof_mistakes,
          "sa podciagi o dlugosci rownej -", len(longest_strings[0]), longest_strings)
