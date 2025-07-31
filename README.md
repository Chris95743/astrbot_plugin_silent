<div align="center">

![:name](https://count.getloli.com/@astrbot_plugin_silent?name=astrbot_plugin_silent&theme=minecraft&padding=6&offset=0&align=top&scale=1&pixelated=1&darkmode=auto)

# astrbot_plugin_silent

_✨ [astrbot](https://github.com/AstrBotDevs/AstrBot) 静默插件 ✨_  

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![AstrBot](https://img.shields.io/badge/AstrBot-3.4%2B-orange.svg)](https://github.com/Soulter/AstrBot)
[![GitHub](https://img.shields.io/badge/作者-Chris-blue)](https://github.com/Chris95743)

</div>

## 🤝 介绍

- 一个智能静默插件，当LLM回复内容中包含"silent"关键词时，自动阻止发送回复消息。
- 适用于需要控制机器人回复行为的场景，避免不必要的消息发送。

## 📦 安装

- 可以直接在astrbot的插件市场搜索astrbot_plugin_silent，点击安装，耐心等待安装完成即可
- 若是安装失败，可以尝试直接克隆源码：

```bash
# 克隆仓库到插件目录
cd /AstrBot/data/plugins
git clone https://github.com/Chris95743/astrbot_plugin_silent

# 控制台重启AstrBot
```

## ⌨️ 使用说明

### 功能特性

- **自动检测**：插件会自动检测LLM回复内容中是否包含"silent"关键词（不区分大小写）
- **智能静默**：当检测到"silent"时，自动清空回复内容并阻止消息发送
- **双重保护**：在LLM响应阶段和消息装饰阶段都进行检测，确保静默功能的可靠性
- **调试友好**：提供详细的日志记录，便于调试和监控

### 工作原理

1. **LLM响应阶段**：检查LLM生成的回复内容，如果包含"silent"则清空回复文本
2. **消息装饰阶段**：再次检查最终的回复内容，确保包含"silent"或为空的消息不会被发送

### 使用场景

- 当你希望LLM在某些情况下不发送回复时，可以在prompt中指示LLM输出包含"silent"的内容
- 适用于条件性回复、敏感内容过滤、调试模式等场景

## 🤝 可能用途

- [x] 控制机器人在特定条件下的静默行为
- [x] 避免发送不必要或不合适的回复消息
- [x] 为LLM提供一种"不回复"的指令机制
- [x] 在调试过程中控制消息输出

## 👥 贡献指南

- 🌟 Star 这个项目！（点右上角的星星，感谢支持！）
- 🐛 提交 Issue 报告问题
- 💡 提出新功能建议
- 🔧 提交 Pull Request 改进代码

## 📌 注意事项

- 插件会检测所有包含"silent"关键词的回复内容（不区分大小写）
- 确保你的LLM模型理解"silent"指令的含义
- 插件运行时会输出调试日志，可通过日志监控插件工作状态
- 本插件仅供学习交流，作者不承担任何责任，如有需要，可QQ联系:1436198704
