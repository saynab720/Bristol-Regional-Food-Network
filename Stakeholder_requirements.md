# Stakeholder Requirements and Goals

**Project:** Bristol Regional Food Network  
**Use Case:** UC01 – Product Listing & Inventory Management  
**Sprint:** Sprint 1  
**Document:** Stakeholder Analysis

## 1. Overview

The Bristol Regional Food Network is a marketplace that connects local food producers with customers. Our chosen use case is **Product Listing and Inventory Management**. This covers how producers add products, update their information and stock, and how the system checks the details before showing them to customers.

We looked at the stakeholders in our strategic BPMN diagram to understand who is involved and what they need from the system. Some stakeholders are directly involved in our use case, while others are part of the wider marketplace.

### Stakeholders identified

| Stakeholder | Role in the marketplace | Involvement in Use Case 1 |
|---|---|---|
| Producers | Add products and keep stock information updated | Direct |
| Customers | View products and their availability | Indirect – use the published information |
| Bristol Regional Food Network / Marketplace Operator | Runs the marketplace and sets product listing rules | Direct |
| Producer & Product Management team | Manages the product catalogue | Direct |
| Marketplace Administrator | Could review problem listings and manage permissions | Proposed role |
| Organic Certification Body | Checks organic certification where needed | Possible involvement |
| Food Safety Regulator | Sets food safety requirements | Wider marketplace |
| Quality, Compliance & Sustainability team | Looks after quality and compliance processes | Related to Use Case 1 |
| Sales & Operations | Uses the product catalogue to sell and fulfil orders | Outside our chosen workflow |
| Finance | Manages financial processes | Outside our chosen workflow |
| Payment Provider | Processes payments | Outside our chosen workflow |
| Delivery Partner | Delivers orders | Outside our chosen workflow |

**Priorities:** **Must Have** means essential for our use case. **Should Have** means useful but needs to be agreed by the group. **Could Have** means an extra feature if we have enough time.

## 2. Producers

Producers are one of the main stakeholders because they will be using the system to add and manage products. Their technical experience varies, so the platform needs to be straightforward and easy to use.

| ID | Producer goal | How we can meet it | Priority |
|---|---|---|---|
| PG01 | Add products easily | Have a form for product name, description, price and availability | Must Have |
| PG02 | Update product information | Allow producers to edit existing listings | Must Have |
| PG03 | Keep stock and seasonal availability up to date | Allow stock and seasonal information to be changed | Must Have |
| PG04 | Make sure products are listed correctly | Check required fields before publishing | Must Have |
| PG05 | Know what went wrong if a listing fails | Show clear error messages and allow corrections | Must Have |
| PG06 | Use the system without much training | Keep the product management pages simple | Must Have |
| PG07 | Show organic certification where relevant | Allow certification details to be checked if we include this feature | Should Have |
| PG08 | Know whether a product has been published | Show a listing status such as published, rejected or pending | Should Have |

## 3. Customers

Customers will not be creating product listings, but they rely on the information producers upload. They need to know what products are available and whether the details are accurate.

| ID | Customer goal | How we can meet it | Priority |
|---|---|---|---|
| CG01 | See clear product information | Show product names, descriptions and prices | Must Have |
| CG02 | Know if a product is available | Show the latest stock and availability information | Must Have |
| CG03 | See which products are seasonal | Display seasonal availability | Must Have |
| CG04 | Know where the product comes from | Show the farm or producer information | Must Have |
| CG05 | See harvest dates where relevant | Include harvest dates for applicable products | Must Have |
| CG06 | Avoid seeing incomplete or invalid listings | Only show products that have passed validation and been published | Must Have |
| CG07 | Know whether organic claims have been checked | Show verified certification information if we include this feature | Should Have |

## 4. Bristol Regional Food Network / Marketplace Operator

The marketplace operator is responsible for how the platform runs. For our use case, their main goal is to make sure product listings follow the same rules and that customers can rely on the information shown.

| ID | Marketplace goal | How we can meet it | Priority |
|---|---|---|---|
| MG01 | Keep product listings accurate | Validate the required product information | Must Have |
| MG02 | Keep the catalogue consistent | Use the same required fields for each product | Must Have |
| MG03 | Support seasonal products | Allow producers to update stock and seasonal details | Must Have |
| MG04 | Deal with misleading or incorrect listings | Agree on a process for reviewing problem listings | Should Have |
| MG05 | Keep track of important changes | Record product updates and relevant actions | Should Have |

### Producer & Product Management team

This team appears as a lane in our strategic BPMN diagram. It is responsible for the **Manage the product catalogue** subprocess, which is the main process we are focusing on. It needs producers to provide the correct information and the system to validate, save and publish it.

## 5. Marketplace Administrator

We have also included a Marketplace Administrator as a possible stakeholder. The administrator is **not shown as a separate participant in our current strategic BPMN**, but could be part of the Producer & Product Management team. This role would be useful if we decide that some listings need manual review.

| ID | Administrator goal | How we can meet it | Priority |
|---|---|---|---|
| AG01 | Stop unauthorised product changes | Only allow producers to edit listings they have permission to manage | Must Have |
| AG02 | See listings that have problems | Show rejected, flagged or pending listings | Should Have |
| AG03 | Review listings when needed | Allow an administrator to approve, reject or request changes | Should Have |
| AG04 | Keep a record of decisions | Record review decisions and important changes | Should Have |
| AG05 | Remove problematic listings temporarily | Allow authorised administrators to unpublish a listing | Could Have |

