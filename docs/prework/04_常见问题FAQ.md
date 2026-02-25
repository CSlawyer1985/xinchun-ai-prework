# 常见问题FAQ (Frequently Asked Questions)

**本文档目的**：帮助你快速解决安装和配置过程中遇到的常见问题

**使用方法**：
1. 使用`Ctrl+F`（Windows）或`Cmd+F`（Mac）搜索关键词
2. 按照问题分类查找
3. 按照解决方法逐步尝试

**如果找不到你的问题**：请跳到最后的"截图求助指南"部分。

---

## 📥 目录

1. [课程机制类问题](#课程机制类问题)
2. [安装类问题](#安装类问题)
3. [配置类问题](#配置类问题)
4. [使用类问题](#使用类问题)
5. [平台特定问题](#平台特定问题)
6. [截图求助指南](#截图求助指南)

---

## 📋 课程机制类问题

### 1. 什么是"保证金模式"？

**回答**：
- 本课程是公益课堂，保证金不是学费
- 保证金的作用是帮助大家形成学习约束，认真听课和完成作业
- 退还基础是“按要求完成听课和作业”（更看重完成度，不只看结果好坏）
- 如中途退课，按约定扣除对应额度后退还剩余保证金

---

### 2. 如果我不能完成作业，保证金会怎么处理？

**回答**：
- 课程默认节奏是：周日晚上上课，课后一周完成作业
- 若出现延期或阶段性跟不上，可先在群里同步，按规则处理即可
- 若你决定中途退出，保证金按约定扣减后退还剩余部分
- 具体金额和节点以报名页/学习约定为准

---

### 3. 为什么课程强调“必须听课+必须做作业”？

**回答**：
- 本课程主要受众是法律人，很多同学是技术小白
- 只有“听课+动手练习”并行，才能把抽象概念转成可用能力
- 作业是课堂内容的消化过程，不是额外负担
- 只要持续完成，你会很快形成自己的AI工作流

---

### 4. 课程是怎么安排的？

**回答**：
- 课程结构采用“模型 × 数据 × 算力”
- 核心课共5次，原则上每周一次，安排在周日晚上
- 每次课后给一周时间做作业和体验
- 后续会视情况邀请技术嘉宾加餐（可选）

---

### 5. 我是法律人、技术基础弱，能跟上吗？

**回答**：
- 可以。课程默认按“技术小白也能执行”的方式设计
- 每节课都配法律场景实操（合同审阅、案卷整理、法条检索、文书生成等）
- 不要求你写复杂代码，但要求你按步骤完成练习
- 遇到问题先查文档，再群里求助，按流程都能解决

---

### 6. 需要提前准备哪些模型和网络条件？

**回答**：
- 建议至少准备：
  - 1个国内模型账号（GLM/Kimi/DeepSeek其一，保证可直连）
  - 1个国际模型账号（ChatGPT/Claude/Gemini其一，做能力对比）
- 国际模型通常需要VPN或企业合规出口网络
- 计费上建议：
  - 高频使用优先评估 `Coding Plan`（订阅）
  - 低频/波动任务优先 `PAYG`（按量计费）

---

## 🔧 安装类问题

### 1. Node.js安装失败

**问题表现**：
- Windows：安装向导卡住或报错
- macOS：提示"无法验证开发者"
- Linux：包管理器安装失败

**可能原因**：
1. 网络连接不稳定
2. 杀毒软件阻止
3. 磁盘空间不足
4. 权限不足

**解决方法**：

**方法1：重新下载安装包**
```
1. 删除已下载的安装包
2. 清空浏览器缓存
3. 重新从官网下载：https://nodejs.org/
4. 重新安装
```

**方法2：Windows - 使用管理员权限**
```
1. 右键点击安装包
2. 选择"以管理员身份运行"
3. 完成安装
```

**方法3：macOS - 解除安全限制**
```bash
# 如果提示"无法验证开发者"，在终端执行：
sudo spctl --master-disable

# 安装完成后，重新启用（可选）：
sudo spctl --master-enable
```

**方法4：Linux - 使用nvm安装**
```bash
# 安装nvm（Node Version Manager）
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# 重新加载终端配置
source ~/.bashrc  # 或 source ~/.zshrc

# 使用nvm安装Node.js
nvm install --lts
```

**方法5：使用离线安装包**
- 如果网络问题，可以下载离线安装包（从其他电脑复制）
- 或使用他人已下载好的安装包

**验证安装成功**：
```bash
node --version
npm --version
```

---

### 2. Claude Code安装报错

**问题表现**：
```
'claude' 不是内部或外部命令
# 或
command not found: claude
# 或
安装脚本执行失败
```

**可能原因**：
- 官方安装方式执行失败
- Windows 未安装 Git for Windows（或 Git Bash 不可用）
- PATH 尚未生效（新安装后未重开终端）
- 兼容安装（npm）权限不足或网络异常

**解决方法**：

**方法1：优先使用官方推荐安装方式**

Windows（PowerShell）：
```powershell
irm https://claude.ai/install.ps1 | iex
```

macOS/Linux：
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**方法2：Windows 检查 Git**
```powershell
git --version
```
- 如果报错，先安装 Git for Windows：`https://git-scm.com/download/win`
- 安装后重开 PowerShell 再试 `claude --version`

**方法3：Windows 备选安装（winget）**
```powershell
winget install Anthropic.ClaudeCode
```

**方法4：指定 Git Bash 路径（Windows 兜底）**
```powershell
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
claude --version
```

**方法5：兼容旧环境（npm，最后再用）**
```bash
npm config set registry https://registry.npmmirror.com
npm install -g @anthropic-ai/claude-code
```

---

### 3. Cherry Studio安装失败

**问题表现**：
- Windows：安装向导报错
- macOS：提示"已损坏"或"无法打开"
- Linux：依赖包缺失

**解决方法**：

**方法1：Windows - 关闭杀毒软件**
```
1. 临时关闭Windows Defender或其他杀毒软件
2. 重新运行安装包
3. 安装完成后重新启用杀毒软件
```

**方法2：macOS - 允许来自任何来源**
```bash
# 如果提示"已损坏"，执行：
xattr -cr /Applications/Cherry\ Studio.app

# 或在系统偏好设置中：
# 系统偏好设置 → 安全性与隐私 → 通用
# 点击"仍要打开"
```

**方法3：Linux - 安装依赖**
```bash
# Ubuntu/Debian
sudo apt-get install -f

# 或安装缺失的依赖
sudo apt-get install libgtk-3-0 libnotify4 libnss3 libxss1 libxtst6 xdg-utils libatspi2.0-0 libuuid1 libappindicator3-1 libsecret-1-0

# Fedora
sudo dnf install libXScrnSaver

# Arch Linux
sudo pacman -S gtk3 libnotify nss libxss libxtst xdg-utils libappindicator-gtk3
```

**方法4：使用AppImage（Linux）**
```bash
# 下载AppImage版本
chmod +x cherry-studio-*.AppImage
./cherry-studio-*.AppImage
```

---

### 4. 权限错误

**问题表现**：
```
EACCES: permission denied
Error: EPERM: operation not permitted
```

**解决方法**：

**Windows**：
```powershell
# 以管理员身份运行PowerShell
# 或在文件属性中取消"只读"属性
```

**macOS/Linux**：
```bash
# 使用sudo
sudo [命令]

# 或修改文件权限
chmod +x [文件]

# 或修改目录所有者
sudo chown -R $USER:$USER ~/.npm-global
```

---

### 5. 磁盘空间不足

**问题表现**：
```
Error: ENOSPC: no space left on device
```

**解决方法**：

**方法1：清理磁盘空间**
- Windows：使用"磁盘清理"工具
- macOS：清理"下载"文件夹、 emptied垃圾桶
- Linux：`sudo apt clean`、`sudo journalctl --vacuum-time=3d`

**方法2：检查可用空间**
```bash
# Windows
wmic logicaldisk get name,freespace

# macOS
df -h

# Linux
df -h
```

**方法3：安装到其他目录**
```bash
# 指定安装路径
npm config set prefix '~/path/to/new/location'
```

---

## ⚙️ 配置类问题

### 1. API Key配置失败

**问题表现**：
```
Error: ANTHROPIC_AUTH_TOKEN not set
Error: 401 Unauthorized
```

**解决方法**：

**方法1：检查配置文件是否存在**
```bash
# Windows
dir $env:USERPROFILE\.claude\settings.json

# macOS/Linux
ls -la ~/.claude/settings.json
```

**方法2：检查配置文件内容**
```bash
# Windows
cat $env:USERPROFILE\.claude\settings.json

# macOS/Linux
cat ~/.claude/settings.json
```

**确认内容正确**：
```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "你的API Key",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/paas/v4/",
    "ANTHROPIC_MODEL": "glm-4.7"
  }
}
```

**方法3：检查API Key是否正确**
- 登录智谱AI平台：https://open.bigmodel.cn/
- 检查API Key是否有效
- 重新生成API Key（如果怀疑泄露）

**方法4：检查JSON格式**
- 确保使用英文引号`"`，不是中文引号`""`
- 确保所有括号、逗号都正确
- 使用在线JSON验证工具：https://jsonlint.com/

---

### 2. coding-tool-helper 无法运行或写入失败

**问题表现**：
```bash
npx @z_ai/coding-helper
# 报错：command not found / npm ERR! / 权限错误
```

或运行后没有把配置写入到 Claude Code。

**解决方法**：

**方法1：先检查 Node.js 与 npm**
```bash
node -v
npm -v
```
- 需要 Node.js 18+（建议20+）
- 如果命令不存在，先安装/重装 Node.js

**方法2：重新执行 helper**
```bash
npx @z_ai/coding-helper
```
- 按向导重新选择 GLM 与 Claude Code
- 重新粘贴 API Key（注意前后不要带空格）

**方法3：网络与权限排查**
- 确保网络可访问 `open.bigmodel.cn`
- Windows 建议以管理员身份运行 PowerShell
- macOS/Linux 如遇权限错误，检查当前用户目录写权限

**方法4：确认配置是否写入**
```bash
# Windows
cat $env:USERPROFILE\.claude\settings.json

# macOS/Linux
cat ~/.claude/settings.json
```
应至少包含：
- `ANTHROPIC_AUTH_TOKEN`
- `ANTHROPIC_BASE_URL`
- `ANTHROPIC_MODEL`

**方法5：仍失败时的兜底**
- 临时使用《02_Claude_Code_安装与配置指南.md》中的“手动配置（仅备用）”
- 在学员群反馈完整报错截图与执行命令

---

### 3. 模型列表找不到GLM-4.7

**问题表现**：
- Cherry Studio中找不到GLM-4.7模型
- 模型下拉菜单为空

**解决方法**：

**方法1：手动添加模型**
1. 打开设置 → 模型服务 → 智谱开放平台
2. 点击"管理模型"或"添加模型"
3. 输入模型名称：`glm-4.7` 或 `glm-4.7`
4. 保存

**方法2：刷新模型列表**
1. 退出Cherry Studio
2. 重新启动
3. 检查模型列表

**方法3：检查API权限**
- 登录智谱AI平台
- 检查账户是否有权限使用该模型
- 检查账户余额是否充足

**方法4：使用其他模型**
- 如果GLM-4.7不可用，可以尝试：
  - `glm-4.7`
  - `glm-4-air`
  - `glm-4-flash`

---

### 4. 网络连接超时

**问题表现**：
```
Error: Request timeout
Error: Failed to connect to API server
```

**解决方法**：

**方法1：测试网络连接**
```bash
# Windows
Test-NetConnection open.bigmodel.cn -Port 443

# macOS/Linux
curl -I https://open.bigmodel.cn/
```

**方法2：检查防火墙设置**
- Windows：检查Windows Defender防火墙
- macOS：检查"系统偏好设置 → 安全性与隐私 → 防火墙"
- Linux：检查`ufw`或`iptables`规则

**方法3：检查代理设置**
- 如果使用VPN，尝试关闭
- 如果使用代理，确保配置正确

**方法4：更换网络**
- 尝试使用手机热点
- 或更换Wi-Fi网络

---

### 5. 配置文件位置找不到

**问题表现**：
```
Cannot find module '~/.claude/settings.json'
Error: ENOENT: no such file or directory
```

**解决方法**：

**方法1：创建配置目录**
```bash
# Windows
mkdir $env:USERPROFILE\.claude

# macOS/Linux
mkdir -p ~/.claude
```

**方法2：检查配置文件路径**
```bash
# Windows
echo $env:USERPROFILE\.claude\settings.json

# macOS/Linux
echo ~/.claude/settings.json
```

**方法3：手动创建配置文件**
1. 打开文本编辑器（记事本、VS Code等）
2. 输入配置内容（参考"步骤5.3"）
3. 保存到正确路径

---

### 6. API认证失败

**问题表现**：
```
Error: 401 Unauthorized
Error: Invalid API Key
```

**解决方法**：

**方法1：检查API Key**
- 确认API Key完整复制（不要有多余空格）
- 确认API Key没有过期

**方法2：重新生成API Key**
```
1. 登录智谱AI平台
2. 进入"API密钥管理"
3. 删除旧的API Key
4. 创建新的API Key
5. 更新配置文件
```

**方法3：检查账户状态**
- 登录智谱AI平台
- 检查账户是否正常
- 检查余额是否充足
- 检查是否需要实名认证

---

## 💻 使用类问题

### 1. Claude Code启动失败

**问题表现**：
```
Error: Cannot find module 'xxx'
Error: Command not found: claude
```

**解决方法**：

**方法1：检查Claude Code是否安装**
```bash
which claude    # macOS/Linux
where claude    # Windows
```

**方法2：重新安装**
Windows（PowerShell）：
```powershell
irm https://claude.ai/install.ps1 | iex
```

macOS/Linux：
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

如果官方安装失败，再使用 npm 兼容重装：
```bash
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code
```

**方法3：检查PATH环境变量**
```bash
# Windows
echo $env:PATH

# macOS/Linux
echo $PATH

# 如果claude的路径不在PATH中，手动添加
```

---

### 2. Cherry Studio无法启动

**问题表现**：
- 点击图标无反应
- 启动后立即崩溃
- 提示"运行时错误"

**解决方法**：

**方法1：查看错误日志**
- Windows：`%APPDATA%\cherry-studio\logs`
- macOS：`~/Library/Logs/cherry-studio`
- Linux：`~/.config/cherry-studio/logs`

**方法2：重启应用**
- 完全退出Cherry Studio（包括后台进程）
- 重新启动

**方法3：重置配置**
```bash
# 删除配置文件夹（会清除所有设置）
# Windows
rm -r %APPDATA%\cherry-studio

# macOS
rm -r ~/Library/Application\ Support/cherry-studio

# Linux
rm -r ~/.config/cherry-studio
```

**方法4：更新显卡驱动**
- 如果是GPU相关问题，更新显卡驱动

---

### 3. 消息发送无响应

**问题表现**：
- 发送消息后长时间无响应
- 显示"发送中"但不结束

**解决方法**：

**方法1：检查网络连接**
- 访问其他网站测试网络
- ping智谱AI服务器：`ping open.bigmodel.cn`

**方法2：检查API余额**
- 登录智谱AI平台
- 检查余额是否充足

**方法3：重新发送**
- 取消当前消息（Ctrl+C或点击取消）
- 重新发送

**方法4：重启工具**
- 完全退出工具
- 重新启动
- 重试

---

### 4. 响应内容异常

**问题表现**：
- AI回复乱码
- 回复内容不相关
- 回复中断

**解决方法**：

**方法1：检查模型选择**
- 确认选择的是智谱AI模型
- 尝试切换到其他模型

**方法2：检查提示词**
- 确保提示词清晰明确
- 尝试简化提示词

**方法3：重新发送**
- 有时是临时问题，重新发送即可

**方法4：检查API状态**
- 访问智谱AI平台
- 查看是否有系统公告

---

### 5. 如何切换模型

**Claude Code**：
```bash
# 方法1：启动时指定
claude --model glm-4.7

# 方法2：在配置文件中设置默认模型
# 编辑~/.claude/settings.json
{
  "env": {
    "ANTHROPIC_MODEL": "glm-4.7"
  }
}
```

**Cherry Studio**：
```
1. 打开对话界面
2. 在右侧边栏找到"模型选择"下拉菜单
3. 选择你想要的模型（如GLM-4.7）
```

---

## 🖥️ 平台特定问题

### Windows特定问题

#### WebView2缺失
**问题表现**：
```
Error: WebView2 runtime is required
```

**解决方法**：
1. 下载并安装WebView2 Runtime：
   https://developer.microsoft.com/en-us/microsoft-edge/webview2/
2. 重新启动Cherry Studio

#### PowerShell执行策略
**问题表现**：
```
cannot be loaded because running scripts is disabled on this system
```

**解决方法**：
```powershell
# 以管理员身份运行PowerShell，执行：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### PATH配置问题
**问题表现**：
```
'claude' 不是内部或外部命令
```

**解决方法**：
```powershell
# 方法1：手动添加到PATH
# 1. 搜索"环境变量"
# 2. 编辑环境变量 → 系统变量 → Path
# 3. 添加npm的全局路径（如C:\Users\YourName\AppData\Roaming\npm）

# 方法2：重启PowerShell（让环境变量生效）
```

---

### macOS特定问题

#### 安全设置阻止
**问题表现**：
```
"Cherry Studio"已损坏，无法打开
```

**解决方法**：
```bash
# 方法1：系统偏好设置
# 系统偏好设置 → 安全性与隐私 → 通用
# 点击"仍要打开"

# 方法2：解除隔离
xattr -cr /Applications/Cherry\ Studio.app

# 方法3：允许任何来源（不推荐）
sudo spctl --master-disable
```

#### Homebrew安装问题
**问题表现**：
```
Error: Failed to download install script
```

**解决方法**：
```bash
# 使用国内镜像
/bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"
```

#### zsh vs bash
**问题表现**：
配置文件在bash中生效，但在zsh中不生效

**解决方法**：
```bash
# 如果使用zsh（macOS Catalina及以后默认），编辑.zshrc
nano ~/.zshrc

# 添加PATH配置
export PATH="$PATH:$(npm config get prefix)/bin"

# 保存并重新加载
source ~/.zshrc
```

---

### Linux特定问题

#### 依赖包缺失
**问题表现**：
```
error while loading shared libraries: libxxx.so: cannot open shared object file
```

**解决方法**：
```bash
# Ubuntu/Debian
sudo apt-get install -f

# 或安装缺失的库
sudo apt-get install libgtk-3-0 libnotify4 libnss3 libxss1 libxtst6 xdg-utils

# Fedora
sudo dnf install gtk3 libnotify nss libXScrnSaver libxss libxtst xdg-utils
```

#### 权限问题
**问题表现**：
```
Error: EACCES: permission denied
```

**解决方法**：
```bash
# 使用sudo
sudo [命令]

# 或修改文件/目录所有者
sudo chown -R $USER:$USER ~/.claude
```

#### Wayland vs X11
**问题表现**：
Cherry Studio在Wayland下显示异常

**解决方法**：
```bash
# 强制使用X11
GDK_BACKEND=x11 ./cherry-studio-*.AppImage
```

---

## 🆘 截图求助指南

### 当所有方法都无效时

如果你尝试了以上所有方法都无法解决问题，可以使用**终局方案**：截图求助AI。

### 如何截取有效的错误信息

**1. 截取完整的错误信息**
- ✅ 包括错误代码（如`Error: EACCES`）
- ✅ 包括错误堆栈（如果有）
- ✅ 包括执行的命令
- ❌ 不要只截一半
- ❌ 不要模糊不清

**2. 提供上下文信息**
- 你在做什么操作
- 你已经尝试过的方法
- 你的操作系统和版本

**3. 保护敏感信息**
- ❌ 不要泄露API Key
- ❌ 不要泄露密码
- ❌ 不要泄露个人隐私
- ✅ 截图时用马赛克遮挡敏感信息

---

### 推荐的AI求助工具

**1. Claude（推荐）**
- 网址：https://claude.ai/
- 优点：回复详细、逻辑清晰
- 适合：复杂问题、编程问题

**2. ChatGPT**
- 网址：https://chat.openai.com/
- 优点：知识广泛
- 适合：各类问题

**3. 文心一言**
- 网址：https://yiyan.baidu.com/
- 优点：中文理解好、国内访问快
- 适合：国内用户、中文问题

---

### 提示词模板

**模板1：安装失败**
```
我在安装AI工具时遇到了错误，请帮我分析原因并提供解决方案。

【工具信息】
工具名称：[Claude Code / Cherry Studio]
工具版本：[如果知道]

【我的环境】
操作系统：[Windows 10 / macOS 13 / Ubuntu 20.04]
Node.js版本：[如果安装了]
npm版本：[如果安装了]

【我在做什么】
[详细描述你在执行什么操作，如"执行npm install命令"]

【错误信息】
[粘贴完整的错误信息或截图描述]

【我已尝试的方法】
1. [方法1]
2. [方法2]
3. [方法3]

请提供详细的解决步骤，最好能一步步说明，谢谢！
```

---

**模板2：配置失败**
```
我在配置AI工具接入智谱AI时遇到了错误，请帮我解决。

【工具信息】
工具名称：[Claude Code / Cherry Studio]

【我的配置】
API Key：sk-***[记得隐藏完整Key]
API地址：https://open.bigmodel.cn/api/paas/v4/
模型名称：glm-4.7

【配置文件内容】
[粘贴settings.json的内容，记得隐藏API Key]

【错误信息】
[粘贴完整的错误信息或截图描述]

【我已尝试的方法】
1. 重新生成API Key
2. 检查网络连接
3. [其他方法]

请告诉我可能的原因和解决方法，谢谢！
```

---

**模板3：使用问题**
```
我在使用AI工具时遇到了问题，请帮我解决。

【工具信息】
工具名称：[Claude Code / Cherry Studio]
使用的模型：[GLM-4.7 / 其他]

【我正在做什么】
[详细描述你的操作，如"发送消息"或"上传文档"]

【预期结果】
[你期望发生什么]

【实际结果】
[实际发生了什么，粘贴错误信息]

【环境信息】
操作系统：[Windows 10 / macOS 13 / Ubuntu 20.04]
网络状况：[正常 / 使用VPN / 其他]

请提供解决方法，谢谢！
```

---

### 需要提供的关键信息清单

在求助时，请尽可能提供以下信息：

**必须提供**：
- [ ] 完整的错误信息（文字或截图）
- [ ] 你在执行什么操作
- [ ] 你的操作系统和版本
- [ ] 工具名称和版本（如果知道）

**建议提供**：
- [ ] 你已经尝试过的解决方法
- [ ] 相关的配置内容（记得隐藏敏感信息）
- [ ] 网络状况（正常/VPN/其他）
- [ ] Node.js/npm版本（如果涉及）

**不要提供**：
- [ ] 完整的API Key（用sk-***代替）
- [ ] 密码
- [ ] 个人隐私信息

---

## 📞 联系支持

如果以上方法都无法解决问题：

**1. 学员微信群**
- 在群里提问，附上错误截图
- 助教或其他学员会帮助你

**2. 联系陈石微信**
- 微信号/手机号：13567896937
- 适用于紧急问题、个别沟通、协助排查

---

## 💡 预防问题的小贴士

1. **按顺序操作**：严格按照指南步骤操作，不要跳过
2. **耐心等待**：有些操作（如下载、安装）需要时间，耐心等待
3. **检查网络**：确保网络稳定，建议使用宽带或WiFi
4. **备份配置**：配置完成后，备份配置文件
5. **记录问题**：遇到问题时，记录错误信息，方便排查
6. **及时求助**：不要拖延，遇到问题及时在群里求助

---

**FAQ版本**：v1.0
**最后更新**：2025年2月4日
**维护者**：新春AI工作坊课程组

---

**祝你顺利完成课前准备！** 🚀
