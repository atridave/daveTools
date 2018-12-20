'''Module for comman animation functions and classes'''

import maya.cmds as cmds

'''function for get time info'''

def get_timerange():

    info = []

    start_frame = cmds.playbackOptions(q=1, min=1)
    end_frame = cmds.playbackOptions(q=1, max=1)
    frames = endFrame-startFrame
    info.append(start_frame)
    info.append(end_frame)
    info.append(frames)
    return info