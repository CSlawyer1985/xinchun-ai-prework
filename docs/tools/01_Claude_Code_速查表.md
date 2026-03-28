---
pageClass: claude-cheatsheet-page
outline: [2, 3]
---

# Claude Code 速查表

<div class="cc-guide-hero">
  <p class="cc-guide-hero__eyebrow">Claude Code Reference</p>
  <h1>课堂上手版 · 完整内容速查</h1>
  <p class="cc-guide-hero__lead">依据 <a href="https://cc.jiangrzc.cn/" target="_blank" rel="noreferrer">cc.jiangrzc.cn</a> 公布内容整理，覆盖快捷键、Slash 命令、MCP、记忆、技能、Agents、CLI 与 Flags。当前对照版本更新日期为 2026 年 3 月 24 日。</p>
  <div class="cc-guide-pills">
    <span>完整内容整理</span>
    <span>适合课堂投屏</span>
    <span>便于第一次安装后回查</span>
  </div>
</div>

<div class="cc-guide-nav">
  <a href="#最近更新">最近更新</a>
  <a href="#键盘快捷键">键盘快捷键</a>
  <a href="#mcp-服务器">MCP</a>
  <a href="#slash-命令">Slash 命令</a>
  <a href="#记忆与文件">记忆与文件</a>
  <a href="#工作流与技巧">工作流与技巧</a>
  <a href="#配置与环境变量">配置与环境变量</a>
  <a href="#skills-与-agents">Skills 与 Agents</a>
  <a href="#cli-与-flags">CLI 与 Flags</a>
</div>

## 最近更新

- `--bare`：极简无头模式，不带 hooks、LSP 与插件。
- `--channels`：支持权限转发与 MCP 推送消息。
- `effort` frontmatter：已支持 skills 与 slash commands。
- `/branch`：替代 `/fork`，同时保留别名。
- `SendMessage`：可以自动恢复已停止的 agents。

## 键盘快捷键

### 通用控制

- `Ctrl C`：取消输入或生成。
- `Ctrl D`：退出会话。
- `Ctrl L`：清屏。
- `Ctrl O`：切换详细输出。
- `Ctrl R`：反向搜索历史。
- `Ctrl G`：在编辑器中打开提示词。
- `Ctrl B`：后台运行任务。
- `Ctrl T`：切换任务列表。
- `Ctrl V`：粘贴图片。
- `Ctrl F`：连按两次可杀死后台 agents。
- `Esc Esc`：回退或撤销。

### 模式切换

- `Shift Tab`：循环切换权限模式。
- `Alt P`：切换模型。
- `Alt T`：切换思考模式。

### 输入

- `\Enter`：快速换行。
- `Ctrl J`：控制序列换行。

### 前缀

- `/`：输入 Slash 命令。
- `!`：直接执行 bash。
- `@`：提及文件并自动补全。

### 会话选择器

- `↑↓`：上下导航。
- `←→`：展开或折叠。
- `P`：预览。
- `R`：重命名。
- `/`：搜索。
- `A`：查看全部项目。
- `B`：只看当前分支。

## MCP 服务器

### 添加服务器

- `--transport http`：远程 HTTP，推荐。
- `--transport stdio`：本地进程。
- `--transport sse`：远程 SSE。

### 作用域

- `Local .claude.json`：单项目使用。
- `Project .mcp.json`：团队共享，可进版本库。
- `User ~/.claude.json`：用户全局配置。

### 管理

- `/mcp`：交互式管理界面。
- `claude mcp list`：列出全部 MCP 服务器。
- `claude mcp serve`：把 Claude Code 本身暴露成 MCP 服务器。
- `Elicitation` 服务器：支持在任务中途向用户发起输入请求。

## Slash 命令

### 会话

- `/clear`：清空对话。
- `/compact [focus]`：压缩上下文。
- `/resume`：恢复或切换会话。
- `/rename [name]`：为当前会话命名。
- `/branch [name]`：分叉对话。
- `/cost`：查看 Token 使用统计。
- `/context`：可视化上下文。
- `/diff`：打开交互式 diff 查看器。
- `/copy`：复制上一条回复。
- `/export`：导出对话。

### 配置

