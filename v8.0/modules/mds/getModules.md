# GET /settings/modules
**Operation:** `getModules` — Retrieve modules
> Retrieves the list of all modules available in the Zoho CRM account, including standard, custom, subform, and linking (MxN) modules. Supports optional filtering by `status`, `feature_name`, and `include` to control the scope and depth of the response. When both `status` and `feature_name` are provided, modules must satisfy both criteria. Returns all matching modules in a single response without pagination.

**Parameters:**
- `status` (query, string, optional) [maxLen=56, pattern=^(visible|scheduled_for_deletion|user_hidden|system_hidden)(,(visible|scheduled_for_deletion|user_hidden|system_hidden))*$]: Specify the visibility status to filter the modules returned in the response. Accepts comma-separated values to retrieve modules matching any of the specified statuses. This is case-sensitive.
- `feature_name` (query, string, optional) [enum=[863 values]]: Specify the feature name to filter modules associated with a specific CRM feature.This is case-sensitive and follows snake_case format. An empty string returns 400 error
- `include` (query, string, optional) [maxLen=3000, pattern=^(custom_view|related_lists|business_card_fields|layouts|fields)(,(custom_view|related_lists|business_card_fields|layouts|fields))*$]: Specify the additional module metadata fields to include in the response. Accepts comma-separated values. Allows retrieving optional module metadata that is not returned by default.
- `fields` (query, array, optional) [maxItems=100] {style=form, explode=False}: Specify the module property names to include in the response. Accepts an array of property names to filter the returned module fields.

**Responses:**

