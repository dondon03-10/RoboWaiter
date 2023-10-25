import py_trees as ptree
from typing import Any
from robowaiter.behavior_lib.Behavior import Bahavior

class IsChatting(Bahavior):
    def __init__(self, name: str, scene):
        super().__init__(name, scene)

    def setup(self, **kwargs: Any) -> None:
        return super().setup(**kwargs)

    def initialise(self) -> None:
        return super().initialise()

    def update(self) -> ptree.common.Status:
        # if self.scene.status?
        return ptree.common.Status.SUCCESS

    def terminate(self, new_status: ptree.common.Status) -> None:
        return super().terminate(new_status)
