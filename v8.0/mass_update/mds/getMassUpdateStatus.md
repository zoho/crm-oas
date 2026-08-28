# GET /{module}/actions/mass_update
**Operation:** `getMassUpdateStatus` — Get mass update job status
> To retrieve the current status and record-processing counts of an asynchronous mass update job that was previously scheduled in your Zoho CRM organization. The job is identified by the `job_id` returned in the response of the scheduler-type mass update request. The response reports the job state along with the total, updated, not-updated, and failed record counts so that the caller can track progress until the job completes.

**Parameters:**
- `module` (path, string, required) [enum=[18 values]]: Specify the API name of the CRM module on which the mass update operation must be performed. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to fetch the valid API name of the module. 
- `job_id` (query, string/int64, required) [pattern=^[0-9]+$]: Specify the unique ID of the mass update job whose status must be retrieved. This is the `job_id` returned in the response of the [Mass Update API](mass_update.yaml#$/{module}/actions/mass_update.post) request.

**Responses:**

- **200**: Returns the current state and record-processing counts of the requested mass update job. [application/json]
    > The request body contains the data required to perform the operation.
    - `data` (array of object) [maxItems=1] **REQ** — Represents the array that contains the status object for the requested mass update job.
      - `Status` (string) **REQ** [enum=['COMPLETED', 'SCHEDULED', 'QUEUED', 'RUNNING', 'SUSPENDED', 'FAILED']] — Represents the current state of the mass update job.

Possible values:

COMPLETED - The mass update job has finished
processing all records.

SCHEDULED - The mass update job has been queued and
is waiting to start.

QUEUED - The mass update job is queued in the
system.

RUNNING - The mass update job is currently
processing records.

SUSPENDED - The mass update job has been paused.

FAILED - The mass update job has terminated due to a
failure.

      - `Failed_Count` (integer/int32) **REQ** — Represents the number of records that failed to update due to validation errors or other processing failures during the mass update job.
      - `Updated_Count` (integer/int32) **REQ** — Represents the number of records that were successfully updated by the mass update job.
      - `Not_Updated_Count` (integer/int32) **REQ** — Represents the number of records that are not yet updated by the mass update job.
      - `Total_Count` (integer/int32) **REQ** — Represents the total number of records that were scheduled to be mass updated by the job.

- **400**: Returns an error when the request fails because of a missing or
invalid `job_id` parameter or an unsupported module.

**Resolution**: Use the job ID received in the response of [Mass
Update API](mass_update.yaml#$./{module}/actions/mass_update.post).
 [application/json]
    > Represents the response wrapper for a failed mass update status request, returning one of the validation or module errors that prevented the request from being processed.
    oneOf:
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a required parameter is missing from the request.
        - `details` (object) **REQ** — Represents additional details about the missing mandatory parameter, including the name of the parameter that was not provided.
        - `message` (string/string) **REQ** — Represents the error message describing the validation failure for the missing parameter.
        - `status` (string/string) **REQ** [enum=['error']] — Represents the overall status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the provided parameter value fails validation.
        - `details` (object) **REQ** — Represents additional details about the invalid parameter, including the name of the parameter whose value failed validation.
        - `message` (string/string) **REQ** — Represents the error message describing the invalid parameter value.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned when the module specified in the request URL is invalid or not supported.
        - `message` (string/string) **REQ** — Represents the error message describing the module validation failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall status of the API response.
        - `details` (object) **REQ** — Represents additional details about the invalid module, including the index of the unsupported segment in the request path.

**Scopes:** ZohoCRM.mass_update.READ, ZohoCRM.mass_update.Leads.READ
