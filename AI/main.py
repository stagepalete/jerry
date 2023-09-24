import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import cv2
import mediapipe as mp
import pyautogui
from threading import Thread
class handTracker():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, modelComplexity=1, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def handsFinder(self, image, draw=False):
            imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.results = self.hands.process(imageRGB)

            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    if draw:
                        self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
            return image

    def positionFinder(self, image, handNo=0, draw=True):
            lmlist = []
            if self.results.multi_hand_landmarks:
                Hand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(Hand.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(image, (lmlist[8][1], lmlist[8][2]), 15, (255, 0, 255), cv2.FILLED)

            return lmlist
def getIndex(lmlist):
    fingerPosition = None
    if len(lmlist) > 8:
        x, y = lmlist[8][1], lmlist[8][2]
        fingerPosition = (x, y)
    return fingerPosition

def track_hand(tracker):
    cap = cv2.VideoCapture(0)  # Используйте камеру с индексом 0

    # Получите размеры экрана
    screen_width, screen_height = pyautogui.size()

    # Создайте окно OpenCV и установите его размеры на весь экран
    cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        success, image = cap.read()
        if not success:
            break  # Выход из цикла при ошибке чтения кадра
        image = cv2.flip(image, 1)
        image = tracker.handsFinder(image)
        lmList = tracker.positionFinder(image)
        fingerPosition = getIndex(lmList)

        if fingerPosition:
            currentX, currentY = pyautogui.position()

            newX = currentX + (fingerPosition[0] - currentX) // 10
            newY = currentY + (fingerPosition[1] - currentY) // 10

            # Установите координаты мыши без задержки
            pyautogui.moveTo(newX, newY, duration=0)

        cv2.imshow("Video", image)

        # Удалите или закомментируйте следующую строку, чтобы не ждать клавишу нажатия
        cv2.waitKey(1)

def main():
    tracker = handTracker()
    thread = Thread(target=track_hand, args=(tracker,))
    thread.start()

    thread.join()  # Ждем завершения потока

if __name__ == '__main__':
    main()