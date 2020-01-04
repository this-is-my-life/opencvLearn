import cv2
import numpy as np

def nothing (x):
  pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Controller")
cv2.createTrackbar("LH", "Controller", 0, 255, nothing)
cv2.createTrackbar("LS", "Controller", 0, 255, nothing)
cv2.createTrackbar("LV", "Controller", 0, 255, nothing)
cv2.createTrackbar("UH", "Controller", 255, 255, nothing)
cv2.createTrackbar("US", "Controller", 255, 255, nothing)
cv2.createTrackbar("UV", "Controller", 255, 255, nothing)

while (True):
  ret, frame = cap.read()

  if ret == True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Controller")
    l_s = cv2.getTrackbarPos("LS", "Controller")
    l_v = cv2.getTrackbarPos("LV", "Controller")

    u_h = cv2.getTrackbarPos("UH", "Controller")
    u_s = cv2.getTrackbarPos("US", "Controller")
    u_v = cv2.getTrackbarPos("UV", "Controller")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Origin', frame)
    cv2.imshow('Converted', hsv)
    cv2.imshow('Masked', mask)
    cv2.imshow('Result', res)

    key = cv2.waitKey(1)
    if key == 27:
      break

  else:
    break

cap.release()
cv2.destroyAllWindows()
