from Camera import Camera
from Authenticator import Authen
from Database import Database
from bson.binary import Binary
import pickle


class Faceid:

    def __init__(self):
        self.au=Authen() #instantiate an authenticatior
        self.cam=Camera() #Instantiate a camera
        self.dbConnect=Database() 


        #REGION OPTIONS#
        self.userDB=self.dbConnect.getUserNames() #For loading usernames from DB
        self.__PIC_CAP=4    #Number of pictures to be taken for registration (can be adjusted)
        self.threshold=0.28  #Rate of Error allowed during face matching (can be adjusted)

    
    #This function Handles registration logic
    def register(self):
        self.cam.get_cam()
        username=input("Username:").strip() #Get username
        self.cam.start_feed()   #Show camera feed
        username=username.upper()   #Sanitize
        if not(username in self.userDB or username==""): #Check for malformed inputs
            print("Starting Registration")
            self.userDB.append(username)    #Add user to DB
            self.cam.snap(self.__PIC_CAP,self.au.detector)   #Take pictures
            pics=self.cam.get_snaps()  #Save all pictures to DB
            print("Processing Face Model")
            self.au.process_candidates(pics)
            user_preds=self.au.get_candidates_embedding()
            data_file={self.dbConnect.get_prop(1):username,self.dbConnect.get_prop(2):Binary(pickle.dumps(user_preds,protocol=2),subtype=128)}
            print("Finalizing")
            self.dbConnect.saveUser(data_file)
            self.cam.stop_feed()
            self.cam.release_cam()
            return 1
        else:
            self.cam.stop_feed()    #Stop Camera feed
            self.cam.release_cam()
            print("[!!!!!!!!!!!] Username not Valid")
            return 0
    

    #this function handles authentication logic
    def authenticate(self):
        self.cam.get_cam()
        self.cam.start_feed()
        if(self.userDB.__len__()!=0):
            username=input("Username:").strip() 
            username=username.upper()
            if (username in self.userDB and username!=""):    #Check if user is trying to log to an existing username
                users_preds=pickle.loads(self.dbConnect.getUserPreds(username)[0][self.dbConnect.get_prop(2)])
                for i in range(0,self.__PIC_CAP):
                    client=self.cam.snap(1,self.au.detector) #take a pic for the client
                    self.au.process_target(client)
                    # get model preditction for all pictures
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

    def get_Admin_Permission(self):
        print("This Task Require Admin Permission")
        id=input("Username: ")
        pwd=input("Password: ")

        mongoUrl=f"mongodb+srv://{id}:{pwd}@cluster0.3chrzdb.mongodb.net/?retryWrites=true&w=majority"

    

    def list_users(self):
        print(15*'-')
        print(f"| Username {(3)*' '}|")
        print(15*'-')
        for name in self.userDB:
            print(f"| {name} {(11-len(name))*' '}|")
        print(f"| {12*' '}|")
        print(15*'-')



def test():
    #test if authenticate can be called before registre
    id=Faceid()
    id.register()
    id.authenticate()
    id.list_users()









if __name__=='__main__':
    pass
    # test()