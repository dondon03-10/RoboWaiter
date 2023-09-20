#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
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

channel = grpc.insecure_channel('localhost:30001',options=[
            ('grpc.max_send_message_length', 1024*1024*1024),
            ('grpc.max_receive_message_length', 1024*1024*1024)
        ])

sim_client = GrabSim_pb2_grpc.GrabSimStub(channel)

def map_test(map_id=0, scene_num=1):
    initworld = sim_client.Init(GrabSim_pb2.NUL())
    print(sim_client.AcquireAvailableMaps(GrabSim_pb2.NUL()))
    initworld = sim_client.SetWorld(GrabSim_pb2.BatchMap(count=scene_num, mapID=map_id))

def joint_test(scene_id=0):
    print('------------------joint_test----------------------')
    action_list = [[0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 36.0, -39.37, 37.2, -92.4, 4.13, -0.62, 0.4],
                   [0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 36.0, -39.62, 34.75, -94.80, 3.22, -0.26, 0.85],
                   [0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 32.63, -32.80, 15.15, -110.70, 6.86, 2.36, 0.40],
                   [0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 28.18, -27.92, 6.75, -115.02, 9.46, 4.28, 1.35],
                   [0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 4.09, -13.15, -11.97, -107.35, 13.08, 8.58, 3.33]]

    for value in action_list:
        action = GrabSim_pb2.Action(scene=scene_id, action=GrabSim_pb2.Action.ActionType.RotateJoints, values=value)
        scene = sim_client.Do(action)

        for i in range(8, 21):  # arm
            print(
                f"{scene.joints[i].name}:{scene.joints[i].angle} location:{scene.joints[i].location.X},{scene.joints[i].location.Y},{scene.joints[i].location.Z}"
            )
        print('')
        for i in range(5, 10):  # Right hand
            print(
                f"{scene.fingers[i].name} angle:{scene.fingers[i].angle} location:{scene.fingers[i].location[0].X},{scene.fingers[i].location[0].Y},{scene.fingers[i].location[0].Z}"
            )
        print('----------------------------------------')
        time.sleep(0.03)
    time.sleep(1)

def gen_obj(scene_id, h=80):
    print('------------------gen objs----------------------')
    scene = sim_client.Observe(GrabSim_pb2.SceneID(value=scene_id))
    ginger_loc = [scene.location.X, scene.location.Y, scene.location.Z]

    obj_list = [
        GrabSim_pb2.ObjectList.Object(x=ginger_loc[0] - 90, y=ginger_loc[1] + 30, yaw=10, z=h, type=4),
        GrabSim_pb2.ObjectList.Object(x=ginger_loc[0] - 80, y=ginger_loc[1] + 31, z=h, type=5),
        GrabSim_pb2.ObjectList.Object(x=ginger_loc[0] - 33, y=ginger_loc[1] - 10.5, z=h+20, type=7),
        GrabSim_pb2.ObjectList.Object(x=ginger_loc[0] - 70, y=ginger_loc[1] + 33, z=h, type=9),
        GrabSim_pb2.ObjectList.Object(x=ginger_loc[0] - 60, y=ginger_loc[1] + 34, z=h, type=13)
    ]
    scene = sim_client.AddObjects(GrabSim_pb2.ObjectList(objects=obj_list, scene=scene_id))
    print(scene.collision)
    time.sleep(5)

def remove_obj(scene_id=0, id_list=[1]):
    print('------------------remove objs----------------------')
    remove_obj_list = id_list
    scene = sim_client.RemoveObjects(GrabSim_pb2.RemoveList(IDs=remove_obj_list, scene=scene_id))
    print(f"remove objects {id_list}. current obj:")
    time.sleep(1)

def clean_obj(scene_id=0):
    print('------------------clean objs----------------------')
    scene = sim_client.CleanObjects(GrabSim_pb2.SceneID(value=scene_id))

def obj_test(scene_id=0):
    gen_obj(scene_id)
    # remove_obj(scene_id, id_list=[0])
    # clean_obj(scene_id)

def grasp_test(hand_id, obj_scene_id, scene_id=0):
    action = GrabSim_pb2.Action(scene=scene_id, action=GrabSim_pb2.Action.ActionType.Grasp, values=[hand_id, obj_scene_id])
    scene = sim_client.Do(action)

def release_test(hand_id, scene_id=0):
    action = GrabSim_pb2.Action(scene=scene_id, action=GrabSim_pb2.Action.ActionType.Release, values=[hand_id])
    scene = sim_client.Do(action)

if __name__ == '__main__':
    map_id = 3                      # 地图编号: 3: 咖啡厅
    scene_num = 1                   # 场景数量
    map_test(map_id, scene_num)     # 场景加载测试
    time.sleep(5)

    for i in range(scene_num):
        print("------------------", i, "----------------------")
        joint_test(i)               # 关节控制测试
        obj_test(i)                 # 物品生成测试
        grasp_test(1, 2)            # 抓取物品测试
        joint_test(i)               # 关节控制测试
        release_test(1)             # 释放物品测试