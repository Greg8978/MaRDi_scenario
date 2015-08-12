#! /usr/bin/env tclsh


package require genom

set usedEndEffector pr2Gripper
set ROBNAME [regsub {c[0-9]} [exec hostname] ""]   

proc initmocap { } {
  connect
  lm spark
  spark::LoadP3d  /home/gmilliez/openrobots/share/move3d/assets/experiments/eu_demos_november2012/mardi.p3d 1 0
  spark::ReadHumans  -ack USE_MOCAP 0 optitrack/bodies/Rigid_Body_1 
  ::spark::UpdateInterface -ack
}

proc initmorse { } {
  connect
  lm spark
  spark::LoadP3d  /home/gmilliez/openrobots/share/move3d/assets/experiments/eu_demos_november2012/mardi.p3d 1 0
  spark::ReadHumans  -ack USE_CONF 0 Human.armature
  spark::ReadRobot -ack lwrCurrentPoseArmRight sahandPosterHand pomPos pomPlatineFramePos sparkyarpRobotConfig pr2Pose pr2JointState pr2JointMap
  spark::ReadObjects -ack USE_VIMAN 0 morseViman USE_VIMAN 0 morseViman
  ::spark::UpdateInterface -ack
  spark::ComputeFacts -ack
}


proc launch { } {
    spark::UpdateAllSituationAssessment SPARK_STOP_SEND_LOOK_DIRECTION_ORO_FACTS 7 0.8

    spark::SetInterfaceParams  640 480 GEN_FALSE GEN_TRUE GEN_TRUE GEN_FALSE GEN_FALSE GEN_FALSE
    spark::ComputeFacts -ack

    spark::TestSphereMonitor -ack

    spark::ChangeCameraPos  4.1 7.2 1 3 -0.7 0.7

    ::spark::UpdateAllSituationAssessment SPARK_SWITCH_DRAW_ACTION_MONITORING_SPHERES 7 0.3

    spark::UpdateVisuInfo  GEN_FALSE 1 -1 2.95 2.81 2.0 0.0 0.0 0.0 50 0 0 1 0.1 0.0 0.0 1 0 SPARK_VISU_INFO_SPHERE -1 SPARK_VISU_INFO_PARAM_REACH_ZOFFSET 1 0.8
}

proc createsphere { } {
    spark::ChangeCameraPos  6 3 -1 7 0.0 0.7
    spark::PlaceObject  LOTR_TAPE 5 4 1 0.0 0.0 0.0
    spark::UpdateSphereMonitor  0 GEN_TRUE LOTR_TAPE 0 HERAKLES_HUMAN1 5 4 1 1 10 1 0.5 SPARK_PICK_OBJECT
}
