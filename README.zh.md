# The Conn: 项目命名哲学与使命

[English Version](README.md) | [CLI 文档](CLI.md) | [使用指南](.the_conn/docs/GUIDE.md) | [开发指南](DEVELOPMENT.md)

## 🚀 快速开始

使用一条命令将 The Conn 框架集成到你的项目：

**Python 用户：**

```bash
# 在当前项目目录下运行
uvx theconn init

# 或指定目标项目路径
uvx theconn init /path/to/your/project
```

**Node.js 用户：**

```bash
# 在当前项目目录下运行
npx theconn-cli init

# 或指定目标项目路径
npx theconn-cli init /path/to/your/project
```

**说明：**

- 默认情况下，命令会在当前工作目录初始化 The Conn 框架
- 如果指定了路径参数，将在目标目录下进行初始化
- 初始化会创建 `.the_conn/` 目录及其必需的子目录结构

然后阅读 `.the_conn/docs/GUIDE.md` 了解详细的使用方法。

## 🚀 快速命令参考

The Conn 提供了统一的命令入口文件 `tc.md`，让你轻松与 AI 交互：

```bash
# 在 AI IDE（如 Cursor）中，使用 @ 符号引用 tc.md 文件：
@tc.md <命令>

# 示例：
@tc.md init                    # 初始化项目
@tc.md story 用户登录          # 创建 Story
@tc.md status                  # 查看项目状态
@tc.md next                    # 获取下一步建议
```

**查看文档：**

- 📘 [快速开始指南](.the_conn/docs/QUICK_START.md)
- 📗 [命令参考手册](.the_conn/docs/COMMANDS.md)
- 📙 [命令映射表](.the_conn/docs/COMMAND_MAPPING.md)

## 🎯 如何使用 The Conn

### 目录结构

初始化后，The Conn 会在你的项目中创建 `.the_conn/` 目录：

```text
.the_conn/
├── epics/              # 📋 规划层 - 项目路线图（初始为空）
│   └── EPIC-01_功能名称/                  # 规划阶段创建
│       ├── README.md
│       └── features/
│           └── FEAT-01_子功能/
│               ├── README.md
│               └── stories/
│                   └── STORY-01_任务描述.md
│
├── context/            # 📚 知识层 - 架构与决策（初始为空）
│   ├── global/         # 项目级上下文
│   │   ├── Architecture.md                # 项目初始化时创建
│   │   ├── Tech_Stack.md                  # 项目初始化时创建
│   │   └── Coding_Standard.md            # 项目初始化时创建
│   └── epics/          # Epic 专属上下文
│       └── EPIC-01/                       # Epic 规划时创建
│           └── Module_Design.md
│
├── playbooks/          # 🤖 工具层 - AI 操作剧本（从 GitHub 下载）
│   ├── tc.md           # 🎯 统一命令入口（新功能！）
│   ├── core/
│   │   ├── core.md
│   │   └── base_rules.md
│   ├── initialization/
│   ├── planning/
│   ├── context/
│   └── execution/
│
├── docs/               # 📚 用户文档（从 GitHub 下载）
│   ├── README.md
│   └── GUIDE.md
│
└── ai_workspace/       # 🔧 执行层 - 临时工作区（初始为空）
    └── EPIC-01/                           # 任务执行时创建
        └── TASK-01_STORY-01_Name/
            ├── task.md
            └── context.manifest.json
```

**初始化时创建的内容：**

- ✅ `playbooks/` - 从 GitHub 下载（所有 AI 操作剧本可直接使用）
  - 包含 `tc.md` - 统一命令入口 🎯
- ✅ `docs/` - 从 GitHub 下载（README.md, GUIDE.md, QUICK_START.md, COMMANDS.md）
- 📁 `epics/` - 空目录（规划阶段填充）
- 📁 `context/global/` - 空目录（通过项目初始化 playbook 填充）
- 📁 `context/epics/` - 空目录（创建 Epic 时填充）
- 📁 `ai_workspace/` - 空目录（临时工作区，建议添加到 `.gitignore`）

### 完整工作流（5 个阶段）

#### 阶段 0：项目初始化

首次设置，创建结构和基础上下文。

```bash
# 运行 `uvx theconn init` 或 `npx theconn-cli init` 后：
# 使用 AI 初始化项目结构

# 新方式（推荐 - 使用 tc.md）：
@tc.md init

# 或传统方式（使用完整 playbook 路径）：
@playbooks/initialization/project_init.md 帮我初始化 The Conn 项目
```

