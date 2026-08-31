# PUT /settings/territories/{territory}/users/{user}
**Operation:** `associateUserToSpecificTerritory` — Territory User
> To associate a specific user with a territory in your Zoho CRM organization.

**Parameters:**
- `territory` (path, string, required) [maxLen=100]: Territory Id Param in URL
- `user` (path, string, required) [maxLen=100]: User Id Param in URL

**Responses:**

- **200**: Returns the result of the user-territory association. [application/json]
    > Represents the success response body returned after associating the user with the territory.
    oneOf:
        - `users` (array of object) [maxItems=100] **REQ** — Represents the list of user-territory association results.
          oneOf:
              type: array of object [maxItems=100]
                - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the association operation for the user.
                - `details` (object) **REQ** — Represents additional details about the association operation.
                  - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the user.
                - `message` (string) **REQ** [maxLen=250] — Represents the status message of the association operation.
                - `status` (string) **REQ** [enum=['success']] — Represents the status of the association operation for the user.

- **400**: Returns an error when the request body contains invalid user IDs or duplicate entries. **Resolution:** Verify the user IDs provided and ensure they are valid and unique. [application/json]
    > Represents the error response body returned when the request data is invalid.
    oneOf:
      - `UserInvalidErrorSchemaOnRequestBody` — Represents the invalid-request error schema returned when the user or territory ID in the URL fails validation.
        - `users` (array of object) [maxItems=100] **REQ** — Represents the list of user entries, each containing the result code, details, status, and message for the corresponding user in the request.
          - `code` (string) **REQ** [enum=[5 values]] — Represents the error or status code for the user entry. Possible values: **INVALID_DATA**, **DUPLICATE_DATA**, **MANDATORY_NOT_FOUND**, **NOT_ALLOWED**, **DEPENDENT_FIELD_MISSING**.
          - `details` (object) **REQ** — Represents additional contextual information about the validation error for the user entry.
            - `api_name` (string/string) [minLen=1] — Represents the API field name associated with the validation error.
            - `json_path` (string/string) [minLen=1] — Represents the JSON path to the field that caused the validation error.
            - `supported_values` (array of string) [maxItems=100] — Represents the list of supported values for the field associated with the validation error.
              items: [maxLen=100]
            - `id` (string/string) — Represents the unique identifier of the resource related to the validation error.
            - `resource_path_index` (integer/int32) — Represents the index in the resource path where the validation error occurred.
            - `dependee` (object) — Represents the dependent field information related to the validation error.
              - `api_name` (string/string) — Represents the API field name of the dependent field that caused the validation error.
              - `json_path` (string/string) [minLen=1] — Represents the JSON path to the dependent field that caused the validation error.
              - `resource_path_index` (integer/int32) — Represents the index in the resource path where the dependent field is located.
            - `owner_status` (string/string) — Represents the status of the user being added to the territory, indicating why the operation failed.
          - `message` (string/string) **REQ** — Represents the detailed error message describing the validation issue for the user entry.
          - `status` (string) **REQ** [enum=['error', 'success', 'failure']] — Represents the outcome status of the user entry in the response. Possible values: **error**, **success**, **failure**.

- **403**: Returns an error when the territory feature is not yet enabled, is disabled, or access is denied. **Resolution:** Ensure the Territories feature is active and that your OAuth token includes the required scopes. [application/json]
    > Represents the error response body returned when access is denied or the territory feature is not enabled.
    oneOf:
      - `TerritoryErrorPermissionDenied` — Territory Not yet Enabled.
        - `code` (string) **REQ** [enum=[4 values]] — Represents the error code indicating why territory access was denied. Possible values: **PERMISSION_DENIED**, **FEATURE_NOT_ENABLED**, **TERRITORY_DISABLED**, **TERRITORY_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the permission denied error, returned as an empty object.
        - `message` (string) **REQ** [maxLen=100] — Represents the human-readable description of why the territory access was denied.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**.

- **500**: An internal server error occurred while processing the request. **Resolution:** Retry the request after some time. If the error persists, contact Zoho CRM support. [application/json]
    > Represents the error response body returned when an internal server error occurs.
    oneOf:
      - `TerritoryInternalServerErrorSchema` — Internal server error.
        - `code` (string) **REQ** [enum=['INTERNAL_SERVER_ERROR']] — Represents the error code for an internal server error. Possible values: **INTERNAL_SERVER_ERROR**.
        - `details` (object) **REQ** — Represents additional details about the internal server error, returned as an empty object.
        - `message` (string) **REQ** [maxLen=100] — Represents the human-readable description of the internal server error.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**.

**Scopes:** ZohoCRM.users.ALL, ZohoCRM.settings.territories.ALL
