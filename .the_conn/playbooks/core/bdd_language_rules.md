# BDD Feature 语言配置规范

本文档定义 BDD Feature 文件的语言使用规则。

---

## 1. 双重语言判断机制

BDD Feature 需要判断两个维度的语言：

### 维度 1：编程语言（决定测试框架）
- 项目使用 Go → 使用 godog
- 项目使用 Python → 使用 pytest-bdd 或 behave
- 项目使用 JavaScript/TypeScript → 使用 cucumber-js
- 项目使用 Java → 使用 Cucumber JVM

### 维度 2：自然语言（决定 Gherkin 关键词）
- 检查该 BDD 框架是否支持用户对话使用的自然语言
- 如果支持 → 使用对话自然语言的 Gherkin 关键词
- 如果不支持 → 使用英文 Gherkin 关键词（默认）

---

## 2. AI 工作流程

```
1. 检查 global Context → 获取项目配置的框架和关键词
2. 识别项目编程语言 → 确定 BDD 框架（用户可指定）
3. 识别用户对话自然语言 → 确定期望的 Gherkin 语言
4. 根据分析结果 → 决定实际使用的 Gherkin 关键词
```

---

## 3. 框架语言支持参考表

| 编程语言      | 常用 BDD 框架 | 支持中文 | 支持英文 | 其他语言支持 |
| ------------- | ------------- | -------- | -------- | ------------ |
| Go            | godog         | ✅        | ✅        | 多语言支持   |
| Python        | pytest-bdd    | ✅        | ✅        | 多语言支持   |
| Python        | behave        | ✅        | ✅        | 多语言支持   |
| JavaScript/TS | cucumber-js   | ✅        | ✅        | 多语言支持   |
| Java          | Cucumber JVM  | ✅        | ✅        | 多语言支持   |
| Ruby          | cucumber      | ✅        | ✅        | 多语言支持   |
| C#            | SpecFlow      | ✅        | ✅        | 多语言支持   |

**⚠️ 重要说明**：
1. **此表仅供参考**，用户可以指定任意 BDD 框架
2. **不同框架的关键词可能不同**，即使都支持中文，关键词也可能有差异
3. **AI 必须先查阅框架文档或分析项目配置，再确定使用的关键词**

---

## 4. 语法示例

### 场景 1：Go 项目 + 中文对话

```
编程语言: Go → BDD 框架: godog
对话语言: 中文 → 期望: 中文 Gherkin
godog 支持中文: ✅ 是 → 使用中文关键词
```

```gherkin
功能: 用户登录

  场景: 用户成功登录
    假如 用户已注册
    当 用户输入正确的用户名和密码
    那么 用户应该成功登录
    而且 页面应该跳转到首页
```

### 场景 2：Python 项目 + 中文对话

```
编程语言: Python → BDD 框架: pytest-bdd
对话语言: 中文 → 期望: 中文 Gherkin
pytest-bdd 支持中文: ❌ 否 → 使用英文关键词
```

```gherkin
Feature: User Login  # 框架不支持中文，使用英文

  Scenario: User logs in successfully
    Given the user is registered
    When the user enters correct username and password
    Then the user should be logged in
    And the page should redirect to home
```

### 场景 3：JavaScript 项目 + 英文对话

```
编程语言: JavaScript → BDD 框架: cucumber-js
对话语言: 英文 → 期望: 英文 Gherkin
cucumber-js 支持英文: ✅ 是 → 使用英文关键词
```

```gherkin
Feature: User Login

  Scenario: User logs in successfully
    Given the user is registered
    When the user enters correct username and password
    Then the user should be logged in
    And the page should redirect to home
```

---

## 5. 特殊情况处理

- 如果无法确定框架的语言支持 → 默认使用英文 Gherkin 关键词
- 用户明确指定语言 → 遵循用户指定
- 框架不支持但用户坚持 → 警告用户可能无法执行

---

**注意**：以上中文关键词（功能/场景/假如/当/那么）是基于 godog 框架的。不同框架可能使用不同的中文关键词，AI 必须先分析具体框架的语法支持。

**最后更新**: 2025-12-16

