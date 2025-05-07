# 💰 Personal Finance Tracker (Python)

A command-line based Personal Finance Tracker built with Python that allows users to log income/expenses, filter transactions by date, view summaries, and generate insightful plots of their financial history.

> 🚀 Designed for individuals who want simple yet powerful local financial tracking without the need for cloud integrations or third-party apps.

---

## 📸 Demo

```bash
 Finance Tracker
1. Add a new Transaction
2. View Transactions and summary within a date range
3. Exit

Automatically calculates total income, total expenses, and net savings.

Visualizes trends using Matplotlib.

.
├── main.py                 # Entry point
├── data_entry.py           # Handles user inputs
├── finance_data.csv        # Transaction data (auto-generated)
├── requirements.txt        # Project dependencies
└── README.md               # You're here!

✨ Features
📅 Date-based transaction logging

💸 Categorize as Income or Expense

🧾 Save and view transaction history in CSV format

📊 Plot income vs. expenses over time

✅ Built-in data validation

📁 Lightweight and file-based, no database required


🛠️ Tech Stack
Python 3.11+

Pandas

Matplotlib

CSV module

CLI-based interface

🖥️ Installation & Setup
Clone the repo
git clone https://github.com/your-username/personal-finance-tracker.git
cd personal-finance-tracker

Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

Install dependencies
pip install -r requirements.txt

Run the application
python main.py

📈 Plot Example
After choosing to view transactions, you'll be asked:
Do you want to plot the transactions? (y/n): y
This will generate a date-wise line chart of your income and expenses.

📌 Sample CSV Format
Date,Amount,Category,Description
06-05-2025,500.0,Income,Salary
05-06-2025,650.2,Expense,Mobile
...

✅ TODO / Roadmap
 Add monthly/weekly summaries

 Export report as PDF

 Add budgeting goals and limits

 GUI version using Tkinter or PyQt

👨‍💻 Author

Vicky Mahajan
Python Developer | MERN Stack Developer
📧 vickyworks50@gmail.com
🔗 LinkedIn
🔗 Portfolio
