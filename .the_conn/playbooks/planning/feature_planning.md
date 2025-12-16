# Feature 规划生成指南

根据需求文档或 Epic 生成 Feature 规划文件。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

## 本 Playbook 的工作范围

**专注于**：生成 Feature 规划文档（创建 Feature README.md 文件）

**📋 规范引用**：

- **测试策略**：`@playbooks/core/test_strategy_rules.md`
- **复杂度评估**：`@playbooks/core/complexity_rules.md`

---

## 命名与格式规范

### ID 命名规则

- **格式**: `FEAT-{序号}`
- **序号**: Epic 内唯一，两位数字，从 01 开始
- **示例**: `FEAT-01`, `FEAT-02`, `FEAT-10`

### 目录命名规则

- **格式**: `FEAT-{序号}_{PascalCaseName}`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `FEAT-01_Init_Project`, `FEAT-02_Generate_Templates`

### 文件路径

```
.the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{PascalCaseName}/README.md
```

**示例**: `.the_conn/epics/EPIC-01_Base_Init/features/FEAT-01_Init_Project/README.md`

### Frontmatter 规范

```yaml
---
id: FEAT-01
status: pending
created: yyyy-mm-dd
---
```

**字段说明**：

- `status`: `pending` (未完成) 或 `done` (已完成)
- `created`: 格式 `yyyy-mm-dd`

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
2. **Story 拆分**: 按功能模块或职责边界拆分，每个 Story 有清晰的实现范围
3. **验收标准**: 端到端的用户流程，可实际验证
4. **命名规范**: Feature 名称使用 PascalCase
5. **粒度控制**: 优先按完整功能模块划分，每个 Feature 包含 2-5 个 Story 即可
6. **便于 AI 编码**: 确保每个 Story 的边界清晰，接口明确，依赖关系简单
7. **测试规划**: 根据 Feature 特征自动规划测试 Story

---

## 自动生成测试 Story (智能引导)

### 测试 Story 决策逻辑（多维度综合判断）

生成 Feature 时，AI 综合以下维度判断是否需要测试 Story：

**多维度评估框架**：

| 评估维度       | 高风险触发条件     | 中风险触发条件   | 权重 |
| -------------- | ------------------ | ---------------- | ---- |
| **功能完整性** | 构成完整用户旅程   | 包含关键业务步骤 | 高   |
| **集成复杂度** | 多系统集成（≥3个） | 双系统集成       | 高   |
| **任务复杂度** | 平均复杂度 ≥ 6.0   | 平均复杂度 ≥ 5.0 | 中   |
| **风险等级**   | 核心业务/金融交易  | 重要业务流程     | 高   |
| **用户可见性** | 用户主要交互流程   | 用户辅助功能     | 中   |
| **Story 数量** | ≥5 个功能 Story    | ≥3 个功能 Story  | 低   |

**决策规则**：

```
✅ 必须添加 E2E: 
   - 任意 1 个高权重高风险条件
   
💡 强烈建议 E2E:
   - 2+ 个高权重中风险条件
   - 1 个高权重中风险 + 2 个中权重条件
   
⚠️ 建议添加 E2E:
   - 2+ 个中权重条件
   - 1 个中权重 + 2 个低权重
   
❌ 无需 E2E:
   - 仅满足低权重条件
   - 不满足任何条件
```

**性能测试判断**：

- 明确性能指标（响应时间、吞吐量、并发数）
- 性能敏感场景（大数据、实时处理、复杂计算）
- 如果检测到 → 建议性能测试 Story

### AI 自动生成输出

**如果需要测试 Story，AI 自动添加：**

```markdown
## 包含的 Story

### 功能开发 Story
- STORY-01: {功能1描述}
- STORY-02: {功能2描述}
- STORY-03: {功能3描述}

### 测试 Story（自动建议）
- STORY-99: E2E_{FeatureName}_Flow
  - **类型**: E2E BDD 测试
  - **目的**: 验证 STORY-01 → STORY-02 → STORY-03 的完整集成流程
  - **触发条件**: 所有功能 Story 完成后
  - **预计场景**: 
    - Happy Path: 完整功能流程验证
    - 异常处理: 错误边界和恢复机制
    - 数据一致性: 跨模块数据验证

💡 **AI 建议理由**: 
检测到 Feature 包含 3 个功能 Story，且涉及数据库和 API 集成，
建议添加 E2E 测试 Story 确保各模块协同工作正常。
```

### 测试 Story 命名规范

| Story 类型 | 命名格式                             | 示例                            |
| ---------- | ------------------------------------ | ------------------------------- |
| E2E 测试   | `STORY-99_E2E_{FeatureName}_Flow`    | `STORY-99_E2E_Auth_Flow`        |
| 集成测试   | `STORY-98_Integration_{FeatureName}` | `STORY-98_Integration_Payment`  |
| 性能测试   | `STORY-97_Performance_{FeatureName}` | `STORY-97_Performance_DataSync` |

**编号约定**: 测试 Story 使用 97-99 编号，与功能 Story 区分

### 决策示例

**场景 1: 核心业务 Feature（必须 E2E）**

```
FEAT-01: 用户认证（4 个 Story，平均复杂度 5.0）

分析: ✅ 完整流程 + 高集成 + 高风险
决策: ✅ 必须添加 STORY-99: E2E_Auth_Flow
```

**场景 2: 技术模块（无需 E2E）**

```
FEAT-02: 配置管理（2 个 Story，平均复杂度 2.3）

分析: ❌ 内部模块 + 低集成 + 低风险
决策: ❌ 无需 E2E，单元测试足够
```

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
