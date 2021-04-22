import cv2

def sepia_filter(filename):
    sepiamatrix = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    image = cv2.imread(filename)

    (b, g, r) = cv2.split(image)

    r_new = r * sepiamatrix[0][0] + g * sepiamatrix[0][1] + b * sepiamatrix[0][2]
    g_new = r * sepiamatrix[1][0] + g * sepiamatrix[1][1] + b * sepiamatrix[1][2]
    b_new = r * sepiamatrix[2][0] + g * sepiamatrix[2][1] + b * sepiamatrix[2][2]

    img_new = cv2.merge((b_new, g_new, r_new))

    cv2.imwrite("rain_sepia.jpeg", img_new)


sepia_filter("rain.jpg")
