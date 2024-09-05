import cv2
import winsound
import time

webcam = cv2.VideoCapture(0)

while True:
    # Read two consecutive frames with a small delay
    ret1, im1 = webcam.read()
    time.sleep(0.1)  # Insert a small delay to capture difference
    ret2, im2 = webcam.read()
    
    # Ensure both frames are successfully captured
    if not ret1 or not ret2:
        break

    # Calculate the absolute difference between the two frames
    diff = cv2.absdiff(im1, im2)
    
    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Threshold the grayscale image to get the motion areas
    _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        
        # Sound alert for large contour areas (motion detected)
        winsound.Beep(800, 100)
    
    # Display the grayscale image
    cv2.imshow("security camera", gray)
    
    # Break the loop if the 'Esc' key is pressed
    if cv2.waitKey(10) == 27:
        break

# Release the webcam and close the window
webcam.release()
cv2.destroyAllWindows()


 

    
    
    