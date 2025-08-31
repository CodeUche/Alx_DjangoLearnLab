# Vuln Hunter
https://codeuche.pythonanywhere.com/scan/

Vuln Hunter is a web application vulnerability scanning platform built with Django, Celery, and Nmap/WhatWeb.
It allows users to scan domains, IP addresses, or URLs to detect potential vulnerabilities, enumerate services, and analyze plugins or technologies running on a target.
The application supports both web-based scanning via forms and API-based scanning via JSON requests.

# Features

    # Multiple Scan Profiles:
        - Fast (-T4 -F)
        - Aggressive (-T4 -A -v)
        - UDP (-sU --top-ports 100)
        - Full (-p- -sV -sC)
        - Stealth (-sS -T3)
        - WhatWeb (technology fingerprinting)

    # Background Task Execution with Celery.
    # Task Status Tracking using Celery task IDs.
    # Result Storage in the database (both structured JSON and raw text).
    # Web UI to submit scans, view progress, and check results.
    # REST API endpoints for integration and automation.
    # Plugin Descriptions for common services (e.g., Apache, MySQL, Redis, PHP).

# Tech Stack
    Backend: Django, Django REST Framework
    Task Queue: Celery
    Broker/Backend: Redis
    Scanning Tools: Nmap, WhatWeb
    Containers: Docker (optional)
    Database: MySQL (or SQLite for local development)
    Frontend: HTML, CSS (custom styles, dark theme)

# Installation
1. Clone the Repository
` git clone https://github.com/CodeUche/ALX_Capstone_Project.git`
` cd vuln-hunter `

2. Create and Activate a Virtual Environment
` python -m venv venv `
` source venv/bin/activate `  # On Linux/Mac
` venv\Scripts\activate `      # On Windows

3. Install Dependencies
` pip install -r requirements.txt `

# Dependencies include:
- Django
- djangorestframework
- celery
- redis
- python-nmap

4. Install Scanning Tools

Make sure nmap and whatweb are installed and available in your system’s PATH.

On Ubuntu/Debian:
` sudo apt update `
` sudo apt install nmap whatweb `

On macOS:
` brew install nmap whatweb `

5. Configure Database
    Edit your settings.py to configure your database (MySQL, SQLite, etc.).

# Run migrations:
` python manage.py migrate `

6. Start Services
# Start Django server
` python manage.py runserver `

# Start Celery worker
`celery -A project_name worker -l info`

# Replace project_name with your Django project name.
# Start Redis
`redis-server`
# Optionally you can use docker - My personal favourite


# Usage
    Web Interface
        1. Navigate to: http://127.0.0.1:8000/scan/
        2. Enter a target (IP/domain).
        3. Choose a scan type.
        4. Submit the scan and wait for results.

# Pages:
    /scan/ – scan submission form
    /scan/submitted/<scan_id>/ – scan progress page
    /scan/result/<scan_id>/ – results page

# API Endpoints
    Start a Scan
    POST /api/scan
    Content-Type: application/json

    {
    "target": "example.com",
    "scan_type": "full"
    }

# Check Scan Status
    GET /api/status/<scan_id>/


# Response example:
{
  "scan_id": 5,
  "status": "COMPLETED",
  "result_json": {
    "target": "example.com",
    "scan_type": "nmap",
    "ports": [
      {"number": 80, "state": "open", "service": "http", "description": "Apache Web Server"},
      {"number": 443, "state": "open", "service": "https", "description": "Nginx Web Server"}
    ]
  },
  "result_text": "Host: example.com ... "
} 


# Models Overview
    - User: Stores username, email, password, and login timestamps.
    - ScanJob: Represents a scan request (target, type, status, results).
    - ScanResult: Stores detailed scan results, parsed data, and vulnerabilities.
    - AuthenticationLog: Tracks user login and logout activity.

# Demo (Terminal Test)
` python manage.py shell `
Run a manual scan from the Django shell:

from vuln_hunter.tasks import run_nmap_scan
from vuln_hunter.models import ScanJob
from django.utils import timezone

scan = ScanJob.objects.create(
    target="google.com",
    scan_type="full",
)
result = run_nmap_scan.delay(scan.id)
print(result.id)

This will enqueue a scan task and return the Celery task ID.

# Known Issues

    - Make sure nmap and whatweb are installed on the server; otherwise, scans will fail.
    - Scans may require root privileges for certain scan types (e.g., UDP, stealth).
    - Long-running scans may need Celery configuration adjustments for timeouts.

# Future Improvements

    - Authentication for API endpoints.
    - Scheduled scans.
    - Reporting system (PDF/CSV export).
    - Real-time WebSocket updates instead of polling.
    - Integration with vulnerability databases.

