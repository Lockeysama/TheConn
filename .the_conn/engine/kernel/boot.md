# The Conn Bootloader (启动引导程序)

## 🚀 启动序列 (Boot Sequence)

1.  **Phase 1: Environment Scan (环境扫描)**:
    *   读取 `context.manifest.json` (如果存在)。
    *   检查 Git 状态并在内存中构建文件树。

2.  **Phase 2: Intent Analysis (意图分析)**:
    *   使用 `triage` 技能解析用户输入。
    *   确定 `mode` (Planning vs Execution)。

3.  **Phase 3: Routing (路由)**:
    *   根据路由表选择 Playbook。

4.  **Phase 4: Skill Assembly (技能装配)**
    *   Load **Persona** (with `<static_skills>`).
    *   Load **Domain Strategies** (priorities & modifiers).
    *   Resolve **Dynamic Injections** from Playbook.

5.  **Phase 5: Execution (执行)**:
    *   将控制权移交给 Playbook。
    *   Kernel 监视所有权限访问。

## 🗺️ 路由表 (Routing Table)

| Intent / Command | Target Playbook | Required Persona |
| :--- | :--- | :--- |
| `tc review`, `review` | `playbooks/requirements_review.md` | `Tech Architect`, `Product Manager` |
| `tc plan`, `story` | `playbooks/story_writing.md` | `Product Manager` |
| `tc diff`, `change` | `playbooks/change_summary.md` | `Tech Architect` |
| `tc quick`, `fix` | `playbooks/quick_fix.md` | `QA Auditor` |
| `tc test`, `e2e` | `playbooks/e2e_story.md` | `QA Auditor` |

## ⚠️ 紧急协议 (Emergency Protocols)

*   **IF** `context.manifest.json` 已损坏 -> 则运行 `session_scan.md` 重建。
*   **IF** 用户请求不明确 -> 路由到 `playbooks/task_generation.md` 进行澄清。
