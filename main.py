from core import app

if __name__ == '__main__':
    for x in range(1, 4):
        app.run(f'data\\bank{x}.csv', f'bank{x}')
