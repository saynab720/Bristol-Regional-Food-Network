# Stakeholder Requirements and Goals
**Project:** Bristol Regional Food Network  
**Sprint:** Sprint 1  
**Document:** Stakeholder Analysis

## 1. Overview

The Bristol Regional Food Network aims to provide a digital platform connecting local food producers with customers.

The platform must accommodate producers with varying levels of technical experience while allowing customers to browse and purchase locally sourced products efficiently.

This document identifies the primary stakeholders, their goals, the corresponding system requirements, and how the proposed platform will address them.

### Priority Classification

- **Must Have:** Essential functionality explicitly required by the project scenario.
- **Could Have:** Optional functionality that could improve the user experience.

---

## 2. Stakeholder 1: Producers

### Stakeholder Description

Producers are local food suppliers who use the platform to advertise and sell their products.

Technical capabilities vary significantly. Some producers rely exclusively on telephone and email communication, while others use basic social media platforms.

The system must therefore be accessible, intuitive and easy to manage without requiring extensive technical knowledge.

### Producer Goals and Requirements

| ID | Stakeholder Goal | System Requirement / Proposed Solution | Priority |
|---|---|---|---|
| PG01 | Manage product listings easily | Provide an interface allowing producers to add, edit and remove products, including names, descriptions, prices and availability | Must Have |
| PG02 | Manage seasonal inventory | Allow producers to update product availability and seasonal stock information regularly | Must Have |
| PG03 | View incoming orders in advance | Provide an order management dashboard and ensure producers receive at least 48 hours' preparation time | Must Have |
| PG04 | Receive weekly payments | Support weekly payment settlements for completed transactions | Must Have |
| PG05 | Maintain transparent financial records | Provide transaction histories and audit trails suitable for accounting and tax reporting | Must Have |
| PG06 | Understand product sales performance | Provide optional sales reports showing product performance and seasonal trends | Could Have |
| PG07 | Learn how to use the platform | Provide short educational videos or tutorials explaining key features | Could Have |
| PG08 | Communicate with customers | Introduce an optional messaging or notification feature for order-related communication | Could Have |

### Producer Requirements Summary

**Functional Requirements:**
- Product listing and editing functionality.
- Seasonal inventory management.
- Order tracking and visibility.
- Minimum 48-hour order preparation window.
- Weekly payment settlement records.
- Financial transaction history and audit trails.

**Non-Functional Requirements:**
- Simple and intuitive user interface.
- Accessibility for users with limited technical experience.
- Minimal training requirements.
- Reliable handling of orders and financial information.

---

## 3. Stakeholder 2: Customers

### Stakeholder Description

Customers are individuals purchasing locally sourced food products through the platform.

They require a straightforward shopping experience that provides accurate product information, supports multiple producers and clearly explains fulfilment arrangements.

### Customer Goals and Requirements

| ID | Stakeholder Goal | System Requirement / Proposed Solution | Priority |
|---|---|---|---|
| CG01 | Browse products by category | Organise products into vegetables, dairy, bakery, preserves and seasonal specialities | Must Have |
| CG02 | Find products efficiently | Implement search functionality allowing customers to locate specific products | Must Have |
| CG03 | Access detailed product information | Display product descriptions, prices, harvest dates, farm origins and seasonal availability | Must Have |
| CG04 | Purchase from one or multiple producers | Provide a checkout process supporting single-vendor and multi-vendor orders | Must Have |
| CG05 | Understand delivery and collection arrangements | Clearly display individual supplier responsibilities, delivery information and collection procedures | Must Have |
| CG06 | Shop from preferred producers | Introduce optional vendor filtering functionality | Could Have |

### Customer Requirements Summary

**Functional Requirements:**
- Product categorisation.
- Product search functionality.
- Detailed product information.
- Single-vendor and multi-vendor checkout.
- Delivery and collection information.
- Clear identification of supplier responsibilities.

**Non-Functional Requirements:**
- Easy-to-navigate shopping interface.
- Clear presentation of product information.
- Reliable checkout functionality.
- Consistent user experience across different vendors.

---

## 4. Stakeholder Goals and System Dependencies

The following dependencies will help inform the project's i* socio-technical model.

| Stakeholder | Goal | Dependency |
|---|---|---|
| Producer | Manage products efficiently | Product management functionality |
| Producer | Prepare orders on time | Order management and notification process |
| Producer | Receive weekly settlements | Payment settlement process |
| Producer | Maintain financial records | Transaction logging and audit functionality |
| Customer | Find suitable products | Product catalogue and search functionality |
| Customer | Make informed purchases | Accurate product and producer information |
| Customer | Purchase from multiple producers | Multi-vendor checkout functionality |
| Customer | Understand fulfilment arrangements | Supplier-specific delivery and collection information |

---

## 5. Conclusion

The primary stakeholders identified are **Producers** and **Customers**.

Producers prioritise straightforward product management, sufficient order preparation time, weekly payment settlements and transparent financial records.

Customers prioritise accessible product information, efficient searching, multi-vendor purchasing and clear delivery or collection arrangements.

The identified requirements will guide the development of the strategic and operational BPMN diagrams, the i* socio-technical model and the executable workflow.

**Note:** Sales analytics, educational videos, customer messaging and vendor filtering are proposed enhancements rather than mandatory requirements from the original scenario. Their inclusion will depend on project scope, available development time and stakeholder priorities.