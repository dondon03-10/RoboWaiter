"""
环境主动探索和记忆
要求输出探索结果（语义地图）对环境重点信息记忆。生成环境的语义拓扑地图，和不少于10个环境物品的识别和位置记忆，可以是图片或者文字或者格式化数据。
"""

from robowaiter.scene.scene import Scene

class SceneAEM(Scene):
    def __init__(self, robot):
        super().__init__(robot)
        self.event_list = [
            (5, self.create_chat_event("测试AEM")),
        ]

    def _reset(self):
        pass
    def _run(self):
        pass


if __name__ == '__main__':
    import os
    from robowaiter.robot.robot import Robot

    robot = Robot()

    # create task
    task = SceneAEM(robot)
    task.reset()
    task.run()