history = []


def add(a, b):
    try:
        answer = float(a) + float(b)
        output = str(a) + ' + ' + str(b) + ' = ' + str(answer)
        print(output)
        history.append(output)
    except TypeError:
        print('ERROR')


def sub(a, b):
    try:
        answer = float(a) - float(b)
        output = str(a) + ' + ' + str(b) + ' = ' + str(answer)
        print(output)
        history.append(output)
    except TypeError:
        print('ERROR')


def mul(a, b):
    try:
        answer = float(a) * float(b)
        output = str(a) + ' * ' + str(b) + ' = ' + str(answer)
        print(output)
        history.append(output)
    except TypeError:
        print('ERROR')


def div(a, b):
    try:
        answer = float(a) / float(b)
        output = str(a) + ' / ' + str(b) + ' = ' + str(answer)
        print(output)
        history.append(output)
    except TypeError:
        print('ERROR')
    except ZeroDivisionError:
        print(str(a) + '/' + str(b) + '=' + 'UNDEFINED')


def calc_history():
    for answers in range(len(history)):
        print(history[answers])


def clear_history():
    history = []
    print(history)


if __name__ == '__main__':
    add(3, 5)
    mul(4, 6)
    div(10, 2)
    sub(100, 70)
    calc_history()