- `/config`：打开设置。
- `/model [model]`：切换模型，可配合方向键调 `effort`。
- `/fast [on|off]`：切换快速模式。
- `/vim`：切换 vim 模式。
- `/theme`：更改颜色主题。
- `/permissions`：查看或更新权限。
- `/effort [level]`：设置 effort，支持 `low / med / high / max / auto`。
- `/color [color]`：设置提示栏颜色。
- `/keybindings`：自定义键盘快捷键。
- `/terminal-setup`：配置终端快捷键。

### 工具

- `/init`：创建 `CLAUDE.md`。
- `/memory`：编辑 `CLAUDE.md` 文件。
- `/mcp`：管理 MCP 服务器。
- `/hooks`：管理 hooks。
- `/skills`：列出可用 skills。
- `/agents`：管理 agents。
- `/chrome`：Chrome 集成。
- `/reload-plugins`：热重载插件。
- `/add-dir <path>`：添加工作目录。

### 特殊功能

- `/btw <question>`：提一个不带上下文的侧边问题。
- `/plan [desc]`：进入 Plan 模式并自动开始。
- `/loop [interval]`：安排周期任务。
- `/voice`：按住说话，支持多语言语音输入。
- `/doctor`：诊断安装问题。
- `/pr-comments [PR]`：获取 GitHub PR 评论。
- `/stats`：查看 streak 与偏好。
- `/insights`：分析会话报告。
- `/desktop`：继续到 Desktop 应用。
- `/remote-control` 或 `/rc`：连接 claude.ai/code 远程会话。
- `/usage`：查看套餐限额与速率状态。
- `/schedule`：云端计划任务。
- `/security-review`：做变更的安全分析。
- `/help`：显示帮助与命令总览。
- `/feedback` 或 `/bug`：提交反馈。
- `/release-notes`：查看完整更新日志。
- `/stickers`：申请贴纸。

## 记忆与文件

### CLAUDE.md 位置

- `./CLAUDE.md`：项目级，团队共享。
- `~/.claude/CLAUDE.md`：个人级，对所有项目生效。
- `/etc/claude-code/`：托管级或组织范围。

### 规则与导入

- `.claude/rules/*.md`：项目规则。
- `~/.claude/rules/*.md`：用户规则。
- `paths:` frontmatter：路径专用规则。
- `@path/to/file`：在 `CLAUDE.md` 中导入其他文件。

### 自动记忆

- `~/.claude/projects/<proj>/memory/`：自动记忆目录。
- 其中会维护 `MEMORY.md` 与主题文件，并自动加载。

## 工作流与技巧

### Plan 模式

- `Shift Tab`：普通模式 → 自动接受 → Plan。
- `--permission-mode plan`：以 Plan 模式启动。

### 思考与 Effort

- `Alt T`：开关思考模式。
- `ultrathink`：当前轮次最高 effort。
- `Ctrl O`：查看详细思考过程。
- `/effort`：快速切换低、中、高。

### Git Worktrees

- `--worktree name`：为功能建立独立分支工作区。
- `isolation: worktree`：让 Agent 在独立 worktree 中运行。
- `sparsePaths`：只 checkout 所需目录。
- `/batch`：自动创建多个 worktrees。

### 语音模式

- `/voice`：启用按住说话。
- `Space (hold)`：按住录音，松开发送。
- 支持 20 种语言。

### 上下文管理

- `/context`：查看使用情况与优化建议。
- `/compact [focus]`：带焦点压缩上下文。
- `Auto-compact`：约 95% 容量时自动压缩。
- `1M context`：Opus 4.6 在 Max/Team/Ent 套餐可用。
- `CLAUDE.md`：压缩后仍保留。

### 会话高阶技巧

- `claude -c`：继续最近一次会话。
- `claude -r "name"`：按名称恢复会话。
- `/btw question`：发起不占上下文的侧边问题。

### SDK / 无头模式

- `claude -p "query"`：非交互运行。
- `--output-format json`：结构化输出。
- `--max-budget-usd 5`：设置成本上限。
- `cat file | claude -p`：通过管道输入内容。

### 调度与远程

- `/loop 5m msg`：周期任务。
- `/rc`：远程控制。
- `--remote`：连接 claude.ai 的网页会话。

