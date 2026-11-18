# GET /settings/blueprints/{blueprintId}/states
**Operation:** `getBlueprintStates` — Get Blueprint States
> To retrieve the states associated with a specific Blueprint in your Zoho CRM organization.

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Specify the [ID of the Blueprint](blueprints.yaml#$.paths./settings/blueprints.get) for which you want to retrieve the states.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Specify the Zoho service context for the request. Possible values: **automation** - Targets the automation service.
- `ids` (query, array, required) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Specify the [unique state IDs](blueprint_state_config.yaml#$.paths./settings/blueprints/{blueprintId}/states.get) to filter the query results. Accepts comma-separated values.

**Schemas:**
`BlueprintModule`:
  > A Zoho CRM module associated with a Blueprint, identified by its API name and unique identifier.
  - `api_name` (string) **REQ** [maxLen=255] — The API name of the Blueprint module.
  - `id` (string) **REQ** [maxLen=255] — The unique identifier of the Blueprint module.
`BlueprintStateSummary`:
  > A summary of a configured Blueprint state, including its associated process, module, picklist value, and escalation settings.
  - `process_id` (string) **REQ** [maxLen=255] — The unique ID of the Blueprint for which the state is configured.
  - `state_escalation` (object `StateEscalationSettings`) **REQ** — The escalation configuration for a Blueprint state, including the escalation period, threshold value, and trigger details.
  - `module` (object `BlueprintModule`) **REQ** — A Zoho CRM module associated with a Blueprint, identified by its API name and unique identifier.
  - `pick_list_value` (object `StatePicklistValue`) **REQ** — A picklist value for a state field, including its display value and unique identifier.
`EscalationAction`:
  > Represents an escalation action, pairing an action type with its name, identifier, and detailed configuration.
  - `details` (object `EscalationActionDetails`) — Action metadata including the action name, identifier, and the list of recipients to escalate to.
  - `type` (string) **REQ** [maxLen=255] — Represents the type of escalation action to be performed.
  - `name` (string) **REQ** [maxLen=255] — Represents the name of the escalation action.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the escalation action.
`EscalationActionDetails`:
  > Action metadata including the action name, identifier, and the list of recipients to escalate to.
  - `escalate_to` (array of object `EscalationRecipientSelection`) [maxItems=1] — The list of escalation targets to which the escalation action is directed.
  - `name` (string) [maxLen=255] — The name of the escalation action.
  - `id` (string) [maxLen=255] — The unique identifier of the escalation action.
  additionalProperties: any
`EscalationRecipientSelection`:
  > A recipient selection for an escalation action, containing the recipient type and ID.
  - `type` (string) **REQ** [maxLen=255, enum=['user', 'role', 'group', 'team_user', 'profile']] — The recipient type for the escalation. Possible values: **user** - An individual CRM user. **role** - A CRM role. **group** - A user group. **team_user** - A team member user. **profile** - A CRM profile.
  - `id` (string) **REQ** [maxLen=255] — The unique identifier of the escalation recipient.
`EscalationTrigger`:
  > An escalation trigger configured with a unique ID, timing parameters, and associated escalation actions.
  - `period` (string) **REQ** [maxLen=255] — The time period associated with the escalation trigger.
  - `execute_type` (string) **REQ** [maxLen=255] — The execution type of the escalation trigger.
  - `id` (string) **REQ** [maxLen=255] — The unique identifier of the escalation trigger.
  - `value` (integer/int32) **REQ** — The numeric threshold value that triggers the escalation condition.
  - `actions` (array of object `EscalationAction`) [maxItems=30] **REQ** — The list of actions associated with the escalation trigger.
`InvalidStateIDQueryParamError`:
  > Error returned when a state ID provided as a query parameter is invalid.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
  - `details` (object) **REQ** — Represents the details of the invalid query parameter error, containing the name and value of the parameter that caused the error.
    - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the query parameter that caused the invalid state error.
    - `id` (string) **REQ** [maxLen=255] — Represents the invalid ID value submitted in the request.
  - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the provided ID is invalid. Possible values: the id given seems to be invalid - Indicates that the supplied ID does not correspond to a valid state.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
`StateEscalationSettings`:
  > The escalation configuration for a Blueprint state, including the escalation period, threshold value, and trigger details.
  - `period` (string) **REQ** [maxLen=255] — The time period defined for the escalation setting.
  - `value` (integer/int32) **REQ** — The numeric threshold value for the escalation setting.
  - `trigger_details` (array of object `EscalationTrigger`) [maxItems=3] **REQ** — The list of trigger detail objects that define the escalation conditions for the state.
`StatePicklistValue`:
  > A picklist value for a state field, including its display value and unique identifier.
  - `actual_value` (string) **REQ** [maxLen=255] — The stored value of the picklist option, used as the internal identifier for the selected state.
  - `id` (string) **REQ** [maxLen=255] — The unique identifier of the picklist value.

**Responses:**

- **200**: Returns the list of states configured for the specified Blueprint. — Schema: `BlueprintStateListResponse` [application/json]
    > Response containing a list of states configured for a blueprint.
    schema: `BlueprintStateListResponse`
    - `states` (array of object `BlueprintStateSummary`) [maxItems=100] **REQ** — Represents the list of Blueprint states included in the response.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a multi-status response. Each item in the array independently indicates success or failure for the corresponding record in the request. — Schema: `BlueprintStateListMultiStatusResponse` [application/json]
    > Represents a multi-status response for retrieving Blueprint states in bulk, containing a **states** array with a mix of successfully retrieved state objects and error entries.
    schema: `BlueprintStateListMultiStatusResponse`
    - `states` (array of object) [maxItems=100] **REQ** — Represents the list of Blueprint state results, where each entry contains either a successfully retrieved state object or a per-record error result.
      oneOf:
        - `BlueprintStateSummary` — A summary of a configured Blueprint state, including its associated process, module, picklist value, and escalation settings.
        - `InvalidStateIDQueryParamError` — Error returned when a state ID provided as a query parameter is invalid.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax. **Resolution:** The request syntax must be corrected before resubmitting. [application/json]
    oneOf:
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
      - `MissingModuleParameterError` — Represents the error response returned when the required **module** parameter is absent from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for this error condition. Possible values: **REQUIRED_PARAM_MISSING** - A required parameter is missing from the request.
        - `details` (object) **REQ** — An object containing additional details about the validation error, including the name of the missing or invalid parameter.
          - `param_name` (string) **REQ** [maxLen=255] — The name of the parameter that is missing from the request.
        - `message` (string) **REQ** [enum=['required param not found']] — The error message returned when a required parameter is missing. Possible values: required param not found - The request is missing a required parameter.
        - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to retrieve Blueprint states. **Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
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
