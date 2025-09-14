from fastmcp import FastMCP
import random

mcp = FastMCP(name="打招呼服务", instructions="打招呼")


@mcp.tool
def say_hello(name: str) -> str:
    """打招呼，并返回一个随机数"""
    return f"你好，{name}，你的随机数是：{random.randint(1, 100)}！"


mcp.run()
