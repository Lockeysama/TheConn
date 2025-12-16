# The Conn CLI 工具

The Conn 提供了两种 CLI 工具，分别针对 Python 和 Node.js 生态系统，让你可以快速将 The Conn 框架集成到任何项目中。

## 🚀 快速开始

### Python 用户（使用 uvx）

```bash
# 初始化 The Conn 框架到当前目录
uvx theconn init

# 使用特定分支（默认使用 stable 分支）
uvx theconn init --branch=v1.0.0

# 指定目标目录
uvx theconn init --path=./my-project
```

### Node.js 用户（使用 npx）

```bash
# 初始化 The Conn 框架到当前目录
npx theconn-cli init

# 使用特定分支（默认使用 stable 分支）
npx theconn-cli init --branch=v1.0.0

# 指定目标目录
npx theconn-cli init --path=./my-project
```

## 📦 命令列表

### `init` - 初始化框架

将 The Conn 框架集成到你的项目中。

**Python:**
```bash
uvx theconn init [--branch=BRANCH] [--path=PATH]
```

**Node.js:**
```bash
npx theconn-cli init [--branch=BRANCH] [--path=PATH]
```

**选项:**
- `--branch` - 指定 GitHub 分支（默认: `stable`）
- `--path` - 目标目录（默认: 当前目录）

**创建的目录结构:**
```
.the_conn/
├── playbooks/          # AI 操作剧本系统（从 GitHub 下载）
│   ├── core/
│   ├── initialization/
│   ├── planning/
│   ├── context/
│   └── execution/
├── docs/               # 用户文档（从 GitHub 下载）
│   ├── README.md
│   └── GUIDE.md
├── epics/              # 你的项目 Epic（空）
├── context/
│   ├── global/         # 全局上下文（空）
│   └── epics/          # Epic 专属上下文（空）
└── ai_workspace/       # 临时工作区（空）
```

**注意:** 默认从 `stable` 分支下载框架文件，确保稳定性。

---

### `update` - 更新框架

更新框架文件到最新版本（保留你的数据）。

**Python:**
```bash
uvx theconn update [--branch=BRANCH] [--path=PATH]
```

**Node.js:**
```bash
npx theconn-cli update [--branch=BRANCH] [--path=PATH]
```

**选项:**
- `--branch` - 指定 GitHub 分支（默认: 使用当前已安装的分支）
- `--path` - 目标目录（默认: 当前目录）

**更新内容:**
- ✅ 更新 `playbooks/`
- ✅ 更新 `docs/`

**保留内容:**
- 📁 `epics/` - 你的项目规划
- 📁 `context/` - 你的上下文文档
- 📁 `ai_workspace/` - 你的工作区

---

### `uninstall` - 卸载框架

卸载 The Conn 框架（保留用户数据）。

**Python:**
```bash
uvx theconn uninstall [--path=PATH]
```

**Node.js:**
```bash
npx theconn-cli uninstall [--path=PATH] [--yes]
```

**选项:**
- `--path` - 目标目录（默认: 当前目录）
- `--yes` - 跳过确认提示（仅 Node.js）

**删除内容:**
- 🗑️ `playbooks/`
- 🗑️ `docs/`

**保留内容:**
- 📁 `epics/`
- 📁 `context/`
- 📁 `ai_workspace/`

> **注意:** 如果要完全删除框架，请手动删除 `.the_conn` 目录。

---

### `check` - 检查更新

检查是否有新版本可用。

**Python:**
```bash
uvx theconn check [--path=PATH]
```

**Node.js:**
```bash
npx theconn-cli check [--path=PATH]
```

**选项:**
- `--path` - 目标目录（默认: 当前目录）

**输出示例:**
```
🔍 Checking for updates on branch 'main'...

Version Comparison:
  Current: a1b2c3d ✓ Installed
  Latest:  e4f5g6h ✓ Available

⚠️  A new version is available!

Run 'theconn update' to update to the latest version.
```

---

## 🔄 典型工作流

### 1. 初始化新项目

```bash
cd my-awesome-project
uvx theconn init

# 或使用 npx
npx theconn-cli init
```

### 2. 添加到 .gitignore

```bash
# 添加临时工作区
echo ".the_conn/ai_workspace/" >> .gitignore
# 添加框架文件（由 CLI 管理）
echo ".the_conn/playbooks/" >> .gitignore
echo ".the_conn/docs/" >> .gitignore
```

### 3. 开始使用

阅读 `.the_conn/docs/GUIDE.md` 了解如何使用框架。

### 4. 定期更新 CLI 工具

