# DELETE /settings/record_locking_configurations
**Operation:** `deleteRecordLockingConfiguration` — Delete record locking configuration
> Deletes the record locking configuration(s) for the specified module using the provided configuration IDs.

**Parameters:**
- `module` (query, string, required) [maxLen=256]: The API name of the module for which the configuration should be deleted.
- `ids` (query, string, required) [maxLen=256]: Comma-separated list of record locking configuration IDs to delete.

**Responses:**

- **200**: Successfully deleted the specified record locking configuration(s). [application/json]
    > Response object for a successful deletion.
    - `record_locking_configurations` (array of object) [maxItems=1] **REQ** — Array containing details of the deleted configuration(s).
      - `status` (string) **REQ** [maxLen=256, enum=['success']] — Indicates successful deletion.
      - `code` (string) **REQ** [maxLen=256, enum=['SUCCESS']] — Success code for the operation.
      - `message` (string) **REQ** [maxLen=256] — Informational message about the deletion.
      - `details` (object) **REQ** — Additional details about the deleted configuration.
        - `id` (string) **REQ** [maxLen=256] — ID of the deleted configuration.

- **400**: Bad Request - The request could not be processed due to invalid input, missing parameters, unsupported features, or permission issues. [application/json]
    > Error response object.
    - `code` (string) **REQ** [maxLen=256, enum=[6 values]] — Error code identifying the failure reason.
    - `message` (string) **REQ** [maxLen=256] — An error message explaining the issue.
    - `status` (string) **REQ** [enum=['error']] — Status indicator, always `error`.
    - `details` (object) **REQ** — Additional error details that vary by error code.
      oneOf:
          - `param_name` (string) **REQ** [maxLen=256] — Name of the missing parameter.
          - `resource_path_index` (integer/int32) **REQ** — Index of the invalid path element.
          - `permissions` (array of string) [maxItems=1] **REQ** — List of required permissions.
            items: [maxLen=256]

**Scopes:** ZohoCRM.settings.record_locking_configurations.DELETE
