from reedsolo import RSCodec

def generate_error_correction(padded_core_bit_list, correction_level):
    correction_bytes = {'L': 10, 'M': 16, 'Q': 22, 'H': 28}
    codec = RSCodec(correction_bytes[correction_level])
    byte_string = _bit_list_to_byte_string(padded_core_bit_list)
    res = codec.encode(byte_string)
    return _byte_string_to_bit_list(res)


def _bit_list_to_byte_string(bit_list):
    return bytes([
        sum([b * 2**(7-p) for p, b in enumerate(bit_list[s:s+8])])
        for s in range(0, len(bit_list), 8)
    ])

def _byte_string_to_bit_list(byte_string):
    return [(by // 2**(7-p)) % 2 for by in byte_string for p in range(8)]
