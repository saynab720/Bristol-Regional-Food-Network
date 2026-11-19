# Camunda Service-task Worker

## Purpose
This folder contains the Python worker for the Bristol Regional Food Network project.

The worker connects to Camunda 8 and handles service tasks for the Producer Product Listing and Inventory Management use case.

## Inventory and Seasonal Availability

The worker will handle these job types:

1. validate-product-availability
2. check-stock-quantity
3. mark-product-available
4. mark-product-out-of-stock
5. mark-product-out-of-season
6. notify-producer-availability

## Requirements

- Python 3.10 or newer
- Camunda 8 running locally

## Running the worker

```powershell
python worker.py