```bash
# Python: 强制重新安装 CLI 工具到最新版本
uvx --force-reinstall theconn --version

# Node.js: 使用最新版本的 CLI 工具
npx theconn-cli@latest --version
```

### 5. 检查框架更新

```bash
uvx theconn check
# 或
npx theconn-cli check
```

### 6. 更新框架内容

```bash
uvx theconn update
# 或
npx theconn-cli update
```

---

## 📌 版本管理

### 使用特定分支

```bash
# 默认使用 stable 分支（推荐）
uvx theconn init

# 使用 main 分支（最新开发版本）
uvx theconn init --branch=main

# 使用特定版本标签
uvx theconn init --branch=v1.0.0

# 更新到特定分支
uvx theconn update --branch=v2.0.0
```

**分支说明:**
- `stable` - 稳定版本（默认，推荐用于生产）
- `main` - 最新开发版本（可能包含未稳定的功能）
- `v*.*.*` - 特定版本标签（用于锁定版本）

### CLI 工具版本管理

The Conn CLI 工具本身也会定期更新。查看和更新 CLI 工具：

**Python (uvx):**
```bash
# 查看当前版本
uvx theconn --version

# 首次使用会自动下载最新版本
uvx theconn init

# 如果本地已有缓存，强制重新安装最新版本
uvx --force-reinstall theconn --version
uvx --force-reinstall theconn init

# 或清除缓存后重新下载
uv cache clean theconn
uvx theconn init
```

**Node.js (npx):**
```bash
# 查看当前版本
npx theconn-cli --version

# 首次使用会自动下载最新版本
npx theconn-cli init

# 如果本地已有缓存，清除缓存后使用最新版本
npm cache clean --force
npx theconn-cli init

# 或直接指定使用最新版本（推荐）
npx theconn-cli@latest init

# 使用特定版本
npx theconn-cli@0.1.6 init
```

**当前版本: 0.1.6**

**💡 提示：** 
- `uvx` 和 `npx` 在首次使用后会缓存下载的包
- 如果发现使用的不是最新版本，使用上述命令强制更新
- 推荐定期运行 `uvx --force-reinstall theconn --version` 或 `npx theconn-cli@latest --version` 检查并更新

---

## 🛠️ 高级用法

### 多项目管理

```bash
# 在不同项目中使用不同分支
cd project-a
uvx theconn init --branch=stable

cd ../project-b
uvx theconn init --branch=experimental
```

### 批量更新

```bash
# 更新所有使用 The Conn 的项目
for dir in projects/*/; do
  uvx theconn update --path="$dir"
done
```

---

## ⚙️ 系统要求

### Python CLI (`theconn`)
- Python >= 3.12
- 自动安装依赖: `click`, `requests`, `rich`

### Node.js CLI (`theconn-cli`)
- Node.js >= 18.0.0
- 自动安装依赖: `chalk`, `commander`, `ora`

---

## 🐛 故障排除

### 问题: CLI 工具版本不是最新的

**原因:** `uvx` 或 `npx` 使用了缓存的旧版本。

**解决方案:**

**Python (uvx):**
```bash
# 方法 1: 使用 --force-reinstall 参数强制重新安装（推荐）
uvx --force-reinstall theconn --version
uvx --force-reinstall theconn init

# 方法 2: 清除缓存
uv cache clean theconn
uvx theconn --version
```

**Node.js (npx):**
```bash
# 方法 1: 指定使用 latest 版本（推荐）
npx theconn-cli@latest --version

# 方法 2: 清除 npm 缓存
npm cache clean --force
npx theconn-cli --version

# 方法 3: 删除 npx 缓存目录
rm -rf ~/.npm/_npx
npx theconn-cli --version
```

---

### 问题: "Branch not found"

**原因:** 指定的分支不存在。

**解决方案:**
```bash
# 使用默认 stable 分支
uvx theconn init

# 或使用 main 分支
uvx theconn init --branch=main

# 检查可用分支
# GitHub 仓库: https://github.com/Lockeysama/TheConn/branches
```

### 问题: "Already initialized"

**原因:** `.the_conn` 目录已存在。

**解决方案:**
```bash
# 如果要更新，使用 update 命令
uvx theconn update

# 如果要重新初始化，先删除旧版本
rm -rf .the_conn
uvx theconn init
```

### 问题: "Network error"

**原因:** 无法连接到 GitHub。

**解决方案:**
- 检查网络连接
- 检查防火墙设置
- 尝试使用代理

---

## 📚 相关链接

- [The Conn 项目主页](https://github.com/Lockeysama/TheConn)
- [使用指南](.the_conn/docs/GUIDE.md)
- [提交问题](https://github.com/Lockeysama/TheConn/issues)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件
