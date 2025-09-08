pre_test0 = [
	[
		' 00 ',
		' 00 ',
		' 00 ',
		' 00 '], [[4,2]]]
pre_test1 = [
	[
		'     0  ',
		' 00  0  ',
		' 00     ',
		' 00     ',
		'   0    ',
		'       0',
		'       0',
		'0000   0'], [[1, 1], [1, 2], [1, 3], [1, 4], [2, 3]]]
#[[4, 3, 0], [0, 5, 1], [5, 7, 1], [7, 0, 0], [1, 1, 1]])
[[4, 3, 0], [0, 5, 1], [5, 7, 1], [7, 0, 0], [1, 1, 1]]


"""code"""


from collections import deque
def pieces_transform(pieces):
    result = []
    for nr, piece in enumerate(pieces):
        h, w= piece
        item = (nr, h, w, h*w, 0) # REMEMBER ABOUT THE LAST 0
        result.append(item)
    result.sort(key=lambda x: x[3], reverse=True)
    print('Pieces transformed:', tuple(result))
    return tuple(result)

def matrix_transform(matrix):
    result = {(hrow, wcol) for hrow in range(len(matrix))
              for wcol in range(len(matrix[0])) if matrix[hrow][wcol] == '0'}
    return result


def if_piece_fits(matrix, point, piece):
    """
    Check if a piece can fit into the current hole set (matrix) at a given point.
    
    Optimized compared to the original:
    - Precompute all cells the piece would cover (relative offsets).
    - Use set operations instead of Python-level nested loops.
    - Early reject if the piece would go out of matrix bounds.
    """
    _, h, w, __, ___ = piece
    hrow, wcol = point

    # --- 1. Generate all occupied cells for this piece placement ---
    # Instead of two nested loops with repeated membership checks,
    # we build a set of all (row, col) coordinates the piece would occupy.
    occupied_cells = {(hrow + i, wcol + j) for i in range(h) for j in range(w)}

    # --- 2. Quick subset test ---
    # Check if all required cells are still available in `matrix`.
    # This single operation (`<=`) is implemented in C for sets,
    # and is usually faster than N × `in` lookups in Python.
    return occupied_cells <= matrix


def holes_remover(matrix, point, piece):
    _, h, w, __, ___ = piece
    hrow, wcol = point
    for i in range(h):
        for j in range(w):
            if (hrow + i, wcol + j) in matrix:
                matrix.remove((hrow + i, wcol + j))
    return matrix


def where_piece_fits(matrix, piece):
    """
    Find all positions (points) where a piece can fit into the current hole set (matrix).

    Optimizations compared to original:
    - Skip candidate points that would obviously go out of bounds.
    - Delegate the actual fitting check to the optimized if_piece_fits.
    """
    positions = []
    _, h, w, __, ___ = piece

    # --- 1. Compute maximum bounds ---
    # If the piece extends beyond these limits, it cannot fit.
    max_h = max(r for r, _ in matrix)
    max_w = max(c for _, c in matrix)

    # --- 2. Test only valid candidate points ---
    # `matrix` is already the set of available holes,
    # so we only check those coordinates (not the whole board).
    for hrow, wcol in matrix:
        # Early reject if the piece would overflow board boundaries
        if hrow + h - 1 > max_h or wcol + w - 1 > max_w:
            continue

        # Delegate to the optimized subset-based fit check
        if if_piece_fits(matrix, (hrow, wcol), piece):
            positions.append((hrow, wcol))

    return positions

def is_superpiece_transformable(piece):
    nr, h, w, area, first = piece
    return h != w and area > 0 and first == 0

def superpiece_transform(piece):
    nr, h, w, area, __ = piece
    return (nr, w, h, area, 1)

def transform_result(result):
    transformed = []
    print('Unsorted result:', result)
    result.sort(key=lambda x: x[2])  # sort by piece number
    for h, w, nr, r in result:
        transformed.append([h, w, r])
    return transformed

