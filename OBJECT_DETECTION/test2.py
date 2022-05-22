import cv2
import numpy as np
import pyttsx3

confThr=0.5
nmsThr=0.4
# Load Yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
# Loading image
img = cv2.imread("2.jpg")
img = cv2.resize(img, None, fx=0.8, fy=0.8)
height, width, channels = img.shape
# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outputs = net.forward(output_layers)
# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outputs:
    for detections in out:
        scores = detections[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > confThr:
            # Object detected
            center_x = int(detections[0] * width)
            center_y = int(detections[1] * height)
            w = int(detections[2] * width)
            h = int(detections[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
indexes = cv2.dnn.NMSBoxes(boxes, confidences, confThr, nmsThr)
font = cv2.FONT_HERSHEY_SIMPLEX
labels = []
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        if label not in labels:
            labels.append(label)
            text_speech  = pyttsx3.init()
            # answer = input("What you want to convert")
            text_speech.say(label)
            text_speech.runAndWait()
        color = colors[i]
        
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
        cv2.putText(img, label, (x, y + 50), font, 2, color, 5)
cv2.imshow("Hassan's Bot", img)
cv2.waitKey(0)
cv2.destroyAllWindows()