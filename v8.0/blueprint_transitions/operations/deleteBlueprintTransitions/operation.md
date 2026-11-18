# DELETE /settings/blueprints/transitions
**Operation:** `deleteBlueprintTransitions` — Blueprint Transitions
> Delete multiple blueprint transitions by IDs in the request body

**Parameters:**
- `ids` (query, array, required) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Represents a comma-separated list (CSV) of unique transition IDs used to retrieve specific blueprint transition configurations.

**Schemas:**
`InvalidTransitionIdentifiersError`:
  > Represents the error response returned when one or more of the provided transition IDs are invalid. The response includes the error code **INVALID_DATA**, a message, a status, and details describing the invalid identifiers.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the supplied identifiers are invalid. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information.
    - `id` (string) **REQ** [maxLen=255] — Represents the invalid identifier reported in the error details.
  - `message` (string) **REQ** [enum=['the ids given seems to be invalid', 'the id given seems to be invalid']] — Represents the error message returned when the supplied identifiers are invalid. Possible values: **the ids given seems to be invalid**, **the id given seems to be invalid**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TransitionRemovalDetail`:
  > Contains the minimal details of a transition referenced in a removal result, including the unique ID of the transition.
  - `id` (string) [maxLen=255] — Represents the unique identifier of the transition included in the removal detail.
`TransitionRemovalNotAllowedError`:
  > Represents the error payload returned when a transition cannot be removed because it is still associated with a blueprint, including the places where the transition remains in use.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when the transition removal is not allowed. Possible values: **NOT_ALLOWED**.
  - `details` (object) **REQ** — Contains the error details object with validation information for the transition removal that is not allowed.
    - `id` (string) **REQ** [maxLen=255] — Represents the ID of the transition that cannot be deleted while it is associated with a blueprint.
    - `associated_places` (array of object) [maxItems=25] **REQ** — Contains the places where the transition is still associated, which prevent its removal.
      - `resource` (object) **REQ** — Represents the resource in which the transition is still associated.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the resource in which the transition is associated.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the resource in which the transition is still associated.
      - `type` (string) **REQ** [maxLen=255] — Indicates the type of the associated place where the transition is in use.
  - `message` (string) **REQ** [enum=['Remove the transtion from the associated blueprint and then delete']] — Represents the error message returned when the transition cannot be deleted because it is associated with a blueprint. Possible values: **Remove the transtion from the associated blueprint and then delete**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TransitionRemovalResultItem`:
  > Represents the per-transition outcome for the transitions settings operation, providing a status code, message, and detail reference for the affected transition.
  - `code` (string) [maxLen=255, enum=['SUCCESS']] — Represents the result code for the removal of the transition. Possible values: **SUCCESS**.
  - `details` (object `TransitionRemovalDetail`) — Contains the minimal details of a transition referenced in a removal result, including the unique ID of the transition.
  - `message` (string) [maxLen=255] — Represents the message that describes the outcome of the transition removal.
  - `status` (string) [maxLen=255] — Indicates the outcome status of the transition removal.

**Responses:**

- **200**: The request was successful. — Schema: `TransitionRemovalSuccessResponse` [application/json]
    > Represents the top-level response indicating all requested transitions were removed successfully, containing a list of per-transition result items.
    schema: `TransitionRemovalSuccessResponse`
    - `transitions` (array of object `TransitionRemovalResultItem`) [maxItems=2] — Contains the removal result for each transition included in the delete request.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Response contains mixed status results — Schema: `TransitionRemovalMultiStatusResponse` [application/json]
    > Represents the top-level response indicating mixed outcomes from the transition removal operation, containing a list of per-transition result items with both successes and failures.
    schema: `TransitionRemovalMultiStatusResponse`
    - `transitions` (array of object) [maxItems=100] — Contains the per-transition removal results. Each item is either a success result or an error result for the corresponding transition.
      oneOf:
        - `TransitionRemovalResultItem` — Represents the per-transition outcome for the transitions settings operation, providing a status code, message, and detail reference for the affected transition.
        - `TransitionRemovalNotAllowedError` — Represents the error payload returned when a transition cannot be removed because it is still associated with a blueprint, including the places where the transition remains in use.
        - `InvalidTransitionIdentifiersError` — Represents the error response returned when one or more of the provided transition IDs are invalid. The response includes the error code **INVALID_DATA**, a message, a status, and details describing the invalid identifiers.
        - `InvalidValueResponse` — Represents the error response returned when invalid module data is provided during a reorder request. The response includes the error code **INVALID_DATA**, a descriptive message, a status, and validation details.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a value in the request is invalid. Possible values: **INVALID_DATA**.
          - `details` (object) **REQ** — Contains the error details object with field-level validation information.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the property that holds the invalid value.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the property that holds the invalid value.
          - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the given ID is invalid. Possible values: **the id given seems to be invalid**.
          - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
        - `transitions` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `TransitionRemovalNotAllowedError` — Represents the error payload returned when a transition cannot be removed because it is still associated with a blueprint, including the places where the transition remains in use.
            - `InvalidTransitionIdentifiersError` — Represents the error response returned when one or more of the provided transition IDs are invalid. The response includes the error code **INVALID_DATA**, a message, a status, and details describing the invalid identifiers.
      - `MissingModuleParameterError` — Represents the error returned when the required module parameter is missing from the request. Possible values for code: **REQUIRED_PARAM_MISSING**.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when a required module parameter is missing. Possible values: **REQUIRED_PARAM_MISSING**.
        - `details` (object) **REQ** — Contains the error details with validation information, including the name of the missing module parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the missing module parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message returned when a required module parameter is missing. Possible values: **One of the expected parameter is missing**.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: No permission to perform this action — Schema: `NoPermissionError` [application/json]
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

**Scopes:** ZohoCRM.settings.transitions.DELETE
