# Claude Code 安装与配置指南（国内直连优先版）

> **课程机制提醒**：本课程为公益课堂，保证金用于学习约束。完成听课与作业是退还基础；若中途退课，将按约定扣减后退还剩余金额。
>
> **学习节奏提醒**：第一堂课主要使用 Cherry Studio，Claude Code 在后续课程（Day 2）重点使用。安装时间可放宽；若遇到困难，请先在群内留言，或参考可靠网络教程后再继续。

**预计完成时间**：45-75分钟
**难度等级**：⭐⭐⭐⭐⭐（难）
**前置要求**：

- [ ] 已阅读《00_课前准备总览.md》
- [ ] 电脑满足硬件和软件要求
- [ ] 已准备智谱GLM API账号与Key
- [ ] 预留出45-75分钟的安装时间

**下一步**：完成后请继续阅读《03_环境验证清单.md》

**参考教程及官方文档**：

- **mac：**
  - https://mp.weixin.qq.com/s/pEPweAhpzZb1ef5oMvaDDA?scene=1&click_id=25
  - https://mp.weixin.qq.com/s/DglI-NdWbVIwGyK_HEbnrw
- **Windows：**
  - https://mp.weixin.qq.com/s/35BwzdVP8u6X-f9pasSo-w
  - https://www.bilibili.com/video/BV19vc5zUEeQ/?spm_id_from=333.337.search-card.all.click&vd_source=9a8fdc30aa63b6d73c89778c70b7e1e0
- **官方文档：**
  - https://code.claude.com/docs/en/overview
  - https://code.claude.com/docs/en/setup
  - https://docs.z.ai/devpack/extension/coding-tool-helper

---

## 📖 工具介绍

### 什么是Claude Code？

**Claude Code** 是Anthropic公司推出的**命令行AI工具**，它可以：

- 🗣️ 通过自然语言对话完成工作
- 📄 处理文字、分析数据、整理文件
- 🔧 自动化执行复杂的工作流
- 💻 读取和编辑本地文件
- 🔍 集成各种MCP（Model Context Protocol）工具

### 为什么选择Claude Code？

**与传统AI聊天工具的区别**：

| 传统AI聊天工具   | Claude Code CLI      |
| ---------------- | -------------------- |
| 只能对话         | 能对话+操作文件      |
| 需要手动复制粘贴 | 自动读取本地文件     |
| 无法批量处理     | 支持批量处理文档     |
| 界面操作         | 命令行操作（更高效） |

**适用场景**：

- ✅ 批量处理法律文书（如审查20份合同）
- ✅ 自动化重复性任务（如提取关键信息）
- ✅ 构建复杂工作流（如"检索→分析→生成报告"）
- ❌ 不适合：需要频繁切换文件、需要可视化操作

### 本课程的配置方案

我们将使用 **Claude Code CLI + 智谱GLM API** 的单线组合：

- 默认模型：`glm-4.7`（或平台最新可用GLM）
- 优先目标：跑通稳定可复用的法律任务链路
- 不做多平台分流，先把主链路跑顺

**安装方式说明（建议）**：

- 主路线：使用 Claude Code 官方推荐的本地安装方式（native install）
- 备路线：使用 `winget`（Windows）安装
- 兼容路线：`npm install -g @anthropic-ai/claude-code`（仅在前两种不可用时使用）

> 说明：如果你已有其他可用模型的 API（且兼容 Claude Code 接入方式），也可以自行接入作为备用。

### 计费与网络准备（开课前）

- 计费方式：按量计费（PAYG）为主
- 建议先小额充值测试，避免一次性大额投入；后续可以考虑更换编程包月/季套餐。
- 网络要求：确保可访问 `open.bigmodel.cn`

---

## 🔍 步骤1：前置要求检查（非必需）

在开始安装之前，我们需要检查你的电脑是否满足要求。

### 1.1 检查操作系统

**操作说明**：确认你的操作系统版本。

#### Windows系统

