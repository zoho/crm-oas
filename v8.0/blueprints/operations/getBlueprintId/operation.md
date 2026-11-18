# GET /settings/blueprints/{blueprintId}
**Operation:** `getBlueprintId` — Get details of a Blueprint by ID
> To get the details of a single Blueprint by its unique identifier in your Zoho CRM organization, send a GET request with the target Blueprint ID. The response includes the full Blueprint record with chart data, states, transitions, connections, layout, tracked field, associated module, and ownership information.

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+] {style=simple, explode=False}: Specify the unique numeric ID of the Blueprint to retrieve. Use the [Get Blueprint by ID](blueprints.yaml#$.paths./settings/blueprints.get) to retrieve the Blueprint ID.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Represents the custom header used to identify the calling service.
- `include` (query, string, optional) [enum=['state', 'transition']] {style=form, explode=True}: Represents the additional fields to include in the response on demand.

**Responses:**

- **200**: Returns a blueprints array containing the full details of the specified Blueprint, including chart data, states, transitions, connections, layout, tracked field, module, name, description, API name, created_by, modified_by, and owner. — Schema: `GetSingleBlueprintResponse` [application/json]
    > Represents the response returned when the Blueprint is successfully retrieved.
    schema: `GetSingleBlueprintResponse`
    - `blueprints` (array of object `PutBlueprintDetailItem`) [maxItems=1] **REQ** — Represents the list containing the Blueprint returned in the response.
      schema: `PutBlueprintDetailItem`
      - `owner` (object) **REQ** — Represents the owner of the Blueprint.
        oneOf:
            type: array of object `OwnerItemBase` [maxItems=25]
              schema: `OwnerItemBase`
              - `resources` (array of object `ChartDataBase3`) [maxItems=25, nullable] — Represents the list of resources associated with the owner.
                schema: `ChartDataBase3`
                - `id` (string) [maxLen=255] — Represents the unique ID of the resource.
                additionalProperties: any
              - `type` (string) [maxLen=255] — Represents the type of the owner.
              additionalProperties: any
            type: null — Null value for owner field
      - `created_time` (string) **REQ** [maxLen=255] — Represents the date and time of the Blueprint's creation.
      - `chart_data` (object) **REQ**
        oneOf:
          - `PutBlueprintChartData` — Represents the chart data configured for the Blueprint.
            - `nodes` (array of object `BlueprintNodeDetail`) [maxItems=12] **REQ** — Represents the list of nodes in the Blueprint chart data.
              schema: `BlueprintNodeDetail`
              - `position_x` (number/double) **REQ** — Represents the x-axis position of the node in the Blueprint diagram.
              - `position_y` (number/double) **REQ** — Represents the y-axis position of the node in the Blueprint diagram.
              - `state` (object `ChartDataBase1`) **REQ** — Represents the state associated with the Blueprint node.
                schema: `ChartDataBase1`
                - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the state.
            - `canvas_size` (object `CanvasSizeSpec`) **REQ** — Represents the dimensions of the Blueprint canvas.
              schema: `CanvasSizeSpec`
              - `width` (integer/int32) **REQ** — Represents the width of the Blueprint canvas.
              - `height` (integer/int32) **REQ** — Represents the height of the Blueprint canvas.
            - `connections` (array of object `ConnectionItemFull`) [maxItems=11] **REQ** — Represents the list of connections in the Blueprint chart data.
              schema: `ConnectionItemFull`
              - `from` (object `ConnectionSourceNode`) **REQ** — Represents the source state of a connection.
                schema: `ConnectionSourceNode`
                - `end_point` (object `NodeEndPointDetail`) **REQ** — Represents the connector anchor point for a Blueprint chart connection, defined by one of the valid endpoint tuples of position and direction values.
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
                - `state` (object `TransitionStateRef`) **REQ** — Represents the state referenced in the transition.
                  schema: `TransitionStateRef`
                  - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the state.
              - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the connection.
              - `to` (object `ConnectionTargetNode`) **REQ** — Represents the target state of a connection.
                schema: `ConnectionTargetNode`
                - `end_point` (object `ChartEndPoint`) **REQ** — Represents the endpoint details of a connection in the Blueprint chart.
                  schema: `ChartEndPoint`
                  - `position_x` (number/double) **REQ** — Represents the x-axis position of the connection endpoint in the Blueprint chart.
                  - `position_y` (number/double) **REQ** — Represents the y-axis position of the connection endpoint in the Blueprint chart.
                  - `direction_x` (number/double) **REQ** — Represents the x-axis direction of the connection endpoint in the Blueprint chart.
                  - `direction_y` (number/double) **REQ** — Represents the y-axis direction of the connection endpoint in the Blueprint chart.
                - `state` (object `StateIdReference`) **REQ** — Represents the state referenced in the Blueprint.
                  schema: `StateIdReference`
                  - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the state.
              - `transition` (object `TransitionReference`) **REQ** — Represents the transition referenced in the Blueprint.
                schema: `TransitionReference`
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the transition.
                - `name` (string) **REQ** [maxLen=255] — Represents the name of the transition.
                - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the transition.
          - `ChartDataNullValue` (null) — Represents the null value returned when no chart data is configured for the Blueprint.
      - `module` (object `BlueprintModuleInfo`) **REQ** — Represents the details of the module associated with the Blueprint.
        schema: `BlueprintModuleInfo`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module associated with the Blueprint.
        - `_precedence` (integer/int32) **REQ** — Represents the precedence order assigned to the module in the Blueprint.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the module associated with the Blueprint.
      - `description` (string) **REQ** [maxLen=255] — Represents the description of the Blueprint.
      - `created_by` (object `CreatedByReference`) **REQ** — Represents the details of the user who created the Blueprint.
        schema: `CreatedByReference`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the Blueprint.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who created the Blueprint.
      - `layout` (object `PutLayoutDetail`) **REQ** — Represents the layout details for which the Blueprint is configured.
        schema: `PutLayoutDetail`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the layout.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the layout.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the layout.
      - `modified_time` (string) **REQ** [maxLen=255] — Represents the date and time when the Blueprint was last modified.
      - `field` (object `PutFieldReference`) **REQ** — Represents the field details referenced in the Blueprint.
        schema: `PutFieldReference`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field.
        - `field_label` (string) **REQ** [maxLen=255] — Represents the label of the field.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the field.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the Blueprint.
      - `continuous` (boolean) **REQ** — Indicates whether the Blueprint is continuous.
      - `criteria` (object `BlueprintEntryCriteriaResponse`) — Contains details of blueprint entry criteria
        schema: `BlueprintEntryCriteriaResponse`
        - `comparator` (string) [maxLen=12, nullable] — Represents the comparator used to evaluate the criteria field against its configured value.
        - `field` (object `CriteriaFieldResponseDetail`) — Contains field details of criteria
          schema: `CriteriaFieldResponseDetail`
          - `id` (string) **REQ** [maxLen=25, pattern=[0-9]+] — Represents the unique ID of the field for which the Blueprint is configured.
          - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the field for which the Blueprint is configured.
          - `field_label` (string) [maxLen=100, nullable] — Represents the label of the field for which the Blueprint is configured.
        - `type` (string) [maxLen=100, nullable] — Represents the type of criteria used to determine whether a record satisfies the Blueprint entry conditions.
        - `value` (string) [maxLen=3, nullable] — Represents the value configured for the criteria field used to evaluate the Blueprint entry condition.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the Blueprint.
      - `modified_by` (object `BlueprintModifiedByDetail`) **REQ** — Represents the details of the user who last modified the Blueprint.
        schema: `BlueprintModifiedByDetail`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified the Blueprint.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who last modified the Blueprint.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the Blueprint.
      - `connections` (array of object `ConnectionGetItem`) [maxItems=11] **REQ** — Represents the list of connections in the Blueprint.
        schema: `ConnectionGetItem`
        - `from_state` (object `FromStateReferenceItem`) **REQ** — Represents the from state of a connection.
          schema: `FromStateReferenceItem`
          - `api_name` (string) [maxLen=255] — Represents the API name of the from state.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the from state.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the from state.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the connection.
        - `transitions` (object `BlueprintTransitionListItem`) **REQ** — Represents an individual transition in the Blueprint list.
          schema: `BlueprintTransitionListItem`
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the transition.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the transition.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the transition.
          - `precedence` (integer/int32) **REQ** — Represents the precedence order of the transition.
          - `common` (boolean) — Indicates whether the transition is configured as a common transition.
        - `to_state` (object `ToStateReferenceItem`) **REQ** — Represents the to state of a connection.
          schema: `ToStateReferenceItem`
          - `api_name` (string) [maxLen=255] — Represents the API name of the to state.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the to state.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the to state.
      - `pipeline` (object `PipelineReference`) — Contains details of the pipeline for which blueprint is configured
        schema: `PipelineReference`
        - `name` (string) [maxLen=255, nullable] — Represents the name of the pipeline.
        - `display_value` (string) [maxLen=100, nullable] — Represents the display value of the pipeline.
        - `id` (string) **REQ** [maxLen=25, pattern=[0-9]+] — Represents the unique ID of the pipeline.
        - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the pipeline.
      - `states` (array of object `GetBlueprintStateItem`) [maxItems=301] — Represents the list of states associated with the Blueprint.
        schema: `GetBlueprintStateItem`
        - `sla_configured` (boolean) **REQ** — Indicates whether an SLA is configured for the state.
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the state.
        - `name` (string) **REQ** [maxLen=100] — Represents the name of the state.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the state.
        - `unsupported_features_present` (boolean) **REQ** — Indicates whether the state contains features that are not supported.
      - `transitions` (array of object `GetBlueprintTransitionItem`) [maxItems=301] — Represents the list of transitions associated with the Blueprint.
        schema: `GetBlueprintTransitionItem`
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the transition.
        - `trigger_type` (string) **REQ** [maxLen=10, enum=['manual', 'automatic']] — Represents the trigger type of the transition.

Possible values:
manual - Indicates that the transition is triggered manually by a user.
automatic - Indicates that the transition is triggered automatically.
        - `name` (string) **REQ** [maxLen=100] — Represents the name of the transition.
        - `transition_type` (string) **REQ** [maxLen=25, enum=['standalone_transition', 'parallel_transition', 'child_transition']] — Represents the type of the transition.

Possible values:
standalone_transition - Indicates that the transition is independent and not part of a parallel or child structure.
parallel_transition - Indicates that the transition runs in parallel with other transitions.
child_transition - Indicates that the transition is a child of a parallel transition.
        - `global` (boolean) **REQ** — Indicates whether the transition is a global transition.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the transition.
        - `parallel_transition_id` (string) [maxLen=255] — Represents the unique ID of the parallel transition associated with this transition.
        - `colour_code` (string) **REQ** [maxLen=50] — Represents the color code assigned to the transition.
        - `special_features` (array of string) [maxItems=25] — Represents the list of special features associated with the transition.
          items: [maxLen=255]
        - `unsupported_features_present` (boolean) **REQ** — Indicates whether the transition contains features that are not supported.
        - `common` (boolean) — Indicates whether the transition is a common transition. Present only when true.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Returns no content when the request is successful but there is no Blueprint record to return.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: One of the expected headers is missing.
**Resolution:** All required headers must be included in the request. Verify the request headers and retry. — Schema: `RequiredHeaderMissingError` [application/json]
    > Represents the error returned when the required X-CRM-ORG header is missing from the request.
    schema: `RequiredHeaderMissingError`
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
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied.
**Resolution:** The CRM administrator must grant the Crm_Implied_Manage_Workflow permission to the user profile in Zoho CRM. — Schema: `NoPermissionError` [application/json]
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

**Scopes:** ZohoCRM.settings.blueprint.READ
