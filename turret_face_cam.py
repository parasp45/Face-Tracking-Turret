import cv2 as cv
import serial
import time

# Replace with the correct port for your system (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux/Mac)
# arduino_port = '/dev/ttyUSB0'  # Change this to match your Arduino's port
# baud_rate = 9600 
# arduino = serial.Serial(port='COM4',baudrate= 9600, timeout=0)
# Wait for the Arduino to initializead

vid = cv.VideoCapture(1)

isture = True

cam_center = 0,0
face_center = 0,0

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

def cam_center_finder(frame):
    cam_w = (frame.shape[1]//2)
    cam_h = (frame.shape[0]//2)
    cam_center = (cam_w,cam_h)
    return cam_center

def face_detection(frame):
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY )
    harr_cascade = cv.CascadeClassifier('har_face.xml') 
    face = harr_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    return face

time.sleep(0)

while True:
    
    istrue, frame = vid.read()
    if isture == False:
        break
    
    cam_center = 0,0
    face_center = 0,0
    

    cam_center = cam_center_finder(frame)
    
    frame = cv.flip(frame, 0)
   
    face = face_detection(frame)
    
    # print('v')
    # print(face)

    for x,y,w,h in face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), thickness=2)

    for x,y,w,h in face:
        x = int(x+(w//2))
        y = int(y+(h//2))
        face_center = (x,y)
    

    (cam_x , cam_y) = cam_center
    (face_x , face_y) = face_center
  
    #   if not face is found give zero value (no movement)
    
    print (face)

    if len(face) == 0: 
        distance_x = 0
        distance_y = 0  
    else:
        distance_x = cam_x - face_x 
        distance_y = cam_y - face_y 
   
    # print (cam_center)
    # print (face_center)

    print(face_x, face_y)
    print(distance_x,distance_y)

    distance = f"{distance_x},{distance_y}\n"
    
    # arduino.write( distance.encode())

    cv.imshow("webcam",frame)

    if cv.waitKey(10) & 0xFF == ord('d'):
        break


arduino.close()
vid.release()
cv.destroyAllWindows()