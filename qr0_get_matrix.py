import json
from pathlib import Path

from qr3_masking import get_refined_matrix

from qr4_zigzag import bit_list_to_raw_matrix

from qr5_bit_list import string_to_bit_list

def get_qr_matrix(content_string):
    qr_layout = json.loads(Path('qrv2_layout.json').read_text(encoding='utf-8'))
    bit_list, err_corr = string_to_bit_list(content_string, qr_layout)
    raw_matrix = bit_list_to_raw_matrix(bit_list, qr_layout)
    matrix = get_refined_matrix(raw_matrix, err_corr, qr_layout)
    return matrix