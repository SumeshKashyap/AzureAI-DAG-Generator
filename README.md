
# 🛠️ GenAI DAG Generator

This Python script generates Apache Airflow DAG code from a **diagram image** using **Azure OpenAI's GPT model**. Simply provide a PNG image of your DAG, and the script will output a Python `.py` file containing a valid Airflow DAG definition.

---

## 📦 Features

- 🖼️ Encodes local DAG diagrams (`.png`) as base64.
- 🤖 Sends the image to Azure OpenAI for analysis with a custom system prompt.
- 🪄 Receives and extracts DAG code in JSON format.
- 📝 Saves the DAG code to a `.py` file.

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

## 🚀 How to Run

1. Place your DAG diagram image in the root folder and name it `airflow_dag_diagram.png`.
2. Run the script:

```bash
python generatedag.py
```

3. If successful, the generated DAG code will be saved to `generated_dag.py`.

---

## ⚠️ Notes

- The image **must** be named `airflow_dag_diagram.png` or you must change the path in the script.
- The OpenAI deployment must support **vision + chat**.
- Ensure you are in the correct working directory when running the script.

---

## 🧠 Prompt Behavior

The system prompt instructs the model to:
- Use provider-specific operators when available (e.g., `S3ToRedshiftOperator`)
- Apply appropriate `TriggerRule`s
- Include edge labels using `airflow.utils.edgemodifier`
- Use `DummyOperator` for start/end tasks

---

## ✍️ Author Tagline (Optional)
*Turning complexity into clarity with data, automation, and AI.*
