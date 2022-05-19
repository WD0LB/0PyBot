from Camera import Camera
from Authenticator import authen
from os import path,mkdir


class Faceid:

    def __init__(self):
        self.au=authen()
        self.cam=Camera()
        self.reg_path=path.join(path.dirname(path.abspath(__file__)),'FaceDB')
        if not(path.isdir(self.reg_path)):
            mkdir(self.reg_path)
        self.reg_index=path.join(self.reg_path,'Regindex')
        # load usernames database
        self.userDB=[]
        if (path.isfile(self.reg_index)):
            self.userDB=self.get_reg_list()
        self.__PIC_CAP=4
        self.threshold=0.3

    

    def register(self):
        username=input("Username:").strip()
        if not(username in self.userDB or username==""):
            self.userDB.append(username)
            self.cam.snap(self.__PIC_CAP)
            pic_path=path.join(self.reg_path,username)
            mkdir(pic_path)
            self.cam.save_snaps(pic_path,username)
            self.save_reg_list()
            return 1
        else:
            print("[!!!!!!!!!!!] Username not Valid")
            return 0



    def get_reg_list(self):
        self.userDB.clear()
        with open(self.reg_index,'r') as file:
            user_db=[]
            user_db=file.read().splitlines()
            return user_db
    
    def save_reg_list(self):
        with open(self.reg_index,'a') as file:
            for username in self.userDB:
                file.write(username+'\n')


    def authenticate(self):
        self.get_reg_list()
        username=input("Username:").strip()
        if not(username in self.userDB or username==""):
            client=self.cam.snap(1)
            users=self.cam.load_snaps(username)
            self.au.extract_candidates(users)
            self.au.process_target(client)
            users_preds=self.au.get_candidates_embedding()
            client_preds=self.au.get_target_embedding()
            score=0
            for i in range(0,self.__PIC_CAP):
                score=score +self.au.is_match(client_preds[0],users_preds[i])
            
            
            if((score/self.__PIC_CAP)<=self.threshold):
                print(f"Successfully Loged In as {username} \ Score: {score/self.__PIC_CAP} :)")
                return 1
            else:
                print(f"You are Not {username} \ Score: {score/self.__PIC_CAP} :( ")
                return 0
        else:
            print("Username not Valid")
            return 0





def test():
    id=Faceid()
    execode=id.authenticate()
    print("execode: " +str(execode))





test()