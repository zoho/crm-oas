# POST /settings/blueprints/{blueprintId}/actions/activate
**Operation:** `activateBlueprint` — Activate Blueprint
> To publish a blueprint draft, republish a blueprint draft, or activate a previously deactivated blueprint in your Zoho CRM organization.

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: The ID of the blueprint to activate. Use the [Get Blueprint by ID](blueprints.yaml#$.paths./settings/blueprints/{blueprintId}.get) to retrieve the Blueprint ID.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Custom header

**Request Body** — application/json `BlueprintActivationPayload`
> Request body
  > Request body wrapper that provides a list of blueprints with their activation settings and required state mappings for transitioning from draft to active.
  - `blueprints` (array of object `BlueprintActivationSettings`) [maxItems=1] **REQ** — This is the root key of the request body (Required)
    schema: `BlueprintActivationSettings`
    - `map_states` (array of object `StateRemapPair`) [maxItems=1, nullable] — The current version will have active records associated with it, so when the draft is set to be activated, remap data is required, which contains the mapping of the picklist ID of the existing state and the replacing state.
      schema: `StateRemapPair`
      - `existing_state` (object `ExistingStateReference`) — Contains data about the existing state
        schema: `ExistingStateReference`
        - `id` (string) [maxLen=50, nullable] — Contains data about the existing state picklist ID
      - `replacing_state` (object `ReplacingStateReference`) — Contains data about the replacing state
        schema: `ReplacingStateReference`
        - `id` (string/int64) [maxLen=50, minLen=1, pattern=^[0-9]+$, nullable] — Contains data about the replacing state picklist ID
    - `move_records` (boolean) **REQ** — The current version will have active records associated with it, so when the draft is set to be activated, remap data is required (Required).

**Responses:**

- **200**: OK - Successful response — Schema: `BlueprintActivationSuccessResponse` [application/json]
    > Response returned upon successful activation of a blueprint. Includes a blueprints array with per-blueprint result details.
    schema: `BlueprintActivationSuccessResponse`
    - `blueprints` (array of object `GeneratedSchema54`) [maxItems=1] — Field: blueprints
      schema: `GeneratedSchema54`
      - `code` (string) [maxLen=255] — Field: code
      - `details` (object `GeneratedSchema39`) — Nested schema for details
        schema: `GeneratedSchema39`
        - `name` (string) [maxLen=50, nullable] — Action name
        - `id` (string) [maxLen=255] — Field: id
        additionalProperties: any
      - `message` (string) [maxLen=255] — Field: message
      - `status` (string) [maxLen=255] — Field: status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: No Content - Successful response with no body content
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
      - `InvalidResourcePathError` — Indicates the resource path is invalid (e.g., invalid path index), typically due to a malformed or incorrect identifier provided for activation.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['the process id given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
        - `blueprints` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `ErrorResponseCore27` — When we try to update more than one blueprint
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) **REQ** — Detail field: maximum_length
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ActivationRecordActionsMissingError` — Dependent field missing: specify the record actions to perform while publishing/activating the blueprint.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) **REQ** — Detail field: dependee
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Specify record actions to be done while publishing this blueprint.']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ActivationStateTargetsMissingError` — Dependent field missing: provide the states needed to move current records to the active version of the blueprint.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) **REQ** — Detail field: dependee
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `dependee_value` (string) **REQ** [maxLen=255] — Nested detail field: dependee_value
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Provide states to move the current records to current version of blueprint']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ErrorResponseCore25` — Blueprint name not provided in the request
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['required field not found']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `MapStatesAmbiguityError` — Ambiguity detected while processing state remapping. Provide valid and consistent values for map_states.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Detail field: ambiguity_due_to
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['Provide proper values']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ErrorResponseCore9` — When transition type provided is invalid
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
                - `supported_values` (array of string) [maxItems=25] **REQ** — Detail field: supported_values
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['the value given is invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ErrorResponseCore4` — Auto-generated from ApiDefinition for MANDATORY_NOT_FOUND
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Required field is missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ErrorResponseCore2` — Auto-generated from ApiDefinition for INVALID_DATA
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) **REQ** [maxLen=255] — Detail field: expected_data_type
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Invalid data type']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ErrorResponseCore6` — Auto-generated from ApiDefinition for INVALID_DATA
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) **REQ** — Detail field: maximum_length
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidValueResponse` — Returned when invalid module data is provided during a reorder request. Includes the code (INVALID_DATA), a descriptive message, status, and validation details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=[4 values]] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `MapStateMandatoryMissingError` — A required field (map_states) is missing during blueprint activation. Returned inside the blueprints array.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) **REQ** — Detail field: dependee
                  - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['mandatory param missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `NoTransitionsInBlueprintError` — Error returned when a blueprint has no transitions defined, preventing it from being activated (code: INVALID_DATA).
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details containing the descriptive message
                - `message` (string) **REQ** [maxLen=255] — Detail field: message
              - `message` (string) **REQ** [enum=['invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `MoveRecordsMandatoryError` — Mandatory field missing: when the blueprint has active records, move_records must be provided to indicate how those records should be handled during activation.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['When blueprint has records, move_records is mandatory']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidProcessIDError` — The provided process ID is invalid, preventing the blueprint from being activated.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `message` (string) **REQ** [maxLen=255] — Detail field: message
        - `message` (string) **REQ** [enum=['the process id given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `BlueprintLimitExceededError` — Activation cannot proceed because the blueprint limit has been exceeded.
        - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `limit` (integer/int32) **REQ** — Detail field: limit
        - `message` (string) **REQ** [enum=['Blueprint limit exceeded']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `DuplicateBlueprintNameError` — Activation or publication is not allowed because another blueprint with the same name already exists.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['Already a blueprint with same name exists']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `DisconnectedStatesError` — The blueprint contains states that are not connected to any other states, which is not allowed.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['There exists states which are not connected to any other states']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `MissingStateTransitionsError` — Required transitions are missing between some states in the blueprint, preventing activation.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['Transitions are missing between few states']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `BlueprintAlreadyPublishedError` — The blueprint is already published. Republish is not allowed; create a draft version and publish that instead.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=[1 values]] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidBlueprintConnectionsError` — The connections defined in the chart data are invalid, preventing the blueprint from being published or activated.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=[1 values]] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `BlueprintAlreadyActiveError` — The blueprint is already active and cannot be activated again.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with the blueprint ID
          - `id` (string) **REQ** [maxLen=255] — Detail field: id
        - `message` (string) **REQ** [enum=['Blueprint is already active']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.CREATE
