# -*- encoding: UTF-8 -*-
import matplotlib.pyplot as plt
import sys
import numpy
import math
import time
from naoqi import ALProxy
from marvelmind import MarvelmindHedge
from time import sleep
from threading import Thread

# State-transition graph
graph = {'1': {'2': 2, '0': 2}, '2': {'3': 2, '1': 2}, '3': {'4': 2, '2': 2},'4': {'5': 2, '3': 2},
        '5': {'6': 1, '4': 2}, '6': {'7': 1, '5': 1},'7': {'8': 1, '6': 1}, '8': {'7': 1, '9': 2},
         '9': {'8': 2, '10': 2}, '10': {'9': 2, '11': 2}, '11': {'10': 2, '12': 2}, '12': {'11': 2, '13': 2},
        '13': {'12': 2, '14': 1}, '14': {'13': 1, '15': 1}, '15': {'14': 1, '0': 1},'0': {'1': 2, '15': 1}}

def dijkstra (graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
            
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    path.pop(len(path) - 1)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
        print('The number of nodes is ' + str(len(path)))

    #################################    
    # Robot moves to target student #
    #################################

    # Get the services ALMotion and ALRobotPosture
    motion = ALProxy("ALMotion", "192.168.1.166", 9559)
    posture = ALProxy("ALRobotPosture", "192.168.1.166" , 9559)
            
    # Set robot stiffness
    motion.setStiffnesses("Body", 1.0)

    # Send the robot to Stand Init
    posture.goToPosture("StandInit", 0.5)

    # Pepper speaks
    tts = ALProxy("ALTextToSpeech", "192.168.1.166", 9559)
    tts.setLanguage("Japanese")
    tts.say("これから歩きます")

    # Disable external anti-collision
    #name = "Move"    
    #enable = False
    #success = motion.setExternalCollisionProtectionEnabled(name, enable)
    #if (success):
    #    print("Collision protection disabled")
    #time.sleep(1.0)
    
    move_count = 0
    for node in path:
        move_count += 1
        print(node)
        print('move count is ' + str(move_count))

        x     = 0.8
        y     = 0.0
        theta = 0.0
        t     = 3/10
        # Robot moves from left to right anticlockwise (Pattern 1)
        if node == "4" and node[0] > node[1]:
            # Robot moves forward only 
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("四")

        elif node == "3" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("三") 
    
        elif node == "2" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("二") 
        
        elif node == "1" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("一")
        
        elif node == "0" and node[0] > node[1]:
            # Robot turns left & moves forward
            motion.moveTo(0.0, 0.0, math.pi/2)
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("ゼロ")

        elif node == "15" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十五")

        elif node == "14" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十四")

        elif node == "13" and node[0] > node[1]:
            # Robot turns left & moves forward
            motion.moveTo(0.0, 0.0, math.pi/2)
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十三")
        
        elif node == "12" and node[0] > node[1]:
            # Robot moves forward
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十二")

        elif node == "11" and node[0] > node[1]:
            # Robot moves forward
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十一")

        elif node == "10" and node[0] > node[1]:
            # Robot moves forward
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十")           

        # Robot moves from right to left anticlockwise (Pattern 2)
        if node == "9" and node[0] < node[1]:
            # Robot moves forward only 
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("九")

        elif node == "10" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十") 
    
        elif node == "11" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十一") 
        
        elif node == "12" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十二")
        
        elif node == "13" and node[0] < node[1]:
            # Robot turns right & moves forward
            motion.moveTo(0.0, 0.0, -math.pi/2)
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十三")

        elif node == "14" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十四")

        elif node == "15" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十五")

        elif node == "0" and node[0] < node[1]:
            # Robot turns right & moves forward
            motion.moveTo(0.0, 0.0, -math.pi/2)
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("ゼロ")
        
        elif node == "1" and node[0] < node[1]:
            # Robot moves forward
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("一")

        elif node == "2" and node[0] < node[1]:
            # Robot moves forward
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("二")

        elif node == "3" and node[0] < node[1]:
            # Robot moves forward
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("三")

        # Robot moves from left to right clockwise (Pattern 3)
        elif node == "1" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("一")

        elif node == "2" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("二") 
        
        elif node == "3" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("三") 
    
        elif node == "4" and node[0] < node[1]:
            # Robot moves forward only 
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("四")
        
        elif node == "5" and node[0] < node[1]:
            # Robot turns right & moves forward
            motion.moveTo(0.0, 0.0, -math.pi/2)
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("五")

        elif node == "6" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("六")

        elif node == "7" and node[0] < node[1]:
            # Robot moves forward only
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("七")

        elif node == "8" and node[0] < node[1]:
            # Robot turns right & moves forward
            motion.moveTo(0.0, 0.0, -math.pi/2)
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("八")
        
        elif node == "9" and node[0] < node[1]:
            # Robot moves forward
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("九")

        elif node == "10" and node[0] < node[1]:
            # Robot moves forward
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十")

        elif node == "11" and node[0] < node[1]:
            # Robot moves forward
            motion.moveToward(-x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十一")           

        # Robot moves from right to left anticlockwise (Pattern 4)
        elif node == "12" and node[0] > node[1]:
            # Robot moves forward 
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十二")

        elif node == "11" and node[0] > node[1]:
            # Robot moves forward
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十一") 

        elif node == "10" and node[0] > node[1]:
            # Robot moves forward
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("十")

        elif node == "9" and node[0] > node[1]:
            # Robot moves forward
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("九")

        elif node == "8" and node[0] > node[1]:
            # Robot turns left & moves forward
            motion.moveTo(0.0, 0.0, math.pi/2)
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("八")
        
        elif node == "7" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("七")

        elif node == "6" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("六")
        
        elif node == "5" and node[0] > node[1]:
            # Robot turns left & moves forward
            motion.moveTo(0.0, 0.0, math.pi/2)
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("五")

        elif node == "4" and node[0] > node[1]:
            # Robot moves forward only 
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("四")

        elif node == "3" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("三") 

        elif node == "2" and node[0] > node[1]:
            # Robot moves forward only
            motion.moveToward(x, y, theta)
            time.sleep(t)
            motion.stopMove()
            tts.say("二") 
                    
def update_line():

    xdata = numpy.append(plt.gca().lines[0].get_xdata(), plt.gca().lines[1].get_xdata())
    ydata = numpy.append(plt.gca().lines[0].get_ydata(), plt.gca().lines[1].get_ydata())

    pos = hedge.position()
    new_x = pos[1]
    new_y = pos[2]
    plt.gca().lines[0].set_xdata(xdata[-29:])
    plt.gca().lines[0].set_ydata(ydata[-29:])
    
    plt.gca().lines[1].set_xdata([new_x])
    plt.gca().lines[1].set_ydata([new_y])
    
    plt.draw()    

def printThread():
    while True:
        try:
            sleep(1)
            pos = hedge.position()
            robot_x = pos[1]
            robot_y = pos[2]
            
            # Get initial positional coordinates of Pepper
            print ("Robot x-position: ", robot_x)
            print ("Robot y-position: ", robot_y)
            
            ####################################
            # Position of student 1 (85,  45)  #
            # Position of student 2 (85,  135) #
            # Position of student 3 (85,  225) #
            # Position of student 4 (85,  315) #
            # Position of student 5 (235, 315) #
            # Position of student 6 (235, 225) #
            # Position of student 7 (235, 135) #
            # Position of student 8 (235, 45)  #
            ####################################

            # Prompt user for robot's initial position (start)
            robot_start = input("Enter starting node position of robot: \n Student 1: 1, \n Student 2: 2, \n Student 3: 3, \n Student 4: 4, \n Student 5: 9, \n Student 6: 10, \n Student 7: 11, \n Student 8: 12\n")

            # Prompt user for robot's target position (goal)
            robot_goal = input("Enter goal node position of robot: \n Student 1: 1, \n Student 2: 2, \n Student 3: 3, \n Student 4: 4, \n Student 5: 9, \n Student 6: 10, \n Student 7: 11, \n Student 8: 12\n")

            # Calculate shortest path (Dijkstra's algorithm)
            dijkstra(graph, str(robot_start), str(robot_goal))

            # Get last position and print
            print (pos)
            print ("Robot x-position: ", pos[1])
            print ("Robot y-position: ", pos[2])
        except KeyboardInterrupt:

            # Stop and close serial port
            hedge.stop()  
            sys.exit()

def main():

    # Create plot
    global fig
    fig = plt.figure(" Pepper Navigation Program")

    # Draw present robot position
    ax = fig.add_subplot(111)
    ax.plot([],[], 'ro')
    ax.grid(True)
    
    # Draw previous robot position
    bx = fig.add_subplot(111)
    bx.plot([],[], 'bo')
    plt.axis('equal')
    plt.tick_params(axis='both', which = 'major', labelsize = 20)
    axes = plt.gca()
    axes.set_xlim([-500, 500])
    axes.set_ylim([-200, 600])
    axes.set_xlabel('x (cm)', fontsize = 20)
    axes.set_ylabel('y (cm)', fontsize = 20)

    # Draw table
    rect = plt.Rectangle((100, 0), 120, 360)
    ax.add_patch(rect)                     
    plt.text(160, 180, 'Table', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 0
    circ = plt.Circle((25, -45), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(25, -45, 'N0', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 1
    circ = plt.Circle((25, 45), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(25, 45, 'N1', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)
    
    # Draw node 2
    circ = plt.Circle((25, 135), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(25, 135, 'N2', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 3
    circ = plt.Circle((25, 225), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(25, 225, 'N3', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 4 
    circ = plt.Circle((25, 315), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(25, 315, 'N4', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 5
    circ = plt.Circle((25, 405), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(25, 405, 'N5', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 6
    circ = plt.Circle((115, 405), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(115, 405, 'N6', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 7
    circ = plt.Circle((205, 405), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(205, 405, 'N7', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 8
    circ = plt.Circle((295, 405), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(295, 405, 'N8', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 9 
    circ = plt.Circle((295, 315), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(295, 315, 'N9', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 10
    circ = plt.Circle((295, 225), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(295, 225, 'N10', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)
    
    # Draw node 11
    circ = plt.Circle((295, 135), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(295, 135, 'N11', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 12
    circ = plt.Circle((295, 45), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(295, 45, 'N12', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 13
    circ = plt.Circle((295, -45), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(295, -45, 'N13', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)
    
    # Draw node 14
    circ = plt.Circle((205, -45), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(205, -45, 'N14', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw node 15
    circ = plt.Circle((115, -45), radius = 10, color = 'g', fill = True)
    ax.add_patch(circ)
    plt.text(115, -45, 'N15', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw chair 1 (student 1)
    circ = plt.Circle((85, 45), radius = 10, color = 'r', fill = True)
    ax.add_patch(circ)
    plt.text(85, 45, 'S1', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)
    
    # Draw chair 2 (student 2)
    circ = plt.Circle((85, 135), radius = 10, color = 'r', fill = True)
    ax.add_patch(circ)
    plt.text(85, 135, 'S2', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw chair 3 (student 3)
    circ = plt.Circle((85, 225), radius = 10, color = 'r', fill = True)
    ax.add_patch(circ)
    plt.text(85, 225, 'S3', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw chair 4 (student 4)
    circ = plt.Circle((85, 315), radius = 10, color = 'r', fill = True)
    ax.add_patch(circ)
    plt.text(85, 315, 'S4', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw chair 5 (student 5)
    circ = plt.Circle((235, 315), radius = 10, color = 'r', fill = True)
    ax.add_patch(circ)
    plt.text(235, 315, 'S5', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw chair 6 (student 6)
    circ = plt.Circle((235, 225), radius = 10, color = 'r', fill = True)
    ax.add_patch(circ)
    plt.text(235, 225, 'S6', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)
    
    # Draw chair 7 (student 7)
    circ = plt.Circle((235, 135), radius = 10, color = 'r', fill = True)
    ax.add_patch(circ)
    plt.text(235, 135, 'S7', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw chair 8 (student 8)
    circ = plt.Circle((235, 45), radius = 10, color = 'r', fill = True)
    ax.add_patch(circ)
    plt.text(235, 45, 'S8', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10)

    # Draw beacon 8
    circ = plt.Circle((100,360), radius = 10, color = 'b', fill = True)
    ax.add_patch(circ)
    plt.text(100, 360, 'B8', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10, color = 'w')

    # Draw beacon 13
    circ = plt.Circle((100, 0), radius = 10, color = 'b', fill = True)
    ax.add_patch(circ)
    plt.text(100, 0, 'B13', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10, color = 'w')

    # Draw beacon 44
    circ = plt.Circle((220, 0), radius = 10, color = 'b', fill = True)
    ax.add_patch(circ)
    plt.text(220, 0, 'B44', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10, color = 'w')

    # Draw beacon 50
    circ = plt.Circle((220, 360), radius = 10, color = 'b', fill = True)
    ax.add_patch(circ)
    plt.text(220, 360, 'B50', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 10, color = 'w')

    global hedge
    # Create MarvelmindHedge thread
    hedge = MarvelmindHedge(tty = "/dev/tty.usbmodemfa131", recieveDataCallback=update_line) 
    hedge.start()
    
    # Create and start console out thread
    plotThread = Thread(target=printThread) 
    plotThread.start()
    
    plt.show()
    
main()