def solve_puzzle(board, pieces):
	# establish set of holes coordinates
    holes = matrix_transform(board)
    print('Holes:', holes)
    # transform pieces into a list of superpieces
    superpieces = pieces_transform(pieces)
    print('Superpieces:', superpieces)

    # creating furnace list
    furnace = deque()

    # initiate furnace with the first package: holes + superpieces + preresult
    first_package = (holes, superpieces, [])
    furnace.append(first_package)
    print ('Furnace:', furnace)

    result = []
    
    # while furnace is not empty
    while furnace and not result:
        current_holes, current_superpieces, current_preresult = furnace.popleft()
        print('Current package:', (current_holes, current_superpieces, current_preresult))
        for piece in current_superpieces:
            print('Current piece:', piece)
            variants = []
            for variant in where_piece_fits(current_holes, piece):
                variants.append(variant)
            
                
            
            print('Variants:', variants)
            for variant in variants:
                # normal pieces
                print('Holes before removing piece:', current_holes)
                new_holes = holes_remover(current_holes.copy(), variant, piece)
                print('New holes after removing piece:', new_holes)
                print('Trying to remove piece:', piece,'from superpieces:', current_superpieces)
                where_piece = current_superpieces.index(piece)
                print('Where piece index:', where_piece)
                new_superpieces = current_superpieces[:where_piece] + current_superpieces[where_piece+1:]
                #new_superpieces = current_superpieces.copy()
                #new_superpieces.remove(piece)  # remove the piece from superpieces
                print('New superpieces:', new_superpieces)
                new_preresult = current_preresult + [(variant[0], variant[1],piece[0], piece[4])]
                print('New preresult:', new_preresult)
                # [x,y,z] <- x,y coordinates , z is rotated
                new_package = (new_holes.copy(), new_superpieces, new_preresult.copy()) #here latest
                if not new_superpieces:
                    print('Solution found:', new_package)
                    result = new_package[2]
                print('New package:', new_package)
                if not new_package in furnace:
                    furnace.append(new_package)
                """# pieces transformed
                if is_superpiece_transformable(piece):
                    new_piece = superpiece_transform(piece)
                    print('New piece rotated:', new_piece)
                    for variant in where_piece_fits(current_holes, new_piece):
                        print('Variant for superpiece rotated:', variant)
                        new_holes = holes_remover(current_holes.copy(), variant, new_piece)
                        print('New holes after removing rotated superpiece:', new_holes)
                        new_superpieces = current_superpieces.copy()
                        new_superpieces.remove(piece)
                        new_preresult = current_preresult + [(variant[0], variant[1], new_piece[0], new_piece[4])]
                        print('New preresult rotated:', new_preresult)
                        new_package = (new_holes.copy(), new_superpieces.copy(), new_preresult.copy())
                        if not new_superpieces:
                            print('Solution found rotated:', new_package)
                            return new_package[2]
                        print('New package rotated:', new_package)
                        furnace.append(new_package)"""
                
            if is_superpiece_transformable(piece):
                for variant in where_piece_fits(current_holes, superpiece_transform(piece)):
                    # repeat previous steps for not transformed superpiece but for transformed superpiece
                    print('R Variant for superpiece:', variant)
                    new_holes = holes_remover(current_holes.copy(), variant, superpiece_transform(piece))
                    print('R New holes after removing superpiece:', new_holes)  
                    ############################  
                    where_superpiece = current_superpieces.index(piece)
                    print('R Where superpiece index:', where_superpiece)
                    new_superpieces = current_superpieces[:where_superpiece] + current_superpieces[where_superpiece+1:]
                    #new_superpieces = current_superpieces.copy()
                    #new_superpieces.remove(piece)
                    #####################################
                    print('R New superpieces after removing superpiece:', new_superpieces)
                    new_preresult = current_preresult + [(variant[0], variant[1], superpiece_transform(piece)[0], superpiece_transform(piece)[4])]
                    print('R New preresult after removing superpiece:', new_preresult)
                    new_package = (new_holes.copy(), new_superpieces, new_preresult.copy())
                    if not new_superpieces:
                        print('Solution found for superpiece:', new_package)
                        result = new_package[2]
                    print('R New package for superpiece:', new_package)
                    if not new_package in furnace:
                        furnace.append(new_package)

    if not result:
        return []
    print('Final result:', transform_result(result)) 
    return transform_result(result)
    

