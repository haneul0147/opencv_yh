import cv2
import numpy as np

# FPS : Frame per Second , 1초당의 몇장의 사진으로
#구성되어있나?

# 비디오 파일 일기 
cap = cv2.VideoCapture('data/videos/chaplin.mp4')

if cap.isOpened() == False:
    print('비디어 파일 여는데 실패했습니다.')
else:
    # 반복문으로 구성한다. 왜냐하면, 동영상은 여러개의 사진으로
    # 되어있기 때문에, 동영상 시작부터 끝까지
    # imshow 를 반복해서 화면에 출력해주면,
    # 이것이 바로 동영상 플레이다.
    while cap.isOpened():
        # 사진 1장찍 사가져와서 
        # frame == 사진
        ret, frame =cap.read()
        
        # 제대로 된 사진이면, 화면에 표시하라고 코딩!
        if ret == True :
            cv2.imshow('Video',frame)
            #동영상이 플레이 하는 동안,멈추고 싶을때눈
            # esc 키를 눌러서 멈추도록 코딩!
            if cv2.waitKey(25) & 0xff == 27:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
