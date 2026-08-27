# D1–D3 Technology Challenge Alignment with ERM Application Scope

## Introduction

**Purpose.** This document assesses whether the requirements of Denso Hackathon 2026 Technology Challenges D1, D2, and D3 [1] align with the capabilities and scope of an Enterprise Resource Management (ERM) application, as characterized in `01_RA_ERM_Market_Research.md` [2].

**Scope.** This assessment is limited to two sources only: the Denso Hackathon 2026 "Technology Challenges" page [1] and the existing ERM market research document [2]. It does not evaluate the technical feasibility of any challenge, does not recommend a solution architecture, and does not define project requirements. All ERM-related claims in this document are traceable to specific sections of [2]; no new ERM vendor, feature, or trend claims are introduced.

**Note on source [1].** A direct fetch of https://densohackathon.vn/theme returned only the page heading ("DENSO Factory Hacks 2026"); the "Technology Challenges" section content (challenge cards D1–D3) did not render via automated fetch, consistent with the page being JavaScript-rendered. The challenge content analyzed below is the verbatim transcription of that section supplied as ground truth, attributed to [1].

---

## 1. Per-Challenge Alignment Verdicts

**Scope boundary carried from [2].**
- ERM can consume data that originates on the factory floor — [2], Introduction — Scope, allows this and discusses it only to describe how ERM systems connect to and ingest floor data.
- ERM does not perform the equipment's job — [2], Introduction — Scope, excludes systems that execute or control work on the factory floor (CNC machine control, PLC/SCADA control, sensor management software), and excludes building the low-level device-to-network connectivity itself.
- This directly affects D1, which is fundamentally a PLC-to-server device-connectivity build (not data consumption), and the "Manufacturing layer" half of D3.

### D1 — Low-Cost Connectivity for Non-IPC Legacy Equipment: **No**

- **Core deliverable:** a low-cost, rapidly deployable PLC–IPC edge gateway that reads legacy PLC data and forwards it to a server [1].
- **Pain point:** legacy, non-IPC equipment has no affordable, fast path to reach a server today — the challenge is solving connectivity at the device/network edge itself [1].
- **ERM gap:** [2]'s own Scope excludes building this device-to-network bridge entirely; ERM only consumes data after it already reaches a standard connector (e.g., SAP Plant Connectivity, IFS MQTT/SOAP) [2, Introduction; Section 3]. No ERM vendor in [2] is documented as providing the gateway itself, or the low-cost/rapid-deployment prototype and cost-comparison deliverables D1 asks for [2, Sections 3, 5].

### D2 — Simulate & Forecast Logistics, Recommend Actions: **Partial**

- **Core deliverable:** a Predict–Detect–Simulate logistics system with a Control-Room-style dashboard and a forecast/bottleneck/action-recommendation report [1].
- **Pain point:** the most demanding ask is discrete-event, what-if simulation to recommend actions — going beyond passive forecasting into active scenario testing [1].
- **ERM gap:** [2] documents demand forecasting and embedded BI dashboards broadly across vendors (SAP Joule, Microsoft Copilot demand planning, Epicor Grow AI, Infor Coleman AI, Plex DemandCaster) [2, Sections 1–2], but no vendor in [2] is documented as offering discrete-event simulation or what-if scenario modeling — that capability is absent from ERM's documented feature set [2, Section 2].

### D3 — Link Production-Chain Data & Predict Incident Impact/Cause: **Partial**

- **Core deliverable:** a production-chain data-linkage model plus an impact-propagation inference engine that recommends department-specific actions [1].
- **Pain point:** the hardest ask is predicting how a change or incident cascades across departments/layers — impact-propagation and cause inference, not just data linkage [1].
- **ERM gap:** [2]'s centralized shared database covers cross-department data sharing [2, Section 1], but knowledge-graph modeling, impact-propagation inference, and rule-based cause/effect reasoning are not documented as ERM features anywhere in [2]. The "Manufacturing layer" half of the required linkage also falls outside ERM's scope per [2]'s Introduction.

