import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/olympusforge/ros2_frost/install/nav2_loopback_sim'
