# Airflow DAG Generator from Image (Vision-AI)

This project leverages Azure OpenAI's Vision capabilities to generate Apache Airflow DAG (Directed Acyclic Graph) Python code directly from an image. Simply provide a diagram of your desired Airflow DAG, and the system will attempt to convert it into executable Python code.

## ✨ Features

* **Image to DAG Code:** Automatically generates Airflow DAG Python code from a visual representation (e.g., a diagram of tasks and dependencies).
* **Base64 Encoding:** Handles local image encoding for submission to the Vision AI model.
* **Azure OpenAI Integration:** Communicates with Azure OpenAI Service to interpret the image and generate code.
* **Configurable Prompts:** Allows customization of the system prompt to guide the AI's code generation.
* **Local File Output:** Saves the generated DAG code directly to a Python file.

## 🚀 Getting Started

Follow these steps to set up and run the DAG generator.

### Prerequisites

* Python 3.8+
* An Azure OpenAI Service instance with a deployed model that supports Vision capabilities (e.g., `gpt-4o`, `gpt-4-vision-preview`).
* Your Azure OpenAI API Key and Endpoint.

### 1. Installation

Clone this repository and install the required Python packages:

```bash
git clone <your-repository-url>
cd airflow-dag-generator
pip install -r requirements.txt

requirements.txt content:

python-dotenv
requests
Pillow


