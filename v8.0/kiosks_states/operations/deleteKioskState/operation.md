# DELETE /settings/kiosks/{kioskId}/states/{stateId}
**Operation:** `deleteKioskState` — Delete a kiosk state
> To delete a specific state from a kiosk configuration in your Zoho CRM account. Removing a state eliminates all its associated configurations, transitions, and connected elements. Use the delete_dependent_states query parameter to control whether dependent states are also removed or left as disconnected components. The kiosk must be in draft status to perform this action. Predefined states (start state and end state) cannot be deleted. Available in Standard, Professional, Enterprise, and Ultimate editions.

**Parameters:**
- `delete_dependent_states` (query, string, optional) [enum=['true|false']]: When a state is deleted, all its associated configurations, transitions, and connected elements are removed. Use the delete_dependent_states query parameter to control whether dependent/child states should also be deleted or left as disconnected components. The default value is true.
Possible values:
true
false

- `kioskId` (path, string, required) [maxLen=255]: Specify the unique identifier of the Kiosk.
- `stateId` (path, string, required) [maxLen=255]: Specify the unique identifier of the kiosk state.

**Responses:**

- **200**: Returns a confirmation that the specified kiosk state has been removed from the kiosk configuration. — Schema: `DeleteStateResponse` [application/json]
    > Represents the success response returned after a kiosk state deletion.
    schema: `DeleteStateResponse`
    - `states` (object `StateOperationResult`) — Represents the operation result for a single kiosk state in a create or update response. Contains the result code, status, message, and state details.
      schema: `StateOperationResult`
      - `code` (string) [maxLen=255] — Represents the result code for the operation on this state.
      - `details` (object `StateOperationResultDetails`) — Represents the details of a state operation result. Contains the unique identifier and resource identifier of the created or updated kiosk state.
        schema: `StateOperationResultDetails`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the kiosk state created or updated.
        - `rid` (string/uuid) [maxLen=255] — Represents the resource identifier of the kiosk state.
      - `message` (string) [maxLen=255] — Represents the result message for the operation on this state.
      - `status` (string) [maxLen=255] — Represents the result status for the operation on this state.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Returned when the request cannot be completed due to invalid input or a constraint violation. Errors include referencing a state ID that does not exist in the kiosk, attempting to delete a state from an active (non-draft) kiosk, or attempting to delete a state whose fields are associated with other components. Resolution: Verify the state ID is valid, ensure the kiosk is in draft status, and remove any dependent component associations before retrying, or use the delete_dependent_states query parameter to remove dependent states automatically. — Schema: `KioskStateErrorResponse` [application/json]
    > Represents the generic error response for kiosk state operations. Contains an error code, error message, and contextual details about the validation failure.
    schema: `KioskStateErrorResponse`
    - `code` (string) **REQ** [enum=[8 values]] — Represents the error category code indicating the type of validation failure.
    - `details` (object) **REQ** — Represents contextual details about the error. The structure varies by error type and may include the affected field path, expected data type, or resource path.
      - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the error.
      - `json_path` (string) [maxLen=1000] — Represents the JSON path pointing to the problematic field in the request body.
      - `expected_data_type` (string) [maxLen=255] — Represents the expected data type when a type mismatch occurs in the request.
      - `maximum_length` (integer/int32) — Represents the maximum allowed length when a field value exceeds the configured limit.
      - `resource_path_index` (integer/int32) — Represents the index in the resource path that is invalid.
      - `permissions` (array of string) [maxItems=100] — Represents the list of required OAuth scopes when access is denied.
        items: [maxLen=255]
      additionalProperties: any
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing what went wrong.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always 'error' for error responses.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.DELETE
