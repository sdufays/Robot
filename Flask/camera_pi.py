import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self, chance1, chance2):
        success, image = self.video.read()
        image = cv2.flip(image, 0)
        image = cv2.flip(image, 1)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        background = image
        height, width, _ = background.shape
        overlay = background.copy()
        radius = 80
        cv2.circle(overlay,
                        (width-radius,height-radius),
                        radius,
                        (0, 255, 255),
                        -1,
                        8) #this is right circle

        if chance1 == 1: #this is forward
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-radius,height-2*radius),
                (0,0,255),
                8)
        if chance1 == 2: #this is left
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-2*radius,height-radius),
                (0,0,255),
                8)
        if chance1 == 3: #this is backward
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-radius,height),
                (0,0,255),
                8)
        if chance1 == 4: #this is right
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width,height-radius),
                (0,0,255),
                8)
        
        cv2.circle(overlay,
                        (radius,height-radius),
                        radius,
                        (0, 255, 255),
                        -1,
                        8) #this is left circle

        if chance2 == 1: #this is forward
            cv2.arrowedLine(overlay,
                            (radius,height-radius),
                            (radius,height-2*radius),
                            (0,0,255),
                            8)
        if chance2 == 2: #this is left
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (0,height-radius),
                (0,0,255),
                8)
        if chance2 == 3: #this is backward
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (radius,height),
                (0,0,255),
                8)
        if chance2 == 4: #this is right
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (2*radius,height-radius),
                (0,0,255),
                8)

        added_image = cv2.addWeighted(background,1,overlay,0.5,0)
        ret, jpeg = cv2.imencode('.jpg', added_image)
        return jpeg.tobytes()