```powershell
# 按Win+R，输入"winver"，回车
# 或在PowerShell中执行：
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

**预期输出**：

```
OS Name:                   Microsoft Windows 10 Pro / Windows 11
OS Version:               10.0.XXXXX 或更高
```

**✅ 成功标志**：显示Windows 10或Windows 11

**❌ 失败表现**：显示Windows 7、Windows 8等

**🔧 解决方法**：

- 升级到Windows 10或更高版本
- 或使用其他电脑（Mac/Linux）

**💡 小贴士**：Windows 10和11都支持，但推荐使用Windows 11（性能更好）。

#### macOS系统

```bash
# 点击左上角苹果图标 → 关于本机
# 或在终端中执行：
sw_vers
```

**预期输出**：

```
ProductName:	macOS
ProductVersion:	13.0 或更高
BuildVersion:	22XXXX
```

**✅ 成功标志**：版本号 ≥ 13.0（Ventura）

**❌ 失败表现**：版本号 < 13.0

**🔧 解决方法**：

- 升级到最新的macOS版本
- 确保至少是macOS 13（Ventura）

**⚠️ 警告**：升级操作系统前请备份重要数据！

#### Linux系统

```bash
# 查看系统版本
cat /etc/os-release
# 或
lsb_release -a
```

**预期输出**：

```
NAME="Ubuntu"
VERSION="20.04.3 LTS" 或更高
# 或其他主流发行版（Debian、CentOS、Fedora等）
```

**✅ 成功标志**：使用主流Linux发行版（Ubuntu、Debian、CentOS、Fedora等）

**❌ 失败表现**：使用小众发行版

**🔧 解决方法**：

- 使用Ubuntu 20.04或更高版本（推荐）
- 或在虚拟机中运行Ubuntu

---

### 1.2 检查Node.js是否已安装

**操作说明**：打开终端/命令行，检查是否已安装Node.js。

#### Windows系统

```powershell
# 在PowerShell中执行：
node --version
# 或
node -v
```

#### macOS/Linux系统

```bash
# 在终端中执行：
node --version
# 或
node -v
```

**预期输出**：

```
v20.18.0
# 或
v18.x.x、v22.x.x 等LTS版本
```

**✅ 成功标志**：显示版本号（如v18.x.x、v20.x.x、v22.x.x）

**❌ 失败表现**：

```
'node' 不是内部或外部命令，也不是可运行的程序
# 或
command not found: node
```

**🔧 解决方法**：

- 如果看到错误信息，说明Node.js未安装，请继续阅读"步骤2：安装Node.js"
- 如果已安装但版本过低（< v18），请升级到最新LTS版本

**💡 小贴士**：Node.js的版本号格式为"v主版本.次版本.修订号"，我们推荐使用v18或v20的LTS（长期支持）版本。

---

### 1.3 检查 Git（Windows 必查）

> 如果你是 macOS/Linux 学员，可直接跳到 1.4。

**操作说明**：Windows 学员打开 PowerShell，执行：

```powershell
git --version
```

**预期输出**：

```
git version 2.xx.x.windows.x
```

**✅ 成功标志**：显示 Git 版本号

**❌ 失败表现**：

```
'git' 不是内部或外部命令，也不是可运行的程序
```

**🔧 解决方法**：

- 安装 Git for Windows：https://git-scm.com/download/win
- 安装完成后重启 PowerShell，再执行 `git --version`
- 如果仍失败，确认 Git 安装路径已加入 PATH

---

### 1.4 检查网络连接

**操作说明**：测试智谱GLM API连通性。

#### Windows系统

```powershell
# 在PowerShell中执行：
Test-NetConnection -ComputerName open.bigmodel.cn -Port 443
```

**预期输出**：

```
ComputerName     : open.bigmodel.cn
RemoteAddress    : XXX.XXX.XXX.XXX
RemotePort       : 443
InterfaceAlias   : Wi-Fi / Ethernet
TcpTestSucceeded : True
```

**✅ 成功标志**：`TcpTestSucceeded : True`

**❌ 失败表现**：`TcpTestSucceeded : False`

**🔧 解决方法**：

- 检查网络连接是否正常
- 尝试访问 https://open.bigmodel.cn/ 浏览器能否打开
- 如果是公司网络，联系IT确认放通目标域名

#### macOS/Linux系统

```bash
# 在终端中执行：
curl -I https://open.bigmodel.cn/
```

**预期输出**：

```
HTTP/2 200
server: nginx
date: ...
```

**✅ 成功标志**：返回 `HTTP/2 200`或 `HTTP/1.1 200`

**❌ 失败表现**：

```
curl: (7) Failed to connect to ...
# 或
Could not resolve host: open.bigmodel.cn
```

**🔧 解决方法**：

- 检查网络连接
- 尝试ping 8.8.8.8测试基础网络
- 如果是公司网络，可能需要联系IT部门开放访问权限

---

**📍 检查点**：在继续之前，请确认：

- [ ] 我的操作系统满足要求（Windows 10+/macOS 13+/主流Linux）
- [ ] 我知道Node.js是否已安装（如已安装，版本≥v18）
- [ ] （Windows）我已安装 Git for Windows 并可执行 `git --version`
- [ ] 我能正常访问智谱GLM API服务器

如果未通过检查点，请先解决上述问题，或查阅《04_常见问题FAQ.md》。

---

## 📦 步骤2：安装Node.js

**如果步骤1中检查到Node.js已安装且版本≥v18，可以跳过此步骤。**

### 2.1 下载Node.js安装包

**操作说明**：访问Node.js官网，下载适合你操作系统的安装包。

#### 方法1：官网下载（推荐）

1. 打开浏览器，访问：https://nodejs.org/
2. 首页会显示两个下载按钮
   - 左边：**LTS**（长期支持版本，推荐）
   - 右边：**Current**（最新版本）
3. 点击左侧的"LTS"按钮下载
   - Windows会下载 `.msi`安装包（约30MB）
   - macOS会下载 `.pkg`安装包（约40MB）
   - Linux会下载源码包或二进制包

**✅ 成功标志**：浏览器开始下载安装包

**💡 小贴士**：LTS版本更稳定，适合生产环境。

**图示参考（Windows）**
![Node.js 下载页](/images/claude-guide/nodejs-download.png)

#### 方法2：使用Homebrew（macOS/Linux推荐）

**如果你使用macOS或Linux，可以使用包管理器安装（更方便）：**

```bash
# 安装Homebrew（如果没有）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 使用Homebrew安装Node.js
brew install node
```

**预期输出**：

```
==> Downloading https://...
==> Installing node
🍺 /usr/local/Cellar/node/20.x.x: X files, YMB
```

**✅ 成功标志**：显示安装成功信息

**⚠️ 警告**：Homebrew安装过程可能需要输入管理员密码，请确保你有权限。

---

### 2.2 安装Node.js

#### Windows系统

**操作说明**：

1. **双击**下载好的 `.msi`安装包
2. 出现安装向导界面
   - 点击"Next"继续
3. **接受许可协议**：
   - 勾选"I accept the terms in the License Agreement"
   - 点击"Next"
4. **选择安装路径**：
   - 默认路径：`C:\Program Files\nodejs\`
   - 建议使用默认路径
   - 点击"Next"
5. **选择安装组件**：
   - **务必勾选**"Add to PATH"（自动配置环境变量）
   - 确保此选项被勾选
   - 点击"Next"
6. **开始安装**：
   - 点击"Install"开始安装
   - 等待安装完成（约1-2分钟）
7. **完成安装**：
   - 点击"Finish"完成安装

**✅ 成功标志**：

- 安装向导显示"Installation completed successfully"
- 可以在"程序和功能"中看到"Node.js"

**❌ 失败表现**：

- 安装过程中出现错误
- 提示权限不足

**🔧 解决方法**：

- **方法1**：以管理员身份运行安装包（右键 → 以管理员身份运行）
- **方法2**：临时关闭杀毒软件和防火墙
- **方法3**：检查磁盘空间是否充足（至少500MB）

**⚠️ 警告**：安装完成后，建议**重启电脑**或**重启PowerShell**，以确保环境变量生效。

---

#### macOS系统

**操作说明**：

1. **双击**下载好的 `.pkg`安装包
2. 出现安装界面
   - 点击"继续"继续安装
3. **查看简介**：
   - 阅读软件信息
   - 点击"继续"
4. **选择安装目标**：
   - 默认：Macintosh HD
   - 点击"继续"
5. **安装类型**：
   - 点击"安装"
6. **输入密码**：
   - 输入管理员密码
   - 点击"安装软件"
7. **等待安装完成**：
   - 显示"安装成功"
   - 点击"关闭"

**✅ 成功标志**：

- 安装向导显示"安装成功"
- 在终端中执行 `which node`显示 `/usr/local/bin/node`

**❌ 失败表现**：

- 提示"无法验证开发者"
- 提示"已损坏"

**🔧 解决方法**：

- **方法1**：在"系统偏好设置 → 安全性与隐私"中点击"仍要打开"
- **方法2**：右键点击安装包 → 打开 → 点击"打开"
- **方法3**：如果仍然失败，尝试使用Homebrew安装（见前文）

---

#### Linux系统（Ubuntu/Debian）

**操作说明**：

```bash
# 更新包管理器
sudo apt update

