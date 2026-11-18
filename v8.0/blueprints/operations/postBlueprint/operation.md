# POST /settings/blueprints
**Operation:** `postBlueprint` — Create a Blueprint
> To create a Blueprint with states and transitions for a module in your Zoho CRM organization. After creating the Blueprint, you must update each transition to set its modified time, which the user interface requires. Although **chart_data** is optional in the schema, provide it before you activate the Blueprint for the first time, including the canvas size, one node for each state, and one connection for each transition. Each state must include a module object, and each transition must include a layout object, both required at runtime.

**Parameters:**
- `X-ZOHO-SERVICE` (header, string, optional) [enum=['automation']] {style=simple, explode=False}: Represents the custom header used to identify the calling service.

**Schemas:**
`ActionDetails`:
  > Details of the actions
  - `name` (string) [maxLen=50, nullable] — Represents the name of the object referenced by this action, such as a tag or webhook, depending on the configured action type.
  - `id` (string) [maxLen=255] — Represents the unique ID of the object referenced by this action, such as a tag, record, or webhook, depending on the configured action type.
  additionalProperties: any
`BlueprintEmailNotificationActionEntry`:
  > Represents the email notification action configured for a Blueprint transition.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the email notification action associated with the transition.
  - `details` (object `ActionDetails`) — Details of the actions
  - `id` (string) [maxLen=25, nullable] — Represents the ID of the email notification action associated with the transition.
  - `type` (string) **REQ** [maxLen=20, enum=['email_notifications'], nullable] — Represents the type of the transition action.

Possible values:
email_notifications - Sends an email notification when the transition occurs.
`BlueprintFieldUpdateActionEntry`:
  > Represents the field update action configured for a Blueprint transition.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the field update action associated with the transition.
  - `details` (object `ActionDetails`) — Details of the actions
  - `id` (string) [maxLen=25, nullable] — Represents the ID of the field update action associated with the transition.
  - `type` (string) **REQ** [maxLen=20, enum=['field_updates'], nullable] — Represents the type of the transition action.

Possible values:
field_updates - Updates one or more fields on the record when the transition occurs.
`BlueprintFunctionsActionEntry`:
  > Represents the function action configured for a Blueprint transition.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the function action associated with the transition.
  - `details` (object `ActionDetails`) — Details of the actions
  - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]+$, nullable] — Represents the ID of the function action associated with the transition.
  - `type` (string) **REQ** [maxLen=20, enum=['functions'], nullable] — Represents the type of the transition action.

Possible values:
functions - Executes a custom function when the transition occurs.
`BlueprintGroupOwnerResource`:
  > Represents the group configured as the owner of the Blueprint or transition.
  - `id` (string) [maxLen=30, nullable] — Represents the unique ID of the group configured as the owner of the Blueprint or transition.
`BlueprintRoleOwnerResource`:
  > Represents the role configured as the owner of the Blueprint or transition.
  - `id` (string) [maxLen=30, nullable] — Represents the unique ID of the role configured as the owner of the Blueprint or transition.
`BlueprintUserOwnerResource`:
  > Represents the user configured as the owner of the Blueprint or transition.
  - `id` (string) [maxLen=30, nullable] — Represents the unique ID of the user configured as the owner of the Blueprint or transition.
`BlueprintWebhookActionEntry`:
  > Represents the webhook action configured for a Blueprint transition.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the webhook action associated with the transition.
  - `details` (object `ActionDetails`) — Details of the actions
  - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]+$, nullable] — Represents the ID of the webhook action associated with the transition.
  - `type` (string) **REQ** [maxLen=20, enum=['webhooks'], nullable] — Represents the type of the transition action.

Possible values:
webhooks - Triggers a webhook when the transition occurs.
`BlueprintWorkflowTaskActionEntry`:
  > Represents the workflow task action configured for a Blueprint transition.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the workflow task action associated with the transition.
  - `details` (object `ActionDetails`) — Details of the actions
  - `id` (string) [maxLen=25, nullable] — Represents the ID of the workflow task action associated with the transition.
  - `type` (string) **REQ** [maxLen=20, enum=['tasks'], nullable] — Represents the type of the transition action.

