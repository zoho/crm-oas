# GET /settings/blueprints/transitions
**Operation:** `getBlueprintTransitions` — Retrieve Blueprint transitions by their IDs
> To retrieve the details of the Blueprint transitions that match the specified transition IDs in your Zoho CRM organization.

**Parameters:**
- `ids` (query, array, required) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Represents a comma-separated list (CSV) of unique transition IDs used to retrieve specific blueprint transition configurations.

**Responses:**

- **200**: Returns a paginated collection of Blueprint transitions matching the specified transition IDs, along with pagination metadata. — Schema: `BlueprintTransitionsListResponse` [application/json]
    > Represents the container for a paginated collection of blueprint transitions and the related pagination information retrieved from the transitions settings endpoint.
    schema: `BlueprintTransitionsListResponse`
    - `transitions` (array of object `BlueprintTransitionDetail`) [maxItems=1] **REQ** — Contains the blueprint transition configurations retrieved by the list operation.
      schema: `BlueprintTransitionDetail`
      - `process_id` (string) [maxLen=255] — Represents the unique ID of the blueprint process to which the transition belongs.
      - `during_inputs` (array of object) [maxItems=2, nullable] **REQ** — Contains the inputs collected while the transition is executed, such as fields, notes, attachments, tags, checklists, related lists, and kiosk screens.
        oneOf:
          - `TransitionInputFieldRule` — Field-based input collected during a transition step, including the display sequence, associated module and field, optionality, type, and an optional validation filter.
            - `sequence_number` (integer/int32) **REQ** — Indicates the order in which the field appears among the inputs collected during the blueprint transition.
            - `validation_filter` (null) **REQ** — Contains the validation filter applied to the value of the field collected during the blueprint transition.
            - `field` (object `TransitionFieldReference`) **REQ** — Reference to a field required or used during a transition, identified by its API name and unique field ID.
              schema: `TransitionFieldReference`
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field referenced in the transition.
              - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the field referenced in the transition.
            - `module` (string) **REQ** [maxLen=255] — Represents the module to which the field collected as input during the blueprint transition belongs.
            - `optional` (boolean) **REQ** — Indicates whether the field is optional when input is collected during the blueprint transition. Possible values: **true**, **false**.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the field input rule configured for the blueprint transition.
            - `type` (string) **REQ** [maxLen=255] — Represents the type of the field collected as input during the blueprint transition.
          - `TransitionInputChecklistRule` — Checklist-based input collected during a transition step, including the display sequence, checklist content, unique identifier, and component type.
            - `sequence_number` (integer/int32) **REQ** — Indicates the display order of the checklist rule within the transition input.
            - `checklist_info` (object `TransitionChecklistInfo`) **REQ** — Contains the title and list of items of a checklist that must be reviewed or completed as part of the transition input.
              schema: `TransitionChecklistInfo`
              - `title` (string) **REQ** [maxLen=255] — Represents the title of the checklist configured for the transition.
              - `items` (array of string) [maxItems=2] **REQ** — Contains the list of checklist items collected during the transition.
                items: [maxLen=255]
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the checklist rule configured for the transition input.
            - `type` (string) **REQ** [maxLen=255] — Represents the type of the checklist rule applied to the transition input.
      - `criteria` (null) **REQ** — Contains the criteria that determine when a record is allowed to move through the transition.
      - `trigger_type` (string) **REQ** [maxLen=255] — Indicates the type of trigger that initiates the transition.
      - `module` (object `TransitionModuleReference`) **REQ** — Represents a reference to the module associated with the transition, providing both the API name and the unique module ID.
        schema: `TransitionModuleReference`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module associated with the transition.
        - `id` (string) **REQ** [maxLen=255] — Represents the ID of the module associated with the transition.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the transition.
      - `transition_type` (string) **REQ** [maxLen=255] — Indicates the type of the transition, such as standalone, common, parallel, child, or automatic.
      - `owners` (array of object `TransitionOwnerDescriptor`) [maxItems=1] **REQ** — Contains the owners who are allowed to move a record through the transition.
        schema: `TransitionOwnerDescriptor`
        - `resources` (array of object `OwnerResourceReference`) [maxItems=1, nullable] **REQ** — Contains the resources that identify the owners allowed to move the record through the transition.
          schema: `OwnerResourceReference`
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the owner resource associated with the blueprint transition.
        - `type` (string) **REQ** [maxLen=255] — Indicates the type of the transition owner, identifying who is allowed to move the record through the transition.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the transition.
      - `actions` (array of object `TransitionActionDescriptor`) [maxItems=1, nullable] **REQ** — Contains the actions that run after the transition is executed, such as tasks, field updates, tags, and email notifications.
        schema: `TransitionActionDescriptor`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the transition action descriptor.
        - `details` (null) **REQ** — Contains the additional details associated with the transition action descriptor.
        - `id` (string) **REQ** [maxLen=255] — Represents the ID of the transition action descriptor.
        - `type` (string) **REQ** [maxLen=255] — Indicates the type of the transition action descriptor.
      - `color_code` (string) **REQ** [maxLen=255] — Represents the color code associated with the transition in the blueprint.
      - `parallel_transition` (object) — Contains the details of the parallel transition associated with this transition, such as its ID and name.
        - `id` (string) [maxLen=255] — Represents the unique ID of the parallel transition.
        - `name` (string) [maxLen=255] — Represents the name of the parallel transition.
      - `description` (string) [maxLen=1000] — Contains the description of the transition.
    - `info` (object `ListPageInfo`) — Contains the pagination metadata for list responses, including the number of records per page, the current page number, the count of records returned, and whether more records are available.
      schema: `ListPageInfo`
      - `per_page` (integer/int32) **REQ** — Represents the number of records returned per page in the paginated response.
      - `count` (integer/int32) **REQ** — Represents the total number of records retrieved in the current paginated response.
      - `page` (integer/int32) **REQ** — Represents the current page number of the paginated response.
      - `more_records` (boolean) **REQ** — Indicates whether additional records are available beyond the current page. Possible values: **true**, **false**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request - The request cannot be processed due to invalid syntax.
