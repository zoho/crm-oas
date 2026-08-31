# DELETE /settings/automation/field_updates/{id}
**Operation:** `deleteFieldUpdateById` — Delete Field Update
> Deletes a single field update action identified by the path ID. Use the [Get Field Updates API](field_updates.yaml#$.paths./settings/automation/field_updates.get) to retrieve the field update ID. Actions associated with active automation rules return a `NOT_ALLOWED` error, and read-only actions cannot be deleted.


**Parameters:**
- `id` (path, string, required) [maxLen=255]: Unique identifier of the field update action. Use the [Get Field Updates API](field_updates.yaml#$.paths./settings/automation/field_updates.get)  to retrieve the field update IDs.

**Responses:**

- **200**: Indicates that the field update was deleted successfully. — Schema: `DeleteFieldUpdateSuccessResponse` [application/json]
    schema: `DeleteFieldUpdateSuccessResponse`
    - `field_updates` (array of object `FieldUpdateActionResult`) [maxItems=1] — Array containing the deleted field update action. Contains exactly one item.
      schema: `FieldUpdateActionResult`
      - `code` (string) **REQ** [maxLen=255, enum=['SUCCESS', 'NOT_ALLOWED', 'INVALID_DATA']] — Operation result code. 'SUCCESS' for successful operations. In bulk operations (DELETE 207), individual items may return error codes like 'NOT_ALLOWED' or 'INVALID_DATA'.
      - `details` (object `ActionResultDetails`) **REQ** — Details object within an action result, containing the server-generated unique identifier of the created, updated, or deleted field update action.
        schema: `ActionResultDetails`
        - `id` (string) **REQ** [maxLen=255] — Unique identifier of the field update action that was created, updated, or deleted.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the operation outcome.
      - `status` (string) **REQ** [maxLen=255, enum=['success', 'error']] — Overall status of the operation. 'success' for successful operations, 'error' for failed individual items in bulk operations.

- **400**: Returned when the field update ID is invalid, missing, or not deletable due to association/read-only constraints. [application/json]
    oneOf:
      - `InvalidFieldUpdateIdError` — Represents an invalid field update ID.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — Index of the resource path segment that contains the invalid ID.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `MissingDeleteIdParameterError` — Indicates that no field update ID was provided for the delete operation.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) [maxLen=255] — Name of the missing required parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `AssociatedFieldUpdateNotAllowedError` — Field update deletion is not allowed because it is associated with an automation feature.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — Index of the field update entry in the request array that is associated with an automation feature.
        - `message` (string) **REQ** [enum=[2 values]] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `DeleteFieldUpdateReadOnlyActionError` — Returned when attempting to delete a read-only field update action.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — Index of the resource path segment related to the error.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Indicates that the user does not have the necessary permissions to edit a field update action. — Schema: `FeatureNoPermissionError` [application/json]
    > Indicates that the user does not have the necessary permissions to create a field update action.
    schema: `FeatureNoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code.
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] — Permission that the current user is missing
        items: [maxLen=255]
      - `api_name` (string) [maxLen=255] — API name of the field associated with the permission error.
      - `json_path` (string) [maxLen=1000] — JSON path to the field in the request body
    - `message` (string) **REQ** [enum=[3 values]] — Represents the error message.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status

**Scopes:** ZohoCRM.settings.automation_actions.DELETE
