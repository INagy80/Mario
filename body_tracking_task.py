import cv2
import mediapipe as mp
from custom_input_task import custom_input_loop
from game_files.Anonymization import displayAnonymization

showBodyMarkers = False  # Marker anzeigen
showAnonymization = True  # Gesicht unkenntlich machen

mp_pose = None
pose = None
mp_drawing = None
playerFrame = None


def custom_input_thread(stop_event):
    global pose, mp_pose, mp_drawing
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)  # Spiegeln für natürliches Feedback
        processed_frame, markerList = getMarkerListAndShowMarkers(frame, showBodyMarkers)

        if markerList:
            custom_input_loop(markerList)

        displayWebcam(processed_frame, markerList)

    cap.release()
    cv2.destroyAllWindows()


def getMarkerListAndShowMarkers(frame, showBodyMarkers):
    global pose, mp_drawing, mp_pose

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        if showBodyMarkers:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )
        return frame, results.pose_landmarks
    else:
        return frame, None


def displayWebcam(frame, markerList):
    if showAnonymization:
        frame = displayAnonymization(frame, markerList)
    mirrored_frame = cv2.flip(frame, 1)
    mirrored_frame = cv2.resize(mirrored_frame, (280, 213))
    mirrored_frame = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2RGB)
    global playerFrame
    playerFrame = mirrored_frame


def getPlayerFrame():
    return playerFrame
