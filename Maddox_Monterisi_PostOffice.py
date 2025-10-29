def zone(zipcode):
    '''
    Description: converts the zipcode that the user inputed into a zone
    Args:
        zipcode(int): zipcode input
    returns:
        the zone based on the zipcode
    '''
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
    '''
    Description: finds the number of zones between the startzone and endzone
    Args:
        startzip(int): the start zipcode
        endzip(int): the start zipcode and end zipcode
    returns: 
        number of zones between start and end
    '''
    startzone = zone(startzip)
    endzone = zone(endzip)

    if startzone == -1 or endzone == -1:
        return -1
    return abs(startzone - endzone)

def find_type(length, height, thickness):
    '''
    Description: finds the type of package based on dimnesions
    Args:
        length(int): input of length
        height(int): input of height
        thickness(int): input of thickness
    returns:
        type of package
    '''
    perim = length * 2 * (height + thickness)
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= thickness <= .016:
        return 'Regular Post Card'
    elif 4.25 < length < 6 and 6 < height < 11.50 and .007 <= thickness <= .015:
        return 'Large Post Card'
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 < thickness < .25:
        return 'Envelope'
    elif 6.125 < length < 24 and 11 <= height <= 18 and .25 <= thickness <= .50:
        return 'Large Envelope'
    elif length > 24 or height > 11 or thickness > 18 and perim <= 84:
        return 'Package'
    elif length > 24 or height > 11 or thickness > 18 and 84 < perim <= 130:
        return 'Large Package'
    else:
        return 'UNMAILABLE'

def find_cost(post_type, total_zones):
    '''
    Description: finds cost of package/postcard
    Args:
        post_type(str): the result of the previous function 
        total_zones(int): the zones traveled
    returns:
        cost of each package taking into account the zones traveled.
    '''
    if post_type == 'Regular Post Card':
        cost = .20 + .03 * total_zones
    elif post_type == 'Large Post Card':
        cost = .37 + .03 * total_zones
    elif post_type == 'Envelope':
        cost = .37 + .04 * total_zones
    elif post_type == 'Large Envelope':
        cost = .60 + + .05 * total_zones
    elif post_type == 'Package':
        cost = 2.95 + .25 * total_zones
    elif post_type == 'Large Package':
        cost = 3.95 + .35 * total_zones
    else:
        cost = 'UNMAILABLE'
    return cost

def interpret_info(info):
    '''
    Description: interprets the info into readable variables
    Args:
        info(str): the info for the zipcodes and dimensions
    returns:
        all the data as variables
    '''
    info = info.split(',')
    length = float(info[0])
    height = float(info[1])
    thickness = float(info[2])
    startzip = int(info[3])
    endzip = int(info[4])
    return length, height, thickness, startzip, endzip 

def format(cost):
    '''
    Description: makes sure the final price is formatted without a zero before the decimal place
    Args:
        cost(int): the total cost of the postage/package factoring in the zones traveled
    returns:
        formatted final price
    '''
    if cost == 'UNMAILABLE':
        return 'UNMAILABLE'
    finalprice = (f'{cost:.2f}')
    if finalprice[0] == '0':
        finalprice = finalprice[1:]
    return finalprice

def main():
    info = input('What is the length, height, and thickness of your card and what zipcode are you mailing from and to? ')
    length, height, thickness, startzip, endzip = interpret_info(info)
    card_type = find_type(length, height, thickness)
    total_zones = find_distance(startzip, endzip)
    cost = find_cost(card_type, total_zones)
    print(format(cost))
main()