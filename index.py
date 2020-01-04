import cv2
import numpy as np

def nothing (x):
  pass

cap = cv2.VideoCapture('sample.mp4')

ret, f1 = cap.read()
ret, f2 = cap.read()

while cap.isOpened():
  diff = cv2.absdiff(f1, f2)
  gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5, 5), 0)
  _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
  dilated = cv2.dilate(thresh, None, iterations=3)
  contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  
  for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if cv2.contourArea(contour) < 200:
      continue
    cv2.rectangle(f1, (x, y), (x+w, y+h), (0, 255, 0), 2)

  cv2.imshow('OpenCV Learn', f1)

  f1 = f2
  ret, f2 = cap.read()

  key = cv2.waitKey(40)
  if key == 27:
    break

cap.release()
cv2.destroyAllWindows()
