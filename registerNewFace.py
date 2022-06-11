import cv2
import os
import time

name = input('Enter your name --> ')
roll = input('Enter your roll no --> ')

name = name + '-' + roll

if os.path.exists(f'Faces/{name}.png'):
    print('User already exist.')

else:
    print('Taking photo...')
    cap = cv2.VideoCapture(0)    

    while True:        
        ret,frame = cap.read()
        cv2.imshow('Hit Escape to click picture.', frame)
        
        if cv2.waitKey(1) == 27:
            cv2.imwrite(f"Faces/{name}.png",frame)
            break
            
    cap.release()
    cv2.destroyAllWindows()
    print('Successfully registered your face.')