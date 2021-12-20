def sudoku_solver(puzzle):
    sudoku_dict = {}
    r = 'ABCDEFGHI'
    c = '123456789'
    for i in range(9):
        for j in range(9):
            sudoku_dict[r[i]+c[j]] = str(puzzle[i][j]) if puzzle[i][j] != 0 else c
    square = [[x+y for x in i for y in j] for i in ('ABC','DEF','GHI') for j in ('123','456','789')]
    peers = {}
    for key in sudoku_dict.keys():
        value = [i for i in square if key in i][0]
        row = [[x+y for x in i for y in j][0] for i in key[0] for j in c]
        col = [[x+y for x in i for y in j][0] for i in r for j in key[1]]
        peers[key] = set(x for x in value+row+col if x != key)
    for i in range(9):
        sudoku_dict = Check(sudoku_dict,peers)
    sudoku_dict = search(sudoku_dict, peers)
    solution = []
    for i in r:
        solution.append([])
        for j in c:
            solution[r.find(i)].append(int(sudoku_dict[i+j]))
    return solution

def Check(sudoku_dict, peers):
    for k,v in sudoku_dict.items():
        if len(v) == 1:
            for s in peers[k]:
                sudoku_dict[s] = sudoku_dict[s].replace(v,'')
                if len(sudoku_dict[s])==0:
                    return False
    return sudoku_dict

def search(sudoku_dict,peers):
    if Check(sudoku_dict,peers)==False:
        return False
    if all(len(sudoku_dict[s]) == 1 for s in sudoku_dict.keys()): 
        return sudoku_dict
    n,s = min((len(sudoku_dict[s]), s) for s in sudoku_dict.keys() if len(sudoku_dict[s]) > 1)
    res = []
    for value in sudoku_dict[s]:
        new_sudoku_dict = sudoku_dict.copy()
        new_sudoku_dict[s] = value
        ans = search(new_sudoku_dict, peers)
        if ans:
            res.append(ans)
    if len(res) > 1:
        raise Exception("Error")
    elif len(res) == 1:
        return res[0]
