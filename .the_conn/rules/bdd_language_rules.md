# BDD Feature 语言配置规范

本文档定义 BDD Feature 文件的语言使用规则。

## ⚠️ 适用范围

**本规范仅适用于 E2E Story (`type: e2e_test`)**

- ✅ E2E Story: 使用 BDD 场景作为验收标准
- ❌ 普通 Story (`type: dev`, `type: bug_fix`): 使用功能清单，不需要 BDD

---

## 1. 语言决策规则

BDD Feature 文件的编写遵循以下原则：

1.  **关键字 (Keywords) 统一使用英文**：
    -   无论项目使用何种编程语言或自然语言，Gherkin 关键字（如 `Feature`, `Scenario`, `Given`, `When`, `Then`, `And`, `But`, `Background`, `Examples`, `Scenario Outline` 等）一律使用英文。
    -   **原因**：保持跨框架的兼容性，减少环境配置复杂度，且所有 BDD 框架原生均支持英文关键字。

2.  **描述 (Descriptions) 使用项目交互语言**：
    -   功能名称、场景描述、步骤详情等内容，应使用项目交互的自然语言。
    -   **判断逻辑**：
        1. **优先遵循指定**：检查 `Testing_Strategy.md` 或全局 Context 中是否有明确定义的语言设置。
        2. **上下文推断**：如果无明确指定，AI 应根据用户当前对话使用的自然语言（如中文或英文）进行自动适配。
    -   **原因**：确保团队成员和利益相关者（Stakeholders）能够以最自然的方式理解业务逻辑和验收标准。

---

## 2. 语法示例

### 示例：标准 BDD 格式 (English Keywords + Chinese Descriptions)

```gherkin
Feature: 用户登录

  Scenario: 用户成功登录
    Given 用户已注册
    When 用户输入正确的用户名和密码
    Then 用户应该成功登录
    And 页面应该跳转到首页

  Scenario Outline: 登录失败尝试
    Given 用户位于登录页面
    When 用户输入用户名 "<username>" 和密码 "<password>"
    Then 页面应显示错误信息 "<message>"

    Examples:
      | username | password | message |
      | admin    | wrong    | 密码错误 |
      | unknown  | 123456   | 用户不存在 |
```

---

## 3. AI 工作流程

1.  **识别项目自然语言**：通过项目文档（如 README.md）或用户对话识别当前工程使用的交互语言。
2.  **生成 Feature 文件**：
    -   **强制**使用英文 Gherkin 关键字。
    -   使用步骤 1 识别的自然语言编写所有描述性文本。
3.  **校验**：确保生成的 `.feature` 文件格式正确，关键字未被翻译。

---

**最后更新**: 2025-12-18
