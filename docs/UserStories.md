#User Stories and Acceptance Criteria -- Use Case 1

Project: Bristol Regional Food Network
Use Case: Producer Product Listing and Inventory Management

##1. Product Listing
**User story**
As a registered producer, I want to submit my product details so that I can list my products on the marketplace.

**Acceptance criteria**
 - Given a registered producer is entering a product, when they provide all required valid details, the system accepts the submission for validation.
 - Given required details are missing or invalid, when the producer submits the product, the system identifies the problem and asks for correction.
 - Given the product passes the required validation checks, when the listing process completes, the product can be published.
 - Given the product has not passed validation, the system must not publish it as a valid listing.


 ##2. Organic Certification
 **User story**
 As a producer who wants to label a product as organic, I want the system to verify my organic certificate so that customers can trust the product's organic status.

 **Acceptance criteria**
 - Given a producer submits a product with an organic claim, when the verification service confirms the certificate is valid, the system records the product as verified for organic status.
 - Given the verification service reports that the certificate is not found or has expired, the ssytem informs the producer of the result.
 - Given the certificate cannot be verified, the producer can choose to publish the product without the organic claim or withdraw the listing.
 - Given the verification service is unavailable, the system follows the agreed retry process and, if necessary, send the case for administrator review.


 ##3. Inventory and Seasonal Availability
 **User story**
 As a producer, I want ot update my product's stock quantity and availability period so that customers can see whether the product is available to order.

 **Acceptance criteria**
 - Given a product is in season and has stock remaining, when the stock quantity is updated, the product is shown as available.
 - Given the stock quantity reaches zero, the product is marked unavailable for new orders.
 - Given a producer adds stock whikle the product is still in season, the product can become available again.
 - Given the product's season has ended, the product is marked unavailable even if stock remains.
 - When the system changes a product's availability status, it notifies the producer according to the agreed workflow.