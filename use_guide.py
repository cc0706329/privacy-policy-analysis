import numpy as np
import use_model

def main():
    x = np.zeros((4,415,300))
    y = use_model.predict(x)
    print(y)

if __name__ == '__main__':
    main()
