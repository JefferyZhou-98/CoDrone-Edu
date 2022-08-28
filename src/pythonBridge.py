"""
    Streaming 6Dof from QTM
"""

import asyncio
import xml.etree.ElementTree as ET
import pkg_resources
import qtm
import socket
import numpy as np


def create_body_index(xml_string):
    """ Extract a name to index dictionary from 6dof settings xml """
    xml = ET.fromstring(xml_string)

    body_to_index = {}
    for index, body in enumerate(xml.findall("*/Body/Name")):
        body_to_index[body.text.strip()] = index

    return body_to_index

def createMatLabPacket(id, position, rotation):
    packetArray = np.empty(13, dtype='>d')
    packetArray[0] = id
    packetArray[1] = position.x
    packetArray[2] = position.y
    packetArray[3] = position.z
    packetArray[4] = rotation.matrix[0]
    packetArray[5] = rotation.matrix[1]
    packetArray[6] = rotation.matrix[2]
    packetArray[7] = rotation.matrix[3]
    packetArray[8] = rotation.matrix[4]
    packetArray[9] = rotation.matrix[5]
    packetArray[10] = rotation.matrix[6]
    packetArray[11] = rotation.matrix[7]
    packetArray[12] = rotation.matrix[8]
    return packetArray

def getID(body_name):
    if body_name == 'tank_11':
        return 1
    elif body_name == 'tank_12':
        return 2
    else:
        return 1

def getNewBody():
    wanted_bodies = ["tank_11", "tank_12"]
    curIndex = 0
    body = wanted_bodies[curIndex]
    curIndex += 1
    if curIndex == len(wanted_bodies):
        curIndex = 0
    yield body
# saving data 
pos = []
euler = []
async def main():

    # Setup MatLab Socket
    my_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.connect(('127.0.0.1', 8825))

    # Connect to qtm
    connection = await qtm.connect("127.0.0.1")

    # Connection failed?
    if connection is None:
        print("Failed to connect")
        return

    # Take control of qtm, context manager will automatically release control after scope end
    async with qtm.TakeControl(connection, "password"):

        realtime = True

        if realtime:
            # Start new realtime
            await connection.new()
        else:
            # Load qtm file
            await connection.load(QTM_FILE)

            # start rtfromfile
            await connection.start(rtfromfile=True)

    # Get 6dof settings from qtm
    xml_string = await connection.get_parameters(parameters=["6d"])
    body_index = create_body_index(xml_string)

    wanted_body = "white_rover"

    def on_packet(packet):
        info, bodies = packet.get_6d()
        print(
            "Framenumber: {} - Body count: {}".format(
                packet.framenumber, info.body_count
            )
        )
        # for wanted_body in wanted_bodies:
        wanted_body = "tank_12"
        if wanted_body is not None and wanted_body in body_index:
            # Extract one specific body
            wanted_index = body_index[wanted_body]
            position, rotation = bodies[wanted_index]
            # extracting roll pitch yaw angles from rotation matrix 
            # using transformation
            rot_matrix = rotation[0]
            yaw = np.arctan2(rot_matrix[3], rot_matrix[0])
            pitch = np.arctan2(-rot_matrix[6], np.sqrt((rot_matrix[7])**2 + (rot_matrix[8])**2))
            roll = np.arctan2(rot_matrix[7], rot_matrix[8])
            euler_ang = [roll, pitch, yaw]
            # print("{} - Pos: {} - Rot: {}".format(wanted_body, position, euler_ang))
            MESSAGE=createMatLabPacket(getID(wanted_body), position, rotation).astype('>d')
            pos.append(position[0])
            euler.append(euler_ang)
            my_socket.send(MESSAGE)
        else:
            # Print all bodies
            for position, rotation in bodies:
                print("Pos: {} - Rot: {}".format(position, rotation))

    # Start streaming frames
    await connection.stream_frames(components=["6d"], on_packet=on_packet)
    

    # Wait asynchronously 5 seconds
    await asyncio.sleep(600)

    # Stop streaming
    await connection.stream_frames_stop()

    

    my_socket.close


if __name__ == "__main__":
    # Run our asynchronous function until complete
    asyncio.get_event_loop().run_until_complete(main())


print(euler)