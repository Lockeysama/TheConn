# 添加 Context 文档指南

你的任务是根据用户提供的内容，创建新的 Context 文档。

---

## 输入

用户会提供：
- Context 类型（从枚举中选择）
- Context 作用域（global 或 EPIC-XX）
- Context 内容（技术方案、设计文档、讨论结果等）

---

## 输出要求

### 1. 确定 Context 类型

**公共 Context Types (scope: global)**:
- `architecture` - 系统架构
- `tech_stack` - 技术栈
- `coding_standard` - 编码规范
- `testing_strategy` - 测试策略
- `deployment` - 部署方案
- `api_convention` - API 约定
- `domain_model` - 核心领域模型

**Epic Context Types (scope: EPIC-XX)**:
- `module_design` - 模块设计
- `data_model` - 数据模型
- `api_spec` - API 规范
- `integration` - 集成方案
- `algorithm` - 算法说明
- `protocol` - 协议设计
- `migration` - 迁移方案

### 2. 确定文件路径

**格式**: `{Type}_{Descriptor}.md`

- **公共 Context**: `.the_conn/context/global/{Type}_{Descriptor}.md`
- **Epic Context**: `.the_conn/context/epics/EPIC-{序号}/{Type}_{Descriptor}.md`

**示例**:
- `.the_conn/context/global/Architecture.md`
- `.the_conn/context/global/Coding_Standard_Go.md`
- `.the_conn/context/epics/EPIC-01/Module_Design_Init.md`
- `.the_conn/context/epics/EPIC-02/Protocol_Design_UDP.md`

### 3. Frontmatter 规范

```yaml
---
type: {type}
scope: global | EPIC-{序号}
title: {标题}
created: yyyy-mm-dd
updated: yyyy-mm-dd
tags:
  - {tag1}
  - {tag2}
---
```

**字段说明**:
- `type`: 从上述枚举中选择（必填）
- `scope`: `global` 或 `EPIC-01` 格式（必填）
- `title`: 文档标题（必填）
- `created`: 创建日期，格式 `yyyy-mm-dd`（必填）
- `updated`: 更新日期，初次创建与 created 相同（必填）
- `tags`: 便于搜索的标签（可选但推荐）

---

## 生成原则

1. **准确分类**: 根据内容选择最合适的 type
2. **合理命名**: Descriptor 应简洁明确，使用 PascalCase
3. **结构清晰**: 使用标题层级组织内容
4. **聚焦决策**: 记录"为什么这样设计"，而非显而易见的细节
5. **保持精简**: 只包含 AI 完成任务必需的信息

---

## 内容结构模板

### 架构/设计类 (architecture, module_design, protocol)

```markdown
# {标题}

## 1. 概述与目标

{简要说明目标和适用场景}

## 2. 核心设计

{核心算法、数据结构、流程}

## 3. 接口设计

{API 或函数签名}

## 4. 实施要点

{关键实现细节}

## 5. 注意事项

{约束、限制、已知问题}
```

### API/数据模型类 (api_spec, data_model)

```markdown
# {标题}

## 1. 概述

{API/模型用途}

## 2. 定义

{数据结构或接口定义}

## 3. 示例

{使用示例}

## 4. 约束

{验证规则、限制}
```

### 集成/迁移类 (integration, migration)

```markdown
# {标题}

## 1. 背景

{为什么需要}

## 2. 方案

{具体方案}

## 3. 步骤

{执行步骤}

## 4. 风险与对策

{风险和应对}
```

---

## 示例

### 示例 1: 添加模块设计文档

**用户输入**:
```
类型: module_design
作用域: EPIC-01
内容: 初始化模块设计 - 负责创建项目目录结构
```

**输出**:

**文件**: `.the_conn/context/epics/EPIC-01/Module_Design_Init.md`

```markdown
---
type: module_design
scope: EPIC-01
title: 初始化模块设计
created: 2025-12-11
updated: 2025-12-11
tags:
  - initialization
  - project-structure
---

# 初始化模块设计

## 1. 概述与目标

提供 CLI 命令一键创建 The Conn 框架的标准目录结构。

## 2. 核心设计

### 2.1 目录结构定义

使用常量定义标准目录树...

### 2.2 幂等性设计

重复执行不覆盖已有文件...

## 3. 接口设计

```python
def init_project(target_path: Path, overwrite: bool = False) -> Result:
    """初始化项目结构"""
```

## 4. 实施要点

- 使用 pathlib 处理路径
- 模板文件作为 package data 打包
- 权限处理: Unix 644, Windows 兼容
```

### 示例 2: 添加协议设计文档

**用户输入**:
```
类型: protocol
作用域: EPIC-02
内容: UDP 可靠传输协议设计（3次冗余 + 动态捎带）
```

**输出**:

**文件**: `.the_conn/context/epics/EPIC-02/Protocol_Design_UDP.md`

```markdown
---
type: protocol
scope: EPIC-02
title: UDP 可靠传输协议
created: 2025-12-11
updated: 2025-12-11
tags:
  - udp
  - reliability
  - protocol
---

# UDP 可靠传输协议设计

## 1. 概述与目标

解决 UDP 丢包问题，实现 99.9% 到达率...

## 2. 核心设计

### 2.1 协议结构

```json
{
  "h": {"seq": 5001, "ts": 1699999001},
  "d": [{"id": 101, "event": "..."}]
}
```

### 2.2 冗余策略

3次发送: T+0ms, T+20ms, T+40ms...

## 3. 实施要点

- Packet 去重使用 seq
- Event 去重使用 id
- 历史窗口保留最近 3-5 个事件
```

---

现在，请根据用户提供的信息创建 Context 文档。
