---
description: ChatGPT 桌面端与 Codex CLI 安装教程：完成官方 GUI 安装、ChatGPT 登录、Codex CLI 登录和第一次本地任务。
---

# ChatGPT CLI 与 GUI 安装指南

本页的“GUI”指新的 **ChatGPT 桌面应用**；本页的“CLI”指 OpenAI 的 **Codex CLI**。两者使用同一个 OpenAI / ChatGPT 账号体系，但入口和工作方式不同：

- **ChatGPT 桌面端**：适合对话、Work、文件处理和图形化使用 Codex；
- **Codex CLI**：在终端中处理本地项目、文件和代码任务。

**预计完成时间**：20—40 分钟

**官方入口**：<https://chatgpt.com/download/>

**官方资料**：

- [ChatGPT 桌面应用迁移说明](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app)
- [ChatGPT macOS 应用下载说明](https://help.openai.com/en/articles/9275200-using-the-chatgpt-macos-app)
- [OpenAI Codex CLI 入门](https://help.openai.com/en/articles/11096431)
- [Codex CLI 与 ChatGPT 登录](https://help.openai.com/en/articles/11381614-api-codex-cli-and-sign-in-with-chatgpt)

> OpenAI 的桌面应用、Codex 和登录流程会持续更新。下载和登录时以官方页面、当前应用界面为准，不使用第三方安装包。

## 一、先理解两种入口

### ChatGPT 桌面端（GUI）

适合：

- 快速提问、整理资料和生成初稿；
- 使用 Work 处理研究、文档、表格、演示文稿和报告；
- 在图形界面中使用 Codex，选择项目目录并查看任务过程；
- 需要截图、文件上传或桌面快捷入口的场景。

### Codex CLI

适合：

- 在终端中处理本地文件和项目目录；
- 检查、修改和生成代码或结构化文件；
- 需要审批、差异查看和更细控制的任务；
- 与 Git、脚本和其他命令行工具配合。

本期不要求大家一开始就把所有入口都学会。先安装并完成一次小任务，重点是理解“选择工作目录—说明任务—检查结果—控制权限”的基本闭环。

## 二、安装 ChatGPT 桌面端（GUI）

### 1. 从官方下载

打开 [ChatGPT 官方下载页](https://chatgpt.com/download/)，页面会根据设备提供对应版本。

不要从网盘、论坛附件或不明镜像下载 ChatGPT 安装包。

### 2. macOS

OpenAI 当前说明新的 ChatGPT macOS 应用支持 macOS 14 及以上，并兼容 Apple Silicon（M1 或更新）和 Intel Mac。安装步骤：

1. 下载适配当前 Mac 的安装包；
2. 打开安装文件，将 ChatGPT 拖入“应用程序”；
3. 从“应用程序”、程序坞或 Spotlight 启动；
4. 使用 ChatGPT 账号登录；
5. 首次打开后确认顶部能够切换 ChatGPT / Codex；如果账号或版本暂时没有某项入口，以当前账号权限和官方说明为准。

macOS 常用快捷入口是 `Option + Space`，可快速打开 ChatGPT 对话窗口。

### 3. Windows

1. 从官方下载页进入 Windows 下载入口；
2. 按系统提示完成安装；
3. 启动 ChatGPT 并登录；
4. 如果使用 Microsoft Store 版本，遵循单位设备对应用商店的管理策略；
5. 登录后确认能够打开 ChatGPT，并查看是否有 Work / Codex 入口。

Windows 的可用功能和分发方式可能受版本、账号和组织策略影响；不要因为某个入口暂时不可见，就安装来源不明的“完整版”。

## 三、GUI 第一个练习

在 ChatGPT 桌面端先使用一份公开或脱敏的小材料，完成：

```text
请阅读我提供的材料，用不超过 300 字概括事实背景，并列出三个需要人工进一步核对的问题。不要补充材料中没有出现的事实。
```

练习重点：

- [ ] 能正常登录和发起对话；
- [ ] 能上传或打开测试材料；
- [ ] 能看懂回答与材料之间的对应关系；
- [ ] 知道如何开启临时对话或删除不需要保留的内容；
- [ ] 没有上传真实客户或单位内部材料。

## 四、安装 Codex CLI

Codex CLI 是 OpenAI 的终端工具。官方入门文档提供 npm 安装路径：

```bash
npm install -g @openai/codex
```

安装完成后检查版本或直接启动：

```bash
codex --version
codex
```

如果你看到 `codex` 找不到：

1. 关闭当前终端，重新打开一个终端窗口；
2. 检查 Node.js 与 npm 是否可用：

```bash
node --version
npm --version
```

3. 如果 npm 全局目录没有加入 PATH，先记录完整错误信息，不要连续重复安装。

## 五、用 ChatGPT 账号登录 Codex CLI

当前官方支持在 Codex CLI 中使用 ChatGPT 登录：

```bash
codex --login
```

然后：

1. 浏览器打开登录页面；
2. 选择“Sign in with ChatGPT”；
3. 使用与桌面端相同的 OpenAI / ChatGPT 账号完成授权；
4. 回到终端启动 `codex`；
5. 按提示选择默认权限或审批方式。

也可以直接运行 `codex`，在首次启动时按界面提示完成登录。

> ChatGPT 登录和 API Key 是两种不同的凭证路径。不要把密码、OAuth 回调内容或自动生成的 Key 发到群里，也不要把 Key 写入项目文件。

## 六、CLI 第一个本地任务

建立独立测试目录：

```text
Codex-夜校测试/
├── 输入材料/
└── 输出结果/
```

在该目录打开终端，启动：

```bash
codex
```

输入：

```text
请检查输入材料文件夹中的文本，生成一份 Markdown 摘要保存到输出结果文件夹。先告诉我你准备读取哪些文件和写入哪个文件，等我确认后再执行。完成后说明你实际做了什么，并列出需要人工检查的地方。
```

这个练习有意保留“先说明、再批准、后执行”的审批步骤。不要一开始就使用全自动模式，也不要在包含真实业务材料的目录中测试。

## 七、GUI 与 CLI 如何分工

| 场景 | 优先入口 | 练习重点 |
|---|---|---|
| 快速提问、资料整理 | ChatGPT 桌面端 | 提问、上传、复核 |
| 研究和交付文档 | ChatGPT 的 Work | 任务范围、来源、成品检查 |
| 本地文件与项目 | Codex CLI | 工作目录、审批、差异检查 |
| 需要批处理或脚本 | Codex CLI | 小步执行、记录命令、可恢复 |

本课程不会把“用了 GUI”当成完成标准。真正的标准是：你知道材料在哪里、工具做了什么、结果如何检查、出了问题如何回滚或求助。

## 八、隐私与权限

- 课前只使用公开、自己编写或已经脱敏的材料；
- 不上传客户姓名、联系方式、身份证号、案卷原件、未公开合同或内部链接；
- 给 CLI 的工作目录要尽量小，不要直接把整个电脑或整个案件目录交给工具；
- 默认采用需要确认的审批方式，先看清楚将读取、修改或生成哪些文件；
- 任何生成的法律结论、事实摘要和文书内容都必须人工复核。

## 九、完成确认

- [ ] 我已从官方页面安装 ChatGPT 桌面端；
- [ ] 我已登录并能完成一次 GUI 小练习；
- [ ] 我已安装 `@openai/codex`；
- [ ] `codex --version` 能返回版本号；
- [ ] 我已用 ChatGPT 账号完成 Codex CLI 登录；
- [ ] 我已在测试目录完成一次需要确认的本地任务；
- [ ] 我知道 GUI、CLI、权限和隐私边界的区别。

完成后继续阅读《03_环境验证清单.md》。
