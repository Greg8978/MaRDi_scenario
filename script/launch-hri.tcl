
proc launch_spark { } {
    lm spark
    spark::LoadP3d /home/ferreira/openrobots/share/move3d/assets/ADREAM/ADREAM_APPART.p3d 1 0
    spark::ReadHumans -ack USE_CONF 0 Human.armature
    spark::ReadRobot -ack pr2JointState pr2JointMap ergerg rthrh rthr pr2Pose pr2JointState pr2JointMap    
    spark::ReadObjects -ack USE_VIMAN 0 morseViman USE_MOCAP 0 kikou
    spark::SetInterfaceAgentParams HERAKLES_HUMAN1 GEN_TRUE GEN_TRUE GEN_FALSE
    spark::UpdateInterface -ack
    spark::ComputeFacts -ack
    spark::SetKBAddress localhost 6969
}

proc launch_spark_readniut { } {
    lm spark
    spark::LoadP3d /home/ferreira/openrobots/share/move3d/assets/ADREAM/ADREAM_APPART.p3d 1 0
    spark::ReadHumans -ack USE_NIUT 0 Human.armature
    spark::ReadRobot -ack pr2JointState pr2JointMap ergerg rthrh rthr pr2Pose pr2JointState pr2JointMap    
    spark::ReadObjects -ack USE_VIMAN 0 morseViman USE_MOCAP 0 kikou
    spark::SetInterfaceAgentParams HERAKLES_HUMAN1 GEN_TRUE GEN_TRUE GEN_FALSE
    spark::UpdateInterface -ack
    spark::ComputeFacts -ack
    spark::SetKBAddress kb_host kb_port
}

proc launch_niut { } {
    lm niut
    niut::Init 1310260002
}
