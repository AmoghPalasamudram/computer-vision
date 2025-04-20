import cv2
import easyocr
import matplotlib.pyplot as plt

image_path = 'C:/amogh/personal/work/projects/computer-vision/sign-reader/images/image_1.png'
img = cv2.imread(image_path)
reader = easyocr.Reader(['en'], gpu = False)
text_ = reader.readtext(img)
for t in text_:
    print(t)

threshold = 0.27

for t in text_:
    bbox, text , score = t

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
