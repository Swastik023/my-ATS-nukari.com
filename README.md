
# Applicant Tracking System (ATS)

## Overview

This project is a comprehensive Applicant Tracking System (ATS) designed to streamline and automate the recruitment process. It features a web-based interface for managing job postings, candidates, and applications, and integrates with the Naukri.com API for additional job-related functionalities.

## Features

- **Job Postings**: Create, manage, and publish job postings both locally and on Naukri.com.
- **Resume Search**: Search for candidates and resumes using specific criteria such as skills and experience.
- **Candidate Management**: Track and manage candidate applications.
- **Automation**: Automates repetitive tasks like posting jobs on external job portals using Selenium and scraping job data from websites.
- **Data Processing**: ETL processes are managed using Apache Airflow for reliable data workflows.

## Project Structure

\`\`\`plaintext
ATS_Project/
│
├── app.py                 # Entry point for the Flask application
├── config.py              # Configuration settings
├── models.py              # SQLAlchemy ORM models
├── routes.py              # API routes
├── naukri_api.py          # Naukri.com API integration utilities
├── selenium_script.py     # Selenium automation for job portals
├── web_scraper.py         # Web scraper for extracting job data
├── resume_parser.py       # NLP-based resume parser
├── scrape_jobs.py         # Additional web scraping script
├── airflow_dag.py         # Airflow DAG for ETL processes
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── Dockerfile             # Docker configuration (if needed)
├── venv/                  # Virtual environment directory
├── migrations/            # Database migration files (generated by Flask-Migrate)
└── frontend/              # React frontend source files
    ├── package.json       # Node.js package configuration
    ├── public/            # Public assets (e.g., index.html, favicon.ico)
    ├── src/               # React source files
        ├── index.js       # Entry point for React
        ├── App.js         # Main React component
        ├── App.css        # Main CSS file for App component
        ├── components/    # React components
            ├── Navbar.js           # Navigation bar component
            ├── JobForm.js          # Job posting form component
            ├── JobList.js          # Job listing component
            ├── ResumeSearch.js     # Resume search form component
            ├── CandidateProfile.js # Candidate profile display component
            ├── CandidateList.js    # List of candidates component
        └── App.css                 # Main CSS for App component
\`\`\`

## Prerequisites

- **Python 3.8+**
- **Node.js & npm** (for the React frontend)
- **PostgreSQL or MySQL** (or any other SQLAlchemy-supported database)
- **Apache Airflow** (optional, for ETL processes)
- **Google Chrome and Chromedriver** (for Selenium scripts)

## Setup

#### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/your_username/ATS_Project.git
cd ATS_Project
\`\`\`

#### 2. Create and Activate a Virtual Environment

\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

#### 3. Install Backend Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

#### 4. Set Up the Database

- Configure your database URI in \`config.py\`.
- Run the following command to initialize the database:

\`\`\`bash
python app.py
\`\`\`

#### 5. Install Frontend Dependencies

Navigate to the \`frontend/\` directory and install the necessary Node.js packages:

\`\`\`bash
cd frontend
npm install
\`\`\`

#### 6. Run the Development Servers

- **Backend (Flask)**:

\`\`\`bash
python app.py
\`\`\`

- **Frontend (React)**:

\`\`\`bash
npm start
\`\`\`

## Usage

#### Job Posting

1. Access the job posting form via the web interface.
2. Fill out the form with job details and submit.
3. The job will be posted locally and on Naukri.com.

#### Resume Search

1. Navigate to the resume search page.
2. Enter search criteria (e.g., skills, experience).
3. View matching resumes retrieved from Naukri.com.

#### Automation Scripts

- **Selenium Script**: Automate job postings on external job portals.
- **Web Scraper**: Extract job data from websites.
- **Resume Parser**: Parse resumes using NLP to extract structured data.

### ETL with Airflow

1. Define and schedule ETL processes using \`airflow_dag.py\`.
2. Use Airflow’s web interface to monitor and manage tasks.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss potential changes.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, feel free to contact me:

**Swastik**
- **Email**: swastik@example.com
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/swastik)
- **GitHub**: [GitHub Profile](https://github.com/swastik)
