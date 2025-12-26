# The Conn Kernel: Registry (注册表)

<kernel_registry>
    <version>2.0.0</version>
    <description>
        映射 Domain -> Rules, Persona -> Files 的中心。
    </description>
</kernel_registry>

## 1. Domain Registration (领域注册)

| Domain ID | Strategy File | Description |
| :--- | :--- | :--- |
| `tech.frontend` | `engine/domains/tech/frontend/rules.md` | React, CSS, Accessibility |
| `tech.backend` | `engine/domains/tech/backend/rules.md` | API, Database, Security |

## 2. Persona Registration (角色注册)

| Persona ID | Definition File | Role |
| :--- | :--- | :--- |
| `tech_arch` | `engine/personas/tech_arch.md` | Technical Architect |
| `product_mgr` | `engine/personas/product_mgr.md` | Product Manager |
| `qa_auditor` | `engine/personas/qa_auditor.md` | QA Auditor
