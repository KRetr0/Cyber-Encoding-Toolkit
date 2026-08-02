<div align="center">

# 🔐 Cyber Encoding Toolkit




### Encoding & Detection Security Utility

A lightweight cybersecurity tool for encoding, decoding and format detection.

<br>

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Status-v1.0.0-success.svg)]()

</div>


---

# 📌 About

**Cyber Encoding Toolkit** is a lightweight command-line cybersecurity utility developed with Python.

The purpose of this project is to provide a simple and fast tool for common encoding and decoding operations used in:

- 🔹 Cybersecurity learning
- 🔹 CTF challenges
- 🔹 Security research
- 🔹 Data analysis
- 🔹 Developer workflows


The project focuses on:

```
Simple
Fast
Modular
Extendable
```

---

# ✨ Features

## 🔐 Encoding & Decoding

Supported formats:

| Format | Encode | Decode |
|---|---|---|
| Base64 | ✅ | ✅ |
| Base32 | ✅ | ✅ |
| Hexadecimal | ✅ | ✅ |
| URL Encoding | ✅ | ✅ |


---

## 🔎 Automatic Detection

The toolkit can analyze input data and detect possible encoding formats.

Example:

```
Input:

SGVsbG8=


Detection:

Most Possible Format:
Base64

Confidence:
85%
```

---

# 🖥️ CLI Interface


```
====================================
 Cyber Encoding Toolkit v1.0.0
====================================

1 - Base64 Encode
2 - Base64 Decode

3 - Base32 Encode
4 - Base32 Decode

5 - Hex Encode
6 - Hex Decode

7 - URL Encode
8 - URL Decode

9 - Automatic Detection

0 - Exit

====================================
```

---

# 🚀 Installation


## Clone Repository

```bash
git clone https://github.com/KRetr0/Cyber-Encoding-Toolkit.git
```


Enter directory:

```bash
cd Cyber-Encoding-Toolkit
```


Run:

```bash
python3 main.py
```


---

# 📚 Usage Examples


## Base64 Encode


Input:

```
Hello World
```


Output:

```
SGVsbG8gV29ybGQ=
```


---

## Hex Encode


Input:

```
Hello
```


Output:

```
48656c6c6f
```


---

## URL Encode


Input:

```
Hello World
```


Output:

```
Hello%20World
```


---

# 🏗️ Project Structure


```
Cyber-Encoding-Toolkit/

│
├── main.py
├── banner.py
│
├── encoders/
│   ├── base64_tool.py
│   ├── base32_tool.py
│   ├── hex_tool.py
│   └── url_tool.py
│
├── core/
│   ├── detector.py
│   └── errors.py
│
├── tests/
│
├── README.md
├── LICENSE
└── requirements.txt

```


---

# 🧪 Testing


Run tests:

```bash
pytest
```


---

# 🛠️ Built With


- Python 3
- Base64 Library
- URL Parsing
- Regular Expressions
- Pytest


---

# 🗺️ Roadmap


## v1.0.0 ✅

Completed:

- [x] CLI Interface
- [x] ASCII Banner
- [x] Base64 Support
- [x] Base32 Support
- [x] Hex Support
- [x] URL Encoding Support
- [x] Detection Engine
- [x] Error Handling


## Future Updates 🚀


Planned:

- [ ] GUI Version
- [ ] Logging System
- [ ] More Encoding Formats
- [ ] Windows Executable
- [ ] Better Detection Engine


---

# 🔐 Security Notice


This project is created for educational and defensive security purposes.


It does **not** include:

- Password cracking
- Exploitation tools
- Malware functionality


This tool only performs encoding, decoding and detection operations.


---

# 👨‍💻 Author


**KRetr0**

Cybersecurity & Software Development Enthusiast


GitHub:

https://github.com/KRetr0


---

# 📄 License


This project is licensed under the MIT License.


<div align="center">

⭐ If you like this project, consider giving it a star!

</div>
