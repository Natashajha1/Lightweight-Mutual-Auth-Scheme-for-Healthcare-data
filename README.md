# 🔐 Secure and Efficient Anonymous Authentication for Distributed Healthcare Systems Handling Medical Big Data

This project implements and analyzes a **lightweight, secure, and anonymous mutual authentication scheme** for distributed IoT-enabled healthcare systems handling medical big data. 
This repository contains both the **protocol specification** written in Verifpal and a **Python-based implementation/simulation** of the scheme.

---

## 📜 Project Highlights

- **Secure Mutual Authentication** between users and IoT devices via a gateway.

 ## 🚀 Features

- ✅ **Mutual Authentication** between users and IoT devices via gateway
- ✅ **Anonymity & Untraceability**: Conceals user identity across sessions
- ✅ **Replay & MITM Resistance** using timestamps and challenge–response validation
- ✅ **Lightweight Design**: Efficient for constrained IoT environments
- ✅ **Secure Key Exchange** based on hashing and XOR-based session generation and validation
- ✅ **Formal Security Verification** using Verifpal against multiple attack vectors to prove resistance to:
- - Replay attacks
  - Man-in-the-middle (MITM)
  - Eavesdropping
  - Privileged insider and capture attacks
- ✅ **Python Simulation** for step-by-step cryptographic workflow

---

## 📁 Files Included

| File/Folder       | Description |
|-------------------|-------------|
| `scheme.vp`       | Verifpal model of the authentication protocol |
| `auth_scheme.py`  | Python implementation of the scheme (simulation + hash logic) |
| `README.md`       | This file |
| `project_ppt`     | Project presentation |


---

## ▶️ How to Run

### 1. 🔒 Verifpal Protocol Analysis

Install Verifpal from: https://verifpal.com/#download

```bash
verifpal analyze scheme.vp
```
### 2. Python Simulation
Ensure Python 3.x is installed, then run:

```bash
python3 auth_scheme.py
```
This simulates parts of the authentication workflow, hash validation, and session key operations.

### Results
![results](https://github.com/user-attachments/assets/b49c076e-1388-4aac-a779-92c686e72b4e)


