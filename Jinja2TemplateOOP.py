import glob
import os
import shutil
import string
import random
from random import choice

from jinja2 import Environment, FileSystemLoader


def deleteFiles():
    # moves files created by the entities to the filesDeleted folder *DOES NOT DELETE THE FILES THEMSELVES*

    currentpath = os.path.abspath(os.getcwd())
    fileDeletedPath = os.path.abspath('filesDeleted')
    for file in glob.glob('*.py'):
        if file == 'main.py':
            try:
                shutil.move(file, fileDeletedPath)
            except Exception:
                rand = ''.join(
                    random.choice(string.digits) for _ in range(2))  # if there is already a file with the same name,
                os.rename(file, file[:-3] + rand + '.py')  # appends some random digits to the name and then move
                shutil.move(file[:-3] + rand + '.py', fileDeletedPath)

    os.chdir(path=os.path.abspath('Domain'))
    for file in glob.glob('*.py'):
        if file != '__init__.py' and file != 'entitate.py':
            try:
                shutil.move(file, fileDeletedPath)
            except Exception:
                rand = ''.join(random.choice(string.digits) for _ in range(2))
                os.rename(file, file[:-3] + rand + '.py')
                shutil.move(file[:-3] + rand + '.py', fileDeletedPath)

    os.chdir('..')

    os.chdir(path=os.path.abspath('Service'))
    for file in glob.glob('*.py'):
        if file != '__init__.py':
            try:
                shutil.move(file, fileDeletedPath)
            except Exception:
                rand = ''.join(random.choice(string.digits) for _ in range(2))
                os.rename(file, file[:-3] + rand + '.py')
                shutil.move(file[:-3] + rand + '.py', fileDeletedPath)

    os.chdir('..')

    os.chdir(path=os.path.abspath('Tests'))
    for file in glob.glob('*.py'):
        if file != '__init__.py' and file != 'utils.py':
            try:
                shutil.move(file, fileDeletedPath)
            except Exception:
                rand = ''.join(random.choice(string.digits) for _ in range(2))
                os.rename(file, file[:-3] + rand + '.py')
                shutil.move(file[:-3] + rand + '.py', fileDeletedPath)

    os.chdir('..')

    os.chdir(path=os.path.abspath('UserInterface'))
    for file in glob.glob('*.py'):
        if file != '__init__.py':
            try:
                shutil.move(file, fileDeletedPath)
            except Exception:
                rand = ''.join(random.choice(string.digits) for _ in range(2))
                os.rename(file, file[:-3] + rand + '.py')
                shutil.move(file[:-3] + rand + '.py', fileDeletedPath)

    os.chdir('..')

    os.chdir(path=os.path.abspath('templates'))
    for file in glob.glob('*.txt'):
        if file == 'consoleFor2.txt' or file == 'mainFor2.txt':
            try:
                shutil.move(file, fileDeletedPath)
            except Exception:
                rand = ''.join(random.choice(string.digits) for _ in range(2))
                os.rename(file, file[:-4] + rand + '.txt')
                shutil.move(file[:-4] + rand + '.txt', fileDeletedPath)

    os.chdir('..')


def writeToFileInFolder(output, fileName, packageName):
    # creates file with name fileName in which output is written and is moved to ./packageName

    with open(fileName, 'w') as f:
        f.write(output)
    srcPath = os.path.abspath(fileName)
    dstPath = os.path.abspath(packageName)
    src = srcPath
    dst = dstPath
    shutil.move(src, dst)


def deleteFilesFromDeletedFolder():
    # deletes files moves to the deleted folder
    path = os.path.abspath('filesDeleted')
    print(path)
    os.chdir(path=path)
    for file in glob.glob('*'):
        os.remove(path + '\\' + file)


def createTest(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr):
    # creates an entity test for adding an entity

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('test_service.txt')
    output = template.render(enter='\n', space=' ', Oras=numeEntitateMare, oras=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen)
    writeToFileInFolder(output, f'test_{numeEntitateMic}_service.py', 'Tests')


def createTestRunAll(numeEntitateMic, numeEntitateMare, numeEntitate1, numeEntitate1low):
    # create run_all file that runs all files

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('test_runall.txt')
    output = template.render(enter='\n', space=' ', Oras=numeEntitateMare, oras=numeEntitateMic, copil=numeEntitate1low,
                             Copil=numeEntitate1)
    writeToFileInFolder(output, f'run_all.py', 'Tests')


def createValidator(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr):
    # creates validators

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('validator.txt')
    output = template.render(enter='\n', space=' ', Oras=numeEntitateMare, oras=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen)
    writeToFileInFolder(output, f'{numeEntitateMic}_validator.py', 'Domain')


def createService1(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr):
    # # create the service.py file for the first entity

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('service1.txt')
    output = template.render(enter='\n', space=' ', Oras=numeEntitateMare, oras=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen)
    writeToFileInFolder(output, f'{numeEntitateMic}_service.py', 'Service')


def createService2(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr, numeEntitate1,
                   genitiv1):
    # create the service.py file for the second entity

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('service2.txt')
    output = template.render(enter='\n', space=' ', Copil=numeEntitateMare, copil=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen, oras=numeEntitate1,
                             orasGenitiv=genitiv1)
    writeToFileInFolder(output, f'{numeEntitateMic}_service.py', 'Service')


def createEntitate(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr):
    # create the domain .py file for an entity

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('domain.txt')
    output = template.render(enter='\n', space=' ', Oras=numeEntitateMare, oras=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen)
    writeToFileInFolder(output, f'{numeEntitateMic}.py', 'Domain')


