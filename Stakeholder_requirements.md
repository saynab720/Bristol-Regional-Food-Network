# Stakeholder Requirements and Goals

**Project:** Bristol Regional Food Network  
**Use Case:** UC01 – Product Listing & Inventory Management  
**Sprint:** Sprint 1  
**Document:** Stakeholder Analysis (aligned with strategic BPMN)

## 1. Overview and Scope

The Bristol Regional Food Network connects local producers with customers. The strategic BPMN depicts four internal functional areas: **Producer & Product Management**, **Sales & Operations**, **Finance**, and **Quality, Compliance & Sustainability**. It also shows external participants: **Producers**, **Customers**, **Payment Provider**, **Organic Certification Body**, **Food Safety Regulator**, and **Delivery Partner**.

**UC01** concentrates on the **Manage the product catalogue** subprocess within Producer & Product Management: creating, validating, publishing and updating listings, including stock and seasonal availability. Other functions shown in the strategic model provide organisational context but are not necessarily implemented in UC01.

### Stakeholder overview and relevance

| Stakeholder / actor | Shown in strategic BPMN? | UC01 relevance | Role |
|---|---|---|---|
| Producers | Yes – external pool | Direct | Supply and update product information and stock |
| Customers | Yes – external pool | Indirect beneficiary | Rely on accurate published product information |
| Bristol Regional Food Network / Marketplace Operator | Yes – central organisation | Direct business stakeholder | Defines catalogue rules and oversees the marketplace |
| Producer & Product Management team | Yes – internal lane | Direct | Owns the product catalogue business process |
| Marketplace Administrator | Not separately labelled; proposed internal role | Conditional | Handles permissions, flagged listings and manual review if adopted |
| Organic Certification Body | Yes – external pool | Conditional | Verifies organic claims if certification checks are in scope |
| Food Safety Regulator | Yes – external pool | Indirect / compliance | Sets relevant food safety expectations; receives compliance reporting in wider enterprise model |
| Sales & Operations team | Yes – internal lane | Downstream | Uses published catalogue information to support sales |
| Quality, Compliance & Sustainability team | Yes – internal lane | Related oversight | Oversees quality and compliance processes |
| Payment Provider | Yes – external pool | Outside UC01 | Supports payment processing in sales/finance workflows |
| Delivery Partner | Yes – external pool | Outside UC01 | Supports order fulfilment and delivery |
| Marketplace Platform | Represented by organisational processes, not a separate external pool | Supporting system | Validates, stores and publishes listing data |

**Priority definitions:** **Must** = essential to the agreed UC01 workflow; **Should** = important proposed support; **Could** = optional enhancement. Proposed features must be confirmed by the group.

## 2. Producers

**Goal:** Manage products independently, keep stock and seasonal information accurate, and understand why a submission succeeds or fails.

| ID | Goal | System requirement / response | Priority |
|---|---|---|---|
| PG01 | Create listings easily | Form for name, description, price and availability | Must |
| PG02 | Correct product details | Edit existing listings | Must |
| PG03 | Keep inventory current | Update stock and seasonal availability | Must |
| PG04 | Publish valid listings | Validate mandatory fields before publication | Must |
| PG05 | Resolve submission errors | Explain validation failures and permit correction | Must |
| PG06 | Use the system with little training | Clear, accessible product management interface | Must |
| PG07 | Support organic claims | Submit certification details for verification if adopted | Should (conditional) |
| PG08 | Know listing status | Display published, rejected or pending status | Should |

## 3. Customers

**Goal:** View accurate, current information about locally sourced products. Customers do not submit listings in UC01.

