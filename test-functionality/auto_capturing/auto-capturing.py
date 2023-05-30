import cv2
import time

# Initialize variables
img_counter = 0
capture_images = False

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Frame", frame)

    # Wait for the spacebar key press
    key = cv2.waitKey(1) & 0xFF

    # Start image capture if spacebar is pressed and capture_images is False
    if key == ord(' ') and not capture_images:
        capture_images = True
        print("Image capture started.")

    # If image capture is enabled, save the frame
    if capture_images:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Screenshot taken:", img_name)
        img_counter += 1

        # Wait for 0.5 seconds
        time.sleep(0.5)

    # Break the loop if 10 images have been captured
    if img_counter == 10:
        print("Image capture completed.")
        break

# Release the VideoCapture object and close windows
cap.release()
cv2.destroyAllWindows()