Possible values:
tasks - Creates a workflow task when the transition occurs.
`CriteriaFieldDetail`:
  > Contains field details of criteria
  - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=[0-9]+] — Represents the unique ID of the field for which the Blueprint is configured.
  - `api_name` (string) [maxLen=100, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — Represents the API name of the field for which the Blueprint is configured.
  - `field_label` (string) [maxLen=100, nullable] — Represents the label of the field for which the Blueprint is configured.
`NodeEndPointDetail`:
  - `position_x` (number/double) **REQ** [enum=[0, 0.12, 0.21, 0.3, 0.4, 0.5, 0.6, 0.7, 0.79, 0.88, 1]] — Represents the horizontal anchor position on the node boundary.
  - `position_y` (number/double) **REQ** [enum=[0, 0.5, 1]] — Represents the vertical anchor position on the node boundary.
  - `direction_x` (number/double) **REQ** [enum=[0]] — Represents the horizontal exit direction of the connector. Always 0 in all valid endpoint combinations.
  - `direction_y` (number/double) **REQ** [enum=[-1, 0, 1]] — Represents the vertical exit direction of the connector.
  oneOf:
      - `position_x` (object) [const=0.5] — Horizontal anchor position for the bottom-center-out endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the bottom-center-out endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the bottom-center-out endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the bottom-center-out endpoint configuration
      - `position_x` (object) [const=0.5] — Horizontal anchor position for the top-center-out endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the top-center-out endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the top-center-out endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the top-center-out endpoint configuration
      - `position_x` (object) [const=0] — Horizontal anchor position for the left-center-out endpoint configuration
      - `position_y` (object) [const=0.5] — Vertical anchor position for the left-center-out endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the left-center-out endpoint configuration
      - `direction_y` (object) [const=0] — Vertical exit direction for the left-center-out endpoint configuration
      - `position_x` (object) [const=1] — Horizontal anchor position for the right-center-out endpoint configuration
      - `position_y` (object) [const=0.5] — Vertical anchor position for the right-center-out endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the right-center-out endpoint configuration
      - `direction_y` (object) [const=0] — Vertical exit direction for the right-center-out endpoint configuration
      - `position_x` (object) [const=0.12] — Horizontal anchor position for the multi-set-1 top-left endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the multi-set-1 top-left endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-1 top-left endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the multi-set-1 top-left endpoint configuration
      - `position_x` (object) [const=0.88] — Horizontal anchor position for the multi-set-1 top-right endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the multi-set-1 top-right endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-1 top-right endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the multi-set-1 top-right endpoint configuration
      - `position_x` (object) [const=0.12] — Horizontal anchor position for the multi-set-1 bottom-left endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the multi-set-1 bottom-left endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-1 bottom-left endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the multi-set-1 bottom-left endpoint configuration
      - `position_x` (object) [const=0.88] — Horizontal anchor position for the multi-set-1 bottom-right endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the multi-set-1 bottom-right endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-1 bottom-right endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the multi-set-1 bottom-right endpoint configuration
      - `position_x` (object) [const=0.3] — Horizontal anchor position for the multi-set-2 top-left endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the multi-set-2 top-left endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-2 top-left endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the multi-set-2 top-left endpoint configuration
      - `position_x` (object) [const=0.7] — Horizontal anchor position for the multi-set-2 top-right endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the multi-set-2 top-right endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-2 top-right endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the multi-set-2 top-right endpoint configuration
      - `position_x` (object) [const=0.3] — Horizontal anchor position for the multi-set-2 bottom-left endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the multi-set-2 bottom-left endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-2 bottom-left endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the multi-set-2 bottom-left endpoint configuration
      - `position_x` (object) [const=0.7] — Horizontal anchor position for the multi-set-2 bottom-right endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the multi-set-2 bottom-right endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-2 bottom-right endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the multi-set-2 bottom-right endpoint configuration
      - `position_x` (object) [const=0.21] — Horizontal anchor position for the multi-set-3 top-left endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the multi-set-3 top-left endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-3 top-left endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the multi-set-3 top-left endpoint configuration
      - `position_x` (object) [const=0.79] — Horizontal anchor position for the multi-set-3 top-right endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the multi-set-3 top-right endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-3 top-right endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the multi-set-3 top-right endpoint configuration
      - `position_x` (object) [const=0.21] — Horizontal anchor position for the multi-set-3 bottom-left endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the multi-set-3 bottom-left endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-3 bottom-left endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the multi-set-3 bottom-left endpoint configuration
      - `position_x` (object) [const=0.79] — Horizontal anchor position for the multi-set-3 bottom-right endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the multi-set-3 bottom-right endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-3 bottom-right endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the multi-set-3 bottom-right endpoint configuration
      - `position_x` (object) [const=0.4] — Horizontal anchor position for the multi-set-4 top-left endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the multi-set-4 top-left endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-4 top-left endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the multi-set-4 top-left endpoint configuration
      - `position_x` (object) [const=0.6] — Horizontal anchor position for the multi-set-4 top-right endpoint configuration
      - `position_y` (object) [const=0] — Vertical anchor position for the multi-set-4 top-right endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-4 top-right endpoint configuration
      - `direction_y` (object) [const=-1] — Vertical exit direction for the multi-set-4 top-right endpoint configuration
      - `position_x` (object) [const=0.4] — Horizontal anchor position for the multi-set-4 bottom-left endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the multi-set-4 bottom-left endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-4 bottom-left endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the multi-set-4 bottom-left endpoint configuration
      - `position_x` (object) [const=0.6] — Horizontal anchor position for the multi-set-4 bottom-right endpoint configuration
      - `position_y` (object) [const=1] — Vertical anchor position for the multi-set-4 bottom-right endpoint configuration
      - `direction_x` (object) [const=0] — Horizontal exit direction for the multi-set-4 bottom-right endpoint configuration
      - `direction_y` (object) [const=1] — Vertical exit direction for the multi-set-4 bottom-right endpoint configuration
`NodeStateDetail`:
  > Contains details of the state mapped with the node (Required)
  - `api_name` (string) **REQ** [maxLen=99] — Represents the API name of the state.
`PutModuleDetail`:
  > Contains the details of the module for which blueprint is configured (Required)
  - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=[0-9]+] — Represents the unique ID of the module.
  - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the module.
  - `precedence` (integer/int32) [nullable] — Represents the precedence of the module.

