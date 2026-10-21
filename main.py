import cv2
from src.grid import get_grid_points, draw_grid, draw_colors
from src.color_detector import detect_face

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    points = get_grid_points(frame)
    colors = detect_face(frame, points)

    frame = draw_grid(frame, points)
    frame = draw_colors(frame, points, colors)

    cv2.imshow("Rubik's Cube Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()