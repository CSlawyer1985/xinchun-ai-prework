# 新春AI工作坊课前指引站点

这是基于 VitePress 的学员查阅站。

## 本地预览

```bash
npm install
npm run docs:dev
```

## 构建

```bash
npm run docs:build
npm run docs:preview
```

## 部署到 GitHub Pages

1. 在 GitHub 创建仓库（例如 `xinchun-ai-prework`）。
2. 将本目录内容推送到该仓库 `main` 分支。
3. 在仓库 Settings -> Pages 中，Build and deployment 选择 `GitHub Actions`。
4. 推送后会自动触发 `.github/workflows/deploy.yml`。

> 说明：配置中会自动识别仓库名并设置 `base`，支持普通仓库 pages 和 `username.github.io` 两种模式。
