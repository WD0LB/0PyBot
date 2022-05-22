from Camera import Camera
from Authenticator import authen
from os import path,mkdir

class Faceid:

    def __init__(self):
        self.au=authen() #instantiate an authenticatior
        self.cam=Camera() #Instantiate a camera
        self.reg_path=path.join(path.dirname(path.abspath(__file__)),'FaceDB') #Path to DB
        if not(path.isdir(self.reg_path)):
            mkdir(self.reg_path)
        self.reg_index=path.join(self.reg_path,'Regindex') #Path to registerd users index
        self.userDB=list() #For loading usernames from DB
        # if (path.isfile(self.reg_index)):
        # self.userDB=self.get_reg_list()
        self.__PIC_CAP=4    #Number of pictures to be taken for registration (can be adjusted)
        self.threshold=0.3  #Rate of Error allowed during face matching (can be adjusted)

    
    #This function Handles registration logic
    def register(self):
        self.cam.get_cam()
        self.cam.start_feed()   #Show camera feed
        self.userDB=self.get_reg_list()
        username=input("Username:").strip() #Get username
        username=username.upper()   #Santize
        if not(username in self.userDB or username==""): #Check for malformed inputs
            self.userDB.append(username)    #Add user to DB
            self.cam.snap(self.__PIC_CAP,self.au.detector)   #Take pictures
            pic_path=path.join(self.reg_path,username)  #Create new path for user
            mkdir(pic_path)
            self.cam.save_snaps(pic_path,username)  #Save all pictures to DB
            self.save_reg_list()    #Save username to RegIndex
            self.cam.stop_feed()
            self.cam.release_cam()
            return 1
        else:
            self.cam.stop_feed()    #Stop Camera feed
            self.cam.release_cam()
            print("[!!!!!!!!!!!] Username not Valid")
            return 0


    #this function read all username from RegIndex
    def get_reg_list(self):
        self.userDB.clear()
        if(path.isfile(self.reg_index)):
            with open(self.reg_index,'r') as file:
                user_db=[]
                user_db=file.read().splitlines()
                return user_db
        else:
            print("Could not find any users")
            return []
    
    #this function saves current usernames in RegIndex
    def save_reg_list(self):
        with open(self.reg_index,'w') as file:
            for username in self.userDB:
                file.write(username+'\n')

    #this function handles authentication logic
    def authenticate(self):
        self.cam.get_cam()
        self.cam.start_feed()
        self.userDB=self.get_reg_list() #get all usernames in DB
        self.userDB
        if(self.userDB.__len__()!=0):
            username=input("Username:").strip() 
            username.upper()
            if not(username in self.userDB or username==""):    #Check if user is trying to log to an existing username
                for i in range(0,self.__PIC_CAP):
                    client=self.cam.snap(1,self.au.detector) #take a pic for the client
                    users=self.cam.load_snaps(username) # load pic of existing candidates
                    # prepare all pictures for processing 
                    self.au.process_candidates(users) 
                    self.au.process_target(client)
                    # get model preditction for all pictures
                    users_preds=self.au.get_candidates_embedding()
                    client_preds=self.au.get_target_embedding()
                    score=0 #final prediction score
                    for i in range(0,self.__PIC_CAP):
                        score=score +self.au.is_match(client_preds[0],users_preds[i])   #check predictions match and accumulate score
                    score/=self.__PIC_CAP #get average of all scores accumulated
                    if((score)<=self.threshold):
                        print(f"Successfully Loged In as {username} \ Score: {score} :)")
                        self.cam.stop_feed()
                        self.cam.release_cam()
                        return 1
                    else :
                        continue
                print(f"You are Not {username} \ Score: {score} :( ")
                self.cam.stop_feed()
                self.cam.release_cam()
                return 0
            else:
                print("Username not Valid")
                self.cam.stop_feed()
                self.cam.release_cam()
                return 0
        else:
            self.cam.stop_feed()
            self.cam.release_cam()
            return 0


def test():
    #test if authenticate can be called before registre
    id=Faceid()
    id.register()
    execode=id.authenticate()
    print("execode: " +str(execode))





if __name__=='__main__':