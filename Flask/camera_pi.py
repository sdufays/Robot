import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self, x1, x2):
        success, image = self.video.read()
        image = cv2.flip(image, 0)
        image = cv2.flip(image, 1)

        background = image
        height, width, _ = background.shape
        overlay = background.copy()
        radius = 80
        cv2.circle(overlay,
                        (width-radius,height-radius),
                        radius,
                        (74, 204, 224),
                        -1,
                        8)

        if x1 == 1: 
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-radius,height-2*radius),
                (255, 74, 219),
                8)
        if x1 == 2:
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-2*radius,height-radius),
                (255, 74, 219),
                8)
        if x1 == 3: #backwards
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width-radius,height),
                (255, 74, 219),
                8)
        if x1 == 4: #this is right
            cv2.arrowedLine(overlay,
                (width-radius,height-radius),
                (width,height-radius),
                (255, 74, 219),
                8)
        
        cv2.circle(overlay,
                        (radius,height-radius),
                        radius,
                        (74, 204, 224),
                        -1,
                        8) #left circle

        if x2 == 1: #forward
            cv2.arrowedLine(overlay,
                            (radius,height-radius),
                            (radius,height-2*radius),
                            (0,0,255),
                            8)
        if x2 == 2: 
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (0,height-radius),
                (0,0,255),
                8)
        if x2 == 3: 
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (radius,height),
                (0,0,255),
                8)
        if x2 == 4: 
            cv2.arrowedLine(overlay,
                (radius,height-radius),
                (2*radius,height-radius),
                (0,0,255),
                8)

        added_image = cv2.addWeighted(background,1,overlay,1,0)
        ret, jpeg = cv2.imencode('.jpg', added_image)
        return jpeg.tobytes()



