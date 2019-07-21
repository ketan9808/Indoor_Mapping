import cv2
import pyzbar.pyzbar as pyzbar
import pyttsx3

def txt_to_speech(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()
    
location = {1001 : 'Welcome to techienest',
            1002:'ground floor',
            1003: 'Basement',
            1004:'reception',
            1005:'classroom 1A',
            1006:'classroom 1B',
            1007:'classroom 0A'}

cap = cv2.VideoCapture(0) #'http://172.20.10.2:4747/video'
font = cv2.FONT_HERSHEY_PLAIN
flag = True
while True:
    status, frame = cap.read()
    if(status == True):
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            if (obj.data).decode("utf-8") == "Main Gate" :
                if flag:
                    txt_to_speech("Welcome to Techie Nest")
                    txt_to_speech("To reach the groung floor section take ten steps directly ahead and take a sharp left turn")
                    txt_to_speech("Climb the three stairs to Enter the groung floor hall")
                    txt_to_speech("Look to your right for further instructions")
                    flag = False
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(5)
        
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
    else:
        txt_to_speech('the camera can not start, please try again later')