# The Conn 项目结构

本文档说明 The Conn 项目的目录结构和开发环境配置。

---

## 📁 目录结构

```
TheConn/
├── .the_conn/              # The Conn 框架本身（用于开发和测试）
│   ├── ai_prompts/         # AI Prompt 模板系统
│   ├── GUIDE.md            # 使用指南
│   └── README.md           # 框架说明
│
├── src/                    # 源代码目录
│   ├── python/             # Python 实现
│   │   └── theconn/        # Python 包
│   │       ├── __init__.py
│   │       ├── cli.py      # CLI 入口
│   │       ├── github.py   # GitHub 集成
│   │       ├── version.py  # 版本管理
│   │       └── commands/   # 命令实现
│   │           ├── init.py
│   │           ├── update.py
│   │           ├── uninstall.py
│   │           └── check.py
│   │
│   └── typescript/         # TypeScript/Node.js 实现
│       ├── package.json    # npm 包配置
│       ├── README.md       # npm 包文档
│       ├── bin/            # 可执行文件
│       │   └── theconn.js
│       └── lib/            # 库代码
│           ├── github.js
│           ├── version.js
│           └── commands/
│               ├── init.js
│               ├── update.js
│               ├── uninstall.js
│               └── check.js
│
├── pyproject.toml          # Python 项目配置
├── .mise.toml              # mise 环境管理配置
├── .python-version         # Python 版本锁定
├── .gitignore              # Git 忽略规则
│
├── README.md               # 项目主文档
├── README.zh.md            # 中文说明
├── CLI.md                  # CLI 使用文档
├── PUBLISHING.md           # 发布指南
└── STRUCTURE.md            # 本文件
```

---

## 🛠️ 环境管理

