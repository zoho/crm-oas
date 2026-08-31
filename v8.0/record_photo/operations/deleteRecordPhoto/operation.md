# DELETE /{module}/{record}/photo
**Operation:** `deleteRecordPhoto` — Delete a record photo
> To delete the photo associated with a specific record in your Zoho CRM organization.

**Parameters:**
- `module` (path, string, required) [maxLen=50]: Specify the API name of the module for which you want to manage the record photo. Refer to the [Get Modules Metadata API](modules.yaml#$.paths./settings/modules.get) to retrieve the module's API name.
- `record` (path, string/int64, required): Specify the unique identifier of the record for which you want to manage the photo. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.
- `restrict_triggers` (query, string, optional) [maxLen=100]: (Optional) Comma-separated list of automation triggers to suppress during the operation. Accepted values are `workflow`, `approval`, `blueprint`, `pathfinder`, and `orchestration`.

**Responses:**

- **200**: Returns a success response confirming the record photo delete operation completed. [application/json]
    > Represents the success response returned after a successful photo delete operation.
    - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code for the photo delete operation. Possible values: **SUCCESS**. 
    - `message` (string) **REQ** [maxLen=1000] — Represents the success message describing the result of the delete operation.
    - `status` (string) **REQ** [enum=['success']] — Represents the status of the response. Possible values: **success**. 
    - `details` (object) **REQ** — Represents additional details about the delete operation.

- **400**: The request is invalid due to an incorrect URL pattern, data, or module name.
**Resolution:** The module API name and record ID in the request URL must be valid. [application/json]
    > Represents the error response returned when the photo DELETE request fails due to an invalid URL pattern, data, or module.
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN', 'INVALID_DATA', 'INVALID_MODULE']] — Represents the error code indicating the type of request error. Possible values: **INVALID_URL_PATTERN**, **INVALID_DATA**, **INVALID_MODULE**. 
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the request failure.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error**. 
    - `details` (object) **REQ** — Represents additional details about the error. Contains the invalid identifier or resource path index when applicable.
      oneOf:
          - `id` (string) **REQ** [maxLen=100] — Represents the invalid identifier that caused the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the invalid resource path in the request URL.

**Scopes:** ZohoCRM.modules.DELETE
