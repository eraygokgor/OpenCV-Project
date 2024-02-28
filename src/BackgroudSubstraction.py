import cv2 as cv


class BackGroundSubtractor:
    def __init__(self, input_video_path):
        self.input_video = input_video_path

    def substract_background(self, algo='MOG2'):
        if algo == 'MOG2':
            back_sub = cv.createBackgroundSubtractorMOG2()
        else:
            back_sub = cv.createBackgroundSubtractorKNN()

        capture = cv.VideoCapture(cv.samples.findFileOrKeep(self.input_video))

        if not capture.isOpened:
            print('Unable to open: ' + self.input_video)
            exit(0)

        while True:
            ret, frame = capture.read()
            if frame is None:
                break

            fg_mask = back_sub.apply(frame)

            cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
            cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

            cv.imshow('Frame', frame)
            cv.imshow('FG Mask', fg_mask)

            keyboard = cv.waitKey(30)
            if keyboard == 'q' or keyboard == 27:
                break
