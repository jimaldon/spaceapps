"""Read fits images."""

# Imports.
import astropy
import astropy.io.fits
import re
import os
from os.path import join, basename
import glob
import matplotlib.pyplot as plt
import cv2


def get_image(file):
   im = file[0].data
   REGEX = r'\[(\d*):(\d*),(\d*):(\d*)\]'
   w1, w2, h1, h2 = re.findall(REGEX, file[0].header['TRIMSEC'])[0]
   return im[int(h1):int(h2), int(w1):int(w2)]


def main():
    fits_folder = '_out'
    save_folder = '_debug_out'
    os.makedirs(save_folder, exist_ok=True)
    
    images = glob.glob(join(fits_folder, '*.fits'))

    for image in images:
        fits_image = astropy.io.fits.open(image)
        img16 = get_image(fits_image)
        print(img16.dtype)
        print(img16.min(), img16.max())
        img8 = cv2.convertScaleAbs(img16, alpha=(255.0/65535.0))
        img8 = (img8 - img8.min()) / (img8.max() - img8.min())
        img8 *= 255
        print(img8.min(), img8.max())
        out_path = join(save_folder, basename(image).replace('.fits', '.png'))
        img8 = cv2.resize(img8, (1024, 1024))
        cv2.imwrite(out_path, img8)
        # plt.imshow(img16)
        # plt.show()


if __name__ == '__main__':
    main()