本项目使用 [mise](https://mise.jdx.dev/) 统一管理 Python 和 Node.js 环境。

### 安装 mise

```bash
# macOS
brew install mise

# 或使用 curl
curl https://mise.run | sh
```

### 初始化环境

```bash
# 克隆项目
git clone https://github.com/Lockeysama/TheConn.git
cd TheConn

# 安装所有工具（Python, Node.js, uv）
mise install

# 安装 Python 依赖
mise run install

# 安装 Node.js 依赖
mise run npm-install
```

---

## 🐍 Python 开发

### 依赖管理

```bash
# 同步依赖
mise run install

# 添加新依赖
mise run add requests

# 添加开发依赖
mise run add --dev pytest

# 查看依赖树
mise run tree
```

### 开发和测试

```bash
# 运行 Python CLI
mise run py-cli --help
mise run py-cli init

# 或直接使用 uv
uv run theconn --help

# 测试 init 命令
mise run test-py-init

# 代码格式化
mise run fmt-py

# 代码检查
mise run lint-py
```

### 构建和发布

```bash
# 构建包
mise run build-py

# 发布到 PyPI（详见 PUBLISHING.md）
cd dist
twine upload *
```

---

## 📦 TypeScript/Node.js 开发

### 依赖管理

```bash
# 安装依赖
mise run npm-install

# 或直接使用 npm
cd src/typescript
npm install
```

### 开发和测试

```bash
# 本地链接（全局可用）
mise run npm-link

# 运行 TypeScript CLI
mise run ts-cli --help
mise run ts-cli init

# 或直接使用 node
node src/typescript/bin/theconn.js --help

# 测试 init 命令
mise run test-ts-init

# 取消链接
mise run npm-unlink
```

### 构建和发布

```bash
# 构建包
mise run build-ts

# 发布到 npm（详见 PUBLISHING.md）
cd src/typescript
npm publish --access public
```

---

## 🧪 测试工作流

### 快速测试两个 CLI

```bash
# Python CLI
mkdir -p /tmp/test-py && cd /tmp/test-py
uv run theconn init
uv run theconn check
uv run theconn update
uv run theconn uninstall

# Node.js CLI
mkdir -p /tmp/test-ts && cd /tmp/test-ts
npx @theconn/cli init  # 或使用本地链接的 theconn
theconn check
theconn update
theconn uninstall --yes
```

### 使用 mise 任务

```bash
# 测试 Python CLI
mise run test-py-init

# 测试 TypeScript CLI
mise run test-ts-init
```

---

## 📝 常用 mise 命令

### 查看所有任务

```bash
mise tasks
```

### 依赖管理
- `mise run install` - 安装 Python 依赖
- `mise run npm-install` - 安装 Node.js 依赖
- `mise run add <package>` - 添加 Python 依赖
- `mise run remove <package>` - 移除 Python 依赖

### 开发运行
- `mise run py-cli [args]` - 运行 Python CLI
- `mise run ts-cli [args]` - 运行 TypeScript CLI
- `mise run npm-link` - 本地链接 TypeScript CLI
- `mise run npm-unlink` - 取消本地链接

### 代码质量
- `mise run fmt-py` - 格式化 Python 代码
- `mise run lint-py` - 检查 Python 代码
- `mise run fmt-ts` - 格式化 TypeScript 代码
- `mise run lint-ts` - 检查 TypeScript 代码

### 构建
- `mise run build-py` - 构建 Python 包
- `mise run build-ts` - 构建 TypeScript 包

### 清理
- `mise run clean` - 清理所有构建产物

---

## 🔧 配置文件说明

### pyproject.toml

Python 项目配置文件，定义：
- 包名、版本、依赖
- CLI 入口点：`theconn`
- 构建系统配置

**重要**：包路径指向 `src/python/theconn`

### package.json

Node.js 包配置文件，定义：
- 包名：`@theconn/cli`
- 可执行文件：`bin/theconn.js`
- 依赖：`chalk`, `commander`, `ora`

**位置**：`src/typescript/package.json`

### .mise.toml

mise 环境管理配置，定义：
- 工具版本：`node = "20"`, `uv = "latest"`
- 环境变量
- 开发任务（tasks）

---

## 🚀 发布流程

### 1. 更新版本号

```bash
# Python（手动编辑 pyproject.toml）
# version = "0.2.0"

# Node.js
cd src/typescript
npm version patch  # 或 minor, major
```

### 2. 构建

```bash
mise run build-py
mise run build-ts
```

### 3. 发布

详见 [PUBLISHING.md](PUBLISHING.md)

---

## 💡 开发技巧

### 同时开发两个 CLI

1. **Python CLI**：使用 `uv run theconn` 实时测试
2. **Node.js CLI**：使用 `mise run npm-link` 后全局可用

### 保持代码一致

两个实现应保持功能一致：
- 相同的命令和选项
- 相同的输出格式
- 相同的错误处理

### 版本同步

确保两个包的版本号保持同步：
- `pyproject.toml`: `version = "0.1.0"`
- `src/typescript/package.json`: `"version": "0.1.0"`

---

## 📚 相关文档

- [README.md](README.md) - 项目介绍
- [CLI.md](CLI.md) - CLI 使用指南
- [PUBLISHING.md](PUBLISHING.md) - 发布流程
- [.the_conn/GUIDE.md](.the_conn/GUIDE.md) - 框架使用指南

---

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交变更（确保 Python 和 TypeScript 都测试通过）
4. 推送到分支
5. 创建 Pull Request

---

## ⚠️ 注意事项

1. **路径变更**：如果你是从旧版本迁移，注意路径已从 `src/theconn` 和 `packages/npm-cli` 变更为 `src/python/theconn` 和 `src/typescript`

2. **环境管理**：推荐使用 `mise` 统一管理环境，但也可以单独使用 `uv` 和 `npm`

3. **测试隔离**：测试时使用临时目录（如 `/tmp/test-*`），避免污染项目目录

4. **版本同步**：发布前确保两个包的版本号一致

---

## 📞 获取帮助

如有问题，请：
- 查看 [Issues](https://github.com/Lockeysama/TheConn/issues)
- 阅读文档
- 提交新 Issue
