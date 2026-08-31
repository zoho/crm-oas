# PUT /settings/record_locking_configurations
**Operation:** `updateRecordLockingConfiguration` — Update record locking configuration
> Updates an existing record locking configuration for the specified module. You can modify any of the configuration settings.

**Parameters:**
- `module` (query, string, required) [maxLen=256]: The API name of the module for which the record locking configuration is being managed. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module names.

**Request Body** (required) — application/json
  > Request body for updating a record locking configuration.
  - `record_locking_configurations` (array of object) [maxItems=1] **REQ** — Array containing the updated record locking configuration.
    - `lock_type` (string) [enum=['automatic', 'manual', 'both']] — Defines the locking mode. `automatic` locks records based on rules, `manual` requires explicit action, `both` supports both.
    - `locked_for` (string) [enum=['all_profiles', 'all_profiles_except_excluded_profiles']] — Indicates which profiles the lock applies to. Use `all_profiles` for everyone, or `all_profiles_except_excluded_profiles` to exclude specific profiles.
    - `restricted_actions` (array of string) [maxItems=10] — List of actions that are restricted on locked records.
      items: [enum=['change_owner', 'update', 'delete', 'tags'], default=update]
    - `excluded_fields` (array of object) [maxItems=15] — Fields that are exempt from locking. Even if a record is locked, these fields can still be modified.
      - `id` (string/int64) **REQ** — The unique identifier of the field. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve field IDs.
    - `feature_type` (string) [enum=['record_locking'], default=record_locking] — Feature type identifier. Must be `record_locking`.
    - `locking_rules` (array of object) [maxItems=5] — A set of rules that define when records should be automatically locked.
      - `name` (string) **REQ** [maxLen=256] — Unique name for the locking rule.
      - `id` (string) [maxLen=32] — Unique identifier of the locking rule. Required when updating an existing rule.
      - `lock_existing_records` (boolean) [default=False] — If `true`, existing records that match the criteria will also be locked when the rule is saved.
      - `criteria` (object) **REQ** — Criteria that records must satisfy for the rule to apply.
    - `restricted_communications` (array of string) [maxItems=10] — List of communication actions that are restricted for locked records.
      items: [enum=['send_mail']]
    - `id` (string) **REQ** [maxLen=32] — Unique identifier of the record locking configuration to update. This field is required.
    - `lock_excluded_profiles` (array of object) [maxItems=15] — Profiles that are excluded from locking. This property is required when `locked_for` is `all_profiles_except_excluded_profiles`.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Profile ID. Use the [Get Profiles API](profiles.yaml#$.paths./settings/profiles.get) to retrieve profile IDs.
    - `lock_for_portal_users` (boolean) [default=True] — If `true`, portal users are also subject to the locking restrictions.

**Responses:**

- **200**: Successfully updated the record locking configuration for the specified module. [application/json]
    > Response object for a successful configuration update.
    - `record_locking_configurations` (array of object) [maxItems=1] **REQ** — Array containing the update response.
      - `status` (string) **REQ** [maxLen=256, enum=['success']] — Indicates that the update was successful.
      - `code` (string) **REQ** [maxLen=256, enum=['SUCCESS']] — Success code for the operation.
      - `message` (string) **REQ** [maxLen=256] — Informational message about the update.
      - `details` (object) **REQ** — Additional details about the updated configuration.
        - `id` (string) **REQ** [maxLen=256] — Unique identifier of the updated configuration.

- **400**: Bad Request - The request could not be processed due to invalid input, missing parameters, unsupported features, or permission issues. [application/json]
    > Union of a flat error object or an array-wrapped error envelope.
    oneOf:
        - `code` (string) **REQ** [maxLen=256] — Error code identifying the failure reason.
        - `message` (string) **REQ** [maxLen=256] — An error message explaining the issue.
        - `status` (string) **REQ** [enum=['error']] — Status indicator, always `error`.
        - `details` (object) **REQ** — Additional error details that vary by error code.
          oneOf:
              - `param_name` (string) **REQ** [maxLen=256] — Name of the missing parameter.
              - `resource_path_index` (integer/int32) **REQ** — Index of the invalid path element.
              - `permissions` (array of string) [maxItems=1] **REQ** — List of required permissions.
                items: [maxLen=256]
        - `record_locking_configurations` (array of object) [maxItems=10] **REQ** — Array of error objects for the configuration item.
          - `code` (string) **REQ** [maxLen=256] — Error code for the configuration error.
          - `message` (string) **REQ** [maxLen=256] — An error message explaining the issue.
          - `status` (string) **REQ** [enum=['error']] — Status indicator, always `error`.
          - `details` (object) **REQ** — Detailed metadata for the configuration error. The structure varies by error type.
            oneOf:
                - `api_name` (string) **REQ** [maxLen=256] — API name of the field involved.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path to the error location.
                - `supported_values` (array of string) [maxItems=50] **REQ** — List of allowed values.
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
                - `expected_fields` (array of object) [maxItems=50] **REQ** — List of expected field descriptors.
                  - `json_path` (string) **REQ** [maxLen=256] — JSON path of the expected field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the expected field.
                - `ambiguity_due_to` (array of object) [maxItems=50] **REQ** — List of ambiguous field descriptors.
                  - `json_path` (string) **REQ** [maxLen=256] — JSON path of the ambiguous field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the ambiguous field.

**Scopes:** ZohoCRM.settings.record_locking_configurations.UPDATE
