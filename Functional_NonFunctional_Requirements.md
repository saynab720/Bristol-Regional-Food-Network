# Functional requirements (FR)

FR1 — The system shall allow a producer to create a new product listing.  
FR2 — The system shall collect the product name, description, category, price, quantity, availability period and origin.  
FR3 — The system shall record relevant harvest dates, allergen information, best-before dates and organic certification status.  
FR4 — The system shall validate the submitted product information and identify missing or invalid details.  
FR5 — The system shall allow a producer to correct invalid or incomplete information before the listing is published.  
FR6 — The system shall verify claimed organic certification using an external or simulated verification service.  
FR7 — The system shall publish a product listing once the required information and applicable verification checks have passed.  
FR8 — The system shall allow producers to update product quantities and seasonal availability.  
FR9 — The system shall mark a product as unavailable when its stock reaches zero.  
FR10 — The system shall make a product available again when stock is replenished and its seasonal availability period remains active.  
FR11 — The system shall handle unsuccessful certification checks and verification-service failures without incorrectly approving a listing.  


# Non-functional requirements (NFR)

NFR1 — Usability: The product listing interface shall be understandable to producers with limited technical knowledge, without requiring extensive training.  
NFR2 — Performance:	The system should validate a product submission and return a result within 3 seconds under normal operating conditions.  
NFR3 — Reliability:	The system shall not publish a product listing if required validation or applicable certification checks have failed.  
NFR4 — Data integrity: The system shall maintain accurate and consistent product quantities and availability statuses when inventory is updated.  
NFR5 — Security: The system shall ensure that only authorised users can create listings or modify product inventory.  
NFR6 — Privacy:	The system shall protect stored business and user information against unauthorised access.  
NFR7 — Maintainability:	Product validation and inventory rules shall be structured so that they can be modified and tested without rebuilding the entire application.  
NFR8 — Compatibility: The interface should work on commonly used desktop and mobile web browsers.   