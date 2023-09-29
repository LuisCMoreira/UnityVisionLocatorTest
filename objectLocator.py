import cv2
import numpy as np
import time

template_path = 'C:\\Users\\LuisC\\Desktop\\unity_screenshot\\screenshot_base.png'
target_path = 'C:\\Users\\LuisC\\Desktop\\unity_screenshot\\template_image.png'

# Load the object image and convert it to grayscale
object_image = cv2.imread(target_path)
object_gray = cv2.cvtColor(object_image, cv2.COLOR_BGR2GRAY)

# Create ORB detector and compute keypoints and descriptors for the object image
orb = cv2.ORB_create()
object_keypoints, object_descriptors = orb.detectAndCompute(object_gray, None)

# Create a named window for the main image
cv2.namedWindow('Main Image with Cross and Text', cv2.WINDOW_NORMAL)

while True:
    # Load the scene image and convert it to grayscale
    scene_image = cv2.imread(template_path)
    main_gray = cv2.cvtColor(scene_image, cv2.COLOR_BGR2GRAY)

    # Create ORB detector and compute keypoints and descriptors for the main image
    main_keypoints, main_descriptors = orb.detectAndCompute(main_gray, None)

    # Check if descriptors exist for both images
    if object_descriptors is not None and main_descriptors is not None:
        # Convert descriptors to correct types
        object_descriptors = object_descriptors.astype(np.uint8)
        main_descriptors = main_descriptors.astype(np.uint8)

        # Create a Brute-Force matcher and match keypoints
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = matcher.match(object_descriptors, main_descriptors)

        try:
            # Select the best match
            best_match = matches[0]

            # Get the matched keypoints
            object_matched_keypoint = object_keypoints[best_match.queryIdx]
            main_matched_keypoint = main_keypoints[best_match.trainIdx]

            # Get the pixel location of the matched keypoints
            object_pixel_location = np.int32(object_matched_keypoint.pt)
            main_pixel_location = np.int32(main_matched_keypoint.pt)
            #print(main_pixel_location)
            
            # Get the rotation angle of the matched keypoints
            object_rotation_angle = object_matched_keypoint.angle
            main_rotation_angle = int(main_matched_keypoint.angle)
            #print(main_rotation_angle)

            # Draw a cross on the main image at the object's location
            cross_size = 10
            cross_thickness = 2
            cross_color = (0, 255, 0)  # Green color

            cross_center = tuple(main_pixel_location)
            cross_start_horizontal = (main_pixel_location[0] - cross_size, main_pixel_location[1])
            cross_end_horizontal = (main_pixel_location[0] + cross_size, main_pixel_location[1])
            cross_start_vertical = (main_pixel_location[0], main_pixel_location[1] - cross_size)
            cross_end_vertical = (main_pixel_location[0], main_pixel_location[1] + cross_size)

            cv2.line(scene_image, cross_start_horizontal, cross_end_horizontal, cross_color, cross_thickness)
            cv2.line(scene_image, cross_start_vertical, cross_end_vertical, cross_color, cross_thickness)

            # Add the pixel location and rotation angle as text on the output image
            text_location = (10, 30)
            text_color = (0, 0, 255)  # Red color
            text_font = cv2.FONT_HERSHEY_SIMPLEX
            text_scale = 0.6
            text_thickness = 2

            pixel_location_text = f"Object XPixel: {main_pixel_location[0]}, Object YPixel: {main_pixel_location[1]}"
            rotation_angle_text = f"Object Rotation Angle: {main_rotation_angle}"

            cv2.putText(scene_image, pixel_location_text, text_location, text_font, text_scale, text_color,
                        text_thickness, cv2.LINE_AA)
            cv2.putText(scene_image, rotation_angle_text, (text_location[0], text_location[1] + 30), text_font,
                        text_scale, text_color, text_thickness, cv2.LINE_AA)

            # Show the main image with the cross and text
            cv2.imshow('Main Image with Cross and Text', scene_image)
            print(pixel_location_text)
            print(rotation_angle_text)

        except IndexError:
            # Display the main image with the "Target not found!!!" message
            text_location = (10, 30)
            text_color = (0, 0, 255)  # Red color
            text_font = cv2.FONT_HERSHEY_SIMPLEX
            text_scale = 0.6
            text_thickness = 2

            cv2.putText(scene_image, "Target not found!!!", text_location, text_font, text_scale, text_color,
                        text_thickness, cv2.LINE_AA)
            cv2.imshow('Main Image with Cross and Text', scene_image)

    else:
        cv2.imshow('Main Image with Cross and Text', scene_image)
        print("Descriptors not found for either object or scene image.")

    # Wait for 5 seconds and break the loop if 'q' is pressed
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

# Release the scene image and destroy the window
cv2.destroyAllWindows()
