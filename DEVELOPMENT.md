# The Conn 开发指南

本文档面向 The Conn 项目的开发者和贡献者，说明如何设置开发环境、开发流程和项目结构。

> **📖 面向用户？** 请查看 [README.md](README.md) 和 [CLI.md](CLI.md)

---

## 📁 项目结构

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
└── .gitignore              # Git 忽略规则
```

### 架构说明

The Conn 提供两个独立但功能一致的 CLI 实现：

1. **Python CLI** (`theconn`) - 使用 `uvx` 运行，面向 Python 生态系统
2. **TypeScript CLI** (`theconn-cli`) - 使用 `npx` 运行，面向 Node.js 生态系统

两个实现的功能完全相同：

- ✅ `init` - 从 GitHub 下载框架文件并初始化项目
- ✅ `update` - 更新框架文件（保留用户数据）
- ✅ `uninstall` - 卸载框架（保留用户数据）
- ✅ `check` - 检查是否有新版本

---

## 🚀 开发环境设置

### 前置要求

本项目使用 [mise](https://mise.jdx.dev/) 统一管理开发环境。

### 1. 安装 mise

```bash
# macOS
brew install mise

# Linux/macOS (使用 curl)
curl https://mise.run | sh

# 配置 shell（根据你使用的 shell）
echo 'eval "$(mise activate bash)"' >> ~/.bashrc
echo 'eval "$(mise activate zsh)"' >> ~/.zshrc
```

### 2. 克隆项目

```bash
git clone https://github.com/Lockeysama/TheConn.git
cd TheConn
```

### 3. 安装所有环境和依赖

```bash
# 安装 Python 3.12, Node.js 20, uv
mise install

# 安装 Python 依赖
mise run install

# 安装 Node.js 依赖
mise run npm-install
```

### 4. 验证安装

```bash
# 查看所有可用的开发任务
mise tasks

# 测试 Python CLI
mise run py-cli --help

# 测试 TypeScript CLI
mise run npm-link
theconn --help
```

---

## 🐍 Python 开发

### 依赖管理

```bash
# 同步依赖（创建虚拟环境）
mise run install

# 添加新依赖
mise run add requests
mise run add click>=8.0

# 添加开发依赖
mise run add --dev pytest
mise run add --dev ruff

# 移除依赖
mise run remove requests

# 查看依赖树
mise run tree

# 更新 uv.lock
mise run lock
```

### 开发和测试

```bash
# 运行 Python CLI
mise run py-cli --help
mise run py-cli init
mise run py-cli update

# 或直接使用 uv（不需要 mise）
uv run theconn --help
uv run theconn init

# 运行任意 Python 命令
mise run cmd python script.py
```

### 代码质量

```bash
# 格式化代码
mise run fmt-py

# 检查代码（linting）
mise run lint-py

# 运行测试（如果有）
mise run test
```

### 测试 CLI

```bash
# 使用 mise 任务自动测试
mise run test-py-init

# 或手动测试
mkdir -p /tmp/test-py && cd /tmp/test-py
uv run theconn init
ls -la .the_conn/
uv run theconn check
uv run theconn update
uv run theconn uninstall
cd - && rm -rf /tmp/test-py
```

### 构建

```bash
# 构建 Python 包
mise run build-py

# 产物在 dist/ 目录
ls dist/
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
# 本地链接（推荐 - 全局可用）
mise run npm-link
theconn --help

# 运行 TypeScript CLI（不链接）
mise run ts-cli --help
mise run ts-cli init

# 或直接使用 node
node src/typescript/bin/theconn.js --help

# 取消链接
mise run npm-unlink
```

### 代码质量

```bash
# 格式化代码（需要先安装 prettier）
mise run fmt-ts

# 检查代码（需要先安装 eslint）
mise run lint-ts
```

### 测试 CLI

```bash
# 使用 mise 任务自动测试
mise run test-ts-init

# 或手动测试（需要先 npm-link）
mkdir -p /tmp/test-ts && cd /tmp/test-ts
theconn init
ls -la .the_conn/
theconn check
theconn update
theconn uninstall --yes
cd - && rm -rf /tmp/test-ts
```

### 构建

```bash
# 构建 TypeScript 包
mise run build-ts