**Request Body** — application/json `CreateBlueprintRequestBody`
> The request body must contain the Blueprint definition to create, including its states, transitions, and connections.
  > Represents the request body used to create a Blueprint.
  - `blueprints` (array of object `CreateBlueprintRequestItem`) [maxItems=1] **REQ** — Represents the root element that contains the details required to create the Blueprint.
    schema: `CreateBlueprintRequestItem`
    - `chart_data` (object `ChartDataSpec`) — Contains chart data of the blueprint configured
      schema: `ChartDataSpec`
      - `canvas_size` (object `CanvasSizeSpec`) **REQ** — Size of the canvas blueprint chart (Required)
        schema: `CanvasSizeSpec`
        - `width` (integer/int32) **REQ** — Represents the width of the Blueprint canvas.
        - `height` (integer/int32) **REQ** — Represents the height of the Blueprint canvas.
      - `nodes` (array of object `BlueprintNodeSpec`) [maxItems=2, nullable] — Represents the list of state nodes in the Blueprint chart.
        schema: `BlueprintNodeSpec`
        - `position_x` (integer/int32) **REQ** — Represents the x-axis position of the node in the Blueprint diagram.
        - `position_y` (integer/int32) **REQ** — Represents the y-axis position of the node in the Blueprint diagram.
        - `state` (object `NodeStateDetail`) **REQ** — Contains details of the state mapped with the node (Required)
      - `connections` (array of object `BlueprintConnectionSpec`) [maxItems=1, nullable] — Represents the list of connections between nodes in the Blueprint chart.
        schema: `BlueprintConnectionSpec`
        - `from` (object `ChartDataBase7`) **REQ** — Details of the source of the connection (Required)
          schema: `ChartDataBase7`
          - `end_point` (object `NodeEndPointDetail`) **REQ** — Details of end point of source of connection (Required)
          - `state` (object `NodeStateDetail`) **REQ** — Contains state details of source node (Required)
        - `to` (object `ConnectionTargetDetail`) **REQ** — Details of target of the connection (Required)
          schema: `ConnectionTargetDetail`
          - `end_point` (object `NodeEndPointDetail`) **REQ** — End point details of the target of the connection (Required)
          - `state` (object `NodeStateDetail`) **REQ** — Contains state details of the target node (Required)
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the connection between two states in the Blueprint chart.
        - `transition` (object `ConnectionTransitionRef`) **REQ** — Details of the transition mapped with the connection (Required)
          schema: `ConnectionTransitionRef`
          - `name` (string) [maxLen=100, nullable] — Represents the name of the transition mapped with the connection.
          - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the transition mapped with the connection.
    - `criteria` (object `BlueprintEntryCriteria`) — Contains details of blueprint entry criteria
      schema: `BlueprintEntryCriteria`
      - `comparator` (string) [maxLen=12, nullable] — Represents the comparator used to evaluate the criteria field against its configured value.
      - `field` (object `CriteriaFieldDetail`) — Contains field details of criteria
      - `type` (string) [maxLen=100, nullable] — Represents the type of criteria used to determine whether a record satisfies the Blueprint entry conditions.
      - `value` (string) [maxLen=3, nullable] — Represents the value configured for the criteria field used to evaluate the Blueprint entry condition.
    - `module` (object `PutModuleDetail`) **REQ** — Contains the details of the module for which blueprint is configured (Required)
    - `description` (string) [maxLen=1000, nullable] — Represents the description of the Blueprint.
    - `owners` (array of object `BlueprintOwnerConfig`) [maxItems=2, nullable] — Represents the list of owners configured for the Blueprint.
      schema: `BlueprintOwnerConfig`
      - `type` (string) **REQ** [maxLen=100, enum=['users', 'role', 'group', 'record_owner', 'portal_user_type']] — Represents the type of owner configured for the Blueprint.

Possible values:
users - Represents one or more specific users.
role - Represents users assigned a specific role.
group - Represents users belonging to a specific group.
record_owner - Represents the owner of the record.
portal_user_type - Represents a specific type of portal user.
      - `resources` (array of object) [maxItems=1] **REQ** — Represents the list of resource details configured for the Blueprint owner.
        anyOf:
          - `BlueprintUserOwnerResource` — Represents the user configured as the owner of the Blueprint or transition.
          - `BlueprintRoleOwnerResource` — Represents the role configured as the owner of the Blueprint or transition.
          - `BlueprintGroupOwnerResource` — Represents the group configured as the owner of the Blueprint or transition.
          - `BlueprintOwnerResource` — Represents the resource details of the Blueprint owner.
            - `id` (string) **REQ** [maxLen=25, pattern=[0-9]+] — Represents the unique ID of the Blueprint owner.
    - `transitions` (array of object `BlueprintTransitionConfig`) [maxItems=1, nullable] — Represents the list of transitions associated with the Blueprint.
      schema: `BlueprintTransitionConfig`
      - `criteria` (object `TransitionCriteriaDisplay`) — Details of criteria configured for the transition to be displayed
        schema: `TransitionCriteriaDisplay`
        - `comparator` (string) **REQ** [maxLen=12] — Represents the comparator used to evaluate the criteria.
        - `field` (object `CriteriaFieldDetail`) **REQ** — Details of fields configured in criteira (Required)
        - `type` (string) **REQ** [maxLen=5] — Represents the type of criteria, denoting whether the field value is compared against a static value or another field.
        - `value` (string) [maxLen=3, nullable] — Represents the value with which the field in the criteria should be compared.
      - `trigger_type` (string) **REQ** [maxLen=10, enum=['manual', 'automatic']] — Represents how the transition is triggered.

Possible values:
manual - The transition is triggered manually by a user.
automatic - The transition is triggered automatically by the system.
      - `module` (object `PutModuleDetail`) — Module details for which transition is configured
      - `description` (string) [maxLen=1000, nullable] — Represents the description of the transition.
      - `owners` (array of object `TransitionOwnerItem`) [maxItems=2, nullable] — Represents the list of owners for whom the transition is accessible.
        schema: `TransitionOwnerItem`
        - `type` (string) [maxLen=100, enum=['users', 'role', 'group', 'record_owner', 'portal_user_type'], nullable] — Represents the type of the owner.

