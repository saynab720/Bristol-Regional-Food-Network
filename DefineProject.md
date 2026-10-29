# Project Scope and Business Objectives – UC1: Product Listing and Inventory Management

**Date:** 22 October 2026

Our group has selected **Use Case 1: Producer Product Listing and Inventory Management**. The project focuses on automating two closely related marketplace functions: product listing and inventory management. These processes are important because they directly affect the accuracy, availability, and reliability of products displayed to customers.

The solution will be modelled using BPMN and implemented in Camunda as executable workflows.

---

# 1. Business Objectives

Business objectives explain what the marketplace aims to achieve by introducing automated product listing and inventory management processes. They provide the business justification for the system and help guide design decisions throughout the project.

| ID | Business Objective | Why It Matters | Success Indicator |
|----|-------------------|----------------|------------------|
| BO1 | Make it quick and easy for producers to list products. | A larger and more diverse catalogue benefits both producers and customers. | Producers can submit products through a single process and approved products are published automatically. |
| BO2 | Maintain accurate and trustworthy product information. | Customers rely on product details such as pricing, allergens, and shelf life when making purchasing decisions. | Invalid or incomplete submissions are identified and returned for correction before publication. |
| BO3 | Ensure organic claims are genuine. | Incorrect organic labelling can damage trust and create legal risks. | Products advertised as organic are successfully verified or published as non-organic. |
| BO4 | Prevent unavailable products from being sold. | Incorrect stock information can result in cancelled orders and a poor customer experience. | Products automatically become unavailable when stock reaches zero or when the season ends. |
| BO5 | Reduce manual administration. | Automation allows administrators to focus on exceptional cases rather than routine checks. | Administrative involvement is only required when automated validation cannot be completed. |
| BO6 | Comply with legal and ethical responsibilities. | Food labelling and data protection obligations must be met. | Allergen information is mandatory and only necessary personal data is collected. |

## Stakeholder Alignment

These objectives support the needs of multiple stakeholders across the marketplace:

- **BO1 and BO4** primarily support producers by making product management easier.
- **BO2, BO3, and BO4** protect customers by ensuring information is accurate and reliable.
- **BO3** supports the certification body by enforcing verification requirements.
- **BO6** aligns with the expectations of food safety regulators.
- **BO5** benefits marketplace administrators by reducing routine workload.

---

# 2. Project Objectives

Project objectives describe what the team will deliver for Assessment Task 1 by **10 December 2026**. While business objectives explain why the system is needed, project objectives define the outputs that will be produced during the project.

| ID | Project Objective | Sprint |
|----|------------------|---------|
| PO1 | Create a strategic BPMN model representing the marketplace. | 1 |
| PO2 | Analyse stakeholder goals and dependencies using i* SD and SR models. | 2 |
| PO3 | Develop operational BPMN models for both selected functionalities, including exception paths. | 2 |
| PO4 | Implement both processes in Camunda using forms, gateways, service tasks, and error handling. | 2–3 |
| PO5 | Demonstrate traceability between business objectives, stakeholder goals, and implemented processes. | 2–3 |
| PO6 | Evaluate legal, ethical, social, and professional considerations. | 3 |
| PO7 | Produce artefacts that can be reused in Task 2. | 3 |

---

# 3. Scope

## 3.1 Functionality 1 – Product Listing and Verification

This functionality enables producers to create and publish new product listings.

The process includes:

1. Submitting product information, including:
   - Product name
   - Description
   - Category
   - Price
   - Quantity
   - Availability period
   - Farm origin
   - Harvest date
   - Allergen information
   - Organic status
   - Best-before date

2. Automatic validation of submitted information.

3. Organic certification checks when a product is marked as organic.

4. Allowing producers to:
   - Publish as non-organic if certification cannot be confirmed.
   - Withdraw the listing if preferred.

5. Exception handling when the certification service is unavailable.

6. Publishing approved products and notifying the producer.

---

## 3.2 Functionality 2 – Inventory and Seasonal Availability

This functionality manages stock levels and product availability.

The process includes:

1. Producers updating stock levels or availability periods.
2. Automatic assessment of whether a product is:
   - Available
   - Out of stock
   - Out of season
3. Automatic withdrawal of products that reach zero stock.
4. Automatic reactivation when stock is replenished during the valid availability period.
5. Withdrawal of products when their seasonal availability expires.
6. Notifications informing producers of important status changes.

---

## 3.3 Agreement with the Module Team

**Agreed with module team:** *To be confirmed during supervision sessions.*

---

## 3.4 In Scope

The project includes:

- A strategic BPMN model of the marketplace.
- i* Strategic Dependency (SD) and Strategic Rationale (SR) models.
- Detailed operational BPMN models for both selected functionalities.
- Executable Camunda workflows.
- A business rule for product availability management.
- A simulated certification service capable of returning:
  - Verified
  - Not Found
  - Expired
  - Unavailable
- Simulated producer notifications.
- Testing scenarios and supporting documentation.
- Evaluation of legal, ethical, social, and professional issues.

---

## 3.5 Out of Scope

The following areas are excluded from Task 1:

- Customer ordering, checkout, and payment processes (Use Case 2), apart from stock updates triggered by orders.
- Food quality incident management and customer notifications (Use Case 3).
- Full web application development using Django or Docker, which will be addressed in Task 2.
- Real third-party services or live producer data.
- Producer registration and account management, as all producers are assumed to already be registered.

---

# 4. Assumptions and Constraints

## 4.1 Assumptions

The project assumes that:

- Producers are already registered and authenticated before using the system.
- Each product belongs to a single producer.
- The organic certification service is simulated but behaves realistically, including occasional service failures.
- Stock reductions from customer purchases arrive as inventory updates rather than through a full ordering process.

## 4.2 Constraints

The project is subject to the following constraints:

- Submission must be completed by **14:00 on 10 December 2026**.
- The team consists of four members working alongside other academic commitments.
- All process implementations must run within Camunda.
- External services must be simulated rather than connected to live systems.
- All models and process artefacts must be produced by the team.
- Any AI-assisted development must be declared.
- Food labelling and personal data handling must comply with relevant UK legal requirements.

---

# 5. Summary

This project focuses on automating two important marketplace functions: **product listing and verification** and **inventory and seasonal availability management**.

The proposed solution will combine strategic and operational process modelling with executable Camunda workflows. By automating product validation, certification checks, and stock management, the system aims to improve accuracy, reduce administrative effort, and support a more reliable experience for both producers and customers.

The project will also demonstrate clear links between business objectives, stakeholder needs, and the implemented processes, providing a strong foundation for the more complete marketplace system developed in Task 2.
