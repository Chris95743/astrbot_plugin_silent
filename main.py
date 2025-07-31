# -*- coding: utf-8 -*-
import re
import logging
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.provider import LLMResponse

@register("silent_plugin", "静默插件", "检测到silent时不发送回复消息的插件", "1.0.0")
class SilentPlugin(Star):
    def __init__(self, context: Context, config: dict):
        super().__init__(context)
        self.silent_pattern = re.compile(r'silent', re.IGNORECASE)
        
        # 设置日志
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
    @filter.on_llm_response(priority=95)
    async def check_silent_in_llm_response(self, event: AstrMessageEvent, response: LLMResponse):
        """
        检查LLM回复内容中是否包含silent标记
        如果包含则修改回复内容并标记为静默
        """
        if not response or not response.completion_text:
            return
            
        text = response.completion_text
        self.logger.debug(f"检查回复内容: {text}")
        
        # 检查回复内容中是否包含silent
        if self.silent_pattern.search(text):
            self.logger.info("检测到silent标记，移除回复内容")
            # 清空回复文本
            response.completion_text = ""
            return

    @filter.on_decorating_result()
    async def check_decorating_result(self, event: AstrMessageEvent):
        """
        在装饰结果阶段检查是否需要阻止发送
        """
        result = event.get_result()
        if not result:
            return
            
        # 获取回复内容进行检查
        reply_text = ""
        try:
            if hasattr(result, 'chain') and result.chain:
                if isinstance(result.chain, str):
                    reply_text = result.chain
                elif hasattr(result.chain, '__iter__'):
                    try:
                        for component in result.chain:
                            if hasattr(component, 'text'):
                                reply_text += str(component.text)
                            elif isinstance(component, str):
                                reply_text += component
                    except (TypeError, AttributeError) as e:
                        self.logger.warning(f"解析回复链时出错: {e}")
        except Exception as e:
            self.logger.error(f"获取回复内容时出错: {e}")
            return
        
        self.logger.debug(f"装饰阶段检查内容: {reply_text}")
        
        # 如果内容包含silent，则不发送
        if self.silent_pattern.search(reply_text):
            self.logger.info("装饰阶段检测到silent标记，阻止发送")
            event.set_result(None)
            return