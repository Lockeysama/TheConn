# Feature 规划生成指南

根据需求文档或 Epic 生成 Feature 规划文件。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

## 本 Playbook 的工作范围

**专注于**：生成 Feature 规划文档（创建 Feature README.md 文件）

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
2. **Story 拆分**: 按功能模块或职责边界拆分，每个 Story 有清晰的实现范围
3. **验收标准**: 端到端的用户流程，可实际验证
4. **命名规范**: Feature 名称使用 PascalCase
5. **粒度控制**: 优先按完整功能模块划分，每个 Feature 包含 2-5 个 Story 即可
6. **便于 AI 编码**: 确保每个 Story 的边界清晰，接口明确，依赖关系简单
7. **测试规划**: 根据 Feature 特征自动规划测试 Story

---

## 自动生成测试 Story (智能引导)

### 测试 Story 决策逻辑

生成 Feature 时，AI 根据以下规则自动判断是否需要测试 Story：

**规则 1: 功能 Story 数量**
- Feature 包含 ≥3 个功能 Story → 自动建议 1 个 E2E BDD Story
- Feature 包含 <3 个功能 Story → 由各 Story 独立测试即可

**规则 2: 集成复杂度**
- Feature 涉及多系统集成（如数据库 + 缓存 + API）→ 建议 1 个集成测试 Story
- Feature 功能独立，无外部依赖 → 无需额外测试 Story

**规则 3: 性能要求**
- Feature 有明确性能指标（如响应时间、吞吐量）→ 建议 1 个性能测试 Story
- Feature 无特殊性能要求 → 无需性能测试 Story

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

### 自动生成决策示例

**场景 1: 简单 Feature（无需测试 Story）**
```
FEAT-01: 配置管理
- STORY-01: 读取配置文件
- STORY-02: 验证配置格式

分析:
- 功能 Story < 3 个 ✓
- 无外部依赖 ✓
- 无性能要求 ✓

💡 决策: 各 Story 的单元测试已足够，无需额外测试 Story
```

**场景 2: 复杂 Feature（需要测试 Story）**
```
FEAT-02: 用户认证
- STORY-01: 用户登录 UI
- STORY-02: Token 生成服务
- STORY-03: 权限验证中间件
- STORY-04: 会话管理

分析:
- 功能 Story = 4 个 ✗ (≥3)
- 涉及数据库 + Redis + API ✗ (多系统集成)
- 登录性能要求 <200ms ✗ (有性能要求)

💡 决策: 建议添加测试 Story
- STORY-99: E2E_Auth_Flow (必需)
- STORY-97: Performance_Login (推荐)
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
