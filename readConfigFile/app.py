import os, shutil

print(f"Name of python executable file {__file__}")

def readconfigfile(filename=None):
    try:
        from configparser import ConfigParser
        absolute_path = os.path.abspath(__file__)
        print("Full path: " + absolute_path)
        print("Directory Path: " + os.path.dirname(absolute_path))
        dirINI = os.path.dirname(absolute_path)
        fileINI = filename
        if not os.path.isfile(os.path.join(dirINI, fileINI)):
            print('File Not found')
            raise Exception   
        else:
            print('Config File Available')
            parser = ConfigParser()
            parser.read(os.path.join(dirINI, fileINI))            
            print ("Sections : ", parser.sections())
            for sect in parser.sections():
                print('Section:', sect)
                for k,v in parser.items(sect):
                    print(' {} = {}'.format(k,v))

    except ImportError:
        print("Module Not found!")
    except Exception as e:
        print("Somethis is wrong with file")
        raise(e)


readconfigfile(filename='config.ini')


