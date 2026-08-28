# POST /users/{userId}/actions/transfer
**Operation:** `userTransferAPI` — Transfer a user
> Transfer user records, assignments, and criteria to another user

**Parameters:**
- `userId` (path, string/int64, required) [pattern=^[0-9]+$]: Represents the unique identifier of the user whose data is to be transferred and whose account is to be deleted. Use the [Get Users API](users.yaml#$.paths./users.get) API to get the valid values.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation.
  > Represents the request body to transfer a user's records, assignments, criteria, and subordinates to another user.
  - `transfer` (array of object) [maxItems=1] **REQ** — Specify the list of transfer operations to perform for the user. Only one transfer operation is allowed per request.
    - `move_subordinate` (object) **REQ** — The details of the new user you want to transfer the subordinates of the old user to.
      - `id` (string) **REQ** [maxLen=19] — Specify the unique identifier of the user to whom the subordinates are reassigned. Use the [Get Users API](users.yaml#$.paths./users.get) API to get the valid values.
    - `transfer` (object) **REQ** — The details of the new user you want to transfer the records of the old user to.
      - `records` (boolean) — Specify whether to transfer the records to the target user.
      - `assignment` (boolean) — Specify whether to transfer the record assignments to the target user.
      - `criteria` (boolean) — Specify whether to transfer the criteria-based data to the target user.
      - `id` (string) **REQ** [maxLen=19] — Specify the unique identifier of the user to whom the data is transferred. Use the [Get Users API](users.yaml#$.paths./users.get) API to get the valid values.

**Responses:**

- **200**: Shows the success response of a user transfer operation is scheduled. [application/json]
    > Provides the response body for successful user transfer operation

    - `transfer` (array of object) [maxItems=1] **REQ** — Represents an array containing transfer operation results.
      - `status` (string) **REQ** [maxLen=100] — Represents the status of the transfer operation.
      - `code` (string) **REQ** [enum=['SCHEDULED']] — Represents the response code indicating operation scheduled.

      - `message` (string) **REQ** [maxLen=500] — Represents the message describing the result.
      - `details` (object) **REQ** — Represents the additional details about the scheduled operation.

        - `job_id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the scheduled job created for the transfer operation.

- **400**: Provides the error response for invalid data or missing required fields. [application/json]
    > Represents the error response returned when the transfer request contains invalid data or is missing required fields.
    oneOf:
        - `transfer` (array of object) [maxItems=1] **REQ** — Represents the list of errors encountered during the transfer operation.
          oneOf:
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
              - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code for the validation failure. 
              - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation failure.
              - `details` (object) **REQ** — Represents the additional details about the validation error.
                oneOf:
                    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that failed validation in the transfer request.
                    - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the field that failed validation in the transfer request.
                    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field associated with an invalid owner status.
                    - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the field associated with an invalid owner status.
                    - `owner_status` (string) **REQ** [enum=['not_crm_user', 'deleted', 'inactive']] — Represents the current status of the
user that prevents the transfer. 


**Possible values**: 

- not_crm_user

- deleted

- inactive

              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code when required fields are missing. 
              - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the missing required fields.
              - `details` (object) **REQ** — Represents the details of the missing required fields in the request.
                - `expected_data` (array of object) [maxItems=100] — Represents the list of required fields that are missing from the request body.
                  - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the required field that is missing from the request.
                  - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the required field that is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code when a required nested field is missing. 
              - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the missing required field.
              - `details` (object) **REQ** — Represents the details of the missing required id field.
                - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the missing field.
                - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the missing field.
                - `parent_api_name` (string) **REQ** [enum=['transfer', 'move_subordinate']] — Represents the parent field under which the id field is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code for the invalid user or not allowed error. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the invalid user in the request path.
        - `details` (object) **REQ** — Represents the details about the invalid user in the request path. owner_status is not returned for the NOT_ALLOWED case where the target user is not a subordinate of the caller.
          - `resource_path_index` (integer/int32) **REQ** — Represents the position index of the invalid user ID in the resource path.
          - `owner_status` (string) [enum=['not_crm_user', 'deleted']] — Represents the current status of the user specified in the request path.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
        - `code` (string) **REQ** [enum=['CONCURRENT_JOB_LIMIT_EXCEEDED']] — Represents the error code returned when the scheduler job limit is reached. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the scheduler limit.
        - `details` (object) **REQ** — Represents the details of the exceeded scheduler limit.
          - `limit` (string) **REQ** [maxLen=10] — Represents the maximum number of transfer and delete jobs that can be scheduled concurrently.

- **403**: Provides the error response body where the user does not have permission to perform this operation. [application/json]
    > Represents the error response returned when the user does not have the required permissions to perform the transfer operation.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. 
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the user lacks the required permission. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the permission issue.

    - `details` (object) **REQ** — Represents the additional details about missing permissions.

      - `permissions` (array of string) [maxItems=1] **REQ** — Represents the list of required permissions that are missing.
        items: [maxLen=200]

**Scopes:** ZohoCRM.change_owner.CREATE
