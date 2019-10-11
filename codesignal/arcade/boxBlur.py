"""
Last night you partied a little too hard. Now there's a black and
white photo of you that's about to go viral! You can't let this ruin
your reputation, so you want to apply the box blur algorithm to the
photo to hide its content.

The pixels in the input image are represented as integers. The algorithm
distorts the input image in the following way: Every pixel x in the output
image has a value equal to the average value of the pixel values from the
3 x 3 square that has its center at x, including x itself. All the pixels
on the border od x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3x3 square:
(1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.666 = 1
The border pixels are cropped from the final result.
"""

import numpy as np
import math

def boxBlur(image):

    np_image = np.array(image)
    lx = len(image[0]) - 2
    ly = len(image) - 2

    new_img = np.zeros((ly,lx))

    x = 0
    y = 3
    for i in range(ly):
        for j in range(lx):
            t = np_image[x + i: y + i, x + j: y + j]
            t.tolist()
            flat_list = [k for sublist in t for k in sublist]
            s = math.floor(sum(flat_list)/9)
            new_img[i][j] = int(s)

    return(new_img.tolist())


image = [[1,1,1],
         [1,7,1],
         [1,1,1]]

print(boxBlur(image))  # [[1]]