# 安装Node.js（使用NodeSource仓库）
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# 验证安装
node --version
npm --version
```

**预期输出**：

```
v20.x.x
10.x.x
```

**✅ 成功标志**：显示Node.js和npm的版本号

**❌ 失败表现**：

```
E: Unable to locate package
# 或
Permission denied
```

**🔧 解决方法**：

- **方法1**：确保使用 `sudo`命令（需要管理员权限）
- **方法2**：尝试使用其他安装方式（如从官网下载二进制包）
- **方法3**：使用nvm（Node Version Manager）安装

---

### 2.3 验证Node.js安装

**操作说明**：重新打开终端/命令行，验证Node.js和npm是否安装成功。

#### Windows/macOS/Linux通用

```bash
# 检查Node.js版本
node --version

# 检查npm版本（npm是Node.js的包管理器）
npm --version

# 查看安装路径
which node    # macOS/Linux
where node    # Windows
```

**预期输出**：

```
v20.18.0  # 或v18.x.x、v22.x.x等LTS版本
10.9.0   # npm版本号（可能不同）
/usr/local/bin/node    # macOS/Linux安装路径
C:\Program Files\nodejs\node.exe  # Windows安装路径
```

**✅ 成功标志**：

- 显示Node.js版本号（≥v18）
- 显示npm版本号
- 显示安装路径

**❌ 失败表现**：

```
'node' 不是内部或外部命令
# 或
command not found: node
```

**🔧 解决方法**：

- **Windows**：
  - 方法1：重启PowerShell（让环境变量生效）
  - 方法2：手动添加Node.js到PATH（见FAQ）
- **macOS/Linux**：
  - 方法1：重启终端
  - 方法2：检查 `/usr/local/bin`是否在PATH中：`echo $PATH`

**💡 小贴士**：如果版本号低于v18，建议卸载后重新安装最新LTS版本。

---

**📍 检查点**：在继续之前，请确认：

- [ ] Node.js已成功安装
- [ ] 版本号 ≥ v18（推荐v20.x.x）
- [ ] npm也已安装
- [ ] 在命令行中执行 `node --version`能正常显示版本号

如果未通过检查点，请查阅《04_常见问题FAQ.md》。

---

## 🚀 步骤3：安装Claude Code CLI

### 3.1 安装 Claude Code（推荐本地安装方式）

**操作说明**：优先使用 Claude Code 官方推荐的本地安装方式。

#### 方式A：官方推荐（优先）

**Windows（PowerShell）**：

```powershell
irm https://claude.ai/install.ps1 | iex
```

**macOS / Linux（Terminal）**：

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

#### 方式B：Windows 备选（winget）

```powershell
winget install Anthropic.ClaudeCode
```

#### 方式C：兼容旧环境（仅备选）

```bash
npm install -g @anthropic-ai/claude-code
```

**✅ 成功标志**：

- 安装流程无报错
- 执行 `claude --version` 能输出版本号

**❌ 常见失败表现**：

```
'claude' 不是内部或外部命令
# 或
command not found: claude
```

**🔧 解决方法**：

- 先重开终端再执行 `claude --version`
- Windows 先确认 `git --version` 正常（Git Bash 是常见依赖）
- 如果方式A失败，再尝试方式B；仍失败再用方式C

---

### 3.2 验证Claude Code安装

**操作说明**：检查Claude Code是否安装成功。

```bash
# 查看Claude Code版本
claude --version

