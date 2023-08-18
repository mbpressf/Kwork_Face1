import cv2
import dlib
import numpy as np

# Load the image
img = cv2.imread('face.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Detect faces in the image
faces = detector(gray)

# Crop the image to get only the face
for face in faces:
    landmarks = predictor(gray, face)
    points = np.zeros((68, 2), dtype=int)
    for i in range(68):
        points[i] = (landmarks.part(i).x, landmarks.part(i).y)
    hull = cv2.convexHull(points)
    mask = np.zeros_like(gray)
    cv2.fillConvexPoly(mask, hull, 255)
    face_img = cv2.bitwise_and(img, img, mask=mask)
    x, y, w, h = cv2.boundingRect(hull)
    head_img = face_img[y:y+h, x:x+w]
    cv2.imshow('Head', head_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()