---

## 2. Requirement-Level Comparison Table

| Challenge | Requirement/Deliverable Point | Covered by ERM per [2]? | Basis |
|---|---|---|---|
| D1 | Develop a simple, low-cost, rapidly deployable PLC–IPC connectivity solution | No | Shop-floor device connectivity is explicitly excluded from ERM scope per [2], Introduction — Scope. |
| D1 | Collect data from legacy PLCs and transmit to a server | Partial | ERM vendor edge/connectivity layers (e.g., SAP Plant Connectivity, Microsoft Azure IoT Hub ingestion) receive data of this kind per [2], Section 3, but the PLC-side collection task itself is out of ERM scope per [2], Introduction. |
| D1 | Deliverable: Low-cost connectivity prototype | No | Hardware/edge prototype is not an ERM application feature; falls under [2], Introduction — Scope exclusion. |
| D1 | Deliverable: Server data transmission demo | Partial | Analogous to vendor edge-gateway data ingestion described in [2], Section 3, but the demo itself is device/edge-layer work, not an ERM feature. |
| D1 | Deliverable: Cost and implementation time comparison report | No | Not a documented ERM application feature in [2]; no comparable reporting feature tied to connectivity cost/time exists in Section 1 or 2. |
| D1 | Tech stack: OPC-UA/Modbus | Partial | OPC-UA appears as a connectivity protocol for ERM vendor edge gateways (SAP PCo) per [2], Section 3; Modbus RTU appears as a legacy shop-floor protocol risk in [2], Section 5. Protocol overlap exists, but implementing it is outside ERM's own feature set. |
| D1 | Tech stack: Low-cost Gateway (Raspberry Pi/ESP32) | No | Not mentioned anywhere in [2]; hardware gateway falls under the excluded shop-floor/device category per [2], Introduction. |
| D1 | Tech stack: MQTT | Partial | MQTT appears as a connectivity protocol in ERM vendor edge layers (SAP PCo, IFS Cloud) per [2], Section 3, but only as a way ERM connects outward, not as an ERM feature itself. |
| D1 | Tech stack: Node-RED | No | Not mentioned anywhere in [2]. |
| D2 | Predict logistics capacity | Yes | Matches AI/ML-based demand forecasting documented across multiple vendors per [2], Section 2 (SAP Joule, Microsoft Copilot demand planning, Epicor Grow AI, Infor Coleman AI, Plex DemandCaster), and reporting/analytics per [2], Section 1. |
| D2 | Detect bottlenecks | Partial | Related to production planning/scheduling features (SAP embedded PP/DS, Infor Advanced Planning & Scheduling) per [2], Section 2, and BI/analytics per [2], Section 1, but "bottleneck detection" is not itself a named ERM feature. |
| D2 | Simulate what-if scenarios to recommend actions | No | Discrete-event or what-if simulation is not documented anywhere in [2] as an ERM/ERP feature. |
| D2 | Deliverable: Predict–Detect–Simulate system | Partial | Composite of the three rows above: forecasting component is Yes, bottleneck detection is Partial, simulation component is No, per [2], Sections 1–2. |
| D2 | Deliverable: Control Room-style dashboard | Yes | Directly matches "Reporting and analytics, ranging from static reports to embedded BI dashboards" per [2], Section 1. |
| D2 | Deliverable: Forecast, bottleneck, and action recommendation report | Partial | Forecast reporting matches [2], Sections 1–2; bottleneck and action-recommendation reporting are not specifically documented ERM features. |
| D2 | Tech stack: Time-series Forecast (Prophet/LSTM) | Yes | Aligns with vendor-documented AI/ML demand-forecasting capability per [2], Section 2 (e.g., SAP Joule, Plex DemandCaster ML forecasting). |
| D2 | Tech stack: Discrete-event Simulation (SimPy/AnyLogic) | No | Not documented anywhere in [2]. |
| D2 | Tech stack: Optimization | Partial | Loosely related to "AI-driven scheduling" (IFS.ai) and "constraint-based production planning and scheduling" (SAP embedded PP/DS) per [2], Section 2, but general-purpose "optimization" is not itself a named ERM feature. |
| D2 | Tech stack: Dashboard | Yes | Matches embedded BI dashboards per [2], Section 1. |
| D3 | Connect production-chain data through Logic and Manufacturing layers | Partial | The "Logic" (business/ERP) side matches ERM's centralized shared database / single source of truth per [2], Section 1; the "Manufacturing layer" side falls into the shop-floor/device-control territory excluded per [2], Introduction — Scope. |
| D3 | Analyze impact propagation | No | Impact propagation analysis is not documented anywhere in [2] as an ERM feature. |
| D3 | Recommend actions for each department when changes occur | Partial | Loosely analogous to ERM's modular, role-based structure spanning departments per [2], Section 1, but automated cross-department change-impact recommendation is not a documented ERM feature. |
| D3 | Deliverable: Production-chain data linkage model | Partial | Data-linkage across departments matches the centralized shared-database concept in [2], Section 1; linkage extending into the manufacturing/device layer is outside ERM scope per [2], Introduction. |
| D3 | Deliverable: Impact propagation inference engine | No | Not documented anywhere in [2]. |
| D3 | Deliverable: Department-specific action recommendations for three scenarios | Partial | Department/module structure and role-based access exist per [2], Section 1, but scenario-based action recommendation is not a documented ERM feature. |
| D3 | Tech stack: Knowledge Graph (Neo4j/RDF) | No | Not mentioned anywhere in [2]. |
| D3 | Tech stack: Impact/What-if Propagation | No | Not documented anywhere in [2]. |
| D3 | Tech stack: Rule + Machine Learning | Partial | Machine learning is broadly documented across ERM vendors' AI features per [2], Sections 2–3, but a rule engine for propagation/cause inference is not documented. |
| D3 | Tech stack: Dashboard | Yes | Matches embedded BI dashboards per [2], Section 1, consistent with the D2 dashboard row. |

