def basic():
    chooseLogOrSing = int(input('''
    1) Sing in
    2) Log in\n'''))
    
    if chooseLogOrSing == 1:
        singIn()
    elif chooseLogOrSing == 2:
        logIn()
    else:
        error()
        
        
def error():
    print('Error!!!')
    basic()
    
def singIn():
    dataList = []
    fullName = input('surname and lastname: ')
    login = input('login: ')
    password = input('password: ')

    dataList.append(fullName)
    dataList.append(password)
    data[login] = dataList
    basic()

def logIn():
    login = input('login: ')
    password = input('password')
    
    if login in data.keys():
        infoWithoutLogin = data[login]
        if infoWithoutLogin[1] == password:
            print('Welcome!!! ' + infoWithoutLogin[0])
            basic()
        else:
            print('Error!!!')
            basic() 
    
data = {}