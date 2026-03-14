from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import webbrowser

@register("yuanshen_web", "浅月tniay", "自动打开原神网页插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
        # 初始化时自动打开原神网页
        logger.info("正在打开原神网页...")
        webbrowser.open("https://ys.mihoyo.com/")

    # 注册指令的装饰器。指令名为 yuanshen。注册成功后，发送 `/yuanshen` 就会触发这个指令，并打开原神网页
    @filter.command("yuanshen")
    async def yuanshen(self, event: AstrMessageEvent):
        """打开原神网页""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        user_name = event.get_sender_name()
        logger.info(f"{user_name} 触发了打开原神网页指令")
        webbrowser.open("https://ys.mihoyo.com/")
        yield event.plain_result(f"已为你打开原神网页，{user_name}!") # 发送一条纯文本消息

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
