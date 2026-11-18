# PUT /settings/blueprints
**Operation:** `putBlueprint` — Update Blueprints
> To update bulk Blueprint configurations. Each Blueprint in the `blueprints` array is replaced with the submitted definition. Use the [Get Blueprint by ID API](blueprints.yaml#$.paths./settings/blueprints.get) to retrieve the Blueprint ID. If the ID is not included in the URL, then it is mandatory to specify the ID in the request body. **Restriction:** Blueprints that have ever been published (activated) cannot be updated directly — even after deactivation. To modify a published Blueprint, clone it as a dependent draft (the source must be active and include `chart_data`), edit the draft, then activate it with `move_records` and `map_states`.

**Parameters:**
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Represents the custom header used to identify the calling service.

**Schemas:**
`ActionDetails`:
  > Represents the details of the object referenced by the transition action, such as a tag, record, or webhook, depending on the configured action type.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the object referenced by this action, such as a tag or webhook, depending on the configured action type.
  - `id` (string) [maxLen=255] — Represents the unique ID of the object referenced by this action, such as a tag, record, or webhook, depending on the configured action type.
  additionalProperties: any
`CrossModuleNodeMappingError`:
  > Represents the error returned when a state from a different module or layout is mapped to a node of this Blueprint.
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
`DeleteBlueprintStatusItem`:
  > Represents an individual Blueprint's deletion status.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code indicating the outcome of the Blueprint deletion.

Possible values:
SUCCESS - Indicates that the Blueprint deletion completed successfully.
  - `details` (object `ActionDetails`) **REQ** — Represents the details of the object referenced by the transition action, such as a tag, record, or webhook, depending on the configured action type.
  - `message` (string) **REQ** [maxLen=255] — Represents the message describing the outcome of the Blueprint deletion.
  - `status` (string) **REQ** [maxLen=255] — Represents the status of the Blueprint deletion operation.
`DependentMismatchConnectionError`:
  > Represents the error returned when a transition from a different module or layout is mapped to a connection of this Blueprint.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when a connection's dependent field values do not match.

Possible values:
DEPENDENT_MISMATCH - Indicates that the dependent field values of the connection do not match the expected configuration.
  - `details` (object) **REQ** — Represents the details object with validation information about the mismatched dependent connection.
    - `dependee` (object) **REQ** — Represents the details of the dependee field that caused the mismatch.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the dependee field.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the dependee field.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with the mismatched dependent value.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field with the mismatched dependent value.
  - `message` (string) **REQ** [enum=['The module or layout of this transition is different from the blueprint']] — Represents the error message returned when a connection's dependent field values do not match.

Possible values:
The module or layout of this transition is different from the blueprint - Indicates that the transition's module or layout does not match the Blueprint's configuration.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
`DependentMismatchPipelineStateError`:
  > Represents the error returned when the given state does not belong to the specified pipeline.
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
`DisconnectedStateError`:
  > Represents the error returned when updates to the Blueprint's connections leave some states no longer connected.
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
`DuplicateBlueprintNameError`:
  > Represents the error returned when a Blueprint with the same name already exists.
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
`DuplicateNameFieldError`:
  > Represents the error returned when the specified name value is a duplicate of an existing one.
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
`FieldMaxLengthInvalidDataError`:
  > Represents the error returned when a field value exceeds its maximum allowed length.
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
`InvalidCriteriaUpdateError`:
  > Represents the error returned when the updated criteria is invalid.
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
`InvalidDataRegexError`:
  > Represents the error returned when the field value does not match the required regular expression pattern.
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
`InvalidDataTypeError`:
  > Represents the error returned when the field value does not match the expected data type.
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
`InvalidDataWithSupportedValuesError`:
  > Represents the error returned when the field value does not match any of the supported values.
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
`MandatoryFieldNotFoundError`:
  > Represents the error returned when a mandatory field is not found in the request.
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
`OrphanConnectionError`:
  > Represents the error returned when the source and target nodes of a connection no longer exist but the connection itself remains.
  - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the error code returned by this response.

Possible values:
CANNOT_PROCESS - Indicates that the state no longer exists but transitions connecting the state remain.
  - `details` (object) **REQ** — Represents the details object with validation information about the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
  - `message` (string) **REQ** [enum=['the state is deleted but transitions connecting the state are not deleted']] — Represents the error message returned by this response.

Possible values:
the state is deleted but transitions connecting the state are not deleted - Indicates that the state no longer exists but transitions connecting the state remain.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
`OrphanStateConnectionError`:
  > Represents the error returned when the only connection linking a state node no longer exists but the state remains.
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

**Request Body** — application/json `PutBlueprintsBulkRequestBody`
> Request body containing the list of blueprints to update. Each object in the `blueprints` array represents a complete Blueprint definition including its states, connections, transitions, owners, criteria, and pipeline configuration.
  > Represents the request body used to update multiple blueprints in bulk.
  - `blueprints` (array of object `BlueprintPutRequestItem`) [maxItems=1] **REQ** — Represents the list of blueprints to be updated.
    schema: `BlueprintPutRequestItem`
    - `chart_data` (object `ChartDataBase`) — Represents the chart data of the Blueprint, including its nodes and connections.
      schema: `ChartDataBase`
      - `nodes` (array of object `NodesItemBase`) [maxItems=25] — Represents the list of state nodes in the Blueprint chart.
        schema: `NodesItemBase`
        - `position_x` (integer/int32) — Represents the horizontal position of the node on the canvas.
        - `position_y` (integer/int32) — Represents the vertical position of the node on the canvas.
        - `state` (object `PostActionStateBase`) — Represents the post action state of the Blueprint.
          schema: `PostActionStateBase`
          - `api_name` (string) [maxLen=255] — Represents the API name of the post action state.
          additionalProperties: any
        additionalProperties: any
      - `connections` (array of object `GetConnectionsItemBase`) [maxItems=25] — Represents the list of connections between nodes in the Blueprint chart.
        schema: `GetConnectionsItemBase`
        - `api_name` (string) [maxLen=255] — Represents the API name of the connection.
        - `from` (object `PutConnectionFromBase`) — Represents the from state details of a connection.
          schema: `PutConnectionFromBase`
          - `end_point` (object `TriggerEndPointBase`) — Represents the endpoint configured for the trigger.
            schema: `TriggerEndPointBase`
            - `position_x` (number) — Represents the horizontal anchor position on the node boundary.
            - `position_y` (integer/int32) — Represents the vertical anchor position on the node boundary.
            - `direction_x` (integer/int32) — Represents the horizontal exit direction of the connector.
            - `direction_y` (integer/int32) — Represents the vertical exit direction of the connector.
            additionalProperties: any
          - `state` (object `ChartDataBase6`) — Represents the details of the state.
            schema: `ChartDataBase6`
            - `api_name` (string) [maxLen=255] — Represents the API name of the state.
            additionalProperties: any
          additionalProperties: any
        - `to` (object `ConnTargetBase`) — Represents the target state of a connection.
          schema: `ConnTargetBase`
          - `end_point` (object `EndPointItemBase`) — Represents the connector anchor point for a Blueprint chart connection, defined by one of the valid endpoint tuples of position and direction values.
            - `position_x` (number/double) [enum=[0, 0.12, 0.21, 0.3, 0.4, 0.5, 0.6, 0.7, 0.79, 0.88, 1]] — Represents the horizontal anchor position on the node boundary.
            - `position_y` (number/double) [enum=[0, 0.5, 1]] — Represents the vertical anchor position on the node boundary.
            - `direction_x` (number/double) [enum=[0]] — Represents the horizontal exit direction of the connector. Always 0 in all valid endpoint combinations.
            - `direction_y` (number/double) [enum=[-1, 0, 1]] — Represents the vertical exit direction of the connector.
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
          - `state` (object `TriggerStateBase`) — Represents the state configured for the trigger.
            schema: `TriggerStateBase`
            - `api_name` (string) [maxLen=255] — Represents the API name of the state.
            additionalProperties: any
          additionalProperties: any
        - `transition` (object `TransitionItemBase`) — Represents a transition configured in the Blueprint.
          schema: `TransitionItemBase`
          - `api_name` (string) [maxLen=255] — Represents the API name of the transition.
          - `name` (string) [maxLen=255] — Represents the name of the transition.
          additionalProperties: any
        additionalProperties: any
      additionalProperties: any
    - `criteria` (object `CriteriaBase`) — Represents the base criteria configuration.
      schema: `CriteriaBase`
      - `comparator` (string) [maxLen=255] — Represents the comparator used to evaluate the criteria.
      - `field` (object `TransitionFieldBase`) — Represents the field configured for the transition.
        schema: `TransitionFieldBase`
        - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents the API name of the field.
        - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Represents the unique ID of the field.
        additionalProperties: any
      - `type` (string) [maxLen=255] — Represents the type of criteria used to determine whether a record satisfies the Blueprint entry conditions.
      - `value` (string) [maxLen=255] — Represents the value configured for the criteria field used to evaluate the Blueprint entry condition.
      additionalProperties: any
    - `continuous` (boolean) — Indicates whether the subform is continuous.
    - `name` (string) **REQ** [maxLen=255] — Field: name
    - `description` (string) [maxLen=255] — Represents the description of the subform.
    - `owners` (array of object `BlueprintPutOwnerItem`) [maxItems=25] — Represents the list of owners of the subform.
      schema: `BlueprintPutOwnerItem`
      - `resources` (array of object) [maxItems=25, nullable] — Represents the list of resource details configured for the Blueprint owner.
        anyOf:
          - `BlueprintUserOwnerResource` — Represents the user configured as the owner of the Blueprint or transition.
            - `id` (string) [maxLen=30, nullable] — Represents the unique ID of the user configured as the owner of the Blueprint or transition.
          - `BlueprintRoleOwnerResource` — Represents the role configured as the owner of the Blueprint or transition.
            - `id` (string) [maxLen=30, nullable] — Represents the unique ID of the role configured as the owner of the Blueprint or transition.
          - `BlueprintGroupOwnerResource` — Represents the group configured as the owner of the Blueprint or transition.
            - `id` (string) [maxLen=30, nullable] — Represents the unique ID of the group configured as the owner of the Blueprint or transition.
          - `BlueprintOwnerResource` — Represents the resource details of the Blueprint owner.
            - `id` (string) **REQ** [maxLen=25, pattern=[0-9]+] — Represents the unique ID of the Blueprint owner.
      - `type` (string) [maxLen=255] — Represents the type of owner configured for the Blueprint.
      additionalProperties: any
    - `id` (string) [maxLen=255] — Represents the unique ID of the subform.
    - `connections` (array of object `PutConnectionItemBase`) [maxItems=25] — Represents the list of connections in the subform.
      schema: `PutConnectionItemBase`
      - `from_state` (object `FromStateBase`) — Represents the from state of a connection.
        schema: `FromStateBase`
        - `api_name` (string) [maxLen=255] — Represents the API name of the from state.
        - `name` (string) [maxLen=255] — Represents the name of the from state.
        additionalProperties: any
      - `api_name` (string) [maxLen=255] — Represents the API name of the connection.
      - `id` (string) [maxLen=255] — Represents the unique ID of the connection.
      - `_delete` (string) [maxLen=255, nullable] — Represents the flag used to mark the connection for deletion.
      - `transitions` (object `TransitionsBase`) — Represents the transitions configured in the Blueprint.
        schema: `TransitionsBase`
        - `api_name` (string) [maxLen=255] — Represents the API name of the transition.
        - `name` (string) [maxLen=255] — Represents the name of the transition.
        - `precedence` (integer/int32) — Represents the precedence of the transition.
        additionalProperties: any
      - `to_state` (object `ToStateBase`) — Represents the to state of a connection.
        schema: `ToStateBase`
        - `api_name` (string) [maxLen=255] — Represents the API name of the to state.
        - `name` (string) [maxLen=255] — Represents the name of the to state.
        additionalProperties: any
      additionalProperties: any
    additionalProperties: any

**Responses:**

- **200**: All blueprints in the request were updated successfully. The response body contains the updated Blueprint records. — Schema: `PutBlueprintListResponse` [application/json]
    > Represents the response returned when the list of blueprints is successfully updated.
    schema: `PutBlueprintListResponse`
    - `blueprints` (array of object) [maxItems=2] — Represents the list of blueprints returned in the response.
      oneOf:
        - `DeleteBlueprintStatusItem` — Represents an individual Blueprint's deletion status.
        - `ChartDataBase4` — Represents the list of blueprints returned in the response.
          - `blueprints` (array of object `DeleteBlueprintStatusItem`) [maxItems=1] — Represents the list of blueprints.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Some blueprints were updated successfully while others failed validation. The response body lists both successful updates and the corresponding validation errors for the failed blueprints. — Schema: `PutBlueprintPartialResponse` [application/json]
    > Represents the response returned when some blueprints are not updated due to errors in the request.
    schema: `PutBlueprintPartialResponse`
    - `blueprints` (array of object) [maxItems=100] — Represents the list of blueprints returned in the response.
      oneOf:
        - `DeleteBlueprintStatusItem` — Represents an individual Blueprint's deletion status.
        - `DependentMismatchConnectionError` — Represents the error returned when a transition from a different module or layout is mapped to a connection of this Blueprint.
        - `CrossModuleNodeMappingError` — Represents the error returned when a state from a different module or layout is mapped to a node of this Blueprint.
        - `DisconnectedStateError` — Represents the error returned when updates to the Blueprint's connections leave some states no longer connected.
        - `InvalidCriteriaUpdateError` — Represents the error returned when the updated criteria is invalid.
        - `DuplicateBlueprintNameError` — Represents the error returned when a Blueprint with the same name already exists.
        - `OrphanConnectionError` — Represents the error returned when the source and target nodes of a connection no longer exist but the connection itself remains.
        - `OrphanStateConnectionError` — Represents the error returned when the only connection linking a state node no longer exists but the state remains.
        - `DuplicateNameFieldError` — Represents the error returned when the specified name value is a duplicate of an existing one.
        - `InvalidDataTypeError` — Represents the error returned when the field value does not match the expected data type.
        - `FieldMaxLengthInvalidDataError` — Represents the error returned when a field value exceeds its maximum allowed length.
        - `InvalidDataRegexError` — Represents the error returned when the field value does not match the required regular expression pattern.
        - `MandatoryFieldNotFoundError` — Represents the error returned when a mandatory field is not found in the request.
        - `InvalidDataWithSupportedValuesError` — Represents the error returned when the field value does not match any of the supported values.
        - `DependentMismatchPipelineStateError` — Represents the error returned when the given state does not belong to the specified pipeline.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request body is invalid or contains Blueprint-level validation errors. No blueprints were updated. Check the response body for specific error codes and field paths. [application/json]
    oneOf:
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
        - `blueprints` (array of object) [maxItems=100] **REQ** — Array of Blueprint-specific error objects, one per Blueprint that failed validation. Each item identifies the Blueprint and the error that prevented the update. Maximum 100 items.
          oneOf:
            - `DependentMismatchConnectionError` — Represents the error returned when a transition from a different module or layout is mapped to a connection of this Blueprint.
            - `CrossModuleNodeMappingError` — Represents the error returned when a state from a different module or layout is mapped to a node of this Blueprint.
            - `DisconnectedStateError` — Represents the error returned when updates to the Blueprint's connections leave some states no longer connected.
            - `InvalidCriteriaUpdateError` — Represents the error returned when the updated criteria is invalid.
            - `DuplicateBlueprintNameError` — Represents the error returned when a Blueprint with the same name already exists.
            - `OrphanConnectionError` — Represents the error returned when the source and target nodes of a connection no longer exist but the connection itself remains.
            - `OrphanStateConnectionError` — Represents the error returned when the only connection linking a state node no longer exists but the state remains.
            - `InvalidBlueprintIdPutError` — Represents the error returned when the Blueprint ID provided in the request is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the ID given seems to be invalid.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned by this response.

Possible values:
the id given seems to be invalid - Indicates that the ID given seems to be invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `DuplicateNameFieldError` — Represents the error returned when the specified name value is a duplicate of an existing one.
            - `InvalidDataTypeError` — Represents the error returned when the field value does not match the expected data type.
            - `FieldMaxLengthInvalidDataError` — Represents the error returned when a field value exceeds its maximum allowed length.
            - `InvalidDataRegexError` — Represents the error returned when the field value does not match the required regular expression pattern.
            - `MandatoryFieldNotFoundError` — Represents the error returned when a mandatory field is not found in the request.
            - `InvalidDataWithSupportedValuesError` — Represents the error returned when the field value does not match any of the supported values.
            - `NotAllowedBulkBlueprintUpdateErrorItem` — Represents the error returned for each active Blueprint entry in the bulk update API.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that published Blueprint cannot be updated.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].id']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['Published blueprint cannot be updated']] — Represents the error message returned by this response.

