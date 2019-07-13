while True:
    display = input('Press enter to continue ----- pre entret fo kontino')
    print('-------------------- Welcome to the main menu Aliens and Humans -------------------- \n\
        Enter an option of your choice ---- echer nu topion fo rou kois\n\
        1. English to Aliench ---- English tre Aliench \n\
        2. Aliench to English ---- Aliench to English')
    
    try:
        choice = int(input('Choice ---- Kois : '))

        if choice == 1:
            with open('englishdict.txt','r') as eng:
                eng_dict = eval(eng.read())

            print('English to Aliench')
            find_word = input('Enter an english word : ')
            for key in eng_dict.keys():
                if find_word == key:
                    print(key,' :',eng_dict[key])

        elif choice == 2:
            with open('englishdict.txt','r') as aln:
                aln_dict = eval(aln.read())

            print('Aliench tre English')
            find_word = input('Enor ne english wur : ')
            for key, value in aln_dict.items():
                if find_word == value:
                    print(value,' :',key)
        else:
            print('Invalid entry ---- iroi entrio')

    except ValueError:
        print('Invalid entry  ---- iroi entrio')
    except:
        print('An error has occured')
