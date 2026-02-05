def load_10_data():
    try:
        with open('titanic.csv', 'r') as file:
            header = file.readline().strip().split(',')  # Read the header row
            name_index = header.index('Name')  # Find the index of 'Name' column
            num_rows = 0
            for line in file:
                row = line.strip().split(',')
                print(row)
                num_rows += 1
                print(row[name_index])
                if num_rows == 10:
                    break

    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")

def overall_survival_rate(file):
    file.seek(0)
    next(file)
    num_survived = 0
    total_passengers = 0

    for line in file:
        row = line.strip().split(',')
        total_passengers +=1

        if row[1] == '1':
            num_survived += 1
    surv_rate = (num_survived/total_passengers)*100
    print(f'The overall survival rate is: {surv_rate:.2f}%')

def survival_rate_gender():
    try:
        with open('titanic.csv', 'r') as file:
            male = 0
            female = 0
            totalM = 0
            totalF = 0
            for line in file:
                row = line.strip().split(',')
                if row[5] == 'male':
                    totalM += 1
                else:
                    totalF += 1
                if row[1] == '1' and row [5] == ('male'):
                    male +=1
                if row[1] == '1' and row [5] == ('female'):
                    female += 1
            male_rate = (male/totalM)*100
            female_rate = (female/totalF)*100
            print(f'The male survival rate is: {male_rate:.2f}%')
            print(f'The female survival rate is: {female_rate:.2f}%')
            print('Females have a higher survival rate. ')
    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")

def age_analysis(file):
    file.seek(0)
    next(file)

    ages = []
    ages_survived = []
    ages_not_survived = []

    for line in file:
        row = line.strip().split(',')
        if row[6] == '':
            continue
        age = float(row[6])
        ages.append(age)

        if row[1] == '1':
            ages_survived.append(age)
        else:
            ages_not_survived.append(age)
    lowest_age = min(ages)
    highest_age = max(ages)

    overall_average_age = sum(ages) / len(ages) if ages else 0
    average_age_survived = sum(ages_survived) / len(ages_survived) if ages_survived else 0
    average_age_not_survived = sum(ages_not_survived) / len(ages_not_survived) if ages_not_survived else 0
    
    print(f'The average age for all passengers is {overall_average_age}')
    print(f'The average age for survivors is {average_age_survived}')
    print(f'The average age for non-survivors is {average_age_not_survived}')
    print(f'The highest age on the Titanic was {highest_age}')
    print(f'The lowest age on the Titanic was {lowest_age}')

def class_analysis(file):
    file.seek(0)
    next(file)

    first_class_amount = 0
    second_class_amount = 0
    third_class_amount = 0

    first_class_survived = 0
    second_class_survived = 0
    third_class_survived = 0

    first_class_fares = []
    second_class_fares = []
    third_class_fares = []


    for row in file:
        row = row.strip().split(',')
        survived = row[1]
        pclass = row[2]
        fare = float(row[10])

        if pclass == '1':
            first_class_amount += 1
            first_class_fares.append(fare)
            if survived == '1':
                first_class_survived += 1

        if pclass == '2':
            second_class_amount += 1
            second_class_fares.append(fare)
            if survived == '1':
                second_class_survived += 1

        if pclass == '3':
            third_class_amount += 1
            third_class_fares.append(fare)
            if survived == '1':
                third_class_survived += 1


    first_class_surv_rate = (first_class_survived/first_class_amount)*100
    second_class_surv_rate = (second_class_survived/second_class_amount)*100
    third_class_surv_rate = (third_class_survived/third_class_amount)*100

    average_fare1 = sum(first_class_fares) / len(first_class_fares)
    average_fare2 = sum(second_class_fares) / len(second_class_fares)
    average_fare3 = sum(third_class_fares) / len(third_class_fares)

    print(f'The first class survival rate is {first_class_surv_rate:.2f}%')
    print(f'The second class survival rate is {second_class_surv_rate:.2f}%')
    print(f'The third class survival rate is {third_class_surv_rate:.2f}%')
    print('The first class had the best survival rate, followed by the second class, then the third class.')
    print(f'The average fare for 1st class is {average_fare1:.2f}')
    print(f'The average fare for 2nd class is {average_fare2:.2f}')
    print(f'The average fare for 3rd class is {average_fare3:.2f}')

