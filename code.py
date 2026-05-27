import cv2
import numpy as np
import time

# Start webcam
cap = cv2.VideoCapture(0)

# Give camera time to warm up
time.sleep(2)

# Capture background
background = 0

for i in range(60):
    ret, background = cap.read()

# Flip background for natural view
background = np.flip(background, axis=1)

print("Background captured successfully!")

while cap.isOpened():

    # Read frame
    ret, frame = cap.read()

    if not ret:
        break

    # Flip frame horizontally
    frame = np.flip(frame, axis=1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Pink color range in HSV
    lower_pink = np.array([140, 50, 50])
    upper_pink = np.array([170, 255, 255])

    # Create mask for pink color
    mask1 = cv2.inRange(hsv, lower_pink, upper_pink)

    # Remove noise
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    # Inverse mask
    mask2 = cv2.bitwise_not(mask1)

    # Segment out the pink colored part
    res1 = cv2.bitwise_and(background, background, mask=mask1)

    # Segment the remaining part
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)

    # Final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Display output
    cv2.imshow("Invisible Cloak Project", final_output)

    # Press ESC to exit
    key = cv2.waitKey(1)

    if key == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()