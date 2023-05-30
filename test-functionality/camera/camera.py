import cv2


def capture_video():
    """
    Captures video from the camera and displays it in a window.
    Press 'Esc' key to exit the program.
    Press 'Space' key to take a screenshot.
    """
    # Create a VideoCapture object
    cam = cv2.VideoCapture(0)

    # Check if camera is opened successfully
    if not cam.isOpened():
        raise ValueError("Failed to open the camera.")

    # Create a window to display the video
    cv2.namedWindow("Camera Feed")

    img_counter = 0

    while True:
        # Read a frame from the camera
        ret, frame = cam.read()

        if not ret:
            print("Failed to capture frame.")
            break

        # Display the frame in the window
        cv2.imshow("Camera Feed", frame)

        # Wait for a key press
        key = cv2.waitKey(1)

        # Check for 'Esc' key press (27 is the ASCII code for 'Esc')
        if key == 27:
            print("Escape key pressed. Exiting...")
            break

        # Check for 'Space' key press (32 is the ASCII code for 'Space')
        elif key == 32:
            img_name = f"opencv_frame_{img_counter}.png"
            cv2.imwrite(img_name, frame)
            print("Screenshot taken:", img_name)
            img_counter += 1

    # Release the camera and close the window
    cam.release()
    cv2.destroyAllWindows()


# Run the program
if __name__ == "__main__":
    capture_video()