这会创建：

- 目录结构
- 初始全局上下文（架构、技术栈、编码规范）
- 项目约定

#### 阶段 1：从需求到规划

将外部需求转换为可执行的开发任务。

##### 步骤 1：需求评审

```bash
# 新方式（推荐）：
@tc.md plan review

# 或传统方式：
@{需求文档} @playbooks/planning/requirements_review.md 开始评审
```

- 与 AI 讨论需求
- 确定技术方案
- 输出：技术方案文档

##### 步骤 2：提取上下文

```bash
# 新方式（推荐）：
@tc.md ctx extract

# 或传统方式：
@{技术方案} @playbooks/context/extract.md 提取上下文
```

- 将可复用知识提取到 `.the_conn/context/global/`
- 创建架构决策、模式、约定

##### 步骤 3：生成规划（选择 A 或 B）

###### 方案 A：批量生成（推荐）

```bash
# 新方式（推荐）：
@tc.md plan breakdown requirements.md
# 或使用缩写：
@tc.md plan bd requirements.md

# 或传统方式：
@{需求文档} @{技术方案} @playbooks/planning/requirements_breakdown.md 开始拆解
```

- AI 展示大纲 → 你确认 → AI 生成所有 Epic/Feature/Story 文件

###### 方案 B：逐步生成

```bash
# 新方式（推荐）：
@tc.md epic 用户管理系统
@tc.md feature 用户认证
@tc.md story 登录功能

# 或传统方式：
@{需求文档} @playbooks/planning/epic_planning.md 生成 Epic
@{需求文档} @playbooks/planning/feature_planning.md 生成 Feature
@{需求文档} @playbooks/planning/story_writing.md 生成 Story
```

##### 步骤 4：提取 Epic 专属上下文

```bash
# 新方式（推荐）：
@tc.md ctx extract

# 或传统方式：
@.the_conn/epics/EPIC-XX_Name/README.md @playbooks/context/extract.md 提取 Epic 上下文
```

- 输出到 `.the_conn/context/epics/EPIC-XX/`
- 包含模块设计、数据模型、API 规范

#### 阶段 2：从 Story 到 Task

为 AI 准备执行材料。

```bash
# 新方式（推荐）：
@tc.md task STORY-01
# 或使用缩写：
@tc.md exec t STORY-01

# 或传统方式：
@{Story文件} @playbooks/execution/task_generation.md 生成 Task
```

在 `.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/` 创建：

1. `task.md` - 任务简报（强调 BDD/TDD 测试先行）
2. `context.manifest.json` - 该任务的上下文清单

#### 阶段 3：执行开发任务

AI 辅助编码，人工监督。

```bash
# 开始任务
@.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/ 开始任务
```

AI 遵循 BDD/TDD 工作流（步骤 1-5）：

1. 创建/更新 `.feature` 文件（BDD 场景）
2. 先编写测试代码
3. 实现业务逻辑使测试通过
4. 运行测试并验证
5. 代码完成

##### ⚠️ 人工审查检查点

- 审查代码实现
- 审查测试覆盖
- 确认符合预期

##### 完成任务闭环（步骤 6-7）

```bash
# 批准后
请继续执行 Step 6-7 完成任务闭环
```

AI 自动：

1. 生成变更摘要
2. 同步 Story 状态为 `done`

#### 阶段 4：任务闭环与同步

如果阶段 3 中未执行步骤 6-7，手动执行：

```bash
# 新方式（推荐）：
@tc.md summary
@tc.md sync STORY-01

# 或传统方式：
@playbooks/execution/change_summary.md 生成变更摘要
@{原始Story文件} @playbooks/execution/story_sync.md 开始同步
```

#### 阶段 5：Bug 修复工作流

对于已完成 Story 中发现的 Bug：

```bash
# 新方式（推荐）：
@tc.md bugfix STORY-01 Bug 描述
# 或使用缩写：
@tc.md plan bf STORY-01 Bug 描述

# 或传统方式：
@playbooks/planning/bug_fix_story.md 生成 Bug Fix Story

父 Story: STORY-01
发现于: 集成测试
现象: ...
```

- 创建 `STORY-XX.X_Name.md`（例如 `STORY-01.1_Fix_Bug.md`）
- 然后按照阶段 2-4 修复

