import cv2
import numpy as np

def displayAnonymization(frame, markerList):
    left_eye = getMarkerPosition(markerList, 2)
    right_eye = getMarkerPosition(markerList, 5)
    nose = getMarkerPosition(markerList, 0)
    x1 = int(left_eye[0] * frame.shape[1])
    x2 = int(right_eye[0] * frame.shape[1])
    y1 = int(left_eye[1] * frame.shape[0])
    y2 = int(right_eye[1] * frame.shape[0])
    z = int(nose[1] * frame.shape[0])
    width = int(np.abs(x2 - x1) * 2)
    height = int(np.abs(y1 - z)) * 2
    top_left = (int(x1 + width * 0.5), int(y1 - height * 1.5))
    bottom_right = (int(x2 - width * 0.5), int(y2 + height * 1.5))

    cv2.rectangle(frame, top_left, bottom_right, (0, 0, 0), -1)

    return frame

def getMarkerPosition(markerList, markerID):
    if markerList != None:
        marker = markerList.landmark[markerID]
        return marker.x, marker.y
    else:
        return -1, -1