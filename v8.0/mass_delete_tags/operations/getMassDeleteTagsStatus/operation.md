# GET /settings/tags/actions/mass_delete
**Operation:** `getMassDeleteTagsStatus` — Mass Delete Tags Status
> To retrieve the current status, the scheduled time, and the success and failure counts for a previously scheduled mass delete tag job in your Zoho CRM organization, using the job ID returned by the Mass Delete Tags POST operation.

**Parameters:**
- `job_id` (query, string/int64, required) [maxLen=19]: Specify the unique identifier of the mass delete tag job for which you want to retrieve the status. Use the job ID returned by the [Mass Delete Tags API](mass_delete_tags.yaml#$.paths./settings/tags/actions/mass_delete.post).

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

**Responses:**

- **200**: Returns the current status and tag deletion counts for the requested mass delete tag job. [application/json]
    > Represents the status payload returned for the queried mass delete tag job, including the job identifier, current execution state, scheduled time, and counts of total, deleted, and failed tags.
    - `mass_delete` (array of object) [maxItems=100] **REQ** — Represents the list of mass delete tag jobs returned for the queried job ID, with one entry per job.
      - `job_id` (string) **REQ** [maxLen=50] — Represents the unique identifier of the mass delete tag job scheduled through the [Mass Delete Tags API](mass_delete_tags.yaml#$.paths./settings/tags/actions/mass_delete.post).
      - `status` (string) **REQ** [maxLen=20] — Represents the current execution state of the mass
delete tag job.

Possible values:

COMPLETED - The job has finished processing all
tags.

SCHEDULED - The job is queued and waiting to begin
processing.

FAILED - The job ended without completing the
deletion.

      - `created_time` (string/date-time) — Represents the timestamp at which the mass delete tag job was scheduled, in ISO 8601 format.
      - `total_count` (integer/int32) [min=0] — Represents the total number of tags that were submitted for deletion in the mass delete tag job.
      - `failed_count` (integer/int32) [min=0] — Represents the number of tags that the job failed to delete.
      - `deleted_count` (integer/int32) [min=0] — Represents the number of tags that the job has deleted successfully.

- **400**: The job ID provided in the request is invalid or does not match any scheduled mass delete tag job. 
Resolution: The job ID must be a valid identifier returned by the [Mass Delete Tags API](mass_delete_tags.yaml#$.paths./settings/tags/actions/mass_delete.post) call.
 — Schema: `MassDeleteTagsErrorResponse` [application/json]
    > Represents the error payload returned by the mass delete tag operations. It provides the error structures for missing mandatory fields, invalid data, ambiguous module identifiers, restricted tag deletion, missing permissions, and invalid job queries.

- **401**: The OAuth access token does not include the scope required to
retrieve the mass delete tag job status. 

Resolution: A new access token must be generated with the
ZohoCRM.settings.tags.READ scope.
 [application/json]
    > Represents the error payload returned when the request cannot be authenticated because the OAuth access token does not include the required scope.
    oneOf:
        - `code` (string) **REQ** [maxLen=30, enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code that identifies the OAuth scope mismatch.
        - `status` (string) **REQ** [maxLen=10, enum=['error']] — Represents the status of the API call when the OAuth scope mismatch occurs.
        - `message` (string) **REQ** [maxLen=200] — Represents the message that describes the OAuth scope mismatch.
        - `details` (object) **REQ** — Represents the details of the OAuth scope mismatch, including the request method and the URL that was called.
          - `method` (string) [maxLen=10] — Represents the HTTP method of the request that triggered the OAuth scope mismatch.
          - `url` (string) [maxLen=200] — Represents the request URL that was called when the OAuth scope mismatch occurred.

- **403**: The user does not have permission to view the status of a mass delete tag job. Resolution: The CRM administrator must grant the required tag management permission to the user profile.
 — Schema: `MassDeleteTagsErrorResponse` [application/json]
    > Represents the error payload returned by the mass delete tag operations. It provides the error structures for missing mandatory fields, invalid data, ambiguous module identifiers, restricted tag deletion, missing permissions, and invalid job queries.

**Scopes:** ZohoCRM.settings.tags.READ
