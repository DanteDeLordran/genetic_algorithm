import numpy as np
from tkinter import filedialog

from numpy import ndarray



def csv_to_matrix() -> ndarray:
    return np.loadtxt(filedialog.askopenfilename(), delimiter=',')


def genetic_algorithm(matrix: ndarray) -> None:

    left_side = matrix[:,:matrix.shape[1]//2]
    right_side = matrix[:,matrix.shape[1]//2:]
    q1 = []
    q2 = []
    total = []

    for i in range(left_side.shape[0]):
        left = 0
        right = 0
        for j in range(left_side.shape[1]):
            if left_side[i,j] == 1:
                left += 1
                if j + 1 < left_side.shape[1] and left_side[i, j + 1] is not None:
                    if left_side[i,j] == left_side[i, j + 1]:
                        left += 1
            else:
                left -= 1
                if j + 1 < left_side.shape[1] and left_side[i, j + 1] is not None:
                    if left_side[i,j] == left_side[i, j + 1]:
                        left -= 1

            if right_side[i,j] == 1:
                right += 1
                if j + 1 < right_side.shape[1] and right_side[i, j + 1] is not None:
                    if right_side[i,j] == right_side[i, j + 1]:
                        right += 1
            else:
                right -= 1
                if j + 1 < right_side.shape[1] and right_side[i, j + 1] is not None:
                    if right_side[i,j] == right_side[i, j + 1]:
                        right -= 1

        if np.sum(left_side[i, :] == 1) > np.sum(left_side[i, :] == 0):
                left += 1
        elif np.sum(left_side[i, :] == 1) < np.sum(left_side[i, :] == 0):
            left -= 1

        if np.sum(right_side[i, :] == 1) > np.sum(right_side[i, :] == 0):
            right += 1
        elif np.sum(right_side[i, :] == 1) < np.sum(right_side[i, :] == 0):
            right -= 1

        q1.append(left)
        q2.append(right)

    for i in range(len(q1)):
        total.append(q1[i] + q2[i])

    print(q1)
    print(q2)
    print(total)
    print(np.sum(total))


def main():
    matrix = csv_to_matrix()
    genetic_algorithm(matrix)


if __name__ == '__main__':
    main()