### 核心概念

#### 规划层级

```text
Epic（业务目标）
  └── Feature（功能模块）
      └── Story（可实现任务）
          └── Task（AI 执行单元）
```

#### ID 命名规范

- Epic：`EPIC-01`, `EPIC-02`, ...
- Feature：`FEAT-01`, `FEAT-02`, ...（每个 Epic 内）
- Story：`STORY-01`, `STORY-02`, ...（每个 Epic 内）
- Bug 修复：`STORY-01.1`, `STORY-01.2`, ...（继承父 Story ID）
- Task：`TASK-01`, `TASK-02`, ...（Epic 内顺序编号）

#### 上下文系统

上下文是指导 AI 生成符合你愿景的代码的"知识库"：

- **全局上下文**（`context/global/`）：整个项目共享
  - Architecture.md - 系统架构
  - Tech_Stack.md - 技术选型
  - Coding_Standard.md - 代码规范
  - Testing_Strategy.md - 测试策略

- **Epic 上下文**（`context/epics/EPIC-XX/`）：Epic 专属知识
  - Module_Design.md - 模块结构
  - Data_Model.md - 数据模式
  - API_Spec.md - API 契约
  - Integration_Plan.md - 集成策略

#### 核心原则

- **你规划，AI 执行**：你定义"做什么"和"为什么"；AI 处理"如何做"
- **上下文为王**：良好维护的上下文确保一致、高质量的 AI 输出
- **测试先行**：总是在实现前创建测试（BDD/TDD）
- **人工审查**：集成前总是要审查
- **迭代开发**：将复杂任务分解为 Story，系统性地处理

### 快速开始示例

初始化后，典型的第一次会话：

```bash
# 新方式（推荐 - 使用 tc.md）：
# 1. 初始化项目结构
@tc.md init

# 2. 需求评审
@tc.md plan review

# 3. 从批准的方案生成规划
@tc.md plan breakdown requirements.md

# 4. 查看项目状态
@tc.md status

# 5. 开始实现第一个 Story
@tc.md task STORY-01

# 6. 导航到工作空间并开始
@.the_conn/ai_workspace/EPIC-01/TASK-01_STORY-01_Login/ 开始任务

# 7. 审查后，同步 Story
@tc.md sync STORY-01

# 8. 获取下一步建议
@tc.md next
```

**传统方式（使用完整 playbook 路径）：**

```bash
# 1. 初始化项目结构
@playbooks/initialization/project_init.md 初始化项目

# 2. 定义你的第一个 Epic（例如：用户认证）
@{auth_requirements.md} @playbooks/planning/requirements_review.md 评审

# 3. 从批准的方案生成规划
@{requirements.md} @{tech_solution.md} @playbooks/planning/requirements_breakdown.md 拆解

# 4. 开始实现第一个 Story
@{STORY-01_Login.md} @playbooks/execution/task_generation.md 生成 Task
@.the_conn/ai_workspace/EPIC-01/TASK-01_STORY-01_Login/ 开始任务

# 5. 审查、批准，让 AI 完成闭环
请继续执行 Step 6-7
```

### 协作技巧

#### 团队协作

- 将 `epics/` 和 `context/` 提交到 Git（共享规划和知识）
- 将 `ai_workspace/` 添加到 `.gitignore`（个人临时工作）
- 使用分支策略：`epic/EPIC-XX` 用于 Epic 级别的工作
- 通过 Epic README 协调 Story ID

#### 单人开发

- 从全局上下文开始（架构、技术栈）
- 一次创建一个 Epic
- 批判性地审查 AI 输出 - 你是舰长
- 随着项目演进保持上下文更新

关于完整的工作流程、故障排除和高级功能，请在初始化后查看 `.the_conn/docs/GUIDE.md`。

## 📚 文档

### CLI 与开发

- **[CLI.md](CLI.md)** - CLI 使用文档（面向用户）
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - 开发指南（面向开发者）
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - 贡献指南
- **[RELEASING.md](RELEASING.md)** - 发布流程（面向维护者）

### The Conn 命令系统（初始化后）

- **[快速开始指南](.the_conn/docs/QUICK_START.md)** - 5 分钟掌握 `@tc.md` 命令
- **[命令参考手册](.the_conn/docs/COMMANDS.md)** - 完整命令列表和详细用法
- **[命令映射表](.the_conn/docs/COMMAND_MAPPING.md)** - `@tc.md` 命令与 Playbook 映射
- **[迁移指南](.the_conn/docs/MIGRATION_GUIDE.md)** - 从直接使用 Playbook 迁移
- **[主要README](.the_conn/docs/README.md)** - 综合操作手册

