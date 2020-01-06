import cv2

face = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('data/haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)

while True:
  _, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face.detectMultiScale(gray, 1.1, 4)

  for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_img = img[y:y+h, x:x+w]
    eyes = eye.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
      cv2.rectangle(roi_img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

  cv2.imshow("Renderd", img)
  if cv2.waitKey(1) & 0xff == ord('q'):
    break

cap.release()
