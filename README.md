
# Zoho CRM OpenAPI Specification (OAS) v8.0

Welcome to the **Zoho CRM OpenAPI Specification (OAS) v8.0** repository. This repository provides OpenAPI specifications and operation-level documentation for Zoho CRM APIs, enabling developers to understand the APIs, generate SDKs, and build integrations using standardized API definitions.

## Overview

The OpenAPI Specification (OAS) is a standardized format for documenting RESTful APIs. It describes API endpoints, request and response formats, schemas, and authentication requirements. The files in this repository can be used to:

- Understand Zoho CRM API endpoints and their usage.
- Generate SDKs in languages such as Python, Java, and Node.js.
- Integrate Zoho CRM with third-party applications.
- Provide compressed operation documentation and examples to CRM Skills.

## Repository Structure

### `v8.0/`

`v8.0/` contains one folder per resource, for example `appointments/`, `record/`, `users/`, and many others.

Each resource folder contains:

- `<resource>.yaml` - the resource OAS file (for example, `appointments.yaml`).
- `index.md` - resource overview with links to operations.
- `operations/<operation_id>/operation.md` - compressed Markdown for each operation.
- `operations/<operation_id>/examples/*.md` - request/response example Markdown files.

Example:

```text
v8.0/appointments/
   appointments.yaml
   index.md
   operations/
      getAppointmentsS/
         operation.md
         examples/
            response-200-success200.md
            response-400-invalidmoduleresponse1.md
```

### `python/`

- `sample_api_runner.py` - sample runner for testing CRM API operations with a generated Python SDK.

## CRM Skills Integration

[CRM Skills](https://github.com/zoho/crm-skills) uses the OAS files, compressed operation Markdown, and examples from this repository to provide API-specific guidance.

For the skill to work correctly, keep these in sync:

- Resource OAS files (`v8.0/<resource>/<resource>.yaml`).
- Operation compressed Markdown (`v8.0/<resource>/operations/<operation_id>/operation.md`).
- Operation example Markdown files (`v8.0/<resource>/operations/<operation_id>/examples/*.md`).

When an OAS file changes, its operation documentation and examples must also be updated. Otherwise, CRM Skills may return stale or inconsistent API guidance.

## Getting Started

### Explore OAS Files

1. Navigate to `v8.0/`.
2. Select the resource folder relevant to your use case, such as `record/`, `users/`, or `appointments/`.
3. Use the resource YAML file as the OpenAPI definition.
4. Refer to `index.md`, `operations/*/operation.md`, and `operations/*/examples/*.md` for supporting documentation and examples.
5. Import the YAML file into Swagger API Hub or Postman to explore the API.

### Generate SDKs

1. In Swagger API Hub, go to **Design > Import API**.
2. Import the raw URL of the required resource YAML file from this repository.
3. Go to **Codegen > Client SDK**.
4. Select a language and download the generated SDK.

## Using the Sample Python Runner

`python/sample_api_runner.py` demonstrates authenticated Zoho CRM API calls with a generated SDK.

1. Configure OAuth credentials (`Client ID`, `Client Secret`, `Refresh Token`) from the [Zoho Developer Console](https://api-console.zoho.com).
2. Install dependencies:

```bash
pip install requests python-dotenv
```

3. Ensure generated Python SDK modules (for example, `swagger_client`) are available in your environment.
4. Run from repository root:

```bash
python3 python/sample_api_runner.py
```

## Support

For help, see [Zoho CRM API Documentation](https://www.zoho.com/crm/developer/docs/) or contact [support@zohocrm.com](mailto:support@zohocrm.com).