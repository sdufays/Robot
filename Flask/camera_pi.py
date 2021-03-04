import time
import io
import threading
import picamera
import cv2
import numpy as np

class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (320, 240)
            camera.hflip = True
            camera.vflip = True

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                data = np.fromstring(stream.getvalue(), dtype=np.uint8)
                image = cv2.imdecode(data, 1)
                # cls.frame = stream.read()

                # background = cv2.imencode('.jpg', cls.frame)
                
                # background = cv2.imread('image.jpg')
                height, width, _ = image.shape
                # overlay = background.copy()
                radius = 80

                cv2.circle(image,
                                (width-radius,height-radius),
                                radius,
                                (0, 255, 255),
                                -1,
                                8)
                cv2.arrowedLine(image,
                                (width-radius,height-radius),
                                (width-radius,height-2*radius),
                                (0,0,255),
                                8)

                cv2.circle(image,
                                (radius,height-radius),
                                radius,
                                (0, 255, 255),
                                -1,
                                8)
                
                cv2.arrowedLine(image,
                                (radius,height-radius),
                                (radius,height-2*radius),
                                (0,0,255),
                                8)
                    

                # added_image = cv2.addWeighted(background,1,overlay,0.5,0)

                #cv2.imwrite('combined.jpg', background)
                frame1 = image.tobytes()
                ret, cls.frame = cv2.imencode(".jpg", frame1)

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - cls.last_access > 10:
                    break
        cls.thread = None
