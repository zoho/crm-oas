# GET /{module}/actions/mass_delete
**Operation:** `getMassDeleteJobStatus` — Retrieve mass delete job status
> To retrieve the status and record counts of a previously scheduled mass delete job in your Zoho CRM organization.

**Parameters:**
- `module` (path, string, required) [minLen=1, enum=[20 values]]: Specify the API name of the CRM module for the mass delete operation. Make a [Get Modules API](modules.yaml#$.paths./settings/modules.get) call for valid values.
- `job_id` (query, string/string, required) [pattern=^[0-9]+$]: Specify the job ID returned in the response of the [Mass Delete API](mass_delete.yaml#$.paths./{module}/actions/mass_delete.post).

**Responses:**

- **200**: Returns the current status and record counts of the requested mass delete job. [application/json]
    > Represents the response payload for a successful mass delete job status retrieval.
    - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Contains the mass delete job status details. 
      - `Status` (string) **REQ** [enum=['COMPLETED', 'SCHEDULED', 'QUEUED', 'RUNNING', 'SUSPENDED', 'FAILED']] — Represents the current status of the mass delete
job. 

Possible values:

**COMPLETED** - The job has finished processing all
records.

**SCHEDULED** - The job is scheduled and waiting to
start.

**QUEUED** - The job is in the queue awaiting
processing.

**RUNNING** - The job is currently in progress.

**SUSPENDED** - The job has been paused.

**FAILED** - The job ended with an error and did not
complete.

      - `Total_Count` (integer/int32) **REQ** [min=0] — Represents the total number of records targeted for deletion by the mass delete job. 
      - `Deleted_Count` (integer/int32) **REQ** [min=0] — Represents the number of records successfully deleted by the mass delete job. 
      - `Failed_Count` (integer/int32) **REQ** [min=0] — Represents the number of records that could not be deleted by the mass delete job. 

- **400**: The request is invalid due to a missing or invalid inputs.

**Resolution:** The **job_id** query parameter is mandatory, and the
module API name in the request path must be valid.
 [application/json]
    > Represents the error response payload for an invalid request. Contains one of the possible error scenarios.
    oneOf:
        - `status` (string) **REQ** [const=error] — Represents the status of the error response. 
        - `code` (string) **REQ** [const=MANDATORY_NOT_FOUND] — Represents the error code for the response.
        - `message` (string) **REQ** [const=mandatory param missing] — Represents the error message for the response. 
        - `details` (object) **REQ** — Contains additional details about the error, including the name of the missing parameter. 
          - `param_name` (string) **REQ** [const=job_id] — Represents the name of the missing required query parameter. 
        - `status` (string) **REQ** [const=error] — Represents the status of the error response.
        - `code` (string) **REQ** [const=INVALID_DATA] — Represents the error code for the response.
        - `message` (string) **REQ** [const=The jobid given seems to be invalid] — Represents the error message for the response. 
        - `details` (object) **REQ** — Contains additional details about the error, including the name of the invalid parameter. 
          - `param_name` (string) **REQ** [const=job_id] — Represents the name of the invalid query parameter. 
        - `status` (string) **REQ** [const=error] — Represents the status of the error response.
        - `code` (string) **REQ** [const=INVALID_MODULE] — Represents the error code for the response. 
        - `message` (string) **REQ** [const=the module name given seems to be invalid] — Represents the error message for the response. 
        - `details` (object) **REQ** — Contains additional details about the error, including the index of the invalid path segment. 
          - `resource_path_index` (integer/int32) **REQ** [const=0] — Represents the index of the resource path segment that contains the invalid module name. 
        - `status` (string) **REQ** [const=error] — Represents the status of the error response. 
        - `code` (string) **REQ** [const=UNABLE_TO_PARSE_DATA_TYPE] — Represents the error code for the response. 
        - `message` (string) **REQ** [const=either the request body or parameters is in wrong format] — Represents the error message for the response.
        - `details` (object) **REQ** — Contains additional details about the error. 

**Scopes:** ZohoCRM.mass_delete.READ
