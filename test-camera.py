from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.capture('test-image.jpg')
