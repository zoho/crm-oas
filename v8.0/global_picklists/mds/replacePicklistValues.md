# POST /settings/global_picklists/{id}/actions/replace_picklist_values
**Operation:** `replacePicklistValues` — Replace Picklist Values
> Schedules or executes replacement of picklist values for the specified global picklist. You can specify either `id`, `display_value`, or both for `old_value` and `new_value`. If both are provided, the system validates them for consistency. The `from` (old) value can be non-existent in the current picklist, but the `to` (new) value must be in the **used** state of the picklist option.

**Tags:** Global Picklists

**Parameters:**
- `id` (path, string/int64, required): Numeric id of the global picklist. Use the [Get All Global Picklists](global_picklists.yaml#$.paths./settings/global_picklists.get) resource to retrieve global picklist IDs.


**Request Body** (required) — application/json
  > Request body for replacing picklist values in a global picklist.
  - `replace_picklist_values` (array of object) [maxItems=1] **REQ** — Array of picklist value replacement pairs.
    - `old_value` (object) **REQ** — The existing picklist value to be replaced.
      - `id` (string/int64) — Id of the resource.
      - `display_value` (string) [maxLen=120] — The picklist display value(translated value if translation enabled).
    - `new_value` (object) **REQ** — The new picklist value that will replace the old one.
      - `id` (string/int64) — Id of the resource.
      - `display_value` (string) [maxLen=120] — The picklist display value(translated value if translation enabled).

**Responses:**

- **200**: OK - Replacement completed immediately since the global set is not associated with any fields. [application/json]
    > Response object for immediate replacement completion.
    - `replace_picklist_values` (array of object) [maxItems=1] **REQ** — Array of replacement operation results.
      - `code` (string) **REQ** [maxLen=50] — Indicates that the replacement operation completed successfully.
      - `details` (object) **REQ** — Additional details about the replacement operation.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message about the replacement operation.
      - `status` (string) **REQ** [maxLen=50] — Status of the replacement operation.

- **202**: Accepted - Replacement scheduled successfully for associated fields. [application/json]
    > response object for scheduled replacement of picklist values.
    - `replace_picklist_values` (array of object) [maxItems=1] **REQ** — Array of replacement operation results.
      - `code` (string) **REQ** [maxLen=50] — Indicates that the replacement operation has been scheduled.
      - `details` (object) **REQ** — Additional details about the replacement operation.
        - `job_id` (string) **REQ** [maxLen=100] — The ID of the scheduled replacement job.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message about the replacement operation.
      - `status` (string) **REQ** [maxLen=50] — Status of the replacement operation.

- **400**: Bad Request - Invalid data, missing fields, ambiguity, or disallowed actions, or if limits exceeded. [application/json]
    oneOf:
        - `replace_picklist_values` (array of object) [maxItems=1] **REQ** — Array of replacement operation error details.
          - `code` (string) **REQ** [enum=[6 values]] — Error code indicating the type of validation or constraint failure.
          - `details` (object) **REQ** — Additional error-specific details.
            - `api_name` (string) [maxLen=100] — name of the field causing the error.
            - `json_path` (string) [maxLen=255] — JSON path to the field causing the error.
            - `ambiguity_due_to` (array of object) [maxItems=30] — if both id and display_value are provided and they don't match
              - `api_name` (string) [maxLen=100] — name of the ambiguous field.
              - `json_path` (string) [maxLen=255] — JSON path to the ambiguous field.
            - `expected_fields` (array of object) [maxItems=10] — List of expected fields that are missing.
              - `api_name` (string) [maxLen=100] — name of the expected field.
              - `json_path` (string) [maxLen=255] — JSON path to where the field is expected.
            - `limit_due_to` (array of object) [maxItems=10] — List of picklist values that caused the limit to be exceeded.
              - `api_name` (string) [maxLen=100] — API name of the field causing limit issue.
              - `json_path` (string) [maxLen=255] — JSON path to the field causing limit issue.
            - `limit` (integer/int32) — The maximum allowed limit that has been exceeded. if this exists in details, limit_due_to will also be present.
          - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the error.
          - `status` (string) **REQ** [enum=['error']] — Status of the error response.
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Error code indicating invalid data or disallowed action.
        - `details` (object) — Additional details about the top-level error.
          - `resource_path_index` (integer/int32) **REQ** [enum=[2]] — Index in the resource path indicating the error location.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message describing the issue.
        - `status` (string) **REQ** [maxLen=50] — Status of the error response.

- **403**: Forbidden [application/json]
    > Error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
      - `permissions` (array of string) [maxItems=1] — List of permissions required to access the resource.
        items: [enum=['Crm_Implied_Customize_Zoho_CRM']]
    - `status` (string) **REQ** [maxLen=100, enum=['error']] — Status of the error response.

- **500**: Internal Server Error [application/json]
    > Internal server error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
    - `status` (string) **REQ** [enum=['error']] — Status of the error response.

**Scopes:** ZohoCRM.settings.global_picklist.ALL
