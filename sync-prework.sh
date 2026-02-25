#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC_DIR="$ROOT_DIR/课前指引"
DST_DIR="$ROOT_DIR/docs-site/docs/prework"

mkdir -p "$DST_DIR"

cp "$SRC_DIR/00_课前准备总览.md" "$DST_DIR/00_课前准备总览.md"
cp "$SRC_DIR/01_Cherry_Studio_安装与配置指南.md" "$DST_DIR/01_Cherry_Studio_安装与配置指南.md"
cp "$SRC_DIR/02_Claude_Code_安装与配置指南.md" "$DST_DIR/02_Claude_Code_安装与配置指南.md"
cp "$SRC_DIR/03_环境验证清单.md" "$DST_DIR/03_环境验证清单.md"
cp "$SRC_DIR/04_常见问题FAQ.md" "$DST_DIR/04_常见问题FAQ.md"

echo "课前指引同步完成: $DST_DIR"
