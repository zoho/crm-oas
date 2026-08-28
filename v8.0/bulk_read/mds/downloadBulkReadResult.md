# GET /read/{jobId}/result
**Operation:** `downloadBulkReadResult` — Download bulk read result
> To download the exported records from a completed bulk read job in Zoho CRM. This API returns a ZIP archive containing the CSV or ICS file with the exported records. The bulk read job must have a COMPLETED state before you can download the result.

**Parameters:**
- `jobId` (path, string, required) [maxLen=100]: Specify the unique identifier of the bulk read job.

**Responses:**

- **200**: The bulk read result file was successfully downloaded as a ZIP archive. [application/zip]
    > Represents the ZIP archive containing the exported bulk read records.
    type: string/binary — Represents the ZIP archive containing the exported bulk read records.

- **404**: The specified bulk read job or its result was not found. [application/json]
    > Represents the error response returned when the specified bulk read job result does not exist.
    - `code` (string) **REQ** [enum=['RESOURCE_NOT_FOUND']] — Represents the error code indicating that the bulk read job result was not found. 
Possible values:
**RESOURCE_NOT_FOUND** - The bulk read job with the specified ID does not exist or the result is not yet available.
    - `details` (object) **REQ** — Represents additional details about the resource not found error. 
      - `resource` (string) **REQ** [maxLen=500] — Represents the type of resource that was not found. 
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the resource not found issue. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
Possible values:
**error** - Indicates that the request failed.

**Scopes:** ZohoCRM.bulk.READ, ZohoCRM.modules.ALL
