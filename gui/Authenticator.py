from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from scipy.spatial.distance import cosine
from mtcnn import MTCNN
from numpy import asarray
from PIL import Image


class authen:
    def __init__(self):
        self.__MODEL=VGGFace(model='resnet50',include_top=False,input_shape=(224,224,3),pooling='avg') #detection model RESNET50
        self.target=[] # for holding target frame
        self.candidates=[] # for holding potential matches frames
        self.detector=MTCNN() # face detector model
        self.required_size=(224,224) # the size of inputs to the model (w,h)

    

    #this function adjust the client face size and prepares it for input
    def process_target(self,face):
        #result=self.detector.detect_faces(pixels)
        # extact the bounding box
        #x1,y1,width,height=result[0]['box']
        #x2,y2=x1+width,y1+height
        #extract face
        #resize pixels to the model size
        img=Image.fromarray(face)
        img=img.resize(self.required_size)
        face_array=asarray(img)
        self.target.append(face_array)

    #this function adjust stored candidates face size and prepares them for input
    def process_candidates(self,snaps):
        for pixels in snaps:
            # result=self.detector.detect_faces(pixels)
            # #extract bounding box
            # x1,y1,width,height=result[0]['box']
            # x2,y2=x1+width,y1+height
            # #extract face
            # face=pixels[y1:y2,x1:x2]
            # #resize pixels to the model size
            img=Image.fromarray(pixels)
            img=img.resize(self.required_size)
            face_array=asarray(img)
            self.candidates.append(face_array)

    #returns model predictions of the candidates
    def get_candidates_embedding(self):
        samples=asarray(self.candidates,'float32')
        samples=preprocess_input(samples,version=2)
        yhat=self.__MODEL.predict(samples)
        return yhat
    
    #return model predictions fo the client
    def get_target_embedding(self):
        sample=asarray(self.target,'float32')
        sample=preprocess_input(sample,version=2)
        xhat=self.__MODEL.predict(sample)
        return xhat

    # check for matches between client and candidates predictions
    def is_match(self,target_embedding,candidate_embedding):
        #calculate distance between embeddings
        score=cosine(target_embedding,candidate_embedding)
        return score
        # if score <=thresh:
        #     print('>face is a match (%.3f <= %.3f)' % (score,thresh))
        #     return score
        # else:
        #     print('>face is NOT a Match (%.3f <= %.3f)' % (score,thresh))
        #     return score