# DELETE /settings/blueprints/{blueprintId}/states
**Operation:** `deleteBlueprintStates` — Delete Blueprint States
> To delete one or more states from a Blueprint in your Zoho CRM organization.

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Specify the [unique ID of the Blueprint](blueprints.yaml#$.paths./settings/blueprints.get) for which you want to delete states.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Specify the Zoho service context for the request. Possible values: **automation** - Targets the automation service.
- `ids` (query, array, required) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Specify the [unique state IDs](blueprint_state_config.yaml#$.paths./settings/blueprints/{blueprintId}/states.get) to filter the query results. Accepts comma-separated values.

**Schemas:**
`AutomationActionReferenceUpdateAlternative`:
  > An automation action reference used in update operations, identified by its **id** and an optional **name**.
  - `name` (string) [maxLen=100, nullable] — The name of the action configured for the automation trigger.
  - `id` (string) [maxLen=255, pattern=[0-9]+] — The unique identifier of the automation action configured for the trigger.
  additionalProperties: any
`InvalidStateIDsError`:
  > Represents the error response returned when one or more of the provided state IDs are invalid.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
  - `details` (object) **REQ** — Represents the details of the validation error, containing an object with the affected record **id**.
    - `id` (string) **REQ** [maxLen=255] — Represents the ID of the invalid state that caused the error.
  - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when an invalid state ID is provided. Possible values: the id given seems to be invalid - The supplied state ID does not correspond to a valid state in Zoho CRM.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
`StateOperationResultItem`:
  > The result of a state operation, including status, code, message, and per-item details.
  - `code` (string) [maxLen=255, enum=['SUCCESS']] — The result code for the operation. Possible values: **SUCCESS** - The operation completed successfully.
  - `details` (object `AutomationActionReferenceUpdateAlternative`) — An automation action reference used in update operations, identified by its **id** and an optional **name**.
  - `message` (string) [maxLen=255] — The message returned for the state operation result.
  - `status` (string) [maxLen=255] — The outcome status of the state operation for the corresponding item.

**Responses:**

- **200**: Returns a confirmation that the Blueprint states were successfully deleted. — Schema: `BlueprintStatesDeleteResponse` [application/json]
    > Represents the response returned after deleting one or more Blueprint states, containing the results for each deleted state.
    schema: `BlueprintStatesDeleteResponse`
    - `states` (array of object `StateOperationResultItem`) [maxItems=2] — Represents the list of Blueprint state objects affected by the delete operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a multi-status response where each item in the array independently indicates success or failure for the corresponding state deletion request. — Schema: `BlueprintStatesDeleteMultiStatusResponse` [application/json]
    > Represents the multi-status response returned when deleting multiple Blueprint states, where each entry in the **states** array independently indicates success or failure for the corresponding state.
    schema: `BlueprintStatesDeleteMultiStatusResponse`
    - `states` (array of object) [maxItems=100] — Represents the list of per-state deletion results, containing one entry for each state processed in the request.
      oneOf:
        - `StateOperationResultItem` — The result of a state operation, including status, code, message, and per-item details.
        - `InvalidStateIDsError` — Represents the error response returned when one or more of the provided state IDs are invalid.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax. **Resolution:** Review and correct the request payload to ensure it uses valid syntax before resubmitting. [application/json]
    oneOf:
      - `InvalidResourcePathError` — Represents the error response returned when the specified resource path is invalid or malformed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of invalid resource path error. Possible values: **INVALID_DATA** - The request contains invalid data.
        - `details` (object) **REQ** — Represents the error details for an invalid resource path. Contains a **resource_path_index** object with validation information identifying the invalid path.
          - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index of the path segment in the request URL that is invalid.
        - `message` (string) **REQ** [enum=['the process id given seems to be invalid']] — Represents the error message describing the issue. Possible values: the process id given seems to be invalid - The specified process ID does not correspond to a valid resource path.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
        - `states` (array of object `InvalidStateIDsError`) [maxItems=25] **REQ** — Array of error objects
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to delete Blueprint states. **Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
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
