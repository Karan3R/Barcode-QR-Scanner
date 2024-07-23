import numpy as np
import cv2
from pyzbar.pyzbar import decode

def decode_image(image_path):
    # Load image
    img = cv2.imread(image_path)
    # Decode the barcodes/QR codes
    decoded_objects = decode(img)
    
    for obj in decoded_objects:
        # Draw rectangle around the detected barcode/QR code
        points = obj.polygon
        if len(points) == 4:
            pts = np.array(points, dtype=np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 255, 0), 2)
        # Print decoded data
        print("Type:", obj.type)
        print("Data:", obj.data.decode('utf-8'))
    
    # Save or display the result
    cv2.imwrite('decoded_image.jpg', img)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
decode_image('C:/Users/ADMIN/Downloads/githubqr.png')
