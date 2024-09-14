import random
import json
import string

alphabet = '    ' + ' ' + string.punctuation + string.ascii_letters + string.digits
def crypter(message, key, direction=1):
    key_index = 0
    encrypted_message = ''
    for char in message:
        key_char = key[key_index % len(key)]
        key_index += 1
        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset*direction) % len(alphabet)
        encrypted_message += alphabet[new_index]
    return encrypted_message

def decrypt(message, key):
    return crypter(message, key, -1)
def encrypt(message, key):
    return crypter(message, key)
def save_questions(element, name):
    file = open(f'./{name}.json', 'w')
    file.write(json.dumps(element))
    file.close()
    return
def read_questions():
    path = './' + input('File\'s name : ') + '.json'
    file = open(path, 'r')
    reader = file.read()
    file.close()
    return json.loads(reader)
def create_list(questions):
    new_test = input('WORD:TRADUCTION >>> ')
    if new_test.lower() != 'none' and new_test.lower() != 'exit':
        new_word = new_test[0:new_test.index(':')]
        new_trad = new_test[new_test.index(':') + 1:len(new_test)]
        questions.update({f'{new_word}': f'{new_trad}'})
        print(questions)
        create_list(questions)
    else:
        save = input('Save questions ? [y/n] ')
        if save.lower() == 'y' or save.lower() == 'yes':
            file_name = input('File\'s name : ')
            passw = input('File\'s password : ')
            new_questions = {'code_path': encrypt('lbcode', passw)}
            for i in questions:
                new_questions.update({f'{i}': f'{encrypt(questions[i], passw)}'})
            save_questions(new_questions, file_name)
    return questions
def tester(questions):
    passw = input('File\'s password : ')
    print(questions['code_path'])
    if decrypt(questions['code_path'], passw) == 'lbcode':
        note = 0
        evaluator = questions.copy()
        result = ['\n']
        i = 0
        while i < len(questions) - 1:
            x = random.randint(1, len(evaluator) - 1)
            print(len(evaluator), x)
            element = list(evaluator.keys())[x]
            response = input(f'{element[0].upper() + element[1:len(element)].lower()} ? ')
            if response == decrypt(evaluator.get(element.lower()), passw) and evaluator.get(element.lower()):
                print('\033[1;92mCorrect\033[0m')
                result.append(f'\033[1;92m{element} : {decrypt(questions.get(element), passw)}\033[0m')
                note += 1
            else:
                print('\033[1;31mIncorrect\033[0m')
                result.append(f'\033[1;31m{element} : {decrypt(questions.get(element), passw)}\033[0m')
            del evaluator[element]
            i += 1
        for i in result:
            print(i)
        print(f'\033[1;34m{note}/{len(questions) - 1}\033[0m')
    else:
        print('Wrong password.')
        defaulter()
def defaulter():
    todo = input('>>> ')
    if todo == 'create':
        create_list({})
        defaulter()
    elif todo == 'test':
        tester(read_questions())
        defaulter()
    elif todo == 'exit' or todo == 'quit' or todo == 'q':
        print('\nGood bye.')
    else:
        print(f'\'{todo}\' is not a command.')
        defaulter()
defaulter()