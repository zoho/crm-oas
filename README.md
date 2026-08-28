
# Zoho CRM OpenAPI Specification (OAS) v8.0

Welcome to the **Zoho CRM OpenAPI Specification (OAS) v8.0** repository. This repository provides the OpenAPI Specification files for Zoho CRM APIs, enabling developers to seamlessly integrate Zoho CRM with their applications using standardized API definitions.

---

## **Overview**

The OpenAPI Specification (OAS) is a standardized format for documenting RESTful APIs. It provides details about API structure, endpoints, request/response formats, and authentication methods in JSON or YAML formats. This repository hosts the OAS files for Zoho CRM APIs to help developers:

- Understand Zoho CRM API endpoints and their usage.
- Generate SDKs in various programming languages.
- Integrate Zoho CRM with third-party applications.

---

## **Repository Structure**

The repository is organized into the following sections:

- **`v8.0/`**: Contains the OAS files for version 8.0 of Zoho CRM APIs.
  - Resource-specific folders such as `record/`, `users/`, `modules/`, and more.
  - Each resource folder typically contains:
    - a primary OpenAPI definition file such as `appointments.yaml` or `apis.yaml`
    - an `index.md` overview file
    - an `mds/` directory with operation-specific markdown files
    - an `mds/examples/` directory with example request/response documentation

- **`python/`**: Contains sample Python utilities for working with this repository.
  - `sample_api_runner.py`: A sample Python runner script demonstrating how to use the OAS files to interact with Zoho CRM APIs.

---

## **Getting Started**

### **1. Explore OAS Files**
1. Navigate to the `v8.0/` folder in this repository.
2. Open the resource-specific folder relevant to your use case (for example, `appointments/` or `apis/`).
3. Use the main `*.yaml` file in that folder as the OpenAPI definition, and refer to `index.md` and `mds/` for supporting documentation and examples.
4. Use tools like Swagger's API Hub or Postman to import and explore these files.

### **2. Generate SDKs**
Zoho CRM's OAS files can be used to generate SDKs in various programming languages such as Python, Java, and Node.js.

#### Steps:
1. Import the OAS file into Swagger's API Hub:
   - Go to **Swagger API Hub > Design > Import API**.
   - Paste the raw link of the selected OAS file from this repository.
2. Navigate to **Codegen > Client SDK** in Swagger's API Hub.
3. Select your preferred language (e.g., Python) and download the generated SDK.

---

## **Using the Sample Python Runner**

The repository includes a sample Python runner script (`python/sample_api_runner.py`) that demonstrates how to authenticate and interact with Zoho CRM APIs using the generated Python SDK.

### **Steps to Run the Sample Runner**
1. **Download the Sample Runner**:
   - Download the `sample_api_runner.py` file from `python/` directory in this repository.
   
2. **Set Up Authentication**:
   Zoho CRM APIs use OAuth 2.0 for secure authentication. To authenticate your requests:

     1. Obtain your `Client ID`, `Client Secret`, and `Refresh Token` from Zoho's [Developer Console](https://api-console.zoho.com).
     2. Configure these credentials in your SDK or runner script.

3. **Install Dependencies**:
   - Ensure you have Python installed on your system.
   - Install the Python packages required by the sample runner:
     ```bash
     pip install requests python-dotenv
     ```
   - Ensure the generated Python SDK is available in your environment so the `swagger_client` imports used by `python/sample_api_runner.py` can be resolved.

4. **Run the Script**:
   - Execute the script from the repository root in your local environment:
     ```bash
      python python/sample_api_runner.py
     ```

5. **Test API Operations**:
   - The script demonstrates basic operations like creating and fetching records using Zoho CRM APIs.

---


## **Support**

For any questions or assistance, refer to [Zoho CRM API Documentation](https://www.zoho.com/crm/developer/docs/) or contact our support team at [support@zohocrm.com](mailto:support@zohocrm.com) .

--- 

Start building powerful integrations with Zoho CRM today! 🚀