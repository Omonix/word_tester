import random
import json
import math

def lb_save_questions(element, name):
    file = open(f'./{name}.json', 'w')
    file.write(json.dumps(element))
    file.close()
    return
def lb_read_questions():
    path = './' + input('File\'s name : ') + '.json'
    file = open(path, 'r')
    reader = file.read()
    file.close()
    return json.loads(reader)
def lb_create_list(questions):
    new_test = input('WORD:TRADUCTION >>> ')
    if new_test.lower() != 'none' and new_test.lower() != 'exit':
        if new_test.index(':'):
            new_word = new_test[0:new_test.index(':')]
            new_trad = new_test[new_test.index(':') + 1:len(new_test)]
            questions.update({f'{new_word}': f'{new_trad}'})
            lb_create_list(questions)
        else:
            print(f'Error: {new_test}')
            lb_create_list(questions)
    else:
        save = input('Save questions ? [y/n] ')
        if save.lower() == 'y' or save.lower() == 'yes':
            file_name = input('File\'s name : ')
            lb_save_questions(questions, file_name)
    return questions
def lb_upper_0(word):
    return word[0].upper() + word[1:len(word)].lower()
def lb_tester(questions):
    note = 0
    evaluator = questions.copy()
    result = ['\n']
    i = 0
    while i < len(questions):
        x = math.floor(random.random() * len(evaluator))
        element = list(evaluator.keys())[x]
        response = input(f'{element[0].upper() + element[1:len(element)].lower()} ? ')
        if response == evaluator.get(element.lower()) and evaluator.get(element.lower()):
            print('\033[1;92mCorrect\033[0m')
            result.append(f'\033[1;92m{lb_upper_0(element)} : {lb_upper_0(questions.get(element))}\033[0m')
            note += 1
        else:
            print('\033[1;31mIncorrect\033[0m')
            result.append(f'\033[1;31m{lb_upper_0(element)} : {questions.get(element)}\033[0m')
        del evaluator[element]
        i += 1
    for i in result:
        print(i)
    print(f'\033[1;34m{note}/{len(questions)}\033[0m')
    lb_defaulter()
def lb_defaulter():
    todo = input('>>> ')
    if todo == 'create':
        lb_create_list({})
        lb_defaulter()
    elif todo == 'test':
        lb_tester(lb_read_questions())
        lb_defaulter()
    elif todo == 'exit' or todo == 'quit' or todo == 'q':
        exit()
    else:
        print(f'\'{todo}\' is not a command.')
        lb_defaulter()
lb_defaulter()