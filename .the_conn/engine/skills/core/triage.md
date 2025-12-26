# Skill: Triage (分诊与归属)

<skill_meta>
    <name>Triage (分诊)</name>
    <type>Core-Methodology (核心方法论)</type>
    <description>Analyzes raw requests to determine type, priority, and parent attribution.</description>
    <inputs>
        <arg name="request">User's raw input string</arg>
        <arg name="context">Current project context (Story list, git status)</arg>
    </inputs>
    <outputs>
        <result name="type">Bug Fix | Hotfix | Feature</result>
        <result name="attribution">Parent Story ID / Epic ID</result>
    </outputs>
</skill_meta>

## 🧠 分类算法 (Classification Logic)

### 1. Keyword Mapping (关键词映射)
| Type | Keywords (Match Any) | Strategy |
| :--- | :--- | :--- |
| **Bug Fix** | 崩溃, 失败, 异常, 错误, bug, crash, fail, error, exception, broken | **Contract-First**: Check if it violates existing Acceptance Criteria. |
| **Hotfix** | 优化, 增加, 改进, 调整, log, config, improve, optimize | **Value-Add**: Functionality is correct, but needs enhancement. |
| **Ambiguous** | 慢, 卡, slow, lag, timeout | **Performance Check**: Compare against defined SLAs. |

### 2. Attribution Logic (归属推断)

#### Priority 1: Explicit ID (显式 ID)
- **Input**: "Fix crash in STORY-123"
- **Action**: 直接链接到 `STORY-123`。

#### Priority 2: Context Search (上下文搜索)
- **Input**: "Login is broken"
- **Action**: 搜索活跃的故事以查找 "Login"。如果严格匹配到一个（状态：进行中/已完成），则归属于该故事。

#### Priority 3: Git Heuristic (Git 启发式)
- **Action**: 检查 `git status` 或 `git log -1`。
- **Logic**: 如果最近的文件属于特定的 Feature，则归属于该 Feature/Epic。

## 🔌 接口定义 (Signature)

```typescript
function Analyze(
  Request: string, 
  Context: ProjectState
): TriageResult {
  request_type: "BugFix" | "Hotfix";
  parent_id: string | null;
  confidence: number;
}
```
