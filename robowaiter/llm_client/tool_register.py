import inspect
import traceback
from copy import deepcopy
from pprint import pformat
from types import GenericAlias
from typing import get_origin, Annotated

_TOOL_HOOKS = {}
_TOOL_DESCRIPTIONS = {}


def register_tool(func: callable):
    tool_name = func.__name__
    tool_description = inspect.getdoc(func).strip()
    python_params = inspect.signature(func).parameters
    tool_params = []
    for name, param in python_params.items():
        annotation = param.annotation
        if annotation is inspect.Parameter.empty:
            raise TypeError(f"Parameter `{name}` missing type annotation")
        if get_origin(annotation) != Annotated:
            raise TypeError(f"Annotation type for `{name}` must be typing.Annotated")

        typ, (description, required) = annotation.__origin__, annotation.__metadata__
        typ: str = str(typ) if isinstance(typ, GenericAlias) else typ.__name__
        if not isinstance(description, str):
            raise TypeError(f"Description for `{name}` must be a string")
        if not isinstance(required, bool):
            raise TypeError(f"Required for `{name}` must be a bool")

        tool_params.append({
            "name": name,
            "description": description,
            "type": typ,
            "required": required
        })
    tool_def = {
        "name": tool_name,
        "description": tool_description,
        "params": tool_params
    }

    # print("[registered tool] " + pformat(tool_def))
    _TOOL_HOOKS[tool_name] = func
    _TOOL_DESCRIPTIONS[tool_name] = tool_def

    return func


def dispatch_tool(tool_name: str, tool_params: dict) -> str:
    if tool_name not in _TOOL_HOOKS:
        return f"Tool `{tool_name}` not found. Please use a provided tool."
    tool_call = _TOOL_HOOKS[tool_name]
    try:
        ret = tool_call(**tool_params)
    except:
        ret = traceback.format_exc()
    return str(ret)


def get_tools() -> dict:
    return deepcopy(_TOOL_DESCRIPTIONS)


# Tool Definitions

# @register_tool
# def random_number_generator(
#         seed: Annotated[int, 'The random seed used by the generator', True],
#         range: Annotated[tuple[int, int], 'The range of the generated numbers', True],
# ) -> int:
#     """
#     Generates a random number x, s.t. range[0] <= x < range[1]
#     """
#     if not isinstance(seed, int):
#         raise TypeError("Seed must be an integer")
#     if not isinstance(range, tuple):
#         raise TypeError("Range must be a tuple")
#     if not isinstance(range[0], int) or not isinstance(range[1], int):
#         raise TypeError("Range must be a tuple of integers")
#
#     import random
#     return random.Random(seed).randint(*range)


# @register_tool
# def get_weather(
#         city_name: Annotated[str, 'The name of the city to be queried', True],
# ) -> str:
#     """
#     Get the current weather for `city_name`
#     """
#
#     if not isinstance(city_name, str):
#         raise TypeError("City name must be a string")
#
#     key_selection = {
#         "current_condition": ["temp_C", "FeelsLikeC", "humidity", "weatherDesc", "observation_time"],
#     }
#     import requests
#     try:
#         resp = requests.get(f"https://wttr.in/{city_name}?format=j1")
#         resp.raise_for_status()
#         resp = resp.json()
#         ret = {k: {_v: resp[k][0][_v] for _v in v} for k, v in key_selection.items()}
#     except:
#         import traceback
#         ret = "Error encountered while fetching weather data!\n" + traceback.format_exc()
#
#     return str(ret)


# @register_tool
# def add(
#         a: Annotated[int, '需要相加的第1个数', True],
#         b: Annotated[int, '需要相加的第2个数', True]
# ) -> int:
#     """
#     获取 `a` + `b` 的值
#     """
#
#     if (not isinstance(a, int)) or (not isinstance(b, int)):
#         raise TypeError("相加的数必须为整数")
#
#     return int(a+b)

@register_tool
def create_sub_task(
        goal: Annotated[str, '子任务需要达到的目标条件集合，例如{On(Coffee,Bar)}，{At(Robot,Table1)}，{Is(AC,Off)}', True]
) -> str:
    """
    当需要完成具身任务（如做咖啡，拿放物体，扫地，前往某位置）时，调用该函数，根据用户的提示进行意图理解，生成子任务的目标状态集合 `goal`（以一阶逻辑的形式表示），用户意图
    做一杯咖啡,则该函数的参数为 "On(Coffee,Bar)",
    前往一号桌,则该函数的参数为 "At(Robot,Table1)",
    打开空调,则该函数的参数为 "Is(AC,On)",。
    关空调,则该函数的参数为 "Is(AC,Off)",。
    """

    return goal

@register_tool
def get_object_info(
        obj: Annotated[str, '需要获取信息的物体名称', True]
) -> str:
    """
    获取场景中指定物体 `object` 在哪里，
    如果`object` 是一个地点，例如洗手间，地方，则输出。
    如果`object`是一个咖啡，则输出。
    如果`object` 是空桌子，则输出一号桌
    """
    near_object = None
    if obj == "Table":
        near_object = "Bar"
    if obj == "洗手间":
        near_object = "大门"
    if obj == "空桌子":
        near_object = "一号桌"
    return near_object



if __name__ == "__main__":
    print(dispatch_tool("get_weather", {"city_name": "beijing"}))
    print(get_tools())
