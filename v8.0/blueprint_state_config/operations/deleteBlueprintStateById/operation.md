# DELETE /settings/blueprints/{blueprintId}/states/{stateId}
**Operation:** `deleteBlueprintStateById` — Delete a Blueprint state
> To delete a single state from a Blueprint in your Zoho CRM organization.

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Specify the [unique ID of the Blueprint](blueprints.yaml#$.paths./settings/blueprints.get) for which you want to delete a state.
- `stateId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Represents the unique ID of the Blueprint state. Use the [Get Blueprint States API](blueprint_state_config.yaml#$.paths./settings/blueprints/{blueprintId}/states.get) to retrieve the state ID.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Specify the Zoho service context for the request. Possible values: **automation** - Targets the automation service.

**Responses:**

- **200**: Returns a confirmation that the Blueprint state was successfully deleted. — Schema: `BlueprintStateDeleteByIDResponse` [application/json]
    > The response returned after deleting a specific Blueprint state, containing the outcome details for the deleted state.
    schema: `BlueprintStateDeleteByIDResponse`
    - `states` (array of object `StateOperationResultItem`) [maxItems=1] — The list of Blueprint state objects affected by the delete operation.
      schema: `StateOperationResultItem`
      - `code` (string) [maxLen=255, enum=['SUCCESS']] — The result code for the operation. Possible values: **SUCCESS** - The operation completed successfully.
      - `details` (object `AutomationActionReferenceUpdateAlternative`) — An automation action reference used in update operations, identified by its **id** and an optional **name**.
        schema: `AutomationActionReferenceUpdateAlternative`
        - `name` (string) [maxLen=100, nullable] — The name of the action configured for the automation trigger.
        - `id` (string) [maxLen=255, pattern=[0-9]+] — The unique identifier of the automation action configured for the trigger.
        additionalProperties: any
      - `message` (string) [maxLen=255] — The message returned for the state operation result.
      - `status` (string) [maxLen=255] — The outcome status of the state operation for the corresponding item.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax. **Resolution:** The request syntax must be corrected before resubmitting. [application/json]
    oneOf:
      - `ErrorResponseCore15` — Represents the error response returned when a required header is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_HEADER_MISSING']] — Represents the error code returned when a required header is missing from the request. Possible values: **REQUIRED_HEADER_MISSING** - A required header was not included in the request.
        - `details` (object) **REQ** — Represents an object containing additional details about the error, including information about the specific header or field that caused it.
          - `header_name` (string) **REQ** [maxLen=255] — Represents the name of the HTTP request header associated with the error.
        - `message` (string) **REQ** [enum=['One of the expected headers is missing']] — Represents the error message describing the issue. Possible values: One of the expected headers is missing - A required request header was not included in the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
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
      - `ActiveBlueprintStateDeleteError` — Error returned when attempting to delete a state from an active blueprint.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — The error code for the operation. Possible values: **NOT_ALLOWED** - The requested action is not permitted.
        - `details` (object) **REQ** — Additional details about the error, including the **resource_path_index** that identifies the location of the error in the request.
          - `resource_path_index` (integer/int32) **REQ** — The index position of the invalid resource path that caused the error.
        - `message` (string) **REQ** [enum=['State cannot be deleted from a published blueprint']] — The error message returned when a Blueprint state deletion fails. Possible values: State cannot be deleted from a published blueprint - The requested state exists in a published Blueprint and cannot be removed.
        - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to delete the Blueprint state. **Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
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

**Scopes:** ZohoCRM.settings.blueprint.states.DELETE