Possible values:
users - Indicates that the owner is a specific user.
role - Indicates that the owner is a role.
group - Indicates that the owner is a group.
record_owner - Indicates that the owner is the record owner.
portal_user_type - Indicates that the owner is a portal user type.
        - `resources` (array of object) [maxItems=1, nullable] — Represents the list of resource details of the owner.
          anyOf:
            - `BlueprintUserOwnerResource` — Represents the user configured as the owner of the Blueprint or transition.
            - `BlueprintRoleOwnerResource` — Represents the role configured as the owner of the Blueprint or transition.
            - `BlueprintGroupOwnerResource` — Represents the group configured as the owner of the Blueprint or transition.
            - `BlueprintOwnerDetail` — Represents the details of the transition owner.
              - `id` (string) [maxLen=30, nullable] — Represents the unique ID of the transition owner.
      - `include_states` (array of object `CommonSourceDetail`) [maxItems=1, nullable] — Represents the list of source states included for the common transition.
        schema: `CommonSourceDetail`
        - `state` (object `CommonSourceStateDetail`) — State details of the common source
          schema: `CommonSourceStateDetail`
          - `name` (string) [maxLen=50, nullable] — Represents the name of the common source state.
          - `api_name` (string) [maxLen=50, nullable] — Represents the API name of the common source state.
      - `layout` (object `TransitionLayoutDetail`) — Layout details for which the transition is configured
        schema: `TransitionLayoutDetail`
        - `name` (string) [maxLen=100, nullable] — Represents the name of the layout.
        - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]{1,19}$, nullable] — Represents the unique ID of the layout.
        - `api_name` (string) [maxLen=100, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — Represents the API name of the layout.
      - `during_inputs` (array of object `DuringTransitionFieldList`) [maxItems=3, nullable] — Represents the list of fields configured to be captured during the transition.
        schema: `DuringTransitionFieldList`
        - `validation_filter` (object `DuringFieldValidationConfig`) — Details of validation configured for the during transition fields
          schema: `DuringFieldValidationConfig`
          - `criteria` (object `FieldValidationCriteria`) **REQ** — Criteria to validate the field (Required)
            schema: `FieldValidationCriteria`
            - `comparator` (string) **REQ** [maxLen=12] — Represents the comparator used to evaluate the field validation criteria.
            - `field` (object `CriteriaFieldDetail`) **REQ** — Field details of the criteria (Required)
            - `type` (string) **REQ** [maxLen=5] — Represents the type of criteria, denoting whether the field value is checked against a static value or another field.
            - `value` (string) **REQ** [maxLen=3] — Represents the value against which the field value should be checked.
          - `validation_message` (string) **REQ** [maxLen=100] — Represents the message displayed to the user when the during-transition field validation fails.
        - `sequence` (integer/int32) **REQ** — Represents the position in which the field is displayed within the during transition popup.
        - `optional` (boolean) [nullable] — Indicates whether the field is optional in the during transition popup.
        - `field` (object `CriteriaFieldDetail`) — Details of the field configured in during transition (Required)
        - `type` (string) **REQ** [maxLen=20, enum=[9 values]] — Represents the type of field configured for display in the during transition popup.

Possible values:
field - Indicates a standard field.
related_list - Indicates a related list.
info - Indicates an information block.
attachment - Indicates an attachment field.
tags - Indicates a tags field.
notes - Indicates a notes field.
checklist - Indicates a checklist field.
widget - Indicates a widget field.
kiosk - Indicates a kiosk field.
        additionalProperties: any
      - `common` (boolean) [nullable] — Indicates whether the transition is configured as a common transition.
      - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the transition.
      - `name` (string) **REQ** [maxLen=50] — Represents the name of the transition.
      - `transition_type` (string) **REQ** [maxLen=25, enum=['standalone_transition', 'parallel_transition', 'child_transition']] — Represents the type of the transition.

Possible values:
standalone_transition - The transition operates independently of other transitions.
parallel_transition - The transition can be executed in parallel with other transitions.
child_transition - The transition is defined as a child of another transition.
      - `actions` (array of object) [maxItems=3, nullable] — Represents the list of actions configured to be triggered after the transition is completed.
        discriminator: `type`
          tasks → #/components/schemas/BlueprintWorkflowTaskActionEntry
          email_notifications → #/components/schemas/BlueprintEmailNotificationActionEntry
          webhooks → #/components/schemas/BlueprintWebhookActionEntry
          field_updates → #/components/schemas/BlueprintFieldUpdateActionEntry
          functions → #/components/schemas/BlueprintFunctionsActionEntry
        oneOf:
          - `BlueprintWorkflowTaskActionEntry` — Represents the workflow task action configured for a Blueprint transition.
          - `BlueprintEmailNotificationActionEntry` — Represents the email notification action configured for a Blueprint transition.
          - `BlueprintWebhookActionEntry` — Represents the webhook action configured for a Blueprint transition.
          - `BlueprintFieldUpdateActionEntry` — Represents the field update action configured for a Blueprint transition.
          - `BlueprintFunctionsActionEntry` — Represents the function action configured for a Blueprint transition.
          - `TransitionPostActionConfig` — Represents the list of actions configured to be triggered after the transition is completed.
            - `name` (string) [maxLen=50, nullable] — Represents the name of the action associated with the transition.
            - `details` (object `ActionDetails`) — Details of the actions
            - `id` (string) [maxLen=25, nullable] — Represents the unique ID of the action associated with the transition.
            - `type` (string) **REQ** [maxLen=20, enum=[8 values], nullable] — Represents the type of the action.

Possible values:
add_tags - Indicates that the action adds tags to the record.
remove_tags - Indicates that the action removes tags from the record.
sms - Indicates that the action sends an SMS.
whatsapp - Indicates that the action sends a WhatsApp message.
create_record - Indicates that the action creates a record.
add_meeting - Indicates that the action adds a meeting.
schedule_call - Indicates that the action schedules a call.
convert - Indicates that the action converts the record.
      - `color_code` (string) [maxLen=10, nullable] — Represents the color code assigned to the transition.
    - `states` (array of object `BlueprintStateEntry`) [maxItems=301, nullable] — Represents the list of states associated with the Blueprint.
      schema: `BlueprintStateEntry`
      - `name` (string) [maxLen=100, nullable] — Represents the name of the state associated with the Blueprint.
      - `state_escalation` (object `StateEscalationAlertDetail`) — Details of escalation alerts configured for the state
        schema: `StateEscalationAlertDetail`
        - `period` (string) **REQ** [maxLen=30, enum=['days', 'hours', 'minutes', 'business_days', 'business_hours']] — Represents the type of period until which the record can remain in the state.

Possible values:
days - Indicates that the period is measured in days.
hours - Indicates that the period is measured in hours.
minutes - Indicates that the period is measured in minutes.
business_days - Indicates that the period is measured in business days.
business_hours - Indicates that the period is measured in business hours.
        - `value` (integer/int32) **REQ** — Represents the value of the period after which the escalation alert is triggered.
        - `trigger_details` (array of object `StateTriggerConfig`) [maxItems=1] **REQ** — Represents the list of triggers configured for the state.
          schema: `StateTriggerConfig`
          - `period` (string) **REQ** [maxLen=10, enum=['days', 'hours', 'minutes']] — Represents the type of the period for which the trigger is configured.

Possible values:
days - Indicates that the period is measured in days.
hours - Indicates that the period is measured in hours.
minutes - Indicates that the period is measured in minutes.
          - `execute_type` (string) **REQ** [maxLen=9, enum=['before', 'on', 'after']] — Represents the type denoting when the action should be triggered.

Possible values:
before - Indicates that the action is triggered before the specified period.
on - Indicates that the action is triggered exactly at the specified period.
after - Indicates that the action is triggered after the specified period.
          - `value` (integer/int32) **REQ** — Represents the value of the period for which the trigger is configured.
          - `actions` (array of object) [maxItems=2, nullable] — Represents the list of actions configured in the trigger.
            discriminator: `type`
              tasks → #/components/schemas/BlueprintWorkflowTaskActionEntry
              email_notifications → #/components/schemas/BlueprintEmailNotificationActionEntry
              webhooks → #/components/schemas/BlueprintWebhookActionEntry
              field_updates → #/components/schemas/BlueprintFieldUpdateActionEntry
              functions → #/components/schemas/BlueprintFunctionsActionEntry
            oneOf:
              - `BlueprintWorkflowTaskActionEntry` — Represents the workflow task action configured for a Blueprint transition.
              - `BlueprintEmailNotificationActionEntry` — Represents the email notification action configured for a Blueprint transition.
              - `BlueprintWebhookActionEntry` — Represents the webhook action configured for a Blueprint transition.
              - `BlueprintFieldUpdateActionEntry` — Represents the field update action configured for a Blueprint transition.
              - `BlueprintFunctionsActionEntry` — Represents the function action configured for a Blueprint transition.
              - `TransitionTriggerActionConfig` — Represents the list of actions configured in the trigger.
                - `name` (string) [maxLen=50, nullable] — Represents the name of the action associated with the state.
                - `details` (object `TransitionActionConfig`) — Details of the action configured
                  schema: `TransitionActionConfig`
                  - `name` (string) [maxLen=50, nullable] — Represents the name of the action.
                  - `escalate_to` (array of object `EscalationAlertTarget`) [maxItems=1, nullable] — Represents the list of escalation alert details configured for the trigger.
                    schema: `EscalationAlertTarget`
                    - `type` (string) **REQ** [maxLen=40, enum=['user', 'role', 'group', 'team_user', 'profile']] — Represents the type of user that receives the escalation alert.

Possible values:
user - Indicates that the alert targets a specific user.
role - Indicates that the alert targets users with a specific role.
group - Indicates that the alert targets a group.
team_user - Indicates that the alert targets a team member.
profile - Indicates that the alert targets users with a specific profile.
                    - `id` (string) **REQ** [maxLen=20, pattern=[0-9]+] — Represents the unique ID of the user to whom the escalation alert should be sent.
                  - `id` (string) **REQ** [maxLen=25, pattern=[0-9]+] — Represents the unique ID of the action.
                - `id` (string) [maxLen=25, pattern=[0-9]+, nullable] — Represents the unique ID of the action associated with the state.
                - `type` (string) **REQ** [maxLen=20, enum=['sla', 'circuits', 'whatsapp', 'sms'], nullable] — Represents the type of the action associated with the state.

Possible values:
sla - Indicates that the action is related to an SLA.
circuits - Indicates that the action is related to circuits of authority.
whatsapp - Indicates that the action sends a WhatsApp message.
sms - Indicates that the action sends an SMS.
      - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the state associated with the Blueprint.
      - `pick_list_value` (object `StatePicklistValue`) — Details of the picklist option mapped with the state
        schema: `StatePicklistValue`
        - `actual_value` (string) [maxLen=100, nullable] — Represents the name of the state.
        - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=[0-9]+] — Represents the unique ID of the picklist option.
      - `module` (object `PutModuleDetail`) — Details of module for which state is configured
    - `pipeline` (object `BlueprintPipelineInput`) — Contains details of the pipeline for which blueprint is configured
      schema: `BlueprintPipelineInput`
      - `name` (string) [maxLen=255, nullable] — Represents the name of the pipeline for which the Blueprint is configured.
      - `display_value` (string) [maxLen=100, nullable] — Represents the display value of the pipeline for which the Blueprint is configured.
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=[0-9]+] — Represents the unique ID of the pipeline for which the Blueprint is configured.
      - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the pipeline for which the Blueprint is configured.
    - `layout` (object `BlueprintLayoutSpec`) **REQ** — Details of the layout for which blueprint is configured (Required)
      schema: `BlueprintLayoutSpec`
      - `name` (string) [maxLen=100, nullable] — Represents the name of the layout for which the Blueprint is configured.
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=[0-9]+] — Represents the unique ID of the layout for which the Blueprint is configured.
      - `api_name` (string) [maxLen=100, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — Represents the API name of the layout for which the Blueprint is configured.
    - `field` (object `CriteriaFieldDetail`) **REQ** — Contains details of the field for which blueprint is configured (Required)
    - `api_name` (string) [maxLen=9, nullable] — Represents the API name of the Blueprint.
    - `continuous` (boolean) **REQ** — Indicates whether the Blueprint is configured as continuous.
    - `name` (string) **REQ** [maxLen=50] — Represents the name of the Blueprint.
    - `connections` (array of object `ConnectionRequestItem`) [maxItems=1, nullable] — Represents the list of connections made between two states and mapped with transitions.
      schema: `ConnectionRequestItem`
      - `from_state` (object `ConnectionSourceStateDetail`) **REQ** — Details of the state associated with source node of the connection (Required)
        schema: `ConnectionSourceStateDetail`
        - `name` (string) [maxLen=100, nullable] — Represents the name of the source state associated with the connection.
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the source state associated with the connection.
      - `transitions` (object `ConnectionTransitionSpec`) **REQ** — Details of transition associated with the connection (Required)
        schema: `ConnectionTransitionSpec`
        - `name` (string) [maxLen=100, nullable] — Represents the name of the transition associated with the connection.
        - `api_name` (string) **REQ** [maxLen=12] — Represents the API name of the transition associated with the connection.
        - `precedence` (integer/int32) [nullable] — Represents the precedence order of the transition associated with the connection.
      - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the connection.
      - `to_state` (object `ConnectionTargetState`) **REQ** — State associated with target node of the connection (Required)
        schema: `ConnectionTargetState`
        - `name` (string) [maxLen=100, nullable] — Represents the name of the target state associated with the connection.
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the target state associated with the connection.

**Responses:**

- **201**: Returns the details of the newly created Blueprint. — Schema: `PostBlueprintSuccessResponse` [application/json]
    > Represents the response returned when the Blueprint is successfully created.
    schema: `PostBlueprintSuccessResponse`
    - `blueprints` (array of object `DeleteBlueprintStatusItem`) [maxItems=1] — Represents the list containing the Blueprint created in the response.
      schema: `DeleteBlueprintStatusItem`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code indicating the outcome of the Blueprint deletion.

Possible values:
SUCCESS - Indicates that the Blueprint deletion completed successfully.
      - `details` (object `ActionDetails`) **REQ** — Represents the details of the object referenced by the transition action, such as a tag, record, or webhook, depending on the configured action type.
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the outcome of the Blueprint deletion.
      - `status` (string) **REQ** [maxLen=255] — Represents the status of the Blueprint deletion operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed because it contains invalid syntax. Resolution: The request payload must be corrected to use valid syntax that matches the expected schema. [application/json]
    oneOf:
        - `blueprints` (array of object) [maxItems=100] **REQ** — Represents the list of error entries returned when a Blueprint in the request cannot be processed, with each entry describing the specific issue for that Blueprint.
          oneOf:
            - `InvalidValueResponse` — Represents the error returned when invalid module data is provided during a reorder request.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the request contains invalid or unexpected data.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [maxLen=255] — Represents the error message returned when the specified value is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `OrphanStateConnectionError` — Represents the error returned when the only connection linking a state node no longer exists but the state remains.
              - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the error code returned by this response.

Possible values:
CANNOT_PROCESS - Indicates that the transition no longer exists but the state connected only by it remains.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['the transition is deleted but the state only connected by it is not deleted']] — Represents the error message returned by this response.

