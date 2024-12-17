
import numpy as np
import cv2
from PIL import Image
import pytesseract
def process_image(imagepath):
    screenshot = Image.open(imagepath)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # cv2.imshow("Screenshot", screenshot)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    text = pytesseract.image_to_string(screenshot,lang='chi_sim')
    return text