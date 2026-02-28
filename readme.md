# The Urban Pulse: NYC Roadwork & Safety Analysis

A modular data pipeline analyzing the correlation between NYC Department of Transportation (DOT) street construction permits and motor vehicle collisions.

## 🏗 Project Architecture
The system is built as a multi-stage pipeline to ensure data integrity and modular testing:
- **ingestion.py**: Interface with Socrata Open Data API (NYC Open Data).
- **cleaning.py**: Data type standardization, coordinate validation, and handling of missing values.
- **analysis.py**: Spatial join between collision points and construction polygons.
- **visualization.py**: Insight generation and mapping.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A GitHub Personal Access Token (for version control)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/the-urban-pulse.git](https://github.com/YOUR_USERNAME/the-urban-pulse.git)
   cd the-urban-pulse