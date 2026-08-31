# POST /Leads/actions/mass_convert
**Operation:** `massConvert` — Submit mass convert job for leads
> To submit a mass convert job that converts lead records into Contacts, Accounts, or Deals in your Zoho CRM organization. The job runs asynchronously and returns a job identifier for status tracking.

**Request Body** (required) — application/json
> The request body must contain the conversion parameters, including the required **ids** array of lead record IDs and optional conversion configuration fields.
  > Represents the request payload for a mass convert operation, containing the lead IDs to convert and optional configuration fields.
  - `ids` (array of string) [maxItems=50] **REQ** — The record IDs of the leads you want to convert. Use the [Get Records API](record.yaml#$.paths./{module}.get) to get the record IDs. Note that you can give a maximum of up to 50 records IDs in this array.
    items: [maxLen=255]
  - `Deals` (object) — Must contain the mandatory keys "Deal_Name", "Stage", "Closing_Date", and "Pipeline"(if enabled), besides the other mandatory fields configured for the Deals module. Note that if there are layouts other than Standard, the custom-defined mandatory fields will not be processed while converting the lead.
    - `Deal_Name` (string) **REQ** [maxLen=255] — Specify the name of the deal to create for the converted lead.
  - `assign_to` (object) — Specify the user to assign the converted records to. Refer to the [Get Users](users.yaml#$.paths./users.get) resource for valid values.
    - `id` (string) **REQ** [maxLen=255] — Specify the ID of the user to assign the converted records to. Refer to the [Get Users](users.yaml#$.paths./users.get) resource for valid values.
  - `portal_user_type` (object) — Specify the portal user type for the contact created from the converted lead. Refer to the [Get Portal User Types](portal_user_type.yaml#$.paths./settings/portals/{portal}/user_type/users.get) resource for valid values.
    - `id` (string/int64) **REQ** [maxLen=255] — Specify the ID of the portal user type to assign to the converted contact. Refer to the [Get Portal User Types](portal_user_type.yaml#$.paths./settings/portals/{portal}/user_type/users.get) resource for valid values.
  - `related_modules` (array of object) [maxItems=3] — The API name and ID of the modules such as Tasks, Meetings, or Calls. If the lead has one or all of these related records, the owner of these records will be changed to the user given in the "assign_to" key.
Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the ID of the module.
    - `api_name` (string) **REQ** [maxLen=100] — Specify the API name of the related module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for API name.
    - `id` (string/int64) **REQ** [maxLen=255] — Specify the ID of the related module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for ID.
  - `carry_over_tags` (array of object) [maxItems=3] — The name and ID of the module you want to associate the tags to while converting the lead. For example, if you give contacts in this array, the tags of the lead will be carried over to the contact that the lead is converted to. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the ID of the module. Note that you can carry over tags to Contacts, Deals, and Accounts.
    - `api_name` (string) **REQ** [maxLen=100] — Specify the API name of the module to carry the tags over to. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
    - `id` (string/int64) **REQ** [maxLen=255] — Specify the ID of the module to carry the tags over to. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
  - `move_attachments_to` (object) — The name and ID of the module you want to move the attachments of the lead to after converting. Use the Modules API to get the ID of the module. Note that you can move the attachments to either Contacts, Deals, or Accounts.
    - `api_name` (string) **REQ** [maxLen=100] — Specify the API name of the module to move the lead's attachments to. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
    - `id` (string/int64) **REQ** [maxLen=255] — Specify the ID of the target module to move the lead's attachments to.
  - `apply_assignment_threshold` (boolean) — Specify whether assignment threshold rules should be applied when assigning the converted records.
Possible values:
**true** - Apply assignment threshold rules (default).
**false** - Skip assignment threshold rules.


**Responses:**

- **202**: Returns confirmation that the mass convert job has been scheduled, along with a job identifier for status tracking. [application/json]
    > Represents the response returned when the mass convert job is successfully scheduled.
    - `code` (string) **REQ** [maxLen=50, enum=['SCHEDULED']] — Represents the response code indicating the job has been scheduled.
Possible values:
**SCHEDULED** - The mass convert job has been accepted and scheduled for execution.

    - `message` (string) **REQ** [maxLen=512] — Represents the message describing the outcome of the mass convert job scheduling. 
    - `status` (string) **REQ** [maxLen=50, enum=['success']] — Represents the status category of the response.
Possible values:
*success** - The mass convert job was scheduled successfully.

    - `details` (object) **REQ** — Represents additional details about the scheduled mass convert job, including the job identifier. 
      - `job_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the scheduled mass convert job, returned for use in subsequent job status requests.

- **400**: The request failed validation due to missing required fields, invalid data, or exceeded limits.
**Resolution:** The request body must include the required fields with valid values and must not exceed the documented limits.
 [application/json]
    > Represents the possible validation error responses for the mass convert operation.
    oneOf:
        - `code` (string) **REQ** [maxLen=100, enum=[8 values]] — Represents the error code identifying the type of validation failure.
Possible values:
**INVALID_REQUEST_METHOD** - The HTTP method used is not allowed for this endpoint.
**INVALID_DATA** - The provided data is invalid.
**REQUIRED_PARAM_MISSING** - A required parameter is missing.
**NOT_ALLOWED** - The requested operation is not permitted.
**MANDATORY_NOT_FOUND** - A mandatory field is missing from the request.
**LIMIT_EXCEEDED** - The request exceeds the allowed limit.
**EXPECTED_FIELD_MISSING** - An expected field is absent from the request.
**AMBIGUITY_DURING_PROCESSING** - The request contains conflicting or ambiguous data.

        - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the validation failure. 
        - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status category of the response.
Possible values:
**error** - The request encountered a validation error.

        - `details` (object) **REQ** — Represents additional details about the validation error, such as field names, JSON paths, expected data types, and limit values. 

- **403**: Permission denied to perform the mass conversion.
**Resolution:** The CRM administrator must grant the required permission to the user's profile.
 [application/json]
    > Represents a permission error response returned when the requesting user lacks permission to perform the mass conversion.
    - `code` (string) **REQ** [maxLen=100, enum=['NO_PERMISSION']] — Represents the error code indicating a permission failure.
Possible values:
**NO_PERMISSION** - The user does not have permission to perform this action.

    - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the permission failure. 
    - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status category of the response.
Possible values:
**error** - The request was denied due to insufficient permissions.

    - `details` (object) **REQ** — Represents additional details about the permission error. 

- **500**: The server encountered an unexpected error while processing the mass convert request.
**Resolution:** The request can be retried. If the error persists, the issue must be investigated on the server side.
 [application/json]
    > Represents a server error response returned when an unexpected error occurs during the mass convert operation.
    - `code` (string) **REQ** [maxLen=100, enum=['INTERNAL_ERROR']] — Represents the error code indicating a server-side failure.
Possible values:
**INTERNAL_ERROR** - The server encountered an unexpected error.

    - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the server failure. 
    - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status category of the response.
Possible values:
**error** - The request failed due to a server error.

    - `details` (object) **REQ** — Represents additional details about the server error, if available. 

**Scopes:** ZohoCRM.mass_convert.leads.CREATE
