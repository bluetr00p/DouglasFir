#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import sys
argv = sys.argv
import os
cwd = os.getcwd()
import json

def initer():
    name = input("Project name(your-project): ") or "your-project"
    version = input("Project version(1.0.0): ") or "1.0.0"
    desc = input("Description of project:") or ""
    lang = input("Programming Language(python3): ") or "python3"
    entryPoint = input("Entry Point(main.py): ") or "main.py"
    startScript = input("Do you need any special launcher(None): eg(flask) ") or ""
    gitRepo = input("Git reposity:") or ""
    author = input("Author: ")
    licences = input("Licencen (MIT): ") or "MIT"
    jsonData = {
        'name': name,
        'version': version,
        'description': desc,
        'language': lang,
        'main': entryPoint,
        "startup": {"run":startScript},
        'repo': {
            'repository': gitRepo,
            'type': 'git'
        },
        'author': author,
        'license': licences,
        'dependencies': {}
    }
    with open('barkfile', 'w') as barkfile:
        json.dump(jsonData, barkfile)


def add(packageName):
    with open('barkfile', 'r') as file:
        barkFile = json.load(file)
    package = packageName.split("@")
    try: 
        barkFile['dependencies'][package[0]] = package[1]
    except IndexError:
        barkFile['dependencies'][package[0]] = ""
    with open('barkfile', 'w') as barkfile:
        json.dump(barkFile, barkfile)

def remove(packageName):
    with open('barkfile', 'r') as file:
        barkFile = json.load(file)
    del barkFile['dependencies'][packageName]
    with open('barkfile', 'w') as barkfile:
        json.dump(barkFile, barkfile)

def install():
    import subprocess
    with open('barkfile', 'r') as file:
        barkFile = json.load(file)
    if barkFile['language'].startswith("python"):
        for i, name in enumerate(barkFile['dependencies']):
            version = barkFile['dependencies'][name]
            comboPackage = name+"=="+version
            subprocess.call([sys.executable, "-m", "pip", "install", comboPackage])

if len(argv) >= 3:
    package = argv[2]
    if len(argv) <= 3:
        if argv[1] == 'add':
            print('adding {}'.format(package))
            add(package)
        elif argv[1] == 'upgrade':
            print('upgrading {}'.format(package))
        elif argv[1] == 'remove':
            print('Removing {}'.format(package))
            remove(package)
    else:
        if argv[3] == "--dev":
            print('adding developer dependency {}'.format(package))
        if argv[3] == "--optional":
            print("adding optional dependency {}".format(package))
elif len(argv) == 2:
    if argv[1] == "init":
        initer()
    elif argv[1] == "install":
        print('installing')
        install()
elif len(argv) == 1:
    print('installing')
    install()



