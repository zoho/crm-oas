# GET /users/actions/transfer
**Operation:** `getTransferAPIStatus` — Get user transfer status
> Retrieves the current status of a user transfer operation using the job ID returned by the transfer request. The response indicates whether the transfer job is scheduled, in progress, completed, or failed.

**Parameters:**
- `job_id` (query, string/int64, required): Indicates the ID of the job scheduled previously through the [Transfer Records and Delete User API](users_transfer.yaml#$.paths./users/{userId}/actions/transfer_and_delete.post).

**Responses:**

- **200**: The transfer status was retrieved successfully. [application/json]
    > Represents the response body for the transfer status request, containing the current status of the scheduled transfer job.
    - `transfer` (array of object) [maxItems=1] **REQ** — Represents the list of transfer operation status details. The array contains a maximum of one object.
      - `status` (string) [enum=['in_progress', 'completed', 'failed', 'scheduled']] — Represents the current status of the transfer
operation. 


**Possible values**: 

- in_progress

- completed

- failed

- scheduled

      - `reason` (string) [maxLen=500] — Represents the failure reason of the job when `status` is `failed`. Not always present.

- **204**: Shows the response when no transfer job was found for the provided job ID.

- **400**: The request failed due to an invalid or missing required parameter. [application/json]
    > Represents the error response returned when a required parameter is missing from the request.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
    - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the failed request. 
    - `message` (string) **REQ** [enum=['mandatory param missing']] — Represents the error message describing the missing parameter. 
    - `details` (object) **REQ** — Represents additional details about the error, including the name of the missing parameter.
      - `param_name` (string) **REQ** [enum=['job_id']] — Represents the name of the missing required parameter. 

**Scopes:** ZohoCRM.change_owner.READ
