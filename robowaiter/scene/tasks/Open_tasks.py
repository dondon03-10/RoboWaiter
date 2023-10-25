"""
人提出请求，机器人完成任务
1. 做咖啡（固定动画）：接收到做咖啡指令、走到咖啡机、拿杯子、操作咖啡机、取杯子、送到客人桌子上
2. 倒水
3. 夹点心

具体描述：设计一套点单规则（如菜单包含咖啡、水、点心等），按照规则拟造随机的订单。在收到订单后，通过大模型让机器人输出合理的备餐计划，并尝试在模拟环境中按照这个规划实现任务。

"""

# todo: 接收点单信息，大模型生成任务规划

from robowaiter.scene.scene import Scene

class SceneOT(Scene):
    def __init__(self, robot):
        super().__init__(robot)

    def _reset(self):
        self.reset_sim()

        self.add_walker(1085, 2630, 220)
        self.control_walker([self.walker_control_generator(0, False, 100, 755, 1900, 180)])

    def _run(self):
        pass

    def _step(self):
        pass