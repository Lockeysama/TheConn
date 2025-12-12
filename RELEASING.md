# The Conn 发布指南

> 📌 **本文档面向项目维护者**  
> 说明如何测试和发布 The Conn CLI 工具到 PyPI 和 npm。
>
> 开发指南请查看 [DEVELOPMENT.md](DEVELOPMENT.md)

---

## 📦 发布前准备

### 检查清单

- [ ] 所有代码已提交到 Git
- [ ] 版本号已更新（`pyproject.toml` 和 `src/typescript/package.json`）
- [ ] 已在本地测试所有命令
- [ ] 已更新 CHANGELOG（如果有）
- [ ] Python 和 TypeScript 版本号已同步
- [ ] GitHub 仓库已推送到远程

---

## 🐍 发布 Python 包到 PyPI

### 1. 本地测试

```bash
# 确保在项目根目录
cd /Users/chenyitao/Documents/git/TheConn

# 使用 mise 安装依赖
mise install
mise run install

# 测试命令
mise run py-cli --help
mise run py-cli init --help

# 或者直接使用 uv
uv run theconn --help

# 创建测试目录并测试
mkdir -p /tmp/test-theconn
cd /tmp/test-theconn
uv run theconn init
uv run theconn check
uv run theconn update
uv run theconn uninstall
```

### 2. 构建发布包

```bash
cd /Users/chenyitao/Documents/git/TheConn

# 清理之前的构建
rm -rf dist/

# 构建包
mise run build-py
# 或直接使用 uv
uv build
```

### 3. 发布到 PyPI

```bash
# 安装 twine（如果还没有）
uv pip install twine

# 先发布到 TestPyPI 测试（推荐）
twine upload --repository testpypi dist/*

# 测试从 TestPyPI 安装
uvx --index-url https://test.pypi.org/simple/ theconn --help

# 确认无误后，发布到正式 PyPI
twine upload dist/*
```

### 4. 验证发布

```bash
# 从 PyPI 安装并测试
uvx theconn --version
uvx theconn --help
uvx theconn init
```

---

## 📦 发布 Node.js 包到 npm

### 1. 本地测试

```bash
cd /Users/chenyitao/Documents/git/TheConn

# 确保 Node.js 环境已安装
mise install

# 安装依赖
mise run npm-install

# 本地链接测试
mise run npm-link

# 测试命令
theconn --help
theconn init --help

# 或者直接运行
mise run ts-cli --help

# 创建测试目录并测试
mkdir -p /tmp/test-theconn-npm
cd /tmp/test-theconn-npm
theconn init
theconn check
theconn update
theconn uninstall --yes

# 取消链接
mise run npm-unlink
```

### 2. 准备发布

```bash
cd /Users/chenyitao/Documents/git/TheConn/src/typescript

# 确保 package.json 正确
npm run test  # 如果有测试

# 检查要发布的文件
npm pack --dry-run
```

### 3. 登录 npm

```bash
# 如果还没有登录
npm login

# 检查登录状态
npm whoami
```

### 4. 发布到 npm

```bash
cd /Users/chenyitao/Documents/git/TheConn/src/typescript

# 发布（第一次发布 scoped package 需要 --access public）
npm publish --access public

# 后续更新直接发布
npm publish
```

### 5. 验证发布

```bash
# 使用 npx 测试
npx theconn-cli --version
npx theconn-cli --help
npx theconn-cli init
```

---

## 🔄 版本更新流程

### 更新版本号

**Python 包：**

编辑 `pyproject.toml`:
```toml
[project]
version = "0.2.0"  # 更新版本号
```

**Node.js 包：**

```bash
cd src/typescript
npm version patch   # 0.1.0 -> 0.1.1
npm version minor   # 0.1.1 -> 0.2.0
npm version major   # 0.2.0 -> 1.0.0
```

### 同步版本号

确保以下位置的版本号保持一致：
- `pyproject.toml` 中的 `version`
- `src/typescript/package.json` 中的 `version`
- `src/python/theconn/cli.py` 中的 `@click.version_option(version="...")`
- `src/typescript/bin/theconn.js` 中的 `.version(...)`

### 完整发布流程

