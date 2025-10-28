import os, sys
this_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(os.path.dirname(this_file), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import time
from televuer import TeleVuer
import logging_mp
logger_mp = logging_mp.get_logger(__name__, level=logging_mp.INFO)

def run_test_TeleVuer():
    # xr-mode
    use_hand_track = True
    tv = TeleVuer(use_hand_tracking = use_hand_track, pass_through=True)

    try:
        input("Press Enter to start TeleVuer test...")
        running = True
        while running:
            start_time = time.time()
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
                logger_mp.info(f"left_hand_pinch: {tv.left_hand_pinch}")
                logger_mp.info(f"left_hand_pinchValue: {tv.left_hand_pinchValue}")
                logger_mp.info(f"left_hand_squeeze: {tv.left_hand_squeeze}")
                logger_mp.info(f"left_hand_squeezeValue: {tv.left_hand_squeezeValue}")
                logger_mp.info(f"right_hand_pinch: {tv.right_hand_pinch}")
                logger_mp.info(f"right_hand_pinchValue: {tv.right_hand_pinchValue}")
                logger_mp.info(f"right_hand_squeeze: {tv.right_hand_squeeze}")
                logger_mp.info(f"right_hand_squeezeValue: {tv.right_hand_squeezeValue}")
            else:
                logger_mp.info("Controller Data:")
                logger_mp.info(f"left_ctrl_trigger: {tv.left_ctrl_trigger}")
                logger_mp.info(f"left_ctrl_triggerValue: {tv.left_ctrl_triggerValue}")
                logger_mp.info(f"left_ctrl_squeeze: {tv.left_ctrl_squeeze}")
                logger_mp.info(f"left_ctrl_squeezeValue: {tv.left_ctrl_squeezeValue}")
                logger_mp.info(f"left_ctrl_thumbstick: {tv.left_ctrl_thumbstick}")
                logger_mp.info(f"left_ctrl_thumbstickValue: {tv.left_ctrl_thumbstickValue}")
                logger_mp.info(f"left_ctrl_aButton: {tv.left_ctrl_aButton}")
                logger_mp.info(f"left_ctrl_bButton: {tv.left_ctrl_bButton}")
                logger_mp.info(f"right_ctrl_trigger: {tv.right_ctrl_trigger}")
                logger_mp.info(f"right_ctrl_triggerValue: {tv.right_ctrl_triggerValue}")
                logger_mp.info(f"right_ctrl_squeeze: {tv.right_ctrl_squeeze}")
                logger_mp.info(f"right_ctrl_squeezeValue: {tv.right_ctrl_squeezeValue}")
                logger_mp.info(f"right_ctrl_thumbstick: {tv.right_ctrl_thumbstick}")
                logger_mp.info(f"right_ctrl_thumbstickValue: {tv.right_ctrl_thumbstickValue}")
                logger_mp.info(f"right_ctrl_aButton: {tv.right_ctrl_aButton}")
                logger_mp.info(f"right_ctrl_bButton: {tv.right_ctrl_bButton}")
            logger_mp.info("=" * 80)

            current_time = time.time()
            time_elapsed = current_time - start_time
            sleep_time = max(0, 0.3 - time_elapsed)
            time.sleep(sleep_time)
            logger_mp.debug(f"main process sleep: {sleep_time}")
    except KeyboardInterrupt:
        running = False
        logger_mp.warning("KeyboardInterrupt, exiting program...")
    finally:
        tv.close()
        logger_mp.warning("Finally, exiting program...")
        exit(0)

if __name__ == '__main__':
    run_test_TeleVuer()