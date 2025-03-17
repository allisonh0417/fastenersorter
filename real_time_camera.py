import cv2
import time
import serial  
from picamera2 import Picamera2
from ultralytics import YOLO

arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (800,480), "format": "RGB888"}) #1920 1080
picam2.configure(video_config)
picam2.start()
model = YOLO("/home/deathstarv3/ee175/best.pt") #yolo model

object_timestamps = {}
DETECTION_THRESHOLD = 5  
output_file = "detected_objects.txt"

while True:
    frame = picam2.capture_array()
    results = model(frame)

    detected_objects = set()
    for result in results:
        for box in result.boxes:
            obj_name = result.names[int(box.cls)]
            detected_objects.add(obj_name)

    current_time = time.time()
    for obj in detected_objects:
        if obj not in object_timestamps:
            object_timestamps[obj] = current_time
        elif current_time - object_timestamps[obj] >= DETECTION_THRESHOLD:
            with open(output_file, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {obj} detected\n")
            print(f"{obj} detected and logged!")
            arduino.write(f"{obj}\n".encode())  #arduino write

    for obj in list(object_timestamps.keys()):  #remove timestamps with no detections to reduce clutter
        if obj not in detected_objects:
            del object_timestamps[obj]

    annotated_frame = results[0].plot()
    cv2.imshow("Camera", annotated_frame)   #camera

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
