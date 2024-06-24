import cv2
import os

# Get gesture name to display
gest_name = input("Enter gesture name to display: ")
path = os.path.join("gestures", gest_name)

images = os.listdir(path)
for img_name in images:
    img = cv2.imread(os.path.join(path, img_name))
    cv2.imshow("Gesture", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
