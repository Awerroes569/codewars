from itertools import product

SLICES=[slice(0,3),slice(3,6),slice(6,9)]

CLUSTERS=product(SLICES,repeat=2)

CLUSTERS=list(CLUSTERS)

def create_cluster(puzzle,cluster):
    return [row[cluster[1]] for row in puzzle[cluster[0]]]

def find_cluster(puzzle,clusters,cell):
    for cluster in CLUSTERS:
        if cell[0] in range(cluster[0].start, cluster[0].stop) and cell[1] in range(cluster[1].start, cluster[1].stop):
            return create_cluster(puzzle,cluster)
    raise ValueError("Cell not found in any cluster")

def prepare_raw_possibles(puzzle):
    possibles = {}
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                possibles[(row, col)] = list(range(1,10))
    return possibles

def reduce_possibles_by_cluster(puzzle, possibles):
    for cell in possibles:
        cluster = find_cluster(puzzle, CLUSTERS, cell)
        for row in cluster:
            for value in row:
                if value in possibles[cell] and value:
                    possibles[cell].remove(value)
    return possibles

def reduce_possibles_by_row(puzzle,possibles):
    for cell in possibles:
        for value in puzzle[cell[0]]:
            if value in possibles[cell] and value:
                possibles[cell].remove(value)
    return possibles

def reduce_possibles_by_col(puzzle,possibles):
    for cell in possibles:
        for row in puzzle:
            if row[cell[1]] in possibles[cell] and row[cell[1]]!=0:
                possibles[cell].remove(row[cell[1]])
    return possibles

def insert_known_values(puzzle,possibles):
    for cell in possibles:
        if len(possibles[cell])==1:
            puzzle[cell[0]][cell[1]]=possibles[cell][0]
    return puzzle[:]

def sudoku(puzzle):
    puzzle=puzzle[:]
    possibles = prepare_raw_possibles(puzzle)
    while not all([all(row) for row in puzzle]):
        possibles = reduce_possibles_by_cluster(puzzle, possibles)
        possibles = reduce_possibles_by_row(puzzle, possibles)
        possibles = reduce_possibles_by_col(puzzle, possibles)
        puzzle = insert_known_values(puzzle, possibles)
    return puzzle[:]



