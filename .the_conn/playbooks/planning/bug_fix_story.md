# Bug Fix Story 生成指南

你是一位资深的质量工程师。你的任务是根据发现的 Bug，生成结构化的 Bug Fix Story 文件。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

## 本 Playbook 的工作范围

**专注于**：

- ✅ **生成 Bug Fix Story 文档**：创建 Bug Fix Story 文件
- ✅ **编写修复方案**：描述修复思路和验收标准
- ✅ **使用代码片段**：可使用代码片段说明问题和修复方案

---

## 使用场景

当以下情况发生时，应使用此模板：

1. 已完成的 Story 在集成/系统测试阶段发现缺陷
2. 生产环境发现的问题
3. 原 Story 的测试覆盖不足导致的边缘情况遗漏

---

---

## 输入

用户会提供以下材料：

- 父 Story ID（被修复的 Story）
- Bug 现象描述（测试场景、预期行为、实际行为）
- 影响范围

---

## 输出要求

### 1. 文件路径

```
.the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{Name}/stories/STORY-{父序号}.{子序号}_{PascalCaseName}.md
```

**示例**: `.the_conn/epics/EPIC-01_Base_Init/features/FEAT-01_Init_Project/stories/STORY-01.1_Fix_Permission.md`

### 2. Bug Fix ID 规则

- **格式**: `STORY-{父序号}.{子序号}`
- **父序号**: 对应的父 Story 编号
- **子序号**: 该 Story 的 Bug 修复序号，从 1 开始
- **示例**: `STORY-01.1`, `STORY-01.2`, `STORY-05.1`

### 3. 文件命名规则

- **格式**: `STORY-{父序号}.{子序号}_{PascalCaseName}.md`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `STORY-01.1_Fix_Permission.md`, `STORY-02.1_Handle_Concurrency.md`

---

## 输出格式

```markdown
---
id: STORY-{父序号}.{子序号}
type: bug_fix
epic: EPIC-{序号}
feature: FEAT-{序号}
status: pending
created: yyyy-mm-dd
depends_on:
  - STORY-{父序号}
---

# Bug Fix: {问题简述}

## 1. 问题

**发现于**: {集成测试 / 系统测试 / 生产环境}

**现象**:
- 场景: {触发问题的条件}
- 预期: {应该发生什么}
- 实际: {实际发生什么}

**影响**: {对功能/用户/系统的影响}

## 2. 分析

**定位**: `{文件路径}` 的 `{函数/方法}`

**原因**: {为什么出问题，1-2 句话}

**遗漏原因**: {原 Story 为何没覆盖到这个场景}

## 3. 修复

**方案**: {简要说明修复思路}

**验收标准（测试清单）**:

- [ ] 修复验证：在 {复现条件} 下执行 {触发动作}，{修复后的正确行为}
- [ ] 回归验证：确保原有功能 {具体功能点} 不受影响
- [ ] 单元测试：新增/修改测试用例覆盖此 Bug 场景
- [ ] 测试通过：所有相关测试通过，代码通过 linter 检查

**验证方式**：
- 运行单元测试套件
- 手动验证 Bug 已修复
- 回归测试确认无副作用

**涉及文件**:
- `{文件路径}` - {说明}

**边界**:
- 禁止修改: {范围}
```

---

## Frontmatter 字段说明

**所有字段均为必填！**

| 字段         | 类型   | 说明                | 示例                |
| ------------ | ------ | ------------------- | ------------------- |
| `id`         | string | Bug Fix ID          | `STORY-01.1`        |
| `type`       | enum   | 固定为 `bug_fix`    | `bug_fix`           |
| `epic`       | string | 所属 Epic ID        | `EPIC-01`           |
| `feature`    | string | 所属 Feature ID     | `FEAT-01`           |
| `status`     | enum   | 状态                | `pending` 或 `done` |
| `created`    | date   | 创建日期            | `2025-12-11`        |
| `depends_on` | array  | 父 Story ID（必须） | `[STORY-01]`        |

**字段约束**:

- `type`: 必须是 `bug_fix`
- `status`: 只能是 `pending` 或 `done`
- `created`: 格式必须是 `yyyy-mm-dd`
- `depends_on`: 第一个元素必须是父 Story ID

---

## 生成原则

1. **问题清晰**: 现象描述要足够详细，能复现问题
2. **追溯关系**: `depends_on` 的第一个元素必须是父 Story ID
3. **验收聚焦**: 测试清单必须包含修复验证和回归验证
4. **范围最小**: 只修复问题，不做额外重构
5. **命名规范**: 使用 PascalCase 命名
6. **测试先行**: 先写测试复现 Bug，再修复代码

---

## 测试策略说明

### Bug Fix 的测试方法

Bug Fix Story 使用**单元测试 + 回归测试**策略：

**1. 修复验证测试**：

- 编写能复现 Bug 的测试用例
- 修复前测试应该失败
- 修复后测试应该通过
- 确保 Bug 不会再次出现

**2. 回归测试**：

- 运行原有的所有测试用例
- 确保修复没有破坏现有功能
- 特别关注相关模块的测试

**3. 边界测试**：

- 测试 Bug 修复的边界情况
- 测试相似场景是否也存在问题
- 确保修复的完整性

### 测试清单要求

必须包含以下内容：

- [ ] **修复验证**：具体描述如何验证 Bug 已修复
- [ ] **回归验证**：确认相关功能不受影响
- [ ] **单元测试**：新增或修改的测试用例
- [ ] **测试通过**：所有测试通过，linter 检查通过

### 测试文件组织

**按编程语言习惯组织**：

- Go: 与源代码同目录，`*_test.go`
- Python: `tests/` 目录下，`test_*.py`
- 其他语言按语言习惯

---

## 示例

```markdown
---
id: STORY-01.1
type: bug_fix
epic: EPIC-01
feature: FEAT-01
status: pending
created: 2025-12-11
depends_on:
  - STORY-01
---

# Bug Fix: 修复文件权限问题

## 1. 问题

**发现于**: 集成测试

**现象**:
- 场景: 在 Linux 系统上执行初始化命令
- 预期: 创建的文件应有 0644 权限
- 实际: 创建的文件权限为 0600

**影响**: 其他用户无法读取配置文件

## 2. 分析

**定位**: `src/theconn/init.py` 的 `create_file()` 函数

**原因**: 使用默认的 open() 权限，未显式设置

**遗漏原因**: 原 Story 只在单用户环境测试，未覆盖多用户场景

## 3. 修复

**方案**: 使用 os.chmod() 显式设置文件权限为 0644

**验收标准（测试清单）**:

- [ ] 修复验证：在 Linux 系统上执行初始化命令，文件权限应为 0644
- [ ] 权限验证：其他用户应能读取创建的文件
- [ ] 回归验证：在不同操作系统上（Linux, macOS, Windows）文件创建成功且内容正确
- [ ] 单元测试：新增文件权限验证测试用例
- [ ] 测试通过：所有测试通过，代码通过 linter 检查

**验证方式**：
- 运行单元测试套件
- 在 Linux 环境手动验证文件权限
- 跨平台测试确认兼容性

**涉及文件**:
- `src/theconn/init.py` - 修改 create_file() 函数
- `tests/test_init.py` - 新增权限验证测试

**边界**:
- 禁止修改: 其他初始化逻辑
```

---

现在，请根据用户提供的 Bug 信息生成 Bug Fix Story。