Possible values:
Published blueprint cannot be updated - Indicates that published Blueprint cannot be updated.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `NotAllowedBulkBlueprintModuleUpdateErrorItem` — Represents the error returned when module data is attempted to be updated through the bulk Blueprint update API.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that module cannot be updated.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprint[0].module.id']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['module cannot be updated']] — Represents the error message returned by this response.

Possible values:
module cannot be updated - Indicates that module cannot be updated.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `NotAllowedLayoutUpdateError` — Represents the error returned when layout data is attempted to be updated through the Blueprint update API.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that layout cannot be updated.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['layout']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].layout']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['layout cannot be updated']] — Represents the error message returned by this response.

Possible values:
layout cannot be updated - Indicates that layout cannot be updated.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `NotAllowedFieldUpdateError` — Represents the error returned when field data is attempted to be updated through the Blueprint update API.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that field cannot be updated.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['field']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].field']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['field cannot be updated']] — Represents the error message returned by this response.

Possible values:
field cannot be updated - Indicates that field cannot be updated.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `NotAllowedModuleUpdateError` — Represents the error returned when module data is attempted to be updated through the Blueprint update API.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that module cannot be updated.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['module']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].module']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['module cannot be updated']] — Represents the error message returned by this response.

Possible values:
module cannot be updated - Indicates that module cannot be updated.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `NotAllowedPipelineUpdateError` — Represents the error returned when pipeline data is attempted to be updated through the Blueprint update API.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned by this response.

