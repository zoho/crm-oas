# GET /settings/fields/{fieldId}/actions/scheduled_jobs
**Operation:** `getScheduledJobs` — Get scheduled jobs for a field
> To retrieve the status of scheduled jobs for picklist field operations in your Zoho CRM account, such as replace or delete picklist option jobs.

**Parameters:**
- `job_id` (query, string/int64, optional): Specify the job ID of the scheduled field or picklist action to filter the results.
- `module` (query, string, required) [maxLen=30] {style=form, explode=True}: Specify the API name of the module for which you want to retrieve field data. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `page` (query, integer/int32, optional): Specify the page number for paginating the scheduled jobs list.
- `per_page` (query, integer/int32, optional): Specify the number of scheduled jobs to return per page.
- `fieldId` (path, string, required) [maxLen=255]: Specify the unique ID of the custom field.

**Responses:**

- **200**: Returns the list of scheduled jobs for the specified field, with their status, action type, and processing details. — Schema: `FieldPicklistJobsResponse` [application/json]
    > Represents the response body for the scheduled jobs request, containing the list of scheduled picklist field action jobs and pagination details.
    schema: `FieldPicklistJobsResponse`
    - `scheduled_jobs` (array of object `FieldPicklistActionJob`) [maxItems=200] **REQ** — Represents the list of scheduled picklist field action jobs retrieved for the specified field.
      schema: `FieldPicklistActionJob`
    - `info` (object `ListPageInfo`) **REQ** — Represents the pagination metadata for the scheduled jobs list, including per-page size, current page, item count, and whether more records are available.
      schema: `ListPageInfo`
      - `per_page` (integer/int32) **REQ** — Represents the per page count.
      - `count` (integer/int32) **REQ** — Represents the count of the jobids.
      - `page` (integer/int32) **REQ** — Represents the page number.
      - `more_records` (boolean) **REQ** — Represents the more records available.

- **204**: No content. The request was processed successfully, and no scheduled jobs are available for the specified field.

- **400**: The request is invalid. Resolution: Ensure the **module** query parameter is a valid module API name, the **fieldId** path parameter is a valid field ID, and required parameters are included. [application/json]
    oneOf:
      - `InvalidModuleError` — Represents the error response returned when the provided module name is invalid or not recognized.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the invalid module error.
        - `details` (object) **REQ** — Represents the validation details for the invalid module error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the query parameter that contains the invalid module name.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message indicating the module name is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `InvalidFieldIdError` — Represents the error response returned when the supplied field ID is invalid for the requested operation.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid field ID error.
        - `details` (object) **REQ** — Represents the validation details for the invalid field ID error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the URL path segment that contains the invalid field ID.
        - `message` (string) **REQ** [enum=['The Field Id is Invalid']] — Represents the error message indicating the field ID is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `FeatureNotSupportedError` — Represents the error response returned when the requested feature is not supported by the current license.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — Represents the error code for the unsupported feature error.
        - `details` (object) **REQ** — Represents additional details about the unsupported feature error.
        - `message` (string) **REQ** [enum=['Your License does not support this feature']] — Represents the error message indicating the feature is not supported.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `RequiredParameterMissingError` — Represents the error response returned when a mandatory request parameter is missing.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the missing required parameter error.
        - `details` (object) **REQ** — Represents the details of the missing required parameter error, including the parameter name.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the required parameter that is missing from the request.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message indicating a required parameter is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status.

- **403**: Permission denied to retrieve scheduled jobs for this field. Resolution: The CRM administrator must grant the required permission to the user's profile. — Schema: `PermissionDeniedError` [application/json]
    > Represents the error response returned when the caller does not have the required permission to perform the requested operation.
    schema: `PermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission denied error.
    - `details` (object) **REQ** — Represents the details of the permission denied error, including the required CRM permissions.
      - `permissions` (array of string) [maxItems=25] **REQ** — Represents the list of CRM permissions required to perform the requested operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating permission was denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status.

**Scopes:** ZohoCRM.settings.fields.READ
