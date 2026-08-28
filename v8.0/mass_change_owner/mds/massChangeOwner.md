# POST /{module}/actions/mass_change_owner
**Operation:** `massChangeOwner` — Submit mass change owner job
> To bulk update the ownership of records in a specified module based on a Custom View, territory, or field-based criteria in your Zoho CRM organization. You cannot change the owner of related records using this API. You can change the owner of up to 50,000 records in a custom view. This API schedules the operation as a job and returns a job ID, which you can use to check the job status. Job statuses are available for up to 60 days. The Mass Change Owner API is available only in the Enterprise and Ultimate editions. The OAuth scope enforced is specific to the target module (for example, **ZohoCRM.change_owner.leads.CREATE** for Leads); modules without a dedicated scope fall back to a generic custom-module scope.

**Parameters:**
- `module` (path, string, required) [maxLen=255]: Specify the API name of the CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation.
  > Specify the details for the mass change owner operation, including the target Custom View, the new owner, an optional territory, and an optional criteria filter.
  - `cvid` (string) **REQ** [maxLen=19] — Specify the unique ID of the Custom View whose records are to be reassigned. Refer to the [Get Custom Views](custom_views.yaml#$.paths./settings/custom_views.get) resource for valid values.
  - `owner` (object) **REQ** — Specify the details of the user to assign as the new owner of the selected records.
    - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the user to assign as the new owner. Refer to the [Get Users](users.yaml#$.paths./users.get) resource for valid values.
  - `territory` (object) — Specify the territory to use as the source of records for the ownership change.
    - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the territory. Refer to the [Get Territories](territories.yaml#$.paths./settings/territories.get) resource for valid values.
    - `include_child` (boolean) [nullable] — Specify whether to include records from child
territories of the specified territory in the ownership
change.

Possible values:

**true** - Include records from child territories.

**false** - Restrict to records in the specified
territory only.

  - `criteria` (object) — Specify the criteria to filter which records are included in the ownership change.
    - `field` (object) **REQ** — Specify the module field on which the criteria condition applies.
      - `api_name` (string) **REQ** [maxLen=255] — Specify the API name of the field. Refer to the [Get Fields](fields.yaml#$.paths./settings/fields.get) resource for valid values.
      - `id` (string) [maxLen=19] — Specify the unique ID of the field. Refer to the [Get Fields](fields.yaml#$.paths./settings/fields.get) resource for valid values.
    - `comparator` (string) **REQ** [enum=[10 values]] — Specify the comparison operator for the criteria.

Possible values:

**equal** - Matches records where the field equals the
specified value.

**not_equal** - Matches records where the field does not
equal the specified value.

**starts_with** - Matches records where the field starts
with the specified value.

**ends_with** - Matches records where the field ends
with the specified value.

**greater_than** - Matches records where the field is
greater than the specified value.

**less_than** - Matches records where the field is less
than the specified value.

**greater_equal** - Matches records where the field is
greater than or equal to the specified value.

**less_equal** - Matches records where the field is less
than or equal to the specified value.

**between** - Matches records where the field value
falls within a specified range.

**not_between** - Matches records where the field value
falls outside a specified range.

    - `value` (string) **REQ** [maxLen=255] — Specify the value to compare against the field using the criteria comparator.

**Responses:**

- **202**: Returns the job details after the mass change owner request is accepted and scheduled for processing. [application/json]
    > Contains the details of the scheduled ownership change job.
    - `data` (array of object) [maxItems=1] **REQ** — Contains the job scheduling details returned when the mass change owner request is accepted.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the mass change owner
operation.

Possible values:

**success** - The mass change owner job was
successfully scheduled.

      - `code` (string) **REQ** [enum=['SCHEDULED']] — Represents the response code for the scheduled job.

Possible values:

**SCHEDULED** - The mass change owner job is
successfully scheduled.

      - `message` (string) **REQ** [enum=['change owner is successfully scheduled']] — Represents the response message for the scheduled job.
      - `details` (object) **REQ** — Represents the additional details about the scheduled mass change owner job. 
        - `job_id` (string) **REQ** [maxLen=19] — Represents the unique ID of the scheduled mass change owner job.

- **400**: The mass change owner request failed due to invalid or missing
input. Resolution: Review the error details in the response to
identify and correct the specific validation issue.
 [application/json]
    > Represents one of the possible error responses returned when the mass change owner request fails due to invalid or missing parameters.
    oneOf:
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the failed request.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing required field.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

        - `details` (object) **REQ** — Represents the additional error details about the missing field.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing required field.
          - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the missing required field in the request body.
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_SUPPORTED']] — Represents the error code for the failed request.

Possible values:

**INVALID_DATA** - The provided data is invalid.

**NOT_SUPPORTED** - The operation is not supported for
this module.

        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid data or unsupported module.
        - `details` (object) **REQ** — Represents the additional error details about the invalid data or unsupported operation.
          oneOf:
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
              - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the invalid field in the request body.
              - `resource_path_index` (integer/int32) **REQ** — Represents the index of the invalid segment in the request URL path.
              - `owner_status` (string) **REQ** [enum=['not_crm_user', 'deleted', 'inactive']] — Represents the status of the specified owner
user.

Possible values:

**not_crm_user** - The specified user is not a
CRM user.

**deleted** - The specified user account is
deleted.

**inactive** - The specified user account is
inactive.

              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field in which the invalid owner ID was provided.
              - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field in which the invalid owner ID was provided.
              - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with the data type mismatch.
              - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field with the data type mismatch.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

        - `code` (string) **REQ** [enum=['RECORD_LIMIT_EXCEEDED']] — Represents the error code for the failed request.

Possible values:

**RECORD_LIMIT_EXCEEDED** - The number of records in
the Custom View exceeds the allowed limit.

        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the record count limit exceeded.
        - `details` (object) **REQ** — Represents the additional error details about the exceeded record limit.
          - `limit` (integer/int32) **REQ** — Represents the maximum number of records allowed per ownership change request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

        - `code` (string) **REQ** [enum=['COMBINED_CRITERIA_LIMIT_EXCEEDED']] — Represents the error code for the failed request.

Possible values:

**COMBINED_CRITERIA_LIMIT_EXCEEDED** - The combined
number of criteria in the Custom View and the request
**criteria** exceeds the allowed limit of 25.

        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the exceeded combined criteria limit.
        - `details` (object) **REQ** — Represents the additional error details about the exceeded combined criteria limit.
          - `limit` (integer/int32) **REQ** — Represents the maximum combined criteria count allowed across the Custom View and the request body.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the failed request.

Possible values:

**NOT_ALLOWED** - The specified owner is a Service
Provider user who can only own records in the Tasks,
Events, Calls, and Appointments modules.

        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the disallowed ownership assignment.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

        - `details` (object) **REQ** — Represents the additional error details about the disallowed owner assignment.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field carrying the disallowed owner.
          - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the disallowed owner field.
        - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code for the failed request.

Possible values:

**EXPECTED_FIELD_MISSING** - A required field is
missing from the criteria object.

        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing criteria fields.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

        - `details` (object) **REQ** — Represents the additional error details about the missing criteria fields.
          - `expected_fields` (array of object) [maxItems=2] **REQ** — Represents the list of expected fields that are missing from the criteria object.
            - `api_name` (string) [maxLen=255] — Represents the API name of the missing expected field.
            - `json_path` (string) [maxLen=255] — Represents the JSON path to the missing expected field.
        - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code for the failed request.

Possible values:

**AMBIGUITY_DURING_PROCESSING** - Both the field ID
and API name were provided, causing ambiguity.

        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the ambiguity in the field specification.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

        - `details` (object) **REQ** — Represents the additional error details about the ambiguous field specification.
          - `ambiguity_due_to` (array of object) [maxItems=2] **REQ** — Represents the list of fields that caused the ambiguity.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused ambiguity.
            - `json_path` (string) [maxLen=255] — Represents the JSON path to the field that caused ambiguity.
        - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING', 'DEPENDENT_MISMATCH']] — Represents the error code for the failed request.

Possible values:

**DEPENDENT_FIELD_MISSING** - A required dependent
field is missing from the criteria.

**DEPENDENT_MISMATCH** - A dependent field value does
not match the expected value.

        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing or mismatched dependent field.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

        - `details` (object) **REQ** — Represents the additional error details about the missing or mismatched dependent field.
          - `dependee` (object) **REQ** — Represents the details of the field that requires the missing dependent field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that requires the dependent field.
            - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field that requires the dependent field.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing or mismatched dependent field.
          - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the missing or mismatched dependent field.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the failed request.

Possible values:

**INVALID_DATA** - The specified owner is not a valid
subordinate user.

        - `details` (object) **REQ** — Represents the additional error details about the invalid owner parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that triggered the validation error.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the subordinate user validation failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.


- **403**: The current user does not have permission to change record ownership in the specified module.
Resolution: Request the Mass Transfer (change owner) permission for this module from your CRM administrator.
 [application/json]
    > Represents the error response returned when the current user lacks the Mass Transfer permission required to change ownership in the specified module.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the failed request.

Possible values:

**NO_PERMISSION** - The current user does not have
permission to change ownership of records in this
module.

    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the missing permission.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

    - `details` (object) **REQ** — Represents the additional error details about the missing permission.
      - `permissions` (array of string) [maxItems=1] **REQ** — Represents the list of permission keys required to perform this operation.
        items: [maxLen=255]

**Scopes:** ZohoCRM.change_owner.CREATE
