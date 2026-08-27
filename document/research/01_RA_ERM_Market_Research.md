# Enterprise Resource Management (ERM) Market Research

## Introduction

**Purpose.** This document studies existing Enterprise Resource Management (ERM) / Enterprise Resource Planning (ERP) applications available in the market. It provides input for defining project goals and overall feature direction. It does not propose a design or architecture.

**Scope.**
- Covers ERM/ERP applications that manage factory-level business operations: production planning, inventory, procurement, quality management, scheduling, finance.
- ERM can consume data that originates on the factory floor (e.g. via a vendor's IoT/edge connectivity layer). This is in scope, and is discussed only to describe how ERM systems connect to and ingest floor data.
- ERM does not perform the equipment's job. Excluded: systems that execute or control work directly on the factory floor — CNC machine control, PLC/SCADA control, sensor management software — and the low-level connectivity hardware/software that bridges a device to a network.
- Does not define mandatory (must-have) requirements for the project; market survey only.

---

## 1. Common Features Across ERM/ERP Applications

The following features are present, in some form, across nearly all ERM/ERP products surveyed in this document:

- A centralized, shared database acting as a single source of truth across departments, removing duplicate data entry between finance, procurement, inventory, and production [1][2].
- A General Ledger (GL) / financial accounting module that other modules (accounts payable, accounts receivable, payroll, purchasing) post transactions into [4].
- An inventory management module tracking item quantity and location at the stock-keeping-unit (SKU) level [5].
- A procurement module managing purchase requisitions, purchase orders, vendor records, and invoice matching, integrated with finance and inventory rather than operating as a standalone tool [6].
- Order management / sales order processing.
- Reporting and analytics, ranging from static reports to embedded business intelligence (BI) dashboards [3].
- Role-based access control and audit/compliance tracking [3].
- A modular architecture, where functional areas (finance, HR, procurement, manufacturing, etc.) are delivered as separate but integrated modules [3][7].
- Deployment flexibility: most current-generation products offer a cloud/SaaS option, and several retain an on-premise or hybrid option [3].
- Mobile access to a subset of functions (approvals, inventory scanning, dashboards) [3].

Gartner, which coined the term "ERP" in 1990, defines it as an integrated application suite sharing a common process and data model across finance, human resources, distribution, manufacturing, and service [1]. This shared-data-model characteristic is the property that distinguishes ERP from a collection of standalone point tools [1][4].

---

## 2. Vendor Overview

The table below lists ten ERP/ERM products with manufacturing-sector applicability, their most notable features, and available pricing or deployment-cost information. Vendors publish list pricing only in isolated cases (Microsoft Dynamics 365, Odoo); for all other vendors, the figures shown are third-party estimates, not vendor-confirmed prices, and are marked as such.

| Vendor / Product | Most Notable Features | Price / Deployment Cost |
|---|---|---|
| **SAP S/4HANA** | In-memory HANA database for combined real-time transactional and analytical processing [8]; embedded PP/DS (constraint-based production planning and scheduling), previously a separate add-on product [9]; "Joule" generative-AI copilot for demand forecasting and planning, in S/4HANA Cloud since Dec. 2024 [10][11]; SAP Digital Manufacturing Cloud (DMC), a cloud MES with a Plant Connectivity (PCo) edge gateway for PLC/IIoT devices via OPC-UA/MQTT/REST [13][14]. | Deployment: public cloud (multi-tenant, "GROW with SAP"), private cloud ("RISE with SAP"), on-premise, sovereign cloud [12]. Pricing not published. Third-party estimate: public cloud ≈ $180–$400/user/month [15]. Estimated 3-year TCO for 100 users: $798K–$2.0M; full enterprise rollouts can exceed $50M including consulting [16]. |
| **SAP Business One** (SMB tier) | "Professional" vs. "Limited" user license tiers [17]; retains both cloud subscription and on-premise perpetual licensing, unlike S/4HANA's cloud-first direction [18]. No confirmed native DMC/IoT-MES bundling at this tier (gap, not confirmed absent). | Third-party estimate: cloud ≈ $95–$250/user/month; on-premise perpetual ≈ $3,500–$5,500/user one-time plus 18–20%/year maintenance [17]. Estimated 3-year TCO for 100 users: $370K–$630K [19]. |
| **Oracle Fusion Cloud ERP** | Over 50 embedded AI assistants across finance/supply chain/HR [20]; Fusion Cloud Manufacturing markets built-in IoT and AI for shop-floor scheduling [22]; 2025-era partnership with Microsoft Azure IoT Operations/Fabric for factory sensor data [21]; "Oracle IoT Intelligent Applications" for production, asset/fleet, and connected-worker monitoring [23]. | Cloud-only SaaS, standard 3-year term, 10-user minimum [20]. Third-party estimate: $175–$625/user/month overall, SCM/manufacturing ≈ $175–$250/user/month [20]. Implementation cost: not found in available sources. |
| **Oracle NetSuite** | Native Manufacturing Edition (WIP, MRP, mobile shop-floor scanning) and native warehouse management [27]. No native MES/IoT layer; relies on third-party MES integration [28]. | Cloud-only, multi-tenant [29]. Third-party estimate: base ≈ $999/month + $99–199/user/month; Manufacturing Edition ≈ $1,599/month base [30]. Implementation: $75K–$250K [31]. |
| **Microsoft Dynamics 365** (Finance & Supply Chain Mgmt. / Business Central) | Copilot-based demand planning that auto-selects a forecasting algorithm per product [33]; "Sensor Data Intelligence" ingesting real-time machine data via Azure IoT Hub/Stream Analytics for downtime, quality, and delay scenarios [34]; F&SCM supports discrete, process, lean, and hybrid manufacturing; Business Central supports discrete manufacturing only [35]. | SaaS-only; no perpetual license found. Official list pricing: Finance $210/user/month, Finance Premium $300/user/month, SCM $210/user/month [36]; Business Central Essentials $80/user/month, Premium $110/user/month, Team Member $8/user/month [37]. Business Central implementation: ≈ $30K–$100K+ [38]. |
| **Infor CloudSuite Industrial (SyteLine)** / **CloudSuite LN** | CSI targets mid-market discrete manufacturers (200–2,000 employees) with built-in Advanced Planning & Scheduling [42]; extends to the shop floor via Infor Factory Track (MES/mobility, barcode, IoT device integration) [43]; CloudSuite LN targets large/complex discrete and process manufacturers (aerospace, automotive) with multi-level BOM and formula management [44]; both share Infor OS, embedded Birst BI, and Coleman AI (demand sensing, predictive maintenance) [45]. Runs on AWS; 2026 Infor–AWS partnership on agentic AI for manufacturing [46][47]. | On-premise perpetual option also exists for CSI [48]. Third-party estimate: CSI ≈ $150/user/month, 5-user minimum, implementation from $25K; CloudSuite LN ≈ $150–$300/user/month, 20-user minimum, first-year total $450K (mid-market) to $6.5M+ (enterprise) [48]. |
| **Epicor Kinetic** | "Epicor Prism" generative-AI copilot for supplier RFQ automation; "Grow AI" ML suite for demand forecasting/inventory optimization, integrated into Prophet 21 order entry [51][56]; native no-code MES ("Epicor Connected Process Control") for digital work instructions [52]; "Advanced MES" captures real-time machine data without requiring OPC-compliant equipment, via a Machine Interface Unit [53]. | Both cloud SaaS and on-premise perpetual licensing offered [54]. Pricing not published. Third-party estimate: ≈ $100–200/user/month + $1,500–2,500/month base platform fee, ≈10-user minimum [54]. Implementation: $50K–$1M depending on scale. |
| **IFS Cloud** | Single codebase unifying ERP, Enterprise Asset Management (EAM), Field Service Management, SCM, PLM, and MES on one data model [57]; "IFS.ai" industrial AI backbone for predictive-failure detection and AI-driven scheduling [58]; composable, containerized "evergreen" architecture deployable to cloud, third-party cloud, or on-premise without reimplementation [59]; IoT/SCADA connectivity via MQTT/SOAP/EDI/XML/JSON [61]. | Pricing not published. Third-party estimate: $100–$300/user/month blended ("Full User" $110–200 vs. "Task User" $50–80) [60]. Implementation: $150K–$5M; large aerospace/defense deployments can exceed $3M/year [60]. |
| **Plex Systems** (Plex Smart Manufacturing Platform, part of Rockwell Automation) | Originated (1989–1995) as an internal MES at an automotive-parts manufacturer; acquired by Rockwell Automation for $2.22B (closed Sept. 2021) [63]. Native embedded MES from inception (finite scheduling, closed-loop quality, paperless operator workflows), now marketed under Rockwell's FactoryTalk brand [64]. ML-based demand forecasting via Plex DemandCaster (2022) [65]. Named a Leader in the IDC MarketScape: Worldwide Manufacturing Execution Systems 2024–2025 assessment (18 vendors evaluated) [67]. | Cloud-only SaaS, no on-premise option [66]. Third-party estimate: ≈ $300–650/user/month, commonly cited as starting around $500/user/month; implementation from $100K+. Target customer profile: $11M+ revenue, 50+ users [66]. |
| **QAD Adaptive ERP** | Acquired by Thoma Bravo (~$2B, 2021); acquired Redzone (connected-workforce/shop-floor platform) in 2023 [68][69]. Internationalization covers compliance in 66 countries — strong multi-site/global localization [70]. "ChampionAI" (2025): agentic (task-executing) AI spanning ERP and Redzone [71]. Blended cloud + on-premise deployment marketed since 2012 [72]. No dedicated native MES comparable to Plex found; shop-floor connectivity is delivered through the Redzone acquisition rather than an in-house MES (inferred, not explicitly vendor-confirmed). | Pricing not published. Third-party estimate: ≈ $90–300/user/month; mid-market annual cost $300K–$1.5M; implementation $100K–$2M [73]. |
| **Odoo** (Manufacturing/MRP) | Community Edition is open-source (LGPLv3, free); Enterprise Edition adds proprietary modules on the same data model [74]. Flat per-user price unlocks the full application suite (MRP, PLM, Quality, Maintenance, Inventory, Accounting) with no per-module fee [75]. "Odoo IoT Box" is a plug-and-play hardware bridge to barcode scanners, sensors, and cameras on the shop floor [76]. No dedicated named AI product found for the Manufacturing module specifically. | Deployment: Odoo Online (multi-tenant SaaS), Odoo.sh (PaaS), on-premise (Custom plan only) [75]. Official pricing: One App Free $0; Standard $8.95/user/month (annual); Custom $13.60/user/month (annual, adds on-premise option, multi-company, API access) [75]. |
| **Rootstock Cloud ERP** | Built natively on the Salesforce Platform, sharing its data model, UI, security model, and workflow engine [77]. Markets itself as "AI-native ERP on Salesforce," embedding Salesforce Einstein AI [78]. Extensible via Salesforce AppExchange and Rootstock's own "Signal Chain Appstore" [79]. No native IoT/shop-floor hardware layer; relies on MuleSoft/AppExchange middleware [83]. | Cloud/SaaS only, multi-tenant on the Salesforce Platform; no on-premise option [82]. Third-party estimate: Rootstock tiers from $100–145/user (base) [80], or $150–300/user/month plus a separate required Salesforce platform license of $25–300/user/month (blended ≈ $200–500/user/month total) [81]. |

Cross-vendor benchmark: Panorama Consulting reports a median ERP implementation timeline of 9 months and an average implementation cost of $450,000 across Tier-1 platforms (SAP, Oracle, Dynamics, Infor, and comparable systems) [32].

**Note on pricing confidence.** Except for Microsoft Dynamics 365 and Odoo, none of the vendors above publish enterprise-tier list pricing. All other dollar figures originate from third-party ERP-pricing aggregators (erpresearch.com, top10erp.org, costbench.com, erp-pilot.com) and should be read as directional estimates, not vendor-confirmed prices.

---

## 3. Trends: Connected Factory, Big Data, and IoT

All ten surveyed vendors have announced or shipped some form of shop-floor/IoT connectivity and analytics/AI capability. The maturity and native-vs-partner nature of this integration varies:

- **SAP**: SAP Digital Manufacturing Cloud (DMC) connects to PLCs and IIoT devices via a "Plant Connectivity" edge gateway, and SAP's edge-computing layer buffers and synchronizes production data between cloud and edge, continuing to operate during cloud outages [13][14]. Joule, SAP's generative-AI copilot, was extended into supply-chain planning applications in December 2024 [11].
- **Oracle**: Fusion Cloud Manufacturing is marketed as connecting the supply chain to the physical factory with built-in IoT and AI [22]; Oracle IoT Intelligent Applications cover production, asset, and connected-worker monitoring [23]; a 2026 partnership with Microsoft extends this to Azure IoT Operations and Microsoft Fabric [21]. Oracle publishes specific outcome claims (e.g., a 20% reduction in demand-forecasting error, up to 50% reduction in unplanned maintenance downtime) that are vendor-published without disclosed methodology or independent verification [25][26].
- **Microsoft**: The "Connected Factory" solution accelerator integrates with OPC Twin/Azure IoT Hub and Microsoft Fabric, and Copilot for Dynamics 365 Supply Chain Management (announced October 2023) provides conversational planning support [39][41]. At Hannover Messe 2026, Microsoft demonstrated an "agentic ERP" concept combining Copilot-based agents with Dynamics 365 [40].
- **Infor**: Markets digital-twin capability where ERP supplies order/material/priority context and the twin ingests IIoT data (run states, cycle times, alarms) [49]; Coleman AI is embedded across the Infor OS platform [45].
- **Epicor**: Epicor IoT gives a real-time shop-floor equipment view, and Kinetic is positioned as integrating IoT, MES, and AI/ML analytics into one ecosystem [55]; Advanced MES captures machine data without requiring OPC-compliant equipment [53].
- **IFS**: IFS Cloud embeds IoT for real-time equipment/production-line monitoring and predictive maintenance, and is marketed as requiring no middleware between ERP and asset management because EAM, ERP, and MES share one data model [62].
- **Rockwell Automation / Plex**: Positions Plex as a Smart Manufacturing Platform connecting MES, ERP, quality, and asset performance management, with stated full connectivity to third-party ERP systems [64]; independently, IDC named Rockwell (Plex + FactoryTalk) a Leader in its 2024–2025 Manufacturing Execution Systems MarketScape [67].
- **Odoo and Rootstock** represent the two ends of the IoT-integration spectrum among the vendors surveyed: Odoo ships its own IoT Box hardware bridge natively [76], while Rootstock has no native shop-floor/IoT layer and depends on Salesforce MuleSoft/AppExchange middleware [83].

**Independent (non-vendor) data on adoption.** The most reliable independently sourced, dated figures found are from Deloitte's 2025 Smart Manufacturing and Operations Survey (fielded Aug–Sep 2024, published May 2025): 46% of manufacturers report using industrial IoT (IIoT) at the facility or network level; 57% use cloud computing; 57% use data analytics; 29% have deployed AI/ML at facility or network level, with a further 23% piloting it; 24% have deployed generative AI at scale, with 38% piloting it [84]. Separately, a Gartner survey of ERP-buying organizations found that 47% intended to move the majority of core ERP to the cloud within five years, while only 2% had already done so, and 30% planned to keep the majority of ERP on-premises for the foreseeable future [85].

Several statistics circulating in secondary/aggregator sources (e.g., a claim that "65% of ERP vendors have integrated AI by 2025" or that "Gartner projects 75% of manufacturing ERP will natively support IoT by 2027") could not be traced to a primary source and are excluded from this document as unverifiable.

**Observation.** Nearly all vendor-specific connected-factory claims in this section originate from vendor marketing or vendor documentation rather than independent audits, and should be read as product capability descriptions, not verified performance benchmarks.

---

## 4. Adapting ERM to Factory Scale, Product Variety, and Multiple Factories

ERP vendors and implementers use a small number of recurring patterns to adapt a single ERP product line to factories of different size, product mix, and count:

- **Tiered product lines by company size.** Several vendors offer a lighter product for smaller sites alongside a full enterprise product (e.g., SAP Business One vs. S/4HANA [17][12]; Infor CloudSuite Industrial for mid-market vs. CloudSuite LN for large/complex manufacturers [42][44]).
- **Two-tier ERP for multi-site organizations.** Headquarters runs a heavily customized Tier-1 ERP for group finance and consolidation, while subsidiaries or smaller plants run a lighter Tier-2 cloud ERP, with data flowing up to the corporate system [86]. This reduces cost and increases local agility at subsidiary sites without requiring central-IT-level governance overhead at every site [87].
- **Global template rollout for multi-plant deployment of a single ERP.** A reusable template (process rules, data standards, roles, integration patterns, KPIs) is defined centrally and rolled out in waves; plants are grouped into cohorts by process similarity, criticality, and change capacity, and governance distinguishes "configuration" (approved local flexibility) from "customization" (unique logic requiring formal review) [88].
- **Single-instance vs. multi-instance architecture.** A single shared-database instance is generally recommended for mid- to upper-mid-market manufacturers expanding across sites, since it simplifies consolidation, master-data governance, security administration, and cross-site analytics [89]. Where multiple instances are required (e.g., due to regulatory or scale constraints), a master-data-governance function is needed to standardize product masters, chart of accounts, and reporting structures across instances [90]; without this governance, multi-site manufacturers tend to accumulate fragmented planning logic, inconsistent costing, and duplicate item masters [91].
- **Support for different manufacturing modes.** Some products explicitly support multiple product-type paradigms within one system — for example, Microsoft Dynamics 365 F&SCM supports discrete, process, lean, and hybrid manufacturing with formula management, while Business Central (its SMB-tier sibling) supports discrete manufacturing only [35]; Infor CloudSuite LN targets manufacturers needing multi-level bills of material and formula management for complex products such as aerospace and automotive components [44].
- **Internationalization/localization for global multi-factory operations.** QAD Adaptive ERP's internationalization module explicitly supports statutory/tax/regulatory compliance in 66 countries as a mechanism for standardizing one ERP product across geographically distributed factories [70].

---

## 5. Connectivity and Security Concerns

- **Expanded attack surface from IT/OT convergence.** Operational technology (OT) equipment on factory floors is frequently 5–20 years old and was not designed for network connectivity; connecting it to IT networks and ERP/IoT platforms creates an attack surface that many manufacturers do not fully account for [92]. Most OT-targeting attacks (cited at 75%) begin as conventional IT breaches — phishing, exposed RDP, compromised VPN — and then move laterally due to inadequate network segmentation between IT and OT [92].
- **Sector-specific threat volume.** Global ransomware incidents rose 32% in 2025 (7,419 incidents); manufacturing was the single most-targeted sector, with 1,466 incidents, up 56% year-over-year. Exploited vulnerabilities were the leading root cause (32%) of manufacturing ransomware incidents, and supply-chain-vector attacks nearly doubled (154 → 297 incidents) between 2024 and 2025 [93].
- **Relevant security standards.** ISA/IEC 62443 is the consensus standard series for securing Industrial Automation and Control Systems (IACS), covering technology, work processes, and human factors, structured by stakeholder role (asset owner, service provider, product developer); it was designated a "horizontal standard" in 2021 [94]. NIST SP 800-82 addresses securing industrial control systems (SCADA, DCS, PLCs); Revision 3 (superseding Revision 2, withdrawn September 2023) broadens scope to OT generally, reflecting increasing OT/IT integration [95][96]. NIST's Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover) and ISO/IEC 27001 substantially overlap: ISO 27001 certification is reported to cover roughly 83% of NIST CSF requirements, and NIST CSF roughly 61% of ISO 27001 requirements [97].
- **Cloud vs. on-premise responsibility split.** In cloud ERP, the provider is responsible for securing the underlying platform, while the customer remains responsible for access control, data governance, and integration security; cloud providers generally invest more in encryption, monitoring, and patching than an individual manufacturer could on its own [98]. Conversely, on-premise deployment is still preferred specifically for the scheduling/MES/machine-control layer in some analyses, due to latency, internet-dependency, and data-security concerns, even where the ERP system itself has moved to the cloud [99].
- **Protocol and integration risk between ERP and shop floor.** Legacy shop-floor devices often use unencrypted protocols (e.g., Modbus RTU) or proprietary serial links with no modern APIs, creating a protocol mismatch with cloud ERP; industry sources report that roughly 40% of ERP/MES integration projects in North American manufacturing fail due to data silos, inconsistent master data, and legacy protocols [100].
- **Data residency / regulatory constraints.** Migrating ERP to the cloud in the European Union must satisfy GDPR data-residency and sovereignty requirements, which a generic (non-region-pinned) cloud deployment may not meet without specific configuration [101].
- **Vendor architecture responses.** Some vendors address IT/OT connectivity risk by shipping their own native connectivity layer rather than relying on generic third-party middleware — for example, SAP's Plant Connectivity (PCo) edge gateway [14] and IFS Cloud's single-data-model integration of EAM, ERP, and MES [62] — while others (e.g., Rootstock) rely on general-purpose integration platforms (MuleSoft/AppExchange) for shop-floor connectivity [83]. No independent (non-vendor) analyst report comparing these approaches head-to-head was found; all "no middleware needed" claims originate from vendor or vendor-aligned sources.

---

## References

[1] TechTarget — ERP (Enterprise Resource Planning) definition. https://www.techtarget.com/searcherp/definition/ERP-enterprise-resource-planning

[2] IBM — What is ERP?. https://www.ibm.com/think/topics/enterprise-resource-planning

[3] CIO.com — What is ERP? Key features of top enterprise resource planning systems. https://www.cio.com/article/272362/what-is-erp-key-features-of-top-enterprise-resource-planning-systems.html

[4] NetSuite — ERP Finance Module. https://www.netsuite.com/portal/resource/articles/erp/erp-finance-module.shtml

[5] Oracle — ERP Modules. https://www.oracle.com/erp/erp-modules/

[6] NetSuite — ERP Modules. https://www.netsuite.com/portal/resource/articles/erp/erp-modules.shtml

[7] Gartner — Service-Centric Cloud ERP Solutions (glossary). https://www.gartner.com/en/information-technology/glossary/service-centric-cloud-erp-solutions

[8] SAP Community — S/4HANA with embedded PP/DS functionality. https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-members/s-4hana-with-embedded-pp-ds-functionality/ba-p/13396002

[9] SAPinsider — A Step Toward Understanding SAP S/4HANA Embedded PP/DS. https://sapinsider.org/a-step-toward-understanding-sap-s-4hana-embedded-pp-ds/

[10] SAP News — Joule, SAP's New Generative AI Assistant (Sept. 2023). https://news.sap.com/2023/09/joule-new-generative-ai-assistant/

[11] SAP News — Joule Available in SAP S/4HANA Cloud Supply Chain Management (Dec. 2024). https://news.sap.com/2024/12/joule-available-sap-s4hana-cloud-supply-chain-management/

[12] LeanIX — SAP S/4HANA Deployment Options. https://www.leanix.net/en/wiki/tech-transformation/sap-s4hana-deployment-options

[13] FORCAM — SAP Digital Manufacturing. https://forcam-enisco.net/en/sap-digital-manufacturing/

[14] SAP Help Portal — SAP Digital Manufacturing for Edge Computing, Integration Guide. https://help.sap.com/docs/sap-digital-manufacturing/integration-guide/sap-digital-manufacturing-for-edge-computing-integration

[15] ERP Research — SAP S/4HANA Public Cloud Pricing. https://www.erpresearch.com/pricing/sap-s4-hana-public-cloud

[16] CostBench — SAP S/4HANA. https://costbench.com/software/erp/sap-s4hana/

[17] ERP Research — SAP Business One Pricing. https://www.erpresearch.com/pricing/sap-business-one

[18] Top10ERP — SAP Business One Pricing. https://www.top10erp.org/products/sap-business-one/pricing

[19] CostBench — SAP Business One. https://costbench.com/software/erp/sap-business-one/

[20] ERP Research — Oracle ERP Fusion Cloud Pricing. https://www.erpresearch.com/en-us/oracle-erp-fusion-cloud-pricing

[21] Barchart — Oracle Collaborates With Microsoft to Enhance Supply Chain Efficiency. https://www.barchart.com/story/news/35460464/oracle-collaborates-with-microsoft-to-enhance-supply-chain-efficiency

[22] Oracle — Fusion Cloud Manufacturing / Smart Manufacturing. https://www.oracle.com/scm/manufacturing/smart-manufacturing/

[23] IT Orizon — Oracle IoT Intelligent Applications. https://itorizon.com/scm/oracle/internet-of-things/

[24] Oracle Blogs — From Industrial IoT Signals to Predictive Maintenance with Oracle AI Data Platform. https://blogs.oracle.com/ai-and-datascience/iot-predictive-maintenance-oracle-aidp

[25] Oracle — AI Demand Forecasting. https://www.oracle.com/scm/ai-demand-forecasting/

[26] Oracle — AI Predictive Maintenance. https://www.oracle.com/scm/ai-predictive-maintenance/

[27] Oracle NetSuite Documentation — Manufacturing Edition (PDF). https://docs.oracle.com/cloud/latest/netsuitecs_gs/NSMNF/NSMNF.pdf

[28] Nuage Consulting Group — NetSuite Advanced Manufacturing: Complete Guide. https://nuagecg.com/blog/netsuite-advanced-manufacturing-complete-guide/

[29] Broken Rubik — NetSuite Pricing: The Definitive Guide. https://www.brokenrubik.com/blog/netsuite-pricing-the-definitive-guide

[30] ERP Research — NetSuite Costs. https://www.erpresearch.com/en-us/netsuite-costs

[31] Kore1 — NetSuite Implementation Cost. https://www.kore1.com/netsuite-implementation-cost/

[32] Panorama Consulting — ERP Report Archives. https://www.panorama-consulting.com/resource-center/erp-report-archives/

[33] Microsoft Learn — Demand Planning Copilot (Dynamics 365 Supply Chain Management). https://learn.microsoft.com/en-us/dynamics365/supply-chain/demand-planning/demand-planning-copilot

[34] Microsoft Learn — IoT Intelligence Home Page (Dynamics 365 Supply Chain Management). https://learn.microsoft.com/en-us/dynamics365/supply-chain/supply-chain-dev/iot-intelligence-home-page

[35] Calsoft — Dynamics 365 Business Central vs. Finance & Supply Chain Management: Manufacturing Comparison. https://www.calsoft.com/dynamics-365-business-central-vs-finance-supply-chain-management-manufacturing-comparison/

[36] Microsoft — Dynamics 365 Finance Pricing. https://www.microsoft.com/en-us/dynamics-365/products/finance/pricing

[37] Microsoft — Dynamics 365 Business Central Pricing. https://www.microsoft.com/en-us/dynamics-365/products/business-central/pricing

[38] Nevastech — Dynamics 365 Business Central Pricing: A Complete 2026 Cost Guide. https://www.nevastech.com/blog/dynamics-365-business-central-pricing-a-complete-2026-cost-guide/

[39] Microsoft — Connected Factory (Azure IoT for Manufacturing). https://www.microsoft.com/en-US/enterprise/manufacturing/azure-iot-connected-factory

[40] HSO — Resilient Supply Chain Management in Uncertain Times with Copilot. https://www.hso.com/blog/resilient-supply-chain-management-in-uncertain-times-with-copilot

[41] Microsoft — Microsoft Announces New Copilot and Demand Planning Capabilities for Dynamics 365 Supply Chain Management (Oct. 2023). https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2023/10/31/microsoft-announces-new-copilot-and-demand-planning-capabilities-for-dynamics-365-supply-chain-management/

[42] ERP Research — Infor SyteLine / CloudSuite Industrial ERP Overview. https://www.erpresearch.com/en-us/infor-syteline-csi-erp-overview

[43] WM Synergy — Infor Factory Track for CloudSuite Industrial (SyteLine). https://wm-synergy.com/resource/infor-factory-track-for-cloudsuite-industrial-syteline/

[44] ERP Research — Infor LN vs. M3 vs. CloudSuite. https://www.erpresearch.com/en-us/infor-ln-vs-m3-vs-cloudsuite

[45] Top10ERP — Infor CloudSuite Industrial (SyteLine) vs. Infor LN. https://www.top10erp.org/erp-software-comparison/by-product/infor-cloudsuite-industrial-syteline_vs_infor-ln

[46] Infor — The Infor Cloud, Built on AWS. https://www.infor.com/resources/the-infor-cloud-built-on-aws

[47] AWS Press Center — Infor and AWS Bring Agentic AI to Manufacturing at Enterprise Scale (2026). https://press.aboutamazon.com/aws/2026/4/infor-and-aws-bring-agentic-ai-to-manufacturing-at-enterprise-scale

[48] ERP Pilot — Infor CloudSuite Pricing. https://www.erp-pilot.com/erp/erp-prices/infor-cloudsuite-pricing

[49] Infor — Digital Twin Manufacturing. https://www.infor.com/industries/industrial-manufacturing/digital-twin-manufacturing

[50] Infor — IoT in Manufacturing. https://www.infor.com/industries/industrial-manufacturing/iot-in-manufacturing

[51] E.C. Solutions — Epicor Grow AI / Epicor Prism. https://www.e-c-solutions.com/en/knowledge/blog/epicor-grow-ai-epicor-prism/

[52] Epicor — Epicor Connected Process Control. https://www.epicor.com/en/products/connected-worker/epicor-connected-process-control/

[53] Encompass — Advanced MES: Connected Factory Machine Interface Unit for Epicor Kinetic. https://encompass-inc.com/advanced-mes-connected-factory-machine-interface-unit-epicor-kinetic/

[54] ERP Research — Epicor Kinetic Pricing. https://www.erpresearch.com/pricing/epicor-kinetic

[55] Epicor — Epicor IoT. https://www.epicor.com/en/products/data-management-integration/epicor-iot/

[56] Epicor — Grow AI. https://www.epicor.com/en-us/products/ai-powered-applications/grow-ai/

[57] ERP Research — IFS ERP for Manufacturing. https://www.erpresearch.com/en-us/ifs-erp-manufacturing

[58] IFS — Manufacturing Industries. https://www.ifs.com/en/industries/manufacturing

[59] IFS — IFS Cloud. https://www.ifs.com/en/ifs-cloud

[60] ERP Research — IFS Applications Pricing. https://www.erpresearch.com/pricing/ifs-applications

[61] TNTRA — IFS Cloud Architecture, Security, Performance, Deployment Models. https://www.tntra.io/blog/ifs-cloud-architecture-security-performance-deployment-models/

[62] Astra Canyon — IFS ERP System for Smart Manufacturing: Integrating IoT, AI, Industry 4.0. https://www.astracanyon.com/blog/ifs-erp-system-for-smart-manufacturing-integrating-iot-ai-industry-4.0

[63] Wikipedia — Plex Systems. https://en.wikipedia.org/wiki/Plex_Systems

[64] Rockwell Automation — FactoryTalk OperationSuite MES: Plex MES. https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes/plex-mes.html

[65] Business Wire — Plex Systems Introduces Machine Learning to Help Companies Improve Demand Forecasting Accuracy (June 2022). https://www.businesswire.com/news/home/20220602005215/en/Plex-Systems-Introduces-Machine-Learning-to-Help-Companies-Improve-Demand-Forecasting-Accuracy

[66] ERP Research — Plex ERP. https://www.erpresearch.com/en-us/plex-erp

[67] Rockwell Automation / Plex — Rockwell Automation Named a Leader, 2024–2025 IDC MarketScape: Worldwide Manufacturing Execution Systems. https://plex.rockwellautomation.com/en-us/resources/rockwell-automation-named-leader-2024-2025-idc-marketscape-worldwide-manufacturing.html

[68] QAD — Thoma Bravo Completes Acquisition of QAD (2021). https://www.qad.com/about/news/-/room/read/2021/thoma-bravo-completes-acquisition-of-qad

[69] Wikipedia — QAD Redzone. https://en.wikipedia.org/wiki/QAD_Redzone

[70] QAD — Adaptive ERP Internationalization. https://www.qad.com/solutions/adaptive-erp/internationalization

[71] QAD — QAD Launches Latest ERP Evolution: QAD Adaptive Powered with Agentic Champion AI (2025). https://www.qad.com/about/news/-/room/read/2025/qad-launches-latest-erp-evolution-qad-adaptive-powered-with-agentic-champion-ai

[72] QAD — QAD Allows Global Customers to Blend Deployment of ERP in the Public Cloud and On-Premise (2012). https://www.qad.com/about/news/-/room/read/2012/qad-allows-global-customers-to-blend-deployment-of-erp-in-the-public-cloud-and-on-premise-an-industry-first-for-manufacturing

[73] ERP Research — QAD ERP Pricing. https://www.erpresearch.com/pricing/qad-erp

[74] Odoo — Editions (Community vs. Enterprise). https://www.odoo.com/page/editions

[75] Odoo — Pricing Plan. https://www.odoo.com/pricing-plan

[76] Tenth Planet — IoT Management in Odoo 18 (IoT Box). https://tenthplanet.in/odoo/product/iot/iot-management-in-odoo-18/

[77] Rootstock — Salesforce for Manufacturing. https://www.rootstock.com/salesforce-for-manufacturing/

[78] Rootstock — Home page (AI-native ERP on Salesforce). https://www.rootstock.com/

[79] Business Wire — Rootstock ERP Launches Appstore for Manufacturing (2024). https://www.businesswire.com/news/home/20240327508373/en/Rootstock-ERP-Launches-Appstore-for-Manufacturing/

[80] Software Connect — Rootstock Cloud ERP Reviews (pricing). https://softwareconnect.com/reviews/rootstock-cloud-erp/

[81] ERP Research — Rootstock Pricing. https://www.erpresearch.com/pricing/rootstock

[82] G2 — Rootstock Cloud ERP Reviews. https://www.g2.com/products/rootstock-cloud-erp/reviews

[83] Rootstock — Enterprise Integration: Salesforce's Acquisition of MuleSoft Puts a Number on the Enterprise Integration Problem. https://www.rootstock.com/cloud-erp-blog/enterprise-integration-salesforces-acquisition-of-mulesoft-puts-a-number-on-the-enterprise-integration-problem/

[84] Deloitte — 2025 Smart Manufacturing and Operations Survey. https://www.deloitte.com/us/en/insights/industry/manufacturing/2025-smart-manufacturing-survey.html

[85] SilverEdge — More Firms Moving to Cloud ERP, According to Gartner Report. https://www.silveredge.com/more-firms-moving-to-cloud-erp-according-to-gartner-report/

[86] NetSuite — Two-Tier ERP. https://www.netsuite.com/portal/resource/articles/erp/two-tier-erp.shtml

[87] TechTarget — Two-Tier ERP (definition). https://www.techtarget.com/searcherp/definition/two-tier-ERP

[88] Umbrex — Manufacturing Execution System Playbook: Multi-Plant Template and Global Rollout Strategy. https://umbrex.com/resources/manufacturing-execution-system-playbook/multi-plant-template-and-global-rollout-strategy/

[89] SAP PRESS Blog — When to Choose a Single Instance of SAP S/4HANA Versus Multiple Instances. https://blog.sap-press.com/when-to-choose-a-single-instance-of-sap-s4hana-versus-multiple-instances

[90] SAP Blogs — SAP MDG: One Instance vs. Multiple Instances, Food for Thought. https://blogs.sap.com/2022/10/28/sap-mdg-mdm-one-instance-vs-multiple-instances-food-for-thought/

[91] SysgenPro — Manufacturing ERP for Operational Governance. https://resources.sysgenpro.com/manufacturing-erp-for-operational-governance

[92] Petronella Technology Group — OT/IT Security in Manufacturing. https://petronellatech.com/blog/ot-it-security-manufacturing/

[93] Industrial Cyber — Manufacturing Absorbs 56% Ransomware Surge of Global Attacks in 2025 as RaaS, Legacy OT, Supply Chains Fuel Spike. https://industrialcyber.co/manufacturing/manufacturing-absorbs-56-ransomware-surge-of-global-attacks-in-2025-as-raas-legacy-ot-supply-chains-fuel-spike/

[94] ISA — ISA/IEC 62443 Series of Standards. https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards

[95] NIST Computer Security Resource Center — SP 800-82 Rev. 2 (Guide to Industrial Control Systems Security). https://csrc.nist.gov/pubs/sp/800/82/r2/final

[96] Corsha — NIST SP 800-82 Revision 3: Making the Case for OT Cybersecurity. https://corsha.com/blog/nist-sp-800-82-revision-3-making-the-case-for-ot-cybersecurity

[97] CyberSaint — NIST vs. ISO: What You Need to Know. https://www.cybersaint.io/blog/nist-vs.-iso-what-you-need-to-know

[98] Kopis — Cloud ERP Security vs. On-Premise. https://kopisusa.com/cloud-erp-security-vs-on-prem/

[99] SysgenPro — Cloud ERP vs. On-Premise ERP Security Comparison for Manufacturing CIOs. https://sysgenpro.com/compare/cloud-erp-vs-on-premise-erp-security-comparison-for-manufacturing-cios

[100] SoftDoes — Industrial Data Integration Guide. https://softdoes.com/insights/industrial-data-integration-guide

[101] Eastgate Software — EU ERP Modernization (GDPR/data residency). https://eastgate-software.com/insights/eu-erp-modernization/
