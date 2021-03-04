import cv2

# main class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # cv2 stream capture
    
    def __del__(self):
        self.video.release()
    
    # overlay function
    def get_frame(self, left_c, right_c):
        success, image = self.video.read()
        radius = 80
        image = cv2.flip(image, 0)
        image = cv2.flip(image, 1)
        # creates the dimensions for the stream
        background = image
        height, width, _ = background.shape
        overlay = background.copy()

        # first left circle
        cv2.circle(overlay,
                        (width-radius,height-radius),
                        radius,
                        (74, 204, 224),
                        -1,
                        8)

        if left_c == 1: 
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-radius,height-2*radius),
                (255, 74, 219),
                8)
        if left_c == 2:
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-2*radius,height-radius),
                (255, 74, 219),
                8)
        if left_c == 3: 
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-radius,height),
                (255, 74, 219),
                8)
        if left_c == 4: 
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width,height-radius),
                (255, 74, 219),
                8)

        # second right circle
        cv2.circle(overlay,
                        (radius,height-radius),
                        radius,
                        (74, 204, 224),
                        -1,
                        8) 

        if right_c == 1: 
            cv2.arrowedLine(overlay,
                            (radius,height-radius),
                            (radius,height-2*radius),
                            (0,0,255),
                            8)
        if right_c == 2: 
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (0,height-radius),
                (0,0,255),
                8)
        if right_c == 3: 
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (radius,height),
                (0,0,255),
                8)
        if right_c == 4: 
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (2*radius,height-radius),
                (0,0,255),
                8)
        # combine the overlay and the stream
        added_image = cv2.addWeighted(background,1,overlay,1,0)
        # convert image to jpg and return 
        ret, jpeg = cv2.imencode('.jpg', added_image)
        return jpeg.tobytes()



