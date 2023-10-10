import csv

def main():
    print("Welcome to our pet information page.")

    try:
        choice = int(input("Which animal are you trying to look for?\n1. Dog\n2. Cat\n"))

    except ValueError:
        print('\n\n*****!Please input only the integers 1 or 2!******\n\n')
        return main()

    if choice == 1:
        print("Here is our dogs:\n")
        dogs = []

        with open('./data/dogs.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            
            
            try:
                for row in csv_reader:
                    animal_info = {
                        'Name': row['name'],
                        'Age': row[' age'].strip(),
                        'Breed': row[' breed'].strip()
                    }
                    dogs.append(animal_info)

                for dog in dogs:
                    print(f'{dog["Name"]}, {dog["Name"]} is {dog["Age"]} years old and a {dog["Breed"]}.')

            except FileNotFoundError:
                print('File not found!')
            except Exception as e:
                print(f'An error occurred: {e}')

    elif choice == 2:
        print("Here is our cats:\n")

        cats = []

        try:
            with open('./data/cats.csv', 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    animal_info = {
                        'Name': row['name'],
                        'Age': row[' age'].strip(),
                        'Breed': row[' breed'].strip()
                    }
                    cats.append(animal_info)

            
                for cat in cats:
                    print(f'{cat["Name"]}, {cat["Name"]} is {cat["Age"]} years old and a {cat["Breed"]}.')
        except FileNotFoundError:
            print('File not found!')
        except Exception as e:
            print(f'An error occurred: {e}')

    else: print("\nPlease input the values 1 or 2.\n1 for dogs, 2 for cats.")

main()
