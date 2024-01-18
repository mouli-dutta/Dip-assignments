import numpy as np

def read_pgm_image(file_path):
    with open(file_path, 'r') as img:
        #read headers
        word = img.readline()
        comment = img.readline()
        res = img.readline()
        max_int = int(img.readline())

        x, y = map(int, res.split(' '))

        # read pixel values
        img_data = []

        for _ in range(x*y):
            img_data.append(int(img.readline()))
        
        # convert img to array and return
        return np.array(img_data).reshape(y, x)

def main():
    print(read_pgm_image('images/1.pgm'))

main()