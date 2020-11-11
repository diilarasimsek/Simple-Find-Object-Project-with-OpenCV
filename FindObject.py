import cv2 as cv
import numpy as np
your_name = cv.imread(r'C:\Users\user\Desktop\Kodlama\image processing\city.png', cv.IMREAD_UNCHANGED)
needle_img = cv.imread(r'C:\Users\user\Desktop\Kodlama\image processing\sign.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(your_name, needle_img, cv.TM_CCOEFF_NORMED)

"""
cv.imshow('Result', result)
cv.waitKey()

"""

# get the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

thereshold = 0.8
if max_val >= thereshold:
    print('Found needle.')
    
    # get dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    
    cv.rectangle(your_name, top_left, bottom_right,
                 color = (0, 255, 0), thickness=2, lineType=cv.LINE_4)
    cv.imshow('Result', your_name)
    cv.waitKey()
else:
    print('Needle not found.')
    






