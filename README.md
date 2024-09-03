### **Updated [README.md](http://readme.md/)**

```markdown
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

```

### **Detailed Explanation of the `components/` Directory**

- **`Navbar.js`**: A navigation bar that allows users to navigate between different sections of the ATS, such as job postings, resume search, and candidate management.
- **`JobForm.js`**: A form component where users can input details for a new job posting and submit it to be stored locally and posted on [Naukri.com](http://naukri.com/).
- **`JobList.js`**: Displays a list of all job postings, fetched from the backend, allowing users to view and manage them.
- **`ResumeSearch.js`**: A form component that allows users to input search criteria and fetch matching resumes from [Naukri.com](http://naukri.com/).
- **`CandidateProfile.js`**: Displays detailed information about a candidate, including their skills, experience, and education.
- **`CandidateList.js`**: Displays a list of candidates, typically showing search results or candidates for a specific job posting.

### **Prerequisites**

- **Python 3.8+**
- **Node.js & npm** (for the React frontend)
- **PostgreSQL or MySQL** (or any other SQLAlchemy-supported database)
- **Apache Airflow** (optional, for ETL processes)
- **Google Chrome and Chromedriver** (for Selenium scripts)

### **Setup**
## Using Docker

You can also run the entire application using Docker, which will handle both the React frontend and Flask backend in a single containerized environment.

### Dockerfile Explanation

This project uses a multi-stage Docker build to handle both the React frontend and the Flask backend:

```
dockerfileCopy code
# Stage 1: Build React Frontend
FROM node:18-alpine AS build

WORKDIR /app

# Install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy and build the React application
COPY frontend/ ./
RUN npm run build

# Stage 2: Setup Flask Backend
FROM python:3.9-slim

WORKDIR /app

# Install backend dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . .

# Copy the built React frontend from the previous stage
COPY --from=build /app/build /app/frontend/build

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]

```

### Building and Running the Docker Container

1. **Build the Docker image**:
    
    In the root directory of the project, run:
    
    ```bash
    bashCopy code
    docker build -t ats_project .
    
    ```
    
2. **Run the Docker container**:
    
    Once the image is built, run the container:
    
    ```bash
    bashCopy code
    docker run -p 5000:5000 ats_project
    
    ```
    
    This command will map port 5000 of your local machine to port 5000 of the Docker container, allowing you to access the application via `http://localhost:5000`.
    
3. **Access the Application**:
    - The Flask API will be running on `http://localhost:5000`.
    - The React frontend is served statically by Flask and is accessible at the same URL.
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      
### 1. Clone the Repository

```bash
git clone <https://github.com/your_username/ATS_Project.git>
cd ATS_Project

```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

```

### 3. Install Backend Dependencies

```bash
pip install -r requirements.txt

```

### 4. Set Up the Database

- Configure your database URI in `config.py`.
- Run the following command to initialize the database:

```bash
python app.py

```

### 5. Install Frontend Dependencies

Navigate to the `frontend/` directory and install the necessary Node.js packages:

```bash
cd frontend
npm install

```

### 6. Run the Development Servers

- **Backend (Flask)**:

```bash
python app.py

```

- **Frontend (React)**:

```bash
npm start

```

### **Usage**

### Job Posting

1. Access the job posting form via the web interface.
2. Fill out the form with job details and submit.
3. The job will be posted locally and on [Naukri.com](http://naukri.com/).

### Resume Search

1. Navigate to the resume search page.
2. Enter search criteria (e.g., skills, experience).
3. View matching resumes retrieved from [Naukri.com](http://naukri.com/).

### Automation Scripts

- **Selenium Script**: Automate job postings on external job portals.
- **Web Scraper**: Extract job data from websites.
- **Resume Parser**: Parse resumes using NLP to extract structured data.

### ETL with Airflow

1. Define and schedule ETL processes using `airflow_dag.py`.
2. Use Airflow’s web interface to monitor and manage tasks.

### **Contributing**

Contributions are welcome! Please submit a pull request or open an issue to discuss potential changes.

### **License**

This project is licensed under the MIT License.

### **Contact**

For any questions or feedback, feel free to contact me:

**Swastik**

- **Email**: [swastikwork007@example.com](mailto:swastikwork007@outlook.com)
