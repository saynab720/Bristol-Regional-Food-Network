# Stakeholder Requirements and Goals

**Project:** Bristol Regional Food Network  
**Use Case:** UC01 – Product Listing & Inventory Management  
**Sprint:** Sprint 1  
**Document:** Stakeholder Analysis

## 1. Overview

The Bristol Regional Food Network is a digital marketplace connecting local food producers with customers.

Use Case 1 focuses on creating, validating, publishing and updating product listings and inventory.

The system must support producers with different levels of technical experience while maintaining accurate product information and ensuring that only valid listings are published.

### Identified Stakeholders

| Stakeholder | Role | Involvement |
|---|---|---|
| Producers | Primary users | Create and update product listings and inventory |
| Customers | End users | View published product information and availability |
| Marketplace Administrator | Administrative user | Manage permissions, review flagged listings and oversee product records |
| Marketplace Operator | Business stakeholder | Maintain marketplace quality, consistency and operational policies |
| External Certification Authority | External stakeholder | Verify product certifications where applicable |
| Platform / System | Supporting system actor | Validate, store, publish and update product information |

### Priority Classification

- **Must Have:** Essential to the agreed core workflow.
- **Should Have:** Important supporting functionality.
- **Could Have:** Optional enhancements.

---

## 2. Stakeholder 1: Producers

### Stakeholder Description

Producers are local food suppliers responsible for creating and maintaining product listings.

Their technical capabilities vary, so the system must provide a simple interface for managing products and seasonal inventory.

### Producer Goals and Requirements

| ID | Stakeholder Goal | System Requirement / Proposed Solution | Priority |
|---|---|---|---|
| PG01 | Create product listings easily | Provide a form for product names, descriptions, prices and availability | Must Have |
| PG02 | Maintain accurate product information | Allow producers to edit existing listings | Must Have |
| PG03 | Manage seasonal inventory | Allow producers to update stock levels and seasonal availability | Must Have |
| PG04 | Publish valid products | Validate required information before publication | Must Have |
| PG05 | Understand submission errors | Display clear validation errors and allow corrections | Must Have |
| PG06 | Manage products independently | Provide an intuitive interface requiring minimal training | Must Have |
| PG07 | Verify product certifications | Support certification checks where applicable | Should Have |
| PG08 | Track listing status | Display whether a listing is published, rejected or awaiting review | Should Have |

---

## 3. Stakeholder 2: Customers

### Stakeholder Description

Customers depend on the marketplace to provide accurate information about locally sourced food products.

Although customers do not directly participate in product management, they are affected by the accuracy of published listings and inventory updates.

### Customer Goals and Requirements

| ID | Stakeholder Goal | System Requirement / Proposed Solution | Priority |
|---|---|---|---|
| CG01 | View accurate product information | Display validated names, descriptions and prices | Must Have |
| CG02 | Identify available products | Display current stock and availability information | Must Have |
| CG03 | Understand seasonal availability | Display seasonal information for relevant products | Must Have |
| CG04 | Identify product origins | Display farm or producer origin information | Must Have |
| CG05 | Access harvest information | Display harvest dates where relevant | Must Have |
| CG06 | Trust published information | Prevent invalid or unpublished listings from appearing in the catalogue | Must Have |
| CG07 | Identify certified products | Display verified certification information where applicable | Should Have |

---

## 4. Stakeholder 3: Marketplace Administrator

### Stakeholder Description

The Marketplace Administrator is responsible for maintaining the administrative integrity of the platform.

For Use Case 1, the administrator may manage producer permissions, review problematic product listings and intervene when automated processes cannot complete successfully.

### Administrator Goals and Requirements

| ID | Stakeholder Goal | System Requirement / Proposed Solution | Priority |
|---|---|---|---|
| AG01 | Control access to product management | Allow authorised producers to manage only their own listings | Must Have |
| AG02 | Monitor product listing status | Provide visibility of published, rejected and pending listings | Should Have |
| AG03 | Review problematic submissions | Provide an administrative review process for flagged listings | Should Have |
| AG04 | Correct inaccurate marketplace information | Allow authorised administrative intervention with recorded changes | Should Have |
| AG05 | Investigate failed validation or verification | Provide error records and relevant submission details | Should Have |
| AG06 | Maintain accountability | Record significant product changes and administrative actions | Should Have |
| AG07 | Suspend inappropriate listings | Allow administrators to temporarily unpublish listings when necessary | Could Have |