## 配置与环境变量

### 配置文件

- `~/.claude/settings.json`：用户设置。
- `.claude/settings.json`：项目共享配置。
- `.claude/settings.local.json`：本地私有配置。
- `~/.claude.json`：OAuth、MCP 与状态。
- `.mcp.json`：项目级 MCP 配置。

### 关键设置

- `modelOverrides`：把模型选择器映射到自定义模型 ID。
- `autoMemoryDirectory`：自定义记忆目录。
- `worktree.sparsePaths`：Sparse checkout 目录。

### 关键环境变量

- `ANTHROPIC_API_KEY`
- `ANTHROPIC_MODEL`
- `CLAUDE_CODE_EFFORT_LEVEL`
- `MAX_THINKING_TOKENS`：`0` 表示关闭。
- `ANTHROPIC_CUSTOM_MODEL_OPTION`：自定义 `/model` 条目。
- `CLAUDE_CODE_PLUGIN_SEED_DIR`：多个插件种子目录。
- `CLAUDECODE=1`：检测 Claude Code shell。
- `IS_DEMO`：演示模式，隐藏邮箱与组织信息。
- `CLAUDE_CODE_MAX_OUTPUT_TOKENS`：默认 32K。
- `CLAUDE_CODE_DISABLE_CRON`

## Skills 与 Agents

### 内置 Skills

- `/simplify`：代码审查，支持 3 个并行 agents。
- `/batch`：大规模并行修改，可拉起 5 到 30 个 worktrees。
- `/debug [desc]`：根据调试日志排障。
- `/loop [interval]`：周期性计划任务。
- `/claude-api`：加载 API 与 SDK 参考。

### 自定义 Skill 位置

- `.claude/skills/<name>/`：项目级 skills。
- `~/.claude/skills/<name>/`：个人级 skills。

### Skill Frontmatter

- `description`：自动触发说明。
- `allowed-tools`：跳过权限提示。
- `model`：为 skill 覆盖模型。
- `effort`：覆盖 effort 等级。
- `context: fork`：在 subagent 中运行。
- `$ARGUMENTS`：用户输入占位符。
- `${CLAUDE_SKILL_DIR}`：Skill 自身目录。
- ``!`cmd` ``：动态上下文注入。

### 内置 Agents

- `Explore`：快速只读。
- `Plan`：做 Plan 模式调研。
- `General`：完整工具，适合复杂任务。
- `Bash`：独立上下文终端。

### Agent Frontmatter

- `permissionMode`：支持 `default / acceptEdits / plan / dontAsk / bypass`。
- `isolation: worktree`：在 git worktree 中运行。
- `memory: user|project`：持久记忆。
- `background: true`：后台任务。
- `maxTurns`：限制 agentic 轮数。
- `SendMessage`：恢复 agents，替代 resume。

## CLI 与 Flags

### 核心命令

- `claude`：交互式模式。
- `claude "q"`：带提示词启动。
- `claude -p "q"`：无头执行。
- `claude -c`：继续最近一次。
- `claude -r "n"`：恢复指定会话。
- `claude update`：更新 Claude Code。

### 关键 Flags

- `--model`：设置模型。
- `-w`：Git worktree。
- `-n / --name`：会话名。
- `--add-dir`：添加目录。
- `--agent`：使用 agent。
- `--allowedTools`：预批准工具。
- `--output-format json/stream`
- `--json-schema`：结构化输出。
- `--max-turns`：限制轮数。
- `--max-budget-usd`：成本上限。
- `--console`：通过 Anthropic Console 认证。
- `--verbose`：详细输出。
- `--bare`：极简无头模式。
- `--channels`：权限转发与 MCP 推送。
- `--remote`：连接网页会话。
- `--effort low/med/high/max`
- `--permission-mode plan/default/...`
- `--dangerously-skip-permissions`：跳过所有提示。
- `--chrome`：连接 Chrome。

### 权限模式

- `default`：询问。
- `acceptEdits`：自动接受编辑。
- `plan`：只读。
- `dontAsk`：除允许工具外一律拒绝。
- `bypassPermissions`：跳过全部。
- `--dangerously-skip-permissions`：对应 CLI 参数。