**Resolution:** The `ids` query parameter in the request must contain valid values. [application/json]
    > The error object returned when the request cannot be processed due to invalid syntax. The response matches one of several error schemas for the 400 or 403 status codes, which describe missing required parameters or invalid request data.
    oneOf:
      - `MissingModuleParameterError` — Represents the error returned when the required module parameter is missing from the request. Possible values for code: **REQUIRED_PARAM_MISSING**.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when a required module parameter is missing. Possible values: **REQUIRED_PARAM_MISSING**.
        - `details` (object) **REQ** — Contains the error details with validation information, including the name of the missing module parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the missing module parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message returned when a required module parameter is missing. Possible values: **One of the expected parameter is missing**.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
      - `InvalidDataError` — Represents a general validation error returned when the request data is invalid. The error code is **INVALID_DATA**.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request data fails validation. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Contains the error details object with field-level validation information about the invalid data failure.
          - `maximum_length` (integer/int32) **REQ** — Indicates the maximum permitted length for the field that caused the validation error.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation error.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation error.
        - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned for the validation failure. Possible values: **Invalid data**.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Forbidden - No permission to perform this action.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
    > Represents the error returned when the user does not have the permission required to perform the action. Possible values for code: **NO_PERMISSION**.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the required permission is missing. Possible values: **NO_PERMISSION**.
    - `details` (object) **REQ** — Contains the error details with the list of missing permissions.
      - `permissions` (array of string) [maxItems=25] **REQ** — Contains the list of permissions required to perform the operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message returned when access is denied due to missing permissions. Possible values: **permission denied**.
    - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.transitions.READ
