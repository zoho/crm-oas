# POST /settings/approval_process/actions/reorder
**Operation:** `postReorder` — Reorder the execution sequence of approval processes
> To reorder the execution sequence of approval processes for a specific module in Zoho CRM. Specify the approval process IDs in the desired sequence. The system updates the execution order of the approval processes for that module.

**Parameters:**
- `module` (query, string, required) [maxLen=3000]: Approval process's module which needs to be reordered.

**Request Body** — application/json `PostreorderRequest`
> The request body must contain a **reorder** object with an **approval_process** array with one object per approval process.
  > Request body schema
  - `reorder` (object `ReorderNested`) **REQ** — root key for reordering the approval processes. (Required)
    schema: `ReorderNested`
    - `approval_process` (array of object `ApprovalProcessNestedV2`) [maxItems=100] **REQ** — A list of approval processes whose sequence/order needs to be updated. (Required)
      schema: `ApprovalProcessNestedV2`
      - `sequence_number` (integer/int32) **REQ** — The new position/order number you want to assign to this approval process. (Required) (Unique)
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — The unique identifier of the approval process that you want to reorder. (Required) (Unique)

**Responses:**

- **200**: Returns the status of the approval process reorder operation. — Schema: `PostreorderResponse200` [application/json]
    > Reordered the approval processes successfully
    schema: `PostreorderResponse200`
    - `reorder` (object `ReorderNested1`) — Nested schema for reorder
      schema: `ReorderNested1`
      - `code` (string) [maxLen=255] — Field: code
      - `details` (object) — Nested schema for details
      - `message` (string) [maxLen=255] — Field: message
      - `status` (string) [maxLen=255] — Field: status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax or duplicate sequence numbers.
**Resolution:** Verify the request syntax and ensure that each approval process is assigned a unique sequence number before retrying. [application/json]
    > Represents the error response for a failed approval process reorder request.
    oneOf:
        - `reorder` (object) **REQ** — Represents the error details returned for the approval process reorder request.
          oneOf:
            - `ProcessAlreadyExistsErrorResponse1` — Duplicate sequence_number is given
              - `code` (string) **REQ** [enum=['ALREADY_EXISTS']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `exists_in` (object) — Detail field: exists_in
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['duplicate sequence number']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `RulesReorderInvalidDataErrorResponse3` — Invalid range of sequence_number given
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `range` (object) — Detail field: range
                  - `from` (integer/int32) — Nested detail field: from
                  - `to` (integer/int32) — Nested detail field: to
              - `message` (string) **REQ** [enum=['invalid sequence number']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessReorderInvalidDataErrorResponse2` — invalid process id
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['invalid approval process id']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericMandatoryFieldMissingError` — Generic error indicating one or more required fields are missing.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Required field is missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericInvalidDataTypeError` — Generic validation error indicating an invalid data type was provided.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) [maxLen=255] — Detail field: expected_data_type
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Invalid data type']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericInvalidDataError` — Generic validation error indicating invalid data was provided.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) — Detail field: maximum_length
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
      - `ProcessReorderParamMissingErrorResponse1` — Missing required parameter: module
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ProcessReorderInvalidModuleErrorResponse1` — module param given is invalid
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['Invalid Module']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ProcessReorderNotAllowedErrorResponse1` — the value of the module param given is not supported or not allowed in approval process
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
        - `message` (string) **REQ** [enum=['the given module is not supported in api']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ProcessReorderInvalidDataErrorResponse1` — no process available for the given module
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['no processes available for given module']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The client does not have access rights to the content.
**Resolution:** The user must obtain the Manage Automation permission in Zoho CRM before retrying the request. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
    > Permission denied is thrown if user doesn't have permission for Manage automation.
    schema: `ApprovalProcessPermissionDeniedErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] — Detail field: permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.approval_process.UPDATE
