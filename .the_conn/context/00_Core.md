# AI 领航员的敏捷持续流动工作流 - 工程化实践示例

## **引言**

本 playbook 为采用 AI 辅助开发的现代化软件团队，提供了一套完整的、端到端的人机协作工作流。它旨在将人类工程师的战略、领域洞察力与 AI 的编码执行速度完美结合，通过一个高度结构化、版本化的项目管理流程，实现前所未有的开发效率与质量。

### 第一部分：核心原则

1. **意图与实现的分离**: 人类领航员定义“做什么”（意图），AI 编码引擎负责“怎么做”（实现）。
2. **规划即代码 (Planning as Code)**: 所有规划（Epics, Features, Stories）都作为 Markdown 文件存放在代码库中，与源代码同步版本化管理。
3. **上下文精准投喂**: 通过清单机制，为每个任务动态组合最相关的上下文，避免信息过载，提升 AI 输出的准确性。
4. **双向同步**: 不仅从“意图”驱动“实现”，也要在“实现”完成后，将变更同步回“意图”，确保文档与代码的持续一致。

***

### **第二部分：**&#x9879;目目录结构

这是整个工作流的骨架，确保所有信息都各归其位，职责清晰。

```shell
my_project/
├── .gitignore
├── .the_conn/                  # [AI协作层] AI 工具和上下文知识库
│   ├── context/                # [知识层] 项目的全局上下文知识库
│   │   ├── 00_ARCHITECTURE.md
│   │   └── 15_PAYMENT_MODULE_DESIGN.md
│   │
│   ├── ai_prompts/             # [工具层] 可复用的 Prompt 工具箱
│   │   ├── personas/
│   │   │   └── senior_java_developer.md
│   │   └── templates/
│   │       ├── task_execution_master.md
│   │       └── story_synchronization.md
│   │
│   └── ai_workspace/           # [执行层] AI 任务的临时工作区 (不提交到 Git)
│       └── PAY-124/
│           ├── task.md
│           ├── context.manifest.json
│           └── final_code_diff.txt
│
├── epics/                      # [规划层] 所有规划文档的唯一事实来源
│   └── EPIC-01_E-commerce_Payment/
│       ├── README.md
│       └── features/
│           └── FEAT-01_Credit_Card_And_PayPal/
│               ├── README.md
│               └── stories/
│                   └── PAY-124_Failed_Payment.md
│
├── src/                        # [实现层] 项目源代码
│   └── main/java/com/ecommerce/...
│
└── tests/                      # [验证层] 所有测试代码
    ├── bdd/
    │   ├── features/           # [规约层] BDD Gherkin 特性文件 (.feature)
    │   │   └── payment/
    │   │       └── payment_failure_handling.feature
    │   └── step_defs/
    │       └── test_payment_failure.py
    └── unit/
        └── com/ecommerce/payment/
            └── PaymentServiceTest.java
```

***

### **第三部分：**&#x56DB;阶段工作流程实践

#### **阶段一：战略规划与意图定义 (****`epics/`****&#x20;目录)**

在此阶段，人类领航员将业务需求转化为结构化的、版本化的 Markdown 文件，作为所有后续工作的"唯一事实来源"。

1. **定义 Epic 与 Feature**: 在 `epics/` 目录下，通过 `README.md` 文件定义高阶的商业目标和功能模块。
2. **撰写 AI-Story**: 在对应的 `stories/` 目录下，为每一个具体的可开发任务创建一个详尽的 `.md` 文件。这份文件是意图的核心。

#### **阶段二：任务执行准备 (AI Interaction)**

领航员触发脚本，为 AI 准备好所有材料，并组装最终的指令。

1. **触发任务**: 领航员在本地运行一个脚本，如 `sh start_ai_task.sh PAY-124`。
2. **生成工作区**: 脚本在 `.the_conn/ai_workspace/` 下创建 `PAY-124/` 目录。
3. **准备上下文**: 脚本在该目录中创建 `context.manifest.json` 和 `task.md`。
4. **组装并发送 Prompt**: 脚本加载 `.the_conn/ai_prompts/templates/task_execution_master.md` 模板，将 Persona、清单中的上下文、以及 `task.md` 的内容全部填充进去，形成最终的 prompt 发送给 AI。

