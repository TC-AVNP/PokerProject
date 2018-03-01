import cv2
import numpy as np 
#boundaries on each table
table1=(200,0)
table2=(692,0)
table3=(200,362)
table4=(689,362)
#template used to compare table
tableTemplate = cv2.imread("tableTemplate.png",0)
#template used to compare buttons
buttonsTemplate = cv2.imread("templateButtontable.png",0)

#receives an image returns a dictionary with the table name and values 
def getActiveTables(image):
	#table images
	tableImages= []
	tableImages.append(image[3:358,200:676])
	tableImages.append(image[3:358,690:1166])
	tableImages.append(image[364:719,200:676])
	tableImages.append(image[364:719,690:1166])
	resultImages={}
	resultImages["table1"] = image[3:358,200:676]
	resultImages["table2"] = image[3:358,690:1166]
	resultImages["table3"] = image[364:719,200:676]
	resultImages["table4"] = image[364:719,690:1166]
	#threshold for matching
	threshold = 0.70
	alreadyDrawn = []
	# algo= cv2.Canny(image, 9000,9000)
	w,h = tableTemplate.shape[::-1]
	res = cv2.matchTemplate(image,tableTemplate,cv2.TM_CCOEFF_NORMED)
	loc = np.where(res>= threshold)

	for pt in zip(*loc[::-1]):
		flag = True
		if (len(alreadyDrawn)==0):
			alreadyDrawn.append(pt)
						
		for x in alreadyDrawn:
			if(abs(x[0] - pt[0]) <40 and abs(x[1] - pt[1])<40):
				flag = False
		if(flag):
			alreadyDrawn.append(pt)
			# cv2.rectangle(algo, pt,(pt[0]+w, pt[1]+h),(255,255,255),3)

		# cv2.imshow("testes", algo)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
	resultValues = {}
	for x in alreadyDrawn:
		if(abs(x[0] -table1[0])<40 and abs(x[1]-table1[1])<40):
			resultValues["table1"] = table1
		if(abs(x[0] -table2[0])<40 and abs(x[1]-table2[1])<40):
			resultValues["table2"] = table2
		if(abs(x[0] -table3[0])<40 and abs(x[1]-table3[1])<40):
			resultValues["table3"] = table3
		if(abs(x[0] -table4[0])<40 and abs(x[1]-table4[1])<40):
			resultValues["table4"] = table4
		
	return resultValues, resultImages

def toPlay(tableImage):
	cv2.imshow("fulliamge",tableImage)
	clip = tableImage[316:356,221:471]
	cv2.imshow("buttons",clip)

	threshold = 0.40

	w,h = buttonsTemplate.shape[::-1]
	res = cv2.matchTemplate(tableImage,buttonsTemplate,cv2.TM_CCOEFF_NORMED)
	loc = np.where(res>= threshold)
	if len(loc[0]>2):
		return True
	else:
		return False



