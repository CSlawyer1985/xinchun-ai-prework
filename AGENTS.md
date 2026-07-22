# 网站域名与部署架构

## 本项目定位

- 站点：四明山法师 AI 夜校
- 正式域名：`https://legalagi.cn/`
- `www` 别名：`https://www.legalagi.cn/`
- GitHub 仓库：`CSlawyer1985/xinchun-ai-prework`
- Cloudflare Pages 项目：`xinchun-ai-prework`
- 构建目录：`docs/.vitepress/dist`
- 生产发布：推送 `main` 分支后，由 Cloudflare Pages 自动构建和部署
- `npm run docs:build` 已在项目内部固定注入 `SITE_URL=https://legalagi.cn`，其优先级高于 Cloudflare 外层遗留的旧环境值

`legalagi.cn` 是本项目唯一 canonical 和访问域名。页面 canonical、Open Graph、JSON-LD、sitemap、robots 及站内绝对链接均应使用该域名。`course.legalagi.cn` 已停用并从 Cloudflare Pages 与 DNS 中移除，不得恢复或写入新的页面、导航及 SEO 数据。

## 整体网站体系

| 正式入口 | 用途 | GitHub 仓库 | Cloudflare Pages 项目 |
|---|---|---|---|
| `https://chenshi.ai/` | 陈石个人博客 | `CSlawyer1985/blog` | `blog` |
| `https://legalagi.cn/` | 四明山法师 AI 夜校（本项目） | `CSlawyer1985/xinchun-ai-prework` | `xinchun-ai-prework` |
| `https://learn-agent.legalagi.cn/` | Agent 结构学习页 | `CSlawyer1985/agent-structure-dashboard` | `agent-structure-dashboard` |
| `https://claude.legalagi.cn/` | Claude for Legal 中国法适配 | `CSlawyer1985/claude-for-legal-ZH` | `claude-for-legal-zh` |
| `https://wiki.legalagi.cn/` | 法律概念 Wiki | `CSlawyer1985/legalwiki` | `legalwiki` |

## 修改约束

1. 本项目站点根地址统一使用 `https://legalagi.cn/`。
2. 博客链接使用 `https://chenshi.ai/`；其他工具使用上表对应子域名。
3. 不要恢复 `cslawyer1985.github.io` 或 `*.pages.dev` 作为生产入口。
4. 不要关闭或删除 GitHub 仓库及原 GitHub Pages；它们保留为代码仓库和回退入口。
5. 修改域名后必须同步检查 `docs/.vitepress/config.mts`、`docs/public/robots.txt`、导航、Markdown 链接及构建后的 sitemap/canonical。
6. 本地验证命令：`SITE_URL=https://legalagi.cn npm run docs:build`。
7. 推送到 GitHub `main` 后无需手动上传，Cloudflare Pages 会自动构建和部署。
