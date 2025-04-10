from djitellopy import Tello
import cv2
import numpy as np
import time

# Initialize the drone
drone = Tello()
try:
  drone.connect()

  # Enable mission pad detection
  drone.enable_mission_pads()
  drone.set_mission_pad_detection_direction(2)     # Detect mission pads in all directions
  drone.streamon()
  cap = drone.get_frame_read()  

  print(f"Battery: {drone.get_battery()}%")

  print("Taking off...")
  drone.takeoff()

  # Move up slightly to ensure clear sensor reading
  drone.move_up(20)

  # Search for Mission Pad 1
  print("Searching for Mission Pad 1...")
  while True:
      pad_id = drone.get_mission_pad_id()
      if pad_id == 1:  # Mission Pad 1 detected
          print("Mission Pad 1 detected. Aligning.....")
          drone.go_xyz_speed_mid(x=0, y=0, z=70, speed = 10, mid=1)
          time.sleep(3)
          print("X position:", drone.get_mission_pad_distance_x())
          print("Y position:", drone.get_mission_pad_distance_y())
          print("Z position:", drone.get_mission_pad_distance_z())
          drone.go_xyz_speed_mid(x=0, y=0, z=50, speed = 10, mid=1)
          time.sleep(3)
          print("X position:", drone.get_mission_pad_distance_x())
          print("Y position:", drone.get_mission_pad_distance_y())
          print("Z position:", drone.get_mission_pad_distance_z())
          drone.go_xyz_speed_mid(x=0, y=0, z=70, speed = 10, mid=1)
          time.sleep(3)
          print("X position:", drone.get_mission_pad_distance_x())
          print("Y position:", drone.get_mission_pad_distance_y())
          print("Z position:", drone.get_mission_pad_distance_z())
          drone.go_xyz_speed_mid(x=0, y=0, z=50, speed = 10, mid=1)
          time.sleep(3)
          print("X position:", drone.get_mission_pad_distance_x())
          print("Y position:", drone.get_mission_pad_distance_y())
          print("Z position:", drone.get_mission_pad_distance_z())
          drone.go_xyz_speed_mid(x=0, y=0, z=70, speed = 10, mid=1)
          time.sleep(3)
          print("X position:", drone.get_mission_pad_distance_x())
          print("Y position:", drone.get_mission_pad_distance_y())
          print("Z position:", drone.get_mission_pad_distance_z())
          drone.go_xyz_speed_mid(x=0, y=0, z=50, speed = 10, mid=1)
          time.sleep(3)
          print("X position:", drone.get_mission_pad_distance_x())
          print("Y position:", drone.get_mission_pad_distance_y())
          print("Z position:", drone.get_mission_pad_distance_z())
          drone.go_xyz_speed_mid(x=0, y=0, z=100, speed = 10, mid=1)
          time.sleep(3)
          break
      else:
          drone.move_forward(30)  # Move forward incrementally to search for the pad
          time.sleep(1)
  print("Aligning with Mission Pad 1 and landing...")

  drone.go_xyz_speed_mid(x=0, y=0, z=0, speed=10, mid=1)

  print("Searching for Mission Pad 1...")
  while True:
    pad_id = drone.get_mission_pad_id()
    if pad_id == 2:  # Mission Pad 1 detected
        target_height = 56
        current_height = drone.get_distance_tof()
        if current_height - target_height >= 5:  # Avoid drastic adjustments
            drone.move_down(current_height-target_height)
        elif target_height - current_height >= 5:
            drone.move_up(target_height-current_height)
            time.sleep(3)
            break
    else:
        drone.move_forward(30)  # Move forward incrementally to search for the pad
        time.sleep(1)

    
    
  drone.land()

except Exception as e:
    print(f"An error occurred: {e}")
    drone.land()


finally:
    # Step 9: Disable mission pad detection and disconnect
    drone.disable_mission_pads()
    drone.end()