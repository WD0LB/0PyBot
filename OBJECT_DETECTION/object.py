import cv2
from matplotlib.pyplot import text
import numpy as np
import pyttsx3

showCap=False
cap=cv2.VideoCapture(0)
classes=[]
whT=320
confThr=0.5
nmsThr=0.4

with open('coco.names','r') as f:
    classes=f.read().rstrip('\n').split("\n")

net=cv2.dnn.readNet('./yolov3.cfg','./yolov3.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

img = cv2.imread("2.jpg")
img = cv2.resize(img, None, fx=0.4, fy=0.4)
height, width, channels = img.shape
height, width, channels = img.shape
def findObjects(outputs,img):
    wT,hT,_=img.shape
    bbox=[]
    classIds=[]
    confs=[]
    for out in outputs:
        for det in out:
            scores=det[5:]
            classId=np.argmax(scores)
            confindence=scores[classId]
            if confindence>confThr:
                #mean-The Object is detected
                #process
                # w,h=int(det[2]*wT),int(det[3]*hT)
                # x,y=int((det[0]*wT)-w/2),int((det[1]*hT)-h/2)
                # Object detected
                center_x = int(det[0] * width)
                center_y = int(det[1] * height)
                w = int(det[2] * width)
                h = int(det[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                bbox.append([x,y,w,h])
                confs.append(float(confindence))
                classIds.append(classId)


    indexes=cv2.dnn.NMSBoxes(bbox,confs,confThr,nmsThr)
    for i in range(len(bbox)):
        if i in indexes:
            x,y,w,h=bbox[i]
            label=str(classes[classIds[i]])
            color = colors[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
            cv2.putText(img,label,(x,y+30),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
            text_speech  = pyttsx3.init()
            # answer = input("What you want to convert")
            text_speech.say(label)
            text_speech.runAndWait()

while True:
    if showCap: _,img=cap.read()
    else: img=cv2.imread('2.jpg')
    
    blob=cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop=False)
    net.setInput(blob)
    layers=net.getLayerNames()
    outputN=[(layers[i-1]) for i in net.getUnconnectedOutLayers()]
    outputs=net.forward(outputN)
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    findObjects(outputs,img)

    cv2.imshow('py',img)
    # while cv2.getWindowProperty('py', 0) >= 0:
    #     cv2.imshow('py',img)
    #     keyCode = cv2.waitKey(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
