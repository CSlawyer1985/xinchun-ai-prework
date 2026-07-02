# 05 法律 Agent 运行结构仪表盘

> 78 个节点拆透法律 Agent——从看懂结构，到会用、会改、会沉淀。

## 这是什么

一个面向法律人自学 AI Agent 的交互仪表盘。把 Claude Code (Harness) 为核心的 Agent 运行结构，拆成 **78 个可点击、可交互的知识节点**，涵盖从输入到输出、从模型到观测、从扩展到沉淀的完整九大模块。

不只是一张静态架构图——点开每个节点，弹出的是**交互演示**：点击步进、滑块对比、构造器、检查清单、知识图谱网络，而非凝固的图片。

## 核心概念

| 模块 | 涵盖内容 |
|------|---------|
| 输入层 | 结构化 Prompt 构造、来源闸门 |
| 工作区 Scope | 用户级/项目级规则分层、Scope Router |
| Framework 能力抽象 | 模型抽象、工具接口、检索、记忆、Agent 循环、中间件 |
| Model 模型核心 | LLM 意图理解、法律推理、上下文整合、自检修正 |
| Runtime 状态执行 | write_todos 任务规划、解析→检索→证据→初稿→评估→判断 |
| Extension 扩展 | SubAgent、Agent Team、Skill、MCP、工作流、Hooks |
| Observability 观测 | Trace→Debug→Eval→Metrics→规则迭代 |
| 输出交付 | 最终法律文件、质量保障、交付物打包 |
| Memory 沉淀 | Harness 五件套（CLAUDE.md/rules/skills/memory/hooks）|

## 交互演示一览

点击节点后，详情页会根据概念类型展示不同交互：
- **Runtime 管线步进**：每一步显示输入/输出，可前进后退
- **Prompt 构造器**：填入字段自动组装结构化 Prompt
- **Agent 循环**：点击/自动播放 LM Loop 五阶段
- **三层上下文模型**：资产层/项目层/会话层 Tab 切换
- **SubAgent 扇出**：滑块调子 Agent 数量
- **Git 工作流**：init→add→commit→push→log→diff→/rewind 终端模拟
- **MCP 计数对比**：N×M 蜘蛛网 vs N+M 总线
- **Wiki 知识图谱**：点击卡片看双向链接网络
- *……共 19 种交互方式*

## 内容来源

卡片定义基于以下材料校准：
- 《Deep Agents 实战》ch01 三层架构、ch04 write_todos/中间件堆栈
- 三期 Harness 速查卡 + 上下文工程速查卡
- AI 通识课 Lesson 24 MCP 生态系统

## 入口

👉 **[打开仪表盘](https://cslawyer1985.github.io/agent-structure-dashboard/)**

---

> 提示：建议配合三期 Day2（Harness 五件套）和 Day4（法律工作流）使用，对照仪表盘的结构理解 Agent 运行时各层如何协作。
