import cv2
import numpy as np

#캠으로부터 데이터를 가져오기 
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print('카메라로부터 정보를 얻을 수 없습니다.')

else:
    # 프레임의 정보를 가져와 보기! 
    # 화면크기를 말하는것! (width,height)
    frame_width = int(cap.get(3))
    frame_heigth = int(cap.get(4))

    print(frame_width,frame_heigth)
    out = cv2.VideoWriter('data/video/output.avi',
                    cv2.VideoWriter_fourcc('M','J','P','G'),
                    10,
                    (frame_width,frame_heigth))
    # 캠으로부터 사진을 계속 입력 받아서 , 화면에도 표시하고
    # 위의 out 에 저장 해주면 된다.
    while True:
        ret,frame = cap.read()
        if ret == True:
            # 화면에도 표시하고
            cv2.imshow('video',frame)
            # 파일에도 저장한다.
            out.write(frame)

            # 유저가 esc 누르며, 촬영 종료
            if cv2.waitKey(1) & 0xff == 27 :
                break
        else :
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()