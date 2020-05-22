def minion_game(string):
    # your code goes here
    s_length = len(string)
    vowel_list = ['A','E','I','O','U']
    stuart_scr = 0
    kevin_scr = 0
    for i in range(s_length):
        if s[i] in vowel_list:
            kevin_scr += s_length - i
        else:
            stuart_scr += s_length - i
    if stuart_scr == kevin_scr:
        print('Draw')
    elif kevin_scr > stuart_scr:
        print('Kevin',kevin_scr)
    else:
        print('Stuart',stuart_scr)

if __name__ == '__main__':
