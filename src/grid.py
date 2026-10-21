import cv2

def get_grid_points(frame, square_size=60):
    h,w = frame.shape[:2]
    center_x = w //2
    center_y = h //2
    
    points = []
    for row in range(3):
        for col in range(3):
            x = center_x + (col-1) * square_size
            y = center_y + (row-1) * square_size
            points.append((x,y))

    return points

def draw_grid(frame,points, square_size=60):
    half = square_size //2

    for (x,y) in points:
        cv2.rectangle(frame, (x-half, y-half) , (x+half, y+half) , (255,255,255),2)

    return frame
