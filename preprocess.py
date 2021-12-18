import cv2
import numpy as np 

class Preprocess:

    def histogram_equlization_rgb(self, img):
        # Simple preprocessing using histogram equalization 
        # https://en.wikipedia.org/wiki/Histogram_equalization

        intensity_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        intensity_img[:, :, 0] = cv2.equalizeHist(intensity_img[:, :, 0])
        img = cv2.cvtColor(intensity_img, cv2.COLOR_YCrCb2BGR)

        # For Grayscale this would be enough:
        # img = cv2.equalizeHist(img)

        return img

    # Add your own preprocessing techniques here.
    
    
     

    def brightnessCorrection(self, img):
    
        b = 30
        c = 50
        
        #values that slightly improve face detection:  b = 50 and c = 40
        #values that improve ear detection: b = 30 and c = 20  
        
        new_img = np.zeros(img.shape, img.dtype)
        
        HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        H, S, V_brightness = cv2.split(HSV)

        limit = 255 - b
       
        #popravimo vrednosti, glede na podani value
        V_brightness[V_brightness > limit] = 0
        V_brightness[V_brightness <= limit] += b

        

        corrected_hsv = cv2.merge((H, S, V_brightness))
        new_img = cv2.cvtColor(corrected_hsv, cv2.COLOR_HSV2BGR)
        
        #cv2.imwrite(filename + '.brightness.jpg', new_img)
        
        return new_img
        
    def contrastAdjustment(self, img):
    
        b = 30
        c = 50
    
        new_img = np.zeros(img.shape, img.dtype)
        
        HSL = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        H, S, L_contrast = cv2.split(HSL)

        limit = 255 - c
        
        L_contrast[L_contrast > limit] = 255
        L_contrast[L_contrast <= limit] += c
        
        corrected_hsl = cv2.merge((H, S, L_contrast))
        new_img = cv2.cvtColor(corrected_hsl, cv2.COLOR_HLS2BGR)
        
        #cv2.imwrite(filename + '.contrast.jpg', new_img)
        
        return new_img


    def grayscale(self, img):

        new_img = np.zeros(img.shape, img.dtype)
        
        new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #cv2.imwrite(filename + '.grayscale.jpg', new_img)
        
        return new_img
       

    def changeResolution(self, img): 
    
        new_img = np.zeros(img.shape, img.dtype)
        
       
        h, w, c = img.shape
        
        new_img = cv2.resize(img, (int(w-80), int(h-60))) 
    
        return new_img; 
    #contrastAdjustment(brightnessCorrection(img))
    #brightnessCorrection(img)
    #contrastAdjustment(img)
    #grayscale(img)
