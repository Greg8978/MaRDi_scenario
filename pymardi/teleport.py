""" Simple script for the CAT AND MOUSE game tutorial

This will command the CAT, using two semantic cameras, to follow
after the MOUSE robot """

import time
import math

from pymorse import Morse

sleeptime = 2

def go_near(furniture_name, robot_teleport):
    """ Get the furniture near which we want 
    the robot to go and move the robot accordingly """
    if furniture_name == "livingroom_coffeetable":
      print("Request to put robot at livingroom_coffeetable.")
      x_y_z_yaw_pitch_roll = {"x": 4.5, "y": 7.3, "z": 0, "yaw": 3.8, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "bedroom_chest":
      print("Request to put robot at bedroom_chest.")
      x_y_z_yaw_pitch_roll = {"x": 5, "y": 11.3, "z": 0, "yaw": 0.0, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "bedroom_console":
      print("Request to put robot at bedroom_console.")
      x_y_z_yaw_pitch_roll = {"x": 4.2, "y": 12.2, "z": 0, "yaw": math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "bedroom_bedsidetable":
      print("Request to put robot at bedroom_bedsidetable.")
      x_y_z_yaw_pitch_roll = {"x": 3.1, "y": 12.1, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "bedroom_shelf":
      print("Request to put robot at bedroom_shelf.")
      x_y_z_yaw_pitch_roll = {"x": 2.4, "y": 9.8, "z": 0, "yaw": 3*math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "kitchen_cupboard":
      print("Request to put robot at kitchen_cupboard.")
      x_y_z_yaw_pitch_roll = {"x": 6.7, "y": 10.6, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "kitchen_table":
      print("Request to put robot at kitchen_table")
      x_y_z_yaw_pitch_roll = {"x": 7.8, "y": 10.2, "z": 0, "yaw": math.pi/8, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "livingroom_table":
      print("Request to put robot at livingroom_table")
      x_y_z_yaw_pitch_roll = {"x": 7.4, "y": 7.6, "z": 0, "yaw": 3*math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    else:
      print("Unknown furniture: " + furniture_name)

def explore(furniture_name, robot_teleport):
    """ Explore near the furniture """
    if furniture_name == "livingroom_coffeetable":
      print("Request to explore around livingroom_coffeetable.")
      x_y_z_yaw_pitch_roll = {"x": 6.8, "y": 7.3, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      #x_y_z_yaw_pitch_roll = {"x": 4.5, "y": 7.3, "z": 0, "yaw": 3.8 + math.pi, "pitch": 0, "roll": 0}
      #robot_teleport.publish(x_y_z_yaw_pitch_roll)
      #time.sleep(sleeptime)
      #x_y_z_yaw_pitch_roll = {"x": 4.5, "y": 7.3, "z": 0, "yaw": 3.8 + 3*math.pi/2, "pitch": 0, "roll": 0}
      #robot_teleport.publish(x_y_z_yaw_pitch_roll)
      #time.sleep(sleeptime)
      #x_y_z_yaw_pitch_roll = {"x": 4.5, "y": 7.3, "z": 0, "yaw": 3.8, "pitch": 0, "roll": 0}
      #robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "bedroom_chest":
      print("Request to explore around bedroom_chest.")
      x_y_z_yaw_pitch_roll = {"x": 5, "y": 11.3, "z": 0, "yaw": math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 5, "y": 11.3, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 5, "y": 11.3, "z": 0, "yaw": 3*math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 5, "y": 11.3, "z": 0, "yaw": 0.0, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "bedroom_console":
      print("Request to explore around bedroom_console.")
      x_y_z_yaw_pitch_roll = {"x": 4.2, "y": 12.2, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 4.2, "y": 12.2, "z": 0, "yaw": 3*math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 4.2, "y": 12.2, "z": 0, "yaw": 0.0, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 4.2, "y": 12.2, "z": 0, "yaw": math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "bedroom_bedsidetable":
      print("Request to explore around bedroom_bedsidetable.")
      x_y_z_yaw_pitch_roll = {"x": 3.1, "y": 12.1, "z": 0, "yaw": 3*math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 3.1, "y": 12.1, "z": 0, "yaw": 0.0, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 3.1, "y": 12.1, "z": 0, "yaw": math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 3.1, "y": 12.1, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "bedroom_shelf":
      print("Request to explore around bedroom_shelf.")
      x_y_z_yaw_pitch_roll = {"x": 2.4, "y": 9.8, "z": 0, "yaw": 0.0, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 2.4, "y": 9.8, "z": 0, "yaw": math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 2.4, "y": 9.8, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 2.4, "y": 9.8, "z": 0, "yaw": 3*math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "kitchen_cupboard":
      print("Request to explore around kitchen_cupboard.")
      x_y_z_yaw_pitch_roll = {"x": 6.7, "y": 10.6, "z": 0, "yaw": 3*math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 6.7, "y": 10.6, "z": 0, "yaw": 0.0, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 6.7, "y": 10.6, "z": 0, "yaw": math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 6.7, "y": 10.6, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "kitchen_table":
      print("Request to explore around kitchen_table.")
      x_y_z_yaw_pitch_roll = {"x": 7.8, "y": 10.2, "z": 0, "yaw": math.pi/8 + math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 7.8, "y": 10.2, "z": 0, "yaw": math.pi/8 + math.pi, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 7.8, "y": 10.2, "z": 0, "yaw": math.pi/8 + 3*math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      x_y_z_yaw_pitch_roll = {"x": 7.8, "y": 10.2, "z": 0, "yaw": math.pi/8, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
    elif furniture_name == "livingroom_table":
      print("Request to explore around livingroom_table.")
      x_y_z_yaw_pitch_roll = {"x": 6.8, "y": 3.0, "z": 0, "yaw": math.pi/2, "pitch": 0, "roll": 0}
      robot_teleport.publish(x_y_z_yaw_pitch_roll)
      time.sleep(sleeptime)
      #x_y_z_yaw_pitch_roll = {"x": 7.4, "y": 7.6, "z": 0, "yaw": math.pi/2, "pitch": 0, "roll": 0}
      #robot_teleport.publish(x_y_z_yaw_pitch_roll)
      #time.sleep(sleeptime)
      #x_y_z_yaw_pitch_roll = {"x": 7.4, "y": 7.6, "z": 0, "yaw": math.pi, "pitch": 0, "roll": 0}
      #robot_teleport.publish(x_y_z_yaw_pitch_roll)
      #time.sleep(sleeptime)
      #x_y_z_yaw_pitch_roll = {"x": 7.4, "y": 7.6, "z": 0, "yaw": 3*math.pi/2, "pitch": 0, "roll": 0}
      #robot_teleport.publish(x_y_z_yaw_pitch_roll)
    else:
      print("Unknown furniture: " + furniture_name)

def camera_scan(h, cam, direction):
    """ Scan environment with camera """
    if direction == "right":
      offset = -1.0
    elif direction == "left":
      offset = 1.0
    else:
      offset = 0.0


    cam.set_pan_tilt(offset * 1.3, 0.5)
    time.sleep(1)
    h.rotate("head_pan_joint", offset * 1.3)
    time.sleep(4)
    h.rotate("head_tilt_joint", 0.5)
    time.sleep(2)
    cam.set_pan_tilt(offset * 1.3, 0.3)
    time.sleep(1)
    h.rotate("head_tilt_joint", 0.3)
    cam.set_pan_tilt(offset * 1.3, 0.0)
    time.sleep(1)
    h.rotate("head_tilt_joint", 0.0)


    cam.set_pan_tilt(offset * 1.3 + 0.4, 0.5)
    time.sleep(1)
    h.rotate("head_pan_joint", offset * 1.3 + 0.4)
    time.sleep(2)
    h.rotate("head_tilt_joint", 0.5)
    time.sleep(2)
    cam.set_pan_tilt(offset * 1.3 + 0.4, 0.3)
    time.sleep(1)
    h.rotate("head_tilt_joint", 0.3)
    cam.set_pan_tilt(offset * 1.3 + 0.4, 0.0)
    time.sleep(1)
    h.rotate("head_tilt_joint", 0.0)
    
    cam.set_pan_tilt(offset * 1.3 - 0.4, 0.5)
    time.sleep(1)
    h.rotate("head_pan_joint", offset * 1.3 - 0.4)
    time.sleep(2)
    h.rotate("head_tilt_joint", 0.5)
    time.sleep(2)
    cam.set_pan_tilt(offset * 1.3 - 0.4, 0.3)
    time.sleep(1)
    h.rotate("head_tilt_joint", 0.3)
    cam.set_pan_tilt(offset * 1.3 - 0.4, 0.0)
    time.sleep(1)
    h.rotate("head_tilt_joint", 0.0)



def give(r):
    """ give object to the human """
    r.rotate("r_shoulder_pan_joint", 0.5)
    time.sleep(2)
    r.rotate("r_shoulder_lift_joint", -1.0)
    time.sleep(2)
    r.rotate("r_elbow_flex_joint", 1.8)
    time.sleep(2)


def default_pause(r, l):
    """ Standard robot position """
    r.rotate("r_shoulder_lift_joint", 1.3)
    l.rotate("l_shoulder_lift_joint", 1.3)
    time.sleep(1)
    r.rotate("r_elbow_flex_joint", -2.5)
    l.rotate("l_elbow_flex_joint", -2.5)
    time.sleep(1)


def main():
    """ Put the robot in the right place """
    with Morse() as morse:
        teleporter = morse.pr2.teleport
        pr2_head = morse.pr2.torso.head
        pr2_cam = morse.pr2.torso.head.ptu
        pr2_r_arm = morse.pr2.torso.r_arm
        pr2_l_arm = morse.pr2.torso.l_arm
        default_pause(pr2_r_arm, pr2_l_arm)
        #default_pause(pr2_r_arm, pr2_l_arm)
        camera_scan(pr2_head, pr2_cam, "left")
        camera_scan(pr2_head, pr2_cam, "right")
        go_near("livingroom_coffeetable", teleporter)
        explore("livingroom_coffeetable", teleporter)
        morse.pr2.grasp(True,"WALLEE_TAPE") 
        time.sleep(sleeptime)
        give(pr2_r_arm)
        go_near("livingroom_table", teleporter)
        go_near("bedroom_bedsidetable", teleporter)
        time.sleep(sleeptime)
        #morse.pr2.grasp(False) 
        #time.sleep(sleeptime)
        #morse.pr2.grasp(True)
        #time.sleep(sleeptime)
        #go_near("kitchen_table", teleporter)
        #explore("livingroom_table", teleporter)
        #time.sleep(sleeptime)
        #go_near("livingroom_table", teleporter)
        #time.sleep(sleeptime)
        #go_near("livingroom_table", teleporter)
        #camera_scan(pr2_head, pr2_cam, "middle")
        #morse.pr2.grasp(False)
        #go_near("kitchen_table", teleporter)
        #camera_scan(pr2_head, pr2_cam, "middle")

if __name__ == "__main__":
    main()
