
# FormalChain - A Simple Blockchain Project

Welcome to FormalChain, a beginner-friendly blockchain project implemented in Python using Flask. This project aims to provide you with a hands-on introduction to blockchain technology. Feel free to explore, learn, and expand upon it.

![FormalChain](assets/formalchain.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

## Introduction

FormalChain is a basic blockchain system designed for educational purposes. It includes fundamental blockchain components such as blocks, transactions, mining, and a simple web interface.

## Features

- **Blockchain:** A simplified blockchain structure with blocks and transactions.
  
- **Mining:** Proof-of-work mining to secure the blockchain and add new blocks.

- **Transactions:** Ability to create and verify transactions.

- **Web Interface:** A basic web interface to interact with the blockchain.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following:

- Python 3.x
- Flask (install via `pip install Flask`)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/FormalChain.git
   cd FormalChain
   ```

2. Set up a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: .\venv\Scripts\Activate.ps1
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python main.py
   ```

5. Access the blockchain explorer in your web browser at `http://localhost:5000`.

## Usage

Explore the following basic functionalities:

- Mine new blocks by visiting `/mine` in your browser.

- Create transactions by sending POST requests to `/transactions/new` with JSON data containing sender, recipient, and amount.

- View the entire blockchain at `/chain`.
