import os, sys
this_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(os.path.dirname(this_file), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import time
from televuer import TeleVuerWrapper
import logging_mp
logger_mp = logging_mp.get_logger(__name__, level=logging_mp.INFO)


def run_test_tv_wrapper():
    # xr-mode
    use_hand_track=False
    tv_wrapper = TeleVuerWrapper(use_hand_tracking=use_hand_track, pass_through=False,
                                 binocular=True, img_shape=(480, 1280),
                                #  webrtc=True, webrtc_url="https://192.168.123.164:60001/offer"
                                )
    try:
        input("Press Enter to start tv_wrapper test...")
        running = True
        while running:
            start_time = time.time()
            logger_mp.info("---- TV Wrapper TeleData ----")
            teleData = tv_wrapper.get_tele_data()

            # import cv2
            # img = cv2.videoCapture(0).read()[1]
            # tv_wrapper.render_to_xr(img)

            logger_mp.info("-------------------=== TeleData Snapshot ===-------------------")
            logger_mp.info(f"[Head Pose]:\n{teleData.head_pose}")
            logger_mp.info(f"[Left Wrist Pose]:\n{teleData.left_wrist_pose}")
            logger_mp.info(f"[Right Wrist Pose]:\n{teleData.right_wrist_pose}")

            if use_hand_track:
                logger_mp.info(f"[Left Hand Positions] shape {teleData.left_hand_pos.shape}:\n{teleData.left_hand_pos}")
                logger_mp.info(f"[Right Hand Positions] shape {teleData.right_hand_pos.shape}:\n{teleData.right_hand_pos}")

                if teleData.left_hand_rot is not None:
                    logger_mp.info(f"[Left Hand Rotations] shape {teleData.left_hand_rot.shape}:\n{teleData.left_hand_rot}")
                if teleData.right_hand_rot is not None:
                    logger_mp.info(f"[Right Hand Rotations] shape {teleData.right_hand_rot.shape}:\n{teleData.right_hand_rot}")

                logger_mp.info(f"[Left Pinch Value]: {teleData.left_hand_pinchValue:.2f}")
                logger_mp.info(f"[Left Squeeze Value]: {teleData.left_hand_squeezeValue:.2f}")
                logger_mp.info(f"[Right Pinch Value]: {teleData.right_hand_pinchValue:.2f}")
                logger_mp.info(f"[Right Squeeze Value]: {teleData.right_hand_squeezeValue:.2f}")

            else:
                logger_mp.info(f"[Left Trigger Value]: {teleData.left_ctrl_triggerValue:.2f}")
                logger_mp.info(f"[Left Squeeze Value]: {teleData.left_ctrl_squeezeValue:.2f}")
                logger_mp.info(f"[Left Thumbstick Value]: {teleData.left_ctrl_thumbstickValue}")
                logger_mp.info(f"[Left A/B Buttons]: A={teleData.left_ctrl_aButton}, B={teleData.left_ctrl_bButton}")

                logger_mp.info(f"[Right Trigger Value]: {teleData.right_ctrl_triggerValue:.2f}")
                logger_mp.info(f"[Right Squeeze Value]: {teleData.right_ctrl_squeezeValue:.2f}")
                logger_mp.info(f"[Right Thumbstick Value]: {teleData.right_ctrl_thumbstickValue}")
                logger_mp.info(f"[Right A/B Buttons]: A={teleData.right_ctrl_aButton}, B={teleData.right_ctrl_bButton}")


            current_time = time.time()
            time_elapsed = current_time - start_time
            sleep_time = max(0, 0.16 - time_elapsed)
            time.sleep(sleep_time)
            logger_mp.debug(f"main process sleep: {sleep_time}")

    except KeyboardInterrupt:
        running = False
        logger_mp.warning("KeyboardInterrupt, exiting program...")
    finally:
        tv_wrapper.close()
        logger_mp.warning("Finally, exiting program...")
        exit(0)

if __name__ == '__main__':
    run_test_tv_wrapper()