def createConsole1(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr):
    # create the jinja2 template for the final console.py file

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('console.txt')
    output = template.render(enter='\n', space=' ', Oras=numeEntitateMare, oras=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen)
    writeToFileInFolder(output, f'consoleFor2.txt', 'templates')


def createConsole2(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr):
    # create the final console.py file

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('consoleFor2.txt')
    output = template.render(enter='\n', space=' ', Copil=numeEntitateMare, copil=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen)
    writeToFileInFolder(output, f'console.py', 'UserInterface')


def createMain1(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr):
    # create the jinja2 template file for the final main.py file

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('main.txt')
    output = template.render(enter='\n', space=' ', Oras=numeEntitateMare, oras=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen)
    writeToFileInFolder(output, f'mainFor2.txt', 'templates')


def createMain2(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr):
    # create the final main.py file
    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    template = env.get_template('mainFor2.txt')
    output = template.render(enter='\n', space=' ', Copil=numeEntitateMare, copil=numeEntitateMic, paramStr=paramStr,
                             paramName=paramName, plural=plural, genitiv=genitiv, gen=gen)
    # writeToFileInFolder(output, f'main.py', 'TEMPLATE')
    with open('main.py', 'w') as f:
        f.write(output)


def readEntitate1():
    '''
    Citeste datele pentru prima entitate. Tipuri de date posibile:

    str0 - string nenul, int+ - int positiv, bool, fixed (de exemplu: dePost={'da', 'nu'})

    :return:
    '''
    print(
        'Urmeaza sa introduceti datele pentru entitati. Prima caracteristica a fiecareia este id sau ceva ce o identifica.\n')
    print('Datele pentru prima entitate:\n')
    numeEntitateMic = input('Numele entitatii (cu litera mica): ')
    numeEntitateMare = numeEntitateMic.capitalize()
    plural = input('Pluralul entitatii (oras - orase): ')
    genitiv = input('Genitivul entitatii (oras - orasului): ')
    gen = input('Genul substantivului (f / m): ')
    caract = int(input('Numarul de caracteristici al entitatii: '))
    paramName = []  # retine tuple de tip (nume, tip/tipuri)
    for i in range(caract):
        nume = input(f'Caracteristica {i + 1} (id/nume/varsta): ')
        tip = input(
            'Tip (str0(nenul)/int+/bool/fixed(in program: da / nu): ): ')  # TODO eventual str simplu si int simplu ca tip de date de intrare
        if tip == 'fixed':
            fixedNum = int(input(f'Numarul de valori pe care il poate lua {nume}: '))
            fixedList = []
            for i in range(fixedNum):
                fixedList.append(input(f'Valoarea {i + 1}: '))
            paramName.append((nume, fixedList))
        else:
            paramName.append((nume, tip))
    paramStr = paramName[0][0] + numeEntitateMare  # pentru numele variabilelor
    for par in paramName[1:]:
        paramStr = paramStr + ', ' + par[0] + numeEntitateMare

    createEntitate(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createService1(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createValidator(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createTest(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName,
               paramStr)  # TODO domain and repo tests
    createConsole1(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createMain1(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)

    readEntitate2(numeEntitateMic, genitiv)  # se citeste a doua entitate


def readEntitate2(numeEntitate1, genitiv1, ):
    print('\nDatele pentru a doua entitate:\n')
    numeEntitateMic = input('Numele entitatii (cu litera mica): ')
    numeEntitateMare = numeEntitateMic.capitalize()
    plural = input('Pluralul entitatii (oras - orase): ')
    genitiv = input('Genitivul entitatii (oras - orasului): ')
    gen = input('Genul substantivului (f / m): ')
    caract = int(input('Numarul de caracteristici al entitatii: '))
    paramName = []
    for i in range(caract):
        nume = input(f'Caracteristica {i + 1} (id/nume/varsta): ')
        tip = input(
            'Tip (str0(nenul)/int+/bool/fixed(in program: da / nu): ): ')  # TODO eventual str simplu si int simplu ca tip de date de intrare
        if tip == 'fixed':
            fixedNum = int(input(f'Numarul de valori pe care il poate lua {nume}: '))
            fixedList = []
            for i in range(fixedNum):
                fixedList.append(input(f'Valoarea {i + 1}: '))
            paramName.append((nume, fixedList))
        else:
            paramName.append((nume, tip))
    paramStr = paramName[0][0] + numeEntitateMare
    for par in paramName[1:]:
        paramStr = paramStr + ', ' + par[0] + numeEntitateMare

    createEntitate(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createService2(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr, numeEntitate1,
                   genitiv1)
    createValidator(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createTest(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createMain2(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createConsole2(numeEntitateMic, numeEntitateMare, plural, genitiv, gen, paramName, paramStr)
    createTestRunAll(numeEntitateMic, numeEntitateMare, numeEntitate1.capitalize(), numeEntitate1)


def menu():
    print('Creati fisierele necesare pentru doua entitati pentru a incepe un proiect OOP in Python. \n')
    print('1. Creati fisierele pentru doua entitati')
    print('2. Muta fisierele vechi create in folderul de filesDeleted')
    print('3. Sterge toate fisierele din folderul filesDeleted')
    try:
        opt = int(input('Optiune: '))
        if opt == 1:
            readEntitate1()
        elif opt == 2:
            deleteFiles()
        elif opt == 3:
            deleteFilesFromDeletedFolder()
        else:
            pass
    except:
        pass




def mainn():
    menu()


mainn()
