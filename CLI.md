# The Conn CLI 工具

The Conn 提供了两种 CLI 工具，分别针对 Python 和 Node.js 生态系统，让你可以快速将 The Conn 框架集成到任何项目中。

## 🚀 快速开始

### Python 用户（使用 uvx）

```bash
# 初始化 The Conn 框架到当前目录
uvx theconn init

# 使用特定分支
uvx theconn init --branch=v1.0.0

# 指定目标目录
uvx theconn init --path=./my-project
```

### Node.js 用户（使用 npx）

```bash
# 初始化 The Conn 框架到当前目录
npx theconn-cli init

# 使用特定分支
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
- `--branch` - 指定 GitHub 分支（默认: `main`）
- `--path` - 目标目录（默认: 当前目录）

**创建的目录结构:**
```
.the_conn/
├── ai_prompts/         # AI Prompt 模板系统
├── epics/              # 你的项目 Epic（空）
├── context/
│   ├── global/         # 全局上下文（空）
│   └── epics/          # Epic 专属上下文（空）
├── ai_workspace/       # 临时工作区（空）
├── GUIDE.md            # 使用指南
├── README.md           # 框架文档
└── .version            # 版本信息
```

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
- ✅ 更新 `ai_prompts/`
- ✅ 更新 `GUIDE.md`
- ✅ 更新 `README.md`
- ✅ 更新 `.version`

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
- 🗑️ `ai_prompts/`
- 🗑️ `GUIDE.md`
- 🗑️ `README.md`
- 🗑️ `.version`

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
echo ".the_conn/ai_workspace/" >> .gitignore
```

### 3. 开始使用

阅读 `.the_conn/GUIDE.md` 了解如何使用框架。

### 4. 定期检查更新

```bash
uvx theconn check
```

### 5. 更新框架

```bash
uvx theconn update
```

---

## 📌 版本管理

### 使用特定分支

```bash
# 初始化时指定分支
uvx theconn init --branch=v1.0.0

# 更新到特定分支
uvx theconn update --branch=v2.0.0

# 切换到开发分支
uvx theconn update --branch=develop
```

### 版本文件

框架会在 `.the_conn/.version` 文件中保存版本信息：

```json
{
  "branch": "main",
  "commit": "a1b2c3d4e5f6g7h8i9j0",
  "installed_at": "2025-12-12T10:00:00.000Z",
  "updated_at": "2025-12-12T15:30:00.000Z"
}
```

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

### 问题: "Branch not found"

**原因:** 指定的分支不存在。

**解决方案:**
```bash
# 使用默认分支
uvx theconn init

# 或检查可用分支
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
- [使用指南](.the_conn/GUIDE.md)
- [提交问题](https://github.com/Lockeysama/TheConn/issues)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件
