from cv2 import VideoCapture,imshow,imwrite,imread,waitKey,destroyAllWindows,CAP_DSHOW

from os import path,mkdir
class Camera:
    

    def __init__(self) -> None:
        self._cam=VideoCapture(0,CAP_DSHOW)
        self.snaps=[]
        self.faces=[]
        self.__INDEX_LIST='index'
        self.db=path.join(path.dirname(path.abspath(__file__)),'FaceDB')
        if not(path.isdir(self.db)):
            mkdir(self.db)
        # self.index_list=path.join(self.db,'faceindex')

    # this function takes pictures using the main camera
    def snap(self,count):
        temp_ret,temp_frame=self._cam.read()
        for i in range(0,count):
            ret,frame=self._cam.read()
            self.snaps.append(frame)
            print("picture was taken",i)
        if(count==1):
            return self.snaps[0]
        else:
            return self.snaps


    
    #this function show the current video feed
    def show_feed(self):
        while(True):
            ret,frame=self._cam.read()
            imshow('Video', frame)
            if waitKey(25) == 13: 
                break
        destroyAllWindows()  

    #this function saves all snaps to a given path and name
    def save_snaps(self ,dir,name):
        index_file=path.join(dir,self.__INDEX_LIST)
        with open(index_file,'a') as file:
            for i in range(0,self.snaps.__len__()):
                file_name=path.join(dir,name+str(i)+'.jpg')
                imwrite(file_name,self.snaps[i])
                file.write(file_name+'\n')

        self.snaps.clear()
        
    def get_index_list(self,username):
        index_file=path.join(self.db,username)
        index_file=path.join(index_file,self.__INDEX_LIST)
        with open(index_file,'r') as file:
            face_db=[]
            face_db=file.read().splitlines()
            return face_db

    def load_snaps(self,name):
        self.snaps.clear()
        face_db=self.get_index_list(name)
        for pic in face_db:
            pixel=imread(pic)
            self.snaps.append(pixel)
        return self.snaps





        


