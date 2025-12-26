# Playbook: Session Profile Scanner (会话扫描)

## ⚠️ 核心公约加载 (Core Constitution)
**必须遵守**: `@engine/kernel/core.md`

## 🎭 技能装配 (Skill Assembly)

### 1. 核心角色 (Personas)
- **Primary**: Tech Architect (`@engine/personas/tech_arch.md`)
  - **Mindset**: Context Awareness (环境感知)

### 2. 动态注入 (Dynamic Injection)
```xml
<dynamic_injection>
    <inject ref="core/triage" reason="Stack Analysis" stage="Step 1" />
</dynamic_injection>
```

---

## 🧭 执行追踪 (Execution Trace)

```xml
<execution_trace>
    <step id="1" status="pending">Stack Detection (技术栈检测)</step>
    <step id="2" status="pending">Legacy Profile Scan (旧配置扫描)</step>
    <step id="3" status="pending">Generate Session Profile (生成会话快照)</step>
</execution_trace>
```

---

## 🧭 扫描流程 (Scan Process)

### Step 1: 技术栈检测 (Stack Detection)
分析项目根目录特征：
- `package.json` -> Node.js / Frontend
- `go.mod` -> Go
- `requirements.txt` / `pyproject.toml` -> Python
- `pom.xml` / `build.gradle` -> Java

识别关键框架 (React, Gin, Django, Spring Boot)。

### Step 2: 旧配置扫描 (Legacy Profile Scan)
检查旧版配置 (Migration Adaptor):
- `.the_conn/context/global/Tech_Stack.md`
- `.the_conn/context/project_profile.json`

### Step 3: 生成会话快照 (Generate Session Profile)
生成目标文件：`.the_conn/runtime/context/session_profile.json`

**JSON Schema**:
```json
{
  "project_name": "String",
  "tech_stack": {
    "language": ["Python", "Go"],
    "framework": ["Django", "Gin"],
    "db": ["PostgreSQL", "Redis"]
  },
  "constraints": {
    "legacy_support": true,
    "deployment": "k8s"
  },
  "complexity_level": "High/Medium/Low",
  "migration_status": "v2_ready"
}
```

---

## ✅ 输出要求 (Artifacts)
- 确保 JSON 格式标准。
- 如果检测到旧版配置，尽量保留关键信息。
- 设置 `migration_status` 为 `v2_ready` 以告知 Core Engine 准备就绪。
