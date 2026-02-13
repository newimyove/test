def read_conf():
    file=open('file','r+',encoding='utf8')
    text=file.read()
    print(text)
    print(eval(text))
    print(type(eval(text)))
    file.close()

if __name__ == '__main__':
    read_conf()