def family_analysis(file):
    file.seek(0)
    header = file.readline().strip().split(',')

    SibSp_index = header.index('SibSp')
    ParCh_index = header.index('Parch')
    survived_index = header.index('Survived')

    family_amount = 0
    nofamily_amount = 0
    family_survived = 0
    nofamily_survived = 0

    familysize2 = 0
    familysize2_survived = 0
    familysize3 = 0
    familysize3_survived = 0
    familysize4 = 0
    familysize4_survived = 0
    familysize5 = 0
    familysize5_survived = 0
    familysize6 = 0
    familysize6_survived = 0
    familysize7 = 0
    familysize7_survived = 0
    familysize8 = 0
    familysize8_survived = 0

    for line in file:
        row = line.strip().split(',')
        sibsp = row[SibSp_index].strip('"')
        parch = row[ParCh_index].strip('"')
        survived = row[survived_index].strip('"')

        if not sibsp.isdigit() or not parch.isdigit():
            continue

        size = int(sibsp) + int(parch) + 1

        if size == 1:
            nofamily_amount += 1
            if survived == '1':
                nofamily_survived += 1
        else:
            family_amount += 1
            if survived == '1':
                family_survived += 1

            if size == 2:
                familysize2 += 1
                if survived == '1':
                    familysize2_survived += 1
            elif size == 3:
                familysize3 += 1
                if survived == '1':
                    familysize3_survived += 1
            elif size == 4:
                familysize4 += 1
                if survived == '1':
                    familysize4_survived += 1
            elif size == 5:
                familysize5 += 1
                if survived == '1':
                    familysize5_survived += 1
            elif size == 6:
                familysize6 += 1
                if survived == '1':
                    familysize6_survived += 1
            elif size == 7:
                familysize7 += 1
                if survived == '1':
                    familysize7_survived += 1
            elif size == 8:
                familysize8 += 1
                if survived == '1':
                    familysize8_survived += 1

    nofamily_survivalrate = (nofamily_survived / nofamily_amount) * 100 if nofamily_amount else 0
    family_survivalrate = (family_survived / family_amount) * 100 if family_amount else 0
    familysize2_rate = (familysize2_survived / familysize2) * 100 if familysize2 else 0
    familysize3_rate = (familysize3_survived / familysize3) * 100 if familysize3 else 0
    familysize4_rate = (familysize4_survived / familysize4) * 100 if familysize4 else 0
    familysize5_rate = (familysize5_survived / familysize5) * 100 if familysize5 else 0
    familysize6_rate = (familysize6_survived / familysize6) * 100 if familysize6 else 0
    familysize7_rate = (familysize7_survived / familysize7) * 100 if familysize7 else 0
    familysize8_rate = (familysize8_survived / familysize8) * 100 if familysize8 else 0

    print(f'The survival rate for a person with no family is {nofamily_survivalrate:.2f}%')
    print(f'The survival rate for a person with any family is {family_survivalrate:.2f}%')
    print(f'The survival rate for a person with a family size of 2 is {familysize2_rate:.2f}%')
    print(f'The survival rate for a person with a family size of 3 is {familysize3_rate:.2f}%')
    print(f'The survival rate for a person with a family size of 4 is {familysize4_rate:.2f}%')
    print(f'The survival rate for a person with a family size of 5 is {familysize5_rate:.2f}%')
    print(f'The survival rate for a person with a family size of 6 is {familysize6_rate:.2f}%')
    print(f'The survival rate for a person with a family size of 7 is {familysize7_rate:.2f}%')
    print(f'The survival rate for a person with a family size of 8 is {familysize8_rate:.2f}%')
            
def main():
    filename = 'titanic.csv'
    with open(filename, 'r') as file:
        while True:
            choice = input('''
                    What do you want:
                    1) load 10 lines
                    2) overall survival rate
                    3) survival by gender
                    4) age analysis
                    5) class analysis
                    6) family analysis
                    '''
                    )
            if choice == '1':
                load_10_data()
            elif choice == '2':
                overall_survival_rate(file)
            elif choice == '3':
                survival_rate_gender()
            elif choice == '4':
                age_analysis(file)
            elif choice == '5':
                class_analysis(file)
            elif choice == '6':
                family_analysis(file)

main()