# Algorithms.py

def get_parity(text, mode='even'):
    # Convert text to binary string
    binary_str = ''.join(format(ord(c), '08b') for c in text)
    count_ones = binary_str.count('1')
    
    if mode == 'even':
        if count_ones % 2 != 0:
            return '1'
        else:
            return '0'
    else: 
        # odd parity
        if count_ones % 2 != 0:
            return '0'
        else:
            return '1'

def get_2d_parity(text):
    # Convert chars to ascii values
    vals = [ord(c) for c in text]
    
    # Calculate row parity
    rows = []
    for v in vals:
        b_val = format(v, '08b')
        if b_val.count('1') % 2 != 0:
            rows.append('1')
        else:
            rows.append('0')
    
    # Calculate col parity
    cols = []
    for i in range(8):
        c_ones = 0
        for v in vals:
            # check bit at index i
            if (v >> (7 - i)) & 1:
                c_ones += 1
        
        if c_ones % 2 != 0:
            cols.append('1')
        else:
            cols.append('0')
        
    return "".join(rows) + "|" + "".join(cols)

def crc16(text):
    data = bytearray(text, 'utf-8')
    c = 0xFFFF 
    
    for b in data:
        c ^= b
        for _ in range(8):
            if c & 1:
                c = (c >> 1) ^ 0xA001
            else:
                c >>= 1
                
    return format(c, '04X') 

def hamming_encode(text):
    # Just a simulation for the project requirement
    return "HAMMING_CODE:" + str(len(text))

def checksum(text):
    s = sum(ord(c) for c in text)
    return format(s & 0xFFFF, '04X')

def check_data(text, method, val_received):
    val_calculated = ""
    
    if method == "PARITY":
        val_calculated = get_parity(text, 'even')
        
    elif method == "2D_PARITY":
        val_calculated = get_2d_parity(text)
        
    elif method == "CRC":
        val_calculated = crc16(text)
        
    elif method == "HAMMING":
        val_calculated = "HAMMING_CODE:" + str(len(text))
        
    elif method == "CHECKSUM":
        val_calculated = checksum(text)
        
    if val_calculated == val_received:
        return "DATA CORRECT", val_calculated
    else:
        return "DATA CORRUPTED", val_calculated