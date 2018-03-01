import cv2
import numpy as np 
import matplotlib.pyplot as  plt
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

plt.imshow(image)
plt.show()