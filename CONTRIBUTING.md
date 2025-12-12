# 贡献指南

感谢你考虑为 The Conn 项目做出贡献！🎉

本文档提供贡献指南，帮助你快速上手。

---

## 📖 文档导航

- **[README.md](README.md)** - 项目介绍（面向用户）
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - 开发指南（面向开发者） ⭐
- **[RELEASING.md](RELEASING.md)** - 发布流程（面向维护者）
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - 本文档

---

## 🚀 快速开始

### 1. Fork 项目

访问 [https://github.com/Lockeysama/TheConn](https://github.com/Lockeysama/TheConn) 并 Fork 到你的账户。

### 2. 克隆仓库

```bash
git clone https://github.com/YOUR_USERNAME/TheConn.git
cd TheConn
```

### 3. 设置开发环境

```bash
# 安装 mise
brew install mise  # macOS
# 或
curl https://mise.run | sh  # Linux/macOS

# 安装所有依赖
mise install
mise run install
mise run npm-install
```

### 4. 创建分支

```bash
git checkout -b feature/your-feature-name
```

### 5. 开发和测试

```bash
# Python CLI
mise run py-cli --help

# TypeScript CLI
mise run npm-link
theconn --help

# 测试
mise run test-py-init
mise run test-ts-init
```

### 6. 提交代码

```bash
git add .
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
```

### 7. 创建 Pull Request

访问你的 Fork 仓库，点击 "New Pull Request"。

---

## 💡 贡献类型

### 🐛 Bug 修复

1. 在 [Issues](https://github.com/Lockeysama/TheConn/issues) 中搜索是否已有相关问题
2. 如果没有，创建新 Issue 描述 Bug
3. Fork 项目并创建分支
4. 修复 Bug 并添加测试
5. 提交 PR 并引用 Issue

### ✨ 新功能

1. 先创建 Issue 讨论功能需求
2. 等待维护者确认后再开始开发
3. Fork 项目并创建分支
4. 实现功能并添加测试
5. 更新文档
6. 提交 PR

### 📝 文档改进

1. 直接 Fork 并修改文档
2. 提交 PR
3. 文档 PR 通常会快速合并

### 🎨 代码优化

1. 创建 Issue 说明优化点
2. 讨论后开始优化
3. 提交 PR

---

## 📋 代码规范

### Python 代码

- 使用 [Ruff](https://github.com/astral-sh/ruff) 进行格式化和检查
- 运行 `mise run fmt-py` 格式化代码
- 运行 `mise run lint-py` 检查代码
- 遵循 PEP 8 风格指南
- 添加类型注解（Type Hints）

### TypeScript 代码

- 使用 4 空格缩进
- 运行 `mise run fmt-ts` 格式化代码（如果配置了）
- 运行 `mise run lint-ts` 检查代码（如果配置了）
- 使用 ESM 模块格式
- 添加 JSDoc 注释

### 提交信息

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**类型（type）**：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更改
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具相关

**示例**：
```
feat(cli): add --verbose flag to init command

Add verbose logging option to see detailed initialization process.

Closes #123
```

---

## 🧪 测试要求

### 测试原则

- 新功能必须包含测试
- Bug 修复应添加回归测试
- 确保 Python 和 TypeScript 实现行为一致

### 运行测试

```bash
# Python CLI 测试
mise run test-py-init

# TypeScript CLI 测试
mise run test-ts-init

# 手动测试
mkdir -p /tmp/test && cd /tmp/test
uv run theconn init
theconn init  # 需要先 npm-link
```

### 测试覆盖

- 测试所有命令（init, update, check, uninstall）
- 测试错误处理
- 测试边界情况

---

## 📚 文档要求

### 代码文档

- Python: 使用 docstring
- TypeScript: 使用 JSDoc

**示例**：

```python
def download_file(url: str, target: Path) -> None:
    """从 URL 下载文件到指定位置。
    
    Args:
        url: 文件 URL
        target: 目标路径
        
    Raises:
        ValueError: URL 无效时
        IOError: 下载失败时
    """
```

```typescript
/**
 * Download a file from URL to target path
 * 
 * @param url - File URL
 * @param target - Target path
 * @throws {Error} If URL is invalid or download fails
 */
async function downloadFile(url: string, target: string): Promise<void> {
  // ...
}
```

### 用户文档

如果功能影响用户使用，需要更新：
- `README.md` - 项目介绍
- `CLI.md` - CLI 使用文档
- `.the_conn/GUIDE.md` - 框架使用指南

---

## 🔍 Pull Request 流程

### 提交前检查清单

- [ ] 代码已格式化
- [ ] 通过所有检查（linting）
- [ ] 添加了必要的测试
- [ ] 测试通过
- [ ] 更新了文档
- [ ] 提交信息符合规范
- [ ] Python 和 TypeScript 功能保持一致（如果涉及）

### PR 描述模板

```markdown
## 描述
简要描述这个 PR 的目的和改动。

## 类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] 文档改进
- [ ] 代码优化
- [ ] 其他

## 变更内容
- 改动 1
- 改动 2

## 测试
说明如何测试这些改动。

## 截图（如果适用）
添加截图或录屏。

## 相关 Issue
Closes #123
```

### 代码审查

- 维护者会审查你的代码
- 可能会要求修改
- 请及时回复评论
- 修改后重新请求审查

---

## 🤝 行为准则

### 我们的承诺

- 尊重所有贡献者
- 欢迎不同观点
- 接受建设性批评
- 关注项目最佳利益

### 不可接受的行为

- 侮辱性/贬损性言论
- 骚扰他人
- 发布他人隐私信息
- 其他不专业行为

### 报告

如果遇到不当行为，请联系项目维护者。

---

## 📞 获取帮助

### 开发问题

1. 查看 [DEVELOPMENT.md](DEVELOPMENT.md)
2. 搜索 [Issues](https://github.com/Lockeysama/TheConn/issues)
3. 创建新 Issue 提问

### 功能讨论

1. 创建 Issue 描述想法
2. 使用 "enhancement" 标签
3. 等待社区讨论

### 联系方式

- GitHub Issues: https://github.com/Lockeysama/TheConn/issues
- Email: 196349143@qq.com

---

## 🎖️ 贡献者

感谢所有贡献者！

<!-- 这里可以添加贡献者列表 -->

---

## 📄 许可证

通过提交 PR，你同意你的贡献遵循项目的 [LICENSE](LICENSE)。

---

## 🙏 感谢

再次感谢你的贡献！每一个 PR 都让 The Conn 变得更好。

Happy Contributing! 🚀
