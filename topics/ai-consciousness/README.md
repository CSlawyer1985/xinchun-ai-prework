# AI 有意识吗？—— 证据专题

线上：https://legalagi.cn/tools/ai-consciousness/ （镜像 https://cslawyer1985.github.io/xinchun-ai-prework/tools/ai-consciousness/）

## 目录
- `data/evidence.src.py` —— **唯一需要手改的数据源**（每条证据一个 `e(...)`）；运行后生成 `data/evidence.json`
- `sources/raw/` —— 原文存档（txt），`archive` 字段指向这里
- `sources/SOURCES.md` —— 来源清单（构建时自动生成，含访问日期）
- `template/index.template.html` —— 页面模板（样式/动效/交互），数据在构建时注入
- `inbox/` —— 每月扫描得到的**候选**材料，人工核验后才进入 evidence
- `scripts/build.py` —— 校验 + 生成 `docs/public/tools/ai-consciousness/index.html`

## 字段
id, cat(origin/school/definition/theory/test/llm/stance/ethics), stance(yes/no/open/na), person, role, date, quote(原文), zh(编者译), src, url, type, status(原文核实/转述/二手核对/待核实), archive, accessed, note(可选), schools(在文件末尾 S 映射里设置：sym 符号主义 / con 连接主义 / beh 行为主义)

## 新增材料 → 重建
1. 打开原始来源，复制**原文**；把全文存为 `sources/raw/<名>.txt`（首行写来源 URL 与访问日期）。
2. 在 `data/evidence.src.py` 的 `# ---- 三大流派支线` 之前追加一条 `e(...)`；如属某流派，在 `S={...}` 中加上 `"id":["con"]`。
3. 没有可靠出处的不收；只能转引的写 `status="二手核对（…）"`。
4. 仓库根目录执行：`python3 topics/ai-consciousness/scripts/build.py --check-links`
5. 本地预览 `docs/public/tools/ai-consciousness/index.html`，然后 `git add -A && git commit -m "ai-consciousness: 新增 xx" && git push`；GitHub Actions 自动部署。

## 每月扫描（建议流程）
扫描只把候选写进 `inbox/YYYY-MM.md`（标题、链接、原文摘录、为何相关），**不直接改页面**；人工按上面步骤核验后再入库重建。建议关键词：AI consciousness / LLM sentience / model welfare / introspection / IIT GWT test / 意识 大模型。


## 影音与引用（第二轮新增）

- `data/media.py`：影音条目 `{id, kind: video|audio|image, title, by, date, yt|mp3|img, url, license, desc, rel, schools, accessed}`。图片只收 PD / CC，文件放 `assets/img/`，build.py 会校验许可与本地文件并复制到 `out/img/`。
- `evidence.src.py` 的引用表 `C`：`{"A": ["B", ...]}` 表示 A 引用或直接讨论 B，用于生成证据网；build.py 校验 id。
- 分类 `define`：问题界定章（Nagel 1974、Block 1995、SEP 意识/感受性）。新增条目必须与界定一致：讨论现象意识；AI 仅限当前连接主义大模型及其 Agent。

### 月度例行新增影音
1. 确认来源权威、链接可达；YouTube 用 oEmbed 核对标题；Commons 图片用 API 查 extmetadata 许可。
2. 追加到 `data/media.py`，`rel` 指向相关证据 id。
3. `python3 scripts/build.py --check-links` 通过后复制到站点并提交。
