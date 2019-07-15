# Generic_ur5_controller
## Description:

simple general purpose ur5 controller


 ## Connection Setup:

-copy contents of ur5_client to a memory stick and save program to ur5

-self.host: host pc ip address, this is the address of the socket connection (windows use ipconfig in cmd), the address in the kg_client.urp program must match this

-port:  socket port for the robot, use 30000 or >=30010 (29999 reserved for dashboard, 30001-30004 reserved for data exchange) set in kg_client.urp (different for every robot sharing a host)

-ee_port: e.g. 'COM20' of any connected end effectors

-db_host: socket address for robot, e.g. '192.168.1.10', set to enable dashboard, set in robot network settings:  
--in static address, set ip to 192.168.1.xx where the first 3 numbers match the self.host address and the last number differs, 
--set mask to 255.255.255.0
--apply


## Troubleshooting:

-have done everything above, and robot still not connecting - turn off wifi and/or disable other network connections
    

## Getting Started:
-main loop in \Generic_ur5_controller\Generic_ur5_controller.py, contains examples of using kg_robot and teach mode

-create specialised robot fns and attach in same format as teach_mode.py by adding an init to kg_robot.py

-use waypoint.py for global robot poses, joints and tool centre points (tcp)
