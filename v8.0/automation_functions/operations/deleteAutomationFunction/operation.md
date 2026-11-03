# DELETE /settings/automation/functions/{functionId}
**Operation:** `deleteAutomationFunction` — Delete Automation Function
> To delete an automation function from your Zoho CRM organization.

**Parameters:**
- `functionId` (path, string/int64, required) [maxLen=255]: Specify the unique ID of the function for which you want to perform the operation.

**Responses:**

- **200**: Returns a confirmation that the automation function was successfully deleted. — Schema: `AutomationFunctionDeletionResponse` [application/json]
    > The response returned after deleting a single automation function, containing the result of the deletion operation.
    schema: `AutomationFunctionDeletionResponse`
    - `functions` (array of object `AutomationFunctionActionResult`) [maxItems=200] **REQ** — The list of deletion results for the specified automation functions.
      schema: `AutomationFunctionActionResult`
      - `code` (string) **REQ** [enum=['SUCCESS']] — The status code indicating the outcome of the automation function action. Possible values: **SUCCESS** - The automation function action was processed successfully.
      - `details` (object `AutomationFunctionOperationDetails`) **REQ** — Operation details for a processed automation function, including the resulting resource identifier.
        schema: `AutomationFunctionOperationDetails`
        - `id` (string/int64) **REQ** — The unique identifier of the automation function that was processed.
      - `message` (string) **REQ** [maxLen=255] — The message describing the result of the operation.
      - `status` (string) **REQ** [enum=['success']] — The overall status of the operation. Possible values: **success** - The operation completed successfully.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax. **Resolution:** The request must be corrected to use valid syntax before resubmitting. — Schema: `UpdateInvalidFunctionIdErrorResponse` [application/json]
    > Validation error returned when the ID used to modify an automation function is invalid.
    schema: `UpdateInvalidFunctionIdErrorResponse`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of validation error. Possible values: **INVALID_DATA** - The function ID provided in the request is invalid.
    - `details` (object) **REQ** — Represents additional error details providing validation information, including the **resource_path_index** of the invalid function ID.
      - `resource_path_index` (integer/int32) **REQ** — The index in the resource path that contains the invalid identifier.
    - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message describing the issue with the request. Possible values: the id given seems to be invalid - The function identifier provided in the request is not recognized.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.DELETE
