import cv2
import time

# import tensorflow

# IntWEBCAM
video = cv2.VideoCapture(0)
# ExtWEBCAM
# video = cv2.VideoCapture(1)

frameCount = 0

firstFrame = None

while True:
    frameCount += 1
    isSuccess, rawFrame = video.read()

    grayFrame = cv2.cvtColor(rawFrame, cv2.COLOR_BGR2GRAY)
    blurredFrame = cv2.GaussianBlur(grayFrame, (21, 21), 0)

    if firstFrame is None:
        firstFrame = blurredFrame
        continue

    deltaFrame = cv2.absdiff(firstFrame, blurredFrame)
    # MOTION will create luminance
    # DELTA FRAME will show BRIGHT FRINGE

    retVal, thresholdFrame = cv2.threshold(deltaFrame, 30, 255, cv2.THRESH_BINARY)
    # retVal is used for determining two spiked threshold

    dilutedFrame = cv2.dilate(thresholdFrame, None, iterations=2)

    # 21:53
    # CONTOURS

    # (contours, _) = cv2.findContours(dilutedFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ( cnts,_) = cv2.findContours(dilutedFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        # SKIP a CONTOUR with area less than 1000
        # For more precision,REDUCE the AREA
        if cv2.contourArea(contour) < 10:
            continue
        # ELSE Draw Boxes
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(rawFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # cv2.imshow("Gray Frame", grayFrame)
    # cv2.imshow("Blurred Frame", blurredFrame)
    cv2.imshow("Ghost Frame", deltaFrame)
    cv2.imshow("Threshold Frame", thresholdFrame)
    # cv2.imshow("Diluted frame", dilutedFrame)
    cv2.imshow("Motion Detection", rawFrame)

    key = cv2.waitKey(1)

    # QUIT PROGRAM
    if key == ord('q'):
        break

    # CALIBRATE and CAPTURE new REFERENCE
    if key == ord('c'):
        firstFrame = blurredFrame
        continue

print("Frames Rendered :", frameCount)
video.release()
cv2.destroyWindow
