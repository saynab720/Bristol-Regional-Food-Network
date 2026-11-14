# BRISTOL REGIONAL FOOD NETWORK

## distributed entrerprise software development project group 36

## case study
Bristol Regional Food Network is a community marketplace that connects around forty small to medium local food producers with customers within twety miles of bristol.
This repository holds our groups analysis, models and executable processes for **Use case 1: Producer product listing and inventory management.** 

we model the enterprise at a strategic level, analyse its stakeholders with i\*, and automate two business processes in **Camunda 8**:

1. **Product listing and verification:** a producer submits a product; the platform validates it, checks any organic claim with an external certification body, and publishes it. Invalid details loop back to the producer, and if the certification service is unavailable an administrator reviews it manually.
2. **Stock and seasonal availability:** when a producer updates stock or availability dates, the platform decides whether the product is available, out of stock or out of season, and notifies the producer.

This work carries forward into Task 2, where it is integrated into a Django REST Framework and Docker product.

## TEAM 
| Name | Github | Role 



**Module team:** Khoa Phung, Dilshan Jayatilake

## Deliverables
 
| Deliverable | Sprint | Location |
|---|---|---|
| Stakeholder analysis | 1 | [`docs/stakeholders.md`](docs/stakeholders.md) |
| Scope and business objectives | 1 | [`docs/scope.md`](docs/scope.md) |
| Strategic BPMN model | 1 (revised after tutor feedback) | [`models/bpmn-strategic/`](models/bpmn-strategic/) |
| Strategic model rationale | 1 | [`docs/strategic-rationale.md`](docs/strategic-rationale.md) |
| i\* Strategic Dependency (SD) model | 2 | [`models/istar/`](models/istar/) |
| i\* Strategic Rationale (SR) model | 2 | [`models/istar/`](models/istar/) |
| i\* rationale and stakeholder tensions | 2 | [`docs/istar-rationale.md`](docs/istar-rationale.md) |
| Operational BPMN – product listing | 2 | [`models/bpmn-operational/`](models/bpmn-operational/) |
| Operational BPMN – stock and availability | 2 | [`models/bpmn-operational/`](models/bpmn-operational/) |
| Executable Camunda processes | 2–3 | [`camunda/processes/`](camunda/processes/) |
| Camunda forms | 2–3 | [`camunda/forms/`](camunda/forms/) |
| Service-task worker (incl. mock certification service) | 2–3 | [`worker/`](worker/) |
| Process variables, job types and error codes | 2 | [`docs/variables.md`](docs/variables.md) |
| Traceability matrix | 2–3 | [`docs/traceability.md`](docs/traceability.md) |
| Test scenarios and evidence | 2–3 | [`docs/test-scenarios.md`](docs/test-scenarios.md) |
| Legal, ethical, social and professional evaluation | 3 | [`docs/lesp.md`](docs/lesp.md) |
| Signed Contribution Matrix | 3 | [`docs/contribution-matrix.pdf`](docs/contribution-matrix.pdf) |
 
### How the models connect
 
```
Stakeholder analysis → i* SD/SR models → Strategic BPMN → Operational BPMN → Camunda processes
                                         "Manage producers   product listing    forms + gateways
                                          and products"      stock/availability + worker
```
 
Each layer refines the one before it. [`docs/traceability.md`](docs/traceability.md) links every stakeholder goal to the process steps and Camunda elements that serve it.
 
---
 
## Repository structure
 
```
.
├── README.md
├── models/                     Diagrams (source + PNG)
│   ├── istar/                  i* SD and SR models (piStar)
│   ├── bpmn-strategic/         Strategic BPMN model
│   └── bpmn-operational/       Operational BPMN models (PNG)
├── camunda/                    Executable Camunda 8 resources
│   ├── processes/              product-listing.bpmn, stock-availability.bpmn
│   └── forms/                  Camunda Forms for each user task
├── worker/                     Python job worker for all service tasks
└── docs/                       Analysis, plans, rationale, tests and evidence
    ├── sprints/                Sprint plans and retrospectives
    ├── standups/               Individual stand-up logs
    └── test-evidence/          Screenshots from Camunda Operate
```
 
---
 
## Running the processes
 
### Requirements
- **Camunda 8 Run (c8run)** – local Camunda 8 engine with Operate and Tasklist
- **Camunda Desktop Modeler** – to deploy the processes and forms
- **Java 21 or newer** – required by c8run
- **Python 3.10 or newer** – for the worker (no extra packages needed)
### 1. Start Camunda
Extract c8run to a local folder such as `C:\Camunda\c8run` (**not** a OneDrive folder), then in PowerShell inside that folder:
```powershell
.\c8run.exe start
```
Check it's running: open http://localhost:8080/operate and log in with `demo` / `demo`.
 
### 2. Deploy
In the Desktop Modeler, deploy each file with **🚀 Deploy → Camunda 8 Self-Managed**, endpoint `http://localhost:26500`, authentication **None**, in this order:
1. All five forms in `camunda/forms/`
2. `camunda/processes/stock-availability.bpmn` (it's called by the next process)
3. `camunda/processes/product-listing.bpmn`
### 3. Start the worker
```powershell
cd worker
python worker.py
```
Leave it running. See [`worker/README.md`](worker/README.md) for options, including simulating the certification service being unavailable.
 
### 4. Run a process
1. In the Desktop Modeler, open `product-listing.bpmn` and click **▶️ Start instance**
2. Open **Tasklist** at http://localhost:8080/tasklist, claim **Enter product details** and fill in the form
3. Watch the instance in **Operate** at http://localhost:8080/operate
Test data and expected results for every path are in [`docs/test-scenarios.md`](docs/test-scenarios.md). Full configuration details are in [`docs/camunda-setup.md`](docs/camunda-setup.md).
 
### Stop Camunda
```powershell
.\c8run.exe stop
```
 
---
 
## Project management
 
We work in **Agile Scrum** across the three assessed sprints.
 
- **Board:** [link to GitHub Projects board]
- **Sprint plans and retrospectives:** [`docs/sprints/`](docs/sprints/)
- **Team charter:** [`docs/team-charter.md`](docs/team-charter.md)
| Sprint | Dates | Focus | Status |
|---|---|---|---|
| Sprint 0 | 28 Sep – 9 Oct 2026 | Group formation, repository, initial backlog | ✅ Complete |
| Sprint 1 | 12 Oct – 30 Oct 2026 | Strategic BPMN, scope, stakeholder analysis, backlog | ✅ Complete |
| Sprint 2 | 2 Nov – 20 Nov 2026 | i\* SD/SR, operational BPMN, initial Camunda automation | 🔄 In progress |
| Sprint 3 | 23 Nov – 10 Dec 2026 | Full automation, integration, LESP, final demonstration | ⏳ Not started |
 
Each sprint's submitted state is tagged in the repository (`sprint-1`, `sprint-2`, `sprint-3`).
**Final submission:** before 14:00 on 10 December 2026.
 
---
 
## How we work
 
1. **Branches:** no direct commits to `main`. One branch per task, e.g. `feature/14-cert-error-boundary`, `docs/traceability`, `fix/gateway-conditions`.
2. **Commits:** small and frequent, from each member's own account, referencing the issue: `#14 Add error boundary to certificate check`.
3. **Pull requests:** every change goes through a PR, reviewed and approved by another member before merging.
4. **Definition of done:** acceptance criteria met, reviewed, merged to `main`, and the owner can explain it.
5. **Shared names:** form keys, gateway conditions and job types use the names in [`docs/variables.md`](docs/variables.md) exactly.
---