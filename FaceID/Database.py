import pymongo
from DBconf import conf


class Database:
    def __init__(self) -> None:
        self.__USERNAMEPROP="Username"
        self.__PREDICTIONPROP="Preds"
        self.client=pymongo.MongoClient(conf["__CLIENT_PROTOCOL"])
        self.db=self.client[conf["__DATABASE_NAME"]]

    def get_prop(self,index):
        if(index==0):
            return "Object(id)"
        if(index==1):
            return self.__USERNAMEPROP
        if(index==2):
            return self.__PREDICTIONPROP
        else:
            return self.__USERNAMEPROP

    def getUserPreds(self,queryName):
        ls_preds=[]
        _collection=self.db[conf["__COLLECTION_NAME"]]
        x=_collection.find({self.__USERNAMEPROP:queryName})
        for ele in x:
            ls_preds.append(ele)
        return ls_preds


    def getUserNames(self):
        _collection=self.db[conf["__COLLECTION_NAME"]]
        lsname=[]
        for x in _collection.find():
           lsname.append(x[self.__USERNAMEPROP])

        return lsname 

    def switch_user(self,creds):
        self.client.close()
        
        if(creds==""):
            self.client=pymongo.MongoClient(conf["__CLIENT_PROTOCOL"])
        else:
            self.client=pymongo.MongoClient(creds)

        self.db=self.client[conf["__DATABASE_NAME"]]

    def saveUser(self,userData):
        _collection=self.db[conf["__COLLECTION_NAME"]]
        _collection.insert_one(userData)