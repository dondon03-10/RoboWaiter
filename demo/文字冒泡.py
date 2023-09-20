#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# enconding = utf8
import sys
import time
import grpc

sys.path.append('./')
sys.path.append('../')

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

from proto import GrabSim_pb2
from proto import GrabSim_pb2_grpc

channel = grpc.insecure_channel('localhost:30001', options=[
    ('grpc.max_send_message_length', 1024 * 1024 * 1024),
    ('grpc.max_receive_message_length', 1024 * 1024 * 1024)
])

sim_client = GrabSim_pb2_grpc.GrabSimStub(channel)


def map_test(map_id=0, scene_num=1):
    initworld = sim_client.Init(GrabSim_pb2.NUL())
    print(sim_client.AcquireAvailableMaps(GrabSim_pb2.NUL()))
    initworld = sim_client.SetWorld(GrabSim_pb2.BatchMap(count=scene_num, mapID=map_id))


def control_robot_action(scene_id=0, type=0, action=0, message="你好"):
    scene = sim_client.ControlRobot(GrabSim_pb2.ControlInfo(scene=scene_id, type=type, action=action, content=message))
    if (scene.info == "action success"):
        return True
    else:
        return False


if __name__ == '__main__':
    map_id = 3  # 地图编号: 0：空房间 1：室内 2:咖啡厅1.0 3: 咖啡厅2.0 4:餐厅 5:养老院 6：会议室
    scene_num = 1  # 场景数量
    map_test(map_id, scene_num)  # 场景加载测试
    time.sleep(5)

    # 文字冒泡
    control_robot_action(0, 0, 1, "你好，欢迎光临")