| ID | Goal | System requirement / response | Priority |
|---|---|---|---|
| CG01 | See trustworthy listings | Display validated product names, descriptions and prices | Must |
| CG02 | Know whether products are available | Display current availability and stock status | Must |
| CG03 | Identify seasonal products | Show seasonal availability | Must |
| CG04 | Understand product origin | Show farm/producer origin information | Must |
| CG05 | Access harvest information | Show harvest dates where applicable | Must |
| CG06 | Avoid invalid listings | Hide rejected, draft or unpublished listings | Must |
| CG07 | Understand organic claims | Show verified certification status if implemented | Should (conditional) |

## 4. Bristol Regional Food Network / Marketplace Operator

**Goal:** Maintain a reliable, consistent product catalogue that supports the enterprise's broader sales and compliance activities. The strategic BPMN represents this organisation through internal lanes; the operator is a business role, not an additional external pool.

| ID | Goal | System requirement / response | Priority |
|---|---|---|---|
| MG01 | Ensure listing quality | Apply standard mandatory-field validation | Must |
| MG02 | Maintain catalogue consistency | Standardise product details and availability fields | Must |
| MG03 | Support seasonal producers | Permit timely seasonal stock updates | Must |
| MG04 | Enforce marketplace policies | Define handling of inaccurate or misleading listings | Should |
| MG05 | Maintain accountability | Keep records of important listing changes | Should |

### Producer & Product Management team

This **internal BPMN lane** owns the **Manage the product catalogue** subprocess. Its operational goals are to process producer submissions, validate product details, publish approved listings and keep availability accurate. It depends on producers for correct information and on the platform for validation, storage and publication.

## 5. Marketplace Administrator (proposed role)

The strategic BPMN does **not** label an administrator as a separate participant. An administrator can be modelled as an internal role within Producer & Product Management **if** the group chooses manual reviews or access administration.

| ID | Goal | System requirement / response | Priority |
|---|---|---|---|
| AG01 | Restrict unauthorised changes | Producers may edit only listings they are permitted to manage | Must (security design) |
| AG02 | Inspect problematic listings | View failed, flagged or pending submissions | Should |
| AG03 | Resolve exceptional submissions | Approve, reject or request corrections in a manual review task | Should (conditional) |
| AG04 | Maintain accountability | Log administrative changes and review decisions | Should |
| AG05 | Suspend problematic listings | Temporarily unpublish listings when necessary | Could |

## 6. Organic Certification Body

The strategic BPMN explicitly shows an **Organic Certification Body** and a **certification** message interaction with the network's quality function. The UC01 comparison also raises certification checks as a design question; therefore verification is **conditional**, not a confirmed mandatory step for every listing.

| ID | Goal | System requirement / response | Priority |
|---|---|---|---|
| OC01 | Receive valid verification requests | Send relevant certification identifiers/details | Should (conditional) |
| OC02 | Return trustworthy results | Handle verified, rejected or unavailable responses | Should (conditional) |
| OC03 | Prevent unsupported claims | Never label an unverified product as certified | Must if certification is shown |
| OC04 | Handle service interruption | Retry, defer or route to review according to agreed rules | Should (conditional) |

## 7. Food Safety Regulator and Quality, Compliance & Sustainability

The BPMN shows a **Food Safety Regulator** linked by **compliance reporting** to the organisation's **Ensure food quality and safety** activity. This is a **wider enterprise relationship**, not proof that the regulator directly approves individual UC01 listings.

| ID | Stakeholder | Goal | UC01 implication | Priority |
|---|---|---|---|---|
| FS01 | Food Safety Regulator | Promote food safety compliance | Catalogue policies should allow required food information to be recorded where applicable | Should / confirm rules |
| FS02 | Quality, Compliance & Sustainability team | Maintain trustworthy food information | Define or review product-data standards and relevant claims | Should |
| FS03 | Quality, Compliance & Sustainability team | Support compliance oversight | Retain relevant listing/change evidence if required | Should |

Do **not** add a regulator approval gateway to the UC01 Camunda process unless the group has confirmed such a business rule.

## 8. Other Stakeholders in the Strategic BPMN (Outside UC01)

