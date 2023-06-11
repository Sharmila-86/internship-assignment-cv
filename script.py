!pip install opencv-python
import cv2
from google.colab.patches import cv2_imshow
import cv2

def get_ouput_image(original_image_path: str, fully_annotated_image_path: str,partially_annotated_image_path: str):
  if not isinstance(str, str):
    raise TypeError("Input must be a string")
  from google.colab.patches import cv2_imshow
  import cv2
  image = cv2.imread("str.jpg")
  cv2_imshow(image)
  x, y, width, height = 250, 250, 300, 200
  image2 = cv2.rectangle(image, (x, y), (x+width, y+height),(0, 255, 0), 2)
  image = cv2.imread('image.jpg')
  cv2_imshow(image2)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
 
  cv2.imwrite(partially_annotated_image_path, image2.jpg)
  annotated_image_path = 'image2.jpg'
  cv2.imwrite(annotated_image_path, image2)

print("Annotated image saved successfully.")
import shutil
def copy_partial_annotated_image(source_path, destination_folder):
  shutil.copy(source_path, destination_folder)