Possible values:
the transition is deleted but the state only connected by it is not deleted - Indicates that the transition no longer exists but the state connected only by it remains.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DuplicateNameFieldError` — Represents the error returned when the specified name value is a duplicate of an existing one.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when a duplicate field name is detected.

Possible values:
DUPLICATE_DATA - Indicates that the specified field name already exists.
              - `details` (object) **REQ** — Represents the details object with validation information about the duplicate name.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when a duplicate name or API name is detected.

Possible values:
The data is already given in the name - Indicates that the specified name is already in use.
a different state with same api_name found - Indicates that another state already uses the same API name.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `InvalidModuleParameterError` — Represents the error returned when the module given in the parameter is invalid.
              - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned by this response.

Possible values:
INVALID_MODULE - Indicates that the module given seems to be invalid.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter associated with the error.
              - `message` (string) **REQ** [enum=['the module given seems to be invalid']] — Represents the error message returned by this response.

Possible values:
the module given seems to be invalid - Indicates that the module given seems to be invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `CrossModuleNodeMappingError` — Represents the error returned when a state from a different module or layout is mapped to a node of this Blueprint.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when a state's module or layout does not match the specified Blueprint.

Possible values:
DEPENDENT_MISMATCH - Indicates that the module or layout of the state differs from that of the Blueprint.
              - `details` (object) **REQ** — Represents the details object that provides validation information about the mismatched module or layout.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field associated with the error.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when a state's module or layout does not match the specified Blueprint.

Possible values:
The module or layout of this state is different from the specified blueprint - Indicates that the state's module or layout does not match the Blueprint's configuration.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DependentMismatchStateWithDependee` — Represents the error returned when a state from a different module or layout, along with its dependee, is mapped to a node of this Blueprint.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when a state's module or layout does not match its dependee field.

