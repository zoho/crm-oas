# DELETE /settings/automation/field_updates
**Operation:** `deleteFieldUpdates` — To delete multiple field update actions
> Deletes multiple Field Update actions specified by their IDs. Specify the action IDs as a comma-separated list using the ids query parameter. You can delete a maximum of 10 actions in a single request. Field Update actions associated with active automation rules or marked as read-only cannot be deleted. Use the Get Field Updates API to retrieve the Field Update IDs. The response includes the success or failure status for each specified ID. Use the [Get Field Updates API](field_updates.yaml#$.paths./settings/automation/field_updates.get) to get the Field Update IDs.

**Parameters:**
- `ids` (query, string, required) [maxLen=10000] {style=form, explode=True}: The unique field update IDs you want to delete. Use the [Get Field Updates API](field_updates.yaml#$.paths./settings/automation/field_updates.get) to retrieve the IDs.



**Schemas:**
`BulkDeleteFailureItem`:
  > Result item for a field update ID that failed during bulk delete. INVALID_DATA indicates the ID does not exist; NOT_ALLOWED indicates the field update is associated with a workflow rule, blueprint, or approval process.
  - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Failure code.
  - `details` (object `BulkDeleteResultDetails`) **REQ** — Identifier details for a bulk-delete result item.
  - `message` (string) **REQ** [maxLen=255] — Failure message.
  - `status` (string) **REQ** [enum=['error']] — Operation status.
`BulkDeleteResultDetails`:
  > Identifier details for a bulk-delete result item.
  - `id` (string) **REQ** [maxLen=20] — Field update ID for which this result applies.
`BulkDeleteSuccessItem`:
  > Result item for a field update ID deleted successfully in bulk delete.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Result code.
  - `details` (object `BulkDeleteResultDetails`) **REQ** — Identifier details for a bulk-delete result item.
  - `message` (string) **REQ** [maxLen=255] — Success message.
  - `status` (string) **REQ** [enum=['success']] — Operation status.

**Responses:**

- **200**: Bulk delete completed successfully for all requested field update IDs. — Schema: `BulkDeleteSuccessResponse` [application/json]
    > Bulk delete success response where all requested field update IDs are deleted.
    schema: `BulkDeleteSuccessResponse`
    - `field_updates` (array of object `BulkDeleteSuccessItem`) [maxItems=10] **REQ** — Deletion result entries for each requested ID.

- **207**: Bulk delete completed with mixed results. Some IDs were deleted successfully while others failed with INVALID_DATA or NOT_ALLOWED. — Schema: `BulkDeleteMixedResponse` [application/json]
    > Bulk delete partial-success response. Contains mixed success and failure items for the requested field update IDs.
    schema: `BulkDeleteMixedResponse`
    - `field_updates` (array of object) [maxItems=10] **REQ** — Per-ID deletion results for the bulk request.
      oneOf:
        - `BulkDeleteSuccessItem` — Result item for a field update ID deleted successfully in bulk delete.
        - `BulkDeleteFailureItem` — Result item for a field update ID that failed during bulk delete. INVALID_DATA indicates the ID does not exist; NOT_ALLOWED indicates the field update is associated with a workflow rule, blueprint, or approval process.

- **400**: Bulk delete failed. Either all provided IDs failed validation/association checks, the ids parameter is missing, or the number of IDs exceeded the maximum allowed limit. [application/json]
    oneOf:
      - `MissingDeleteIdParameterError` — Indicates that no field update ID was provided for the delete operation.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) [maxLen=255] — Name of the missing required parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `BulkDeleteErrorResponse` — Bulk delete error response where all provided field update IDs failed validation or association checks.
        - `field_updates` (array of object `BulkDeleteFailureItem`) [maxItems=10] **REQ** — Per-ID failure results for the bulk request.
      - `IdsLimitExceededError` — Returned when the number of IDs provided in the ids query parameter exceeds the maximum allowed limit of 10.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the data provided is invalid
        - `details` (object) **REQ** — Details about the limit that was exceeded
          - `maximum_length` (integer/int32) — The maximum number of IDs allowed in a single bulk delete request
          - `param_name` (string) [maxLen=255] — The query parameter that exceeded the limit
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `BulkDeleteFailureItem` — Result item for a field update ID that failed during bulk delete. INVALID_DATA indicates the ID does not exist; NOT_ALLOWED indicates the field update is associated with a workflow rule, blueprint, or approval process.
      - `BulkDeleteInvalidIdParamError` — Returned when a single non-existent field update ID is supplied via the ids query parameter on the bulk delete endpoint. The error carries details.param_name='ids' (not resource_path_index) to indicate the failure is tied to the bulk query parameter, not a URL path segment.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the data provided is invalid
        - `details` (object) **REQ** — Details identifying which parameter caused the error
          - `param_name` (string) [maxLen=255] — The query parameter whose value is invalid (ids)
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Indicates that the user does not have the necessary permissions to delete field update details. — Schema: `FeatureNoPermissionError` [application/json]
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