- **200**: Returns all modules in the Zoho CRM account with their configuration details, permissions, fields, layouts, and related lists. All matching modules are included in a single response without pagination. [application/json]
    > Response body containing the array of module metadata objects.
    - `modules` (array of object) [maxItems=600] **REQ** — Array of module metadata objects returned for the Zoho CRM account, up to 600 entries, each containing configuration, capabilities, fields, layouts, profiles, and permissions.
      - `global_search_supported` (boolean) — Indicates whether global search functionality is supported for this module.
      - `public_fields_configured` (boolean) — Indicates whether public fields have been configured for this module.
      - `recycle_bin_on_delete` (boolean) — Indicates whether deleted records are moved to the recycle bin instead of being permanently deleted.
      - `has_more_profiles` (boolean) — Indicates whether more profiles exist beyond those returned in the current response.
      - `sub_menu_available` (boolean) — Whether a submenu is available for this module in the navigation.
      - `lookupable` (boolean) — Indicates whether this module can be used as a lookup target in other modules.
      - `profile_count` (integer/int32) — Represents the number of profiles associated with this module; 0 indicates no profile assignments.
      - `module_type` (string) [enum=['CONFIGURATION_ENTITIES', 'ENTITIES']] — Represents the type classification of the module; exposed only for pathfinder and orchestration modules. Possible values: `CONFIGURATION_ENTITIES`, `ENTITIES`.
      - `cc_enabled` (boolean) — Whether CommandCenter functionality is enabled for email communications in this module; exposed only for orchestration modules and not applicable for API-supported modules.
      - `deletable` (boolean) — Indicates whether records in this module can be deleted.
      - `description` (string) [maxLen=255, nullable] — User-defined description of the module, up to 255 characters; null when no description has been set.
      - `creatable` (boolean) — Indicates if new records can be created in this module.
      - `inventory_template_supported` (boolean) — Indicates whether inventory templates are supported for this module.
      - `modified_time` (string/date-time) [nullable] — Timestamp of the most recent modification to the module, returned as a timezone-aware date-time string; null if the module has never been modified.
      - `presence_sub_menu` (boolean) — Indicates whether this module has a presence submenu option.
      - `triggers_supported` (boolean) — Whether workflow triggers are supported for this module.
      - `id` (string/int64) **REQ** — Represents the unique identifier for the module.
      - `api_name` (string) [maxLen=50] — Unique API identifier for the module used in third-party integrations; starts with a letter, contains only alphanumeric characters and underscores, and has no consecutive or trailing underscores.
      - `plural_label` (string) [maxLen=50] — Plural display label for the module; returns the translated label when translation is enabled, otherwise matches `actual_plural_label`.
      - `actual_plural_label` (string) [maxLen=50] — Original plural label of the module as stored in the database, without any translation applied.
      - `actual_singular_label` (string) [maxLen=50] — Original singular label of the module as stored in the database, without any translation applied.
      - `singular_label` (string) [maxLen=50] — Singular display label for the module; returns the translated label when translation is enabled, otherwise matches `actual_singular_label`.
      - `isBlueprintSupported` (boolean) — Indicates whether Blueprint (process automation) is supported for this module.
      - `visibility` (integer/int32) — Bitwise feature visibility flags for the module; the base value 1 indicates fully visible. Add flag values to hide specific features: 2=WEBUIHIDDEN, 4=TABMENU, 8=LOOKUP, 16=RELATEDLIST, 32=MULTISELECTLOOKUP, 64=MODULE_SETTING, 128=AUTOMATION, 256=TEMPLATES, 512=IMPORT, 1024=EXPORT, 4096=REPORT, 8192=API.
      - `convertable` (boolean) — Whether records in this module can be converted to another module type.
      - `editable` (boolean) — Whether records in this module can be edited by users.
      - `emailTemplate_support` (boolean) — Indicates whether Email Templates functionality is supported for this module.
      - `email_parser_supported` (boolean) — Indicates whether email parsing is supported for this module.
      - `filter_supported` (boolean) — Indicates whether records in this module can be filtered.
      - `show_as_tab` (boolean) — Indicates whether the module appears as a tab in the main navigation.
      - `web_link` (string) [nullable] — URL for web tab modules; supports dynamic parameter substitution via the arguments array.
      - `viewable` (boolean) — Whether records in this module can be viewed.
      - `api_supported` (boolean) — Whether API operations are supported for this module.
      - `quick_create` (boolean) — Indicates whether the quick create form is available for this module.
      - `generated_type` (string) [enum=[9 values]] — Method by which this module was generated or created.
      - `static_subform_properties` (object) — Configuration properties for static subform modules, including the list of field references.
        - `fields` (array of object) [maxItems=25] **REQ** — Array of field references included in the static subform, up to 25 entries.
          - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the static subform field.
          - `id` (string/int64) **REQ** — Represents the unique identifier of the static subform field.
      - `feeds_required` (boolean) — Indicates whether activity feeds are required for this module.
      - `scoring_supported` (boolean) — Indicates whether lead or record scoring functionality is supported for this module.
      - `webform_supported` (boolean) — Whether webform integration is supported for this module.
      - `arguments` (array of object) [maxItems=50, nullable] — Array of argument objects used to substitute dynamic parameters in web tab URLs; for example, `https://...&id=${Users.User Id}&name=${Users.First Name}`. Duplicates are allowed, up to 50 entries.
        - `name` (string) **REQ** [maxLen=50] — Key used in the web tab URL template to identify the substitution parameter.
        - `value` (string) **REQ** [maxLen=100] — Field substitution reference expression (for example, `users.recordId`) resolved at runtime for web tab URL parameter substitution.
      - `module_name` (string) [maxLen=50] — Represents the display name of the module.
      - `business_card_field_limit` (integer/int32) [min=0] — Maximum number of fields that can be displayed on the business card view for this module; must be a non-negative integer.
      - `access_type` (string) [enum=['org_based', 'team_based']] — Access control type for the module; `org_based` grants organization-wide access and `team_based` grants team-specific access. This value is immutable after module creation and cannot be updated via PUT operations.
      - `private_profile` (object) — Private profile configuration for the module, containing the profile identifier and name.
        - `name` (string) **REQ** [maxLen=101] — Name of the private profile associated with the module.
        - `id` (string/int64) **REQ** — Unique identifier of the private profile associated with the module.
      - `track_current_data` (boolean) — Whether current data tracking is enabled for this module.
      - `modified_by` (object)
        oneOf:
            - `name` (string) **REQ** [maxLen=101] — Represents the name of the user who last modified the module.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the user who last modified the module.
            type: null — Null value indicating the module has never been modified.
      - `profiles` (array of object) [maxItems=203] — List of profiles that have permission to view this module; may be empty for certain module types, with up to 203 entries.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the profile.
        - `name` (string) **REQ** [maxLen=50] — Represents the display name of the profile.
      - `parent_module` (object) — Reference to the parent module if this is a child or related module; an empty object `{}` for standalone modules, `null` in some cases, or an object with `api_name` and `id` for child modules.
        - `api_name` (string) [maxLen=50] — Represents the API name of the parent module.
        - `id` (string/int64) — Represents the unique identifier of the parent module.
      - `status` (string) [enum=['visible', 'scheduled_for_deletion', 'user_hidden', 'system_hidden']] — Lifecycle state of the module. Possible values: `visible`, `user_hidden`, `system_hidden`, `scheduled_for_deletion`. This status is separate from the numeric bitwise `visibility` flags. It does not itself enable/disable individual features.
      - `sequence_number` (integer/int32) — Represents the display order of the module in the navigation list.
      - `territory` (object) — Territory assignment for the module, containing the territory identifier, name, and subordinates flag.
        - `name` (string) **REQ** [maxLen=100] — Name of the territory; for example, "All Territories" when the ID is 0.
        - `id` (string/int64) **REQ** — Unique identifier of the territory; 0 indicates the special "All Territories" territory.
        - `subordinates` (boolean) **REQ** — Whether subordinate territories are included in this territory assignment.

- **204**: No modules match the specified filter criteria.

- **400**: Bad request returned when the `status` parameter contains unsupported values or when `feature_name` is provided as an empty string. [application/json]
    > Contains the error response when the request contains invalid parameter values.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid data in the request. Always `INVALID_DATA`.
        - `details` (object) **REQ** — Details about the validation error, including the parameter name, the invalid value index, and the list of supported values.
          - `index` (integer/int32) **REQ** — Zero-based index of the invalid value in the comma-separated `status` parameter.
          - `supported_values` (array of string) [maxItems=10, uniqueItems] **REQ** — Unordered list of valid status values; each value appears exactly once, up to 10 entries.
            items: [maxLen=50]
          - `param_name` (string) **REQ** [enum=['status']] — Name of the parameter that contains the invalid value. Always `status` for this error variant.
        - `message` (string) **REQ** [maxLen=1000] — A message describing the validation failure for the invalid status parameter.
        - `status` (string) **REQ** [enum=['error']] — Status of the request. Always `error` for failed requests.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid data in the request. Always `INVALID_DATA`.
        - `details` (object) **REQ** — Empty details object returned when the `feature_name` parameter is provided as an empty string.
        - `message` (string) **REQ** [maxLen=1000] — A message describing the validation failure for the empty feature_name parameter.
        - `status` (string) **REQ** [enum=['error']] — Status of the request. Always `error` for failed requests.

**Scopes:** ZohoCRM.settings.modules.READ
