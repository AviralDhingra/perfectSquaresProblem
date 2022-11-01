import numpy as np


def itr(MAX):
    l = []
    x = int(MAX**(1/2))
    for i in range(1, x+1):
        l.append(i)
    perfect_squares = []
    for num in l:
        num = (num**2)
        perfect_squares.append(num)

    ending_digits = np.array(perfect_squares) % 10
    ending_digits[ending_digits == 0] = 10
    return perfect_squares, ending_digits


if __name__ == '__main__':
    # Plotted Graphs : 500, 1500
    MAX = int(input('Max : '))
    perfect_squares, ending_digits = itr(MAX)
    print(f'Perfect Squares : {perfect_squares}')
    for i in range(1, 10+1):
        frequency = np.count_nonzero(ending_digits == i)
        print(str(i), '=>', str(frequency))