#### **阶段三：代码实现与审查**

AI 根据指令执行开发任务，并由人类领航员进行质量把关。

1. **AI 生成规约与代码**: AI 首先根据 Story 中的 BDD 场景，创建或更新位于 `tests/bdd/features/` 目录下的 Gherkin 文件。然后，它会编写相应的 BDD 步骤定义（在 `tests/bdd/step_defs/`）和单元测试（在 `tests/unit/`），最后编写业务逻辑代码（在 `src/`）来让所有测试通过。
2. **AI 提交拉取请求 (Pull Request)**: AI 将所有相关代码变更提交为一个 PR。
3. **人类领航员审查**: 领航员审查代码的逻辑、架构符合性以及方案的优雅性。

#### **阶段四：同步与闭环**

在 PR 被最终批准并合并后，启动此流程，确保“意图”与“实现”的最终一致性。

1. **合并 PR**: 领航员将通过审查的 PR 合并到主分支。
2. **触发同步**: 领航员运行同步脚本，如 `sh sync_story.sh PAY-124`。
3. **脚本准备同步材料**: 获取该 PR 的最终 `git diff`，并读取原始的 story 文件。
4. **执行同步 Prompt**: 脚本使用 `.the_conn/ai_prompts/templates/story_synchronization.md` 模板，将原始 Story 和最终代码变更一同发给 AI，要求其更新 Story。
5. **领航员确认并提交**: AI 返回更新后的 Story 内容。领航员进行最终确认，然后将这个变更提交到 `epics/` 目录，完成闭环。

***

## **附录：文件示例与模板**

### **A.1. 规划文件 (****`epics/`****&#x20;目录)**

**`epics/EPIC-01_E-commerce_Payment/README.md`**

```markdown
# EPIC-01: 电子商务支付能力

- **业务价值**: 为用户提供安全、多样化的支付选项，预计能将订单转化率提升 5%。
- **范围**: 包括信用卡、PayPal 支付，以及后续的退款和对账功能。
- **关键指标**: `支付成功率`, `订单转化率`, `平均支付耗时`。
- **负责人**: @navigator-lead
```

**`epics/.../features/FEAT-01_Credit_Card_And_PayPal/README.md`**

```markdown
# Feature: FEAT-01 支持信用卡与 PayPal 支付

- **目标**: 实现端到端的信用卡和 PayPal 支付流程，包括成功和失败场景。
- **包含的故事**: `PAY-123 (成功支付)`, `PAY-124 (失败处理)`, `PAY-125 (PayPal 集成)`。
- **验收标准**:
  - 用户可以成功使用 Visa/Mastercard 支付。
  - 用户可以成功使用 PayPal 账户支付。
  - 所有支付失败都有明确的用户提示。
```

**`epics/.../stories/PAY-124_Failed_Payment.md`****&#x20;(AI-Story 源文件)**

