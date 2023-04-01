from ultralytics import YOLO
import cv2

class YOLODetector:
    def __init__(self, model1, model2, URL):
        self.model1 = YOLO(model1)
        self.model2 = YOLO(model2)
        self.URL = URL
        self.cap = cv2.VideoCapture(URL)


    def detect_objects(self):
        while True:
            success, img = self.cap.read()
            cv2.namedWindow("Model YOLOv8", cv2.WINDOW_NORMAL)
            cv2.namedWindow("Model YOLOv5", cv2.WINDOW_NORMAL)
            if not success:
                break
            res1 = self.model1(img, device='cpu')
            res1_plotted = res1[0].plot()

            res2 = self.model2(img, device='cpu')
            res2_plotted = res2[0].plot()

            cv2.imshow("Model YOLOv8", res1_plotted)
            cv2.imshow("Model YOLOv5", res2_plotted)

            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

if __name__ == "__main__":
    detector = YOLODetector("yolov8l.pt", "yolov5s.pt", "http://195.196.36.242/mjpg/video.mjpg")
    detector.detect_objects()


# from ultralytics import YOLO
# from effdet import EfficientDet
# import cv2

# class YOLODetector:
#     def __init__(self, model2, URL):
#         self.model1 = EfficientDet(model1 = 'efficientdet-d0', pretrained = True)
#         self.model2 = YOLO(model2)
#         self.URL = URL
#         self.cap = cv2.VideoCapture(URL)


#     def detect_objects(self):
#         while True:
#             success, img = self.cap.read()
#             cv2.namedWindow("EffDet", cv2.WINDOW_NORMAL)
#             cv2.namedWindow("YOLOv5", cv2.WINDOW_NORMAL)
#             if not success:
#                 break
#             res1 = self.model1.forward(img)
#             res1_plotted = self.model1.visualize(img, res1)

#             res2 = self.model2(img, device='cpu')
#             res2_plotted = res2[0].plot()

#             cv2.imshow("EffDet", res1_plotted)
#             cv2.imshow("YOLOv5", res2_plotted)

#             if cv2.waitKey(1) & 0xFF == ord('q'): 
#                 break

# if __name__ == "__main__":
#     detector = YOLODetector("yolov5s.pt", "http://195.196.36.242/mjpg/video.mjpg")
#     detector.detect_objects()


