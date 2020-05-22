import string
from collections import defaultdict

def print_rangoli(size):
    # your code goes here
    dict_default= defaultdict(list)
    num = size
    alph = list(string.ascii_lowercase)

    for i in range(1, (2 * num - 1) + 1):
        for j in range(1, (2 * (2 * num - 1) - 1) + 1):
            dict_default[i].append('-')

    k = (len(dict_default) * 2) // 2
    temp = (len(dict_default) // 2)
    for i in range(1, len(dict_default) + 1):
        if i <= (len(dict_default) + 1) // 2:
            index = num
            middle = (len(dict_default[i]) + 1) // 2
            for j in range(k, k + 4 * i - 3, 2):
                dict_default[i][j - 1] = alph[index - 1]
                if j >= middle:
                    index = index + 1
                else:
                    index = index - 1
            k = k - 2
        else:
            dict_default[i] = dict_default[temp]
            temp = temp - 1

    for i in range(1, len(dict_default) + 1):
        print(''.join(dict_default[i]))

if __name__ == '__main__':
