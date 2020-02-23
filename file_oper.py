
try:
    with open('add_num.py', mode='r') as open_file:
        print('File can be seen')

except FileNotFoundError as err:
    print('File not available')
    raise err
