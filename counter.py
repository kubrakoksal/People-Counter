import io, os
from numpy import random
from google.cloud import vision
from Pillow_Utility import draw_borders, Image
import pandas as pd
import time
from sort import *
import numpy as np
import argparse
import cv2

up=0
down=0
cap = cv2.VideoCapture('Pedestrian.mp4')
mot_tracker = Sort() 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"Token.json"
client = vision.ImageAnnotatorClient()

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(100, 3),dtype="uint8")
dict_person={}


count=0;
while(1):
    #ret, frame = cap.read()
    frame=cv2.imread(str(count)+".jpg")
    #width  = cap.get(3) # float
    #height = cap.get(4) # float
    height, width, channels = frame.shape

    print(width,height)
    cv2.imwrite("frame.jpg",frame)
    imagetemp=open("frame.jpg", 'rb')
    content = imagetemp.read()
    start = time.time()

    image = vision.types.Image(content=content)
    response = client.object_localization(image=image)
    localized_object_annotations = response.localized_object_annotations
    end = time.time()
    print(end-start)
    detections=[]
    cv2.line(frame, (3,400), (1181,400), (0,0,0), 3) 
    cv2.putText(frame, (str(up)+"---"+str(down)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX,2, (0,0,0), 2)
    df = pd.DataFrame(columns=['name', 'score'])
    print(localized_object_annotations)
    for obj in localized_object_annotations:
        if(obj.name=="Person" and obj.score>=0.82):
            df = df.append(
                dict(
                    name=obj.name,
                    score=obj.score
                ),
                ignore_index=True)
            
            r, g, b = random.randint(150, 255), random.randint(
                150, 255), random.randint(150, 255)
        
            bounding=obj.bounding_poly
            detections.append([bounding.normalized_vertices[0].x * width, bounding.normalized_vertices[0].y * height,
            bounding.normalized_vertices[2].x * width, bounding.normalized_vertices[2].y * height,obj.score])
    print(detections)
    trackers = mot_tracker.update(detections)
    end = time.time()
    a=0
    for d in trackers:
        x=int(d[0])
        y=int(d[1])
        w=int(d[2]-d[0])
        h=int(d[3]-d[1])
        color = [int(c) for c in COLORS[a]]
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        text = "{}".format(d[4])
        cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, color, 2)
        if(y<=403 and (y+h)>=397):
            if(d[4] not in dict_person):
                dict_person[d[4]] = y
                cv2.putText(frame, "Alana girdi", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color, 2)
        else:
            print("BURADA")
            print(dict_person)
            if(d[4] in dict_person and  (dict_person[d[4]]-y>0)):
                up+=1
                dict_person.pop(d[4])
            elif(d[4] in dict_person and  (dict_person[d[4]]-y<0)):
                down+=1
                dict_person.pop(d[4])


        a+=1
    print(df)
    cv2.imshow("count",frame)
    cv2.waitKey(1)
    count+=1
cap.release()
cv2.destroyAllWindows()	
