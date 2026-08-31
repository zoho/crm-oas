# POST /settings/record_locking_configurations
**Operation:** `createRecordLockingConfiguration` — Create record locking configuration
> Creates a new record locking configuration for the specified module. You can define locking rules, restricted actions, excluded fields, and other settings.

**Parameters:**
- `module` (query, string, required) [maxLen=256]: The API name of the module for which the record locking configuration is being managed. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module names.

**Request Body** (required) — application/json
  > Request body for creating a record locking configuration.
  - `record_locking_configurations` (array of object) [maxItems=1] **REQ** — Array containing the record locking configuration details to be created.
    - `lock_type` (string) **REQ** [enum=['automatic', 'manual', 'both']] — Defines the locking mode. `automatic` locks records based on rules, `manual` requires explicit action, `both` supports both.
    - `locked_for` (string) [enum=['all_profiles', 'all_profiles_except_excluded_profiles']] — Indicates which profiles the lock applies to. Use `all_profiles` for everyone, or `all_profiles_except_excluded_profiles` to exclude specific profiles.
    - `restricted_actions` (array of string) [maxItems=10] — List of actions that are restricted on locked records. These actions cannot be performed on locked records.
      items: [enum=['change_owner', 'update', 'delete', 'tags'], default=update]
    - `excluded_fields` (array of object) [maxItems=15] — Fields that are exempt from locking. Even if a record is locked, these fields can still be modified.
      - `id` (string/int64) **REQ** — The unique identifier of the field. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve field IDs.
    - `feature_type` (string) [enum=['record_locking'], default=record_locking] — Feature type identifier. Must be `record_locking` for this configuration.
    - `locking_rules` (array of object) [maxItems=5] — A set of rules that define when records should be automatically locked. Each rule contains criteria that records must match to be locked.
      - `name` (string) **REQ** [maxLen=256] — Unique name for the locking rule.
      - `lock_existing_records` (boolean) [default=False] — If `true`, existing records that match the criteria will also be locked when the rule is saved.
      - `criteria` (object) **REQ** — Criteria that records must satisfy for the rule to apply. The structure depends on the field type and operator.
    - `restricted_communications` (array of string) [maxItems=10] — List of communication actions that are restricted for locked records.
      items: [enum=['send_mail']]
    - `restricted_custom_buttons` (array of object) [maxItems=30] — List of custom buttons that are restricted on locked records. These buttons cannot be used on locked records.
      - `id` (string/int64) **REQ** [maxLen=19] — Unique identifier of the custom button.
    - `lock_excluded_profiles` (array of object) [maxItems=15] — Profiles that are excluded from locking. These profiles can still edit locked records. This property is required when `locked_for` is `all_profiles_except_excluded_profiles`.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Profile ID. Use the [Get Profiles API](profiles.yaml#$.paths./settings/profiles.get) to retrieve profile IDs.
    - `lock_for_portal_users` (boolean) [default=True] — If `true`, portal users are also subject to the locking restrictions.
    additionalProperties: any

**Responses:**

- **201**: Successfully created the record locking configuration for the specified module. [application/json]
    > Response object for a successful configuration creation.
    - `record_locking_configurations` (array of object) [maxItems=1] **REQ** — Array containing details of the created record locking configuration.
      - `status` (string) **REQ** [enum=['success']] — Indicates that the creation operation was successful.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Success code for the operation.
      - `message` (string) **REQ** [maxLen=255] — Informational message about the creation.
      - `details` (object) **REQ** — Additional details about the created configuration.
        - `id` (string) **REQ** [maxLen=255] — Unique identifier of the newly created record locking configuration.

- **400**: Bad Request - The request could not be processed due to invalid syntax, missing parameters, or invalid data. [application/json]
    > Union of a simple error object or an array-wrapped error envelope.
    oneOf:
        - `code` (string) **REQ** [maxLen=256, enum=[10 values]] — Error code that identifies the failure reason.
        - `message` (string) **REQ** [maxLen=256] — An error message explaining the issue.
        - `status` (string) **REQ** [enum=['error']] — Status indicator, always `error`.
        - `details` (object) **REQ** — Additional information that varies by error code.
          oneOf:
              - `param_name` (string) **REQ** [maxLen=256] — Name of the missing parameter.
              - `resource_path_index` (integer/int32) **REQ** — Index of the invalid path element.
              - `permissions` (array of string) [maxItems=1] **REQ** — List of permissions required to perform the operation.
                items: [maxLen=256]
              - `limit` (integer/int32) **REQ** — The maximum allowed value.
              - `available_limit` (integer/int32) — Remaining available capacity, if applicable.
              - `param_name` (string) [maxLen=256] — Parameter name that hit the limit (e.g., module).
        - `record_locking_configurations` (array of object) [maxItems=1] — Array containing a single error object for the configuration item.
          - `code` (string) **REQ** [maxLen=256, enum=[8 values]] — Error code for the configuration error.
          - `details` (object) **REQ** — Detailed metadata for the configuration error. The structure varies by error type.
            oneOf:
                - `api_name` (string) **REQ** [maxLen=256] — API name of the field involved.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path pointing to the location of the error.
                - `supported_values` (array of string) [maxItems=15] **REQ** — List of allowed values.
                  items: [maxLen=256]
                - `api_name` (string) **REQ** [maxLen=256] — API name of the field.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path to the error location.
                - `limit` (integer/int32) **REQ** — Maximum allowed count.
                - `available_limit` (integer/int32) — Remaining available count, if positive.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the array that exceeded the limit.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path to the array location.
                - `dependee` (object) **REQ** — Information about the field that is causing the dependency.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field.
                  - `json_path` (string) **REQ** [maxLen=256] — JSON path of the dependee field.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the missing dependent field.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path of the missing dependent field.
                - `expected_fields` (array of object) [maxItems=15] **REQ** — List of expected field descriptors (each with JSON path and API name).
                  - `json_path` (string) **REQ** [maxLen=256] — JSON path of the expected field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the expected field.
                - `ambiguity_due_to` (array of object) [maxItems=15] **REQ** — List of ambiguous field descriptors.
                  - `json_path` (string) **REQ** [maxLen=256] — JSON path of the ambiguous field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the ambiguous field.
          - `message` (string) **REQ** [maxLen=256] — An error message explaining the issue.
          - `status` (string) **REQ** [enum=['error']] — Status indicator, always `error`.

**Scopes:** ZohoCRM.settings.record_locking_configurations.CREATE
