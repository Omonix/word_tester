import random

def tester():
    questions = {'cubrir': 'cubierto', 'abrir': 'abierto', 'morir': 'muerto', 'imprimir': 'impreso'}
    evaluator = questions.copy()
    result = ['\n']
    i = 0
    while i < len(questions):
        x = int(random.random() * len(evaluator))
        element = list(evaluator.keys())[x]
        response = input(f'{element[0].upper() + element[1:len(element)].lower()} ? ')
        if response == evaluator.get(element.lower()) and evaluator.get(element.lower()):
            print('\033[1;92mCorrect\033[0m')
            result.append(f'\033[1;92m{element} : {questions.get(element)}\033[0m')
        else:
            print('\033[1;31mIncorrect\033[0m')
            result.append(f'\033[1;31m{element} : {questions.get(element)}\033[0m')
        del evaluator[element]
        i += 1
    for i in result:
        print(i)
tester()