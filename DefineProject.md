Project Scope and Business Objectives — UC1 Product Listing
22 Oct 2026 
Our group has chosen Use Case 1: Producer Product Listing and Inventory Management. We will automate two functionalities in Camunda: listing a product, and managing its stock and availability.xh

1. Business objectives
These are what the marketplace as a business wants to achieve through product listing and inventory management. They explain why the system is worth building.
#
Business objective
Why it matters
How we would know it's met
BO1
Make it quick and easy for producers to list products
More products listed means more choice for customers and more commission for the marketplace
A producer can submit a product in one form; valid products go live without waiting for an admin
BO2
Keep product information accurate and trustworthy
Customers need correct prices, allergens and best-before dates to buy safely
Every published product has passed validation; missing or invalid details are always sent back for correction
BO3
Only allow genuine organic claims
False organic labels damage customer trust and can break the law
Every product marked organic has a verified certificate, or is published as non-organic
BO4
Never sell what isn't available
Selling out-of-stock or out-of-season items leads to cancelled orders and unhappy customers
A product becomes unavailable automatically when stock hits zero or its season ends, and available again when restocked in season
BO5
Reduce manual admin work
Automated checks free the admin team to deal with real problems
Admins only step in for exceptions, such as the verification service being down
BO6
Meet legal and ethical duties
Food labelling and data protection are legal requirements
Allergen information is mandatory on every listing; producers' personal data is only collected where needed
These link to the stakeholder analysis: BO1 and BO4 serve producers, BO2 to BO4 serve customers, BO3 serves the certification body, BO6 serves the food safety regulator, and BO5 serves the marketplace administrator.
2. Project objectives
These are what our team will deliver for Assessment Task 1 by 14:00 on 10 December 2026. Business objectives say why; project objectives say what we will produce.
#
Project objective
Sprint
PO1
Model the whole marketplace in a strategic BPMN model
1
PO2
Analyse stakeholders' goals and dependencies in i* SD and SR models
2
PO3
Model both functionalities as detailed operational BPMN processes, including alternative and exception paths
2
PO4
Make both processes executable in Camunda, with forms, service tasks, decisions and error handling
2–3
PO5
Show traceability from business objectives and stakeholder goals to the running processes
2–3
PO6
Evaluate the legal, ethical, social and professional issues of the system
3
PO7
Deliver components that can be carried into the Task 2 Django and Docker product
3
3. Scope
The two functionalities
Functionality 1 — Product listing and verification
1. A producer submits a new product: name, description, category, price, quantity, availability period, farm origin, harvest date, allergens, organic claim and best-before date.
2. The system checks the details. If anything is missing or invalid, the producer is asked to correct it.
3. If the product is claimed as organic, the certificate is checked with a simulated certification service.
4. If the certificate fails, the producer can publish it as non-organic or withdraw it.
5. If the certification service is unavailable, the system retries, then passes it to an administrator to review manually.
6. Once everything is valid, the product is published and the producer is notified.
Functionality 2 — Inventory and seasonal availability
1. A producer updates a product's stock quantity or availability period.
2. The system decides whether the product is available, out of stock or out of season.
3. When stock reaches zero, the product automatically becomes unavailable for new orders.
4. When stock is replenished and the product is still in season, it becomes available again.
5. When the availability period ends, the product is withdrawn automatically.
6. The producer is notified of changes.
Agreed with module team: [tutor name, date, any changes requested]
In scope
• Strategic BPMN model of the whole marketplace
• i* SD and SR models
• Operational BPMN models for both functionalities, including exception paths
• Executable Camunda processes with user tasks, Camunda Forms, service tasks, gateways, events and process variables
• A business rule for availability (in-stock / out of stock / out of season)
• A simulated organic certification service that can return verified, not found, expired or unavailable
• Simulated producer notifications
• Test scenarios, README, and an evaluation of legal, ethical, social and professional issues
Out of scope
• Customer ordering, checkout and payment (Use Case 2), except a stock update triggered when an order is placed
• Food incidents and customer notifications (Use Case 3)
• A full website front end, Django REST Framework services and Docker (Task 2)
• A real certification service, real producer data or live hosting
• Producer registration and account management (we assume producers are already registered)
4. Assumptions and constraints
Assumptions
• Producers are already registered and logged in before they list a product.
• One product belongs to one producer.
• The organic certification service is simulated by us; it behaves like a real external service, including being unavailable sometimes.
• Stock reductions from customer orders arrive as a simple update; the full ordering process is not built.
Constraints
• Deadline: submission before 14:00 on 10 December 2026, with no late window.
• Team: 4 members, working alongside other modules.
• Technology: processes must run in Camunda; BPMN diagrams alone are not enough.
• External services: must be simulated, not live.
• Academic integrity: all models and diagrams are drawn by us; any AI help with code is declared.
• Legal: allergen information is mandatory on every listing (UK food labelling rules), and personal data is handled in line with UK GDPR.