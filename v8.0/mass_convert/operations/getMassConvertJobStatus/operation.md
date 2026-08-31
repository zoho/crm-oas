# GET /Leads/actions/mass_convert
**Operation:** `getMassConvertJobStatus` — Get mass convert job status
> To retrieve the current status and conversion counts of a previously scheduled mass convert job in your Zoho CRM organization.

**Parameters:**
- `job_id` (query, string, required) [maxLen=255]: Specify the identifier of the mass convert job to retrieve the status for. You can get the Job ID from the response of the [Mass Convert API](mass_convert.yaml#$.paths./Leads/actions/mass_convert.get).

**Responses:**

- **200**: Returns the current status and conversion counts for the specified mass convert job. [application/json]
    > Represents the successful response for a mass convert job status request, containing a data array of job status entries.
    - `data` (array of object) [maxItems=5] **REQ** — Represents the list of job status objects for the scheduled mass convert job. 
      - `Status` (string) **REQ** [maxLen=50] — Indicates the current processing status of the mass convert job.
Possible values:
**completed** - The job finished processing all scheduled leads.
**scheduled** - The job is queued for execution.
**in progress** - The job is currently running.
**failed** - The job did not complete.

      - `Total_Count` (integer/int32) **REQ** — Represents the total number of leads scheduled for conversion in the job. 
      - `Converted_Count` (integer/int32) **REQ** — Represents the number of leads that were successfully converted in the job. 
      - `Not_Converted_Count` (integer/int32) **REQ** — Represents the number of leads that have not yet been converted. 
      - `Failed_Count` (integer/int32) **REQ** — Represents the number of leads for which conversion failed. 

- **400**: The request is invalid due to a missing or invalid **job_id** parameter.
*Resolution:** A valid **job_id** must be included in the request as a query parameter.
 [application/json]
    > Represents a validation error response returned when the job status request fails due to missing or invalid parameters.
    - `code` (string) **REQ** [maxLen=100, enum=['REQUIRED_PARAM_MISSING', 'INVALID_DATA']] — Represents the error code identifying the type of validation failure.
Possible values:
**REQUIRED_PARAM_MISSING** - A required parameter is missing from the request.
**INVALID_DATA** - The provided parameter value is invalid.

    - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the validation failure. 
    - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status category of the response.
Possible values:
**error** - The request encountered a validation error.

    - `details` (object) **REQ** — Represents additional details about the error, such as the name of the missing or invalid parameter. 

- **403**: Permission denied to retrieve the mass convert job status.
**Resolution:** The CRM administrator must grant the required permission to the user's profile.
 [application/json]
    > Represents a permission error response returned when the requesting user lacks permission to retrieve the mass convert job status.
    - `code` (string) **REQ** [maxLen=100, enum=['NO_PERMISSION']] — Represents the error code indicating a permission failure.
Possible values:
**NO_PERMISSION** - The user does not have permission to perform this action.

    - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the permission failure. 
    - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status category of the response.
Possible values:
**error** - The request was denied due to insufficient permissions.

    - `details` (object) **REQ** — Represents additional details about the permission error. 

**Scopes:** ZohoCRM.mass_convert.leads.READ
