# POST /settings/approval_process/{approvalProcessId}/rules/actions/reorder
**Operation:** `postReorderRules` — Reorder the rules of an Approval Process
> To update the sequence of rules within one Approval Process, reorder the rules by assigning new sequence numbers to each rule ID in your Zoho CRM organization.

**Parameters:**
- `approvalProcessId` (path, string/int64, required) [maxLen=255, minLen=1, pattern=^[0-9]+$]: The unique identifier of the approval process to clone

**Request Body** — application/json `ReorderNestedV1`
> The request body must contain a reorder object with a rules array. You can include a maximum of 5 rule objects per request. For each rule, specify the ID of the rule to reorder and the new sequence number to assign to it.
  > Request body schema
  - `reorder` (object `ReorderNestedV2`) **REQ** — The main object that contains the information required to update the order of rules within an approval process. (Required)
    schema: `ReorderNestedV2`
    - `rules` (array of object `RulesNestedV2`) [maxItems=5] **REQ** — A list of rule entries whose sequence positions need to be rearranged. (Required)
      schema: `RulesNestedV2`
      - `sequence_number` (integer/int32) **REQ** — The new position or order number that you want to assign to the rule. (Required) (Unique)
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — The unique identifier of the rule that you want to reorder. (Required) (Unique)

**Responses:**

- **200**: Returns the result of the rule reordering in the Approval Process, including a code, a message confirming that the approval rules were reordered successfully, and the status of the request. — Schema: `PostreorderResponse200` [application/json]
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

- **400**: The request failed because the Approval Process ID in the URL is invalid or a sequence number is out of range, or a rule ID is invalid.
**Resolution:** The request URL must contain a valid Approval Process ID, and every rule ID and sequence number in the reorder data must be valid. [application/json]
    > Represents a bad request error caused by an invalid Approval Process ID in the request URL or by invalid rule reordering data.
    oneOf:
      - `ProcessInvalidDataErrorResponse9` — Invalid Id is sent in the URL for cloning.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
        - `reorder` (object) **REQ** — Contains error details for invalid reorder data, such as an invalid sequence number or an invalid rule ID.
          oneOf:
            - `RulesReorderInvalidDataErrorResponse1` — Range of sequence_number for rules exceeding the available number of rules.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `range` (object) — Detail field: range
                  - `from` (integer/int32) — Nested detail field: from
                  - `to` (integer/int32) — Nested detail field: to
              - `message` (string) **REQ** [enum=['invalid sequence number']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
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
            - `RulesReorderInvalidDataErrorResponse2` — invalid data for unique field : id
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['invalid approval rule id']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The user does not have the Manage automation permission required to reorder rules in an Approval Process.
**Resolution:** The Zoho CRM administrator must grant the Manage automation permission to the user's profile. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
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
