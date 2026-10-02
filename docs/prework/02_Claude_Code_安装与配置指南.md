---
description: Claude Code 最新安装与配置指南：原生安装、Windows 与 WSL 选择、登录、版本诊断、更新和第一次本地任务。
---

# Claude Code 安装与配置指南

Claude Code 是面向本地文件和项目目录的命令行 AI 工作区。WorkBuddy 先帮助你熟悉“描述任务—执行—检查结果”的 Agent 闭环；Claude Code 再把这个闭环推进到终端、本地文件和可复用工作流。

**预计完成时间**：45—75 分钟
**难度等级**：⭐⭐⭐⭐⭐（难）

**官方文档**：

- [Claude Code 概述](https://code.claude.com/docs/zh-CN/overview)
- [高级设置与安装](https://code.claude.com/docs/zh-CN/setup)
- [快速开始](https://code.claude.com/docs/zh-CN/quickstart)

> 官方安装命令和账户要求可能变化。本文以当前官方文档为准；如果页面上的版本号、登录按钮或终端提示发生变化，以官方页面和当前客户端为准。

## 一、系统要求

官方当前列出的支持范围包括：

- macOS 13.0 及以上；
- Windows 10 1809 及以上或 Windows Server 2019 及以上；
- Ubuntu 20.04、Debian 10、Alpine Linux 3.19 及以上；
- 4GB 以上内存，支持 x64 或 ARM64；
- 能够访问互联网；
- Shell 可使用 Bash、Zsh、PowerShell 或 CMD。

### Windows 先做一个选择

- **原生 Windows**：适合直接处理 Windows 本地文件；不要求 WSL。建议另外安装 Git for Windows，以便使用 Git Bash。
- **WSL 2**：适合已经使用 Linux 工具链、希望在 Linux 环境中工作的同学。安装和启动 Claude Code 都在 WSL 终端内完成。

本期先以“原生 Windows 或 macOS”作为主路径；不熟悉 WSL 的同学不要为了跟教程完全一致而额外引入 WSL。

## 二、推荐安装方式：官方原生安装器

当前官方推荐使用原生安装器。它不要求先安装 Node.js，安装后会自动维护更新。

### macOS、Linux 或 WSL

在终端运行：

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows PowerShell

在 PowerShell 运行：

```powershell
irm https://claude.ai/install.ps1 | iex
```

### Windows CMD

在 CMD 运行：

```bat
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

安装完成后，关闭当前终端，重新打开一个新的终端窗口。不要把 PowerShell 命令粘贴到 CMD，也不要把 CMD 的 `&&` 命令直接粘贴到 PowerShell。

## 三、验证安装

先确认版本：

```bash
claude --version
```

如果成功，应当输出 Claude Code 版本号。再运行只读诊断：

```bash
claude doctor
```

重点查看：

- 安装是否健康；
- PATH 是否正确；
- 设置文件是否存在格式错误；
- 自动更新状态是否正常；
- 是否有需要处理的警告。

如果终端提示找不到 `claude`，先关闭终端并重新打开；仍然失败时，再根据提示检查 PATH，不要连续重复执行安装命令。

## 四、登录与账户

在准备好的测试目录中启动：

```bash
claude
```

按浏览器提示完成登录。当前官方文档说明，Claude Code 需要符合条件的 Claude 账户或受支持的企业 / 云平台接入；免费的 claude.ai 账户不包含 Claude Code 访问权限。

如果课程组另行提供第三方模型网关或组织账号配置，请以课程组发布的配置说明为准。不要把 API Key 直接写进群消息、截图、项目文件或公开仓库。

## 五、Windows 额外配置

### Git for Windows

Claude Code 在原生 Windows 上可以使用 PowerShell 工具；安装 Git for Windows 后，还可以使用 Git Bash。建议从 [Git 官方网站](https://git-scm.com/download/win)下载安装，并重新打开终端。

验证：

```powershell
git --version
```

如果 Claude Code 找不到 Git Bash，可在设置文件中配置：

```json
{
  "env": {
    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
  }
}
```

### WSL 2

如果选择 WSL 2：

1. 在 WSL 发行版中打开终端；
2. 按“macOS、Linux 或 WSL”的命令安装；
3. 在 WSL 文件系统或已经挂载的项目目录中启动 `claude`；
4. 不要把 Windows PowerShell 与 WSL 的路径、命令混在同一条操作链中。

## 六、VS Code（可选）

如果你习惯在编辑器中查看文件，可以安装 VS Code，并在项目目录打开终端启动 Claude Code。VS Code 是辅助查看和编辑工具，不是 Claude Code 的必备前置。

建议先完成命令行验证，再处理编辑器集成。这样即使插件没有连接成功，也能判断问题究竟在 Claude Code、终端还是编辑器。

## 七、完成第一次本地任务

建立独立测试目录，例如：

```text
ClaudeCode-夜校测试/
├── 输入材料/
└── 输出结果/
```

放入公开或已经脱敏的文本，然后在该目录启动 Claude Code：

```text
请阅读输入材料文件夹中的文本，提取三个关键事实，生成一份 Markdown 摘要保存到输出结果文件夹。不要补充材料中没有出现的事实，并告诉我你读取了哪些文件、生成了哪些文件、哪些地方需要人工检查。
```

验收以下结果：

- [ ] Claude Code 读取了正确的目录和文件；
- [ ] 生成文件出现在预期位置；
- [ ] 输出内容没有明显遗漏或虚构；
- [ ] 你能看懂它执行了什么；
- [ ] 你没有把真实客户材料直接放入测试目录。

## 八、更新与版本策略

原生安装器会自动检查并维护更新。需要立即更新时，可运行：

```bash
claude update
```

检查当前版本：

```bash
claude --version
```

如果你使用 Homebrew 或 WinGet 安装，则需要由对应包管理器更新：

```bash
brew upgrade claude-code
winget upgrade Anthropic.ClaudeCode
```

本期不建议为了“固定一个旧版本”而复制网上过时的安装命令；遇到版本差异时，先以官方安装页为准。

## 九、常见问题

### `claude` 找不到

关闭当前终端，重新打开；再运行 `claude --version`。如果仍然失败，运行 `claude doctor`，把完整输出中的路径和错误信息带到群里。

### Windows PowerShell 报 `&&` 错误

你可能把 CMD 命令粘贴到了 PowerShell。PowerShell 提示符通常以 `PS C:\` 开头；请改用 PowerShell 专用安装命令。

### Windows 需要管理员权限吗？

官方原生安装路径通常不要求以管理员身份运行。只有在单位设备策略、安装目录权限或安全软件拦截时，才需要联系设备管理员处理。

### 是否必须先安装 Node.js？

不必。当前官方原生安装器不以 Node.js 作为必备前置。只有选择 npm 安装路径时，才需要按官方文档准备相应 Node.js 版本。

### 登录后仍然无法使用

检查账户是否具备 Claude Code 权限、网络是否稳定，以及是否误设置了不匹配的 API 环境变量。不要把多个供应商的 Key 混在同一份配置里。

## 完成确认

- [ ] 我已按当前官方路径安装 Claude Code；
- [ ] `claude --version` 能返回版本号；
- [ ] `claude doctor` 没有未处理的关键错误；
- [ ] 我已完成登录；
- [ ] 我已在测试目录中完成一次本地文件任务；
- [ ] 我知道如何更新、诊断和安全地提交问题截图。

完成后继续阅读《03_环境验证清单.md》。
