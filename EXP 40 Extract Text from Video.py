import cv2
import pytesseract
def extract_text(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
          if not ret:
            break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
   if text.strip():
            print("Text:", text.strip())
            cv2.imshow("Video", frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  cap.release()
    cv2.destroyAllWindows()
video_path = input("Enter video path: ")
extract_text(video_path)
