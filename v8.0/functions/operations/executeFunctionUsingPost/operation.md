# POST /functions/{function_name}/actions/execute
**Operation:** `executeFunctionUsingPost` — Execute a function using the POST method
> To execute a standalone function that is exposed as a REST API, using an OAuth access token and the HTTP POST method. OAuth 2.0 must be enabled for the REST API endpoint of the function.

**Parameters:**
- `function_name` (path, string, required): Specify the API name of the standalone function to execute.
- `auth_type` (query, string, required): Specify **oauth** to execute the function with an OAuth access token.
- `arguments` (query, string, optional): Specify the function arguments as a URL-encoded JSON object. Keys are the argument names defined in the function. For example, **{"customer_name":"Example"}**.

**Responses:**

- **200**: Returns the output of the executed function. [application/json]
    > Represents the successful response body, containing the function's return value.
    - `code` (string) **REQ** [enum=['success']] — Represents the status code of the execution.
    - `message` (string) **REQ** — Represents the status message of the execution.
    - `details` (object) **REQ** — Represents the result of the execution.
      - `output` (string) **REQ** — Represents the value returned by the function.
      - `output_type` (string) **REQ** — Represents the data type of **output**.
      - `id` (string) **REQ** — Represents an identifier returned with the execution result.

- **401**: The access token does not have the required scope. Resolution: Generate a new access token with the **ZohoCRM.functions.execute.CREATE** scope. [application/json]
    oneOf:
        - `code` (string) — The error code identifying the type of error.
        - `message` (string) — A message describing the error.
        - `details` (object) — Error details.
        - `status` (string) — The status of the response (error).

**Scopes:** ZohoCRM.functions.execute.CREATE