### Administrator Functional Requirements

- **FR16:** The system must restrict product management to authorised users.
- **FR17:** The system should allow administrators to view product listing statuses.
- **FR18:** The system should allow administrators to review flagged submissions.
- **FR19:** The system should record administrative changes to product information.
- **FR20:** The system could allow authorised administrators to suspend listings.

### Administrator Non-Functional Requirements

- **Security:** Administrative functionality must be protected by role-based access controls.
- **Accountability:** Administrative actions should be traceable to an authorised user.
- **Reliability:** Administrative changes must not corrupt existing product records.
- **Usability:** Listing statuses and errors should be easy to understand.

---

## 5. Stakeholder 4: Marketplace Operator

### Stakeholder Description

The Marketplace Operator represents the organisation responsible for running the Bristol Regional Food Network.

Unlike the administrator, who performs day-to-day system administration, the marketplace operator focuses on the business objectives, quality standards and operating policies of the platform.

These responsibilities could belong to the same person in a small organisation, but separating them helps clarify the different stakeholder goals.

### Marketplace Operator Goals and Requirements

| ID | Stakeholder Goal | System Requirement / Proposed Solution | Priority |
|---|---|---|---|
| MG01 | Maintain accurate marketplace listings | Ensure product information is validated before publication | Must Have |
| MG02 | Provide a consistent product catalogue | Define standard product information requirements | Must Have |
| MG03 | Support seasonal local food availability | Ensure producers can update seasonal information | Must Have |
| MG04 | Maintain trust in the marketplace | Establish policies for inaccurate or misleading listings | Should Have |
| MG05 | Monitor marketplace activity | Provide visibility of listing creation, updates and validation failures | Should Have |
| MG06 | Support marketplace accountability | Maintain records of significant product changes | Should Have |
| MG07 | Improve producer participation | Provide guidance for producers with limited technical experience | Could Have |

### Marketplace Operator Functional Requirements

- **FR21:** The system must apply agreed product validation rules consistently.
- **FR22:** The system must support the required product information fields.
- **FR23:** The system should provide records of product publication and updates.
- **FR24:** The system should support review of listings that violate marketplace policies.
- **FR25:** The system could provide reporting on product listing activity.

### Marketplace Operator Non-Functional Requirements

- **Data Quality:** Published product records must follow consistent validation rules.
- **Reliability:** Product publishing and updating must operate consistently.
- **Maintainability:** Validation rules should be configurable or maintainable as marketplace policies evolve.
- **Transparency:** Significant listing changes should be traceable.

---

## 6. Stakeholder 5: External Certification Authority

### Stakeholder Description

An External Certification Authority is an organisation or verification service that may confirm whether a product holds a claimed certification, such as an organic certification.

This stakeholder is **conditional**. It is relevant only if the group includes certification verification in Use Case 1.

For the Camunda assessment, the verification interaction could be simulated rather than integrated with a real external organisation.

### Certification Authority Goals and Requirements

| ID | Stakeholder Goal | System Requirement / Proposed Solution | Priority |
|---|---|---|---|
| CA01 | Receive valid verification requests | Send required certification identifiers or details | Should Have |
| CA02 | Provide accurate certification results | Return a verified, rejected or unavailable status | Should Have |
| CA03 | Prevent unsupported certification claims | Do not mark products as verified without a successful result | Should Have |
| CA04 | Handle service interruptions | Support retry, pending review or failure handling | Should Have |

### Certification Functional Requirements

- **FR26:** The system should submit certification details for verification when applicable.
- **FR27:** The system should process successful and unsuccessful verification responses.
- **FR28:** The system should handle unavailable verification services.
- **FR29:** The system must not falsely display a certification as verified.

---

## 7. Stakeholder Goals and Dependencies

These relationships can be used when constructing the i* socio-technical model.

