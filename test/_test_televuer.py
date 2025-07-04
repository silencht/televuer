import os, sys
this_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(os.path.dirname(this_file), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import time
import numpy as np
from multiprocessing import shared_memory
from televuer import TeleVuer
import logging_mp
logger_mp = logging_mp.get_logger(__name__, level=logging_mp.INFO)

def run_test_TeleVuer():
    # image
    image_shape = (480, 640 * 2, 3)
    image_shm = shared_memory.SharedMemory(create=True, size=np.prod(image_shape) * np.uint8().itemsize)
    image_array = np.ndarray(image_shape, dtype=np.uint8, buffer=image_shm.buf)

    # from image_server.image_client import ImageClient
    # import threading
    # image_client = ImageClient(tv_img_shape = image_shape, tv_img_shm_name = image_shm.name, image_show=True, server_address="127.0.0.1")
    # image_receive_thread = threading.Thread(target = image_client.receive_process, daemon = True)
    # image_receive_thread.daemon = True
    # image_receive_thread.start()

    # xr-mode
    use_hand_track = True
    tv = TeleVuer(binocular = True, use_hand_tracking = use_hand_track, img_shape = image_shape, img_shm_name = image_shm.name, webrtc=False)

    try:
        input("Press Enter to start TeleVuer test...")
        running = True
        while running:
            logger_mp.info("=" * 80)
            logger_mp.info("Common Data (always available):")
            logger_mp.info(f"head_pose shape: {tv.head_pose.shape}\n{tv.head_pose}\n")
            logger_mp.info(f"left_arm_pose shape: {tv.left_arm_pose.shape}\n{tv.left_arm_pose}\n")
            logger_mp.info(f"right_arm_pose shape: {tv.right_arm_pose.shape}\n{tv.right_arm_pose}\n")
            logger_mp.info("=" * 80)

            if use_hand_track:
                logger_mp.info("Hand Tracking Data:")
                logger_mp.info(f"left_hand_positions shape: {tv.left_hand_positions.shape}\n{tv.left_hand_positions}\n")
                logger_mp.info(f"right_hand_positions shape: {tv.right_hand_positions.shape}\n{tv.right_hand_positions}\n")
                logger_mp.info(f"left_hand_orientations shape: {tv.left_hand_orientations.shape}\n{tv.left_hand_orientations}\n")
                logger_mp.info(f"right_hand_orientations shape: {tv.right_hand_orientations.shape}\n{tv.right_hand_orientations}\n")
                logger_mp.info(f"left_hand_pinch_state: {tv.left_hand_pinch_state}")
                logger_mp.info(f"left_hand_pinch_value: {tv.left_hand_pinch_value}")
                logger_mp.info(f"left_hand_squeeze_state: {tv.left_hand_squeeze_state}")
                logger_mp.info(f"left_hand_squeeze_value: {tv.left_hand_squeeze_value}")
                logger_mp.info(f"right_hand_pinch_state: {tv.right_hand_pinch_state}")
                logger_mp.info(f"right_hand_pinch_value: {tv.right_hand_pinch_value}")
                logger_mp.info(f"right_hand_squeeze_state: {tv.right_hand_squeeze_state}")
                logger_mp.info(f"right_hand_squeeze_value: {tv.right_hand_squeeze_value}")
            else:
                logger_mp.info("Controller Data:")
                logger_mp.info(f"left_controller_trigger_state: {tv.left_controller_trigger_state}")
                logger_mp.info(f"left_controller_trigger_value: {tv.left_controller_trigger_value}")
                logger_mp.info(f"left_controller_squeeze_state: {tv.left_controller_squeeze_state}")
                logger_mp.info(f"left_controller_squeeze_value: {tv.left_controller_squeeze_value}")
                logger_mp.info(f"left_controller_thumbstick_state: {tv.left_controller_thumbstick_state}")
                logger_mp.info(f"left_controller_thumbstick_value: {tv.left_controller_thumbstick_value}")
                logger_mp.info(f"left_controller_aButton: {tv.left_controller_aButton}")
                logger_mp.info(f"left_controller_bButton: {tv.left_controller_bButton}")
                logger_mp.info(f"right_controller_trigger_state: {tv.right_controller_trigger_state}")
                logger_mp.info(f"right_controller_trigger_value: {tv.right_controller_trigger_value}")
                logger_mp.info(f"right_controller_squeeze_state: {tv.right_controller_squeeze_state}")
                logger_mp.info(f"right_controller_squeeze_value: {tv.right_controller_squeeze_value}")
                logger_mp.info(f"right_controller_thumbstick_state: {tv.right_controller_thumbstick_state}")
                logger_mp.info(f"right_controller_thumbstick_value: {tv.right_controller_thumbstick_value}")
                logger_mp.info(f"right_controller_aButton: {tv.right_controller_aButton}")
                logger_mp.info(f"right_controller_bButton: {tv.right_controller_bButton}")
            logger_mp.info("=" * 80)
            time.sleep(0.03)
    except KeyboardInterrupt:
        running = False
        logger_mp.warning("KeyboardInterrupt, exiting program...")
    finally:
        image_shm.unlink()
        image_shm.close()
        logger_mp.warning("Finally, exiting program...")
        exit(0)

if __name__ == '__main__':
    run_test_TeleVuer()