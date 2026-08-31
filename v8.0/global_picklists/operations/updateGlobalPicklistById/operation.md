# PATCH /settings/global_picklists/{id}
**Operation:** `updateGlobalPicklistById` — Update a Global Picklist by ID
> Updates an existing global picklist identified by the path parameter \{id\}. You can update display_label, api_name, description, pick_list_values_sorted_lexically, and pick_list_values. Backend-generated properties (actual_label, customizable, modified_by, created_by, presence) cannot be updated. For pick_list_values, you can add new values, update existing values (using id), move values between used/unused (one at a time), or delete values (one at a time using _delete: true). Bulk operations for moving to unused or deletion are not allowed.

**Parameters:**
- `id` (path, string/int64, required): Numeric id of the global picklist. Use the [Get All Global Picklists](global_picklists.yaml#$.paths./settings/global_picklists.get) resource to retrieve global picklist IDs.


**Request Body** (required) — application/json
  > Request body for updating a global picklist.
  - `global_picklists` (array of object) [maxItems=1] **REQ** — Array containing the global picklist to update.
    - `display_label` (string) [maxLen=50] — Updated display label of the global picklist.
    - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
    - `description` (string) [maxLen=1000, nullable] — Updated description of the global picklist.
    - `pick_list_values_sorted_lexically` (boolean) — Indicates if picklist values should be sorted lexically.
    - `pick_list_values` (array of object) [maxItems=5000] — Array of picklist values to add, update, or delete. For updates, include id and fields to update. For deletion, include id and _delete: true. Only one value can be moved to unused or deleted per request.
      - `id` (string/int64) — Id of the resource.
      - `display_value` (string) [maxLen=120] — The picklist display value(translated value if translation enabled).
      - `reference_value` (string) [maxLen=120] — Reference value of the picklist field.
      - `type` (string) [enum=['unused', 'used']] — Type of the picklist value (used or unused). Only one value can be moved to unused per request.
      - `_delete` (boolean) — Set to true to delete this picklist value. Only one value can be deleted per request.

**Responses:**

- **200**: OK - Global picklist updated successfully. [application/json]
    > Response object for successful update of a global picklist.
    - `global_picklists` (array of object) [maxItems=1] **REQ** — Array containing the updated global picklist response.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Response code indicating successful update.
      - `details` (object) **REQ** — Details of the updated global picklist.
        - `id` (string/int64) **REQ** — Id of the resource.
      - `message` (string) **REQ** [maxLen=255] — Human-readable success message.
      - `status` (string) **REQ** [enum=['success']] — Status of the operation.

- **400**: Bad Request - Invalid data, missing required fields, duplicate values, special characters, length exceeded, limit exceeded, reserved keywords, or operation not allowed. [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Error code indicating the type of validation or constraint failure.
        - `details` (object) **REQ** — Additional error-specific details.
          - `resource_path_index` (integer/int32) **REQ** [const=2] — Index in the resource path indicating the error location.
        - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the error.
        - `status` (string) **REQ** [enum=['error']] — Status of the error response.
        - `global_picklists` (array of object) [maxItems=1] **REQ** — Array of global picklist update error details.
          - `code` (string) **REQ** [enum=[5 values]] — Error code indicating the type of validation or constraint failure.
          - `details` (object) **REQ** — Additional error-specific details.
            - `api_name` (string) [maxLen=100] — Name of the field causing the error.
            - `json_path` (string) [maxLen=255] — JSON path to the field causing the error.
            - `id` (string) [maxLen=100] — ID of the resource causing the error.
            - `maximum_length` (integer/int32) — Maximum allowed length for the field.
            - `limit_due_to` (object)
              oneOf:
                  type: array of object [maxItems=10]
                    - `api_name` (string) **REQ** [maxLen=100] — API name of the field causing limit issue.
                    - `json_path` (string) **REQ** [maxLen=255] — JSON path to the field causing limit issue.
                  - `api_name` (string) **REQ** [maxLen=100] — API name of the field causing limit issue.
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the field causing limit issue.
            - `limit` (integer/int32) — The maximum allowed limit that has been exceeded.
          - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the error.
          - `status` (string) **REQ** [enum=['error']] — Status of the error response.

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

**Scopes:** ZohoCRM.settings.global_picklist.UPDATE
