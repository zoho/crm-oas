# DELETE /settings/blueprints/transitions/{transitionId}
**Operation:** `deleteBlueprintTransitionById` — Blueprint Transition
> This is a new API to delete single transitions in a single API

**Parameters:**
- `transitionId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: The ID of the transition to delete
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Represents a custom request header that identifies the Zoho service associated with the request. Possible values: **automation**.

**Responses:**

- **200**: Successful response is returned. — Schema: `BlueprintTransitionRemovalResponse` [application/json]
    > Represents the 200 OK response payload for removing a blueprint transition. Provides transitions, an array of per-transition result entries describing the outcome of the delete operation.
    schema: `BlueprintTransitionRemovalResponse`
    - `transitions` (array of object `TransitionOperationResultEntry`) [maxItems=1] — Contains the removal result of the blueprint transition targeted by the delete operation.
      schema: `TransitionOperationResultEntry`
      - `code` (string) [maxLen=255] — Represents the result code returned for the individual transition operation entry.
      - `details` (object `TransitionOperationDetail`) — Represents the details that identify the transition involved in the blueprint transitions operation, including the unique transition ID.
        schema: `TransitionOperationDetail`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the transition operation detail.
      - `message` (string) [maxLen=255] — Represents the message returned for the individual transition operation entry, describing its outcome.
      - `status` (string) [maxLen=255] — Indicates the response status of the individual transition operation entry.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request. The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
      - `TransitionRemovalNotAllowedError` — Represents the error payload returned when a transition cannot be removed because it is still associated with a blueprint, including the places where the transition remains in use.
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
      - `BlueprintIdInvalidError` — Represents the error returned when the blueprint ID in the request is invalid. Possible values: **INVALID_DATA**.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the blueprint ID is invalid. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Contains the error details object with validation information about the invalid blueprint ID.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the index of the resource path associated with the invalid blueprint ID.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the blueprint ID is invalid. Possible values: **the id given seems to be invalid**.
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