Possible values:
NOT_ALLOWED - Indicates that pipeline cannot be updated.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['pipeline']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].pipeline']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['pipeline cannot be updated']] — Represents the error message returned by this response.

Possible values:
pipeline cannot be updated - Indicates that pipeline cannot be updated.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `PipelineEmptyInvalidDataError` — Represents the error returned when the pipeline value is empty during the Blueprint update API.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that pipeline cannot be empty.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['pipeline']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=['$.blueprints[0].pipeline']] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['pipeline cannot be empty']] — Represents the error message returned by this response.

Possible values:
pipeline cannot be empty - Indicates that pipeline cannot be empty.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
            - `InvalidStateConnectionError` — Represents the error returned when the from_state or to_state ID in a connection is invalid or does not belong to the Blueprint.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the given state is either invalid or does not belong to this Blueprint.
              - `details` (object) **REQ** — Represents the details object with validation information about the error.
                - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [enum=[2 values]] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['the given state is either invalid or does not belong to this blueprint']] — Represents the error message returned by this response.

Possible values:
the given state is either invalid or does not belong to this blueprint - Indicates that the given state is either invalid or does not belong to this Blueprint.
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
            - `DeletedConnectionNotUpdatedError` — Represents the error returned when a deleted connection has not been reflected in the chart data.
              - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the error code returned when a deleted connection is not updated in the chart data.

Possible values:
CANNOT_PROCESS - Indicates that the request could not be processed due to the state of the data.
              - `details` (object) **REQ** — Represents the details object identifying the stale connection field and its path.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
              - `message` (string) **REQ** [enum=['deleted connection not updated in chart data']] — Represents the error message returned when a deleted connection is not updated in the chart data.

Possible values:
deleted connection not updated in chart data - Indicates that a connection removed from the chart data was not reflected consistently.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The OAuth token does not have the required scope (`ZohoCRM.settings.blueprint.ALL` or `ZohoCRM.settings.blueprint.UPDATE`) to update blueprints. — Schema: `NoPermissionError` [application/json]
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

**Scopes:** ZohoCRM.settings.blueprint.UPDATE