```markdown
---
id: PAY-124
epic: EPIC-01_E-commerce_Payment
feature: FEAT-01_Credit_Card_And_PayPal
status: ready_for_dev
author: @navigator-lead
bdd_feature_file: tests/bdd/features/payment/payment_failure_handling.feature
---

# AI-Story: 信用卡支付的健壮错误处理

## 1. 业务动机
当前支付失败的反馈模糊，导致用户体验差、客服压力大。此任务旨在提供明确、可操作的错误反馈，提升支付成功率。

## 2. 用户故事
> 作为一个购物者，我想要在我使用无效信用卡支付时，能够看到明确区分的失败提示，以便于我能理解问题所在并快速采取行动。

## 3. 验收标准 (BDD Scenarios)
*此部分内容将被 AI 用来创建或更新位于 `tests/bdd/features/payment/payment_failure_handling.feature` 的 Gherkin 文件。*

**特性: 信用卡支付的错误反馈**
  为了提供清晰的用户指引，作为支付系统，我需要在支付失败时根据不同原因展示不同的提示信息。

  **场景: 因信用卡信息错误导致支付被拒**
    假如 一个待支付的订单
    而且 我使用一张已被银行因“信息错误”而拒绝的信用卡
    当 我尝试支付
    那么 我应该会看到提示信息："支付失败：银行拒绝了您的请求，请检查卡信息是否正确。"

  **场景: 因信用卡额度不足导致支付被拒**
    假如 一个待支付的订单
    而且 我使用一张因“额度不足”而被银行拒绝的信用卡
    当 我尝试支付
    那么 我应该会看到提示信息："支付失败：信用卡额度不足。"

## 4. 技术实现要点
- **核心文件**: `src/main/java/com/ecommerce/payment/PaymentService.java`
- **核心方法**: `processCreditCardPayment(...)`
- **异常处理**:
  - 捕获 `Gateway` 抛出的 `CardDeclinedException`，并检查其 `getDeclineReason()` 的返回值（`INSUFFICIENT_FUNDS` 或 `INVALID_CARD_DETAILS`）。
  - 捕获 `GatewayTimeoutException`。

## 5. 工作范围与边界
- **只允许修改**: `PaymentService.java` 及其测试类。
- **绝对禁止**: 修改 `Order` 模块或 `Gateway` 接口。
```

### **A.2. BDD Gherkin 文件 (****`tests/bdd/features/`****&#x20;目录)**

**`tests/bdd/features/payment/payment_failure_handling.feature`**

```gherkin
# language: zh-CN
# This file is auto-generated/updated by AI based on Story PAY-124.
# Manual edits might be overwritten.

特性: 信用卡支付的错误反馈
  为了提供清晰的用户指引并减少支付障碍，
  作为支付系统，
  我需要在支付失败时，根据不同的失败原因，向用户展示不同的提示信息。

  场景: 因信用卡信息错误导致支付被拒
    假如 一个待支付的订单
    而且 我使用一张已被银行因“信息错误”而拒绝的信用卡
    当 我尝试支付
    那么 支付应该失败
    而且 订单状态应保持为 "待支付"
    而且 我应该会看到提示信息："支付失败：银行拒绝了您的请求，请检查卡信息是否正确。"

  场景: 因信用卡额度不足导致支付被拒
    假如 一个待支付的订单
    而且 我使用一张因“额度不足”而被银行拒绝的信用卡
    当 我尝试支付
    那么 支付应该失败
    而且 我应该会看到提示信息："支付失败：信用卡额度不足。"
```

### **A.3. 上下文文件 (****`.the_conn/context/`****&#x20;目录)**

**`.the_conn/context/00_ARCHITECTURE.md`**

```markdown
# 项目架构总览

## 1. 核心设计原则
- **分层架构**: 严格遵循 `Controller` -> `Service` -> `Repository` 的分层结构。业务逻辑必须封装在 Service 层。
- **领域驱动设计 (DDD)**: 核心业务概念（如 Order, Payment）应被建模为富领域对象。
- **依赖倒置**: 服务应依赖于接口而非具体实现，通过依赖注入（DI）来管理。

## 2. 主要模块职责
- **`com.ecommerce.order`**: 负责订单创建、状态流转、查询。
- **`com.ecommerce.payment`**: 负责与第三方支付网关交互，处理支付和退款逻辑。
- **`com.ecommerce.user`**: 负责用户账户管理和认证。

## 3. 技术栈
- **后端**: Java 21, Spring Boot 3
- **数据库**: PostgreSQL 15
- **构建工具**: Maven
- **测试框架**: JUnit 5 (单元测试), Cucumber (BDD 测试)
```

### **A.4. AI 工作区文件 (****`.the_conn/ai_workspace/`****&#x20;目录)**