# 查看帮助信息
claude --help

# 查看安装路径
which claude    # macOS/Linux
where claude    # Windows
```

**预期输出**：

```
claude-code version 2.1.2  # 或其他版本号

Usage: claude [options] [command]

Options:
  -V, --version          output the version number
  -h, --help             display help for command
  ...

/usr/local/bin/claude    # macOS/Linux安装路径
C:\Users\YourName\...\claude.exe 或 claude.cmd  # Windows安装路径（以实际安装方式为准）
```

**✅ 成功标志**：

- 显示版本号（如2.1.2）
- 显示帮助信息
- 显示安装路径

**❌ 失败表现**：

```
'claude' 不是内部或外部命令
# 或
command not found: claude
```

**🔧 解决方法**：

- **方法1**：重开终端/PowerShell，再次执行 `claude --version`
- **方法2（Windows）**：确认 Git 正常：
  ```powershell
  git --version
  ```
- **方法3（Windows）**：如果 Git 已安装但仍报错，可指定 Git Bash 路径后再试：
  ```powershell
  $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
  claude --version
  ```
- **方法4**：官方安装失败时，改用 `winget install Anthropic.ClaudeCode`
- **方法5（备选）**：仍失败时再使用 npm 兼容安装

**💡 小贴士**：如果安装路径不在PATH中，你需要手动添加。这是最常见的问题。

---

### 3.3 安装 Visual Studio Code

**操作说明**：安装 VS Code，方便你通过图形界面使用 Claude Code。

#### Windows/macOS/Linux 通用步骤

1. 打开官网：https://code.visualstudio.com/
2. 点击下载按钮，选择与你系统匹配的安装包
3. 双击安装包并按默认选项安装
4. 安装完成后，打开 VS Code

**✅ 成功标志**：

- VS Code 能正常启动
- 能看到左侧活动栏（资源管理器、搜索、扩展等图标）

**❌ 失败表现**：

- 安装包无法运行
- 打开后闪退或卡死

**🔧 解决方法**：

- 重新下载安装包（避免损坏）
- 关闭杀毒软件后重试安装
- Windows 使用“以管理员身份运行”安装程序

---

### 3.4 在 VS Code 安装 Claude Code 插件

**操作说明**：在 VS Code 扩展市场安装 Claude Code 插件，后续可在对话窗口中直接使用。

1. 打开 VS Code，点击左侧“扩展”（或按 `Ctrl+Shift+X` / `Cmd+Shift+X`）
2. 在搜索框输入：`Claude Code for VS Code`
3. 选择发布者为 **Anthropic** 的 Claude Code 扩展
4. 点击“Install/安装”
5. 安装后按提示重载窗口（Reload）

**✅ 成功标志**：

- 扩展状态显示“已安装”
- VS Code 侧边栏或命令面板中可看到 Claude Code 入口

**首次使用建议**：

- 打开命令面板（`Ctrl+Shift+P` / `Cmd+Shift+P`）
- 输入 `Claude`，执行 Claude Code 相关命令
- 选择使用本机已安装的 Claude Code CLI（推荐）

**💡 小贴士**：如果扩展搜索不到，先检查网络，再尝试把关键词改为 `Anthropic` 或 `Claude` 重新搜索。

---

**📍 检查点**：在继续之前，请确认：

- [ ] Claude Code CLI已成功安装
- [ ] 执行 `claude --version`能显示版本号
- [ ] 执行 `claude --help`能显示帮助信息
- [ ] （Windows）`git --version` 正常
- [ ] VS Code 已安装并可正常打开
- [ ] VS Code 中已安装 Claude Code 插件

如果未通过检查点，请查阅《04_常见问题FAQ.md》。

---

## 🔑 步骤4：准备模型 API Key（以智谱GLM为示例）

### 4.1 注册/登录模型平台（示例：智谱开放平台）

**操作说明**：访问智谱AI开放平台，注册或登录账号。

1. 打开浏览器，访问：https://open.bigmodel.cn/
2. 首页右上角有"登录/注册"按钮
3. **注册账号**（如果没有账号）：
   - 点击"注册"
   - 输入手机号
   - 获取并输入验证码
   - 设置密码
   - 完成注册
4. **登录账号**：
   - 输入手机号和密码
   - 点击"登录"

**✅ 成功标志**：

- 成功登录到智谱AI开放平台
- 看到控制台界面

**💡 小贴士**：

- 建议使用常用手机号注册（方便找回密码）
- 新用户有免费额度，足够测试使用
- 记住你的账号密码，后续还需要使用

---

### 4.2 获取API Key

**操作说明**：在智谱AI控制台中获取API Key。

1. **进入控制台**：

   - 登录后，点击右上角"控制台"
   - 或访问：https://open.bigmodel.cn/usercenter/apikeys
2. API密钥管理页面

   - 页面标题："API密钥"
   - 显示已有的API Key列表（如果有的话）
3. **创建新的API Key**：

   - 点击"创建API Key"或"新建API Key"按钮
   - 弹出一个对话框
   - 输入API Key的名称（可选，如"Claude Code"）
   - 点击"确定"或"创建"
4. **复制API Key**：

   - 显示新创建的API Key
   - 格式类似：`xxxxxxxx.xxxxxxxxxxxx.xxxxxxxxxxxx`
   - **⚠️ 重要**：立即复制并保存这个API Key！
   - 关闭对话框后，将无法再次查看完整的API Key
5. **保存API Key**：

   - 建议保存到安全的地方（如密码管理器）
   - 或创建一个文本文件保存：
     ```bash
     # Windows
     echo sk-xxxxxxxx.xxxxxxxxxxxx.xxxxxxxxxxxx > %USERPROFILE%\zhipu_api_key.txt

     # macOS/Linux
     echo sk-xxxxxxxx.xxxxxxxxxxxx.xxxxxxxxxxxx > ~/zhipu_api_key.txt
     ```

**✅ 成功标志**：

- 成功创建API Key
- 已复制并保存API Key

**图示参考（GLM API Key）**
![智谱控制台入口](/images/claude-guide/glm-console-entry.png)
![添加新 API Key](/images/claude-guide/glm-add-api-key.png)
![复制 API Key](/images/claude-guide/glm-copy-api-key.png)

**❌ 失败表现**：

- 提示"账户余额不足"
- 提示"实名认证未完成"

**🔧 解决方法**：

- **余额不足**：新用户有免费额度，如果提示不足，需要充值（建议先充值100元测试）
- **实名认证**：按照提示完成实名认证（需要身份证）

**⚠️ 重要警告**：

- **绝对不要泄露你的API Key**！
- 不要在公共场所、社交媒体、公开代码仓库中暴露API Key
- 如果API Key泄露，立即删除并重新创建
- 不要将API Key提交到Git仓库

---

### 4.3 充值建议（可选）

**操作说明**：如果免费额度用完，需要充值。

1. 在控制台中找到"充值"或"余额管理"页面
2. 选择充值金额（建议先充值100元测试）
3. 选择支付方式（支付宝、微信等）
4. 完成支付

**💡 费用说明**：

- GLM计费会随模型版本与策略更新而调整
- 具体单价请以平台实时公示为准，不要按旧截图做预算
- 建议先小额充值验证链路，再根据使用频率决定订阅或按量

---

**📍 检查点**：在继续之前，请确认：

- [ ] 已成功注册/登录模型平台（示例：智谱开放平台）
- [ ] 已创建API Key
- [ ] 已复制并保存API Key到安全的地方
- [ ] 知道API Key的位置（文件路径或密码管理器）

---

## ⚙️ 步骤5：用 Coding Tool Helper 自动接入 GLM（必做）

> 这一节是本课程的关键：你必须学会用 `coding-tool-helper` 把 GLM 接入 Claude Code。
> 这是对小白最友好的方式，避免手工改配置文件出错。
>
> 官方参考：`https://docs.z.ai/devpack/extension/coding-tool-helper`

