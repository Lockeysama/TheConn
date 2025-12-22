# 贡献指南

感谢你考虑为 The Conn 项目做出贡献！🎉

**相关文档：**

- [DEVELOPMENT.md](DEVELOPMENT.md) - 开发环境设置和发布流程
- [README.md](README.md) - 项目介绍

---

## 🚀 快速开始

```bash
# 1. Fork 并克隆
git clone https://github.com/YOUR_USERNAME/TheConn.git
cd TheConn

# 2. 设置开发环境（详见 DEVELOPMENT.md）
mise install
mise run install
mise run npm-install

# 3. 创建分支
git checkout -b feature/your-feature-name

# 4. 开发和测试
mise run py-cli --help
mise run test-py-init

# 5. 提交
git add .
git commit -m "feat: add your feature"
git push origin feature/your-feature-name

# 6. 创建 Pull Request
```

---

## 💡 贡献类型

- **Bug 修复** - 搜索或创建 Issue，然后提交 PR
- **新功能** - 先在 Issue 中讨论，获得确认后再开发
- **文档改进** - 直接提交 PR，通常快速合并
- **代码优化** - 创建 Issue 说明优化点后提交 PR

---

## 📋 代码规范

**Python**: 使用 Ruff 格式化，遵循 PEP 8，添加类型注解

```bash
mise run fmt-py   # 格式化
mise run lint-py  # 检查
```

**TypeScript**: 4 空格缩进，使用 ESM，添加 JSDoc

**提交信息**: 使用 [Conventional Commits](https://www.conventionalcommits.org/)

```
feat(cli): add --verbose flag
fix(init): handle missing directory
docs: update README
```

---

## 🧪 测试

```bash
mise run test-py-init   # Python 测试
mise run test-ts-init   # TypeScript 测试
```

- 新功能必须包含测试
- Bug 修复应添加回归测试
- 确保 Python 和 TypeScript 行为一致

---

## 🔍 Pull Request 清单

提交前确认：

- [ ] 代码已格式化并通过检查
- [ ] 添加了测试且测试通过
- [ ] 更新了相关文档
- [ ] 提交信息符合规范
- [ ] Python 和 TypeScript 功能保持一致

---

## 📞 获取帮助

- 查看 [DEVELOPMENT.md](DEVELOPMENT.md)
- 搜索或创建 [Issue](https://github.com/Lockeysama/TheConn/issues)
- Email: <196349143@qq.com>

---

感谢你的贡献！🚀
