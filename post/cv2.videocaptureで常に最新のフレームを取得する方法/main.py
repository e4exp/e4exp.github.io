import os
import time

import cv2


def main(dir_save: str):

    os.makedirs(dir_save, exist_ok=True)

    # setup
    cap = cv2.VideoCapture(0)
    print(cap.get(cv2.CAP_PROP_FPS))

    cnt = 0
    while True:
        try:
            ret, frame = cap.read()
            if ret:
                # 5秒おきにカメラ画像を保存
                time.sleep(5)
                print(cnt)
                path_save = os.path.join(dir_save, f"{str(cnt).zfill(3)}.jpg")
                cv2.imwrite(path_save, frame)

            cnt += 1
        except Exception as e:
            print(e)
            break

    cap.release()


if __name__ == "__main__":
    dir_save = "save"
    main(dir_save)
