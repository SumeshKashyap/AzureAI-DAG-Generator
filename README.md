
# 🛠️ GenAI DAG Generator

This Python script generates Apache Airflow DAG code from a **diagram image** using **Azure OpenAI's GPT model**. Simply provide a PNG image of your DAG, and the script will output a Python `.py` file containing a valid Airflow DAG definition.

---

##  Features

- Encodes local DAG diagrams (`.png`) as base64.
-  Sends the image to Azure OpenAI for analysis with a custom system prompt.
-  Receives and extracts DAG code in JSON format.
-  Saves the DAG code to a `.py` file.

---

## 🧾 Requirements

- Python 3.8+
- Access to Azure OpenAI with a **chat completion deployment** that supports **image input**
- `.env` file with credentials

### 🔧 Python Libraries

Install dependencies:

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```txt
Pillow
requests
python-dotenv
```

---

## 🔐 .env Configuration

Create a `.env` file in the same directory as your script with the following content:

```env
OPENAI_API_KEY=<your-azure-openai-api-key>
OPENAI_API_ENDPOINT=https://<resource>.openai.azure.com/openai/deployments/<deployment-name>/chat/completions?api-version=2024-02-15-preview
```

Replace values appropriately based on your Azure OpenAI resource and deployment.

---

## 📁 Folder Structure

```
GenAI DAG Generator/
│
├── airflow_dag_diagram.png     # Your input DAG diagram (PNG format)
├── generated_dag.py            # Output file (will be generated)
├── generatedag.py              # Main script
├── .env                        # Your Azure OpenAI credentials
└── README.md                   # This file
```

---

##  How to Run

1. Place your DAG diagram image in the root folder and name it `airflow_dag_diagram.png`.
2. Run the script:

```bash
python generatedag.py
```

3. If successful, the generated DAG code will be saved to `generated_dag.py`.

---

##  Notes

- The image **must** be named `airflow_dag_diagram.png` or you must change the path in the script.
- The OpenAI deployment must support **vision + chat**.
- Ensure you are in the correct working directory when running the script.

---

##  Prompt Behavior

The system prompt instructs the model to:
- Use provider-specific operators when available (e.g., `S3ToRedshiftOperator`)
- Apply appropriate `TriggerRule`s
- Include edge labels using `airflow.utils.edgemodifier`
- Use `DummyOperator` for start/end tasks

---


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


2. Configuration
Create a .env file in the root directory of your project (the same directory as your Python script) and add your Azure OpenAI credentials:

Code snippet

OPENAI_API_KEY="YOUR_AZURE_OPENAI_KEY"
OPENAI_API_ENDPOINT="https://<your-resource-name>[.openai.azure.com/openai/deployments/](https://.openai.azure.com/openai/deployments/)<your-deployment-name>/chat/completions?api-version=2024-02-15-preview"
Replace YOUR_AZURE_OPENAI_KEY with your actual Azure OpenAI API key.
Replace the OPENAI_API_ENDPOINT with your specific endpoint URL, including your resource name, deployment name, and API version.
3. Prepare Your DAG Diagram
Place your Airflow DAG diagram image file (e.g., airflow-dag-diagram.png) in the same directory as your Python script or update the local_image_path variable in main.py accordingly.

Example airflow-dag-diagram.png (conceptual):
(Imagine an image here showing a simple Airflow DAG with nodes like "Start Task" -> "Process Data" -> "Load Data" -> "End Task", possibly with labels.)

4. Running the Generator
Execute the main Python script:

Bash

python your_script_name.py
(Replace your_script_name.py with the actual name of your Python file, e.g., generate_dag.py)

The script will:

Read and encode your image.
Send the encoded image and a system prompt to the Azure OpenAI Vision model.
Extract the generated Python DAG code from the AI's response.
Save the generated code to a file named generated_dag.py (or your specified output_path).

