# Sample Data

This folder contains realistic test datasets for all course projects and examples.

## Data Files (Coming Soon)

- **customer_inquiries.json** - Sample customer service tickets and inquiries
- **product_catalog.json** - E-commerce product data with inventory levels
- **order_data.json** - Sample order processing data for workflow testing
- **agent_configs.json** - Example agent configuration files

## Usage

All sample data is designed to work seamlessly with the course notebooks:

```python
import json
from pathlib import Path

# Load sample data in any notebook
data_path = Path("../02-sample-data")
with open(data_path / "customer_inquiries.json") as f:
    inquiries = json.load(f)
```

## Data Format

All data files use JSON format for easy integration with Python and agent communication protocols.

**Privacy:** All sample data is synthetic and created specifically for learning purposes.
