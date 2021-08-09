import cv2
import time

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter("OUTPUT.avi",fourcc,30.0,(480, 640))
width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)
print(f'프레임 너비: {width}, 프레임 높이 : {height}, 초당 프레임 수 : {fps}')

prev_time = 0
while True:
    ret, frame = cap.read()
    prev_time = time.time()
    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):# 총 프레임 수
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    if ret == False:
        continue
    cv2.imshow('video', frame)
    writer.write(frame)
    if cv2.waitKey(1)&0xFF == 27:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()