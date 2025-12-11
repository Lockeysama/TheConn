# Feature 规划生成指南

根据需求文档或 Epic 生成 Feature 规划文件。

---

## 输出要求

### 1. 文件路径

```
.the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{PascalCaseName}/README.md
```

**示例**: `.the_conn/epics/EPIC-01_Base_Init/features/FEAT-01_Init_Project/README.md`

### 2. Feature ID 规则

- **格式**: `FEAT-{序号}`
- **序号**: Epic 内唯一，两位数字，从 01 开始
- **示例**: `FEAT-01`, `FEAT-02`, `FEAT-10`

### 3. 目录命名规则

- **格式**: `FEAT-{序号}_{PascalCaseName}`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `FEAT-01_Init_Project`, `FEAT-02_Generate_Templates`

---

## 输出格式

```markdown
# Feature: FEAT-{序号} {Feature 名称}

- **所属 Epic**: EPIC-{序号}
- **目标**: {一句话说明功能目标}
- **包含的故事**: STORY-{序号}, STORY-{序号}, ...
- **验收标准**:
  - {端到端验收项1}
  - {端到端验收项2}
- **创建日期**: {yyyy-mm-dd}
```

---

## 生成原则

1. **目标描述**: 从用户/业务视角描述，说明"为什么"和"价值是什么"
2. **Story 拆分**: 粒度适中，每个 Story 1-3 天可完成
3. **验收标准**: 端到端的用户流程，可实际验证
4. **命名规范**: Feature 名称使用 PascalCase

---

## 示例

```markdown
# Feature: FEAT-01 初始化项目结构

- **所属 Epic**: EPIC-01
- **目标**: 提供 CLI 命令一键初始化 The Conn 项目结构
- **包含的故事**: STORY-01, STORY-02
- **验收标准**:
  - 用户执行 `theconn init` 后，所有必需目录和文件创建成功
  - 生成的模板文件内容完整且格式正确
  - 重复执行不会覆盖已有文件
- **创建日期**: 2025-12-11
```

---

现在，请根据用户提供的材料生成 Feature 规划。
