# Project Scope and Business Objectives — UC1: Product Listing

**Date:** 22 October 2026

Our group has chosen **Use Case 1: Producer Product Listing and Inventory Management**. We will automate two functionalities in Camunda: listing a product and managing its stock and availability.

## 1. Business Objectives

Business objectives describe what the marketplace wants to achieve through product listing and inventory management. They explain why the system is worth building.

| ID | Business Objective | Why It Matters | How We Would Know It's Met |
|---|---|---|---|
| BO1 | Make it quick and easy for producers to list products. | More products listed means more choice for customers and more commission for the marketplace. | A producer can submit a product through one form, and valid products go live without waiting for an administrator. |
| BO2 | Keep product information accurate and trustworthy. | Customers need correct prices, allergen information, and best-before dates to buy safely. | Every published product has passed validation; missing or invalid details are always sent back for correction. |
| BO3 | Only allow genuine organic claims. | False organic labels damage customer trust and can break the law. | Every product marked organic has a verified certificate, or is published as non-organic. |
| BO4 | Never sell what isn't available. | Selling out-of-stock or out-of-season items leads to cancelled orders and unhappy customers. | A product becomes unavailable automatically when stock reaches zero or its season ends, and becomes available again when restocked in season. |
| BO5 | Reduce manual administrative work. | Automated checks free the administrator team to deal with genuine problems. | Administrators only intervene for exceptions, such as the verification service being unavailable. |
| BO6 | Meet legal and ethical duties. | Food labelling and data protection are legal requirements. | Allergen information is mandatory on every listing, and producers' personal data is only collected where needed. |

### Stakeholder Alignment

These business objectives link to the stakeholder analysis:

- **BO1 and BO4:** Support producers.
- **BO2 to BO4:** Protect and serve customers.
- **BO3:** Supports the certification body.
- **BO6:** Supports the food safety regulator.
- **BO5:** Benefits the marketplace administrator.

## 2. Project Objectives

Project objectives describe what our team will deliver for Assessment Task 1 by **14:00 on 10 December 2026**.

Business objectives explain *why* the system is needed, while project objectives explain *what* we will produce.

| ID | Project Objective | Sprint |
|---|---|---|
| PO1 | Model the whole marketplace in a strategic BPMN model. | 1 |
| PO2 | Analyse stakeholders' goals and dependencies using i* Strategic Dependency (SD) and Strategic Rationale (SR) models. | 2 |
| PO3 | Model both functionalities as detailed operational BPMN processes, including alternative and exception paths. | 2 |
| PO4 | Make both processes executable in Camunda, with forms, service tasks, decisions, and error handling. | 2–3 |
| PO5 | Show traceability from business objectives and stakeholder goals to the running processes. | 2–3 |
| PO6 | Evaluate the legal, ethical, social, and professional issues of the system. | 3 |
| PO7 | Deliver components that can be carried into the Task 2 Django and Docker product. | 3 |

## 3. Scope

### 3.1 Functionality 1 — Product Listing and Verification

1. A producer submits a new product with the following details:
   - Name
   - Description
   - Category
   - Price
   - Quantity
   - Availability period
   - Farm origin
   - Harvest date
   - Allergen information
   - Organic claim
   - Best-before date

2. The system validates the submitted details. If anything is missing or invalid, the producer is asked to correct it.

3. If the product is claimed to be organic, its certificate is checked using a simulated certification service.

4. If the certificate fails verification, the producer can choose to publish the product as non-organic or withdraw it.

5. If the certification service is unavailable, the system retries the request and then refers the case to an administrator for manual review.

6. Once all required checks are completed successfully, the product is published and the producer is notified.

### 3.2 Functionality 2 — Inventory and Seasonal Availability

1. A producer updates a product's stock quantity or availability period.

2. The system determines whether the product is available, out of stock, or out of season.

3. When stock reaches zero, the product automatically becomes unavailable for new orders.

4. When stock is replenished and the product is still in season, it becomes available again.

5. When the availability period ends, the product is automatically withdrawn from availability.

6. The producer is notified of relevant changes.

### 3.3 Agreement with the Module Team

**Agreed with module team:** [Tutor name, date, and any changes requested]

### 3.4 In Scope

The project includes:

- A strategic BPMN model of the whole marketplace.
- i* Strategic Dependency (SD) and Strategic Rationale (SR) models.
- Operational BPMN models for both functionalities, including exception paths.
- Executable Camunda processes with user tasks, Camunda Forms, service tasks, gateways, events, and process variables.
- A business rule for product availability: in stock, out of stock, or out of season.
- A simulated organic certification service that can return the following outcomes:
  - Verified
  - Not found
  - Expired
  - Unavailable
- Simulated producer notifications.
- Test scenarios and a README file.
- An evaluation of the legal, ethical, social, and professional issues associated with the system.

### 3.5 Out of Scope

The following are excluded from Task 1:

- Customer ordering, checkout, and payment (Use Case 2), except for stock updates triggered when an order is placed.
- Food quality incidents and customer notifications (Use Case 3).
- A full website front end, Django REST Framework services, and Docker implementation, which are part of Task 2.
- A real certification service, real producer data, or live hosting.
- Producer registration and account management, as producers are assumed to be already registered.

## 4. Assumptions and Constraints

### 4.1 Assumptions

- Producers are already registered and logged in before listing a product.
- Each product belongs to one producer.
- The organic certification service is simulated by the team. It behaves like a real external service, including occasional unavailability.
- Stock reductions resulting from customer orders arrive as simple updates. The full ordering process is not implemented.

### 4.2 Constraints

- **Deadline:** Submission must be completed before 14:00 on 10 December 2026, with no late submission window.
- **Team:** Four members working alongside other modules.
- **Technology:** Processes must run in Camunda; BPMN diagrams alone are not sufficient.
- **External services:** All external services must be simulated rather than live.
- **Academic integrity:** All models and diagrams must be created by the team. Any AI assistance with code must be declared.
- **Legal compliance:** Allergen information is mandatory on every listing under applicable UK food labelling requirements, and personal data must be handled in accordance with UK GDPR.

## 5. Summary

The project focuses on automating two core marketplace functionalities: **product listing and verification**, and **inventory and seasonal availability management**.

The team will create strategic and operational models, implement executable Camunda workflows, simulate external services, handle exceptions, and test the resulting processes. The solution must demonstrate traceability between business objectives, stakeholder needs, and implemented workflows while considering relevant legal, ethical, social, and professional responsibilities.