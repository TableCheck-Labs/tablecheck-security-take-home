# TableCheck Security Operations Engineer - Technical Assessment
Take-home project for the TableCheck Security Role.

## Overview
You are provided with a Python application in the app directory that implements user authentication, file handling, and system information features. Your task is to conduct a thorough security assessment and provide a comprehensive report.

## Setup
1. Review the README.md in the app directory for application setup instructions
2. The application runs locally and requires only Python with the specified dependencies
3. Test the application functionality before beginning your assessment

## Assessment Requirements

### 1. Security Assessment Report
Please provide a detailed report containing:

#### a) Executive Summary (1 page max)
- Overview of critical findings
- Risk assessment summary
- Prioritized recommendations

#### b) Vulnerability Assessment
For each security finding:
- Severity rating (Critical/High/Medium/Low)
- CVSS score where applicable
- CWE (Common Weakness Enumeration) reference
- OWASP Top 10 2021 mapping where relevant
- Impact on SOC 2 and/or ISO 27001 controls

#### c) Technical Analysis
For each vulnerability discovered:
- Detailed technical description
- Proof of concept/reproduction steps
- Specific code references
- Potential attack scenarios

#### d) Remediation Plan
For each finding:
- Detailed fix recommendations with code examples
- Suggested security controls and recommendations to avoid this issue in the future
- Provide an estimate on risk with a timeframe (example: Critical, immediate)

### 2. Security Automation
Provide examples of:
- Pre-commit hooks for security checks
- Sample security test cases
- Dependency scanning configuration
- SAST tool configuration
- Anything else you can recommend or think of

## Report Format
- Submit as a PDF or Markdown document
- Include relevant code snippets
- Maximum length: 8 pages (excluding code samples)
- Use clear section headings and formatting

## Evaluation Criteria
Your assessment will be evaluated on:
1. Depth of security analysis
2. Accuracy of vulnerability identification
3. Quality of remediation recommendations
4. Understanding of secure coding practices
5. Clarity of technical communication
6. Practicality of proposed solutions

## Time Allocation
- Complete this assessment within 3 hours
- Allocate time approximately:
  - Application review: 45 minutes
  - Vulnerability assessment: 1 hour
  - Report writing: 1 hour 15 minutes

## Submission Instructions
1. Submit your report as a single PDF file
2. Name the file: `security-assessment-{yourname}.pdf`
3. Include any supporting scripts/configs in a separate folder
4. Email or upload the submission to GitHub

## Notes
- Focus on identifying security issues, not functional bugs
- Consider both direct vulnerabilities and security misconfigurations
- Demonstrate your understanding of secure development practices
- Show how findings relate to real-world security risks
