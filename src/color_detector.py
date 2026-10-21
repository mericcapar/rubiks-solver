import cv2
import numpy as np

def get_average_color(frame, x, y, size=10):
    region = frame[y - size : y + size, x - size : x + size]
    return region.mean(axis=(0, 1))


def classify_color(bgr):
    pixel = np.uint8([[bgr]])
    hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
    h, s, v = int(hsv[0]), int(hsv[1]), int(hsv[2])

    if s < 60 and v > 120:
        return "white"
    if h < 8 or h > 165:
        return "red"
    if h < 22:
        return "orange"
    if h < 38:
        return "yellow"
    if h < 85:
        return "green"
    if h < 135:
        return "blue"
    return "red"


def detect_face(frame, points):
    colors = []
    for (x, y) in points:
        bgr = get_average_color(frame, x, y)
        colors.append(classify_color(bgr))
    return colors