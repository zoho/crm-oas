# GET /settings/record_locking_configurations
**Operation:** `getRecordLockingConfiguration` — Get record locking configuration
> Retrieves the existing record locking configuration for the specified module.

**Parameters:**
- `module` (query, string, required) [maxLen=256]: The API name of the module for which the record locking configuration is being managed. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module names.

**Responses:**

- **200**: Successfully retrieved the record locking configuration details for the specified module. [application/json]
    > Response object containing the record locking configuration details.
    - `record_locking_configurations` (array of object) [maxItems=1] **REQ** — Array containing the record locking configuration details.
      - `lock_type` (string) **REQ** [enum=['automatic', 'manual', 'both']] — The locking mode used for this configuration.
      - `locked_for` (string) **REQ** [enum=['all_profiles', 'all_profiles_except_excluded_profiles']] — Indicates which profiles the lock applies to.
      - `restricted_actions` (array of string) [maxItems=5] **REQ** — List of actions that are restricted on locked records.
        items: [enum=['change_owner', 'update', 'delete', 'tags', 'convert']]
      - `created_time` (string/date-time) **REQ** — Timestamp when the configuration was created.
      - `excluded_fields` (array of object) [maxItems=15] **REQ** — Fields that are exempt from locking.
        - `api_name` (string) **REQ** [maxLen=256] — API name of the excluded field.
        - `id` (string) **REQ** [maxLen=32] — Unique identifier of the excluded field.
      - `feature_type` (string) **REQ** [enum=['record_locking'], default=record_locking] — Feature type identifier (always `record_locking`).
      - `locking_rules` (array of object) [maxItems=5] **REQ** — List of locking rules defined in the configuration.
        - `name` (string) **REQ** [maxLen=256] — Name of the locking rule.
        - `id` (string) **REQ** [maxLen=32] — Unique identifier of the locking rule.
        - `lock_existing_records` (boolean) **REQ** [default=False] — Indicates whether existing records are locked when the rule is applied.
        - `criteria` (object) — Criteria that records must match for the rule to apply.
          - `comparator` (string) **REQ** [maxLen=256] — The comparator used in the criteria.
          - `field` (object) **REQ** — Details of the field used in the criteria.
            - `api_name` (string) **REQ** [maxLen=256] — API name of the field.
            - `id` (string) **REQ** [maxLen=32] — Unique identifier of the field.
          - `type` (string) **REQ** [maxLen=256] — Type of the criteria.
          - `value` (object)
      - `modified_time` (string/date-time) **REQ** — Timestamp when the configuration was last modified.
      - `restricted_communications` (array of string) [maxItems=1] **REQ** — List of communication actions restricted on locked records.
        items: [enum=['send_mail']]
      - `system_defined` (boolean) **REQ** — Indicates whether the configuration is system-defined.
      - `created_by` (object) **REQ** — User who created the configuration.
        - `name` (string) **REQ** [maxLen=256] — Name of the user.
        - `id` (string) **REQ** [maxLen=32] — Unique identifier of the user.
      - `modified_by` (object) **REQ** — User who last modified the configuration.
        - `name` (string) **REQ** [maxLen=256] — Name of the user.
        - `id` (string) **REQ** [maxLen=32] — Unique identifier of the user.
      - `id` (string) **REQ** [maxLen=32] — Unique identifier of the configuration.
      - `restricted_custom_buttons` (array of object) [nullable] **REQ** — List of custom buttons restricted on locked records (may be null).
        - `name` (string) [maxLen=256] — Name of the custom button.
        - `id` (string) **REQ** [maxLen=32] — Unique identifier of the custom button.
      - `lock_excluded_profiles` (array of object) [maxItems=15] **REQ** — Profiles that are excluded from locking.
        - `name` (string) **REQ** [maxLen=256] — Name of the profile.
        - `id` (string) **REQ** [maxLen=32] — Unique identifier of the profile.
      - `lock_for_portal_users` (boolean) **REQ** [default=True] — Indicates whether portal users are subject to locking.

- **204**: No record locking configuration is configured for the specified module.

- **400**: Bad Request - The request could not be processed due to invalid input, missing parameters, unsupported features, or permission issues. [application/json]
    > Error response object.
    - `code` (string) **REQ** [maxLen=256, enum=[5 values]] — Error code identifying the failure reason.
    - `message` (string) **REQ** [maxLen=256] — An error message explaining the issue.
    - `status` (string) **REQ** [enum=['error']] — Status indicator, always `error`.
    - `details` (object) **REQ** — Additional error details that vary by error code.
      oneOf:
          - `param_name` (string) **REQ** [maxLen=256] — Name of the missing parameter.
          - `resource_path_index` (integer/int32) **REQ** — Index of the invalid path element.
          - `permissions` (array of string) [maxItems=1] **REQ** — List of required permissions.
            items: [maxLen=256, enum=['Crm_Implied_Customize_Zoho_CRM']]

**Scopes:** ZohoCRM.settings.record_locking_configurations.READ
