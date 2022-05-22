from threading import Thread,Lock
from cv2 import VideoCapture,imshow,imwrite,imread,waitKey,destroyAllWindows,CAP_DSHOW,rectangle
from cv2 import CascadeClassifier,cvtColor,COLOR_BGR2GRAY
from os import path,mkdir
class Camera:
    

    def __init__(self) -> None:
        self._cam=VideoCapture(0,CAP_DSHOW) #select internal camera as feed source
        self.snaps=[] # to store captured frames
        self.stop_cdt=False # condition to stop the camera feed
        self.mutex=Lock()   # Mutex for access control to stop condition
        self.face_cascade=CascadeClassifier(path.join(path.dirname(path.abspath(__file__)),'cascades/haarcascade_frontalface_alt2.xml'))
        self.__INDEX_LIST='index' # name of the index file
        self.db=path.join(path.dirname(path.abspath(__file__)),'FaceDB') #name and path of the DB
        if not(path.isdir(self.db)):
            mkdir(self.db)

    # this function takes pictures using the main camera
    def snap(self,count,detec):
        temp_ret,temp_frame=self._cam.read()
        box=[]
        for i in range(0,count):
            #loop until a face box can be detected
            while True:
                ret,frame=self._cam.read()
                box=self.get_face_box(frame,detec)
                if (box.__len__()!=0):
                    break

            #extract the face from the frame
            frame=self.extract_face(frame,box)
            #add the face to main array
            
            self.snaps.append(frame)
            if(count==1):
                pass
            else:
                print("picture was taken",i+1)

            #if only one frame was taken return corresponding face
        if(count==1):
            return self.snaps[0]
        else:
            return self.snaps
    
    # this function detects faces and return detection box coordinates
    def get_face_box(self,fra,detector): 
        result=detector.detect_faces(fra)
        return result

    # this function uses face box coordinate to extract a face from a frame
    def extract_face(self,fra,frame_box):
        #extract bounding box
        x1,y1,width,height=frame_box[0]['box']
        #create face coordinates
        x2,y2=x1+width,y1+height
        #extract face
        return fra[y1:y2,x1:x2]


    
    #this function show the current video feed
    def show_feed(self):
        while(True):
            ret,frame=self._cam.read()
            gray=cvtColor(frame,COLOR_BGR2GRAY)
            box=self.face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
            for (x1,y1,width,height) in box:
                x2,y2=x1+width,y1+height
                rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
            imshow('Video Feed', frame)
            key=waitKey(1)
            self.mutex.acquire()
            if self.stop_cdt or key==ord('q'): 
                self.mutex.release()
                self.stop_cdt=False
                destroyAllWindows()
                exit(1)
            self.mutex.release()

    #this function starts a new thread for the show feed function
    def start_feed(self):
        self.thread=Thread(target=self.show_feed,args=())
        self.thread.daemon=True
        self.thread.start()
    def stop_feed(self):
        self.mutex.acquire()
        self.stop_cdt=True
        self.mutex.release()

    #this function saves all snaps to a given path and name
    def save_snaps(self ,dir,name):
        index_file=path.join(dir,self.__INDEX_LIST)
        with open(index_file,'a') as file:
            for i in range(0,self.snaps.__len__()):
                file_name=path.join(dir,name+str(i)+'.jpg')
                imwrite(file_name,self.snaps[i])
                file.write(file_name+'\n')

        self.snaps.clear()
        

    #this function reads all present face in a dir using the index file
    def get_index_list(self,username):
        index_file=path.join(self.db,username)
        index_file=path.join(index_file,self.__INDEX_LIST)
        if (path.isfile(index_file)):
            with open(index_file,'r+') as file:
                face_db=[]
                face_db=file.read().splitlines()
                return face_db
        else:
            print('\{Error\} Couldn\'t find Index File ')
            return []


    #this function loads all faces from dir and return a refrence to the array that holds them
    def load_snaps(self,name):
        self.snaps.clear()
        face_db=self.get_index_list(name)
        for pic in face_db:
            pixel=imread(pic)
            self.snaps.append(pixel)
        return self.snaps


#--------------------------OPTIONAL-------------------------------


# class VideoStream():
#     def __init__(self,src=0) -> None:
#         self.capture=VideoCapture(0,CAP_DSHOW)
#         self.frame=0
#         self.thread=Thread(target=self.update,args=())
#         self.thread.daemon=True
#         self.thread.start()

    
#     def update(self):
#         while True:
#             if self.capture.isOpened():
#                 (self.status,self.frame)=self.capture.read()
#             sleep(.01)
        

#     def show_frame(self):
#         imshow('Video Feed',self.frame)
#         key=waitKey(1)
#         if key==ord('q'):
#             self.capture.release()
#             destroyAllWindows()
#             exit(1)


