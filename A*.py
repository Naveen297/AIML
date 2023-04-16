def move(ar, p, st):
    rh = 99999
    store_st = st.copy()
    for i in range(len(ar)):
        dupl_st = st.copy()
        temp = dupl_st[p]
        dupl_st[p] = dupl_st[ar[i]]
        dupl_st[ar[i]] = temp
        tmp_rh = count(dupl_st)
        if tmp_rh < rh:
            rh = tmp_rh
            store_st = dupl_st.copy()
    return store_st, tmp_rh


def print_in_format(matrix):
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print("")
        print(str(matrix[i]) + " ", end=" ")


def count(s):
    c = 0
    ideal = [1, 2, 3,
             4, 5, 6,
             7, 8, 0]
    for i in range(9):
        if s[i] != 0 and s[i] != ideal[i]:
            c += 1
    return c


start = [1, 2, 3,
         0, 5, 6,
         4, 7, 8]

h = count(start)
level = 1
print("\n..................Level " + str(level) + "....................")
print_in_format(start)
print("\n Heuristic Value (misplaced tiles): " + str(h))

while h > 0:
    pos = int(start.index(0))
    level += 1
    if pos == 0:
        arr = [1, 3]
    elif pos == 1:
        arr = [0, 2, 4]
    elif pos == 2:
        arr = [1, 5]
    elif pos == 3:
        arr = [0, 4, 6]
    elif pos == 4:
        arr = [1, 3, 5, 7]
    elif pos == 5:
        arr = [2, 4, 8]
    elif pos == 6:
        arr = [3, 7]
    elif pos == 7:
        arr = [4, 6, 8]
    elif pos == 8:
        arr = [5, 7]

    start, h = move(arr, pos, start)
    print("\n...........Level " + str(level) + "...............")
    print_in_format(start)
    print("\nHeuristic value (misplaced tiles): " + str(h))