# 产物在 src/typescript/*.tgz
ls src/typescript/*.tgz
```

---

## 🧪 测试工作流

### 完整测试流程

```bash
# 1. 测试 Python CLI
mise run test-py-init

# 2. 测试 TypeScript CLI
mise run test-ts-init

# 3. 手动验证功能
mkdir -p /tmp/test-all && cd /tmp/test-all

# Python CLI
uv run theconn init --branch=main
uv run theconn check
uv run theconn update
uv run theconn uninstall

# Node.js CLI
theconn init --branch=main  # 需要先 npm-link
theconn check
theconn update
theconn uninstall --yes

cd - && rm -rf /tmp/test-all
```

### 功能一致性检查

确保两个实现行为一致：

```bash
# 输出格式应该相同
uv run theconn --help
theconn --help

# 命令行为应该相同
uv run theconn init --branch=main
theconn init --branch=main

# 错误处理应该相同
uv run theconn init  # 在已初始化的目录
theconn init         # 应该报相同的错误
```

---

## 📝 常用 mise 任务

### 查看所有任务

```bash
mise tasks
```

### 任务分类

#### 依赖管理

- `mise run install` - 安装 Python 依赖
- `mise run npm-install` - 安装 Node.js 依赖
- `mise run add <package>` - 添加 Python 依赖
- `mise run remove <package>` - 移除 Python 依赖

#### 开发运行

- `mise run py-cli [args]` - 运行 Python CLI
- `mise run ts-cli [args]` - 运行 TypeScript CLI
- `mise run npm-link` - 本地链接 TypeScript CLI
- `mise run npm-unlink` - 取消本地链接

#### 测试

- `mise run test-py-init` - 测试 Python CLI init
- `mise run test-ts-init` - 测试 TypeScript CLI init

#### 代码质量

- `mise run fmt-py` - 格式化 Python 代码
- `mise run lint-py` - 检查 Python 代码
- `mise run fmt-ts` - 格式化 TypeScript 代码
- `mise run lint-ts` - 检查 TypeScript 代码

#### 构建

- `mise run build-py` - 构建 Python 包
- `mise run build-ts` - 构建 TypeScript 包

#### 清理

- `mise run clean` - 清理所有构建产物

---

## 🔧 配置文件

### pyproject.toml

Python 项目配置文件：

- 定义包名、版本、依赖
- CLI 入口点：`theconn = "theconn.cli:main"`
- 构建系统：hatchling
- 包路径：`src/python`

### src/typescript/package.json

Node.js 包配置文件：

- 包名：`theconn-cli`
- 可执行文件：`bin/theconn.js`
- 依赖：`chalk`, `commander`, `ora`
- 类型：`"type": "module"` (ESM)

### .mise.toml

mise 环境管理配置：

- 工具版本：
  - `node = "20"` (Node.js 20 LTS)
  - `uv = "latest"` (最新版 uv)
- 环境变量
- 开发任务定义（20+ 任务）

### .python-version

Python 版本锁定：`3.12`

---

## 💡 开发技巧

### 同时开发两个 CLI

1. **Python CLI**：
   - 使用 `uv run theconn` 实时测试
   - 无需安装，直接运行

2. **Node.js CLI**：
   - 使用 `mise run npm-link` 全局可用
   - 修改代码后立即生效

### 保持功能一致

两个实现应该：

- ✅ 支持相同的命令和选项
- ✅ 产生相同的输出格式
- ✅ 使用相同的错误处理
- ✅ 保持相同的版本号

### 版本同步

发布前确保版本号一致：

- `pyproject.toml`: `version = "0.1.0"`
- `src/typescript/package.json`: `"version": "0.1.0"`
- `src/theconn/cli.py`: `@click.version_option(version="0.1.0")`
- `src/typescript/bin/theconn.js`: `.version('0.1.0')`

### 不使用 mise？

完全可以！

**Python 开发：**

```bash
uv sync
uv run theconn --help
```

**Node.js 开发：**

```bash
cd src/typescript
npm install
node bin/theconn.js --help
```

但 mise 提供了更好的开发体验和团队一致性。

---

## 🐛 调试

### Python CLI 调试

```bash
# 添加调试输出
import sys
print(f"Debug: {variable}", file=sys.stderr)

# 使用 pdb
import pdb; pdb.set_trace()

# 查看日志
uv run theconn init 2>&1 | tee debug.log
```

### TypeScript CLI 调试

```bash
# 添加调试输出
console.error('Debug:', variable);

# 使用 node inspect
node --inspect src/typescript/bin/theconn.js init

# 查看日志
theconn init 2>&1 | tee debug.log
```

---

## ⚠️ 注意事项

### 路径变更（从旧版本迁移）

如果你从旧版本迁移：

| 旧路径              | 新路径                |
| ------------------- | --------------------- |
| `src/theconn/`      | `src/python/theconn/` |
| `packages/npm-cli/` | `src/typescript/`     |

### 测试隔离

测试时使用临时目录：

```bash
# ✅ 好
mkdir -p /tmp/test-theconn
cd /tmp/test-theconn

# ❌ 不好
cd ~/projects/my-project  # 可能污染真实项目
```

### Git 提交

提交前检查：

- [ ] Python 和 TypeScript 都测试通过
- [ ] 代码已格式化
- [ ] 版本号已同步（如果修改了）
- [ ] 文档已更新（如果需要）

---

## 📦 发布流程

> 📌 **本节面向项目维护者**

### 发布前检查

- [ ] 所有代码已提交到 Git
- [ ] 版本号已更新（`pyproject.toml` 和 `src/typescript/package.json`）
- [ ] 已在本地测试所有命令
- [ ] Python 和 TypeScript 版本号已同步

### 更新版本号

**Python 包** - 编辑 `pyproject.toml`:

```toml
[project]
version = "0.2.0"  # 更新版本号
```

**Node.js 包**:

```bash
cd src/typescript
npm version patch   # 0.1.0 -> 0.1.1
npm version minor   # 0.1.1 -> 0.2.0
npm version major   # 0.2.0 -> 1.0.0
```

### 发布 Python 包到 PyPI

```bash
# 1. 构建
mise run build-py

# 2. 测试发布到 TestPyPI（推荐）
twine upload --repository testpypi dist/*
uvx --index-url https://test.pypi.org/simple/ theconn --help

# 3. 发布到正式 PyPI
twine upload dist/*

# 4. 验证
uvx theconn --version
```

### 发布 Node.js 包到 npm

```bash
# 1. 测试
cd src/typescript
npm pack --dry-run

# 2. 登录 npm（如果还没登录）
npm login

# 3. 发布
npm publish --access public  # 首次发布
npm publish                   # 后续更新

# 4. 验证
npx theconn-cli --version
```

### 完整发布流程

```bash
# 1. 更新版本号并提交
git add .
git commit -m "chore: bump version to 0.2.0"
git tag v0.2.0
git push origin main
git push origin v0.2.0

# 2. 发布 Python 包
mise run build-py
twine upload dist/*

# 3. 发布 Node.js 包
cd src/typescript
npm publish
```

### 发布后检查

- [ ] PyPI 上能找到新版本
- [ ] npm 上能找到新版本
- [ ] `uvx theconn --version` 显示正确版本
- [ ] `npx theconn-cli --version` 显示正确版本
- [ ] 测试所有命令（init, update, check, uninstall）

---

## 📚 相关文档

- [README.md](README.md) - 项目介绍
- [CLI.md](CLI.md) - CLI 使用文档
- [CONTRIBUTING.md](CONTRIBUTING.md) - 贡献指南

---

## 🤝 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📞 获取帮助

- 查看 [Issues](https://github.com/Lockeysama/TheConn/issues)
- 提交新 Issue

---

## 🎉 开始开发

1. **查看所有任务**：`mise tasks`
2. **测试 Python CLI**：`mise run py-cli --help`
3. **测试 Node.js CLI**：`mise run npm-link && theconn --help`
4. **开始编码**：修改代码并实时测试

Happy Coding! 🚀
