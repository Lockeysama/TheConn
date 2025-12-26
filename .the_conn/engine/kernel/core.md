# The Conn Kernel: Core Constitution (核心宪法)

<kernel_core>
    <version>2.0.0</version>
    <status>ACTIVE (活跃)</status>
    <description>
        定义了 "Engine (引擎)" 和 "Runtime (运行时)" 之间的基本法则和关注点分离。
    </description>
</kernel_core>

## 1. 核心指令 (Prime Directives)

### Article I: Separation of Concerns (第一条: 关注点分离)
- **Engine (引擎) (Immutable)**: 包含 Persona 定义、Playbook 模板、核心技能和领域规则。这是系统的 "DNA"。
- **Runtime (运行时) (Mutable)**: 包含活动会话数据、任务清单、生成的工件 (Artifacts) 和临时上下文。这是系统的 "记忆"。
- **Rule**: Engine **从不** 写入自身。Engine 只写入 Runtime。

### Article II: The Trinity Model (第二条: 三位一体模型)
- **Persona (谁)**: 意图的持有者；通过 `<static_skills>` 装备能力。
- **Skill (怎么做)**: 无论谁在使用，都会产生确定性输出的执行算法。
- **Domain (在哪里)**: 提供 `<priorities>` (优先级) 和 `<skill_modifiers>` (技能修饰) 的战略上下文。

### Article III: Explicit Context (第三条: 显式上下文)
- **Rule**: 不要在没有加载 `context.manifest.json` 或 `session_scan.md` 的情况下假设以前的状态。
- **Rule**: 每一个动作都必须由特定的 Persona 归属并记录在执行跟踪中。

## 2. 权限模型 (Permission Model)

| Zone | Read Access | Write Access |
| :--- | :--- | :--- |
| **Engine/** | ✅ Universal | ❌ Forbidden (Requires Kernel Update) |
| **Runtime/** | ✅ Universal | ✅ Allowed (Via Transaction) |
| **User/Code** | ✅ Universal | ✅ Allowed (Via Playbook Output) |
