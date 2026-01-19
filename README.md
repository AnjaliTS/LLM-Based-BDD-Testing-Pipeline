LLM-Based BDD Testing Pipeline

A system for generating, validating, and executing Behavior-Driven Development (BDD) test scenarios from natural language requirements using Large Language Models (LLMs).

This repository demonstrates a complete pipeline that:

Takes user requirements in plain English

Uses an LLM to generate Gherkin feature scenarios

Allows human review and approval

Filters and executes approved tests using traditional BDD tooling

Produces test reports and artifacts

This approach bridges modern AI language understanding with traditional BDD test automation.

🚀 Features

✅ LLM-driven scenario generation
Convert free-text requirements into executable Gherkin scenarios.

📋 Scenario validation & human approval
Focus on happy path (and optionally negative / edge cases).

🛠 Test execution harness
Uses BDD frameworks to automate tests derived from generated scenarios.

📊 Rich reports & artifacts
HTML reports, summaries, and execution logs are captured for analysis.

📌 Example outputs included
Pre-generated .feature files and test reports are stored in the repo.

📦 Repository Structure
.
├── config.py                     # Configuration for LLM and execution
├── py313_tester.py                   # Entrypoint to generate & run tests
├── generated_scenarios_*.feature  # Auto-generated Gherkin files
├── scenarios_*.feature           # Approved, executable scenarios
├── *.json                       # Approval records & pipeline reports
├── *.html                       # Test execution reports
├── *.png                        # UI screenshots from test runs
├── requirements.txt             # Python dependencies
├── execution_summary.txt        # Test execution summary
└── .gitignore

🧠 How It Works

Input requirements
Provide user stories or specification sentences describing app behavior.

LLM Processing
A language model analyzes the input and writes Gherkin scenarios.

Review & Approval
Generated scenarios are manually reviewed and marked approved.

Scenario orchestration
Approved scenarios are assembled as .feature files.

Test automation
Tests are executed using a BDD framework + automation engine.

Reports & Logging
Test results are captured in human-readable HTML reports and summaries.

🧪 Example

A requirement like:

Users should be able to login, submit orders, and track order status

might generate Gherkin steps like:

Feature: User Order Management

  Scenario: Successful Login
    Given a user is on the login page
    When the user enters correct credentials
    Then the user is logged in


Automated execution produces HTML reports summarizing pass/fail results.

🧩 Installation

Ensure Python 3.10+ is installed:

git clone https://github.com/AnjaliTS/LLM-Based-BDD-Testing-Pipeline.git
cd LLM-Based-BDD-Testing-Pipeline
pip install -r requirements.txt

▶️ Running the Pipeline

To generate and run tests locally:

python py313_tester.py


This script will:

Generate Gherkin scenarios via the LLM

Apply approval filters

Run tests and save reports
