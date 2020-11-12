import cv2 as cv
import numpy as np

# your_name is the name I give to the variable representing the whole picture. (Because it's a picture from the movie Your Name)
# After you copy the file path of your picture, you can paste it in the brackets below.
your_name = cv.imread(r'C:\Users\user\Desktop\Kodlama\image processing\city.png', cv.IMREAD_UNCHANGED)
# needle_name is the name I give to the variable that represents the selected part from the picture.
needle_img = cv.imread(r'C:\Users\user\Desktop\Kodlama\image processing\sign.png', cv.IMREAD_UNCHANGED)

# You can review the documentation on OpenCV's website for the TM_CCOEFF_NORMED section and more.
result = cv.matchTemplate(your_name, needle_img, cv.TM_CCOEFF_NORMED)

# In this part I reserved as a comment, you can see the possible position of the piece you selected in the whole picture in a more distinct white form than the others.
"""
cv.imshow('Result', result)
cv.waitKey()

"""

# get the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

# I have set a limit on the accuracy of the match by giving a threshold value.
# If the accuracy rate is less than this number (0.8 for my code) 'Needle not found.' text will appear on the screen.
# If the value is greater than or equal to this number, the location of the selected part will appear in the pop-up window.
thereshold = 0.8
if max_val >= thereshold:
    print('Found needle.')
    
    # get dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    
    # With this code, I have shown the location of the part we selected in a green rectangle.
    cv.rectangle(your_name, top_left, bottom_right,
                 color = (0, 255, 0), thickness=2, lineType=cv.LINE_4)
    cv.imshow('Result', your_name)
    cv.waitKey()
else:
    print('Needle not found.')
    






