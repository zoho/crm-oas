# GET /settings/modules/{moduleIdentifier}
**Operation:** `getModuleByApiName` — Get module metadata by API name
> Retrieves complete metadata for a specific CRM module identified by its API name, including fields, layouts, profiles, related lists, and feature capabilities. Returns 204 when the module is not available through this endpoint, or 400 when the identifier is invalid or the module is unsupported

**Parameters:**
- `moduleIdentifier` (path, object, required): Specify the module identifier, either the numeric module ID or the module API name(case-sensitive).
- `fields` (query, array, optional) [maxItems=100] {style=form, explode=False}: Specify the module property names to include in the response. Accepts an array of property names to filter the returned module fields.
- `include_inner_details` (query, string, optional) [maxLen=512] {style=form, explode=False}: Specify the nested field paths to include additional inner details in the module response. Accepts comma-separated values. Allows requesting extra metadata beyond the default module fields(for example fields.lookup.query_details.criteria.)

**Responses:**

- **200**: 200 OK - Module metadata retrieved successfully; returns the full configuration object for the requested CRM module [application/json]
    > Complete configuration metadata for a single CRM module, including its fields, layouts, profiles, related lists, and supported capabilities
    - `modules` (array of object) [maxItems=1] **REQ** — Array of module metadata objects returned for the specified API name. Contains at most one element, as each API name maps to a single module.
      - `global_search_supported` (boolean) — True when records in this module appear in global search results; false when the module is excluded from global search.
      - `public_fields_configured` (boolean) — True when public fields have been configured for this module.
      - `recycle_bin_on_delete` (boolean) — True when deleted records are moved to the recycle bin instead of being permanently deleted.
      - `has_more_profiles` (boolean) — True when the profiles array is truncated and additional profiles exist beyond those returned (pagination indicator); false when the full profile list is included.
      - `sub_menu_available` (boolean) — True when a submenu is available for this module in the UI navigation
      - `lookupable` (boolean) — True when this module can be targeted as a lookup field by other modules.
      - `profile_count` (integer/int32) — Count of profiles assigned to this module; 0 indicates no profile assignments are configured. Maximum 203 profiles per module.
      - `module_type` (string) [enum=['CONFIGURATION_ENTITIES', 'ENTITIES']] — Categorizes the module as ENTITIES for standard data modules or CONFIGURATION_ENTITIES for configuration and settings modules.
      - `cc_enabled` (boolean) — True when CommandCenter (workflow orchestration) is enabled for this module; false when not configured or unsupported.
      - `deletable` (boolean) — True when records in this module can be permanently deleted; false for protected modules such as configuration entities or system-managed records.
      - `description` (string) [maxLen=255, nullable] — User-defined description of the module. Null when no description has been set. Maximum 255 characters; empty string should not be used.
      - `source` (string) [enum=['crm', 'platform_plugin', 'marketplace_plugin', 'campaign_integration']] — Origin of the module configuration. Possible values: crm - native CRM module; platform_plugin - module from a platform plugin; marketplace_plugin - module from a marketplace plugin; campaign_integration - module created via campaign integration
      - `creatable` (boolean) — True when new records can be created in this module; false for read-only modules such as analytics or configuration entities.
      - `inventory_template_supported` (boolean) — True when inventory templates (e.g., for quotes, invoices) can be configured for this module; false when not supported.
      - `modified_time` (string/date-time) [nullable] — ISO 8601 timestamp with timezone offset recording when the module configuration was last modified. Null when the module has never been modified after creation.
      - `presence_sub_menu` (boolean) — True when the presence submenu is available for this module.
      - `triggers_supported` (boolean) — True when workflow triggers are supported for this module
      - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for this module. Required field; used as the stable reference across all API operations.
      - `api_name` (string) [maxLen=50] — Case-sensitive API name used to reference this module in API requests (e.g., 'Leads', 'Contacts', 'CustomModule1').
      - `plural_label` (string) [maxLen=50] — Localized plural display label for the module as shown in the UI, reflecting the active language setting. Maximum 50 characters.
      - `actual_plural_label` (string) [maxLen=50] — System-level plural label for the module as stored in the database, representing the untranslated base value. Maximum 50 characters.
      - `actual_singular_label` (string) [maxLen=50] — System-level singular label for the module as stored in the database, representing the untranslated base value. Maximum 50 characters.
      - `singular_label` (string) [maxLen=50] — Localized singular display label for the module, up to 50 characters
      - `isBlueprintSupported` (boolean) — True when Blueprint process automation can be configured for this module; false when Blueprint is not available for this module type.
      - `visibility` (integer/int32) [min=1, max=16383] — Bitwise integer flags controlling module and feature visibility, ranging from 1 to 16383. Base value 1 means fully visible. Add flag values to suppress specific UI surfaces: 2=web UI hidden, 4=tab menu, 8=lookup, 16=related list, 32=multi-select lookup, 64=module settings, 128=automation, 256=templates, 512=import, 1024=export, 4096=reports, 8192=API. 
      - `convertable` (boolean) — True when records in this module can be converted to records in another module (e.g., Leads to Contacts/Accounts).
      - `editable` (boolean) — True when existing records in this module can be edited by users with appropriate permissions; false for read-only modules.
      - `emailTemplate_support` (boolean) — True when email templates can be used to send emails from records in this module; false when email template functionality is not supported.
      - `email_parser_supported` (boolean) — True when email parsing is supported for this module, enabling automatic record creation or updates from inbound emails.
      - `filter_supported` (boolean) — True when this module supports custom view filtering; false for modules that do not allow filter configuration.
      - `show_as_tab` (boolean) — True when this module is rendered as a tab in the navigation UI
      - `web_link` (string) [nullable] — URL associated with this module; null when no web link is configured
      - `viewable` (boolean) — True when records in this module can be viewed by the current user
      - `api_supported` (boolean) — True when the module is accessible via the Zoho CRM API; false for modules that are not externally queryable through API endpoints.
      - `quick_create` (boolean) — True when quick create functionality is enabled for this module.
      - `generated_type` (string) [enum=[8 values]] — Classification of how this module was generated. Possible values: default - standard system module; custom - user-created module; web - web tab module; linking - many-to-many linking module; subform - dynamic subform module; static_subform - static subform; field_tracker - field change tracker; picklisttracker - picklist change tracker.
      - `static_subform_properties` (object) — Static subform configuration properties defined for fields within this module
        - `fields` (array of object) [maxItems=1000] **REQ** — Field references included in the static subform, up to 1000 items
          - `api_name` (string) **REQ** [maxLen=50] — API name of the static subform field, up to 50 characters
          - `id` (string/int64) **REQ** — Unique numeric identifier of the static subform field, returned as a string
      - `feeds_required` (boolean) — True when activity feeds are enabled for this module, displaying a timeline of record activities and updates.
      - `scoring_supported` (boolean) — True when lead or contact scoring is supported for this module
      - `webform_supported` (boolean) — True when web forms can be created for this module
      - `arguments` (array of object) [maxItems=10] — Array of argument objects (up to 10) used to substitute dynamic parameters in web tab URLs (e.g., https://...&id=${Users.User Id}&name=${Users.First Name}). Duplicates are allowed and order is preserved for multi-occurrence parameters; empty for non-web-tab modules.
        - `name` (string) **REQ** [maxLen=50] — Key name of the URL argument used as a placeholder in the web tab URL template. Maximum 50 characters.
        - `value` (string) **REQ** [maxLen=100] — Field substitution reference expression resolving to a CRM field value at runtime (e.g., users.recordId). Maximum 100 characters.
      - `module_name` (string) [maxLen=50] — System-level API name identifying the module, used in API requests and responses. Maximum 50 characters.
      - `business_card_field_limit` (integer/int32) [min=0] — Maximum number of fields allowed in the business card view for this module. Non-negative integer; 0 means no fields are configured.
      - `access_type` (string) [enum=['org_based', 'team_based']] — Access control scope for the module. Possible values: org_based - organization-wide access; team_based - team-specific access. Immutable after module creation; cannot be changed via PUT.
      - `private_profile` (object) — Private profile configuration for team-based access control. Populated only when access_type is 'team_based' with profile name and ID; null for org_based modules.
        - `name` (string) **REQ** [maxLen=101] — Display name of the private profile; maximum 101 characters.
        - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the private profile.
      - `track_current_data` (boolean) — True when current data tracking is enabled for records in this module
      - `modified_by` (object) — Represents the user who last modified this module configuration.
        oneOf:
            - `name` (string) **REQ** [maxLen=101] — Name of the user who modified the custom view.
            - `id` (string/int64) **REQ** — Unique identifier of the user who modified the custom view.
            type: null — Indicates that has never been modified.
      - `profiles` (array of object) [maxItems=203] — Profiles with access to this module; contains up to 203 entries.
        - `id` (string/int64) **REQ** — Unique numeric identifier of the profile (as string).
        - `name` (string) [maxLen=50] — Display name of the profile; maximum 50 characters.
      - `parent_module` (object) — Reference to the parent module for child modules such as subforms and field trackers. Returns an empty object {} for standalone modules. This is populated with api_name and id for modules with parent relationships.
        - `api_name` (string) [maxLen=50] — API name of the parent module, used to identify it in API calls. Maximum 50 characters.
        - `id` (string/int64) — Unique numeric identifier (as string) of the parent module.
      - `$field_states` (array of string) [maxItems=1, nullable] — Nullable array of field-state identifiers (up to 1 entry, max 20 characters each) that govern dynamic field visibility and validation rules within this module.
        items: [maxLen=20]
      - `business_card_fields` (array of object) [maxItems=15] — Fields displayed in the business card view (up to 15). Present only when 'business_card_fields' is included in the include parameter. Can be empty array, array of objects with api_name and id, or array of string API names.
        oneOf:
            - `api_name` (string) **REQ** [maxLen=50] — API name of the field
            - `id` (string/int64) **REQ** — Unique identifier of the field
            type: string [maxLen=50] — Field API name
      - `per_page` (integer/int32) — Default number of records displayed per page when listing data for this module.
      - `$properties` (array of object) [maxItems=50, nullable] — Nullable array of extended property objects (up to 50) representing additional module capabilities; each item is either a string property name or an object with arbitrary key-value pairs.
        oneOf:
            type: string [maxLen=50] — Property name identifier
            additionalProperties: any
      - `$on_demand_properties` (array of string) [maxItems=100, nullable] — Nullable array of string identifiers (up to 100, max 50 chars each) for module properties that are loaded on-demand rather than included in the default response.
        items: [maxLen=50]
      - `search_layout_fields` (array of string) [maxItems=10] — Up to 10 fields displayed in the search result layout for this module
        items: [maxLen=25]
      - `kanban_view_supported` (boolean) — True when the module's data structure supports kanban view. A false value means kanban view cannot be enabled regardless of settings.
      - `lookup_field_properties` (object) [nullable] — Configuration properties governing lookup field behavior for this module. Null when the module has no lookup field configuration.
      - `kanban_view` (boolean) — True when kanban view is currently enabled for this module. Distinct from kanban_view_supported, which reflects capability regardless of current setting.
      - `chart_view` (boolean) — True when chart view is currently enabled for this module. Distinct from chart_view_supported, which reflects capability.
      - `chart_view_supported` (boolean) — True when the module's data structure supports chart visualization. A false value means chart view cannot be enabled regardless of settings.
      - `related_lists` (array of object) [maxItems=2147483647] — Related lists (subforms and related modules) displayed in this module's detail view; populated only when 'related_lists' is included in the include query parameter.
        - `id` (string/int64) **REQ** — Unique numeric identifier of the related list, returned as a string.
        - `sequence_number` (string/int32) **REQ** — Display position of this related list; lower values appear first.
        - `display_label` (string) **REQ** [maxLen=50] — UI display label for this related list. Maximum 50 characters.
        - `api_name` (string) **REQ** [maxLen=50] — API name used to reference this related list programmatically, up to 50 characters.
        - `module` (object) [nullable] — Module details associated with this related list entry, including its name and metadata; null if no module is linked.
        - `name` (string) **REQ** [maxLen=50] — System-level name identifying the related list module; maximum 50 characters.
        - `action` (string) **REQ** [maxLen=64, nullable] — Action URL or operation identifier associated with this related list, up to 64 characters; null when no action is defined.
        - `href` (string) **REQ** [maxLen=2048, minLen=1, nullable] — Reference URL for the related list, or null if not applicable. Between 1 and 2048 characters when present.
        - `type` (string) **REQ** [enum=[9 values]] — Classification of this related list. Possible values: default - standard related list; multiselectlookup - multi-select lookup; combined_view - combined view; custom_lookup - custom lookup; custom_related_list - custom related list; slyteui - Slyte UI; queries - query-based; custom_function - function-based; grouped - grouped list.
        - `connectedlookupApiName` (string) [maxLen=50] — API name of the connected lookup field linking this related list to another module, up to 50 characters.
        - `field_enabled` (boolean) — True when this related list field is enabled and active.
        - `customize_sort` (boolean) **REQ** — True when sorting for this related list can be customized.
        - `customize_fields` (boolean) **REQ** — True when fields in this related list can be customized.
        - `customize_display_label` (boolean) **REQ** — True when the display label for this related list can be customized.
        - `status` (string) **REQ** [enum=['visible']] — Visibility status of this related list; currently only 'visible' is supported.
        - `sort_by` (object) — Field by which records in this related list are sorted by default; contains the field's API name and unique identifier.
          - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the field used for sorting records in this related list.
          - `api_name` (string) **REQ** [maxLen=50] — API name of the field used for sorting, up to 50 characters.
        - `sort_order` (string) [enum=['asc', 'desc', None], nullable] — Sort direction applied to records in this related list. Possible values: asc - ascending; desc - descending; null - no sort order configured.
        - `fields` (array of object) [maxItems=1000] — List of fields displayed in this related list. Maximum 1000 items.
          - `id` (string/int64) **REQ** — Unique numeric identifier of the field, returned as a string.
          - `api_name` (string) **REQ** [maxLen=50] — API name of the field used in programmatic access. Maximum 50 characters.
        - `visibility` (integer/int32) — Numeric code controlling where this related list appears or is hidden in the UI
        - `personality_name` (string) [maxLen=50] — Personality name assigned to this related list configuration, distinguishing its behavioral variant; maximum 50 characters.
        - `record_operations` (object) — Set of allowed record-level operations within this related list, such as create, edit, and assign.
          - `edit` (boolean) **REQ** — True when editing of records within this related list is permitted for the current user.
          - `create` (boolean) **REQ** — True when creation of records within this related list is permitted for the current user.
          - `bulk_edit` (boolean) **REQ** — True when bulk edit of records in this related list is permitted for the current user.
          - `delete` (boolean) **REQ** — True when deletion of associated records from this related list is permitted for the current user.
          - `disassociate` (boolean) **REQ** — True when disassociation of records from this related list is permitted for the current user.
          - `assign` (boolean) **REQ** — True when the assign operation is permitted for records in this related list.
        - `connectedmodule` (string) [maxLen=250, minLen=1, pattern=^[A-Za-z0-9_]+$, nullable] — API name of the connected module for this related list; null when no module connection exists. Between 1 and 250 alphanumeric or underscore characters when present.
        - `linkingmodule` (string) [maxLen=250, minLen=1, pattern=^[A-Za-z0-9_]+$, nullable] — API name of the linking module associated with this related list; null when no linking module is configured. Between 1 and 250 alphanumeric or underscore characters when present.
        - `parent_related_lists` (array of object) [maxItems=100, nullable] — Array of parent related list references when this entry is nested within another related list; null for top-level related lists. Maximum 100 items.
          - `api_name` (string) **REQ** [maxLen=50] — API name of the parent related list containing this entry; maximum 50 characters.
          - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the parent related list.
        - `_layout_specific_properties` (array of object) [maxItems=2147483647] — Per-layout configuration entries governing how this related list appears within each associated layout; contains up to 2,147,483,647 items.
          - `sequence_number` (integer/int32) **REQ** — Numeric position defining the display order of this related list within its associated layout.
          - `layout` (object) **REQ** — Layout reference object identifying the specific layout to which this related list configuration applies.
            - `name` (string) [maxLen=40] — Display name of the layout, up to 40 characters.
            - `id` (string/int64) — Unique numeric identifier (as string) for the layout.
          additionalProperties: any
      - `filter_status` (boolean) — True when custom view filters are currently active for this module; false when no active filter state is set.
      - `related_list_properties` (object) [nullable] — Configuration and settings for related lists in this module; null when no related-list properties are defined.
      - `display_field` (object) — Field designation used as the record display name or title in this module. Either a string containing the field's API name, or an object with api_name and id.
        oneOf:
            type: string [maxLen=50] — API name of the display field
            - `api_name` (string) **REQ** [maxLen=50] — API name of the display field
            - `id` (string/int64) **REQ** — Unique identifier of the display field
            type: null — No display field configured
      - `layouts` (array of object) [maxItems=7] — Array of layout configuration objects (up to 7) available for this module, ordered by relevance of profiles and record creation for the current user. Populated only when 'layouts' is included in the include query parameter.
        - `has_more_profiles` (boolean) — True when additional profiles beyond the current page are associated with this layout, signaling that further pagination is required.
        - `created_time` (string/date-time) [nullable] — ISO 8601 timestamp with timezone offset recording when the layout was created; nullable.
        - `modified_time` (object) — Represents the timestamp when this layout was last modified, in ISO 8601 format.
          oneOf:
              type: string/date-time — Timestamp when layout was last modified in ISO 8601 format with timezone offset. Null if never modified.
              type: null — Indicates that has never been modified.
        - `visible` (boolean) — True when the layout is visible and accessible to users.
        - `source` (string) **REQ** [enum=['crm', 'platform_plugin', 'marketplace_plugin', 'campaign_integration']] — Source system that originated the layout configuration. Possible values: crm, platform_plugin, marketplace_plugin, campaign_integration.
        - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for the layout.
        - `name` (string) **REQ** [maxLen=40] — Internal API name of the layout. Maximum 40 characters.
        - `api_name` (string) [maxLen=40] — API name used to reference this layout in API requests. Maximum 40 characters.
        - `display_label` (string) **REQ** [maxLen=40] — Human-readable label displayed in the UI for this layout. Maximum 40 characters.
        - `status` (string) **REQ** [enum=['active', 'inactive', 'downgraded', 'hidden']] — Current lifecycle state of the layout. Possible values: active - in use; inactive - disabled; downgraded - reduced to simpler type; hidden - not visible in UI.
        - `show_business_card` (boolean) — True when the business card view is enabled for this layout.
        - `generated_type` (string) **REQ** [enum=[10 values]] — Classification of how the layout was generated. Possible values: default - standard system layout; custom - user-created; web - web tab; linking - many-to-many; subform - dynamic subform; static_subform - static subform; orchestration - CommandCenter; field_tracker - field change tracker; webtab_slyteui - Slyte UI web tab; system - core system layout.
        - `created_for` (string) [maxLen=100, nullable] — Identifier of the entity (user, profile, or role) for which this layout was created. Maximum 100 characters. Null if created for general use.
        - `convert_mapping` (object) — Conversion mapping configuration defining target modules (Accounts, Contacts, Deals) and field-level mappings when records in this module are converted. Populated only when 'convert_mapping' is included in the include parameter.
          - `Contacts` (object) — Configuration object for converting this module's records to Contacts, including the Contacts module's display label, id, and internal name.
            - `display_label` (string) **REQ** [maxLen=40] — Human-readable display label for the Contacts module shown in the conversion UI. Maximum 40 characters.
            - `name` (string) **REQ** [maxLen=40] — Internal system name of the Contacts module. Maximum 40 characters.
            - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for the Contacts module used as the conversion target.
          - `Deals` (object) — Configuration object for converting this module's records to Deals, including the Deals module's display label, id, internal name, and an array of field-level mapping configurations.
            - `fields` (array of object) [maxItems=1000] **REQ** — Array of field mapping objects (up to 1000) specifying how source module fields map to Deals fields during conversion; each entry contains the Deals field api_name, display label, id, and whether the field is required.
              - `api_name` (string) **REQ** [maxLen=50] — API name of the target Deals field in this mapping. Maximum 50 characters.
              - `field_label` (string) **REQ** [maxLen=100] — Human-readable display label for the Deals field in the conversion UI. Maximum 100 characters.
              - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the Deals field in this mapping.
              - `required` (boolean) **REQ** — True when this Deals field must be populated during the record conversion process; false when it is optional.
            - `display_label` (string) **REQ** [maxLen=40] — Human-readable display label for the Deals module shown in the conversion UI. Maximum 40 characters.
            - `name` (string) **REQ** [maxLen=40] — API name used internally to identify the Deals module within the conversion mapping. Maximum 40 characters.
            - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for the Deals module used as the conversion target.
          - `Accounts` (object) — Configuration object for converting this module's records to Accounts, including the Account module's display label, id, and internal name.
            - `display_label` (string) **REQ** [maxLen=40] — Human-readable display label for the Accounts module shown in the conversion UI. Maximum 40 characters.
            - `name` (string) **REQ** [maxLen=40] — Internal system name of the Accounts module. Maximum 40 characters.
            - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for the Accounts module used as the conversion target.
          - `Invoices` (object) — Conversion target configuration object for the Invoices module, containing display label and identifier details.
            - `display_label` (string) **REQ** [maxLen=40] — Human-readable label displayed for the Invoices module in the conversion mapping. Maximum 40 characters.
            - `name` (string) **REQ** [maxLen=40] — API name used internally to identify the Invoices module within the conversion mapping. Maximum 40 characters.
            - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for the Invoices module in the conversion mapping.
          - `SalesOrders` (object) — Conversion target configuration object for the SalesOrders module, containing display label and identifier details.
            - `display_label` (string) **REQ** [maxLen=40] — Human-readable label displayed for the SalesOrders module in the conversion mapping. Maximum 40 characters.
            - `name` (string) **REQ** [maxLen=40] — API name used internally to identify the SalesOrders module within the conversion mapping. Maximum 40 characters.
            - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for the SalesOrders module in the conversion mapping.
        - `modified_by` (object) — Represents the user who last modified this layout.
          oneOf:
              - `name` (string) **REQ** [maxLen=101] — Name of the user who modified the custom view.
              - `id` (string/int64) **REQ** — Unique identifier of the user who modified the custom view.
              type: null — Indicates that has never been modified.
        - `profiles` (array of object) [maxItems=202] — Array of user profile objects (up to 202) that have access to this layout, each containing profile id, name, and default view configuration.
          - `default` (boolean) **REQ** — True when this profile serves as the default profile for the layout.
          - `name` (string) **REQ** [maxLen=50] — Name identifying the profile associated with this layout. Maximum 50 characters.
          - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for this profile.
          - `_default_view` (object) **REQ** — Default custom view configuration applied to this profile, determining the initial view presented to users accessing records.
            - `name` (string) **REQ** [maxLen=40] — Display name of the default custom view. Maximum 40 characters.
            - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the default view associated with this profile.
            - `type` (string) **REQ** [enum=['inventory_templates', 'layout', 'canvas', 'wizard']] — Category of the default custom view. Possible values: inventory_templates, layout, canvas, wizard.
          - `_default_assignment_view` (object) **REQ** — Default assignment view configuration applied when records are assigned under this profile, controlling how record assignment operations are presented.
            - `name` (string) **REQ** [maxLen=40] — Display name of the default assignment view. Maximum 40 characters.
            - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the default assignment view associated with this profile.
            - `type` (string) **REQ** [enum=['inventory_templates', 'layout', 'canvas', 'wizard']] — Category of the default assignment view. Possible values: inventory_templates, layout, canvas, wizard.
        - `created_by` (object) — User who created this layout, containing id and name. Null when created by the system.
          - `name` (string) **REQ** [maxLen=101] — Full name of the user who created the layout. Maximum 101 characters.
          - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the user who created the layout.
        - `sections` (array of object) [maxItems=7] — Ordered list of sections grouping fields within the layout. Maximum 7 sections.
        - `actions_allowed` (object) — Object enumerating the operations that the current user can perform on this layout, including flags for clone, deactivate, delete, downgrade, edit, rename, and configure permissions.
          - `edit` (boolean) **REQ** — True when the current user has permission to edit the fields and settings of this layout.
          - `rename` (boolean) **REQ** — True when the current user has permission to rename this layout.
          - `clone` (boolean) **REQ** — True when the current user has permission to clone this layout.
          - `downgrade` (boolean) **REQ** — True when the current user has permission to downgrade this layout to a simpler layout type.
          - `delete` (boolean) **REQ** — True when the current user has permission to delete this layout.
          - `deactivate` (boolean) **REQ** — True when the current user has permission to deactivate this layout.
          - `set_layout_permissions` (boolean) **REQ** — True when the current user has permission to configure profile-based access permissions for this layout.
      - `fields` (array of object) [maxItems=1000] — Array of complete field metadata objects (up to 1000) for all fields in this module. Populated only when 'fields' is included in the include query parameter and when the service is creator.
      - `custom_view` (object) — Default custom view configuration for the module, including filter criteria, display fields, sort settings, and sharing options. Exposed only when 'custom_view' is included in the include parameter.
        - `cross_filters` (array of object) [minItems=1, maxItems=3] — Array of cross-module filter objects enabling advanced filtering based on related module conditions (e.g., filter Contacts by associated Deals criteria).
        - `$modified_criteria` (boolean) — True when the filter criteria of this custom view have been modified from their original configuration.
        - `display_value` (string) **REQ** [maxLen=100] — Human-readable label for the custom view as displayed in the CRM UI. Maximum 100 characters.
        - `system_name` (string) **REQ** [maxLen=255, nullable] — Internal system name for this custom view, stored separately from the user-visible display_value. Nullable; maximum 255 characters.
        - `category` (string) **REQ** [enum=['created_by_me', 'shared_with_me', 'public_views']] — Integer code representing the sharing category of the custom view (e.g., private, shared_with_everyone, shared_with_roles).
        - `created_time` (string/date-time) **REQ** [nullable] — ISO 8601 datetime when the custom view was created, including timezone offset (e.g., 2025-11-20T14:30:00+05:30). Null for system views.
        - `modified_time` (object) **REQ** — Represents the timestamp when this Custom View was last modified, in ISO 8601 format.
          oneOf:
              type: string/date-time — Timestamp when layout was last modified in ISO 8601 format with timezone offset. Null if never modified.
              type: null — Indicates that has never been modified.
        - `last_accessed_time` (string/date-time) **REQ** [nullable] — ISO 8601 datetime when this view was last accessed, including timezone offset. Null if never accessed after creation.
        - `name` (string) **REQ** [maxLen=100] — System name identifier for the custom view, distinct from display_value. Maximum 50 characters.
        - `created_by` (object) **REQ** — User object identifying who created this custom view, containing id and name. Null for system-generated views.
          - `name` (string) **REQ** [maxLen=101] — Display name of the CRM user who created this custom view. Maximum 101 characters.
          - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the CRM user who created this custom view.
        - `modified_by` (object) **REQ** — Represents the user who last modified this Custom View.
          oneOf:
              - `name` (string) **REQ** [maxLen=101] — Name of the user who modified the custom view.
              - `id` (string/int64) **REQ** — Unique identifier of the user who modified the custom view.
              type: null — Indicates that has never been modified.
        - `module` (object) — Reference object identifying the module to which this custom view belongs, containing the module's unique identifier and API name. This is exposed only for client calls.
          - `api_name` (string) **REQ** [maxLen=50] — API name of the module this custom view belongs to. Maximum 50 characters.
          - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the module this custom view belongs to.
        - `criteria` (object) **REQ** — Represents the filter criteria applied to this Custom View.
          oneOf:
              - `comparator` (string) **REQ** [maxLen=15] — Comparison operator used for filtering (e.g., equal, contains, greater_than, less_than).
              - `field` (object) **REQ** — Field reference specifying which field to filter on.
                - `api_name` (string) **REQ** [maxLen=50] — API name of the field to filter.
                - `id` (string/int64) **REQ** — Unique identifier of the field.
              - `type` (string) **REQ** [maxLen=50] — type of the field being filtered.
              - `value` (object) **REQ** — Filter value to compare against. Can be boolean, string, number, object, array, or null depending on field type and comparator.
              type: null — No filter criteria applied.
        - `default` (boolean) **REQ** — True when this custom view is the default view loaded for the module; only one view per module can be the default.
        - `system_defined` (boolean) **REQ** — True when this custom view was created automatically by the system; false when created by a user.
        - `locked` (boolean) **REQ** [default=False, nullable] — True when the view is locked by an administrator; locked views cannot be modified or deleted by regular users.
        - `favorite` (integer/int32) **REQ** [nullable] — Numeric ranking position of this view in the user's favorites list. Null when the view has not been marked as a favorite.
        - `offline` (boolean) — True when this view is available for offline access in Zoho CRM mobile applications. Only exposed for crmmobile and routeiq services.
        - `access_type` (string) **REQ** [enum=['shared', 'public', 'only_to_me']] — Access scope for the custom view, determining visibility to other users (e.g., private, shared with all, shared with roles).
        - `shared_to` (array of object) [maxItems=100, nullable] **REQ** — Array of sharing target objects (users, roles, groups, or territories) with whom this custom view is shared. Null for public or non-shared views.
          oneOf:
              - `subordinates` (boolean) **REQ** [enum=[True], nullable] — Indicates if subordinates of the specified entity are included in sharing.
              - `type` (string) **REQ** [enum=['territories', 'roles', 'groups', 'users']] — Type of entity the view is shared with (territories, roles, groups, users).
              - `name` (string) **REQ** [maxLen=50] — Name of the entity (user, role, group, or territory).
              - `id` (string/int64) **REQ** — Unique identifier of the entity.
              - `subordinates` (boolean) **REQ** [enum=[False], nullable] — Indicates if subordinates are excluded from sharing.
              - `type` (string) **REQ** [enum=['territories', 'roles', 'groups', 'users']] — Type of entity the view is shared with (territories, roles, groups, users).
              - `name` (string) **REQ** [maxLen=50] — Name of the entity (user, role, group, or territory).
              - `id` (string/int64) **REQ** — Unique identifier of the entity.
        - `fields` (array of object) [maxItems=1000] **REQ** — Ordered list of field objects to display as columns in this custom view, each identified by api_name and id.
          - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the field displayed as this view column.
          - `api_name` (string) **REQ** [maxLen=50] — API name of the field displayed as this view column. Maximum 50 characters.
          - `_pin` (boolean) **REQ** — True when this field column is pinned in the custom view, keeping it visible during horizontal scrolling.
        - `sort_by` (object) **REQ** — Field object specifying the column used to sort records in this view, containing api_name and id. Null when no sort field is configured.
          - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the field used as the sort column in this view.
          - `api_name` (string) **REQ** [maxLen=50] — API name of the field used as the sort column in this view. Maximum 50 characters.
        - `sort_order` (string) **REQ** [enum=['asc', 'desc', None], nullable] — Sort direction applied to this view. Possible values: asc - ascending order; desc - descending order; null - no sort order is configured.
        - `wrap_text` (boolean) — True when text wrapping is enabled for field values displayed in this custom view; false when values are truncated to a single line.
        - `id` (string/int64) **REQ** — Unique numeric identifier (as string) for this custom view.
      - `zia_view` (boolean) — True when Zia AI view is enabled for this module; applicable only to the Deals module
      - `default_mapping_fields` (array of object) [maxItems=25] — Array of default field mapping objects (up to 25) for data import and integration operations. Exposed only for SALESORDERS, INVOICES, QUOTES, QUOTEDITEMS, ORDEREDITEMS, and INVOICEDITEMS modules; each entry identifies a field by api_name and id.
        - `api_name` (string) **REQ** [maxLen=50] — API name of the field in the default mapping configuration. Maximum 50 characters.
        - `id` (string/int64) **REQ** — Unique numeric identifier (as string) of the field in the default mapping configuration.
      - `activity_badge` (string) [enum=['Enabled', 'Not_Supported', 'Disabled']] — Activity badge status for the module. Possible values: Enabled - badge is active; Not_Supported - module does not support activity badges; Disabled - badge is inactive.
      - `status` (string) [enum=['visible', 'scheduled_for_deletion', 'user_hidden', 'system_hidden']] — Represents the visibility status of the module. Possible values: visible - module is active and visible; scheduled_for_deletion - module is queued for removal; user_hidden - hidden by user preference; system_hidden - hidden by system configuration
      - `sequence_number` (integer/int32) — Numeric position of this module in the navigation list; lower values appear first, ranging from 1 to 200
      - `$others_awaiting` (boolean) — True when other users are awaiting action on records in this module. Exposed only for the Approvals module.
      - `territory` (object) — Territory restriction applied to the module; null when territory management is not enabled for the organization
        - `name` (string) [maxLen=50] — Display name of the assigned territory (e.g., 'All Territories', 'North America')
        - `id` (string/int64) — Unique identifier of the territory as a string-encoded numeric ID; '0' indicates no territory restriction is applied
        - `subordinates` (boolean) — True when subordinate (child) territories are included within the scope of this territory restriction
      - `showleadchainsync` (boolean) — True when lead chain synchronization is enabled for this module; only exposed for the Leads module
      - `show_social` (boolean) — True when social tab features are enabled for this module
      - `show_visitor` (boolean) — True when the ZLiveDesk visitor tracking feature is enabled for this module
      - `show_googlesync` (boolean) — True when Google Contact Sync is enabled for this module
      - `showtiktoksync` (boolean) — True when the TikTok LeadChain Sync feature is enabled for this module
      - `show_webform` (boolean) — True when the web forms feature is enabled for this module
      - `showfacebooksync` (boolean) — Indicates if the Facebook LeadChain Sync feature is enabled for this module
      - `show_emailparser` (boolean) — True when the Email Parser feature is enabled for this module
      - `showlinkedinsync` (boolean) — True when the LinkedIn LeadChain Sync feature is enabled for this module
      - `masked_fields_count` (integer/int32) — Count of masked fields in this module. Exposed only when the 'fields' include parameter is specified.

- **204**: 204 No Content - Requested module exists in the system but is not exposed through this endpoint (for example, web tab modules or certain system modules); no response body is returned; use GET /crm/v8/settings/modules to retrieve such modules

- **400**: 400 Bad Request - Request failed due to a syntactic error (malformed or empty api_name) or a semantic error (unsupported module, API version mismatch, or invalid module identifier); error codes include NOT_SUPPORTED, API_NOT_SUPPORTED, INVALID_REQUEST, and INVALID_MODULE [application/json]
    > Contains the 400 error response for a failed single-module retrieval request.
    oneOf:
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code indicating the module is not supported.
        - `details` (object) **REQ** — Details about the unsupported resource.
          - `resource_path_index` (integer/int32) [min=0] — Index of the invalid resource in the URL path (0-based). Typically 2 for the {api_name} parameter.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message explaining that the module is not supported.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Error code indicating the requested API version is not supported.
        - `details` (object) **REQ** — Details about the supported API version.
          - `supported_version` (integer/int32) [min=1] — The minimum or recommended API version that supports this endpoint.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message explaining API version incompatibility.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Error code indicating an invalid request.
        - `details` (object) **REQ** — Additional details about the invalid request (typically empty).
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message explaining the invalid request.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating the module is invalid.
        - `details` (object) **REQ** — Details about the invalid module reference.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Index of the invalid resource in the URL path (0-based). Typically 2 for the {moduleIdentifier} parameter.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message explaining the invalid module.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator.

**Scopes:** ZohoCRM.settings.modules.READ
