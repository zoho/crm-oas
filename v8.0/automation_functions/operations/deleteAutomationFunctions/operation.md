# DELETE /settings/automation/functions
**Operation:** `deleteAutomationFunctions` — Delete Functions
> To delete one or more automation functions from your Zoho CRM organization.

**Parameters:**
- `ids` (query, string/int64, required): Specify the unique IDs of the records for which you want to perform the operation. Accepts comma-separated values.

**Schemas:**
`AutomationFunctionActionResult`:
  > Represents the result of processing an automation function action, including a status code, message, and associated details.
  - `code` (string) **REQ** [enum=['SUCCESS']] — The status code indicating the outcome of the automation function action. Possible values: **SUCCESS** - The automation function action was processed successfully.
  - `details` (object `AutomationFunctionOperationDetails`) **REQ** — Operation details for a processed automation function, including the resulting resource identifier.
  - `message` (string) **REQ** [maxLen=255] — The message describing the result of the operation.
  - `status` (string) **REQ** [enum=['success']] — The overall status of the operation. Possible values: **success** - The operation completed successfully.
`AutomationFunctionDeleteInvalidDataError`:
  > Error result returned when an invalid function ID is specified during bulk deletion.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of error. Possible values: **INVALID_DATA** - The request contains an invalid function ID.
  - `details` (object `AutomationFunctionOperationDetails`) **REQ** — Operation details for a processed automation function, including the resulting resource identifier.
  - `message` (string) **REQ** [maxLen=255] — The error message describing the issue.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates that the request resulted in an error.
`AutomationFunctionOperationDetails`:
  > Operation details for a processed automation function, including the resulting resource identifier.
  - `id` (string/int64) **REQ** — The unique identifier of the automation function that was processed.

**Responses:**

- **200**: Returns the deletion status for each automation function in the request. — Schema: `AutomationFunctionDeletionResponse` [application/json]
    > The response returned after deleting a single automation function, containing the result of the deletion operation.
    schema: `AutomationFunctionDeletionResponse`
    - `functions` (array of object `AutomationFunctionActionResult`) [maxItems=200] **REQ** — The list of deletion results for the specified automation functions.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a multi-status response. Each item in the **functions** array independently indicates success or failure for the corresponding automation function in the request. — Schema: `AutomationFunctionBulkRemovalResponse` [application/json]
    > The response returned after removing one or more automation functions in bulk, containing per-item results for each function in the request.
    schema: `AutomationFunctionBulkRemovalResponse`
    - `functions` (array of object) [minItems=2, maxItems=200] **REQ** — The list of individual removal results, one entry per automation function included in the bulk request.
      oneOf:
        - `AutomationFunctionActionResult` — Represents the result of processing an automation function action, including a status code, message, and associated details.
        - `AutomationFunctionDeleteInvalidDataError` — Error result returned when an invalid function ID is specified during bulk deletion.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax. **Resolution:** The request body must be corrected to use valid syntax before resubmitting. — Schema: `MissingIdParameterErrorResponse` [application/json]
    > Represents the error response returned when a required identifier parameter is missing from the request.
    schema: `MissingIdParameterErrorResponse`
    - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code identifying the type of error. Possible values: REQUIRED_PARAM_MISSING - Indicates that a required identifier parameter was not supplied in the request.
    - `details` (object) **REQ** — The error details for the missing parameter. Contains the **param_name** property identifying the required parameter that was not provided.
      - `param_name` (string) **REQ** [maxLen=255] — The name of the required parameter that is missing.
    - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — The error message describing the issue. Possible values: **One of the expected parameter is missing** - Indicates that a required parameter was not included in the request.
    - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.DELETE
