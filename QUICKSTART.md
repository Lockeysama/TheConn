# 快速开始 - 新项目结构

本项目已重构为更清晰的结构，使用 mise 统一管理 Python 和 Node.js 环境。

---

## 🎯 新的目录结构

```
src/
├── python/theconn/     # Python CLI 实现
└── typescript/         # Node.js CLI 实现
```

---

## 🚀 首次设置

### 1. 安装 mise

```bash
# macOS
brew install mise

# 其他系统
curl https://mise.run | sh
```

### 2. 初始化项目

```bash
cd /Users/chenyitao/Documents/git/TheConn

# 安装所有环境（Python 3.12 + Node.js 20 + uv）
mise install

# 安装 Python 依赖
mise run install

# 安装 Node.js 依赖
mise run npm-install
```

---

## 🧪 测试 CLI 工具

### Python CLI

```bash
# 直接运行
uv run theconn --help
uv run theconn init

# 或使用 mise 任务
mise run py-cli --help
mise run py-cli init

# 完整测试
mise run test-py-init
```

### TypeScript CLI

```bash
# 本地链接（推荐）
mise run npm-link
theconn --help  # 现在全局可用

# 或直接运行
mise run ts-cli --help
node src/typescript/bin/theconn.js --help

# 完整测试
mise run test-ts-init

# 取消链接
mise run npm-unlink
```

---

## 📝 常用命令

### 查看所有可用任务

```bash
mise tasks
```

### Python 开发

```bash
mise run install        # 安装依赖
mise run add requests   # 添加依赖
mise run py-cli --help  # 运行 CLI
mise run fmt-py         # 格式化代码
mise run lint-py        # 检查代码
mise run build-py       # 构建包
```

### Node.js 开发

```bash
mise run npm-install    # 安装依赖
mise run npm-link       # 本地链接
mise run ts-cli --help  # 运行 CLI
mise run fmt-ts         # 格式化代码
mise run lint-ts        # 检查代码
mise run build-ts       # 构建包
```

### 清理

```bash
mise run clean  # 清理所有构建产物
```

---

## 📦 发布准备

### 1. 更新版本号

```bash
# Python: 编辑 pyproject.toml
version = "0.2.0"

# Node.js
cd src/typescript
npm version patch  # 0.1.0 -> 0.1.1
```

### 2. 测试

```bash
# Python
mkdir -p /tmp/test-py && cd /tmp/test-py
uv run theconn init
uv run theconn check

# Node.js
mkdir -p /tmp/test-ts && cd /tmp/test-ts
theconn init  # 如果已 npm link
theconn check
```

### 3. 构建

```bash
mise run build-py
mise run build-ts
```

### 4. 发布

详见 [PUBLISHING.md](PUBLISHING.md)

---

## 📚 文档

- [STRUCTURE.md](STRUCTURE.md) - 详细的项目结构说明
- [CLI.md](CLI.md) - CLI 使用文档
- [PUBLISHING.md](PUBLISHING.md) - 发布流程
- [.mise.toml](.mise.toml) - mise 配置（查看所有任务定义）

---

## 🔍 与旧结构的对比

| 旧路径              | 新路径                |
| ------------------- | --------------------- |
| `src/theconn/`      | `src/python/theconn/` |
| `packages/npm-cli/` | `src/typescript/`     |

---

## ⚡ 为什么使用 mise？

1. **统一环境管理**：一个工具管理 Python、Node.js 和其他工具
2. **版本锁定**：团队成员使用相同的工具版本
3. **任务自动化**：预定义的开发任务，简化工作流
4. **跨项目一致性**：所有项目使用相同的工具

---

## ❓ 常见问题

### Q: 我还可以不用 mise 吗？

A: 可以！你仍然可以：
- Python: `uv sync && uv run theconn`
- Node.js: `cd src/typescript && npm install && node bin/theconn.js`

但 mise 提供了更好的开发体验。

### Q: 如何更新 mise 工具版本？

A: 编辑 `.mise.toml` 中的 `[tools]` 部分，然后运行 `mise install`

### Q: 出现 "command not found: theconn" 怎么办？

A: 
- Python CLI: 使用 `uv run theconn` 或 `mise run py-cli`
- Node.js CLI: 先运行 `mise run npm-link`

---

## 🎉 你已经准备好了！

现在你可以：
1. 使用 `mise tasks` 查看所有可用命令
2. 运行 `mise run py-cli --help` 测试 Python CLI
3. 运行 `mise run npm-link && theconn --help` 测试 Node.js CLI
4. 阅读 [STRUCTURE.md](STRUCTURE.md) 了解更多细节

开始构建吧！🚀
