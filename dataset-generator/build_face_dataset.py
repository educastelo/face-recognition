# import the necessary packages
from imutils.video import VideoStream
import imutils
import time
import cv2
import os

# load OpenCV's Haar cascade for face detection from disk
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus far
print("[INFO] starting video stream...")

# using webcam
vs = VideoStream(src=0).start()
time.sleep(2.0)

total = 0
frame_count = 0

# output directory
output_dir = f"dataset/{input('Digite o nome do usuário a ser cadastrado: ')}"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# loop over the frames from the video stream
while total < 50:
    # grab the frame from the threaded video stream, clone it, (just
    # in case we want to write it to disk), and then resize the frame,
    # so we can apply face detection faster
    frame = vs.read()
    orig = frame.copy()
    frame = imutils.resize(frame, width=1000)

    # detect faces in the grayscale frame
    rects = detector.detectMultiScale(
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(rects) > 0:
        # loop over the face detections and draw them on the frame
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if frame_count % 5 == 0:
            # save the face image each 5 frames
            p = os.path.sep.join([output_dir, "{}.png".format(str(total).zfill(5))])
            cv2.imwrite(p, orig)
            total += 1

    # Increment the frame counter and reset it when it reaches 5
    frame_count += 1
    if frame_count == 5:
        frame_count = 0

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# print the total faces saved and do a bit of cleanup
print("[INFO] {} face images stored".format(total))
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
