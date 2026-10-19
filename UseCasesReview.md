# Review and comparison of the 3 use cases given to us:

## 1. Product Listing & Inventory
 - A producer lists a product, the system validates it and the product is published or updated.

 **We would need to implement:**  
    - A form for entering product information  
    - Validation for mandatory fields  
    - Decide whether organic certifications need to be checked  
    - Product publication and stock availability updates  
    - Exception handling if validation fails or verification service is unavailable  

 **Main Challenge:** Making the validation, stock rules and external verification flow executable rather than just drawing them.

## 2. Multi-Vendor Order & Payment
 - A customer checks out, the system coordinates multiple producers and payment is processed.
 
 **We would need to implement:**  
    - Check out form & stock validation  
    - Decision for unavailable products  
    - Orders split across multiple producers  
    - Simulated payments, retries & exception handling  
    - Producer specific amounts and the marketplace's 5% commission

 **Main Challenge:** Coordinating order date, inventory, payment outcomes and multiple producers without losing consistency.

## 3. Food Quality Incident & Traceability
 - An incident is investigated, affected products and customers are identified and follow-up actions are recorded.

 **We would need to implement:**  
    - Incident reporting form  
    - Retrieval of product, produce and order information  
    - Decision to close or escalate the incident  
    - Product suspension and customer notifications  
    - Notification failure handling and authorised review  

 **Main Challenge:** Tracing affected customers and products, recording notification results and handlong manual follow-up.


