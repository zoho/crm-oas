# POST /users/actions/transfer_and_delete
**Operation:** `userTransferWithoutId` — Transfer and delete a user
> Transfer user records, assignments, and criteria to another user

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation.
  > Request body for transferring and deleting user data
  - `transfer_and_delete` (array of object) [maxItems=1] **REQ** — Specify the list of user transfer and delete operations to perform. The array accepts a maximum of one entry.
    - `id` (string) **REQ** [maxLen=19] — Specify the unique identifier of the user whose data is to be transferred and who is to be deleted.
    - `move_subordinate` (object) **REQ** — Provides the details of the user to whom subordinates will be moved.
      - `id` (string) **REQ** [maxLen=19] — Specify the unique identifier of the user to whom the subordinates of the deleted user are moved. Use the [Get Users API](users.yaml#$.paths./users.get) API to get the valid values.
    - `transfer` (object) **REQ** — Provides the transfer settings for records, assignments, and criteria.
      - `records` (boolean) — Specify whether to transfer the records of the deleted user to the target user.
      - `assignment` (boolean) — Specify whether to transfer the assignments of the deleted user to the target user.
      - `criteria` (boolean) — Specify whether to transfer the criteria of the deleted user to the target user.
      - `id` (string) **REQ** [maxLen=19] — Specify the unique identifier of the user to whom the data of the deleted user is transferred. Use the [Get Users API](users.yaml#$.paths./users.get) API to get the valid values.

**Responses:**

- **200**: Shows the success response of user transfer and delete operation is scheduled. [application/json]
    > Provides the response body for successful user transfer and delete operation.
    - `transfer_and_delete` (array of object) [maxItems=1] **REQ** — Represents an array containing transfer and delete operation results.
      - `status` (string) **REQ** [maxLen=100] — Represents the status of the transfer and delete operation.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the rsponse code indicating operation scheduled.
      - `message` (string) **REQ** [maxLen=500] — Represents the message describing the result.
      - `details` (object) **REQ** — Represents the additional details about the scheduled operation.
        - `job_id` (string) **REQ** [maxLen=50] — Represents the unique identifier of the scheduled job created for the transfer and delete operation.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the user involved in the transfer and delete operation.

- **400**: Provides the error response body for an invalid data or missing required fields. [application/json]
    > Represents the error response returned when the transfer and delete operation request contains invalid data, constraint violations, or is missing required fields.
    oneOf:
        - `transfer_and_delete` (array of object) [maxItems=1] **REQ** — Represents the list of errors encountered during the transfer and delete operation.
          oneOf:
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
              - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code for the validation failure. 
              - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation failure.
              - `details` (object) **REQ** — Represents the contextual details of the validation error, varying based on the type of invalid data encountered.
                oneOf:
                    - `id` (string) **REQ** [maxLen=19] — Represents the identifier value that failed validation in the request.
                    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that failed validation.
                    - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the field that failed validation in the request body.
                    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains an incorrect data type.
                    - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the field that contains an incorrect data type.
                    - `expected_data_type` (string) **REQ** [maxLen=50] — Represents the data type that the field expects for a valid request.
                    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field associated with an invalid owner status.
                    - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the field associated with an invalid owner status.
                    - `owner_status` (string) **REQ** [enum=['no_crm_user', 'deleted', 'inactive']] — Represents the current status of the
user that prevents the transfer. 


**Possible values**: 

- no_crm_user

- deleted

- inactive

                    - `index` (integer/int32) **REQ** — Represents the zero-based index of the array element that contains invalid data.
                    - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the array element that contains invalid data.
                    - `expected_data_type` (string) **REQ** [maxLen=50] — Represents the data type that the array element expects for a valid request.
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
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code for the invalid data. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the issue.
        - `details` (object) **REQ** — Represents the details about the data constraint violation, including the field that exceeds the maximum allowed length.
          - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that exceeds the maximum allowed length.
          - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the field that exceeds the maximum allowed length.
          - `maximum_length` (integer/int32) **REQ** — Represents the maximum number of elements allowed in the field.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
        - `code` (string) **REQ** [enum=['CONCURRENT_JOB_LIMIT_EXCEEDED']] — Represents the error code returned when the scheduler job limit is reached. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the scheduler limit.
        - `details` (object) **REQ** — Represents the details of the exceeded scheduler limit.
          - `limit` (string) **REQ** [maxLen=10] — Represents the maximum number of transfer and delete jobs that can be scheduled concurrently.

- **403**: Provides the error response for a request where user does not have permission to perform this operation. [application/json]
    > Represents the error response returned when the user does not have the required permissions to perform the transfer and delete operation.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. 
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the user lacks the required permission. 
    - `message` (string) **REQ** [maxLen=500] — Provides the message describing the issue in the request.
    - `details` (object) — Provides the additional details about missing permissions.
      - `permissions` (array of string) [maxItems=1] **REQ** — Provides the list of required permissions that are missing.
        items: [maxLen=200]

**Scopes:** ZohoCRM.users.UPDATE
