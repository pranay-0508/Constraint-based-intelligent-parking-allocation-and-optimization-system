
# Constraint-based Intelligent Parking Allocation and Optimization System

## Description
AI-based smart parking management system using Constraint Satisfaction Problem (CSP), heuristic search, and explainable AI reasoning for intelligent parking allocation and optimization.

## Features
- Super Admin and Admin Authentication
- Unique Admin Code Generation
- CSP-Based Parking Allocation
- Priority and Distance Optimization
- Parking Analytics Dashboard
- Real-Time Slot Monitoring
- Explainable AI Reasoning

## Technologies Used
- Python
- Streamlit
- SQLite
- Pandas
- Plotly

## How to Run

### Step 1 — Install Dependencies

pip install -r requirements.txt

### Step 2 — Initialize Database

python src/init_db.py

### Step 3 — Run Application

streamlit run dashboard/streamlit_app.py

### Step 4 — Open Browser

http://localhost:8501

## Workflow

1. Register Super Admin
2. Login as Super Admin
3. Generate Unique Admin Code
4. Register Admin using generated code
5. Login as Admin
6. Allocate Parking Slots
7. View Analytics Dashboard