| Depender | Dependee | Goal or Dependency |
|---|---|---|
| Producer | Platform | Submit and publish valid product listings |
| Producer | Platform | Update stock and seasonal availability |
| Producer | Administrator | Receive assistance with flagged or problematic listings |
| Customer | Platform | Access accurate published product information |
| Customer | Producer | Receive accurate product and availability information |
| Marketplace Administrator | Platform | Access listing statuses and validation errors |
| Marketplace Administrator | Producer | Obtain corrected or missing product information |
| Marketplace Operator | Producer | Maintain accurate and current listings |
| Marketplace Operator | Administrator | Enforce marketplace listing policies |
| Marketplace Operator | Platform | Apply consistent product validation rules |
| Platform | Producer | Receive complete and accurate product information |
| Platform | Certification Service | Obtain verification results when applicable |

### Important Dependencies

**Producer → Platform:** Producers depend on the platform to validate, store and publish their products.

**Customer → Producer and Platform:** Customers depend on producers to maintain accurate information and on the platform to display it correctly.

**Administrator → Platform:** Administrators depend on the platform to identify listing problems and support corrective action.

**Marketplace Operator → Administrator:** The marketplace operator depends on administrative processes to enforce listing policies.

**Platform → Certification Authority:** Where certification is required, the platform depends on an external verification result.

---

## 8. Use Case 1: Product Listing & Inventory Management

| Attribute | Description |
|---|---|
| Use Case ID | UC01 |
| Use Case Name | Product Listing & Inventory Management |
| Primary Actor | Producer |
| Supporting Actors | Marketplace Administrator, Platform, optional Certification Authority |
| Business Stakeholder | Marketplace Operator |
| Goal | Create, validate, publish and update product listings |
| Trigger | Producer submits a new listing or updates an existing product |
| Preconditions | Producer has permission to manage the relevant product |
| Success Outcome | Valid product information is saved and published |
| Failure Outcome | Invalid information is rejected or routed for review |

### Main Success Scenario

1. The producer accesses the product management interface.
2. The producer enters product details.
3. The producer submits the listing.
4. The platform validates the required fields.
5. If applicable, certification information is verified.
6. The platform saves the validated product record.
7. The platform publishes or updates the listing.
8. The producer receives confirmation.
9. Customers can view the updated product information.

### Alternative Scenario A: Validation Failure

1. The producer submits incomplete or invalid information.
2. The platform identifies the validation errors.
3. The listing is not published.
4. The producer receives an explanation.
5. The producer corrects and resubmits the information.

### Alternative Scenario B: Administrator Review

1. A submission is flagged for manual review.
2. The administrator receives the review task.
3. The administrator examines the listing.
4. The administrator approves, rejects or requests corrections.
5. The platform updates the listing status.
6. The producer receives the outcome.

*This is a proposed workflow extension, not a confirmed requirement from the original scenario.*

### Alternative Scenario C: Certification Service Failure

1. The platform requests certification verification.
2. The external service fails or becomes unavailable.
3. The platform records the failure.
4. The listing remains unverified.
5. The system applies the agreed retry or review policy.

*This scenario applies only if certification verification is included.*

---

### Suggested Executable Workflow

1. Start event: Producer submits a product.
2. Service task: Validate product information.
3. Exclusive gateway: Is the submission valid?
4. Invalid path: Return errors for correction.
5. Optional service task: Verify certification.
6. Optional gateway: Is manual review required?
7. Optional user task: Administrator reviews listing.
8. Service task: Save product information.
9. Service task: Publish or update listing.
10. End event: Listing successfully processed.

### Technical Requirements

The group should demonstrate:

- Executable validation logic.
- BPMN gateways for successful and failed submissions.
- Product publication or inventory update behaviour.
- Error handling and correction paths.
- Optional administrator review.
- Optional certification verification with failure handling.

---

## 10. Conclusion

Use Case 1 involves several stakeholders with different responsibilities.

**Producers** need an accessible way to create and manage listings.

**Customers** depend on accurate product information and availability.

**Marketplace Administrators** support access control, review and correction of problematic listings.

**Marketplace Operators** define the quality standards and policies governing marketplace listings.

**External Certification Authorities**, where relevant, support verification of product certification claims.

The platform coordinates these interactions through validation, product storage, publication and inventory updates.

These stakeholder relationships provide a foundation for the strategic BPMN diagram, operational BPMN diagram, i* socio-technical model and executable Camunda workflow.

