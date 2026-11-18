# POST /settings/blueprints/{blueprintId}/actions/deactivate
**Operation:** `deactivateBlueprint` — Deactivate Blueprint
> To deactivate a published blueprint in your Zoho CRM organization.

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: The ID of the blueprint to deactivate. Use the [Get Blueprint by ID](blueprints.yaml#$.paths./settings/blueprints/{blueprintId}.get) to retrieve the Blueprint ID.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Custom header

**Request Body** — application/json `BlueprintDeactivationRequest`
> Request body
  > Request payload that lists the blueprints to process for deactivation. The blueprints array (required) contains one or more Blueprint Deactivation Item objects specifying deactivation behavior for each blueprint.
  - `blueprints` (array of object `BlueprintDeactivationItem`) [maxItems=1] **REQ** — Root element within which data is specified (Required)
    schema: `BlueprintDeactivationItem`
    - `exit_records` (boolean) [nullable] — Indicates whether the record in the particular blueprint should be exited after the blueprint is deactivated.

**Responses:**

- **200**: OK - Successful response — Schema: `BlueprintDeactivationResponse` [application/json]
    > Successful response for a blueprint deactivation request. Returns a blueprints array containing one Blueprint Deactivation Result Item per processed blueprint.
    schema: `BlueprintDeactivationResponse`
    - `blueprints` (array of object `BlueprintDeactivationResultItem`) [maxItems=1] — Field: blueprints
      schema: `BlueprintDeactivationResultItem`
      - `status` (string) [maxLen=255] — Field: status
      - `code` (string) [maxLen=255] — Field: code
      - `details` (object `GeneratedSchema154`) — Nested schema for details
        schema: `GeneratedSchema154`
        - `id` (string) [maxLen=255] — Field: id
      - `message` (string) [maxLen=255] — Field: message
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
      - `ErrorResponseCore15` — Missing required header: X-CRM-ORG
        - `code` (string) **REQ** [enum=['REQUIRED_HEADER_MISSING']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `header_name` (string) **REQ** [maxLen=255] — Detail field: header_name
        - `message` (string) **REQ** [enum=['One of the expected headers is missing']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidResourcePathError` — Indicates the resource path is invalid (e.g., invalid path index), typically due to a malformed or incorrect identifier provided for activation.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['the process id given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `BlueprintCannotBeDeactivatedError` — The blueprint cannot be deactivated, typically because it is in a state that does not allow deactivation.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with the blueprint ID
          - `id` (string) **REQ** [maxLen=255] — Detail field: id
        - `message` (string) **REQ** [enum=['Blueprint cannot be deactivated']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `BlueprintAlreadyInactiveError` — The blueprint is already inactive and cannot be deactivated again.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with the blueprint ID
          - `id` (string) **REQ** [maxLen=255] — Detail field: id
        - `message` (string) **REQ** [enum=['Blueprint is already inactive']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
        - `blueprints` (array of object `ErrorResponseCore2`) [maxItems=25] **REQ** — Array of error objects
          schema: `ErrorResponseCore2`
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
          - `details` (object) **REQ** — Error details with validation information
            - `expected_data_type` (string) **REQ** [maxLen=255] — Detail field: expected_data_type
            - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
            - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
          - `message` (string) **REQ** [enum=['Invalid data type']] — Error message
          - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.CREATE
