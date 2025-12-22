# Epic 初始化指南

为新的 Epic 初始化基础设施，包括目录结构、上下文目录和初始 README。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@rules/base_rules.md` 中定义的所有基础公约。**

**📋 规范引用**：

本 Playbook 依赖以下规范文件（AI 必须先加载）：
- **基础公约**: `@rules/base_rules.md` - 禁止事项、文件路径约定、质量标准

本 Playbook **不依赖**以下规范：
- ❌ `test_strategy_rules.md` - Epic 初始化不涉及测试策略
- ❌ `bdd_language_rules.md` - Epic 初始化不涉及 BDD

**原因**: epic_init 只负责创建基础设施（目录和初始 README），不涉及测试规划

## 本 Playbook 的工作范围

**专注于**：初始化新 Epic 的基础设施

**使用说明**：
- **通常情况**：本 Playbook 由 `epic_planning.md` 自动调用，用户无需直接使用
- **直接使用场景**：仅需创建目录结构而不生成规划内容时，使用 `tc plan epic-init <名称>`
- **推荐方式**：直接使用 `tc epic <名称>`，会自动处理初始化和规划生成

**包括**：
1. 自动识别下一个可用的 Epic 编号
2. 创建 Epic 目录结构
3. 创建 Epic 上下文目录
4. 生成初始 Epic README.md 文件

**不包括**：
- 详细的 Epic 规划内容（使用 `@playbooks/planning/epic_planning.md`）
- Feature 和 Story 的生成

---

## 命名与格式规范

### ID 命名规则

- **格式**: `EPIC-{序号}`
- **序号**: 全局唯一，两位数字，从 01 开始
- **示例**: `EPIC-01`, `EPIC-02`, `EPIC-10`

### 目录命名规则

- **格式**: `EPIC-{序号}_{PascalCaseName}`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `EPIC-01_Base_Init`, `EPIC-02_UserManagement`

### 自动编号逻辑

1. **扫描现有 Epic**：列出 `.the_conn/epics/` 目录下所有以 `EPIC-` 开头的目录
2. **提取编号**：从目录名中提取数字编号（如 `EPIC-01_Name` → `01`）
3. **计算下一个编号**：找到最大编号 + 1，格式化为两位数字
4. **示例**：
   - 现有: `EPIC-01`, `EPIC-02`, `EPIC-05`
   - 下一个: `EPIC-06`

---

## 执行步骤

### Step 1: 自动识别 Epic 编号

**操作**：
1. 使用 `list_dir` 工具列出 `.the_conn/epics/` 目录
2. 提取所有 `EPIC-XX` 格式的编号
3. 计算下一个可用编号

**输出示例**：
```
🔍 扫描现有 Epic...
   发现: EPIC-01, EPIC-02
   
✅ 下一个可用编号: EPIC-03
```

### Step 2: 解析用户输入并确认 Epic 信息

**解析用户输入**：

用户输入格式：`@tc.md epic-init <Epic名称> [简单描述]`

- **Epic 名称**：第一个参数（必需）
- **简单描述**：后续所有文本（可选，如果没有则使用 Epic 名称作为描述）

**示例**：
```bash
# 带描述
@tc.md epic-init 用户管理系统 实现用户注册、登录和权限管理
→ 名称: "用户管理系统"
→ 描述: "实现用户注册、登录和权限管理"

# 仅名称
@tc.md epic-init 数据分析模块
→ 名称: "数据分析模块"
→ 描述: "数据分析模块" (使用名称作为默认描述)
```

**与用户确认**：
- Epic 编号: `EPIC-XX`
- Epic 名称: `{用户提供的名称}`
- Epic 描述: `{用户提供的描述或名称}`
- 目录名称: `EPIC-XX_{PascalCaseName}`

**示例对话**：
```
📋 准备创建新 Epic:
   - 编号: EPIC-03
   - 名称: 用户管理系统
   - 描述: 实现用户注册、登录和权限管理
   - 目录: EPIC-03_UserManagement
```

### Step 3: 创建目录结构

**创建以下目录**：

```
.the_conn/
├── epics/
│   └── EPIC-XX_{PascalCaseName}/
│       └── features/              # 空目录，待后续填充
│
└── context/
    └── epics/
        └── EPIC-XX/               # Epic 专属上下文目录
