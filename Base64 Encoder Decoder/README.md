# Cyber Encoding Toolkit

A Python-based encoding and decoding utility that supports multiple data representation formats.

This project provides tools for working with Base64, Base32, Hexadecimal, and URL Encoding formats. It also includes an automatic detection system that analyzes input data and estimates the possible encoding format.

---

# Features

* Base64 Encode / Decode
* Base32 Encode / Decode
* RFC 4648 compatible Base32 support
* Hexadecimal Encode / Decode
* Multiple Hex output formats
* URL Encode / Decode
* Standard URL Encoding
* Form URL Encoding
* Automatic Encoding Detection
* Confidence Score System
* Command Line Interface (CLI)
* File Input Support
* Batch Processing

---

# Project Structure

```
Cyber-Encoding-Toolkit/

│
├── main.py
├── base64_tool.py
├── base32_tool.py
├── hex_tool.py
├── url_tool.py
├── detector.py
└── README.md
```

---

# Installation

Requirements:

* Python 3.x

No external libraries are required.

Run the application:

```bash
python3 main.py
```

---

# What is Encoding?

Encoding is the process of converting data into another representation format.

Encoding:

* Is not encryption.
* Does not provide security.
* Makes data transfer and storage easier.
* Can be reversed back to the original data.

Example:

Original:

```
Hello
```

Encoded:

```
SGVsbG8=
```

---

# Supported Formats

## 1. Base64

Base64 converts binary data into printable ASCII characters.

Common usage:

* JWT tokens
* API data
* Email attachments
* Data transmission

### Encode

Command:

```bash
python3 main.py --type base64 --encode Hello
```

Output:

```
SGVsbG8=
```

### Decode

Command:

```bash
python3 main.py --type base64 --decode SGVsbG8=
```

Output:

```
Hello
```

---

# 2. Base32

Base32 is similar to Base64 but uses a smaller character set.

Common usage:

* Data transfer systems
* QR code systems
* Key generation systems

### Encode

Command:

```bash
python3 main.py --type base32 --encode Hello
```

Example output:

```
JBCUYTCP
```

---

# 3. Hexadecimal

Hexadecimal represents each byte using two hexadecimal characters.

Example:

Original:

```
Hello
```

Hex:

```
48656c6c6f
```

Common usage:

* Malware analysis
* Binary analysis
* Memory dump analysis
* Network analysis

---

## Hex Encode

Command:

```bash
python3 main.py --type hex --encode Hello
```

Output:

```
48656c6c6f
```

---

## Hex Decode

Command:

```bash
python3 main.py --type hex --decode 48656c6c6f
```

Output:

```
Hello
```

---

# 4. URL Encoding

URL Encoding converts unsafe characters into `%HH` encoded format.

Example:

Original:

```
hello world
```

Encoded:

```
hello%20world
```

Common usage:

* Web requests
* HTTP analysis
* Form data processing

---

## URL Encode

Command:

```bash
python3 main.py --type url --encode "hello world"
```

Output:

```
hello%20world
```

---

## Form Encoding

Form encoding replaces spaces with `+`.

Example:

```
hello+world
```

---

# Automatic Format Detection

The tool analyzes input data and predicts the possible encoding format.

Supported detections:

* Base64 patterns
* Base32 patterns
* Hexadecimal patterns
* URL Encoding patterns

Example:

Command:

```bash
python3 main.py --detect SGVsbG8=
```

Output:

```
Base64: 85%
```

---

# Command Line Usage

## Base64

Encode:

```bash
python3 main.py --type base64 --encode Test
```

Decode:

```bash
python3 main.py --type base64 --decode VGVzdA==
```

---

## Hex

Encode:

```bash
python3 main.py --type hex --encode Security
```

Decode:

```bash
python3 main.py --type hex --decode 5365637572697479
```

---

# File Analysis

The tool can analyze multiple inputs from a file.

Example:

```bash
python3 main.py --file data.txt
```

Example file:

```
SGVsbG8=
48656c6c6f
hello%20world
```

---

# Security Applications

This project demonstrates practical encoding analysis used in cybersecurity.

## Base64

Used in:

* JWT analysis
* API token inspection
* Encoded data analysis

## Hexadecimal

Used in:

* Malware analysis
* Binary inspection
* File format analysis

## URL Encoding

Used in:

* Web security testing
* HTTP request analysis
* Parameter inspection

---

# Learning Objectives

This project demonstrates:

* Data encoding standards
* String manipulation
* Binary data processing
* Regular expressions
* Pattern recognition
* CLI application development
* Modular Python project structure

---

# Technologies

* Python 3
* argparse
* base64 module
* urllib module
* Regular Expressions (re)

---

# Important Note

Encoding is not encryption.

Encoding only changes the representation of data.

It does not protect information or provide confidentiality.