## 6. Organic Certification Body

The Organic Certification Body is shown in our strategic BPMN diagram. It could be involved when a producer claims that a product is organic. We still need to decide as a group whether certification checking will be part of our executable workflow.

| ID | Goal | How we can meet it | Priority |
|---|---|---|---|
| OC01 | Receive the details needed to check a claim | Send the relevant certification information | Should Have |
| OC02 | Give a clear verification result | Handle approved, rejected and unavailable responses | Should Have |
| OC03 | Avoid showing false certification claims | Do not mark a product as verified unless the check succeeds | Must Have if included |
| OC04 | Handle a failed verification service | Allow a retry or send the listing for review, depending on our agreed rules | Should Have |

## 7. Food Safety Regulator and Quality, Compliance & Sustainability

Our strategic BPMN also includes the **Food Safety Regulator** and the **Quality, Compliance & Sustainability** team. They are important to the marketplace because product information needs to meet relevant quality and food safety expectations.

However, our BPMN does not show the regulator approving every individual product listing. We should not add this step to Use Case 1 unless it is an agreed requirement.

| ID | Stakeholder | Goal | How it relates to our use case |
|---|---|---|---|
| FS01 | Food Safety Regulator | Make sure relevant food safety rules are followed | Product listings may need to include certain information, depending on the rules |
| FS02 | Quality, Compliance & Sustainability team | Keep product information trustworthy | Help decide what product details and claims need checking |
| FS03 | Quality, Compliance & Sustainability team | Support compliance checks | Keep relevant records where needed |

## 8. Other Stakeholders in the BPMN

These stakeholders are shown in the strategic diagram but are not directly involved in our chosen product listing workflow.

| Stakeholder | What they do | Why they are outside Use Case 1 |
|---|---|---|
| Sales & Operations | Handles sales and order fulfilment | Uses the product catalogue after listings have been published |
| Finance | Manages financial activities | Payments and settlements are not part of product listing |
| Payment Provider | Processes customer payments | Belongs to the checkout and payment process |
| Delivery Partner | Delivers customer orders | Belongs to the order fulfilment process |

## 9. Stakeholder Goals and Dependencies

We can use these relationships when creating our **i\* model**. They show who depends on whom to achieve their goals.

| Stakeholder | Depends on | Reason |
|---|---|---|
| Producer | Marketplace Platform | To validate, save and publish product listings |
| Producer | Producer & Product Management team | To help with listing problems when needed |
| Customer | Producer | To provide correct product and stock information |
| Customer | Marketplace Platform | To show the latest published product details |
| Producer & Product Management team | Producer | To provide complete and accurate product information |
| Marketplace Operator | Producer & Product Management team | To keep the product catalogue consistent |
| Marketplace Administrator (if included) | Marketplace Platform | To view listing errors and review flagged products |
| Marketplace Platform (if included) | Organic Certification Body | To check certification claims |
| Quality, Compliance & Sustainability team | Marketplace Operator | To agree on product information and compliance rules |
| Marketplace Operator | Food Safety Regulator | To understand relevant food safety expectations |

## 10. Use Case 1: Product Listing & Inventory Management

**Main process in our strategic BPMN:** Producer & Product Management → **Manage the product catalogue**.

**Main actor:** Producer  
**Supporting system:** Marketplace Platform  
**Other possible actors:** Marketplace Administrator and Organic Certification Body  
**Expected result:** A valid product is published or updated with accurate stock and availability information.

### Main process

1. The producer enters a new product or updates an existing one.
2. The system checks that the required information has been entered correctly.
3. If something is missing or incorrect, the producer receives an error message and can fix it.
4. If the information is valid, the system carries out any additional checks we have agreed on, such as organic certification.
5. The system saves the product information and stock details.
6. The product is published or updated in the catalogue.
7. The producer receives confirmation and customers can see the updated information.

### Other scenarios we need to consider

- **Invalid information:** The product should not be published until the producer corrects the errors.
- **Stock update:** The producer changes stock or seasonal availability and the system saves the new information.
- **Certification check fails:** If we include certification checking, the system should not show an unverified product as certified.
- **Manual review:** If we include an administrator review, flagged products can be checked before publication.

## 11. Functional and Non-Functional Requirements

### Functional requirements

The system must allow producers to add and edit product listings, enter product details, update stock and seasonal availability, and submit information for validation. Invalid listings must not be published, and customers should only see the latest published product information. Producers should only be able to change listings they are authorised to manage.

We may also include certification checking, administrator reviews and records of important changes, depending on what the group agrees is achievable.

### Non-functional requirements

The system should be easy to use, especially for producers who are not confident with technology. It should keep product information accurate and consistent, protect listings from unauthorised changes, and give clear feedback when something goes wrong. Validation rules should also be straightforward to maintain.

## 12. Conclusion

For Use Case 1, the main stakeholders are **Producers, Customers, the Bristol Regional Food Network and the Producer & Product Management team**. We have also considered the Marketplace Administrator, Organic Certification Body and the quality and regulatory stakeholders shown in our strategic BPMN.

Our focus is on making it easier for producers to list products and manage stock, while making sure customers can see accurate information. The other stakeholders help us understand the wider marketplace, but we do not need to include all of their processes in our Camunda workflow.

**Things we still need to agree as a group:** Whether organic certification checks are included, whether any listings need administrator approval, and what stock and seasonal availability rules we will use.
