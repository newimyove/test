import copy
def use_assignment():
    a=[1,2]
    b=a
    print(id(a))
    print(id(b))

def use_copy():
    c=[[1,2],[3,4]]
    d=copy.copy(c)
    print('the ids of the copied element:')
    print(id(d))
    print(id(c))
    print(id(c[0][1]))
    print(id(d[0][1]))

def use_deepcopy():
    a=[[1,2],[3,4]]
    b=copy.deepcopy(a)
    print('the ids of the deepcopied element:')
    print(id(a[0][1]))
    print((id(b[0][1])))
if __name__ == '__main__':
    use_assignment()
    use_copy()
    use_deepcopy()