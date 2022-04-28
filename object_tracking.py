import cv2 #For image processing
import numpy as np #To store image
from object_detection import ObjectDetection

# Initialize Object Detection
od = ObjectDetection()

cap = cv2.VideoCapture("los_angeles.mp4")


while True:
    _, frame = cap.read()

    # Detect objects on frame
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
            print(box)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.realease()
cv2.destroyAllWindows()

