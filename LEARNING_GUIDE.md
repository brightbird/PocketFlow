# PocketFlow 学习指南（初学者版）

## 第一步：环境准备

1. 确保安装了Python 3.8+
2. 克隆项目到本地：
   ```bash
   git clone https://github.com/The-Pocket/PocketFlow.git
   cd PocketFlow
   ```
3. 安装项目：
   ```bash
   pip install -e .
   ```

## 第二步：理解核心概念

### 1. 什么是Node（节点）？
- Node是PocketFlow的基本构建块
- 每个Node有三个主要方法：
  - `prep()`: 准备数据
  - `exec()`: 执行主要逻辑
  - `post()`: 处理结果

### 2. 什么是Flow（流程）？
- Flow连接多个Node形成工作流
- 控制Node之间的执行顺序

## 第三步：从简单示例开始

### 1. 运行最简单的示例
进入 `cookbook/pocketflow-chat/` 目录：
```bash
cd cookbook/pocketflow-chat/
pip install -r requirements.txt
```

设置OpenAI API密钥：
```bash
export OPENAI_API_KEY=your_actual_api_key_here
```

运行示例：
```bash
python main.py
```

### 2. 理解代码结构
查看以下文件：
- `main.py`: 主程序入口
- `utils.py`: 工具函数（如调用LLM）
- `flow.py`: 定义工作流程（如果有）

## 第四步：逐步深入复杂示例

1. `pocketflow-workflow` - 学习工作流模式
2. `pocketflow-agent` - 学习Agent模式
3. `pocketflow-batch` - 学习批处理

## 第五步：理解核心框架

查看 `pocketflow/__init__.py` 文件，这是整个框架的核心（仅100行代码！）

## 学习建议

1. **不要急于求成**：每个示例都要运行并理解
2. **动手修改**：尝试修改示例代码看效果
3. **查看文档**：访问 https://the-pocket.github.io/PocketFlow/
4. **加入社区**：通过Discord与其他开发者交流