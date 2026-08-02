# 🔐 Cyber Encoding Toolkit

```
 ██████╗██╗   ██╗██████╗ ███████╗██████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝


        Cyber Encoding Toolkit v1.0.0
        Encoding & Detection Security Utility
```

<p align="center">

A lightweight cybersecurity utility for encoding, decoding and detecting common data formats.

</p>

---

## 📌 About The Project

**Cyber Encoding Toolkit** is a simple and modular command-line security tool developed with Python.

The purpose of this project is to provide a fast way to perform common encoding and decoding operations used during:

- Cybersecurity learning
- CTF challenges
- Security testing
- Data analysis
- Developer workflows

The project focuses on being:

✅ Simple  
✅ Fast  
✅ Modular  
✅ Easy to extend  

---

# 🚀 Features

## Encoding & Decoding

Supported formats:

| Format | Encode | Decode |
|---|---|---|
| Base64 | ✅ | ✅ |
| Base32 | ✅ | ✅ |
| Hexadecimal | ✅ | ✅ |
| URL Encoding | ✅ | ✅ |


---

## 🔎 Automatic Detection

The toolkit can analyze input data and estimate possible formats.

Example:

```
Input:

SGVsbG8=


Output:

Detection Results:

Base64: 85%
```

---

# 🖥️ CLI Interface

Example:

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

# ⚙️ Installation

## Requirements

- Python 3.10+

Clone repository:

```bash
git clone https://github.com/KRetr0/Cyber-Encoding-Toolkit.git
```

Enter project folder:

```bash
cd Cyber-Encoding-Toolkit
```

Run:

```bash
python main.py
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

# 🛠️ Technologies

Built with:

- Python
- Base64 Module
- URL Parsing
- Regex Detection
- Pytest

---

# 🎯 Roadmap

## v1.0.0

Completed:

- ✅ CLI interface
- ✅ Banner system
- ✅ Base64 support
- ✅ Base32 support
- ✅ Hex support
- ✅ URL encoding support
- ✅ Detection engine
- ✅ Error handling


## Future Updates

Planned:

- GUI version
- More encoding formats
- Better detection engine
- Logging system
- Windows executable release


---

# 🔐 Security Notice

This project is created for educational and defensive security purposes.

It does not perform:

- Password cracking
- Exploitation
- Malware analysis

It is only designed for encoding and decoding operations.

---

# 👨‍💻 Author

**KRetr0**

Cybersecurity & Software Development Enthusiast

GitHub:

https://github.com/KRetr0

---

# 📄 License

This project is licensed under the MIT License.