Possible values:
DEPENDENT_MISMATCH - Indicates that the module or layout of the state differs from that of the dependee field.
              - `details` (object) **REQ** — Represents the details object with validation information about the mismatched state and its dependee field.
                - `dependee` (object) **REQ** — Represents the details of the dependee field associated with the mismatched state.
                  - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path that identifies the dependee field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when a state's module or layout does not match the specified Blueprint.

Possible values:
The module or layout of this state is different from the specified blueprint - Indicates that the state's module or layout does not match the Blueprint's configuration.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `MultipleUpdateNotAllowedError` — Represents the error returned when an attempt is made to update more than one Blueprint.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that invalid data.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field value.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned by this response.

Possible values:
invalid data - Indicates that invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `InvalidTransitionTypeError` — Represents the error returned when the transition type provided is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the value given is invalid.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['the value given is invalid']] — Represents the error message returned by this response.

Possible values:
the value given is invalid - Indicates that the value given is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DependentMismatchTransitionError` — Represents the error returned when a transition from a different module or layout is mapped to a connection of this Blueprint.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when a transition's module or layout does not match its dependent field.

Possible values:
DEPENDENT_MISMATCH - Indicates that the module or layout of the transition differs from that of the dependent field.
              - `details` (object) **REQ** — Represents the details object with validation information about the mismatched transition.
                - `dependee` (object) **REQ** — Represents the details of the dependee field associated with the mismatched transition.
                  - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path that identifies the dependee field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['The module or layout of this transition is different from the blueprint']] — Represents the error message returned when a transition's module or layout does not match the Blueprint.

Possible values:
The module or layout of this transition is different from the blueprint - Indicates that the transition's module or layout does not match the Blueprint's configuration.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `InvalidCriteriaUpdateError` — Represents the error returned when the updated criteria is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that invalid data.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned by this response.

Possible values:
invalid data - Indicates that invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `UnsupportedBlueprintFieldError` — Represents the error returned when the given field is not supported for configuring the Blueprint.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that the given field not supported for Blueprint creation.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned by this response.

Possible values:
the given field not supported for blueprint creation - Indicates that the given field not supported for Blueprint creation.
From state and to state of the transition seems to be the same state - Indicates that from state and to state of the transition seems to be the same state.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DisconnectedStateError` — Represents the error returned when updates to the Blueprint's connections leave some states no longer connected.
              - `code` (string) **REQ** [enum=['CANNOT_PROCEED']] — Represents the error code returned when a state is not connected to any other state.

