def get_next_pos(row, column, size):
    if column % 2 == 0:
        if column == 0:
            row -= 1
        else:
            column -= 1
    else:
        if column % 4 == 1:
            if row == (size-1):
                column -= 1
            else:
                row += 1
                column += 1
        else:
            if row == 0:
                column -= 1
            else:
                row -= 1
                column += 1
    
    if row < 0 or row >= size or column < 0 or column >= size:
        return None, None
    
    return row, column



def bit_list_to_raw_matrix(bit_list, qr_layout):
    matrisen = []

    size = qr_layout["side_length"]
    for c in range(size):
        row = []
        for r in range(size):
            row.append(0)
        matrisen.append(row)


    x, y = size-1, size-1
    matrisen[x][y] = 0
    for num in bit_list:
            
            while ([x, y] in qr_layout["fixed_positions"]["ones"]) or \
                  ([x, y] in qr_layout["fixed_positions"]["zeros"]) or \
                  ([x, y] in qr_layout["meta_positions"]["first"]) or \
                  ([x, y] in qr_layout["meta_positions"]["second"]):
                x, y = get_next_pos(x, y, size)
                if x is None or y is None:
                    break

            if x is not None and y is not None:
                matrisen[x][y] = num
                x, y = get_next_pos(x, y, size)
                if x is None or y is None:
                    break

    return matrisen