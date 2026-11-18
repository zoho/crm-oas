# GET /settings/blueprints/{blueprintId}/states/{stateId}
**Operation:** `getBlueprintStateById` — Get a Blueprint state by ID
> To retrieve the details of a single Blueprint state in your Zoho CRM organization.

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Specify the [unique ID of the Blueprint](blueprints.yaml#$.paths./settings/blueprints.get) for which you want to retrieve the state.
- `stateId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Represents the unique ID of the state. Use the [Get Blueprint States API](blueprint_state_config.yaml#$.paths./settings/blueprints/{blueprintId}/states.get) to retrieve the state ID.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Specify the Zoho service context for the request. Possible values: **automation** - Targets the automation service.

**Responses:**

- **200**: Returns the details of the specified Blueprint state. — Schema: `BlueprintStateDetailResponse` [application/json]
    > Represents the response payload containing detailed information for a single Blueprint state, including its associated state data.
    schema: `BlueprintStateDetailResponse`
    - `states` (array of object `BlueprintStateDetail`) [maxItems=1] **REQ** — The list of Blueprint state detail objects returned in the response.
      schema: `BlueprintStateDetail`
      - `process_id` (string) **REQ** [maxLen=255] — The unique ID of the Blueprint for which the state is configured.
      - `state_escalation` (object `StateEscalationProfile`) — An escalation profile for a state, containing the timing period, escalation value, and trigger details.
        schema: `StateEscalationProfile`
        - `period` (string) **REQ** [maxLen=255] — The period associated with the state escalation profile.
        - `value` (integer/int32) **REQ** — The numeric value associated with the escalation profile state.
        - `trigger_details` (array of object `StateEscalationTrigger`) [maxItems=3] **REQ** — The list of trigger details associated with the escalation profile.
          schema: `StateEscalationTrigger`
          - `period` (string) **REQ** [maxLen=255] — The time period after which the escalation trigger activates for the current state.
          - `execute_type` (string) **REQ** [maxLen=255] — The execution type for the state escalation trigger.
          - `id` (string) **REQ** [maxLen=255] — The unique identifier of the state escalation trigger.
          - `value` (integer/int32) **REQ** — The numeric threshold value that triggers the state escalation.
          - `actions` (array of object `StateEscalationAction`) [maxItems=10] **REQ** — The list of actions associated with the state escalation trigger.
            schema: `StateEscalationAction`
            - `details` (object `StateEscalationActionDetails`) **REQ** — The escalation action configuration for a specific state, including the recipients to escalate to.
              schema: `StateEscalationActionDetails`
              - `escalate_to` (array of object `EscalationRecipientReferencebyState`) [maxItems=1] **REQ** — The list of escalation targets for the state escalation action.
                schema: `EscalationRecipientReferencebyState`
                - `id` (string) **REQ** [maxLen=255] — The unique identifier of the escalation recipient.
                - `type` (string) **REQ** [maxLen=255, enum=['user', 'role', 'group', 'team_user', 'profile']] — The recipient type for the escalation target. Possible values: **user** - An individual CRM user. **role** - A CRM role. **group** - A CRM user group. **team_user** - A team user. **profile** - A CRM profile.
            - `type` (string) **REQ** [maxLen=255] — The type of the state escalation action.
            - `name` (string) **REQ** [maxLen=255] — The name of the escalation action.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the state escalation action.
      - `module` (object `BlueprintModuleDetails`) **REQ** — The module associated with a Blueprint state, including its unique identifier and API name.
        schema: `BlueprintModuleDetails`
        - `api_name` (string) **REQ** [maxLen=255] — The API name of the Blueprint module.
        - `id` (string) **REQ** [maxLen=255] — The unique identifier of the Blueprint module.
      - `pick_list_value` (object `StatePicklistValueDetails`) **REQ** — A picklist value for a state field, containing the unique identifier and the corresponding actual value.
        schema: `StatePicklistValueDetails`
        - `actual_value` (string) **REQ** [maxLen=255] — The actual stored value of the picklist option in Zoho CRM.
        - `id` (string) **REQ** [maxLen=255] — The unique identifier of the picklist value.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request could not be processed due to invalid syntax. **Resolution:** The request syntax must be corrected before resubmitting. [application/json]
    oneOf:
      - `InvalidStateIDError` — Error returned when the provided state identifier is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the state ID is invalid. Possible values: **INVALID_DATA** - The provided state ID is not valid.
        - `details` (object) **REQ** — Represents an object containing additional details about the validation error, including the **resource_path_index** of the invalid state ID.
          - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index of the path segment in the request URL where the invalid state ID was encountered.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the provided ID is invalid. Possible values: the id given seems to be invalid - Indicates that the supplied ID does not correspond to a valid state.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the response contains an error.
      - `InvalidResourcePathError` — Represents the error response returned when the specified resource path is invalid or malformed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of invalid resource path error. Possible values: **INVALID_DATA** - The request contains invalid data.
        - `details` (object) **REQ** — Represents the error details for an invalid resource path. Contains a **resource_path_index** object with validation information identifying the invalid path.
          - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index of the path segment in the request URL that is invalid.
        - `message` (string) **REQ** [enum=['the process id given seems to be invalid']] — Represents the error message describing the issue. Possible values: the process id given seems to be invalid - The specified process ID does not correspond to a valid resource path.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
      - `ErrorResponseCore15` — Represents the error response returned when a required header is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_HEADER_MISSING']] — Represents the error code returned when a required header is missing from the request. Possible values: **REQUIRED_HEADER_MISSING** - A required header was not included in the request.
        - `details` (object) **REQ** — Represents an object containing additional details about the error, including information about the specific header or field that caused it.
          - `header_name` (string) **REQ** [maxLen=255] — Represents the name of the HTTP request header associated with the error.
        - `message` (string) **REQ** [enum=['One of the expected headers is missing']] — Represents the error message describing the issue. Possible values: One of the expected headers is missing - A required request header was not included in the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to access the Blueprint state. **Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
    > Represents the error response returned when the requesting user lacks permission to perform the operation.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for a permission failure. Possible values: **NO_PERMISSION** - The requesting user does not have permission to perform this action.
    - `details` (object) **REQ** — Represents error details with permission information.
      - `permissions` (array of string) [maxItems=100] **REQ** — Represents the list of permissions required to perform the requested operation.
        items: [enum=['Crm_Implied_Manage_Workflow']]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message returned when permission is denied. Possible values: permission denied - Indicates that the requesting user does not have the required permission to perform this action.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates that the request was not processed successfully.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.states.READ