## 核心思想：在 AI 浪潮中，为人类领航员重夺指挥权

在人工智能驱动软件开发的新纪元，我们面临一个根本性的选择：是让开发者沦为 AI 指令的被动修正者，还是将他们提升为驾驭 AI 强大动力的战略指挥官？

**The Conn 的诞生，正是为了实现后者。**

我们拒绝混乱、失控的 AI 生成过程。我们坚信，最卓越的软件，依旧源于人类的智慧、远见与架构能力。AI 不应是驾驶员，而应是最高效、最可靠的引擎与船员。人类，才是决定航船去向的唯一 **领航员 (The Navigator)**。

## **我们的隐喻：星舰“进取号”的舰桥**

为了清晰地定义这套人机协作的哲学，我们将整个开发过程比作一次星际航行：

- **领航员 (The Navigator) - 人类开发者**：
    您是舰长，是战略决策者。您不负责去引擎室拧每一颗螺丝，但您要设定最终的目的地（业务目标）、规划穿越星辰大海的航线（软件架构）、并在关键时刻做出决策（技术选型、逻辑审查）。您的智慧和经验，是航行成功的唯一保障。

- **AI 船员 (The AI Crew) - AI 代理与工具**：
    他们是高效、忠诚的执行者。他们掌握着强大的引擎（代码生成）、精准的传感器（测试与分析）和可靠的防御系统（代码修复）。他们能完美执行您下达的任何指令，但他们不会、也不应决定航船的航向。

- **舰桥 (The Bridge) - 开发环境**：
    这是您的指挥中心，是信息汇集与指令发出的地方。

- **指挥台 (The Conn) - 本项目框架**：
    这便是我们的项目——**The Conn**。它不是整座舰桥，而是舰桥上最核心的那个**指挥与航行控制台**。

## **为什么命名为“The Conn”？**

“Conn”一词源自海军术语，特指对舰船航向与速度的**直接指挥权**。在《星际迷航》等科幻作品中，当舰长说出 **“You have the Conn”** 时，意味着将飞船的驾驶控制权正式移交。

我们以此为名，蕴含着双重敬意与一层宣言：

1. **致敬专业**：它代表了工程学的严谨与专业性。
2. **致敬远见**：它唤起了我们对未来科技协同的美好想象。
3. **我们的宣言**：我们通过这个项目，将软件开发的“指挥权”——The Conn——郑重地交还到每一位人类开发者手中。

**The Conn 框架，就是您用来发号施令、掌控全局的指挥台。** 它将您的战略意图（架构设计、任务规划）精准地翻译成 AI 能够理解并执行的具体指令，并确保整个过程始终在您的掌控之下。

## **我们的目标 (Our Mission)**

**The Conn** 致力于成为 AI 时代下，为人类开发者赋能的标准化协作框架。我们的核心目标是：

1. **赋能领航员 (Empower the Navigator)**：提供一套清晰、高效的交互界面与工作流，让开发者能以最自然的方式进行战略规划、下达指令和审查结果，而非陷入到与 AI 纠缠的细节泥潭中。

2. **标准化协作流程 (Standardize the Workflow)**：固化一套“人类规划、AI 执行”的最佳实践。通过提供项目脚手架、标准化的指令模板和敏捷工作流，确保人机协作的稳定、高效与可预测。

3. **安全地释放 AI 的潜力 (Unleash AI, Safely)**：作为人类与 AI 之间的核心接口，The Conn 将内置强大的“护栏”，确保 AI 的执行始终服务于人类的战略意图，防止偏离航道，让开发者可以放心地将重复性、工程化的任务交给 AI。

4. **提升开发体验与项目质量 (Elevate Experience & Quality)**：最终，我们旨在将开发者从繁琐的编码工作中解放出来，聚焦于创造、架构和解决复杂问题，从而在大幅提升开发速度的同时，创造出更高质量、更具远见的软件产品。

---

> **The Conn 不仅仅是一个工具集或一个脚手架，它是一种宣言，一种工作哲学。**
>
> **它宣言：在人工智能的星辰大海中，人类永远是掌舵人。**
>
> **在这里，我们重申：You have the Conn.**
