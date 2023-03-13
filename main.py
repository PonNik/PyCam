# importing required libraries 
import cv2 
import time 
import os
import webCam as wc

webcam_stream = wc.WebcamStream(stream_id=0) #  stream_id = 0 is for primary camera 
webcam_stream.start()

# processing frames in input stream
num_frames_processed = 0 

frame_rate = 1./30
prev = 0

dirs = str(time.time())
os.makedirs(dirs)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f'{dirs}/cam_world.mp4', fourcc, 30.0, (640, 480))
file = open(f'{dirs}/time.csv', 'w')

start = time.time()
while True :
    #print(f"start: {time.time()}")
    if webcam_stream.stopped is True :
        break
    else :
        frame = webcam_stream.read()
    #print(f"end  : {time.time()}")

    t = time.time()
    
    if prev <= t:
        out.write(frame)
        num_frames_processed += 1
        prev = t + frame_rate
        cv2.imshow('record' , frame)
        file.write(f"frame {num_frames_processed}; {t - start}\n")
        if cv2.waitKey(1) == ord('q'):
            webcam_stream.stop()
    
end = time.time()
webcam_stream.stop() # stop the webcam stream

# printing time elapsed and fps
elapsed = end-start
fps = num_frames_processed/elapsed 
print("FPS: {} , Elapsed Time: {} , Frames Processed: {}".format(fps, elapsed, num_frames_processed))

# closing all windows 
out.release()
cv2.destroyAllWindows()