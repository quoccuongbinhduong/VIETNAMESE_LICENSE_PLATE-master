import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
     # Thu lan luot tung khung hinh (frame-by-frame)
     ret, frame = cap.read()
     # Thao tac tren frame (chuyen thanh anh xam)
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     # Hien thi frame
     cv2.imshow('frame', gray)
     if cv2.waitKey(1) & 0xFF == ord('q'):
          break
# Giai phong video khi thuc hien xong thao tac
cap.release()
cv2.destroyAllWindows()