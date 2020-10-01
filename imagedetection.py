#This code is working absolutely fine!
import cv2
import os
import time
from MessageEmail.email_message import *
count=0
time_enter_flag=False
next_time=time.time()
def inform():
    email_send()
    send_message()    #to operate this we have to change Auth token!
def new(img_counter):
    name='frame1.jpg'
    img=cv2.imread(name,cv2.IMREAD_UNCHANGED)
    scale_percent=23
    px=0.0264583333   #1px=0.0264583333cm
    
    #calculate the 50 percent of original dimensions
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    # dsize
    dsize = (width, height)
    output = cv2.resize(img, dsize) #output contains resized image.The above logic is for     resized image
    
    cv2.imshow("Original Image",output)
    cv2.waitKey(100)
    gray=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
    FaceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces=FaceCascade.detectMultiScale(   #use FaceCascade object to detect faces
         gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20,20)
        )
    img_data=[]
    for(x,y,w,h) in faces:                   #ploting a rectangle
        
        cv2.rectangle(output,(x,y),(x+w,y+h),(255,90,10),2)
        data=(x,y,x+w,y+h) 
        img_name = "detected.jpg"
        cv2.imwrite(img_name,output)
        cv2.imshow('Detected faces',output)    
        cv2.waitKey(10)
        img_data.append(data) #data is a tuple which contains the dimensions 
    
    length=[]
    breadth=[]
    total_dist=[]
    dist_flag=False
    
    if (len(faces) > 1 and len(faces) < 5):    #if more than 4 faces detected,send mail and SMS
        
        for i in img_data:
            length.append(i[0]/2)            #contains x axis info of image(x axis values)
            breadth.append(i[1]/2)           #contains y axis info of image(y axis values)
        for i in range(len(faces)-1):        
            for j in range(1,len(faces)):
                if(i!=j): #this logic is being added to avoid the calculation of distance     between you and yourself!   
                    distance=(((length[j]-length[i])**2)+((breadth[j]-breadth[i])**2))**0.5
                    distance=distance*0.0264583333 #converted px to cm
                    total_dist.append(int((distance)))
                   
                    if distance<40:      #if distance is less than 40 cm,voialated
                        dist_flag=True
                        break
                        
                    
                        #Pair of person on which distance is calculated
        print(total_dist)          #This array consist of all the distances in pixels     between each other
    elif len(faces)<=1:
            if os.path.exists("frame1.jpg"):
                os.remove("frame1.jpg")
            else:
                print("The file does not exist")
            dist_flag=False
            
    else:
        dist_flag=True        
    if dist_flag==True:
        global count
        global next_time
        if(count==0):
            
            count=1
            time_enter_flag=True
            now_time=time.time()
            next_time=now_time+30
            inform()
        else:
            
            now_time=time.time()
            
            if(now_time>next_time):
                
                next_time=now_time+30         #delay of 30secs added!
                inform()
                if os.path.exists("frame1.jpg"):
                    os.remove("frame1.jpg")
                else:
                    print("The file does not exist")
            
            
        
       
        
        
        
        

    
    
    

