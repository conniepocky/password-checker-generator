import cv2
from matplotlib import pyplot as plt

img = cv2.imread("images/cat1.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalcatface.xml')

cats = cat_cascade.detectMultiScale(img_gray, 1.3, 5)

print(cats)

for (x, y, width, height) in cats:
    cv2.rectangle(img_rgb, (x, y), (x + height, y + width), (0, 255, 0), 5)

plt.subplot(1, 1, 1)
plt.title("Cat Detection")
plt.imshow(img_rgb)
plt.show()



