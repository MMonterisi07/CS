try:
    with open('titanic.csv', 'r') as file:
        header = file.readline().strip().split(',')  # Read the header row
        name_index = header.index('Name')  # Find the index of 'Name' column
       
        for line in file:
            row = line.strip().split(',')
            print(row)
            print(row[name_index])
except FileNotFoundError:
    print("Error: 'titanic.csv' file not found.")
def read_csv_manual(filename, delimiter=','):
    data = []

    with open(filename, 'r') as file:
        for line in file:
            row = [cell.strip() for cell in line.strip().split(delimiter)]
            data.append(row)
    return data

my_data = read_csv_manual('titanic.csv')
print(my_data)
def survival_rate()
