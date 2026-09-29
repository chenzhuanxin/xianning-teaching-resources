#!/usr/bin/env bash
# 一键推送到 GitHub。用法：
#   bash push_to_github.sh <你的GitHub用户名> <仓库名>
# 例：
#   bash push_to_github.sh gongqizi0 xianning-edu

set -e

USER_NAME="$1"
REPO_NAME="${2:-xianning-edu}"

if [ -z "$USER_NAME" ]; then
  echo "用法: bash push_to_github.sh <你的GitHub用户名> [仓库名]"
  exit 1
fi

cd "$(dirname "$0")"

echo "==> 目标仓库: https://github.com/${USER_NAME}/${REPO_NAME}"

# 若远程已存在则更新，否则添加
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "https://github.com/${USER_NAME}/${REPO_NAME}.git"
else
  git remote add origin "https://github.com/${USER_NAME}/${REPO_NAME}.git"
fi

echo "==> 推送中（会提示输入用户名和 Token）..."
echo "    提示: 密码栏请填 Personal Access Token，不是账号密码"
git push -u origin main

echo ""
echo "==> 推送完成！"
echo ""
echo "下一步（可选）：开启 GitHub Pages，让 index.html 变成可访问的网址"
echo "  仓库页 -> Settings -> Pages -> Source 选 'Deploy from a branch'"
echo "  Branch 选 'main'，目录选 '/ (root)'，保存"
echo "  稍等 1-2 分钟后访问: https://${USER_NAME}.github.io/${REPO_NAME}/"