---

## 3. Closing Synthesis

Based solely on the table above:

- **D1 sits outside ERM's documented scope.** Every requirement/deliverable point is rated No or, at best, Partial via incidental protocol overlap (OPC-UA/Modbus/MQTT appearing in ERM vendors' connectivity layers per [2], Section 3). The challenge's core task — building a PLC-to-server device gateway — falls squarely within the shop-floor/device-control category that [2]'s Introduction/Scope excludes from ERM.
- **D2 is mixed, weighted toward ERM's documented scope.** Forecasting and dashboard/reporting requirements (4 of 10 rows rated Yes) align directly with ERM features documented in [2], Sections 1–2. Bottleneck detection and optimization are Partial (2 rows). Discrete-event/what-if simulation (2 rows, including the composite system deliverable) is not documented as an ERM feature in [2].
- **D3 is mixed, weighted toward outside ERM's documented scope.** Only the dashboard requirement is a clean Yes. Data linkage and department-recommendation requirements are Partial, tracing to ERM's shared-database and modular/role-based structure per [2], Section 1, but qualified by the excluded manufacturing-layer connection. Knowledge-graph modeling and impact-propagation/inference mechanics (3 of 8 rows) are not documented anywhere in [2].

Overall: D2 is the challenge with the largest fraction of requirements traceable to documented ERM features in [2]; D1 has the smallest; D3 falls in between but leans toward outside ERM's documented scope, primarily due to its manufacturing-layer linkage and knowledge-graph/inference requirements.

---

## References

[1] Denso Hackathon 2026 — Technology Challenges — https://densohackathon.vn/theme

[2] `01_RA_ERM_Market_Research.md` — Enterprise Resource Management (ERM) Market Research (internal document)
