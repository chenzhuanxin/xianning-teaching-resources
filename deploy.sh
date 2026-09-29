#!/usr/bin/env bash
# ============================================================
# 一键推送到 GitHub + 后续 Pages 指引
#
# 用法：
#   bash deploy.sh gongqizi0            # 只填用户名，仓库名默认 xianning-edu
#   bash deploy.sh gongqizi0 my-repo    # 自定义仓库名
#
# 前置条件：已登录 GitHub 并在网页上创建了同名空仓库
#          （或者允许脚本用 Token 自动创建）
# ============================================================

set -e

USER_NAME="$1"
REPO_NAME="${2:-xianning-edu}"

if [ -z "$USER_NAME" ]; then
  echo ""
  echo "  用法: bash deploy.sh <GitHub用户名> [仓库名]"
  echo "  例:   bash deploy.sh gongqizi0"
  echo ""
  exit 1
fi

cd "$(dirname "$0")"

REMOTE_URL="https://github.com/${USER_NAME}/${REPO_NAME}.git"

echo ""
echo "============================================"
echo "  目标仓库 : ${REMOTE_URL}"
echo "  本地分支 : main"
echo "  提交数量 : $(git rev-list --count main)"
echo "  文件数量 : $(git ls-files | wc -l | tr -d ' ')"
echo "============================================"
echo ""

# ---- 1. 配置远程 ----
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
  echo "[1/4] 已更新远程地址"
else
  git remote add origin "$REMOTE_URL"
  echo "[1/4] 已添加远程地址"
fi

# ---- 2. 检查远程仓库是否能访问 ----
echo "[2/4] 检查远程仓库..."
if ! git ls-remote "$REMOTE_URL" >/dev/null 2>&1; then
  echo ""
  echo "  !! 无法访问远程仓库。请先确认："
  echo "     1) 已在 https://github.com/new 创建了名为 '${REPO_NAME}' 的仓库"
  echo "     2) 仓库是 Public（否则需要 Token 才有权限）"
  echo "     3) 账号拼写正确：${USER_NAME}"
  echo ""
  echo "     若要自动创建仓库，可用 GitHub CLI："
  echo "       winget install --id GitHub.cli"
  echo "       gh auth login"
  echo "       gh repo create ${REPO_NAME} --public --source=. --push"
  echo ""
  exit 1
fi
echo "      远程仓库可达 ✓"

# ---- 3. 推送 ----
echo "[3/4] 推送中（需要认证）..."
echo "      ----------------------------------------"
echo "      提示：Password 处请粘贴 Personal Access Token"
echo "      创建地址：https://github.com/settings/tokens"
echo "      （Generate new token (classic)，勾选 repo 权限）"
echo "      ----------------------------------------"
echo ""
git push -u origin main

# ---- 4. 完成 ----
echo ""
echo "[4/4] 推送完成 ✓"
echo ""
echo "============================================"
echo "  仓库地址: https://github.com/${USER_NAME}/${REPO_NAME}"
echo ""
echo "  开启在线访问（GitHub Pages）："
echo "    1. 打开 https://github.com/${USER_NAME}/${REPO_NAME}/settings/pages"
echo "    2. Source 选 'Deploy from a branch'"
echo "    3. Branch 选 'main'，目录选 '/ (root)'，点 Save"
echo "    4. 等 1-2 分钟，访问："
echo "       https://${USER_NAME}.github.io/${REPO_NAME}/"
echo "============================================"
echo ""
