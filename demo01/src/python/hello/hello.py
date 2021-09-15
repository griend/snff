import time

def hello(name='World'):
    print(f'Hello, {name}!')
    time.sleep(3600)

if __name__ == '__main__':
    hello()
    hello('Cees')
