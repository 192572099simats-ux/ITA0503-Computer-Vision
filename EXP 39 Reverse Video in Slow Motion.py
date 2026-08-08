import cv2
def reverse_slow_motion(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
   cap.release()
   for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
video_path = input("Enter video path: ")
reverse_slow_motion(video_path)