# Test cases
assert pieces_transform([[1, 1]]) == ((0, 1, 1, 1, 0),), "pieces_transform failed 1"
assert pieces_transform([[1, 1], [1, 2], [1, 3], [1, 4], [2, 3]]) == ((4, 2, 3, 6, 0), (
    3, 1, 4, 4, 0), (2, 1, 3, 3, 0), (1, 1, 2, 2, 0), (0, 1, 1, 1, 0)), "pieces_transform failed 2"
assert pieces_transform([[2, 1], [1, 2]]) == ((0, 2, 1, 2, 0),
                                      (1, 1, 2, 2, 0)), "pieces_transform failed 3"
assert pieces_transform([[1, 2], [2, 4], [1, 1]]) == ((
    1, 2, 4, 8, 0), (0, 1, 2, 2, 0), (2, 1, 1, 1, 0)), "pieces_transform failed 4"

assert matrix_transform(pre_test0[0]) == {(0, 1), (0 ,2), (1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)}, "matrix_transform failed 1"
assert matrix_transform(pre_test1[0]) == {(
    0, 5), (1, 1), (1, 2), (1, 5), (2, 1), (2, 2), (3, 1), (3, 2), (4, 3), (5, 7), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3), (7, 7)}, "matrix_transform failed 2"

assert if_piece_fits(matrix_transform(pre_test0[0]), (1, 1), (1, 1, 2, 2,0)) == True, "if_piece_fits failed 1"
assert if_piece_fits(matrix_transform(pre_test0[0]), (1, 1), (1, 2, 2, 4, 0)) == True, "if_piece_fits failed 2"
assert if_piece_fits(matrix_transform(pre_test0[0]), (1, 1), (1, 1, 3, 3, 0)) == False, "if_piece_fits failed 3"
assert if_piece_fits(matrix_transform(pre_test0[0]), (1, 1), (1, 1, 4, 4,0)) == False, "if_piece_fits failed 4"
assert if_piece_fits(matrix_transform(pre_test0[0]), (0, 0), (1, 1, 1, 1, 0)) == False, "if_piece_fits failed 5"
assert if_piece_fits(matrix_transform(pre_test0[0]), (7, 7), (1, 1, 1, 1, 0)) == False, "if_piece_fits failed 6"
assert if_piece_fits(matrix_transform(pre_test0[0]), (3, 3), (1, 1, 1, 1,0)) == False, "if_piece_fits failed 7"
assert if_piece_fits(matrix_transform(pre_test0[0]), (3, 2), (1, 1, 1, 1, 0)) == True, "if_piece_fits failed 8"
assert if_piece_fits(matrix_transform(pre_test0[0]), (0, 1), (1, 4, 2, 8,0)) == True, "if_piece_fits failed 9"
assert if_piece_fits(matrix_transform(pre_test0[0]), (0, 1), (1, 4, 3, 12, 0)) == False, "if_piece_fits failed 10"
assert if_piece_fits(matrix_transform(pre_test1[0]), (0, 5), (1, 1, 1, 1, 0)) == True, "if_piece_fits failed 11"
assert if_piece_fits(matrix_transform(pre_test1[0]), (1, 1), (1, 1, 2, 2, 0)) == True, "if_piece_fits failed 12"
assert if_piece_fits(matrix_transform(pre_test1[0]), (1, 1), (1, 3, 2, 6, 0)) == True, "if_piece_fits failed 13"
assert if_piece_fits(matrix_transform(pre_test1[0]), (1, 2), (1, 3, 1, 3,0)) == True, "if_piece_fits failed 14"

assert set(where_piece_fits(matrix_transform(pre_test0[0]), (1, 2, 2, 4, 0))) == {(0, 1), (1, 1), (2, 1)}, "where_piece_fits failed 1"
assert set(where_piece_fits(matrix_transform(pre_test0[0]), (1, 4, 1, 4, 0))) == {(0, 1), (0, 2)}, "where_piece_fits failed 2"
assert set(where_piece_fits(matrix_transform(pre_test0[0]), (1, 4, 2, 8, 0))) == {(0, 1)}, "where_piece_fits failed 3"
assert set(where_piece_fits(matrix_transform(pre_test1[0]), (1, 2, 2, 4, 0))) == {(1, 1), (2, 1)}, "where_piece_fits failed 4"
assert set(where_piece_fits(matrix_transform(pre_test1[0]), (1, 1, 4, 8, 0))) == {
    (7, 0)}, "where_piece_fits failed 5"
