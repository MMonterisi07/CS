def zone(zipcode):
    if 1 <= zipcode <= 6999:
        return 1
    elif zipcode >= 7000 and zipcode <= 19999:
        return 2
    elif zipcode >= 20000 and zipcode <= 35999:
        return 3
    elif zipcode >= 36000 and zipcode <= 62999:
        return 4
    elif zipcode >= 63000 and zipcode <= 84999:
        return 5
    elif zipcode >= 85000 and zipcode <= 99999:
        return 6
    else:
        return -1
def find_distance(startzip, endzip):
    startzone = zone(startzip)
    endzone = zone(endzip)
    total_zones = abs(startzone - endzone)
    return total_zones
def find_type(length, height, thickness):
    pre_perim = height + thickness
    pre_perim2 = pre_perim * 2
    perim = length * pre_perim2
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= thickness <= .016:
        type = 'Regular Post Card'
    elif 4.25 < length < 6 and 6 < height < 11.50 and .007 <= thickness <= .015:
        type = 'Large Post Card'
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 < thickness < .25:
        type = 'Envelope'
    elif 6.125 < length < 24 and 11 <= height <= 18 and .25 <= thickness <= .50:
        type = 'Large Envelope'
    elif length > 24 and height > 11 and thickness > 18 and perim <= 84:
        type = 'Package'
    elif length > 24 and height > 11 and thickness > 18 and 84 < perim <= 130:
        type = 'Large Package'
    else:
        return 'Unmailable'
    return type
def find_cost(type, total_zones):
    if type == 'Regular Post Card':
        cost = .20 + .03 * total_zones
    elif type == 'Large Post Card':
        cost = .37 + .03 * total_zones
    elif type == 'Envelope':
        cost = .37 + .04 * total_zones
    elif type == 'Large Envelope':
        cost = .60 + + .05 * total_zones
    elif type == 'Package':
        cost = 2.95 + .25 * total_zones
    elif type == 'Large Package':
        cost = 3.95 + .35 * total_zones
    return cost
def interpret_info(info):
    info = info.split(',')
    length = float(info[0])
    height = float(info[1])
    thickness = float(info[2])
    startzip = int(info[3])
    endzip = int(info[4])
    return length, height, thickness, startzip, endzip 
def format(cost):
    finalprice = f'{cost:.2f}'
    if finalprice[0] == '0':
        finalprice = finalprice[1:]
    return f'{cost:.2f}'
def format_zipcode(startzip, endzip):
    
def main():
    info = input('What is the length, height, and thickness of your card and what zipcode are you mailing from and to? ')
    length, height, thickness, startzip, endzip = interpret_info(info)
    card_type = find_type(length, height, thickness)
    total_zones = find_distance(startzip, endzip)
    cost = find_cost(card_type, total_zones)
    print(format(cost))
main()