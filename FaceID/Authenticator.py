from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from scipy.spatial.distance import cosine
from mtcnn import MTCNN
from numpy import asarray
from PIL import Image


class authen:
    def __init__(self):
        self.__MODEL=VGGFace(model='resnet50',include_top=False,input_shape=(224,224,3),pooling='avg')
        self.target=[]
        self.candidates=[]
        self.detector=MTCNN()
        self.required_size=(224,224)

    

    def process_target(self,pixels):
        result=self.detector.detect_faces(pixels)
        # extact the bounding box
        x1,y1,width,height=result[0]['box']
        x2,y2=x1+width,y1+height
        #extract face
        face=pixels[y1:y2,x1:x2]
        #resize pixels to the model size
        img=Image.fromarray(face)
        img=img.resize(self.required_size)
        face_array=asarray(img)
        self.target.append(face_array)

    
    def extract_candidates(self,snaps):
        for pixels in snaps:
            result=self.detector.detect_faces(pixels)
            #extract bounding box
            x1,y1,width,height=result[0]['box']
            x2,y2=x1+width,y1+height
            #extract face
            face=pixels[y1:y2,x1:x2]
            #resize pixels to the model size
            img=Image.fromarray(face)
            img=img.resize(self.required_size)
            face_array=asarray(img)
            self.candidates.append(face_array)

    def get_candidates_embedding(self):
        samples=asarray(self.candidates,'float32')
        samples=preprocess_input(samples,version=2)
        yhat=self.__MODEL.predict(samples)
        return yhat
    
    def get_target_embedding(self):
        sample=asarray(self.target,'float32')
        sample=preprocess_input(sample,version=2)
        xhat=self.__MODEL.predict(sample)
        return xhat

    def is_match(self,target_embedding,candidate_embedding,thresh=0.3):
        #calculate distance between embeddings
        score=cosine(target_embedding,candidate_embedding)
        if score <=thresh:
            print('>face is a match (%.3f <= %.3f)' % (score,thresh))
            return score
        else:
            print('>face is NOT a Match (%.3f <= %.3f)' % (score,thresh))
            return score