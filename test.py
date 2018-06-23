from shutil import copyfile
import cv2
import en_stego
import de_stego

copyfile('./samples/strawberries.png', './dist/strawberries.png')
copyfile('./samples/violet.png', './dist/violet.png')

# Hide the child image inside parent
en_image = en_stego.hide('./dist/strawberries.png', './dist/violet.png')

cv2.imwrite('./dist/en.png', en_image)