
def set_fixed_fields(matrix, qr_layout):
    
    for cords in qr_layout["fixed_positions"]["zeros"]: 
      x, y = cords
      matrix[x][y] = 0

    for cords in qr_layout["fixed_positions"]["ones"]: 
      x, y = cords
      matrix[x][y] = 1
          
    return matrix




def set_meta_fields(matrix, err_corr, mask_no, qr_layout):

    pattern = qr_layout["meta_patterns"][err_corr][mask_no]
    
    i = 0

    for cords in qr_layout["meta_positions"]["first"]:
        x, y = cords
        matrix[x][y] = pattern[i]
        i += 1

    i = 0
    
    for cords in qr_layout["meta_positions"]["second"]:
        x, y = cords
        matrix[x][y] = pattern[i]
        i += 1
    return matrix