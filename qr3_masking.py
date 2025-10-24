def should_flip(row, col, mask_no):
  if mask_no == 0:
    if (row + col) % 2 == 0:
      return True
    
  if mask_no == 1:
    if row % 2 == 0:
      return True
    
  if mask_no == 2:
    if col % 3 == 0:
      return True
    
  if mask_no == 3:
    if (row + col) % 3 == 0:
      return True
    
  if mask_no == 4:
    if (row//2 + col//3) % 2 == 0:
      return True  
    
  if mask_no == 5:
    if (row*col) % 2 + (row*col) % 3 == 0:
      return True
    
  if mask_no == 6:
    if ((row*col) % 2 + (row*col) % 3) % 2 == 0:
      return True
    
  if mask_no == 7:
    if ((row+col) % 2 + (row*col) % 3) % 2 == 0:
      return True

  return False





def get_masked_matrix(matrix, mask_no):
    rows = len(matrix)

    cols = len(matrix[0])


    nymatrise = []

    for i in range(rows):
        listrow = []
        for j in range(cols):
          orgverdi = matrix[i][j]

          if should_flip(i, j, mask_no):
            nyverdi = 1 - orgverdi
          else:
            nyverdi = orgverdi
          listrow.append(nyverdi)
        nymatrise.append(listrow)

    return(nymatrise)

def score_matrix(matrix):
  count0 = 0

  count1 = 0

  for line in matrix:
    for num in line:
      if num == 1:
        count1 += 1
      elif num == 0:
        count0 += 1
      else:
        continue
  
  difference = abs(count1-count0)

  return difference



def get_refined_matrix(raw_matrix, error_correction_level, qr_layout):

  from qr2_matrix_completion import set_meta_fields, set_fixed_fields

  liste = []

  for i in range(7):
    
    fixed_matrix = set_fixed_fields(set_meta_fields(get_masked_matrix(raw_matrix, i), error_correction_level, i, qr_layout), qr_layout)

    liste.append(score_matrix(fixed_matrix))

  minstetall = (min(liste))

  best_mask_no = liste.index(minstetall)

  return(set_fixed_fields(set_meta_fields(get_masked_matrix(raw_matrix, best_mask_no), error_correction_level, best_mask_no, qr_layout), qr_layout))