### 5.1 一条命令启动工具（推荐）

在终端执行：

```bash
npx @z_ai/coding-helper
```

如果你未来会频繁使用，也可全局安装（可选）：

```bash
npm install -g @z_ai/coding-helper
coding-helper
```

**✅ 成功标志**：

- 终端出现 `Coding Tool Helper` 的交互界面
- 可以用键盘方向键选择，用回车确认

### 5.2 按向导一步步配置（照着选即可）

进入向导后，按这个顺序操作：

1. 选择界面语言（中文）
2. 选择 Coding Plan / GLM 方案
3. 粘贴你在步骤4拿到的 GLM API Key
4. 选择要管理的工具：`Claude Code`
5. 确认自动写入配置

> 小白提示：你只需要“方向键 + 回车”，不用记复杂参数。

### 5.3 配置完成后自检

向导结束后，执行：

```bash
claude --version
claude
```

如果正常进入交互界面，并且能收到回复，说明接入成功。

### 5.4 如果向导失败，先做这3件事

1. 关闭终端，重开后再次执行：`npx @z_ai/coding-helper`
2. 检查 Node.js 版本（需18+）：`node -v`
3. 确认 API Key 可用且未复制错（避免前后空格）

### 5.5 手动配置（仅作为备用）

如果你临时无法使用 `coding-tool-helper`，再使用手动方式：

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "你的GLM_API_KEY",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/paas/v4/",
    "ANTHROPIC_MODEL": "glm-4.7"
  }
}
```

文件路径：

- Windows：`%USERPROFILE%\.claude\settings.json`
- macOS/Linux：`~/.claude/settings.json`

**📍 检查点（本节完成标准）**：

- [ ] 已成功运行 `npx @z_ai/coding-helper`
- [ ] 已在向导中完成 GLM + Claude Code 配置
- [ ] 执行 `claude` 可以正常进入会话

---

## 🔁 步骤5.6：安装 CC Switch（第二堂课前必须）

> 作用：后续切换模型服务时，不用手改配置文件，直接点选切换。

项目地址：`https://github.com/farion1231/cc-switch`

