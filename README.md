# 🔐 Secure and Efficient Anonymous Authentication for Distributed Healthcare Systems Handling Medical Big Data

This project implements and analyzes a **lightweight, secure, and anonymous mutual authentication scheme** for distributed IoT-enabled healthcare systems handling medical big data. 
This repository contains both the **protocol specification** written in Verifpal and a **Python-based implementation/simulation** of the scheme.

---

## 📜 Project Highlights

- **Secure Mutual Authentication** between users and IoT devices via a gateway.
- **Anonymity**, **integrity**, and **lightweight design** using:
  - XOR operations
  - Hash functions
  - Timestamp verification
  - Session key generation and validation
- **Formally verified** using the Verifpal symbolic analysis tool to prove resistance to:
  - Replay attacks
  - Man-in-the-middle (MITM)
  - Eavesdropping
  - Privileged insider and capture attacks

---

## 📁 Files Included

| File/Folder       | Description |
|-------------------|-------------|
| `scheme.vp`       | Verifpal model of the authentication protocol |
| `auth_scheme.py`  | Python implementation of the scheme (simulation + hash logic) |
| `README.md`       | This file |

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


