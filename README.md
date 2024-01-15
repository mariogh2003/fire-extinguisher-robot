# Fire-extinguishing-robot
The robot navigates a 4x4 grid featuring green square markers that denote various buildings potentially requiring delivery of fire suppression. These building markers are connected by sets of red and blue lines, indicating the lateral and longitudinal streets that the robot must traverse to reach its destinations. 

# Problem description
• The map representing the city is a 122cm x 122cm elevated platform.\n
• The distance separating building markers measures 30cm.
• Streets are delineated by 1.9cm thick lines, with longitudinal streets marked in red and lateral streets marked in blue.
• Building markers are identified by 6.4 cm x 6.4 cm green squares situated at street intersections.
• The Fire Extinguishing Robot's journey commences at the fire station, located at position (0,0).
• A robot may go through buildings if they are not on fire or if there are no fire suppressants blocking its way.
• The fire suppressants will always be colored cubes of fixed size (2.54cm^3). There are six possible colors.
• Items can only be loaded onto the Fire Extinguishing Robot at the fire station.
• An external operator will provide cubes to your robot.
• All six cubes (one of each color) will be loaded onto the Fire Extinguishing Robot at the initial loading time.
• Each firefighting run will consist of delivering fire suppressants to extinguish 3 different fires, at 3 different locations.
• Every fire can only be extinguished with its corresponding fire suppressant.
• Deliveries of fire suppressant within a 10cm radius of the center of the building marker.
• The location of the fires and the type of fires should be entered as a user input at the beginning of the program (e.g. Input coordinates: 1,2,A,3,3,B,0,1,E)
