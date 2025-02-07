def is_valid_temperature(temp, unit):
    if unit == 'C' and (temp>=0 and temp<=100):
        return True
    elif unit == 'F' and (temp>=32 and temp<=212):
        return True
    else:
        return False


print(is_valid_temperature(240, 'F'))