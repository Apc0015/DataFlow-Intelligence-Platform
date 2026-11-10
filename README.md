# DataFlow Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-red.svg)](https://streamlit.io/)
[![CI](https://github.com/Apc0015/DataFlow-Intelligence-Platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Apc0015/DataFlow-Intelligence-Platform/actions/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen.svg)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

I built the **DataFlow Intelligence Platform** as a modular multi-domain analytics application using Python and Streamlit. My goal was to create a unified platform that processes, validates, and visualizes complex datasets across three distinct domains: commercial aviation route networks, higher-education enrollment funnels, and global socioeconomic indicators.

Instead of building a static dashboard or a monolithic script, I organized the platform into dedicated data loaders, automated CSV validators, business integrity checkers, and modular visualization components.

---

## Architecture & How It Works

The platform follows a layered pipeline architecture:

```
┌────────────────────────────────────────────────────────┐
│                   Data Ingestion Layer                 │
│  - Raw CSVs (data/raw/2022.csv, university_data.csv)   │
│  - Synthetic Generators (deterministic fallbacks)      │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│              Validation & Cleaning Pipeline            │
│  - CSVValidator: structure, empty rows, placeholders   │
│  - Decimal normalization ('7,821' -> 7.821)            │
│  - DataIntegrityChecker: domain business logic rules   │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│                    Analytics Engines                   │
│  - Aviation: route calculations, peak departure hours  │
│  - Education: admissions funnels, retention cohorts    │
│  - Socioeconomic: correlation, regression, rankings    │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│                  Presentation Layer                    │
│  - Streamlit multi-page interface (src/app.py)         │
│  - Interactive visualizations (Plotly, Folium)         │
│  - Custom lightweight CSS styling (src/utils/styles.py)│
└────────────────────────────────────────────────────────┘
```

### 1. Data Ingestion & Sanitization (`src/utils/data_handler.py`)
- **Raw CSV loading**: Ingests World Happiness Report data (`data/raw/2022.csv`) and university longitudinal metrics (`data/raw/university_data.csv`).
- **Resilient fallbacks**: If raw files are absent or corrupted, the platform dynamically generates statistically bounded synthetic datasets so the UI never crashes.
- **Flight route simulation**: Generates realistic flight schedules, geographical coordinates, airline distributions, and flight distances for major East Coast hubs (JFK, ATL, MIA, BOS, PHL).
- **Streamlit Caching**: Utilizes `@st.cache_data` to ensure zero redundant file reads or expensive re-computations during user interaction.

### 2. CSV Validation & Data Quality (`src/utils/csv_validator.py`)
- **Structural checks**: Verifies file existence, non-zero file sizes, parsability, and required column presence.
- **Sanitization**: Filters out placeholder markers (such as `'xx'`, `'N/A'`, `'NULL'`), normalizes comma-decimal formats common in European datasets, and coerces numeric fields.
- **Data Quality Reports**: Computes row counts, missing value tallies, null percentages, memory footprints, and summary distributions.
- **Domain Business Logic (`DataIntegrityChecker`)**:
  - *Happiness Data*: Enforces happiness scores in $[0, 10]$, non-negative GDP, and non-empty country identifiers.
  - *University Data*: Enforces the admission funnel hierarchy ($\text{Enrolled} \le \text{Admitted} \le \text{Applications}$), realistic academic year ranges, and percentage bounds $[0, 100]$ for retention and satisfaction.

### 3. Analytics Modules (`src/components/`)
- **Portfolio Overview** (`portfolio_overview.py`): Platform directory highlighting capabilities, technology stack, and navigation guide.
- **Transportation Analytics** (`transportation_analytics_simple.py`): Interactive geospatial mapping with Folium and route performance breakdowns with Plotly across domestic and international destinations. Analyzes hourly flight volume distributions, airline market shares, and flight distance patterns.
- **Education Intelligence** (`education_intelligence_simple.py`): Student success and institutional performance analytics. Tracks application and enrollment funnels, departmental enrollment distributions (Engineering, Business, Arts, Sciences), multi-year retention rates, and GPA distributions.
- **Visualization Excellence** (`visualization_excellence_simple.py`): Practical showcase of data storytelling and visualization design. Demonstrates effective chart construction versus common pitfalls, correlation modeling between GDP per capita and national happiness, and regional metric distributions.

---

## Repository Structure

```
DataFlow-Intelligence-Platform/
├── .devcontainer/
│   └── devcontainer.json          # VS Code Dev Container configuration
├── .github/
│   └── workflows/
│       └── ci.yml                 # Automated testing workflow on push / PR
├── data/
│   └── raw/
│       ├── 2022.csv               # World Happiness Report dataset
│       └── university_data.csv    # 10-year university admissions dataset
├── deployment/
│   ├── Dockerfile                 # Multi-stage container build
│   └── docker-compose.yml         # Container configuration for app & services
├── docs/
│   ├── API_DOCUMENTATION.md       # Pipeline architecture & module reference
│   ├── DEVELOPMENT_SETUP.md       # Dev setup and environment guide
│   └── USER_GUIDE.md              # User walkthrough for each module
├── src/
│   ├── app.py                     # Main Streamlit web application
│   ├── components/
│   │   ├── education_intelligence.py
│   │   ├── education_intelligence_simple.py
│   │   ├── portfolio_overview.py
│   │   ├── transportation_analytics.py
│   │   ├── transportation_analytics_simple.py
│   │   ├── visualization_excellence.py
│   │   └── visualization_excellence_simple.py
│   └── utils/
│       ├── csv_validator.py       # Structural validation and data integrity
│       ├── data_handler.py        # Centralized data loader and generator
│       └── styles.py              # CSS styles and UI color tokens
├── tests/
│   ├── __init__.py
│   └── test_platform.py           # Automated pytest test suite (22 tests)
├── .env.example                   # Environment configuration template
├── .gitignore                     # Git ignore patterns
├── CSS_FIX_REPORT.md              # UI styling fix logs
├── IMPROVEMENTS.md                # Platform enhancement notes
├── pytest.ini                     # Pytest runner configuration
├── requirements.txt               # Project Python dependencies
├── test_app.py                    # Standalone integration validation script
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Apc0015/DataFlow-Intelligence-Platform.git
cd DataFlow-Intelligence-Platform
```

### 2. Set Up a Virtual Environment
```bash
# On macOS / Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)
```bash
cp .env.example .env
```

### 5. Run the Application
```bash
streamlit run src/app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser to explore the dashboard.

---

## Running with Docker

You can also run the platform in a containerized environment using Docker:

```bash
# Build and start the container
docker compose -f deployment/docker-compose.yml up --build dataflow-platform
```

Access the application at [http://localhost:8501](http://localhost:8501).

---

## Automated Testing & CI

I wrote an automated test suite covering all data transformation pipelines, CSV validation rules, business logic integrity checks, synthetic fallbacks, and UI helpers:

```bash
# Run the complete test suite with Pytest
pytest tests/ -v

# Run the standalone pipeline verification script
python3 test_app.py
```

### What the Tests Cover:
- **Data Ingestion**: Verifies CSV row counts, column mappings, numeric conversions, and synthetic generation fallbacks.
- **Data Validation**: Tests detection of missing columns, empty files, malformed rows, placeholder strings (`xx`, `N/A`, `NULL`), and comma-decimal conversion.
- **Business Logic Integrity**: Validates domain constraints such as admission funnel ordering, retention percentage bounds, and happiness scale boundaries.
- **Domain Pipelines**: Validates education cohort generation (2,500 student records) and socioeconomic indicators.
- **Continuous Integration**: Every push and pull request to `main` is automatically tested across Python 3.11 and 3.12 via GitHub Actions (`.github/workflows/ci.yml`).

---

## Tech Stack

- **Language**: Python 3.11+
- **Frontend / Application Framework**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly, Folium, Streamlit-Folium, Matplotlib, Seaborn
- **Machine Learning & Modeling**: Scikit-learn
- **Testing**: Pytest, Pytest-Cov
- **Containerization**: Docker, Docker Compose
- **Continuous Integration**: GitHub Actions

---

## Author

**Ayush Chhoker**
- GitHub: [@Apc0015](https://github.com/Apc0015)
- LinkedIn: [linkedin.com/in/apc15](https://www.linkedin.com/in/apc15/)
- Email: [Ayushchhoker15@gmail.com](mailto:Ayushchhoker15@gmail.com)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