| Stakeholder / function | Strategic BPMN involvement | Why excluded from UC01 execution |
|---|---|---|
| Sales & Operations | Sell local food and fulfil/deliver orders | Uses published listings downstream; order processing is separate |
| Finance | Manage finances | Settlements and payment records are outside listing management |
| Payment Provider | Payment processing | Relevant to checkout/payment use case |
| Delivery Partner | Delivery services | Relevant to order fulfilment |

These stakeholders should remain visible in the **strategic BPMN** and broader stakeholder map, without adding payment or delivery tasks to UC01.

## 9. Stakeholder Dependencies for i* Modelling

| Depender | Dependee | Dependency |
|---|---|---|
| Producer | Marketplace Platform | Validate, publish and update listings |
| Producer | Producer & Product Management | Support exceptional listing issues |
| Customer | Producer | Accurate product and availability information |
| Customer | Marketplace Platform | Current published catalogue |
| Producer & Product Management | Producer | Complete, correct listing data |
| Marketplace Operator | Producer & Product Management | Consistent catalogue management |
| Marketplace Administrator (if adopted) | Marketplace Platform | Listing status, errors and review tools |
| Marketplace Platform | Organic Certification Body (if adopted) | Certification verification result |
| Quality, Compliance & Sustainability | Marketplace Operator | Agreed quality and compliance policies |
| Marketplace Operator | Food Safety Regulator | Relevant regulatory expectations (wider enterprise) |

## 10. UC01 Workflow and BPMN Alignment

**Strategic parent process:** Producer & Product Management → **Manage the product catalogue** (collapsed subprocess).

**Primary actor:** Producer.  
**Supporting system:** Marketplace Platform.  
**Conditional participants:** Marketplace Administrator and Organic Certification Body.  
**Outcome:** Valid listing created or updated, with accurate availability.

### Main flow

1. Producer enters or updates product information.
2. Platform validates required fields and business rules.
3. Gateway: Is the submission valid?
4. If **no**, return clear errors; producer corrects and resubmits.
5. If **yes**, perform any agreed optional certification check or manual review.
6. Platform saves the product and stock/seasonal information.
7. Platform publishes or updates the catalogue listing.
8. Producer receives confirmation; customers can view the current listing.

### Exception paths

- **Invalid information:** Do not publish; return errors for correction.
- **Inventory change:** Validate and save updated stock/seasonal availability.
- **Certification service unavailable (conditional):** Keep certification unverified and apply the agreed retry/review rule.
- **Administrator review (conditional):** Route flagged submission to an authorised reviewer.

## 11. Functional and Non-Functional Requirements Summary

**Core functional requirements:** Create/edit listings; capture required product details; validate submissions; reject invalid entries; update stock and seasonal availability; publish valid records; show current catalogue data; restrict unauthorised edits.

**Conditional functional requirements:** Certification verification; administrative review; listing suspension; enhanced audit records.

**Non-functional requirements:** Usability for producers with limited technical experience; accurate and consistent data; secure authorisation; reliable publication and update behaviour; maintainable validation rules; clear error feedback.

## 12. Conclusion and Scope Notes

The stakeholder analysis now reflects the **actual participants and organisational functions shown in the strategic BPMN**, while retaining the specific boundaries of **UC01 Product Listing & Inventory Management**.

- **Direct UC01 focus:** Producers, customers as beneficiaries, Producer & Product Management, and the marketplace platform/operator.
- **Conditional UC01 support:** Marketplace Administrator and Organic Certification Body.
- **Wider strategic/compliance context:** Food Safety Regulator and Quality, Compliance & Sustainability.
- **Outside UC01:** Payment Provider, Delivery Partner, Finance, and order fulfilment.

**Assumptions to confirm:** Whether organic certification checks are mandatory, whether flagged listings need manual approval, the exact stock/seasonal business rules, and any required regulatory product fields. The strategic BPMN does not establish these operational rules by itself.