**`.the_conn/ai_workspace/PAY-124/context.manifest.json`**

```json
{
  "description": "Context files for task PAY-124: Payment Failure Handling. Includes high-level architecture for overall structure and the specific payment module design for implementation details.",
  "files": [
    ".the_conn/context/00_ARCHITECTURE.md",
    ".the_conn/context/15_PAYMENT_MODULE_DESIGN.md"
  ]
}
```

**`.the_conn/ai_workspace/PAY-124/task.md`****&#x20;(由脚本从 AI-Story 生成)**

````markdown
# AI 开发简报: [PAY-124] 信用卡支付的健壮错误处理

## 1. 核心目标
为信用卡支付流程添加健壮的异常处理逻辑，根据不同的失败原因（卡信息错误、额度不足）向用户返回明确的错误提示。

## 2. 验收标准 (BDD Scenarios)
你必须实现能让以下 Gherkin 场景通过的代码。这些场景定义了你的工作的“完成标准”。

```gherkin
特性: 信用卡支付的错误反馈
  为了提供清晰的用户指引，作为支付系统，我需要在支付失败时根据不同原因展示不同的提示信息。

  场景: 因信用卡信息错误导致支付被拒
    假如 一个待支付的订单
    而且 我使用一张已被银行因“信息错误”而拒绝的信用卡
    当 我尝试支付
    那么 我应该会看到提示信息："支付失败：银行拒绝了您的请求，请检查卡信息是否正确。"

  场景: 因信用卡额度不足导致支付被拒
    假如 一个待支付的订单
    而且 我使用一张因“额度不足”而被银行拒绝的信用卡
    当 我尝试支付
    那么 我应该会看到提示信息："支付失败：信用卡额度不足。"
```

## 3. 技术实现要点
核心文件: src/main/java/com/ecommerce/payment/PaymentService.java
核心方法: processCreditCardPayment(...)
异常处理: 捕获 CardDeclinedException 并检查其 getDeclineReason() 的返回值。

## 4. 工作范围与边界
只允许修改: PaymentService.java 及其测试类。
绝对禁止: 修改 Order 模块或 Gateway 接口。
````

**A.5. Prompt 模板 (`.the_conn/ai_prompts/` 目录)**

`.the_conn/ai_prompts/templates/task_execution_master.md`

```markdown
{{persona}}

你的任务是完成一项软件开发工作。请严格遵循以下所有指示。

### 1. 全局背景知识

这是你完成任务所需了解的项目架构和规范。

{{global_context}}

### 2. 当前核心任务简报
这是本次具体的任务简报，包含了你的目标、验收标准和工作范围。

{{task_brief}}

### 3. 指示
- 根据任务简报中的 BDD 场景，创建或更新对应的 .feature 文件。
- 编写必要的单元测试和 BDD 步骤定义。
- 编写业务逻辑代码以使所有测试通过。
- 提交一份包含所有变更的 PR 描述。

现在，请开始工作。

```

`.the_conn/ai_prompts/templates/story_synchronization.md`

````markdown
你是一位严谨的技术文档工程师。你的任务是确保我们的规划文档（AI-Story）与最终的代码实现保持 100% 一致。

请对比以下的【原始 Story】和【最终代码变更】，然后更新 Story 的内容。

**规则**:
1.  **只更新技术细节**: 你只能修改 "验收标准 (BDD Scenarios)" 和 "技术实现要点" 部分。
2.  **保持业务意图不变**: 绝对不能修改 "业务动机" 和 "用户故事" 部分。
3.  **精确对齐**: 确保 BDD 场景中的预期结果（如错误信息、状态）与代码中的实现完全匹配。
4.  直接输出更新后的完整 Story 文件内容（包括 frontmatter），不要添加任何额外的解释。

---

### **【原始 Story】**

```markdown
{{original_story_content}}

【最终代码变更 (Git Diff)】

{{final_code_diff}}
```

现在，请生成更新后的 Story 文件内容。

````
