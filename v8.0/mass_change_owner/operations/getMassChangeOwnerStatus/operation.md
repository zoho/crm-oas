# GET /{module}/actions/mass_change_owner
**Operation:** `getMassChangeOwnerStatus` — Get mass change owner job status
> To retrieve the status of a previously scheduled mass change owner job in your Zoho CRM organization. The OAuth scope enforced is specific to the target module (for example, **ZohoCRM.change_owner.leads.READ** for Leads); modules without a dedicated scope fall back to a generic custom-module scope.

**Parameters:**
- `module` (path, string, required) [maxLen=255]: Specify the API name of the CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values. **Deals** and **Meetings** are normalized internally to **Potentials** and **Events** respectively before the job's module is checked.
- `job_id` (query, string, required) [maxLen=19]: Specify the unique ID of the mass change owner job returned in the response of [Mass Change Owner API](mass_change_owner.yaml#$.paths./{module}/actions/mass_change_owner.post).

**Responses:**

- **200**: Returns the status details of the mass change owner job identified by the specified job ID. [application/json]
    > Contains the job status data returned for a successful retrieval request.
    - `data` (array of object) [maxItems=1] **REQ** — Contains the job status details for the mass change owner job.
      - `Status` (string) **REQ** [enum=['COMPLETED', 'SCHEDULED', 'FAILED']] — Represents the current status of the mass change
owner job.

Possible values:

**COMPLETED** - The job is finished successfully.

**SCHEDULED** - The job is queued and has not
started processing yet.

**FAILED** - The job did not complete successfully.

      - `Failed_Count` (integer/int32) **REQ** — Represents the number of records for which the ownership change operation failed. 
      - `Not_Updated_Count` (integer/int32) **REQ** — Represents the number of records for which the ownership has not yet been updated. 
      - `Updated_Count` (integer/int32) **REQ** — Represents the number of records for which the ownership was successfully updated. 
      - `Total_Count` (integer/int32) **REQ** — Represents the total number of records that were processed by the mass change owner job.

- **204**: Returned when the specified job ID does not correspond to any mass change owner job, whether currently scheduled or aged out of the live job store (jobs older than 60 days are looked up from the audit log). Despite the 204 status, the response carries a JSON error body. [application/json]
    > Represents the error response returned when no job data could be found for the specified job ID.
    - `code` (string) **REQ** [enum=['NO_DATA']] — Represents the error code for the response.

Possible values:

**NO_DATA** - No job data was found for the specified
job ID.

    - `message` (string) **REQ** [maxLen=255] — Represents the message describing the absence of job data.

- **400**: The **job_id** query parameter is missing from the request. 
Resolution: The request must include a valid **job_id** obtained from the response of the previous [Mass Change Owner API](mass_change_owner.yaml#$.paths./{module}/actions/mass_change_owner.post) call.
 [application/json]
    > Represents the error response returned when the **job_id** query parameter is missing from the request.
    - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the failed request.

Possible values:

**REQUIRED_PARAM_MISSING** - A required query parameter is
missing.

    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the issue. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

    - `details` (object) **REQ** — Represents the additional error details about the missing parameter. 
      - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the missing required query parameter. 

- **404**: Returned when the specified job ID corresponds to a mass change owner job that was scheduled for a different module than the one specified in the **module** path parameter. This module check is only performed while the job is still tracked by the live job scheduler; once a job ages out of the live store (see the 60-day retention note above), a module mismatch on an older job instead returns **204** with the **NO_DATA** body, not this 404. [application/json]
    > Represents the error response returned when the job ID belongs to a mass change owner job scheduled for a different module than the one specified in the request.
    - `code` (string) [maxLen=255, nullable] — Represents the error code for the failed request. May be absent when the underlying exception does not populate an error code.
    - `message` (string) [maxLen=255, nullable] — Represents the error message describing the module mismatch. May be absent when the underlying exception does not populate an error message.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

    - `details` (object) — Represents the additional error details, if any.

**Scopes:** ZohoCRM.change_owner.READ
