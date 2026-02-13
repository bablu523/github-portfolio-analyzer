# 🚀 AI-Powered GitHub Portfolio Analyzer & Enhancer

![Hackathon](https://img.shields.io/badge/Hackathon-UnsaidTalks-blue)
![Tech Stack](https://img.shields.io/badge/Tech-FastAPI%20|%20Gemini%20AI%20|%20TailwindCSS-success)

## 📌 The Problem
For early-career developers, GitHub is their professional portfolio. Yet, most profiles fail to communicate real skill, consistency, or real-world impact to recruiters. Great developers often get their resumes passed over simply because their repositories lack clear "hiring signals" like documentation, architecture context, and narrative.

## 💡 The Solution
This AI-powered evaluator bridges the gap between raw code and what hiring managers actually look for. By analyzing a user's repositories, it acts as a **Senior Technical Recruiter**, providing an objective score and actionable feedback.

### ✨ Key Features
* **Live GitHub API Integration:** Fetches real-time repository data, languages, and documentation status.
* **AI Recruiter Brain:** Powered by Google Gemini 2.5 Flash, tuned with a highly specific prompt to look for engineering maturity and storytelling.
* **Recruiter Readiness Score (0-100):** An objective benchmark of how hirable the profile looks.
* **Actionable Insights:** Generates specific Green Flags (strengths), Red Flags (gaps), and high-value next steps (e.g., "Add an architecture diagram to Repo X").
* **One-Click PDF Export:** Students can instantly download their recruiter report to track their progress.

## 🛠️ System Architecture & Tech Stack
* **Backend:** Python & FastAPI (for lightning-fast, asynchronous API requests).
* **AI Engine:** Google Generative AI (Gemini 2.5 Flash) for parsing code signals into human-readable recruiter advice.
* **Frontend:** HTML, Vanilla JavaScript, and Tailwind CSS (via CDN) for a clean, student-friendly interface.
* **Export:** `html2pdf.js` for seamless report generation.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/bablu523/github-portfolio-analyzer.git](https://github.com/bablu523/github-portfolio-analyzer.git)
   cd github-portfolio-analyzer
