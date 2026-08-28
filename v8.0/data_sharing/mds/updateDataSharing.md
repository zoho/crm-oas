# PUT /settings/data_sharing
**Operation:** `updateDataSharing` — Data Sharing Settings
> To update your organization's default data-sharing permissions for modules. You can modify data-sharing access for both system-defined and custom modules.

**Request Body** — application/json
  > Root request body for updating data sharing settings.
  - `data_sharing` (array of object) [maxItems=100] **REQ** — Contains the details of your organization's default data-sharing permissions for modules.
    - `share_type` (string) **REQ** [enum=['private', 'public_read_write', 'public', 'public_read_only']] — Represents the access level you want to set for the module. **Possible values:** **private** - Only the record owner and their superior can view the records in the module. **public_read_only** - Users can view others' records but cannot modify or delete them. **public_read_write** - Users can view and modify others' records but cannot delete them. **public** - Users can view, modify, and delete others' records.
    - `module` (object) **REQ** — Contains the API name and ID of the module for which you want to change user access. Mandatory.
      - `api_name` (string) [maxLen=100] — Represents the API name of the module.
      - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique ID of the module.

**Responses:**

- **200**: The data sharing settings were updated successfully. [application/json]
    > Response object containing the update status for data sharing settings.
    - `data_sharing` (array of object) [maxItems=100] **REQ** — Array containing the update status for each module's data sharing setting.
      - `status` (string) **REQ** [enum=['success']] — Indicates the operation status.
      - `code` (string) **REQ** [enum=['SUCCESS']] — The status code of the operation.
      - `message` (string) **REQ** [enum=['data sharing settings updated successfully']] — A message describing the result of the operation.
      - `details` (object) **REQ** — Object containing additional details about the updated module.
        - `module` (string) [maxLen=100] — The API name of the module whose data sharing setting was updated.

- **400**: The request failed due to invalid data, missing mandatory fields, or an attempt to modify a module that is public in portals. [application/json]
    oneOf:
        - `data_sharing` (array of object) [maxItems=100] — Array containing the error details for each module's data sharing setting.
          - `status` (string) **REQ** [enum=['error']] — The status of the response.
          - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code identifying the type of error. **INVALID_DATA**- Indicates invalid input such as an invalid share_type or module. **NOT_ALLOWED**- Indicates the module is public in portals and cannot be modified.
          - `message` (string) **REQ** [enum=[2 values]] — A message describing the error.
          - `details` (object) **REQ** — Object containing additional details about the error, such as the field name and JSON path that caused the error.
            - `api_name` (string) [maxLen=100] — The API name of the field that caused the error.
            - `json_path` (string) [maxLen=2147483647] — The JSON path of the field that caused the error.
            - `regex` (string) [enum=['private|public_read_only|public_read_write|public']] — The expected regex pattern for the field value.
            - `expected_data_type` (string) [enum=['text', 'bigint']] — The expected data type of the field.
        - `status` (string) [enum=['error']] — The status of the response.
        - `code` (string) [enum=['INVALID_DATA']] — The error code identifying the type of error.
        - `message` (string) [enum=['invalid data']] — A message describing the error.
        - `details` (object) — Object containing additional details about the error.
          - `api_name` (string) [maxLen=100] — The API name of the field that caused the error.
          - `json_path` (string) [maxLen=2147483647] — The JSON path of the field that caused the error.
          - `maximum_length` (integer/int32) — The maximum number of items allowed in the request.

- **403**: The user does not have the required permission to update data sharing settings. [application/json]
    > Error response returned when the user does not have the Crm_Implied_Manage_Data_Sharing permission to update data sharing settings.
    - `status` (string) **REQ** [enum=['error']] — The status of the response.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The error code identifying the type of error.
    - `message` (string) **REQ** [enum=['permission denied']] — A message describing the error.
    - `details` (object) **REQ** — Object containing additional error details.
      - `permissions` (array of string) [maxItems=1] **REQ** — Array containing the list of permissions required to perform the operation.
        items: [enum=['Crm_Implied_Manage_Data_Sharing']]

**Scopes:** ZohoCRM.settings.data_sharing.UPDATE, ZohoCRM.settings.data_sharing.ALL
