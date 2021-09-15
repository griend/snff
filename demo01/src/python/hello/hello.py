import time

def hello(name='World'):
    print(f'Hello, {name}!')
    time.sleep(120)


if __name__ == '__main__':
    hello()
    hello('Cees')
