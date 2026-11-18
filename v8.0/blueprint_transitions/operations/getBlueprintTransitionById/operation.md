# GET /settings/blueprints/transitions/{transitionId}
**Operation:** `getBlueprintTransitionById` — Get Blueprint transition
> To retrieve the configuration details of a single Blueprint transition by its transition ID in your Zoho CRM organization. The response contains a transitions array with one Blueprint Transition Record, including its process ID, during inputs, owners, criteria, and actions.

**Parameters:**
- `transitionId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Specify the ID of the Blueprint transition you want to retrieve. Refer to the [Get Blueprint Transitions](blueprint_transitions.yaml#$.paths./settings/blueprints/transitions.get) resource for valid values.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Represents a custom request header that identifies the Zoho service associated with the request. Possible values: **automation**.

**Responses:**

- **200**: Returns the configuration details of the requested Blueprint transition. The response contains a transitions array with a single Blueprint Transition Record. — Schema: `BlueprintTransitionByIDResponse` [application/json]
    > Represents the successful response payload returned when retrieving transition details by identifier. Contains a transitions array with one or more blueprint transition records.
    schema: `BlueprintTransitionByIDResponse`
    - `transitions` (array of object `BlueprintTransitionRecord`) [maxItems=1] **REQ** — Contains the list of blueprint transition configurations retrieved in the response.
      schema: `BlueprintTransitionRecord`
      - `process_id` (string) [maxLen=255] — Represents the unique identifier of the blueprint process to which the transition belongs.
      - `during_inputs` (array of object) [maxItems=2, nullable] **REQ** — Contains the inputs collected from the user while executing the transition, such as fields, notes, attachments, tags, checklists, related lists, and kiosk screens.
        oneOf:
          - `TransitionInputFieldConfiguration` — Configuration for a field-type input collected during a transition, including the display sequence number, field reference, module context, optionality setting, unique identifier, type, and an optional validation filter.
            - `sequence_number` (integer/int32) **REQ** — Indicates the display order of the field among the inputs collected during the blueprint transition.
            - `validation_filter` (null) **REQ** — Contains the validation filter applied to the values entered for the field during the blueprint transition.
            - `field` (object `TransitionFieldMinimalReference`) **REQ** — Compact reference to a field used as a transition input, providing the field's unique identifier (ID) and API name for resolving input targets.
              schema: `TransitionFieldMinimalReference`
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the transition field.
              - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier (ID) of the transition field.
            - `module` (string) **REQ** [maxLen=255] — Represents the API name of the module to which the transition input field belongs.
            - `optional` (boolean) **REQ** — Indicates whether providing a value for the field is optional while performing the blueprint transition. Possible values: **true**, **false**.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the field collected as input during the blueprint transition.
            - `type` (string) **REQ** [maxLen=255] — Represents the data type of the field collected as input during the blueprint transition.
          - `TransitionInputChecklistDescriptor` — Descriptor for a checklist-type input collected during a transition, capturing the input sequence number, checklist details, unique identifier, and type.
            - `sequence_number` (integer/int32) **REQ** — Indicates the sequence number that defines the order of the checklist item in the transition input.
            - `checklist_info` (object `TransitionChecklistDetails`) **REQ** — Represents a checklist definition used as input during the transition, including its display title and ordered list of checklist items.
              schema: `TransitionChecklistDetails`
              - `title` (string) **REQ** [maxLen=255] — Represents the title of the checklist collected during the transition.
              - `items` (array of string) [maxItems=2] **REQ** — Contains the list of checklist items collected during the transition.
                items: [maxLen=255]
            - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the checklist descriptor collected as input during the transition.
            - `type` (string) **REQ** [maxLen=255] — Represents the type of the checklist item collected as input during the blueprint transition.
      - `criteria` (null) **REQ** — Represents the criteria that must be satisfied for a record to move through the transition.
      - `description` (string) [maxLen=1000] — Represents the description of the transition, providing additional details about its purpose.
      - `trigger_type` (string) **REQ** [maxLen=255] — Indicates how the transition is triggered, such as automatically when the record meets the transition criteria.
      - `module` (object `BlueprintModuleMinimalReference`) **REQ** — Represents a lightweight reference to the module associated with a transition, including the module ID and API name used to scope transition behavior.
        schema: `BlueprintModuleMinimalReference`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module to which the blueprint belongs.
        - `id` (string) **REQ** [maxLen=255] — Represents the ID of the module to which the blueprint belongs.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the transition in the blueprint.
      - `transition_type` (string) **REQ** [maxLen=255] — Indicates the type of the transition, such as standalone, common, parallel, child, or automatic.
      - `owners` (array of object `TransitionOwnerAssignment`) [maxItems=1] **REQ** — Represents the users permitted to execute the transition and move the record from one stage of the blueprint to another.
        schema: `TransitionOwnerAssignment`
        - `resources` (array of object `TransitionOwnerResource`) [maxItems=1, nullable] **REQ** — Contains the resources assigned as owners of the transition, identifying who can move the record between states.
          schema: `TransitionOwnerResource`
          - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the owner resource assigned to the transition.
        - `type` (string) **REQ** [maxLen=255] — Indicates the type of owner assignment that determines who can move the record through the transition.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the transition.
      - `actions` (array of object `TransitionActionSummary`) [maxItems=1, nullable] **REQ** — Contains the actions executed after the transition is completed, such as tasks, field updates, tags, and email notifications.
        schema: `TransitionActionSummary`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the transition action.
        - `details` (null) **REQ** — Contains the details of the action configured for the transition.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the transition action.
        - `type` (string) **REQ** [maxLen=255] — Indicates the type of the action configured for the transition, such as a task, field update, tag, or email notification.
      - `color_code` (string) **REQ** [maxLen=255] — Represents the color code associated with the transition in the blueprint.
      - `parallel_transition` (object) — Contains the configuration of the parallel transition associated with this transition, or null when no parallel transition is configured.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the parallel transition associated with this transition.
        - `name` (string) [maxLen=255] — Represents the name of the parallel transition associated with this transition.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The user does not have permission to perform this action.
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
