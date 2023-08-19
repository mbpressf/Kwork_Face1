import cv2
import mediapipe as mp

# Load the image
img = cv2.imread('face.png')

# Initialize the face detection model
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

# Detect faces in the image
results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Crop the faces and save them
for detection in results.detections:
    bbox = detection.location_data.relative_bounding_box
    x1 = int(bbox.xmin * img.shape[1])
    y1 = int(bbox.ymin * img.shape[0])
    x2 = int((bbox.xmin + bbox.width) * img.shape[1])
    y2 = int((bbox.ymin + bbox.height) * img.shape[0])
    face = img[y1:y2, x1:x2]
    cv2.imwrite('face.jpg', face)
