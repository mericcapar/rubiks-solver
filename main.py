import cv2
from src.grid import get_grid_points, draw_grid

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if not ret:
        break

    points = get_grid_points(frame)
    frame = draw_grid(frame,points)

    cv2.imshow('Rubrik Cube Scanner', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()