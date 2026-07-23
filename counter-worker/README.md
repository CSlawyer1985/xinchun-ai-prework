# night-counter · 访问计数 Worker

四明山法师 AI 夜校的网站访问计数服务，基于 Cloudflare Workers + KV。

- **PV**：每次访问 +1
- **UV**：按访客 IP 哈希做 30 天去重
- **CORS 白名单**：只接受 `legalagi.cn` 与本地开发源的请求，避免被外部站点刷数
- 数据存在 KV，换域名迁移时把 KV 一起带走，**基数不丢**

## 一次性部署（5 步）

```bash
cd counter-worker

# 1. 登录 Cloudflare（浏览器 OAuth，仅首次）
npx wrangler login

# 2. 创建 KV 命名空间，把返回的 id 填进 wrangler.toml 的 id 字段
npx wrangler kv namespace create COUNTER

# 3. 写入基数（从旧统计迁移过来的起点）
npx wrangler kv key put --binding=COUNTER pv 2046
npx wrangler kv key put --binding=COUNTER uv 2046

# 4. 部署 Worker
npx wrangler deploy

# 5. 把部署输出的 workers.dev URL 填到前端 SiteCounter.vue 的 COUNTER_URL
```

## 本地调试

```bash
npx wrangler dev
```

## 校验

部署后直接 curl：

```bash
curl https://night-counter.<你的子域>.workers.dev/api/counter
# {"pv":2047,"uv":2046}
```

## 调整基数

```bash
npx wrangler kv key put --binding=COUNTER pv <新PV>
npx wrangler kv key put --binding=COUNTER uv <新UV>
```
