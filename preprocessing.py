# step 1 :  select image from local pc 
# step 2 :  perform edge detection (canny method)

# requirements
import cv2
from matplotlib import pyplot as plt
from tkinter import Tk , filedialog
from fastapi import FastAPI



# Edge detection process 
def pre_processing(path):
    if path:
        image = cv2.imread(file_path)
        if image is None:
            print("Failed to load image...")
        else:
            fig,axs = plt.subplots(1,2, figsize = (10,5))
            # coloring the image to RGB
            image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            axs[0].imshow(image_rgb)
            axs[0].set_title("Image Preview")
            axs[0].axis('off')
            # image blur
            blur_image = cv2.GaussianBlur(image,(5,5),0)
            # canny edge_detector process
            t_lower = 50
            t_upper = 50
            canny_image = cv2.Canny(blur_image,t_lower,t_upper)
            axs[1].imshow(canny_image, cmap = 'gray')
            axs[1].set_title("Cannay Edge Detection")
            axs[1].axis('off')
            plt.tight_layout()
            plt.show()

# dynamic access to files
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title = "Select Image", filetypes= [("Image Files", "*.jpg *.png *.jpeg *.bmp")])
pre_processing(file_path)