```

**操作**：
1. 使用 `write` 工具创建 Epic README.md（自动创建父目录）
2. 使用 `write` 工具在 `features/` 目录下创建 `.gitkeep` 占位文件
3. 使用 `write` 工具在 `context/epics/EPIC-XX/` 目录下创建 `.gitkeep` 占位文件

### Step 4: 生成初始 Epic README

**文件路径**：`.the_conn/epics/EPIC-XX_{PascalCaseName}/README.md`

**内容模板**：

```markdown
---
id: EPIC-XX
status: pending
created: yyyy-mm-dd
---

# EPIC-XX: {Epic 名称}

## 概述

{用户输入的简单描述}

## 业务价值

待补充

## 范围

待补充

## 关键指标

待补充

## Features 概览

待规划 - 使用 `@tc.md plan feature` 或 `@tc.md plan breakdown` 生成

## 测试里程碑

待规划 - 根据 Features 确定后补充

---

## 相关上下文

Epic 专属上下文位于: `.the_conn/context/epics/EPIC-XX/`

使用 `@tc.md ctx add` 或 `@tc.md ctx extract` 添加上下文文档。
```

**字段说明**：
- `id`: Epic 编号
- `status`: `pending` (规划中/进行中) 或 `done` (已完成)
- `created`: 创建日期，格式 `yyyy-mm-dd`
- **概述**：直接使用用户输入的描述（一句话即可）
- **其他字段**：保留为"待补充"，后续手动或使用 `@tc.md epic` 完善

### Step 5: 确认完成

**输出摘要**：

```
✅ Epic 初始化完成！

📁 创建的目录结构:
   ├── .the_conn/epics/EPIC-XX_{PascalCaseName}/
   │   ├── README.md
   │   └── features/
   └── .the_conn/context/epics/EPIC-XX/

📝 下一步建议:
   1. 使用 @tc.md plan review 来讨论并生成技术方案
```

---

## 使用示例

### 示例 1: 创建第一个 Epic（带简单描述）

```bash
用户: @tc.md epic-init 用户管理系统 实现用户注册、登录和权限管理

AI:
🔍 扫描现有 Epic...
   未发现现有 Epic
   
✅ 下一个可用编号: EPIC-01

📋 准备创建新 Epic:
   - 编号: EPIC-01
   - 名称: 用户管理系统
   - 描述: 实现用户注册、登录和权限管理
   - 目录: EPIC-01_UserManagement
   
[创建目录和文件...]

✅ Epic 初始化完成！

生成的 README.md 概述：
"实现用户注册、登录和权限管理"
```

### 示例 2: 创建后续 Epic（仅名称）

```bash
用户: @tc.md epic-init 数据分析模块

AI:
🔍 扫描现有 Epic...
   发现: EPIC-01, EPIC-02
   
✅ 下一个可用编号: EPIC-03

📋 准备创建新 Epic:
   - 编号: EPIC-03
   - 名称: 数据分析模块
   - 描述: 数据分析模块（使用名称作为默认描述）
   - 目录: EPIC-03_DataAnalysis
   
[创建目录和文件...]

✅ Epic 初始化完成！
```

---

## 注意事项

1. **编号唯一性**: 系统自动确保 Epic 编号不重复
2. **命名规范**: Epic 名称会自动转换为 PascalCase 用于目录名
3. **极简内容**: 初始 README 只包含：
   - 用户输入的简单描述（写入"概述"部分）
   - 其他字段保留为"待补充"
   - 后续使用 `@tc.md epic` 或手动完善详细内容
4. **描述处理**: 
   - 如果用户提供描述，使用用户描述
   - 如果只提供名称，使用名称作为默认描述
5. **上下文目录**: 创建空的上下文目录，等待后续添加文档
6. **Git 友好**: 使用 `.gitkeep` 文件确保空目录可以被 Git 跟踪

---

## 与其他 Playbook 的配合

- **epic_planning.md**: 用于生成详细的 Epic 规划内容
- **requirements_breakdown.md**: 批量生成 Epic/Feature/Story
- **context/extract.md**: 提取 Epic 专属上下文
- **feature_planning.md**: 在 Epic 下创建 Features

**推荐工作流**：

```bash
# 1. 初始化 Epic 基础设施
@tc.md epic-init {Epic名称} {简单描述}

# 2. 讨论并生成技术方案
@tc.md plan review

# 3. 完善 Epic 规划（可选）
@tc.md epic {Epic名称}  # 使用 epic_planning.md 生成详细内容

# 4. 创建 Features
@tc.md feature {Feature名称}

# 5. 提取上下文
@tc.md ctx extract
```

---

现在，请提供 Epic 名称，我将为你初始化新的 Epic 基础设施。