assert set(where_piece_fits(matrix_transform(pre_test1[0]), (1, 3, 2, 6, 0))) == {(1, 1)}, "where_piece_fits failed 5"

assert superpiece_transform((0, 1, 2, 2, 0)) == (0, 2, 1, 2, 1), "superpiece_transform failed 1"
assert superpiece_transform((0, 3, 5, 15, 0)) == (0, 5, 3, 15, 1), "superpiece_transform failed 2"

assert is_superpiece_transformable((0, 1, 2, 2, 0)) == True, "is_superpiece_transformable failed 1"
assert is_superpiece_transformable((0, 2, 1, 2, 0)) == True, "is_superpiece_transformable failed 2"
assert is_superpiece_transformable((8, 2, 1, 0, 0)) == False, "is_superpiece_transformable failed 3"
assert is_superpiece_transformable((8, 2, 1, 2, 1)) == False, "is_superpiece_transformable failed 4"
assert is_superpiece_transformable((8, 8, 8, 64, 0)) == False, "is_superpiece_transformable failed 5"
#matrix, point, piece
assert holes_remover(matrix_transform(pre_test0[0]),(0, 1), (1, 2, 2, 4, 0)) == { (2, 1), (2, 2), (3, 1), (3, 2)}, "holes_remover failed 1"
assert holes_remover(matrix_transform(pre_test0[0]),(0, 1), (1, 1, 2, 2, 0)) == { (1, 1), (1, 2),(2, 1), (2, 2), (3, 1), (3, 2)}, "holes_remover failed 2"
assert holes_remover(matrix_transform(pre_test0[0]),(0, 1), (1, 4, 2, 8, 0)) == set(), "holes_remover failed 3"
# {(1, 2), (7, 1), (2, 1), (7, 7), (1, 5), (3, 1), (4, 3), (1, 1), (7, 0), (5, 7), (7, 3), (6, 7), (0, 5), (2, 2), (7, 2), (3, 2)}
assert holes_remover(matrix_transform(
    pre_test1[0]), (1, 1), (1, 1, 2, 4, 0)) == {(7, 1), (2, 1), (7, 7), (1, 5), (3, 1), (4, 3), (7, 0), (5, 7), (7, 3), (6, 7), (0, 5), (2, 2), (7, 2), (3, 2)}, "holes_remover failed 4"
assert holes_remover(matrix_transform(pre_test1[0]), (0, 0), (1, 20, 20, 400, 0)) == set(), "holes_remover failed 5"
assert holes_remover(matrix_transform(pre_test1[0]), (7, 0), (1, 1, 4, 4, 0)) == {(1, 2), (2, 1), (7, 7), (
    1, 5), (3, 1), (4, 3), (1, 1), (5, 7), (6, 7), (0, 5), (2, 2), (3, 2)}, "holes_remover failed 6"

assert holes_remover(matrix_transform(pre_test1[0]), (1, 2), (1, 7, 1, 7, 0)) == {(7, 1), (2, 1), (7, 7), (1, 5), (3, 1), (4, 3), (1, 1), (7, 0), (5, 7), (7, 3), (6, 7), (0, 5)}, "holes_remover failed 7"
assert holes_remover(matrix_transform(pre_test1[0]), (0, 0), (1, 6, 1, 6, 0)) == {(1, 2), (7, 1), (2, 1), (7, 7), (
    1, 5), (3, 1), (4, 3), (1, 1), (7, 0), (5, 7), (7, 3), (6, 7), (0, 5), (2, 2), (7, 2), (3, 2)}, "holes_remover failed 8"



"""
matrix = matrix_transform(pre_test1[0])
print(if_piece_fits(matrix, (1,1),(1, 1, 2, 0) )),
print("Positions where piece fits (1,2):")
print(where_piece_fits(matrix, (1, 2, 1, 0)))
"""
print(solve_puzzle(pre_test1[0], pre_test1[1]))
#print(holes_remover(matrix_transform(pre_test0[0]), (0, 1), (1, 2, 2, 4, 0)))
#[[4, 3, 0], [0, 5, 1], [5, 7, 1], [7, 0, 0], [1, 1, 1]])

