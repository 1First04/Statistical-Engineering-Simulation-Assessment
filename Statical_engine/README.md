# 📊 Statistical Engineering & Simulation Engine

---

## 🚀 Project Overview

This project is a **pure Python statistical engine and simulation system** designed to:

* Process raw numerical datasets
* Compute key statistical measures (mean, median, mode, variance, standard deviation)
* Detect outliers using Z-score methodology
* Simulate real-world probabilistic scenarios using **Monte Carlo methods**
* Demonstrate the **Law of Large Numbers (LLN)** through server failure simulation

The system is built **from scratch using only Python standard libraries**, emphasizing both **mathematical correctness** and **software engineering best practices**.

---

## 🧠 Mathematical Logic

### 📌 Variance Formula

The project implements both **Population Variance** and **Sample Variance**:
<img width="563" height="260" alt="image" src="https://github.com/user-attachments/assets/48eac7cd-6035-4569-b908-16f7c111434f" />


👉 The key difference is:

* Population uses **n**
* Sample uses **(n - 1)** to reduce bias

---

### 📌 Median (Even vs Odd Handling)

* **Odd and Even number of elements**:

<img width="685" height="107" alt="image" src="https://github.com/user-attachments/assets/bc655fb1-728c-4ee7-94a1-9f51cdfad8c7" />

==> This ensures accurate central tendency regardless of dataset size.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/statistical-engine.git
cd statistical-engine
```

---

### 2. Run the Main Program

```bash
python main.py
```

---

### 3. (Optional) Run in Jupyter Notebook

```bash
jupyter notebook
```

Then import:

```python
from stat_engine import StatEngine
```

---

## 🧪 Testing

This project uses Python’s built-in `unittest` framework.




---

