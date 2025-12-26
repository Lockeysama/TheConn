# Skill: Code Review (代码审查)

<skill_meta>
    <name>Code Review (代码审查)</name>
    <type>Tech-Quality (技术质量)</type>
    <description>审查代码变更，确保符合架构规范、安全标准和可维护性要求。</description>
    <inputs>
        <arg name="diff">代码变更 (Diff)</arg>
        <arg name="context">相关的故事或任务</arg>
    </inputs>
    <outputs>
        <result name="comments">审查意见 (Comments)</result>
        <result name="approval">是否批准 (Status)</result>
    </outputs>
</skill_meta>

## 🧠 核心算法 (Algorithms)

### 1. Structure Check (架构检查)
- **Dependency Direction**: 是否违反了分层架构依赖？(例如: Domain 层依赖 UI 层)
- **Circular Dependency**: 是否引入了循环依赖？
- **Module Cohesion**: 修改是否破坏了模块内聚性？

### 2. Logic & Correctness (逻辑与正确性)
- **Edge Cases**: 空值、负数、极大值处理了吗？
- **Concurrency**: 线程安全吗？有无竞态条件？
- **Error Handling**: 异常是否被捕获并正确处理 (记录日志/返回错误码)？

### 3. Style & Readability (风格与可读性)
- **Naming**: 变量名是否清晰表达意图？
- **Complexity**: 函数是否过长？循环是否过深？
- **Comments**: 复杂逻辑是否有注释解释 "Why"？

## 🔌 接口定义 (Signature)

```typescript
function ReviewCode(
  Diff: string,
  Context: Task
): {
  comments: CodeComment[];
  status: "Approved" | "RequestChanges";
}
```
