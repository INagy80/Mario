from game_files.custom_actions import post_action, Action

# ID-Konstanten für Hände und Kopf
LEFT_WRIST  = 15
RIGHT_WRIST = 16
NOSE        = 0

# Für Sprung-Logik
prev_nose_y    = None
jumping        = False
threshold_jump = 0.05  # y-Delta in [0–1] für “Sprung”

def custom_input_loop(markerList):
    """
    Steuert Mario:
      – Hände (Wrists) nach links/rechts
      – Kopf (Nase) zum Springen
    """
    global prev_nose_y, jumping

    if not markerList:
        return

    landmarks = markerList.landmark

    # --- LINKS/RECHTS per Hände ---
    left_x   = landmarks[LEFT_WRIST].x
    right_x  = landmarks[RIGHT_WRIST].x
    center_x = (left_x + right_x) / 2

    if center_x < 0.45:
        post_action(Action.LEFT)
        post_action(Action.RIGHT_STOP)
    elif center_x > 0.55:
        post_action(Action.RIGHT)
        post_action(Action.LEFT_STOP)
    else:
        post_action(Action.LEFT_STOP)
        post_action(Action.RIGHT_STOP)

    # --- SPRUNG per Kopfbewegung (Nase Y) ---
    nose_y = landmarks[NOSE].y
    if prev_nose_y is not None:
        delta = prev_nose_y - nose_y
        # Wenn Kopf schnell nach oben → Sprung
        if delta > threshold_jump and not jumping:
            post_action(Action.JUMP)
            jumping = True
        # Wenn Kopf wieder unten → Sprung beenden
        elif delta <= 0 and jumping:
            post_action(Action.JUMP_STOP)
            jumping = False

    prev_nose_y = nose_y
