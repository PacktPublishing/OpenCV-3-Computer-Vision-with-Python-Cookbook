#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='../data/Lena.png', help='Image path.')
parser.add_argument('--out_png', default='../data/Lena_compressed.png',
                    help='Output image path for lossless result.')
parser.add_argument('--out_jpg', default='../data/Lena_compressed.jpg',
                    help='Output image path for lossy result.')
params = parser.parse_args()
img = cv2.imread(params.path)

# save image with lower compression - bigger file size but faster decoding
cv2.imwrite(params.out_png, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

# check that image saved and loaded again image is the same as original one
saved_img = cv2.imread(params.out_png)
assert saved_img.all() == img.all()

# save image with lower quality - smaller file size
cv2.imwrite(params.out_jpg, img, [cv2.IMWRITE_JPEG_QUALITY, 0])
