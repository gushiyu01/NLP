def open_file():
    with open('C://Users//gushiyu//Desktop//python.txt', 'r', encoding='UTF-8') as f:
        data = f.read()
        print(data)


if __name__ == '__main__':
    open_file()
