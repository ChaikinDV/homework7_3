general_text = {}
def read_text(name):
    with open(name, 'r', encoding='utf=8') as f:
        text = []
        for line in f:
            text.append(line)
        general_text.setdefault(name, text)
    return general_text
read_text('1.txt')
read_text('2.txt')
read_text('3.txt')

def write_file():
    with open('4.txt', 'w', encoding='utf=8') as f:
        for k, v in sorted(general_text.items(), key=lambda x: len(x[1])):
            f.write(f'{k}\n')
            f.write(f'{(str(len(v)))}\n')
            f.write(''.join(v))
            f.write('\n')
write_file()