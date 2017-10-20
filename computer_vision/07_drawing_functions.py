import numpy as np
import cv2


img = cv2.imread('images/saturn.png')


def draw_circle():
    """
    cv2.circle(img, center, radius, color, thickness, lineType, shift)

        params:
        img       --> Input image where circle is to be drawn
        center    --> x, y coordinate of circle center
        radius    --> circle radius in pixels
        color     --> circle line color in BGR tuple (B, G, R)
        thickness --> circle line thickness in pixels
        lineType  --> type of circle boundary (options: 8, 4, CV_AA)
        shift     --> Number of fractional bits in the coordinates of the center
                      and in the radius value.

        returns:
        None
    """
    red = (0, 0, 255)
    height, width = img.shape[:2]
    img_center = (int(width/2.), int(height/2.))
    cv2.circle(img, img_center, 20, red, 2)
    cv2.imshow('Drawn Circle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_line():
    """
    cv2.line(img, pt1, pt2, color, thickness, lineType, shift)

        params:
        img       --> Input image where circle is to be drawn
        pt1       --> first point of the line segment (x, y)
        pt2       --> second point of the line segment (x, y)
        color     --> circle line color in BGR tuple (B, G, R)
        thickness --> circle line thickness in pixels
        lineType  --> type of circle boundary (options: 8, 4, CV_AA)
        shift     --> Number of fractional bits in the coordinates of the center
                      and in the radius value.

        returns:
        None
    """
    blue = (255, 0, 0)
    height, width = img.shape[:2]
    num_lines = 5
    exs_0 = np.random.randint(width, size=num_lines)
    exs_1 = np.random.randint(width, size=num_lines)
    whys_0 = np.random.randint(height, size=num_lines)
    whys_1 = np.random.randint(height, size=num_lines)
    for i in range(len(exs_0)):
        cv2.line(img, (exs_0[i], whys_0[i]), (exs_1[i], whys_1[i]), blue, 2)

    # show image with random lines
    cv2.imshow('Original Image w/Circle + Lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

draw_circle()
draw_line()
