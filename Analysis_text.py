from datetime import datetime
from fileinput import close
from collections import Counter

time_data = datetime.now().strftime('%c')          # переменная времени
time_data = time_data[-4:] + time_data[3:-4] # нужный мне формат
Mode_selection=''
while True:
    if Mode_selection=='':
        Mode_selection=input('''
Hello!!! I'm a text analyzer! I can help you with analysis of any text!
You can choose analysis of text from file or analysis of the entered text!

Please choose!!! :

If you want analysis of text from file.   Write me :  (1)
if you want analysis of the entered text. Write me :  (2)
if you want finish the program.           Write me :  (0)''')
    elif Mode_selection =='123':
        print('\nInvalid input! Try again!')
        Mode_selection = input('''
Please choose!!! :

If you want analysis of text from file.   Write me :  (1)
if you want analysis of the entered text. Write me :  (2)
if you want finish the program.           Write me :  (0)''')

    if Mode_selection == '1':

        while True: # просим ввести имя файла и присваеваем его пееременной текст если файла нет просим ввести по новой
            file=input('''
Write me name your file! 
The file must be location in the program folder!
Input form for file name : (file_name.txt)''')
            try:
                with open(file, encoding='utf-8') as file_text:
                    text=file_text.read()
                break
            except FileNotFoundError:
                print('''
\n\nI didn't find a file with this name! 
Try entering the file name again!\n''')

        text_length  =  len(text)
        #количество символов в тексте с пробелами |

        text_length_without_spaces_and_newline = len(text.replace(' ','')\
                                       .replace('\n', ''))
        #количество всех символов за исключенем переноса строки и пробела

        spaces_in_text    =  text.count(' ')
        #количество пробелов в строке

        newline_in_text   =  text.count('\n')
        #количество переносов строки

        text              =  text.lower()
        #приводим текст к нижнему регистру для адекватного анализа

        i = 0
        # переменая цыкла

        text_letters  =  ''
        #переменная для букв

        text_words    =  ''
        #переменная для слов

        text_SSymbol  =  ''
        # переменая для спец символов

        text_digit    =  ''
        #переменная для цыфр без потери смысла (тоесть 3.14 даты и тд)

        text_digit_symbol  =  ''
        # переменная для цыфр (для проверки сколько 1 или другой символ вст в тексте)

        proposals_in_text  =  0
        # переменная для подсчета количества предложений

        download1=0
        average_length = 0

        download2=0
        print('\n')

        name_file = input('Write me a name for the file name with text analysis!')
        name_file = name_file.strip() + '.txt'

        while len(text)>i:
            # цыкл для распределения данных из текста

            if text[i].isalpha():
                # проверяем на букву если да добовляем к переменной буква слово
                text_words += text[i]
                text_letters += text[i]
                if i>1 and text[i-1].isdigit() and(not text[i+1].isalpha() or not text[i+2].isalpha()):
                    text_digit += text[i]

            if text[i].isdigit():
                #проверка на цыфру если добовляем к переменным цыфрам
                text_digit += text[i]
                text_digit_symbol += text[i]

            if text[i] == ' ' or text[i] == '\n':
                # проверка на пробел\перенос если да добовляем ко всем спискам
                text_words += text[i]
                text_digit += text[i]
            if  text[i] == '\n':
                proposals_in_text  +=1

            if i>=2 and  not text[i].isalnum():
                # проверка на спец символ добовляем к переменной спец символов
                text_SSymbol += text[i] + ' '

                if i>=2 and not i+1==len(text) and ((text[i-1].isdigit() or text[i+1].isdigit())
                        # проверка на то являеться спецсимвол важным для числа
                        and not text[i-1].isalpha()):
                    text_digit += text[i]

                if text[i-1].isalpha() and not text[i-2].isalnum():
                    # проверка на анограмы
                    text_words += text[i]

                else: text_words += ' '
                # на всякий добовляем пробел после спец символа

            if ((i>2 and (text[i] in ( '!', '.', '?', )))
                    and text[i-1].isalpha() and text[i-2].isalpha()
                    and not text[i+1].isalpha()):
                # проверка на количество предложений
                proposals_in_text += 1

            download=100/len(text)
            download1+=download
            download2+=download

            if download1>=1: #окно загрузки
                print('█', end='')
                download-=1
            if download2>=(100-download):
                print('\n' + ' ' *60 + 'Analise finish! \n ')

            i += 1
        print('\n')

        text_words        =   text_words.split()
        #переводим к списку с сохранением структуры и смысла

        text_digit        =   text_digit.split()
        #переводим к списку с сохранением структуры и смысла

        text_letters      =   list(text_letters)
        #приводим к списку для анализа каждой буквы отдельно

        text_SSymbol      =   text_SSymbol.split()
        #переводим к списку с сохранением структуры и смысла

        text_digit_symbol = list(text_digit_symbol)
        # приводи к списку для анализа каждой цыфры отдельно


        number_of_text_digit          =  len(text_digit)
        # узнаем количество цыфр

        number_of_text_words          =  len(text_words)
        # узнаем количество слов

        number_of_text_SSymbol        =  len(text_SSymbol)
        # узнаем количество символов

        number_of_text_letters        =  len(text_letters)
        # узнаем количество букв

        number_of_text_digit_symbol   =   len(text_digit_symbol)
        # узнаем количество цыфр отдельно каждую


        unique_SSymbols        =  len(set(text_SSymbol))
        # узнаем количество унткальных симвалов

        unique_words           =  len(set(text_words))
        # узнаем количество уникальных слов

        unique_digits          =  len(set(text_digit))
        # узнаем количество уникальных цыфр целых

        unique_digits_symbol   =  len(set(text_digit_symbol))
        # узнаем количество уникальных цыфр по одной

        unique_litters         =  len(set(text_letters))
        # узнаем количество уникальных букв

        if len(text_digit)>0:
            average_length         =   round(number_of_text_letters
                                         /
                                         number_of_text_words, 3)
        #узнаем средную длину слова и округляем до 3 знаков

        counter_word    =   Counter(text_words)
        # делаем словаоь для выявления чяястотности слов

        counter_digit   =    Counter(text_digit)
        # делаем словаоь для выявления чяястотности цыфр целых

        counter_SSymbol  =   Counter(text_SSymbol)
        # делаем словаоь для выявления чяястотности символов

        counter_letters  =   Counter(text_letters)
        # делаем словаоь для выявления чяястотности букв

        counter_digit_symbol=Counter(text_digit_symbol)
        # делаем словаоь для выявления чяястотности цыфр по отдельности

        max_min_number_word_in_text    =    sorted(set(text_words), key=len)
        # сортруем словарь чтобы найти самое длинное короткое слово 5 тех и 5 тех

        d=max_min_number_word_in_text # создаю псевдоним

        words_list = list(counter_word.items())
        # делаем список из слов
        words_list.sort(key=len)

        digits_list = list(counter_digit.items())
        # делаем список из цифр
        digits_list.sort(key=len)

        letters_list = list(counter_letters.items())
        # делаем список из букв
        letters_list.sort()

        SSymbol_list = list(counter_SSymbol.items())
        # делаем список из спец символов

        digits_symbol_list = list(counter_digit_symbol.items())
        # делаем список из цыфр по символьно
        digits_symbol_list.sort()

        range_len = max(len(words_list), len(digits_list),
                        len(letters_list), len(SSymbol_list),
                        len(digits_symbol_list))
        #узнаем максимальную длинну среди всех списков

        t=len("Analysis text from file : ")+len(file)+4
        t2=len("Text analysis saved in file : ")+len(name_file)+4
        if t%2 == 1:
            t+=1
        if t2%2 ==1:
            t2+=1
        if t2>t:
            t=t2
        # для графической подгонки и формирования таблицы даты и названия файла

        if len(d)<5:
            r=5-len(d)
            d+=['-',]*r
        # для ситуаций с маленьким текстом


        text_for_file=f'''
{'*'*t:^140}
{"Analysis text from file : "+file:^142}
{"Text analysis saved in file : " + name_file:^142}
{'Data & time : '+time_data:^142}
{'*'*t:^140}
{'_'*142}
|{'Analysis Report':^140}|
{'_'*142}
| Total number of characters         | {f'{text_length} pcs':<102}|
| Without spaces and newlines        | {f'{text_length_without_spaces_and_newline} pcs':<102}|
| Number of spaces                   | {f'{spaces_in_text} pcs':<102}|
| Number of newlines                 | {f'{newline_in_text} pcs':<102}|
| Number of sentences                | {f'{proposals_in_text} pcs':<102}|
| Average word length                | {f'{average_length} pcs':<102}|
|{'-'*36}|{'-'*103}| 
| 5 shortest words                   | {d[0]+', '+d[1]+', '+d[2]+',':<102}|
|                                    | {d[3]+', '+d[4]+'.':<102}|
|{'-'*36}|{'-'*103}|                          
| 5 longest words                    | {d[-1]+', '+d[-2]+',':<102}|
|                                    | {d[-3]+', '+d[-4]+', '+ d[-5]+'.':<102}|
|{'-'*36}|{'-'*103}|              
| Letters in text                    | {f'{number_of_text_letters} pcs':<102}|
| Unique letters                     | {f'{unique_litters} pcs':<102}|
|{'-'*36}|{'-'*103}|
| Words in text                      | {f'{number_of_text_words} pcs':<102}|
| Unique words                       | {f'{unique_words} pcs':<102}|
|{'-'*36}|{'-'*103}|
| Numbers in text                    | {f'{number_of_text_digit} pcs':<102}|
| Unique numbers                     | {f'{unique_digits} pcs':<102}|
|{'-'*36}|{'-'*103}|
| Individual digits                  | {f'{number_of_text_digit_symbol} pcs':<102}|
| Unique individual digits           | {f'{unique_digits_symbol} pcs':<102}|
|{'-'*36}|{'-'*103}|
| Special symbols in text            | {f'{number_of_text_SSymbol} pcs':<102}|
| Unique special symbols             | {f'{unique_SSymbols} pcs':<102}|
{'='*142}

{'-'*142}
|{'Text frequency analysis table':^140}|
{'-'*142}
|{'Word':^23}|{'Count':^12}| |{'letters':^9}|{'Count':^12}| |{'SSymbol':^9}|{'Count':^12}| |{'SymDigit':^10}|{'Count':^12}| |{'Digit':^12}|{'Count':^12}|
{'-'*142}
'''
        for i in range(range_len):

            if len(words_list)>i:
                w=words_list[i]
            else:
                w=('-', '0')
            if len(digits_list) > i:
                d = digits_list[i]
            else:
                d = ('-', '0')
            if len(letters_list) > i:
                l = letters_list[i]
            else:
                l = ('-', '0')
            if len(SSymbol_list) > i:
                SS = SSymbol_list[i]
            else:
                SS = ('-', '0')
            if len(digits_symbol_list) > i:
                ds = digits_symbol_list[i]
            else:
                ds = ('-', '0')
            text_for_file+=\
                f'|{w[0]:^23}|{f'{w[1]} pcs':^12}| |{l[0]:^9}|{f'{l[1]} pcs':^12}| |{SS[0]:^9}|{f'{SS[1]} pcs':^12}| |{ds[0]:^10}|{f'{ds[1]} pcs':^12}| |{d[0]:^12}|{f'{d[1]} pcs':^12}|\n'
        text_for_file+=f'{'-'*142}'

        with open(name_file, 'a+', encoding='utf-8') as file_text:
            file_text.write('\n'*5+text_for_file)
        print(text_for_file)

        Mode_selection = input('''
The program has finished analyzing the text!!!

If you want finish the program        Write me :  (0)
If you want a new text analysis       Write me :  (1)''')
        if not Mode_selection == 0 and Mode_selection == 1:
            Mode_selection='123'
            continue

    elif Mode_selection == '2':
        text = input('Write me your text!!!')

        text_length = len(text)
        # количество символов в тексте с пробелами |

        text_length_without_spaces_and_newline = len(text.replace(' ', '') \
                                                     .replace('\n', ''))
        # количество всех символов за исключенем переноса строки и пробела

        spaces_in_text = text.count(' ')
        # количество пробелов в строке

        newline_in_text = text.count('\n')
        # количество переносов строки

        text = text.lower()
        # приводим текст к нижнему регистру для адекватного анализа

        i = 0
        # переменая цыкла

        text_letters = ''
        # переменная для букв

        text_words = ''
        # переменная для слов

        text_SSymbol = ''
        # переменая для спец символов

        text_digit = ''
        # переменная для цыфр без потери смысла (тоесть 3.14 даты и тд)

        text_digit_symbol = ''
        # переменная для цыфр (для проверки сколько 1 или другой символ вст в тексте)

        proposals_in_text = 0
        # переменная для подсчета количества предложений

        download1 = 0

        download2 = 0
        print('\n')

        name_file = input('Write me a name for the file name with text analysis!')
        name_file = name_file.strip() + '.txt'

        while len(text) > i:
            # цыкл для распределения данных из текста

            if text[i].isalpha():
                # проверяем на букву если да добовляем к переменной буква слово
                text_words += text[i]
                text_letters += text[i]
                if i > 1 and text[i - 1].isdigit() and (not text[i + 1].isalpha() or not text[i + 2].isalpha()):
                    text_digit += text[i]

            if text[i].isdigit():
                # проверка на цыфру если добовляем к переменным цыфрам
                text_digit += text[i]
                text_digit_symbol += text[i]

            if text[i] == ' ' or text[i] == '\n':
                # проверка на пробел\перенос если да добовляем ко всем спискам
                text_words += text[i]
                text_digit += text[i]
            if text[i] == '\n':
                proposals_in_text += 1

            if i >= 2 and not text[i].isalnum():
                # проверка на спец символ добовляем к переменной спец символов
                text_SSymbol += text[i] + ' '

                if i >= 2 and not i + 1 == len(text) and ((text[i - 1].isdigit() or text[i + 1].isdigit())
                                                          # проверка на то являеться спецсимвол важным для числа
                                                          and not text[i - 1].isalpha()):
                    text_digit += text[i]

                if text[i - 1].isalpha() and not text[i - 2].isalnum():
                    # проверка на анограмы
                    text_words += text[i]

                else:
                    text_words += ' '
                # на всякий добовляем пробел после спец символа

            if ((i > 2 and (text[i] in ('!', '.', '?',)))
                    and text[i - 1].isalpha() and text[i - 2].isalpha()
                    and not text[i + 1].isalpha()):
                # проверка на количество предложений
                proposals_in_text += 1

            download = 100 / len(text)
            download1 += download
            download2 += download

            if download1 >= 1:  # окно загрузки
                print('█', end='')
                download -= 1
            if download2 >= (100 - download):
                print('\n' + ' ' * 60 + 'Analise finish! \n ')

            i += 1
        print('\n')

        text_words = text_words.split()
        # переводим к списку с сохранением структуры и смысла

        text_digit = text_digit.split()
        # переводим к списку с сохранением структуры и смысла

        text_letters = list(text_letters)
        # приводим к списку для анализа каждой буквы отдельно

        text_SSymbol = text_SSymbol.split()
        # переводим к списку с сохранением структуры и смысла

        text_digit_symbol = list(text_digit_symbol)
        # приводи к списку для анализа каждой цыфры отдельно

        number_of_text_digit = len(text_digit)
        # узнаем количество цыфр

        number_of_text_words = len(text_words)
        # узнаем количество слов

        number_of_text_SSymbol = len(text_SSymbol)
        # узнаем количество символов

        number_of_text_letters = len(text_letters)
        # узнаем количество букв

        number_of_text_digit_symbol = len(text_digit_symbol)
        # узнаем количество цыфр отдельно каждую

        unique_SSymbols = len(set(text_SSymbol))
        # узнаем количество унткальных симвалов

        unique_words = len(set(text_words))
        # узнаем количество уникальных слов

        unique_digits = len(set(text_digit))
        # узнаем количество уникальных цыфр целых

        unique_digits_symbol = len(set(text_digit_symbol))
        # узнаем количество уникальных цыфр по одной

        unique_litters = len(set(text_letters))
        # узнаем количество уникальных букв

        average_length=0

        if len(text_digit) > 0:
            average_length = round(number_of_text_letters
                                   /
                                   number_of_text_words, 3)
        # узнаем средную длину слова и округляем до 3 знаков

        counter_word = Counter(text_words)
        # делаем словаоь для выявления чяястотности слов

        counter_digit = Counter(text_digit)
        # делаем словаоь для выявления чяястотности цыфр целых

        counter_SSymbol = Counter(text_SSymbol)
        # делаем словаоь для выявления чяястотности символов

        counter_letters = Counter(text_letters)
        # делаем словаоь для выявления чяястотности букв

        counter_digit_symbol = Counter(text_digit_symbol)
        # делаем словаоь для выявления чяястотности цыфр по отдельности

        max_min_number_word_in_text = sorted(set(text_words), key=len)
        # сортруем словарь чтобы найти самое длинное короткое слово 5 тех и 5 тех

        d = max_min_number_word_in_text  # создаю псевдоним

        words_list = list(counter_word.items())
        # делаем список из слов
        words_list.sort(key=len)

        digits_list = list(counter_digit.items())
        # делаем список из цифр
        digits_list.sort(key=len)

        letters_list = list(counter_letters.items())
        # делаем список из букв
        letters_list.sort()

        SSymbol_list = list(counter_SSymbol.items())
        # делаем список из спец символов

        digits_symbol_list = list(counter_digit_symbol.items())
        # делаем список из цыфр по символьно
        digits_symbol_list.sort()

        range_len = max(len(words_list), len(digits_list),
                        len(letters_list), len(SSymbol_list),
                        len(digits_symbol_list))
        # узнаем максимальную длинну среди всех списков


        t = len("Text analysis saved in file : ") + len(name_file) + 4
        if t % 2 == 1:
            t += 1
        # для графической подгонки и формирования таблицы даты и названия файла
        if len(d)<5:
            r=5-len(d)
            d+=['-',]*r



        text_for_file = f'''
{'*' * t:^140}
{"Text analysis saved in file : " + name_file:^142}
{'Data & time : ' + time_data:^142}
{'*' * t:^140}
{'_' * 142}
|{'Analysis Report':^140}|
{'_' * 142}
| Total number of characters         | {f'{text_length} pcs':<102}|
| Without spaces and newlines        | {f'{text_length_without_spaces_and_newline} pcs':<102}|
| Number of spaces                   | {f'{spaces_in_text} pcs':<102}|
| Number of newlines                 | {f'{newline_in_text} pcs':<102}|
| Number of sentences                | {f'{proposals_in_text} pcs':<102}|
| Average word length                | {f'{average_length} pcs':<102}|
|{'-' * 36}|{'-' * 103}| 
| 5 shortest words                   | {d[0] + ', ' + d[1] + ', ' + d[2] + ',':<102}|
|                                    | {d[3] + ', ' + d[4]+'.':<102}|
|{'-' * 36}|{'-' * 103}|                          
| 5 longest words                    | {d[-1] + ', ' + d[-2]+',':<102}|
|                                    | {d[-3] + ', ' + d[-4] + ', ' + d[-5]+'.':<102}|
|{'-' * 36}|{'-' * 103}|              
| Letters in text                    | {f'{number_of_text_letters} pcs':<102}|
| Unique letters                     | {f'{unique_litters} pcs':<102}|
|{'-' * 36}|{'-' * 103}|
| Words in text                      | {f'{number_of_text_words} pcs':<102}|
| Unique words                       | {f'{unique_words} pcs':<102}|
|{'-' * 36}|{'-' * 103}|
| Numbers in text                    | {f'{number_of_text_digit} pcs':<102}|
| Unique numbers                     | {f'{unique_digits} pcs':<102}|
|{'-' * 36}|{'-' * 103}|
| Individual digits                  | {f'{number_of_text_digit_symbol} pcs':<102}|
| Unique individual digits           | {f'{unique_digits_symbol} pcs':<102}|
|{'-' * 36}|{'-' * 103}|
| Special symbols in text            | {f'{number_of_text_SSymbol} pcs':<102}|
| Unique special symbols             | {f'{unique_SSymbols} pcs':<102}|
{'=' * 142}

{'-' * 142}
|{'Text frequency analysis table':^140}|
{'-' * 142}
|{'Word':^23}|{'Count':^12}| |{'letters':^9}|{'Count':^12}| |{'SSymbol':^9}|{'Count':^12}| |{'SymDigit':^10}|{'Count':^12}| |{'Digit':^12}|{'Count':^12}|
{'-' * 142}
'''
        for i in range(range_len):

            if len(words_list) > i:
                w = words_list[i]
            else:
                w = ('-', '0')
            if len(digits_list) > i:
                d = digits_list[i]
            else:
                d = ('-', '0')
            if len(letters_list) > i:
                l = letters_list[i]
            else:
                l = ('-', '0')
            if len(SSymbol_list) > i:
                SS = SSymbol_list[i]
            else:
                SS = ('-', '0')
            if len(digits_symbol_list) > i:
                ds = digits_symbol_list[i]
            else:
                ds = ('-', '0')
            text_for_file += \
                f'|{w[0]:^23}|{f'{w[1]} pcs':^12}| |{l[0]:^9}|{f'{l[1]} pcs':^12}| |{SS[0]:^9}|{f'{SS[1]} pcs':^12}| |{ds[0]:^10}|{f'{ds[1]} pcs':^12}| |{d[0]:^12}|{f'{d[1]} pcs':^12}|\n'
        text_for_file += f'{'-' * 142}'

        with open(name_file, 'a+', encoding='utf-8') as file_text:
            file_text.write('\n'*5+text_for_file)
        print(text_for_file)

        Mode_selection = input('''
The program has finished analyzing the text!!!

If you want finish the program        Write me :  (0)
If you want a new text analysis       Write me :  (1)''')
        if not Mode_selection == 0 and Mode_selection == 1:
            Mode_selection = '123'
            continue

    elif Mode_selection == '0':
        print('Program finish! Have Good day')
        break

    else:
        Mode_selection='123'
