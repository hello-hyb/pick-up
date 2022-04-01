words = []
num = []
one = ['if', 'int', 'for', 'while', 'do', 'return', 'break', 'continue']
four = ['+', '-', '*', '/', '=', '>', '<', '>=', '<=', '!=']
five = [',', ';', '{', '}', '(', ')']
i = 0
with open('code.txt', 'r') as f:
    data = f.read()
    while i < len(data):
        if data[i].isalpha():
            words.append(data[i])
            if not data[i+1].isalpha():
                value = ''.join(words)
                if value in one:
                    print('(1, "%s")' % value)
                else:
                    print('(2, "%s")' % value)
                words = []
            i += 1
        elif data[i].isdigit() or data[i] == '.':
            num.append(data[i])
            if not data[i+1].isdigit() and data[i+1] != '.':
                print('(3, "%s")' % ''.join(num))
                num = []
            i += 1
        else:
            value = data[i]
            if data[i] == '>' and data[i+1] == '=' or data[i] == '<' and data[i+1] == '=' or data[i] == '!' and data[i+1] == '=':
                value = data[i] + data[i+1]
                i += 1
            if value in four:
                print('(4, "%s")' % value)
            elif value in five:
                print('(5, "%s")' % value)
            i += 1


