import py_trees as ptree
from typing import Any
from robowaiter.behavior_lib._base.Act import Act
from robowaiter.behavior_lib._base.Behavior import Status

class PickUp(Act):
    can_be_expanded = True
    num_args = 1
    valid_args = Act.all_object
    def __init__(self, *args):
        super().__init__(*args)
        self.target_obj = self.args[0]


    @classmethod
    def get_info(cls,arg):
        info = {}
        info["pre"] = {f'At(Robot,{arg})','Holding(Nothing)'}
        info["add"] = {f'Holding({arg})'}
        info["del_set"] = {f'Holding(Nothing)'}
        for place in Act.all_place:
            info["del_set"] |= {f'On({arg},{place})'}
        return info


    def _update(self) -> ptree.common.Status:
        # self.scene.test_move()
        op_type=16
        obj_id = 0
        # 遍历场景里的所有物品，根据名字匹配位置最近的 obj-id

        if self.args=="Coffee":
            obj_id = 273

        self.scene.op_task_execute(op_type, obj_id=obj_id)

        self.scene.state["condition_set"] |= (self.info["add"])
        self.scene.state["condition_set"] -= self.info["del_set"]
        return Status.RUNNING
