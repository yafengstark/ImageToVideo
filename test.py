import cv2
item = 'SmirkBoy00001.jpg'

print('image: ' + item)



img = cv2.imread(item)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()