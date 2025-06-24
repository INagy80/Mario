import os
import threading

from game_files.Core import Core
from body_tracking_task import custom_input_thread


def run_game():
    # Set the working directory to the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # create event for stopping the custom input thread
    stop_event = threading.Event()
    # Create a Thread object
    input_thread = threading.Thread(target=custom_input_thread, args=(stop_event,))

    # init the game
    oCore = Core()
    # Start the custom input thread
    input_thread.start()
    # start the main game loop
    oCore.main_loop(stop_event)

    # Wait for the custom input thread to complete
    input_thread.join()

    print("All threads finished. Shutting down.")
