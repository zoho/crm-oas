# POST /settings/tags/actions/mass_delete
**Operation:** `massDeleteTags` — Mass delete tags
> To schedule a background job that deletes multiple tags in bulk from a single module in your Zoho CRM organization. You can delete tags in bulk from one module per API call. The response returns a job identifier that can be used with the Mass Delete Tags Status GET operation to track the progress of the deletion.

**Schemas:**
`MassDeleteTagsErrorResponse`:
  oneOf:
      - `code` (string) **REQ** [maxLen=30, enum=['MANDATORY_NOT_FOUND']] — Represents the error code indicating that a required field is missing from the request.
      - `status` (string) **REQ** [maxLen=10, enum=['error']] — Represents the status of the error response.
      - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the missing required field.
      - `details` (object) **REQ** — Represents the details that identify the missing required field.
        - `api_name` (string) [maxLen=50] — Represents the API name of the missing required field.
        - `json_path` (string) [maxLen=200] — Represents the JSON path that points to the missing required field in the request body.
      - `code` (string) **REQ** [maxLen=20, enum=['INVALID_DATA']] — Represents the error code indicating that invalid data was provided in the request.
      - `status` (string) **REQ** [maxLen=10, enum=['error']] — Represents the status of the error response.
      - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the invalid data in the request.
      - `details` (object) **REQ** — Represents the details that identify the invalid field and the validation that failed.
        - `api_name` (string) [maxLen=50] — Represents the API name of the field that contains invalid data.
        - `json_path` (string) [maxLen=200] — Represents the JSON path that points to the field with invalid data in the request body.
        - `expected_data_type` (string) [maxLen=50] — Represents the expected data type of the field.
        - `maximum_length` (integer/int32) [min=0] — Represents the maximum allowed number of items or characters for the field that failed validation.
      - `code` (string) **REQ** [maxLen=40, enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code indicating that the module ID and the module API name in the request refer to different modules.
      - `status` (string) **REQ** [maxLen=10, enum=['error']] — Represents the status of the error response.
      - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the ambiguous module identifiers in the request.
      - `details` (object) **REQ** — Represents the details that identify the conflicting module identifiers in the request.
        - `ambiguity_due_to` (array of object) [maxItems=10] **REQ** — Represents the list of conflicting field identifiers that produced the ambiguity in the module reference.
          - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the conflicting field.
          - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path of the conflicting field in the request body.
      - `code` (string) **REQ** [maxLen=20, enum=['NOT_ALLOWED']] — Represents the error code indicating that one or more tags cannot be deleted because they are associated with CRM features.
      - `status` (string) **REQ** [maxLen=10, enum=['error']] — Represents the status of the error response.
      - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the restriction preventing the deletion of the tags.
      - `details` (object) **REQ** — Represents the details that identify the tag whose association blocks the deletion.
        - `api_name` (string) [maxLen=50] — Represents the API name of the field related to the restricted deletion attempt.
        - `json_path` (string) [maxLen=200] — Represents the JSON path that points to the tag identifier whose association blocks the deletion.
      - `code` (string) **REQ** [maxLen=20, enum=['NO_PERMISSION']] — Represents the error code indicating that the user does not have permission to perform the action.
      - `status` (string) **REQ** [maxLen=10, enum=['error']] — Represents the status of the error response.
      - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the permission denial.
      - `details` (object) **REQ** — Represents the details that identify the permissions missing from the user profile.
        - `permissions` (array of string) [maxItems=10] — Represents the list of permission identifiers that the user profile is missing.
          items: [maxLen=100]
      - `mass_delete` (array of object) [maxItems=1] **REQ** — Represents the wrapper array that carries the error for the queried mass delete tag job.
        - `code` (string) **REQ** [maxLen=20, enum=['INVALID_DATA']] — Represents the error code indicating that the provided job_id is invalid.
        - `status` (string) **REQ** [maxLen=10, enum=['error']] — Represents the status of the error response.
        - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the invalid job query.
        - `details` (object) **REQ** — Represents the details that identify the invalid job_id value provided in the request.
          - `job_id` (string) [maxLen=50] — Represents the invalid or unknown job_id value that was provided in the query parameter.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation. 
  > Represents the request payload for scheduling a mass delete tag job, containing the target module and the tags to delete.
  - `mass_delete` (array of object) [maxItems=100] **REQ** — Specify the list of mass delete tag jobs. Each entry identifies the module and the tags to delete in that module within a single job.
    - `module` (object) **REQ** — Specify the module from which the tags must be deleted, identified by its unique ID and API name.
      - `api_name` (string) **REQ** [maxLen=50] — Specify the API name of the module from which the tags must be deleted.
      - `id` (string) **REQ** [maxLen=50] — Specify the unique ID of the module from which the tags must be deleted. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the valid values. 
    - `tags` (array of object) [maxItems=100] **REQ** — Specify the tags to delete from the module. Each entry identifies a single tag by its unique ID. Use the [Get Tags API](tags.yaml#$./settings/tags.get) to get the valid ID. 
      - `id` (string) **REQ** [maxLen=255] — Specify the unique ID of the tag to delete.
      - `name` (string) [maxLen=50] — Specify the name of the tag to delete.

**Responses:**

- **202**: Returns the job identifier and the schedule code for the mass delete tag job that was queued for processing. [application/json]
    > Represents the response payload returned when a mass delete tag job is scheduled successfully, including the job identifier and the schedule code.
    - `status` (string) **REQ** [maxLen=20] — Represents the status of the API call. For a scheduled job, the value is success.
    - `code` (string) **REQ** [maxLen=10] — Represents the code that identifies the result of scheduling the mass delete tag job. For a successful schedule, the value is SCHEDULED.
    - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the outcome of scheduling the mass delete tag job.
    - `details` (object) **REQ** — Represents the details of the scheduled mass delete tag job, including the job identifier returned by the system.
      - `job_id` (string) **REQ** [maxLen=50] — Represents the unique identifier assigned to the scheduled mass delete tag job. Use this value with the [Mass Delete Tags Status](mass_delete_tags.yaml#$.paths./settings/tags/actions/mass_delete.get) API call to know the job state.

- **400**: The request payload is missing required fields, references unknown
or restricted tags, or violates the structural constraints of the
mass delete tag operation. 

Resolution: The request payload must include the mass_delete array,
the module, and a valid tags array that references existing tags not
currently associated with CRM features.
 — Schema: `MassDeleteTagsErrorResponse` [application/json]
    > Represents the error payload returned by the mass delete tag operations. It provides the error structures for missing mandatory fields, invalid data, ambiguous module identifiers, restricted tag deletion, missing permissions, and invalid job queries.

- **401**: The OAuth access token does not include the scope required to
schedule a mass delete tag job. 

Resolution: A new access token must be generated with the
ZohoCRM.settings.tags.DELETE scope.
 [application/json]
    > Represents the error payload returned when the request cannot be authenticated because the OAuth access token does not include the required scope.
    oneOf:
        - `code` (string) **REQ** [maxLen=30, enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code that identifies the OAuth scope mismatch.
        - `status` (string) **REQ** [maxLen=10, enum=['error']] — Represents the status of the API call when the OAuth scope mismatch occurs.
        - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the OAuth scope mismatch.
        - `details` (object) **REQ** — Represents the details of the OAuth scope mismatch, including the request method and the URL that was called.
          - `method` (string) [maxLen=10] — Represents the HTTP method of the request that triggered the OAuth scope mismatch.
          - `url` (string) [maxLen=200] — Represents the request URL that was called when the OAuth scope mismatch occurred.

- **403**: The user does not have enough permission to delete tags from the
specified module. 

Resolution: The CRM administrator must grant the required tag
management permission to the user profile.
 — Schema: `MassDeleteTagsErrorResponse` [application/json]
    > Represents the error payload returned by the mass delete tag operations. It provides the error structures for missing mandatory fields, invalid data, ambiguous module identifiers, restricted tag deletion, missing permissions, and invalid job queries.

**Scopes:** ZohoCRM.settings.tags.DELETE