### 安装方式（按系统）

- Windows：到 Releases 下载 `Windows.msi` 或便携版zip
- macOS（Homebrew推荐）：

```bash
brew tap farion1231/ccswitch
brew install --cask cc-switch
```

- Linux：到 Releases 下载 `.deb` / `.rpm` / `.AppImage` / `.flatpak`

### 上手最小步骤

1. 打开 CC Switch，点击“Add Provider”
2. 添加你要的供应商配置
3. 点击“Enable”启用
4. 重启终端或 Claude Code 让配置生效

> 当前课程先用 GLM 跑通主链路；CC Switch 是后续扩展模型的标准工具。

## 🧪 步骤6：测试Claude Code

### 6.1 启动Claude Code

**操作说明**：在终端/命令行中启动Claude Code。

```bash
# 启动Claude Code交互式会话
claude
```

**预期输出**：

```
Initializing Claude Code...
Connected to model: glm-4.7

You are now connected to Claude Code!
Type your message and press Enter to send.
Type /exit or Ctrl+C to exit.

You: _
```

**✅ 成功标志**：

- 显示"Connected to model: glm-4.7"（或你配置的模型）
- 能看到 `You:`提示符，等待输入

**图示参考（Windows）**
![运行 claude 启动](/images/claude-guide/claude-run.png)
![进入交互界面](/images/claude-guide/claude-interactive.png)

