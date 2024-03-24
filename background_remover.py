import cv2
import numpy as np

def remove_background(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or unable to load the image.")
        return
    
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1,65), np.float64)
    fgdModel = np.zeros((1,65), np.float64)
    rect = (50, 50, img.shape[1]-50, img.shape[0]-50)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    return img

def main():
    image_path = input("Enter the path to the image: ")
    output_image = remove_background(image_path)
    if output_image is not None:
        cv2.imshow('Foreground', output_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
