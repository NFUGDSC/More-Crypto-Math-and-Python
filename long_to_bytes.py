def long_to_bytes(long):
    result = ""
    for i in range(len(str(long))):
        result+=(chr(long >> (i * 8) & 0xff))
    return result[::-1]
