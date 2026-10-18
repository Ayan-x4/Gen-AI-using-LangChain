# LangChain Models

Small Python examples for learning how to use LangChain with chat models,
Hugging Face models, Google Gemini, text embeddings, and document similarity.

This repository is a collection of independent experiments rather than one
deployable application. Each script can be run separately from the repository
root.

## Examples included

| Folder | Script | Demonstrates |
| --- | --- | --- |
| `ChatModels/` | `chatmodel_google.py` | Calling Google Gemini through LangChain. |
| `ChatModels/` | `chatmodel_hf_local.py` | Running TinyLlama locally with a Transformers pipeline. |
| `ChatModels/` | `chatmodel_huggingface_model.py` | Calling TinyLlama through a hosted Hugging Face endpoint. |
| `EmbeddedModels/` | `embedding_hf_local.py` | Creating an embedding for a single text with a local Hugging Face model. |
| `EmbeddedModels/` | `document_similarity.py` | Finding the most similar WWE document with cosine similarity. |
| `Langchain_Prompts/` | `chatbot.py` | Using TinyLlama as an interactive terminal chatbot. |

The examples use these models:

- **Chat and text generation:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2`
- **Google chat:** `gemini-3.6-flash` as configured in `chatmodel_google.py`

## Requirements

- Python 3.10 or newer
- Internet access for the first model download and for hosted providers
- A compatible PyTorch installation for local Hugging Face and embedding examples
- A Google API key for the Gemini example
- A Hugging Face token for the hosted Hugging Face example

The repository includes a `requirements.txt` file with the LangChain,
provider, Transformers, and machine-learning utility packages. The local
embedding examples additionally require `sentence-transformers`, and local
model execution normally requires `torch`; these packages are not currently
listed in `requirements.txt`.

## Installation

Create and activate a virtual environment from the repository root:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the declared dependencies and the local-model dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install torch sentence-transformers
```

Choose the PyTorch installation appropriate for your hardware if you need a
CUDA or other accelerator build. CPU inference works for these demonstrations,
but downloading and running TinyLlama locally can take time and memory.

## Environment variables

The Google and hosted Hugging Face scripts load variables from a local `.env`
file. Create `.env` in the repository root and add the credentials needed for
the providers you want to use:

```dotenv
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

Only add the variables you need. Keep `.env` private: it is ignored by Git and
API keys should never be committed to the repository. Public Hugging Face
models can usually be downloaded without a token, although authentication can
help with access limits.

## Run the examples

Run commands from the repository root after activating the virtual environment.

### Google Gemini

Sends the fixed prompt `What is capital of India` to the configured Gemini
model and prints the response:

```bash
python ChatModels/chatmodel_google.py
```

This requires a working `GOOGLE_API_KEY`, network access, and access to the
model name configured in the script. Model names and provider requirements can
change; update the `model` value in the script if the provider no longer
supports it.

### Local Hugging Face chat model

Downloads TinyLlama on its first run, runs inference locally, and prints the
answer to a fixed capital-of-India question:

```bash
python ChatModels/chatmodel_hf_local.py
```

This does not use a hosted Hugging Face endpoint. Model files are cached by the
Hugging Face libraries and can require significant disk space, RAM, and startup
time.

### Hosted Hugging Face chat model

Sends the same type of prompt to the Hugging Face inference service:

```bash
python ChatModels/chatmodel_huggingface_model.py
```

This requires a valid `HUGGINGFACEHUB_API_TOKEN`, network access, available
inference capacity, and a provider that supports the selected model and task.

### Single-text embedding

Creates and prints the embedding vector for `I love Programming`:

```bash
python EmbeddedModels/embedding_hf_local.py
```

The first run downloads `sentence-transformers/all-MiniLM-L6-v2`.

### Document similarity

Embeds ten short WWE-related documents, compares them with the query
`tell me about Brock Lesnar`, and prints the highest-scoring document and its
cosine-similarity score:

```bash
python EmbeddedModels/document_similarity.py
```

This is an in-memory similarity demonstration. It is not a full vector
database or retrieval-augmented generation application.

### Interactive terminal chatbot

Starts a TinyLlama chat loop. Enter `exit` to stop the program:

```bash
python Langchain_Prompts/chatbot.py
```

Example interaction:

```text
You: What is LangChain?
Bot: ...
You: exit
```

## Local versus hosted models

The two TinyLlama chat examples use different execution modes:

- `chatmodel_hf_local.py` downloads model weights and runs Transformers in the
  local Python process. It can run without a Hugging Face API token.
- `chatmodel_huggingface_model.py` sends requests to a hosted Hugging Face
  inference provider. It requires credentials, network access, and provider
  availability.

The interactive chatbot also runs TinyLlama locally. Its output can vary with
the installed Transformers version, model revision, hardware, and generation
configuration.

## Project structure

```text
Langchain_Models/
├── ChatModels/
│   ├── chatmodel_google.py
│   ├── chatmodel_hf_local.py
│   └── chatmodel_huggingface_model.py
├── EmbeddedModels/
│   ├── document_similarity.py
│   └── embedding_hf_local.py
├── Langchain_Prompts/
│   └── chatbot.py
├── requirements.txt
└── README.md
```

## Troubleshooting

### `ModuleNotFoundError: No module named 'sentence_transformers'`

Install the extra local embedding dependency:

```bash
python -m pip install sentence-transformers
```

### PyTorch or model-loading errors

Install a PyTorch build compatible with your operating system and hardware,
then retry the local example. Also check that there is enough disk space for
the Hugging Face model cache and enough RAM for TinyLlama.

### Hugging Face authentication or endpoint errors

Confirm that `HUGGINGFACEHUB_API_TOKEN` is present in `.env`, that the token is
valid, and that the selected model is available through the configured
inference provider. The local examples and hosted example have different
requirements.

### Google authentication or model errors

Confirm that `GOOGLE_API_KEY` is present and active. If the configured
`gemini-3.6-flash` model is unavailable for your account or region, replace the
model identifier in `ChatModels/chatmodel_google.py` with one supported by your
Google Gemini integration.

## Validation

There is currently no automated test suite or CI configuration. You can still
check Python syntax for all example scripts without making provider calls:

```bash
python -m compileall ChatModels EmbeddedModels Langchain_Prompts
```

For a dependency check, run:

```bash
python -m pip check
```

The example scripts perform real model downloads or API calls when run, so
their output depends on network access, provider availability, model revisions,
and local hardware.

## Notes

- The scripts are intentionally small learning examples and execute their
  work immediately when started.
- The prompts and documents are currently hard-coded in the scripts.
- Dependencies are not pinned, so behavior may change when providers or
  LangChain integrations release new versions.
- OpenAI and Anthropic integrations are listed in `requirements.txt`, but the
  current examples do not use them yet.
