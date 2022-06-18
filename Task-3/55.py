'''5.Array re-dimensioning'''
import numpy as np
def main():
    print('Initialised array')
    a = np.array([1, 2, 3, 4])
    print(a)
    print('current shape of the array')
    print(a.shape)
    print('changing shape to 2,3')
    a.shape = (2, 2)
    print(a)
if __name__ == "__main__":
    main()