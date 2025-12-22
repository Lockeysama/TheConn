# The Conn CLI 工具

The Conn 提供 CLI 工具，让你快速将框架集成到任何项目中。

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
├── rules/              # 核心规则和约束（从 GitHub 下载）
├── playbooks/          # AI 操作剧本系统（从 GitHub 下载）
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

```bash
# 1. 初始化新项目
cd my-project
uvx theconn init  # 或 npx theconn-cli init

# 2. 添加到 .gitignore
echo ".the_conn/ai_workspace/" >> .gitignore
echo ".the_conn/playbooks/" >> .gitignore
echo ".the_conn/docs/" >> .gitignore

# 3. 开始使用（参阅 .the_conn/docs/GUIDE.md）

# 4. 定期检查更新
uvx theconn check  # 或 npx theconn-cli check

# 5. 更新框架
uvx theconn update  # 或 npx theconn-cli update
```

## ⚙️ 系统要求

- **Python CLI**: Python >= 3.12
- **Node.js CLI**: Node.js >= 18.0.0

## 🐛 常见问题

**Q: CLI 工具不是最新版本？**

```bash
# Python: 强制更新
uvx --force-reinstall theconn --version

# Node.js: 使用最新版
npx theconn-cli@latest --version
```

**Q: 目录已存在？**

```bash
# 使用 update 命令更新
uvx theconn update

# 或删除后重新初始化
rm -rf .the_conn && uvx theconn init
```

**Q: 网络错误？**

检查网络连接和防火墙设置。

## 📚 更多信息

- [项目主页](https://github.com/Lockeysama/TheConn)
- [使用指南](.the_conn/docs/GUIDE.md)
- [提交问题](https://github.com/Lockeysama/TheConn/issues)
