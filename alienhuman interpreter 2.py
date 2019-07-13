import csv
while True:
    display = input('Press enter to continue ----- pre entret fo kontino')
    print('-------------------- Welcome to the main menu Aliens and Humans -------------------- \n\
        Enter an option of your choice ---- echer nu topion fo rou kois\n\
        1. English to Aliench ---- English tre Aliench \n\
        2. Aliench to English ---- Aliench to English \n\
        3. Add a new word ---- adt nuo wurr')
    
    try:
        choice = int(input('Choice ---- Kois : '))

        if choice == 1:
            with open('dictionary2.csv','r') as eng:
                reader = csv.reader(eng, delimiter = ',')
                print('English to Aliench')
                find_word = input('Enter an english word : ')
                for line in reader:
                    if line[0] == find_word.lower() :
                        print(find_word.lower(), ':', line[1])

        elif choice == 2:
            with open('dictionary2.csv','r') as aln:
                reader = csv.reader(aln, delimiter = ',')
                print('Aliench tre English')
                find_word = input('Entro ne alieniish wurr : ')
                for line in reader:
                    if line[1] == find_word.lower():
                        print(find_word, ':', line[0])

        elif choice == 3:
            print('Add a new word ---- adt nuo wurr')
            print('Enter the english word ---- Entro de english wurr')
            eng_word = input(': ')
            print('Enter the alienish word ---- Entro de alienish wurr')
            aln_word = input(': ')
            with open('dictionary2.csv','a+', newline = '') as new:
                new_word = eng_word , aln_word + ' '
                writer = csv.writer(new)
                writer.writerow(new_word)
                print('Word has been added ---- wurr shukre iatde')
        
        else:
            print('Invalid entry ---- iroi entrio')


    except ValueError:
        print('Invalid entry  ---- iroi entrio')
    except:
        print('An error has occured')
