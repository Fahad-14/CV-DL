import cv2
import os

# Get gesture name
gest_name = input("Enter gesture name: ")
path = os.path.join("gestures", gest_name)
os.makedirs(path, exist_ok=True)

# Initialize camera
cam = cv2.VideoCapture(0)

img_counter = 0

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (300, 300), (100, 100), (0, 255, 0), 2)
    cv2.imshow("Gesture Capture", frame)
    img_name = os.path.join(path, "{}.png".format(img_counter))

    key = cv2.waitKey(1)
    if key == ord('c'):
        roi = frame[100:300, 100:300]
        cv2.imwrite(img_name, roi)
        img_counter += 1
    elif key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
