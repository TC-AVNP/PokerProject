from Table import getActiveTables, toPlay
from Commands import clika
from grabScreen import grab_screen
import pyscreenshot as ImageGrab
import argparse
import cv2
import time
import numpy as np 
value= 143

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--value", required=True,
#     help="starting value")


# args = vars(ap.parse_args())

# value = args["value"]





# print (listValues)
# print( iamgeList)
# for x in listValues:
# 	# cv2.imshow("x",iamgeList[x])
# 	flag = toPlay(iamgeList[x])
# 	print(str(x)+" tem a flag do jogo a : "+str(flag))
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()



# oi()

def printTaker():
	global value
	while True:
		#ciclos de 10 em 10 segundos
		for i in range(0,5):
			print(i+1)
			time.sleep(1)
		print("Passaram 10 segundos!")
		 # grab fullscreen
		grab_screen()
		image = cv2.imread("print.png",0)
		listValues, imageList = getActiveTables(image)#print
		print (listValues)
		for x in listValues:
			# cv2.imshow("x",imageList[x])
			flag = toPlay(imageList[x])
			print(str(x)+" tem a flag do jogo a : "+str(flag))
			if(flag):
				value += 1
				nameContinuation = "cards/cardSet"+str(value)+".png"
				cv2.imwrite(nameContinuation, imageList[x])
				print("tirado print com o valor " + nameContinuation)
				clika(x)
printTaker()