# GET /settings/approval_process
**Operation:** `getApprovalProcess` — Get Approval Processes
> To get the list of Approval Processes configured in your Zoho CRM organization, including each process's details such as name, module, execution trigger, approval type, active status, and rules with stages and approver configuration, along with pagination info.

**Parameters:**
- `module` (query, string, optional) [maxLen=3000]: Filter approval process based on module name
- `filter` (query, string, optional) [maxLen=10000]: For filtering the approval process using name
- `page` (query, integer/int32, optional) [min=1]: Param for pagination
- `per_page` (query, integer/int32, optional) [min=1, max=200]: Param for pagination
- `ids` (query, string/int64, optional) [maxLen=19, minLen=1, pattern=^[0-9]+$]: Approval process ids
- `generated_type` (query, string, optional) [enum=['custom', 'internal']]: Used to fetch "internal" approval processes  If not provided, by default fetch only user created approval processes. (generated_type = custom)
- `active` (query, boolean, optional): To filter active and inactive processes.

**Schemas:**
`GETCreatedByNested`:
  > Nested schema for created_by
  - `name` (string) **REQ** [maxLen=255] — Field: name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
`GETModifiedByNested`:
  > Nested schema for modified_by
  - `name` (string) **REQ** [maxLen=255] — Field: name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
`GETModuleNested`:
  > Nested schema for module
  - `api_name` (string) **REQ** [maxLen=255] — Field: api_name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id

**Responses:**

- **200**: Returns the list of Approval Processes configured in the Zoho CRM organization. Each item in the approval_process array is an Approval Process definition with details such as the module, description, active status, rules count, and creation metadata, and the info object provides pagination details for the result set. — Schema: `GetapprovalprocessResponse200` [application/json]
    > If approval processes were configured in the org, then list of approval processes were returned.
    schema: `GetapprovalprocessResponse200`
    - `approval_process` (array of object) [maxItems=200] **REQ** — Field: approval_process
      oneOf:
        - `GETApprovalProcessNested1` — Nested schema for approval_process
          - `created_time` (string) **REQ** [maxLen=255] — Field: created_time
          - `module` (object `GETModuleNested`) **REQ** — Nested schema for module
          - `description` (string) **REQ** [maxLen=255] — Field: description
          - `active` (boolean) **REQ** — Field: active
          - `rules_count` (integer/int32) **REQ** — Field: rules_count
          - `created_by` (object `GETCreatedByNested`) **REQ** — Nested schema for created_by
          - `execute_on` (string) **REQ** [maxLen=255] — Field: execute_on
          - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
          - `modified_time` (string) **REQ** [maxLen=255] — Field: modified_time
          - `name` (string) **REQ** [maxLen=255] — Field: name
          - `modified_by` (object `GETModifiedByNested`) **REQ** — Nested schema for modified_by
          - `generated_type` (string) **REQ** [maxLen=255] — Field: generated_type
          - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
        - `GETApprovalProcessNested2` — Nested schema for approval_process
          - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
          - `created_time` (string) **REQ** [maxLen=255] — Field: created_time
          - `modified_time` (string) **REQ** [maxLen=255] — Field: modified_time
          - `module` (object `GETModuleNested`) **REQ** — Nested schema for module
          - `name` (string) **REQ** [maxLen=255] — Field: name
          - `modified_by` (object `GETModifiedByNested`) **REQ** — Nested schema for modified_by
          - `active` (boolean) **REQ** — Field: active
          - `rules_count` (integer/int32) **REQ** — Field: rules_count
          - `generated_type` (string) **REQ** [maxLen=255] — Field: generated_type
          - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `created_by` (object `GETCreatedByNested`) **REQ** — Nested schema for created_by
          - `execute_on` (string) **REQ** [maxLen=255] — Field: execute_on
    - `info` (object `GETInfoNested`) **REQ** — Nested schema for info
      schema: `GETInfoNested`
      - `per_page` (integer/int32) **REQ** — Field: per_page
      - `count` (integer/int32) **REQ** — Field: count
      - `page` (integer/int32) **REQ** — Field: page
      - `more_records` (boolean) **REQ** — Field: more_records
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Indicates that no Approval Processes are configured in the Zoho CRM organization or none match the request criteria. The response has no body.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed because it contains invalid data, an invalid module name, or input values that do not match the expected pattern.
**Resolution:** The request should be retried after confirming that the module parameter names a valid module, the filter comparator is "equal" or "contains", and the generated_type parameter is "custom" or "internal". [application/json]
    > Represents the error structure returned when the request to list Approval Processes cannot be processed due to invalid syntax. Matches exactly one of the possible bad request error variants defined for this operation.
    oneOf:
      - `ProcessInvalidModuleErrorResponse10` — If the module given in the module param is invalid or not found.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ProcessPatternNotMatchedErrorResponse1` — If the filter's comparator is given a value other than "equal" or "contains" this error is thrown.
        - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) [maxLen=255] — Detail field: api_name
        - `message` (string) **REQ** [enum=['Please check whether the input values are correct']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ProcessInvalidDataErrorResponse1` — If param "ids" is given a list of values other than type long, this error response is received.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['invalid data', 'invalid param']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ProcessPatternNotMatchedErrorResponse2` — If param "generated_type" is given a value other than "custom" & "internal" this error response is received.
        - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['Please check whether the input values are correct']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied.
**Resolution:** The user's CRM profile should be granted the Manage automation permission before the request is retried. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
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

**Scopes:** ZohoCRM.settings.approval_process.READ