1. **更新所有版本号**
   ```bash
   # 编辑 pyproject.toml
   version = "0.2.0"
   
   # 更新 Node.js 版本
   cd src/typescript && npm version 0.2.0
   ```

2. **提交代码**
   ```bash
   git add .
   git commit -m "chore: bump version to 0.2.0"
   ```

3. **打标签**
   ```bash
   git tag v0.2.0
   ```

4. **推送到 GitHub**
   ```bash
   git push origin main
   git push origin v0.2.0
   ```

5. **发布 Python 包**
   ```bash
   mise run build-py
   twine upload dist/*
   ```

6. **发布 Node.js 包**
   ```bash
   cd src/typescript
   npm publish
   ```

---

## 🧪 自动化发布（可选）

### GitHub Actions 工作流

创建 `.github/workflows/release.yml`:

```yaml
name: Release Packages

on:
  release:
    types: [published]

jobs:
  publish-pypi:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Install uv
        run: pip install uv
      
      - name: Build package
        run: uv build
      
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: |
          pip install twine
          twine upload dist/*

  publish-npm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          registry-url: 'https://registry.npmjs.org'
      
      - name: Install dependencies
        run: cd src/typescript && npm install
      
      - name: Publish to npm
        run: cd src/typescript && npm publish --access public
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

### 设置 GitHub Secrets

1. **PyPI Token**:
   - 访问 https://pypi.org/manage/account/token/
   - 创建新 token
   - 在 GitHub 仓库设置中添加 `PYPI_API_TOKEN`

2. **npm Token**:
   - 运行 `npm token create`
   - 在 GitHub 仓库设置中添加 `NPM_TOKEN`

---

## 📝 发布后检查清单

- [ ] 在 PyPI 上能找到新版本：https://pypi.org/project/theconn/
- [ ] 在 npm 上能找到新版本：https://www.npmjs.com/package/theconn-cli
- [ ] `uvx theconn --version` 显示正确版本
- [ ] `npx theconn-cli --version` 显示正确版本
- [ ] 测试所有命令（init, update, check, uninstall）
- [ ] 更新 GitHub Release Notes
- [ ] 更新文档中的版本号引用（如果有）
- [ ] 在社交媒体或社区宣布新版本（可选）

---

## 🔧 故障排除

### PyPI 发布失败

#### 问题：文件已存在

```
File already exists
```

**解决方案**：
- 版本号已被使用
- 更新版本号后重新构建
- 不能重复发布相同版本

#### 问题：认证失败

```
Invalid or non-existent authentication
```

**解决方案**：
1. 访问 https://pypi.org/manage/account/token/
2. 创建 API token
3. 使用 token 登录：
   ```bash
   twine upload --username __token__ --password <your-token> dist/*
   ```

### npm 发布失败

#### 问题：没有发布权限

```
You do not have permission to publish
```

**解决方案**：
1. 确认已登录：`npm whoami`
2. 如果是 scoped package，首次发布需要：
   ```bash
   npm publish --access public
   ```

#### 问题：版本已存在

```
Version already exists
```

**解决方案**：
- 更新版本号：`npm version patch`
- 或手动编辑 `package.json`

---

## 📚 相关资源

- [PyPI 官方文档](https://packaging.python.org/tutorials/packaging-projects/)
- [npm 发布文档](https://docs.npmjs.com/cli/v9/commands/npm-publish)
- [Semantic Versioning](https://semver.org/)
- [uv 文档](https://docs.astral.sh/uv/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

---

## ⚠️ 重要提醒

1. **测试优先**：发布前务必在本地和测试环境充分测试
2. **版本同步**：确保 Python 和 Node.js 包版本号一致
3. **备份代码**：发布前确保代码已提交并推送到 GitHub
4. **文档更新**：发布新版本时更新 README 和 CHANGELOG
5. **谨慎操作**：
   - PyPI: 发布后无法删除，只能 yank
   - npm: 发布后 72 小时内可以撤销，之后只能废弃
6. **遵循语义化版本**：使用 [Semantic Versioning](https://semver.org/)

---

## 📞 获取帮助

如果发布过程中遇到问题：
- 查看 [Issues](https://github.com/Lockeysama/TheConn/issues)
- 参考 [DEVELOPMENT.md](DEVELOPMENT.md)
- 提交新 Issue
