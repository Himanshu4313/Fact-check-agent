# Fact-Check Agent: AI-Powered Truth Verification System

## Overview

Fact-Check Agent is an AI-powered web application designed to combat misinformation and outdated content in documents. The system automatically analyzes PDF files, extracts factual claims, verifies them against live web sources, and generates an actionable fact-checking report.

In today's AI-driven content ecosystem, marketing reports, research papers, blogs, and business documents often contain outdated statistics, incorrect figures, or hallucinated information. Fact-Check Agent acts as a "Truth Layer" that helps users validate information before making decisions.

---

## Problem Statement

Organizations increasingly rely on AI-generated and internet-sourced content. However, factual inaccuracies can lead to:

- Poor business decisions
- Loss of credibility
- Incorrect reporting
- Compliance risks
- Misinformation propagation

Manually verifying every statistic or claim is time-consuming and inefficient.

### Solution

Fact-Check Agent automates the verification process by:

1. Extracting factual claims from uploaded PDFs
2. Searching trusted live web sources
3. Comparing claims against real-world evidence
4. Generating a structured verification report

---

## Key Features

### Smart Claim Extraction

Automatically identifies:

- Statistics
- Dates
- Percentages
- Financial figures
- Technical statements
- Business metrics

### Live Web Verification

Cross-checks extracted claims using real-time web search results.

### AI-Powered Validation

Uses Large Language Models (Gemini) to analyze evidence and determine claim accuracy.

### Intelligent Classification

Each claim is categorized as:

-  Verified
-  Inaccurate
-  False

### Downloadable Reports

Generate structured verification reports for auditing and further analysis.

---

## System Workflow

```text
PDF Upload
     ↓
Text Extraction
     ↓
Claim Identification
     ↓
Live Web Search
     ↓
Evidence Collection
     ↓
AI Verification Engine
     ↓
Fact-Checking Report
```

---

## Technology Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Layer
- Google Gemini

### Search Layer
- Tavily Search API

### Data Processing
- PyMuPDF
- Pandas

### Environment Management
- Python Dotenv

---

## Architecture

### 1. Document Processing Layer

Extracts raw text from uploaded PDF documents.

### 2. Claim Extraction Layer

Identifies verifiable factual statements from unstructured text.

### 3. Verification Layer

Retrieves supporting evidence using live web search.

### 4. Decision Engine

Evaluates claims against collected evidence using AI reasoning.

### 5. Reporting Layer

Produces a structured fact-check report with verification status and explanations.

---

## Example Output

| Claim | Status | Explanation |
|---------|---------|-------------|
| Google was founded in 1998 | Verified | Matches multiple trusted sources |
| Earth has two moons | False | No credible evidence supports claim |
| India's population is 1.8 billion | Inaccurate | Latest estimates are significantly lower |

---

## Business Impact

### For Marketing Teams
Validate campaign statistics before publication.

### For Researchers
Verify factual accuracy in reports and whitepapers.

### For Content Teams
Reduce misinformation and improve content quality.

### For Enterprises
Build trust and compliance through automated fact verification.

---

## Project Structure

```text
fact-check-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── services/
│   ├── pdf_parser.py
│   ├── claim_extractor.py
│   ├── web_search.py
│   └── verifier.py
│
└── utils/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Himanshu4313/Fact-check-agent.git
cd fact-check-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run Application

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Deployment

The application can be deployed on:

- Streamlit Cloud
- Render
- Vercel

---

## Future Enhancements

### Confidence Scoring
Assign confidence levels to every verification result.

### Source Attribution
Display references used during verification.

### Multi-Language Support
Fact-check content across multiple languages.

### Batch Processing
Verify multiple PDF documents simultaneously.

### Enterprise Dashboard
Analytics and monitoring for large organizations.

---

## Why This Project Matters

As AI-generated content becomes mainstream, the ability to automatically validate information will become increasingly critical. Fact-Check Agent demonstrates how AI can be used not only to generate content but also to improve trust, transparency, and reliability in digital information systems.