**❌ 失败表现**：

```
Error: ANTHROPIC_AUTH_TOKEN not set
# 或
Error: Failed to connect to API server
# 或
Error: 401 Unauthorized
```

**🔧 解决方法**：

- **错误1（Token未设置）**：
  - 检查 `settings.json`文件路径是否正确
  - 检查配置文件是否正确加载
- **错误2（连接失败）**：
  - 检查网络连接
  - 检查 `ANTHROPIC_BASE_URL`是否正确
- **错误3（401错误）**：
  - 检查API Key是否正确
  - 检查API Key是否已过期或被禁用
  - 登录智谱AI平台检查API Key状态

---

### 6.2 发送测试消息

**操作说明**：在Claude Code中发送一条测试消息。

在 `You:`提示符后输入：

```
你好，请介绍一下你自己。
```

按**回车键**发送消息。

**预期输出**：

```
You: 你好，请介绍一下你自己。

Assistant: 你好！我是智谱AI开发的人工智能助手GLM（General Language Model）。我可以帮助您回答问题、提供信息、进行对话交流等。请问有什么可以帮助您的吗？
```

**✅ 成功标志**：

- 能正常发送消息
- 能收到AI的回复
- 回复内容正常（不是乱码或错误信息）

**❌ 失败表现**：

```
Error: Request timeout
# 或
Error: 500 Internal Server Error
# 或
[长时间无响应]
```

