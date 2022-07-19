import os

import cv2

#this function is not in use yet
def clahe_queue(files):

    filesFound = [files]
    os.chdir(os.path.dirname(files))
    print('Applying CLAHE, this might take awhile...')

    for i in filesFound:
        currentVideo = os.path.basename(i)
        saveName = str('CLAHE_') + str(currentVideo[:-4]) + str('.avi')
        cap = cv2.VideoCapture(currentVideo)
        imageWidth = int(cap.get(3))
        imageHeight = int(cap.get(4))
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        out = cv2.VideoWriter(saveName, fourcc, fps,
                              (imageWidth, imageHeight), 0)
        while True:
            ret, image = cap.read()
            if ret == True:
                im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                claheFilter = cv2.createCLAHE(
                    clipLimit=2, tileGridSize=(16, 16))
                claheCorrecttedFrame = claheFilter.apply(im)
                out.write(claheCorrecttedFrame)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                print(str('Completed video ') + str(saveName))
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return saveName

