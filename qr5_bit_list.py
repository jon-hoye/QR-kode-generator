from qr6_error_correction import generate_error_correction

def string_to_data(content_string):

  liste = []

  for num in content_string:
     temp_liste = ([int(x) for x in f'{ord(num):08b}'])
     liste.extend(temp_liste)
  return liste



def get_core_bit_list(content_string):
   
   HEAD = [0, 1, 0, 0]

   TERMINATOR = [0, 0, 0, 0]

   my_len = len(content_string)
   len_bit_list = [int(x) for x in f'{my_len:08b}'] 
   
   data = string_to_data(content_string)

   return(HEAD + len_bit_list + data + TERMINATOR)


def pad_bit_list(core_bit_list, pad_to_bytes):
    PAD1 = [1, 1, 1, 0, 1, 1, 0, 0]
    PAD2 = [0, 0, 0, 1, 0, 0, 0, 1]

    liste = core_bit_list

    state = "pad1"

    while len(liste) < pad_to_bytes*8:
       
      if state == "pad1":
        liste += PAD1
        state = "pad2"
        continue

      if state == "pad2":
        liste += PAD2
        state = "pad1"
        continue

    return liste



def string_to_bit_list(content_string, qr_layout):
    
    bytes = qr_layout["byte_capacity"]

    total_bit = bytes * 8
   
    core_bit_list = get_core_bit_list(content_string)

    cbl_len = len(core_bit_list)


    ledig_bit = total_bit - cbl_len
    
    if ledig_bit >= 224:
       error_mode = "H"
       error_corr_bytes = 28
    elif ledig_bit >= 176:
       error_mode = "Q"
       error_corr_bytes = 22
    elif ledig_bit >= 128:
       error_mode = "M"
       error_corr_bytes = 16
    elif ledig_bit >= 80:
       error_mode = "L"
       error_corr_bytes = 10
    else:
      raise ValueError("error")
    
    target_data_bytes = bytes - error_corr_bytes
    bit_list_pad = pad_bit_list(core_bit_list, target_data_bytes)

    final_bit_list = generate_error_correction(bit_list_pad, error_mode)

    return final_bit_list, error_mode