Possible values:
CANNOT_PROCEED - Indicates that the request cannot proceed because the state has no connections.
              - `details` (object) **REQ** — Represents the details object with validation information about the disconnected state.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['given state is not connected to any other state']] — Represents the error message returned when a state is not connected to any other state.

Possible values:
given state is not connected to any other state - Indicates that the specified state has no connections to any other state.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DuplicateTransitionNameError` — Represents the error returned when the name of one of the transitions already exists.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when a duplicate transition name is detected.

Possible values:
DUPLICATE_DATA - Indicates that a transition with the same name already exists in the Blueprint.
              - `details` (object) **REQ** — Represents the details object with validation information about the duplicate transition name.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['There is already a transition with the same name used in the blueprint']] — Represents the error message returned when a duplicate transition name is detected.

Possible values:
There is already a transition with the same name used in the blueprint - Indicates that another transition in the Blueprint already uses the same name.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DuplicatePicklistStateError` — Represents the error returned when a state has a picklist value that is already used by another state in the request.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when a duplicate Picklist state is detected.

Possible values:
DUPLICATE_DATA - Indicates that a state using the same Picklist value already exists in the Blueprint.
              - `details` (object) **REQ** — Represents the details object with validation information about the duplicate Picklist state.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when a duplicate Picklist state is detected.

Possible values:
There is already a state with the same pick list value used in the blueprint - Indicates that another state in the Blueprint already uses the same Picklist value.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DuplicateIncludeStateInCommonTransition` — Represents the error returned when a state provided in include_states is already used in the request.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when a state is duplicated in the include_states list of a common transition.

Possible values:
DUPLICATE_DATA - Indicates that the state has already been added to the include_states list.
              - `details` (object) **REQ** — Represents the details object with validation information about the duplicate include state.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['state already added as in include_states for the connection']] — Represents the error message returned when a state is duplicated in the include_states list of a connection.

Possible values:
state already added as in include_states for the connection - Indicates that the specified state is already present in the include_states list for the connection.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `BlueprintLimitExceededError` — Represents the error returned when the maximum number of blueprints allowed to be created has already been reached.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code identifying that the Blueprint limit has been exceeded.

Possible values:
LIMIT_EXCEEDED - Indicates that the maximum number of Blueprints allowed has already been created.
              - `details` (object) **REQ** — Represents the details object that provides validation information about the exceeded Blueprint limit.
                - `limit` (integer/int32) **REQ** — Represents the maximum number of blueprints allowed to be created.
              - `message` (string) **REQ** [enum=['Blueprint limit exceed']] — Represents the error message returned when the Blueprint limit is exceeded.

Possible values:
Blueprint limit exceed - Indicates that the maximum number of Blueprints allowed has already been reached.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DuplicateBlueprintNameError` — Represents the error returned when a Blueprint with the same name already exists.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when the Blueprint name already exists.

Possible values:
DUPLICATE_DATA - Indicates that a Blueprint with the same name already exists.
              - `details` (object) **REQ** — Represents the details object with validation information about the duplicate Blueprint name.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['There is already a blueprint with this name']] — Represents the error message returned when a Blueprint with the same name already exists.

Possible values:
There is already a blueprint with this name - Indicates that another Blueprint is already using the specified name.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `BlueprintNameMissingError` — Represents the error returned when the Blueprint name is not provided in the request.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when the Blueprint name is not provided in the request.

Possible values:
MANDATORY_NOT_FOUND - Indicates that a required field, such as the Blueprint name, was not provided.
              - `details` (object) **REQ** — Represents the details object that provides validation information about the missing Blueprint name.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that is missing from the request.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that is missing from the request.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message returned when the Blueprint name is not provided.

Possible values:
required field not found - Indicates that a required field was not provided in the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `InvalidDataTypeError` — Represents the error returned when the field value does not match the expected data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that invalid data type.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message returned by this response.

Possible values:
Invalid data type - Indicates that invalid data type.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `FieldMaxLengthInvalidDataError` — Represents the error returned when a field value exceeds its maximum allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a field value exceeds its maximum allowed length.

Possible values:
INVALID_DATA - Indicates that the provided data is invalid.
              - `details` (object) **REQ** — Represents the details object with validation information about the field that exceeds its maximum length.
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field value.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['Invalid data', 'invalid data']] — Represents the error message returned when the field value exceeds its maximum allowed length.

Possible values:
Invalid data - Indicates that the provided data is invalid.
invalid data - Indicates that the provided data is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `MandatoryFieldNotFoundError` — Represents the error returned when a mandatory field is not found in the request.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned by this response.

Possible values:
MANDATORY_NOT_FOUND - Indicates that required field is missing.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message returned by this response.

Possible values:
Required field is missing - Indicates that required field is missing.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `InvalidDataRegexError` — Represents the error returned when the field value does not match the required regular expression pattern.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that invalid data.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `regex` (string) **REQ** [maxLen=255] — Represents the regular expression pattern that the field value must match.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned by this response.

Possible values:
Invalid data - Indicates that invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `InvalidDataWithSupportedValuesError` — Represents the error returned when the field value does not match any of the supported values.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that invalid data.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned by this response.

