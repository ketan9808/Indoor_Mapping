import cv2
import pyzbar
import numpy as np



import speech_recognition as sr
def listen():
    r = sr.recognizer()
    with sr.Microphone as source:
        audio = r.listen(source)
        try:
            text = r.recognize_googel(audio)
            return True, text
        except:
            return False, 'error'

def current_map(Qmap):
    # algorithm to navigate in the qmap
    speak('What is your destination.')
    listen()
    
locations = {1001: 'Welcome to techienest',
             1002: 'Welcome Home'}
loadmap = {'Welcome to techienest':np.zeros((10,10)),# Qmap of techienest
           'Welcome Home':np.zeros((10,10))} # Qmap of home

cap = cv2.VideoCapture(0)
while(1):
    camera_check, frame = cap.read()
    if camera_check == True:
        # check for any QR codes in image
        decodedobjects = pyzbar.decode(frame)
        for obj in decodedobjects:
            data = (obj.data).decode('utf-8)
            if data in locations.keys():
                speak(locations[data])
                current_map(loadmap[locations[data]])
    else:
        # speak the camera is not available please take some assistant
        speak('Camera is not available. Please contact someone for assistant.')
        cap.release()
        break
    
    # replace it with voice command in future
    k = cv2.waitKey(2)
    if k == ord('q')|k == ord('Q'):
        speak('Bye, have a greate journey.')
        cv2.destroyAllWindows()
        cap.release()
        break