**🔧 解决方法**：

- **超时错误**：
  - 检查网络连接
  - 尝试重新发送消息
- **服务器错误**：
  - 可能是智谱AI服务器临时故障
  - 等待几分钟后重试
- **无响应**：
  - 按 `Ctrl+C`退出，重新启动 `claude`
  - 检查API配置是否正确

---

### 6.3 退出Claude Code

**操作说明**：退出Claude Code交互式会话。

**方法1**：输入退出命令

```
/exit
```

**方法2**：使用快捷键

- 按 `Ctrl+C`（Windows/Linux/macOS通用）

**预期输出**：

```
Exiting Claude Code...
Goodbye!
```

**✅ 成功标志**：

- 成功退出
- 返回到命令行提示符

---

**📍 检查点**：在继续之前，请确认：

- [ ] Claude Code能正常启动
- [ ] 能发送测试消息并收到回复
- [ ] AI的回复内容正常
- [ ] 能正常退出Claude Code

如果未通过检查点，请查阅《04_常见问题FAQ.md》。

---

## 🎉 恭喜！

如果你已经：

- ✅ 完成了所有步骤
- ✅ 通过了所有检查点
- ✅ 看到了预期的成功标志

**那么你已经成功完成了Claude Code的安装和配置！** 🎊

### 你现在拥有：

1. ✅ **Node.js运行环境**（v20.x.x或更高）
2. ✅ **Git for Windows**（Windows学员，Git Bash 可用）
3. ✅ **Claude Code CLI工具**（已安装并配置）
4. ✅ **Visual Studio Code**（可视化工作台）
5. ✅ **VS Code Claude Code 插件**（对话窗口可用）
6. ✅ **智谱AI模型接入**（通过 Coding Tool Helper 配置成功）
7. ✅ **CC Switch**（后续切换模型准备完成）

### 你可以：

- 💬 通过命令行与AI对话
- 📄 让AI读取和处理本地文件
- 🔧 使用MCP工具扩展功能
- 🚀 开始构建你的AI工作流

---

## 📚 下一步

**下一步**：请继续阅读《03_环境验证清单.md》

接下来请用环境验证清单做一次完整联调。完成后，你将拥有两类可用入口：

- **Cherry Studio**：适合可视化操作、知识库管理、Skill开发
- **Claude Code（CLI + VS Code 插件）**：适合命令行与对话窗口双入口协作

---

## ❓ 常见问题快速链接

如果在安装过程中遇到问题，可以先查阅《04_常见问题FAQ.md》，也可以快速浏览“参考教程及官方文档“推荐资源排查安装步骤是否准确。

---

## 🆘 如果以上都无法解决

如果FAQ中没有你遇到的问题，可以使用**终局方案**：截图求助AI。

在使用终局方案前，建议先做两件事：

1. 在学员群留言，说明你卡住的步骤和报错信息
2. 在微信公众号、B站等平台搜索关键词：`claude code 安装`
   上面有大量图文与视频安装教程，可用于交叉排查

**如何截图求助**：

1. 截取完整的错误信息（不要只截一半）
2. 打开网页版AI工具：
   - 智谱开放平台帮助中心：https://open.bigmodel.cn/
   - 你常用的通用AI问答工具（任选其一）
3. 使用以下提示词模板：

```
我在安装Claude Code并接入模型API时遇到了错误，请帮我分析原因并提供解决方案。

我的操作系统：[Windows 10/Mac macOS 13/Ubuntu 20.04]
我在执行的步骤：[简述你正在做什么，如"执行claude命令时"]
错误信息：[粘贴错误信息或截图描述]

我的配置文件内容：
[粘贴settings.json的内容，记得隐藏API Key]

请提供详细的解决步骤，谢谢！
```

**⚠️ 注意**：不要泄露你的API Key！粘贴配置文件时，可以用 `sk-***`代替完整的API Key。

---

**祝你安装顺利！** 🚀