Possible values:
Invalid data - Indicates that invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DependentFieldMissingError` — Represents the error returned when a dependent field is missing from the request.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code returned when a dependent field required by the Blueprint is missing.

Possible values:
DEPENDENT_FIELD_MISSING - Indicates that a field required by a dependent field is missing from the request.
              - `details` (object) **REQ** — Represents the details object with validation information about the missing dependent field.
                - `dependee` (object) **REQ** — Represents the details of the dependee field that is missing.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the dependee field.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the dependee field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that is missing its dependent field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that is missing its dependent field.
              - `message` (string) **REQ** [maxLen=255] — Represents the error message describing which dependent field is missing.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `PostBlueprintAmbiguityDuringProcessingErrorItem` — Represents the error returned when both ID and api_name are provided for a module, layout, or field, causing ambiguity.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code returned by this response.

Possible values:
AMBIGUITY_DURING_PROCESSING - Indicates that ambiguity while processing the request.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `ambiguity_due_to` (array of object) [minItems=2, maxItems=2] **REQ** — Represents the list of fields causing the ambiguity during processing.
                  - `api_name` (string) **REQ** [enum=['id', 'api_name']] — Represents the API name of the invalid field.
                  - `json_path` (string) **REQ** [enum=[6 values]] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message returned by this response.

Possible values:
Ambiguity while processing the request - Indicates that ambiguity while processing the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `CannotProcessStateNotConnectedError` — Represents the error returned when a state in the chart data nodes is not connected to any other state.
              - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the error code returned when a state is not connected to any other state.

Possible values:
CANNOT_PROCESS - Indicates that the request could not be processed because the state is not connected.
              - `details` (object) **REQ** — Represents the details object that identifies the field and its path associated with the unconnected state.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field associated with the error.
              - `message` (string) **REQ** [enum=['given state is not connected to any other state']] — Represents the error message returned when a state is not connected to any other state.

Possible values:
given state is not connected to any other state - Indicates that the specified state has no connections to other states.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `SpecialCharacterNameError` — Represents the error returned when the Blueprint name contains special characters.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that should not contain special characters.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['name']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].name']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['should not contain special characters']] — Represents the error message returned by this response.

Possible values:
should not contain special characters - Indicates that should not contain special characters.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `TransitionAlreadyAssociatedError` — Represents the error returned when the given transition is already associated with another Blueprint.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the request contains invalid or unexpected data.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].connections[0].transitions.id']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['the given transition is already associated with another blueprint']] — Represents the error message returned by this response.

Possible values:
the given transition is already associated with another blueprint - Indicates that the given transition is already associated with another Blueprint.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `TransitionDifferentModuleError` — Represents the error returned when the given transition belongs to a different module and cannot be associated with this Blueprint.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the given transition belongs to a different module and cannot be associated with this Blueprint.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].connections[0].transitions.id']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned by this response.

Possible values:
the given transition belongs to a different module and cannot be associated with this blueprint - Indicates that the given transition belongs to a different module and cannot be associated with this Blueprint.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `NotAllowedSlaTerminalStateError` — Represents the error returned when an SLA is configured on a terminal state that has no outgoing transitions.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that sLA cannot be configured for a terminal (leaf) state that has no outgoing transitions.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].connections[0].to_state.id']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned by this response.

Possible values:
SLA cannot be configured for a terminal (leaf) state that has no outgoing transitions - Indicates that sLA cannot be configured for a terminal (leaf) state that has no outgoing transitions.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `WidgetDuringFieldContinuousBlueprintError` — Represents the error returned when a widget during field is configured for a continuous Blueprint transition, which is not allowed.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that widget during field cannot be configured for a continuous Blueprint transition.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned by this response.

Possible values:
Widget during field cannot be configured for a continuous blueprint transition - Indicates that widget during field cannot be configured for a continuous Blueprint transition.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DependentMismatchPipelineStateError` — Represents the error returned when the given state does not belong to the specified pipeline.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when the specified pipeline state does not match its dependent field.

Possible values:
DEPENDENT_MISMATCH - Indicates that the given state option does not belong to the specified pipeline.
              - `details` (object) **REQ** — Represents the details object with the dependee and field path information.
                - `dependee` (object) **REQ** — Represents the details of the field this error depends on.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the dependee field.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the dependee field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['The given state option does not belong to the specified pipeline']] — Represents the error message returned when the given state option does not belong to the specified pipeline.

Possible values:
The given state option does not belong to the specified pipeline - Indicates that the state selected for the field is not part of the associated pipeline.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `ConvertActionTerminalStateError` — Represents the error returned when a convert action is associated with a transition whose target state is not a terminal state.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when a convert action is associated with a transition whose target state is not a terminal state.

Possible values:
NOT_ALLOWED - Indicates that the convert action is not allowed because the target state is not a terminal state.
              - `details` (object) **REQ** — Represents the details object that identifies the invalid field and its path.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when a convert action is associated with a transition whose target state is not a terminal state.

Possible values:
convert action can only be associated with transitions whose target state is a terminal (leaf) state - Indicates that the convert action is only valid for transitions ending in a terminal state.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `RequiredHeaderMissingError` — Represents the error returned when the required X-CRM-ORG header is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_HEADER_MISSING']] — Represents the error code returned by this response.

Possible values:
REQUIRED_HEADER_MISSING - Indicates that one of the expected headers is missing.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `header_name` (string) **REQ** [maxLen=255] — Represents the name of the missing header.
        - `message` (string) **REQ** [enum=['One of the expected headers is missing']] — Represents the error message returned by this response.

Possible values:
One of the expected headers is missing - Indicates that one of the expected headers is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `PostBlueprintMaxBlueprintsInvalidDataError` — Represents the error returned when more than one Blueprint object is provided in the create Blueprint request.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that invalid data.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `maximum_length` (integer/int32) **REQ** [enum=[1]] — Represents the maximum allowed length for the field value.
          - `api_name` (string) **REQ** [enum=['blueprints']] — Represents the API name of the invalid field.
          - `json_path` (string) **REQ** [enum=['$.blueprints']] — Represents the JSON path of the invalid field.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned by this response.

Possible values:
invalid data - Indicates that invalid data.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to create a Blueprint. Resolution: The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
    > Represents the error returned when the user does not have permission to perform this action.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned by this response.

Possible values:
NO_PERMISSION - Indicates that the request contains invalid or unexpected data.
    - `details` (object) **REQ** — Represents the details object with validation information about the error.
      - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to perform this action.
        items: [maxLen=100]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message returned by this response.

Possible values:
permission denied - Indicates that permission denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.CREATE
