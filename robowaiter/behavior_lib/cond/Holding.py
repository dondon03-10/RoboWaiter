import py_trees as ptree
from typing import Any
from robowaiter.behavior_lib._base.Cond import Cond

class Holding(Cond):
    can_be_expanded = True
    num_params = 2
    valid_args = [tuple(Cond.all_object|{'Nothing'})]

    def __init__(self,*args):
        super().__init__(*args)


    def _update(self) -> ptree.common.Status:
        # if self.scene.status?

        if self.name in self.scene.state["condition_set"]:
            return ptree.common.Status.SUCCESS
        else:
            return ptree.common.Status.FAILURE

        # if self.scene.state['chat_list'] == []:
        #     return ptree.common.Status.FAILURE
        # else:
        #     return ptree.common.Status.SUCCESS