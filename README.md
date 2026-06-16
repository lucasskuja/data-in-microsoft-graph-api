# microsoft-graph-to-object-storage

A compact reference implementation for moving files from Microsoft Graph / OneDrive into cloud object storage.

This repository captures a practical ingestion pattern: authenticate with Microsoft Graph, retrieve a file from OneDrive, and land it in a raw storage layer on Amazon S3 or Google Cloud Storage. It is intentionally small and easy to adapt, making it useful as a starting point for production-oriented data ingestion workflows, internal accelerators, or architecture prototypes.

The current implementation focuses on a direct file transfer flow. It is best used as a reusable foundation that teams can extend with their own orchestration, metadata handling, retry policies, file discovery rules, and deployment conventions.

## What This Repository Covers

- Microsoft Graph authentication using MSAL and client credentials
- File download from OneDrive through the Microsoft Graph API
- File landing to Amazon S3 or Google Cloud Storage
- Environment-based configuration for credentials and target storage

## Current Scope

Included today:

- A single Python entry point for Graph-to-storage transfer
- Support for one file path per execution
- Storage targets for S3 and GCS
- Basic automated tests around token acquisition and file download behavior

Not included yet:

- Scheduling or orchestration
- Recursive file discovery or folder synchronization
- Incremental loading or state tracking
- Structured logging, retries, or error classification
- Packaging as a reusable Python module or CLI
- Infrastructure-as-code or deployment automation

## Architecture Overview

The current flow is intentionally straightforward:

1. Acquire an application token from Microsoft Entra ID through MSAL.
2. Request a file from OneDrive through the Microsoft Graph content endpoint.
3. Upload the file bytes to the selected object storage target.

```text
Microsoft Entra ID
        |
        v
 Microsoft Graph / OneDrive
        |
        v
 Python transfer script
        |
        +--> Amazon S3
        |
        +--> Google Cloud Storage
```

## Repository Structure

```text
.
|-- src/
|   `-- main.py
|-- tests/
|   |-- __init__.py
|   `-- test_main.py
|-- .env.example
|-- CONTRIBUTING.md
|-- LICENSE
|-- Makefile
|-- README.md
`-- requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and provide the required values for your environment.

Microsoft Graph:

- `CLIENT_ID`
- `CLIENT_SECRET`
- `TENANT_ID`
- `USER_ID`

Amazon S3:

- `AWS_ACCESS_KEY`
- `AWS_SECRET_KEY`
- `S3_BUCKET`

Google Cloud Storage:

- `GCS_BUCKET`
- `GCS_CREDENTIALS_PATH`

## How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

or:

```bash
make install
```

Run the current entry point:

```bash
python src/main.py
```

or:

```bash
make run
```

The example in `src/main.py` is configured with a fixed file path and target selection. For real usage, adapt the input parameters and environment variables to your project conventions.

## How To Adapt

This repository is most useful when treated as a small integration baseline. Common extension points include:

- replacing the hard-coded example inputs with runtime parameters
- adding file selection or folder traversal logic
- introducing retry, logging, and error handling standards
- wrapping the flow in an orchestrator such as Airflow, Dagster, or a scheduler
- standardizing object naming, partitioning, and metadata conventions for your raw layer

## Testing

Run the current test suite with:

```bash
pytest tests/
```

or:

```bash
make test
```

The existing tests validate core integration behavior at a basic level and should be expanded as the implementation grows.

## Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines aligned with the reference-implementation goal of this repository.

## License

This project is available under the terms of the [LICENSE](LICENSE).
