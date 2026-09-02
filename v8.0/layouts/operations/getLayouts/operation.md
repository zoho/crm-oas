# GET /settings/layouts
**Operation:** `getLayouts` — Get layouts metadata
> To retrieve the layout configurations for a specified module in your Zoho CRM organization.  **Note:** - The **profiles** array is **null** if the user does not have the Module Customization permission in their profile. - For the Deals module, when the pipeline feature is enabled, multiple layouts exist per pipeline, each with its own set of layouts. - Score and Visit Summary sections are system-generated and read-only. - The API returns all layouts for the module in a single response; pagination is not supported.

**Parameters:**
- `module` (query, string, required) [maxLen=50]: Specify the API name of the required module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `mode` (query, string, optional) [enum=['all', 'business_card', 'quick_create']]: Specify the layout mode to filter the response. Available modes vary by module type. Possible values: `all` - Request all available layout modes. `business_card` - Business card layout view. `quick_create` - Quick create form layout.
- `include` (query, string, optional) [enum=['total_profiles', 'portal_user_types']]: Specify additional data to include in the response beyond the default layout structure. Possible values: `total_profiles` — include the total count of profiles associated with each layout. `portal_user_types` — include portal user type associations for each layout.
- `include_inner_details` (query, string, optional) [maxLen=255, pattern=^[a-z_]+(\.[a-z_]+)?(,[a-z_]+(\.[a-z_]+)?)*$]: Specify additional inner details to include in the response for each field. Possible values: `fields.allowed_permissions_to_update` - Include the set of permissions eligible for update per field. `fields.portal_user_types` - Include portal user type permission entries per field.
- `include_element_types` (query, string, optional) [enum=['field', 'mirror_field']]: Specify the type of field component in the layout, distinguishing standard fields from mirror fields that derive their value from a lookup source. Possible values: `field` — a standard data field in the layout. `mirror_field` — a field that reflects a value from a related module lookup.

**Schemas:**
`ConvertMappingTargetModule`:
  > Represents the target layout configuration for a module involved in a record conversion operation, identifying the layout by its API name and display label.
  - `display_label` (string) **REQ** [maxLen=255] — Represents the label of the target module's layout as it appears in the CRM interface during record conversion.
  - `name` (string) **REQ** [maxLen=255] — Represents the unique API name that programmatically identifies the target layout within the conversion mapping configuration.
  - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the target layout.
`ErrorDetails`:
  > Contains additional context-specific details accompanying an API error response, providing structured diagnostics such as the offending parameter name, expected data type, supported values, or dependency information.
  - `param_name` (string) [maxLen=100] — Identifies the specific request parameter whose value or absence triggered the error, enabling targeted correction of the offending input.
  - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Resource ID related to the error, if applicable.
  - `expected_data_type` (string) [maxLen=50] — Indicates the data type that the API expects for the parameter that failed validation, enabling callers to correct the value format before retrying the request.
  - `supported_values` (array of string) [maxItems=10] — Contains the discrete values accepted for the parameter identified in the error, providing a reference set to correct the offending request.
    items: [maxLen=100]
  - `dependee` (object) — Contains structured information about the controlling parameter whose presence or value is required before the missing dependent parameter becomes valid or applicable.
    - `param_name` (string) [maxLen=100] — Identifies the API parameter name of the dependee — the controlling parameter that must be supplied or satisfied to make the associated dependent parameter applicable in the request.
  - `resource_path_index` (integer/int32) — Indicates the zero-based position within a multi-segment URL path at which the invalid or unrecognised segment was detected, helping to locate the exact portion of the resource path that caused the error.
  - `permissions` (array of string) [maxItems=20] — Contains the set of OAuth permission scopes that must be granted to the authenticating user or application before the requested action can be completed. Returned when the request is denied due to insufficient permissions.
    items: [maxLen=100]
  additionalProperties: any
`ErrorResponse`:
  > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.
  - `code` (string) **REQ** [enum=[11 values]] — Identifies the category of error returned by the API. Possible values: `REQUIRED_PARAM_MISSING` — a mandatory parameter was absent from the request; `DEPENDENT_PARAM_MISSING` — a parameter required by another supplied parameter was not provided; `INVALID_MODULE` — the specified module does not exist or is not accessible; `INVALID_DATA` — one or more field values failed validation; `NOT_SUPPORTED` — the requested operation is not supported for the target resource; `NOT_ALLOWED` — the operation is not permitted in the current context; `AUTHENTICATION_FAILURE` — the supplied credentials could not be verified; `OAUTH_SCOPE_MISMATCH` — the OAuth token does not carry the scope required for the operation; `INVALID_REQUEST_METHOD` — the HTTP method used is not accepted by the endpoint; `INTERNAL_ERROR` — an unexpected server-side failure occurred; `NO_PERMISSION` — the authenticated user lacks the CRM profile permission needed to perform the action.
  - `details` (object `ErrorDetails`) **REQ** — Contains additional context-specific details accompanying an API error response, providing structured diagnostics such as the offending parameter name, expected data type, supported values, or dependency information.
  - `message` (string) **REQ** [maxLen=1000] — Contains a short, descriptive explanation of the error condition, providing context that supplements the structured error code.
  - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request. Possible values: `error` — the request did not complete successfully and the response body contains error details.
`MaskDetailsProfile`:
  > Represents a CRM profile that is permitted to view the unmasked value of a masked field, exempting users of this profile from the field's masking rules.
  - `name` (string) **REQ** [maxLen=60] — Represents the name of the CRM profile that is permitted to view the unmasked field value, identifying which user group is exempt from the field's masking rules.
  - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the profile.
`UserReference`:
  > User who created the layout
  - `name` (string) **REQ** [maxLen=100, minLen=1] — Represents the display name of the CRM user, shown in audit fields and reference contexts such as created_by and modified_by.
  - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.

**Responses:**

- **200**: Successful response returned when the API retrieves layout configurations for the specified module, containing the full array of layout objects. [application/json]
    oneOf:
      - `LayoutResponseSchema` — Represents the response schema for layout retrieval operations, containing an array of layout objects each with complete configuration details including sections, profiles, and portal user type associations.
        - `layouts` (array of object) [maxItems=15] **REQ** — Contains the array of layout objects returned for the specified module, each representing a complete layout configuration including sections, fields, profiles, and portal user type associations.
          - `has_more_profiles` (boolean) **REQ** — Indicates whether additional profile associations exist for this layout beyond those included in the current response. Possible values: `true` — more profile associations are available; `false` — all profile associations are represented.
          - `created_time` (object) **REQ**
            oneOf:
                type: string/date-time — Represents the ISO 8601 datetime with timezone offset recording when this layout was first created in the CRM.
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `convert_mapping` (object)
            oneOf:
              - `ConvertMappingModule` — Represents the convert mapping configuration that defines how record field values are transferred across modules during a record conversion operation.
                oneOf:
                    title: Leads Convert Mapping
                    - `Contacts` (object `ConvertMappingTargetModule`) **REQ** — Represents the target layout configuration for a module involved in a record conversion operation, identifying the layout by its API name and display label.
                    - `Deals` (object `ConvertMappingTargetModuleWithFields`) **REQ** — Represents the target layout configuration for a module involved in a record conversion, including field-level mapping details that define how source field values are transferred.
                      schema: `ConvertMappingTargetModuleWithFields`
                      - `display_label` (string) **REQ** [maxLen=255] — Represents the label of the target module's layout as it appears in the CRM interface during record conversion. This variant is accompanied by field-level mapping details.
                      - `name` (string) **REQ** [maxLen=255] — Represents the unique API name that programmatically identifies the target layout within the conversion mapping configuration. This variant is accompanied by field-level mapping details.
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the target layout.
                      - `fields` (array of object) [maxItems=100] **REQ** — Contains the collection of field configurations belonging to the target module's layout that participate in the record conversion process, each describing how a specific field is handled during the transfer of data.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the field in the target module.
                        - `field_label` (string) **REQ** [maxLen=255] — Represents the name of the field as it appears in the CRM interface within the target module's layout during record conversion.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the field.
                        - `required` (boolean) **REQ** — Indicates whether the field must be populated for the record conversion to proceed successfully. Possible values: `true` — the field is mandatory and a value must be provided before conversion can complete; `false` — the field is optional and may be left unpopulated during conversion.
                    - `Accounts` (object `ConvertMappingTargetModule`) **REQ** — Represents the target layout configuration for a module involved in a record conversion operation, identifying the layout by its API name and display label.
                    title: Quotes Convert Mapping
                    - `SalesOrders` (object `ConvertMappingTargetModule`) **REQ** — Represents the target layout configuration for a module involved in a record conversion operation, identifying the layout by its API name and display label.
                    - `Invoices` (object `ConvertMappingTargetModule`) **REQ** — Represents the target layout configuration for a module involved in a record conversion operation, identifying the layout by its API name and display label.
                    title: Sales Orders Convert Mapping
                    - `Invoices` (object `ConvertMappingTargetModule`) **REQ** — Represents the target layout configuration for a module involved in a record conversion operation, identifying the layout by its API name and display label.
                    title: No Convert Mapping
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `visible` (boolean) **REQ** — Indicates whether this layout is currently visible and accessible to users in the CRM interface. Possible values: `true` — the layout is visible and selectable; `false` — the layout is hidden.
          - `created_for` (object) **REQ**
            oneOf:
                type: string [maxLen=100] — Represents the integration or system context that prompted the creation of this layout, identifying the source platform or feature responsible for provisioning it.
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `portal_user_types` (array of object) [maxItems=50] — Contains the list of portal user type associations for this layout, each specifying which portal user category the layout is associated with and the default view configuration for that user type.
            - `default` (boolean) **REQ** — Indicates whether this layout is the default for the associated portal user type. Possible values: `true` — this is the default layout for this portal user type; `false` — it is not the default.
            - `name` (string) **REQ** [maxLen=255] — Represents the name of the portal user type associated with this layout entry.
            - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the portal user type
            - `_default_view` (object) **REQ** — Represents the default view assigned to this portal user type for the layout, defining which view is presented to portal users of this type by default.
              - `name` (string) **REQ** [maxLen=255] — Represents the API name of the default view assigned to this portal user type.
              - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the default view
              - `type` (string) **REQ** [enum=['layout', 'wizard']] — Indicates the category of the default view assigned to this portal user type, such as a layout view or a wizard-based view.
          - `profiles` (object) **REQ**
            oneOf:
                type: array of object `ProfileReference` [minItems=1, maxItems=50]
                  schema: `ProfileReference`
                  - `_default_assignment_view` (object) **REQ** — Represents the default view configuration used for record assignment for users belonging to this profile and layout combination.
                    - `name` (string) **REQ** [maxLen=100, minLen=1] — Represents the name of the view used as the default for record assignment for this profile.
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                    - `type` (string) **REQ** [enum=['canvas', 'layout']] — Indicates the type of view used for record assignment. Possible values: `canvas` — a custom canvas view; `layout` — a standard field layout.
                  - `default` (boolean) **REQ** — Indicates whether this profile is the default profile assignment for the layout. Possible values: `true` — this is the default profile; `false` — this is not the default profile.
                  - `name` (string) **REQ** [maxLen=60, minLen=1] — Represents the display name of the CRM profile associated with this layout assignment.
                  - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                  - `_default_view` (object) **REQ** — Represents the default view assigned to this profile for the layout, used when users of this profile open a record in the standard detail context.
                    - `name` (string) **REQ** [maxLen=100, minLen=1] — Represents the name of the default view assigned to this profile for the layout.
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                    - `type` (string) **REQ** [enum=['layout', 'wizard']] — Indicates the type of the default view assigned to this profile. Possible values: `layout` — a standard field layout; `wizard` — a guided multi-step wizard.
                  - `type` (string) [enum=['normal_profile', 'lite_profile']] — Represents the classification type of the profile, distinguishing between available profile tiers. Possible values: `normal_profile` — a full-access standard CRM profile. `lite_profile` — a restricted-access lite profile.
                  additionalProperties: any
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `source` (string) **REQ** [enum=['crm', 'platform_plugin', 'marketplace_plugin', 'campaign_integration']] — Represents the origin channel of this layout. Possible values: `crm` — the layout is built into the standard module definition. `platform_plugin` — the layout comes from a Zoho platform plugin. `marketplace_plugin` — the layout comes from a Marketplace extension. `campaign_integration` — the layout comes from a Campaigns integration.
          - `created_by` (object)
            oneOf:
              - `UserReference` — User who created the layout
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `sections` (array of object) [minItems=0, maxItems=100] **REQ** — Contains the ordered list of sections within this layout, each grouping a set of fields and defining display properties such as column count and tab traversal order.
            - `isSubformSection` (boolean) **REQ** — Indicates whether this section renders as an embedded subform that displays related module records inline within the parent record's layout. Possible values: `true` — the section is a subform; `false` — the section is a standard field group.
            - `parent_section` (object) — Represents a reference to the parent section when this section is nested as a subform or dependent section within the layout hierarchy.
              oneOf:
                  - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the parent section.
                  - `name` (string) **REQ** [maxLen=100] — Represents the name of the parent section under which this nested section is organized within the layout.
                - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
            - `type` (string) [enum=['used', 'unused']] — Represents the usage status type of this section within the layout. Possible values: `used` — the section contains fields assigned to it. `unused` — the section exists in the layout but contains no assigned fields.
            - `display_label` (string) **REQ** [maxLen=100, minLen=1] — Represents the name of the section as displayed in the CRM interface, used as the section heading on record create and detail pages.
            - `mode` (string) **REQ** [enum=[8 values]] — Represents the layout mode for which this section applies, controlling in which view contexts the section and its fields render. Possible values: `all` — applies across all layout modes. `business_card` — applies to the business card view. `quick_create` — applies to the quick-create form. `default_create` — applies to the default record creation form. `create_edit` — applies to both create and edit forms. `view` — applies to the record detail view. `quick_view` — applies to the quick view panel. `subform_default_create` — applies to the default create form within a subform context.
            - `sequence_number` (number/int32) **REQ** [min=1] — Represents the ordinal position of this section within the layout, controlling the order in which sections are rendered on record forms.
            - `actions_allowed` (object `ActionsAllowed`) **REQ** — Permissions for section operations. System sections (Score, Visit Summary) will have restricted permissions.
              schema: `ActionsAllowed`
              - `add_field` (boolean) **REQ** — Indicates whether new fields may be introduced into the layout section. Possible values: `true` — adding fields to the section is permitted; `false` — adding fields to the section is not permitted.
              - `rename` (boolean) **REQ** — Indicates whether the display name of the layout section may be changed. Possible values: `true` — renaming the section is permitted; `false` — renaming the section is not permitted.
              - `change_tab_traversal` (boolean) **REQ** — Indicates whether the keyboard tab traversal order of fields within the layout section may be modified. Possible values: `true` — changing the tab traversal order is permitted; `false` — changing the tab traversal order is not permitted.
              - `reorder` (boolean) **REQ** — Indicates whether the relative ordering of sections or fields within the layout may be changed. Possible values: `true` — reordering is permitted; `false` — reordering is not permitted.
              - `delete` (boolean) **REQ** — Indicates whether the layout section may be permanently removed from the layout. Possible values: `true` — deleting the section is permitted; `false` — deleting the section is not permitted.
              - `remove_field` (boolean) **REQ** — Indicates whether existing fields may be detached from the layout section. Possible values: `true` — removing fields from the section is permitted; `false` — removing fields from the section is not permitted.
              - `change_column_count` (boolean) **REQ** — Indicates whether the number of columns displayed within the layout section may be modified. Possible values: `true` — adjusting the column count for the section is permitted; `false` — adjusting the column count for the section is not permitted.
            - `tab_traversal` (string) **REQ** [enum=['left_to_right', 'top_to_bottom']] — Indicates the direction of keyboard tab navigation within this section, determining the order in which focus moves between fields when users press Tab. Possible values: `left_to_right` — focus moves horizontally across columns first. `top_to_bottom` — focus moves vertically down each column first.
            - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API identifier for the section
            - `column_count` (number/int32) **REQ** [enum=[1, 2]] — Indicates the number of columns in which fields are arranged within this section, controlling the side-by-side or single-column display of fields on record forms.
            - `is_parent_section` (boolean) — Indicates whether this section acts as the parent container for a dependent subform section, establishing a hierarchical section relationship within the layout. Possible values: `true` — this is a parent section; `false` — this section is not a parent container.
            - `name` (string) **REQ** [maxLen=50, minLen=1] — Represents the internal name of the section used to reference it in layout configurations and API operations.
            - `generated_type` (string) **REQ** [enum=['default', 'custom']] — Indicates whether this section originates from automatic system generation or from an administrator's manual configuration. Possible values: `default` — automatically generated by the CRM platform. `custom` — defined manually by an administrator.
            - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
            - `fields` (array of object `FieldSchema`) [maxItems=500] **REQ** — Contains the ordered list of fields assigned to this section. Fields are presented in ascending sequence_number order.
              schema: `FieldSchema`
              - `associated_module` (object) — Contains the details of the CRM module linked to this field when the field represents a subform, identifying the related module and the layout governing how its records are embedded and displayed within the parent module's layout.
                oneOf:
                    - `module` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z0-9_]+$] — API name of the associated module
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the associated module
                    - `layout` (object) — Represents the name of the layout applied to the associated module's records when displayed within the subform field, determining which set of fields and sections are rendered in the embedded view.
                      - `name` (string) **REQ** [maxLen=100, minLen=1] — Represents the name of the layout applied to the associated module's records when displayed within the subform field, determining which set of fields and sections are rendered in the embedded view.
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the layout
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `webhook` (boolean) — Indicates whether webhook notifications are triggered when this field's value changes on a record. Possible values: `true` — changes to this field trigger configured webhook endpoints; `false` — field changes do not initiate webhook notifications.
              - `operation_type` (object) — Represents the set of operations permitted on this field, specifying independently whether values can be supplied or modified through API-based create/update calls and through the CRM web interface create/update forms.
                - `web_update` (boolean) **REQ** — Indicates whether this field accepts a new value when a record is saved through the CRM web interface during an update. Possible values: `true` — the field is editable in the web edit form; `false` — the field is read-only or hidden in the web update form.
                - `api_create` (boolean) **REQ** — Indicates whether this field accepts a value when a record is saved through the API during creation. Possible values: `true` — the field value can be set via API during record creation; `false` — the field value cannot be set via API at record creation time.
                - `web_create` (boolean) **REQ** — Indicates whether this field appears and accepts a value when a record is saved through the CRM web interface during creation. Possible values: `true` — the field is editable in the web create form; `false` — the field does not appear or is locked in the web create form.
                - `api_update` (boolean) **REQ** — Indicates whether this field accepts a new value when a record is saved through the API during an update. Possible values: `true` — the field can be modified via API during a record update; `false` — the field is read-only for API-based update operations.
              - `colour_code_enabled_by_system` (boolean) — Indicates whether color-code functionality has been activated for this field by the system platform rather than by a user or administrator. Possible values: `true` — the system has enabled color coding for this field; `false` — color coding on this field is not system-activated.
              - `field_label` (string) [maxLen=100, minLen=1] — Represents the label assigned to the field, displayed in forms, detail views, and list columns within the module layout.
              - `tooltip` (object) — Represents the tooltip configuration attached to this field, defining contextual help text displayed to users when they hover over or focus on the field in a record form.
                oneOf:
                    - `name` (string) **REQ** [maxLen=25] — Indicates the delivery mechanism for the tooltip, such as whether it is rendered as a static label or as a modal help popup.
                    - `value` (string) **REQ** [maxLen=255] — Contains the help text displayed in the tooltip when users interact with this field, providing contextual guidance on the field's purpose or expected input.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `display_format_properties` (object) — Contains supplementary rendering configuration for field types that require additional display directives beyond a simple format string, such as phone number dial-code positioning or the orientation and layout style of radio button groups.
                oneOf:
                    - `split` (number/int32) — Indicates the formatting pattern applied to split a phone number into its dial-code prefix and local number segments when rendering the field in the UI.
                    - `radio_display_type` (string) [maxLen=25] — Specifies the layout orientation used to render radio button options in the UI, such as arranging choices horizontally in a row or vertically in a stacked column.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `type` (string) [maxLen=25, enum=['all', 'unused', 'used']] — Indicates the field's layout usage status, determining whether the field appears in layout sections. Possible values: `used` — the field is placed in at least one layout section. `unused` — the field exists in the module but has no assignment to any section. `all` — the field appears regardless of layout placement status.
              - `field_read_only` (boolean) — Indicates whether the field is locked against user edits at the field level, independent of profile-based permissions. Possible values: `true` — the field value cannot be modified by users; `false` — the field is editable subject to applicable profile permissions.
              - `customizable_properties` (object) — Contains the set of field attributes that administrators are permitted to modify through the CRM layout editor, such as label, required status, or visibility, reflecting which aspects of the field definition are not locked by the system.
                oneOf:
                    type: array of string [maxItems=100, uniqueItems]
                      type: string [maxLen=50] — Represents the API name of a single field attribute that can be modified by an administrator, identifying a specific configurable aspect of the field such as its label, tooltip, or mandatory setting.
                      items: [maxLen=50]
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `required` (boolean) — Indicates whether this field must contain a value before a record can be saved. Possible values: `true` — the field is mandatory and a value must be supplied; `false` — the field is optional.
              - `subform_properties` (object) — Contains the display configuration settings for this field when it appears within a subform section, such as custom column width and column pinning behavior.
                oneOf:
                    - `custom_width` (object) **REQ** — Indicates the custom column width in pixels assigned to this field when it is displayed as a column in a subform, overriding the default column sizing.
                      oneOf:
                          type: integer/int32 [min=50, max=1000] — Represents the active custom column width in pixels for this field when displayed in a subform section.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `pinned_column` (boolean) **REQ** — Indicates whether this field's column is frozen in place when users scroll horizontally through a subform, keeping the field visible regardless of scroll position. Possible values: `true` — the column is pinned; `false` — the column scrolls with the subform.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `display_label` (string) [maxLen=100, minLen=1] — Represents the name of the field displayed in the module layout, used as the visible title in forms, list views, and detail pages.
              - `allowed_permissions_to_update` (object) — Represents the set of permission levels that can be actively assigned to this field across profiles, indicating which visibility and access states are eligible for modification. Returned only when the query parameter `include_inner_details=fields.allowed_permissions_to_update` is specified in the request.
                - `read_write` (boolean) **REQ** — Indicates whether the read-write permission level is eligible to be assigned to this field. Possible values: `true` — the field can be configured for full read and write access for specific profiles, permitting both viewing and editing; `false` — the read-write permission cannot be applied to this field.
                - `hidden` (boolean) **REQ** — Indicates whether the hidden permission level is eligible to be assigned to this field. Possible values: `true` — the field's visibility can be set to hidden for specific profiles, concealing it entirely from their layout view; `false` — the hidden permission cannot be applied to this field.
                - `read_only` (boolean) **REQ** — Indicates whether the read-only permission level is eligible to be assigned to this field. Possible values: `true` — the field can be configured as read-only for specific profiles, allowing users to view but not edit its value; `false` — the read-only permission cannot be applied to this field.
              - `read_only` (boolean) — Indicates whether this field is locked against user edits through the CRM interface and API, preventing any modification of its value after it has been set. Possible values: `true` — the field cannot be modified; `false` — the field is editable subject to applicable permissions.
              - `association_details` (object) — Contains the relationship metadata for fields connected to other records through lookup associations, describing the linked module, the nature of the relationship, and any constraints governing how related records appear or display.
                oneOf:
                    - `related_field` (object) **REQ** — Represents the corresponding field on the related module that is linked through the association, containing identifying metadata such as the field's API name and display label.
                      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the related field
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the related field
                    - `lookup_field` (object) **REQ** — Represents the lookup field on the source module that establishes the association, containing identifying metadata such as the field's API name and display label.
                      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the lookup field
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the lookup field
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `businesscard_supported` (boolean) — Indicates whether the field is eligible to appear on the business card view, which surfaces key record details in compact preview panels across Zoho CRM. Possible values: `true` — the field can be included in the business card layout; `false` — the field is excluded from business card display.
              - `sharing_properties` (object) — Contains the sharing configuration for this field, defining how its value participates in record-level sharing rules and whether specific sharing preferences are active.
                - `scheduler_status` (object) **REQ**
                  oneOf:
                      type: string [maxLen=50] — Represents the active status of the sharing scheduler for this field, indicating the current state of sharing rule propagation.
                    - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                - `share_permission` (string) **REQ** [maxLen=50] — Represents the sharing access level assigned to this field, controlling whether users who receive shared record access can read, edit, or are restricted from this field's value.
                - `share_preference_enabled` (boolean) **REQ** — Indicates whether the sharing preference configuration is active for this field. Possible values: `true` — sharing preference settings are applied to this field; `false` — sharing preference is not enabled.
                - `share_with_superiors` (boolean) — Indicates whether this field's value is shared with users in superior roles in the CRM role hierarchy when record sharing propagates upward. Possible values: `true` — the field is shared with superior role users; `false` — the field is not shared with superiors.
              - `multi_module_lookup` (object) — Represents the multi-module lookup configuration for fields that can reference records from more than one CRM module within a single lookup relationship, including the participating modules and dynamic addition settings.
                oneOf:
                    - `display_label` (string) [maxLen=50] — Represents the identifying label of the multi-module lookup field in the CRM interface, identifying the lookup relationship across its participating modules.
                    - `api_name` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the multi module lookup field
                    - `modules` (array of object) [maxItems=100] — Contains the collection of CRM modules that participate in this multi-module lookup relationship, each representing a valid source from which the user can select a referenced record.
                      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the module
                      - `module_name` (string) **REQ** [maxLen=50] — Indicates the internal API name of the module participating in the multi-module lookup, used to identify the module programmatically across CRM operations.
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the module
                    - `dynamic_module_addition_allowed` (boolean) — Indicates whether additional CRM modules can be incorporated into this multi-module lookup relationship at runtime without requiring a layout reconfiguration. Possible values: `true` — new modules may be added dynamically; `false` — the participating modules are fixed at configuration time.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the field
              - `created_time` (object) — Represents the date and time at which the field definition was first created in the CRM, recorded for audit and chronological tracking purposes.
                oneOf:
                    type: string/date-time — Represents the ISO 8601 datetime with timezone offset recording when this field definition was first created in the CRM.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `filterable` (boolean) — Indicates whether the field can be used as a filter criterion in record search, list view filtering, and report conditions. Possible values: `true` — the field is available as a filter option; `false` — the field cannot be used for filtering.
              - `visible` (boolean) — Indicates whether this field is currently displayed in the module layout. Possible values: `true` — the field is shown in the layout and visible to users with appropriate permissions; `false` — the field is hidden from the layout.
              - `mask_details` (object) — Represents the field masking configuration that controls how the field's stored value is partially or fully hidden from users who do not have permission to view sensitive data, including rules for how many characters are revealed and which profiles can bypass masking.
                oneOf:
                    title: Partial Mask
                    - `show_first` (integer/int32) **REQ** [min=0, max=50] — Indicates the number of characters revealed at the start of the field value when partial masking is applied, allowing a prefix of the data to remain visible while the remainder is hidden.
                    - `complete_mask` (boolean) **REQ** — Indicates whether the entire field value is hidden from unauthorized users rather than partially revealed. Possible values: `true` — the value is completely obscured; `false` — partial character reveal rules defined by show_first and show_last apply.
                    - `show_last` (integer/int32) **REQ** [min=0, max=50] — Indicates the number of characters revealed at the end of the field value when partial masking is applied, allowing a suffix of the data to remain visible while the preceding portion is hidden.
                    - `profiles` (array of object `MaskDetailsProfile`) [maxItems=50] **REQ** — Contains the list of CRM profiles whose members are permitted to view the unmasked field value, exempting those users from the masking rules applied to all other profiles.
                    title: Complete Mask
                    - `complete_mask` (boolean) **REQ** — Indicates whether the entire field value is hidden in this alternate masking schema variant. Possible values: `true` — the value is completely obscured; `false` — partial reveal rules apply.
                    - `profiles` (array of object `MaskDetailsProfile`) [maxItems=50] **REQ** — Contains the list of CRM profiles whose members can view the unmasked field value in this alternate masking schema variant, exempting those users from the masking rules applied to all other profiles.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `refer_from_field` (object) — Represents the source field from which this mirror or derived field obtains its value, establishing a read-through relationship where the field reflects data from another field in a related module.
                oneOf:
                    - `api_name` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the reference field
                    - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the reference field
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `portal_user_types` (array of object) [maxItems=50] — Contains the list of portal user type permission configurations for this field, specifying which portal user type categories can view or edit the field's value when accessing records through a customer or partner portal.
                - `permission_type` (string) **REQ** [enum=['read_write', 'read_only', 'hidden']] — Represents the access level granted to portal users of this type for the field. Possible values: `read_write` — full read and write access; portal users can view and edit the field. `read_only` — view access only; portal users can see but cannot modify the field value. `hidden` — the field is not visible to portal users of this type.
                - `name` (string) **REQ** [maxLen=255] — Represents the name of the portal user type, identifying the category of external users whose field permissions are described in this entry.
                - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the portal user type
              - `profiles` (array of object) [maxItems=100, uniqueItems] — Contains the list of profile-level permission entries for this field, each describing the access level a specific CRM profile has to view or edit the field's value.
                - `permission_type` (string) **REQ** [maxLen=25, enum=['read_write', 'read_only', 'hidden']] — Represents the level of access granted to users of this profile for the field. Possible values: `read_write` — full read and write access; users can view and edit the field. `read_only` — view access only; users can see but cannot modify the field value. `hidden` — the field is not visible to users of this profile.
                - `name` (string) **REQ** [maxLen=60] — Represents the name of the CRM profile for which this field permission entry applies.
                - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the profile
              - `view_type` (object) — Represents the view-mode availability settings for this field, specifying in which CRM interaction contexts — such as record creation, editing, viewing, or quick-create — the field is shown or editable.
                - `view` (boolean) **REQ** — Indicates whether this field is visible when a record is viewed in detail mode. Possible values: `true` — the field is displayed on the record detail page; `false` — the field is hidden from the detail view.
                - `edit` (boolean) **REQ** — Indicates whether this field is presented and editable in the record edit form. Possible values: `true` — the field is shown in edit mode; `false` — the field is hidden or read-only during editing.
                - `quick_create` (boolean) **REQ** — Indicates whether this field is included in the abbreviated quick-create form. Possible values: `true` — the field appears in the quick-create panel; `false` — the field is excluded from quick-create.
                - `create` (boolean) **REQ** — Indicates whether this field is presented in the record creation form. Possible values: `true` — the field is shown when creating a new record; `false` — the field does not appear in the create form.
              - `subform` (object) — Represents the subform configuration for fields that embed a related module's records inline within the parent module's layout, including the API name of the associated subform module and its subform tab identifier.
                oneOf:
                    - `module` (string) **REQ** [maxLen=50] — Represents the API name of the module whose records are embedded as a subform in the parent module's layout.
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the subform tab.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `separator` (boolean) — Indicates whether this field functions as a visual separator element in the layout rather than a data-entry field. Possible values: `true` — the element is a layout separator that creates a visual break between sections or field groups; `false` — the element is a standard data field.
              - `searchable` (boolean) — Indicates whether this field's value can be used as a search term in the CRM's global and module-level search functionality. Possible values: `true` — the field is indexed for search and returns results when matched; `false` — the field is excluded from search indexing.
              - `history_tracking_enabled` (boolean) — Indicates whether change history recording is active for this field, controlling whether updates to the field's value are logged in the audit trail. Possible values: `true` — field value changes are captured and retained in history tracking; `false` — changes to this field are not recorded in the audit trail.
              - `show_type` (number/int32) — Represents the internal numeric code that controls the display behavior or rendering mode of the field in the CRM UI, supplementing the data_type classification with additional display context.
              - `external` (object) — Contains the integration configuration for fields that receive or expose values through external systems, such as third-party connectors or Zoho marketplace extensions.
                oneOf:
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `api_name` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API identifier for the field
              - `parent_field` (object) — Represents the parent field reference for nested or composite fields such as address components, identifying the field under which this field is grouped in the module layout.
                oneOf:
                    - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the parent field
                    - `name` (string) **REQ** [maxLen=50] — Represents the API name of the parent field under which this nested field is organized within the module layout.
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the parent field
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `unique` (object) — Represents the uniqueness constraint configuration for this field, controlling whether duplicate values are permitted across records in the module and whether the check is case-sensitive.
                - `case_sensitive` (boolean) — Indicates whether the field's uniqueness constraint treats values differing only in letter case as distinct. Possible values: `true` — case-sensitive comparison is applied and values with different casing are treated as unique; `false` — the uniqueness check is case-insensitive.
              - `enable_colour_code` (boolean) — Indicates whether color coding is currently active for this field, allowing field values to be visually differentiated by color in list views and kanban boards. Possible values: `true` — color coding is enabled for the field; `false` — color coding is not active.
              - `child_fields` (object) — Contains the ordered collection of sub-fields that compose a composite field, such as the individual address components (street, city, state, country, zip) grouped under a single parent field.
                oneOf:
                    type: array of object [maxItems=100]
                      - `sequence_number` (number/int32) **REQ** [min=1] — Indicates the ordinal position of the child field within the composite field, determining the rendering order of sub-fields in the layout UI.
                      - `field` (object) **REQ** — Contains the identifying attributes of the child field, such as its API name, used to reference the corresponding FieldSchema within the module layout.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the child field
                        - `name` (string) **REQ** [maxLen=100] — Represents the API name of the child field, used to uniquely identify it within the parent composite field and reference it in layout and data operations.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the child field
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `pick_list_values` (object) — Contains the list of selectable options defined for a picklist field, each representing a distinct choice that users can select when populating the field on a record.
                oneOf:
                    type: array of object [maxItems=4000]
                      - `display_value` (string) **REQ** [maxLen=120] — Represents the label displayed to users for this picklist option in forms, detail views, and filter dropdowns, which may be a localized version of the stored actual value.
                      - `sequence_number` (number/int32) **REQ** [min=1] — Indicates the ordinal position of this picklist option within the field's list of available choices, determining the display order in dropdown menus and filter panels.
                      - `record_category_value` (object) — Reference to an existing record category value mapped to this picklist option. **At least one identifier must be provided**: `id`, `rid`, or `api_name`. Multiple identifiers can be provided for validation purposes. Server-side validation enforces this requirement.
                        - `id` (string/int64) — Unique identifier of the record category value
                        - `api_name` (string) [maxLen=255] — API name of the record category value
                      - `deal_category` (string) [maxLen=100] — Represents the deal pipeline category classification associated with this picklist option, used to group and report on deals by their stage category.
                      - `reference_value` (string) [maxLen=120] — Represents the system-internal reference identifier for this picklist option, used in cross-field mapping and dependent picklist resolution where the display value alone is insufficient to uniquely identify the option.
                      - `maps` (array of object) [maxItems=4000] **REQ** — Contains the dependent picklist mapping configuration for this option, defining which values become available in dependent fields when this option is selected in the parent picklist.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the dependent picklist field.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the dependent picklist field.
                        - `pick_list_values` (array of object) [maxItems=500] **REQ** — Contains the subset of picklist values available in the dependent field when this parent option is selected, restricting user choices to contextually appropriate options.
                          - `display_value` (string) **REQ** [maxLen=120] — Represents the label displayed in the CRM interface for this dependent picklist option, which may differ from its stored actual value.
                          - `colour_code` (object) **REQ** — Represents the hexadecimal color code associated with this dependent picklist option, used to color-code records by their selected value when color coding is enabled for the field.
                            oneOf:
                                type: string [maxLen=7, minLen=7, pattern=^#[0-9A-Fa-f]{6}$] — Represents the hexadecimal color code in #RRGGBB format for this dependent picklist option when color coding is active.
                              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                          - `actual_value` (string) **REQ** [maxLen=120] — Represents the internal value stored when this dependent picklist option is selected, used as the system identifier for the choice in data storage and API responses.
                          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the picklist value.
                      - `colour_code` (object) — Represents the color associated with this picklist option when color-coded list views are enabled for the field, used to visually distinguish records by their selected value.
                        oneOf:
                            type: string [maxLen=7, minLen=7, pattern=^#[0-9A-Fa-f]{6}$] — Represents the hexadecimal color code in #RRGGBB format associated with this picklist option when color coding is active.
                          - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                      - `probability` (number/int32) [min=0, max=100] — Represents the percentage probability of deal closure associated with this picklist option, used in forecast calculations and reporting for deal stage fields.
                      - `forecast_category` (object) — Represents the sales forecast classification associated with this picklist option, grouping deals in a given stage into a defined forecast bucket such as Pipeline, Best Case, or Closed Won.
                        - `name` (string) [maxLen=100] — Represents the name of the forecast category assigned to this picklist option, identifying the forecast bucket to which deals at this stage are attributed.
                        - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the forecast category
                      - `actual_value` (string) **REQ** [maxLen=120] — Represents the internal value stored in the database when this picklist option is selected, which may differ from the label displayed to the user.
                      - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the pick list value
                      - `forecast_type` (string) [maxLen=50] — Indicates the type of forecast behavior associated with this picklist option, classifying how deals at this stage are treated in forecast calculations.
                      - `type` (string) [maxLen=50] — Represents the classification type of this picklist option, distinguishing system-defined choices from user-created ones or categorizing options by their behavioral role within the field.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `system_mandatory` (boolean) — Indicates whether this field is enforced as mandatory by the CRM system itself, as opposed to being made required through an administrator's layout configuration. Possible values: `true` — the field is system-level mandatory and cannot be made optional; `false` — the mandatory status is controlled by layout configuration.
              - `private` (object)
                oneOf:
                    - `restricted` (boolean) **REQ** — Indicates whether this field is subject to privacy restrictions that limit its visibility to the record owner and administrators. Possible values: `true` — access to the field value is restricted based on record ownership; `false` — the field is accessible to all users with the appropriate module permissions.
                    - `type` (string) **REQ** [maxLen=25, enum=['High', 'Low']] — Represents the privacy restriction level applied to this field. Possible values: `High` — high-level privacy restriction with strict access control. `Low` — low-level privacy restriction with relaxed access control.
                    - `export` (boolean) **REQ** — Indicates whether this field's value is included when records are exported from the CRM, subject to the field's privacy settings. Possible values: `true` — the field is included in exports; `false` — the field is excluded from exported data.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `virtual_field` (boolean) — Indicates whether this field is a computed or transient field that exists only at the API layer and does not map to a persistent database column. Possible values: `true` — the field is virtual and its value is derived at runtime; `false` — the field is backed by a database column.
              - `json_type` (string) [maxLen=25, enum=['jsonarray', 'integer', 'string', 'jsonobject', 'boolean', 'double', 'long']] — Represents the primitive JSON data type used to serialize this field's value in API request and response payloads. Possible values: `string` — a text value. `integer` — a whole number. `boolean` — a true or false value. `double` — a decimal number. `long` — a large integer. `jsonobject` — a structured object. `jsonarray` — an array of values.
              - `crypt` (object) — Contains the encryption settings applied to this field, specifying how sensitive data stored in the field is protected at rest within the CRM platform.
                oneOf:
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `range` (object) — Represents the numeric range constraint applied to this field, specifying the minimum and maximum values that the field accepts when a record is saved.
                oneOf:
                    - `from` (object) **REQ**
                      oneOf:
                          type: number/double — Represents the lower bound of the numeric range constraint, defining the minimum value the field accepts.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `to` (object) **REQ**
                      oneOf:
                          type: number/double — Represents the upper bound of the numeric range constraint, defining the maximum value the field accepts.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `created_source` (string) [maxLen=60, enum=['', 'default', 'extension', 'integration']] — Indicates the origin channel through which this field originates in the module. Possible values: `default` — the field is part of the standard CRM module definition; `extension` — the field was added through a CRM extension or plug-in package; `integration` — the field was provisioned via a third-party integration.
              - `display_type` (number/int32) — Indicates the internal numeric code that controls how the field is rendered in the CRM UI, mapping to predefined display modes such as text box, drop-down, or date picker.
              - `ui_type` (number/int32) — Represents the internal numeric code that identifies the UI component type used to render and interact with this field in the CRM interface, such as a text input, date picker, or reference selector.
              - `validation_rule` (object) — Represents the Validation Rule configuration applied to this field, referencing the rule that governs acceptable input formats, value ranges, or logical conditions evaluated when a record is saved.
                oneOf:
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the validation rule applied to this field.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `modified_time` (object) — Represents the date and time at which the field's definition or configuration was most recently changed in the CRM, recorded for audit and change-tracking purposes.
                oneOf:
                    type: string/date-time — Represents the ISO 8601 datetime with timezone offset recording when this field's configuration was most recently changed.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `file_upolad_optionlist` (object) — Contains the list of permitted file source options for file-upload fields, defining where users may select files from when populating the field.
                oneOf:
                    type: array of object [maxItems=20]
                      - `display_value` (string) **REQ** [maxLen=100] — Represents the label shown in the CRM interface for the file upload source option, communicating the upload channel name to the end user.
                      - `actual_value` (string) **REQ** [maxLen=100] — Represents the system-level identifier for the file upload source, used internally to route the upload request to the correct provider.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `public` (boolean) — Indicates whether this field's value is accessible to external users or public-facing integrations. Possible values: `true` — the field is marked as public and may be exposed through portals or external APIs; `false` — the field is restricted to internal CRM users.
              - `section_id` (number/int32) — Indicates the numeric identifier of the section within the module layout that contains this field, used to group fields and determine their organizational placement on record forms.
              - `static_values` (object) — Contains the predefined option list for fields with a fixed set of choices, such as static picklists and radio button fields, where the available values are defined at layout configuration time.
                oneOf:
                    type: array of object [maxItems=500]
                      - `sequence_number` (integer/int32) **REQ** [min=1] — Indicates the display order of this static option within the field's predefined choice list, determining the position in which the option appears to users.
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the static value option.
                      - `value` (string) **REQ** [maxLen=255] — Represents the stored value for this static option, used as the system identifier and the data written to the record when the option is selected.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `currency` (object) — Contains the currency-specific display and calculation settings for the field, including the number of decimal places to retain and the rounding strategy applied when storing or presenting monetary values.
                oneOf:
                    - `rounding_option` (string) [maxLen=25, enum=['round_up', 'round_down', 'round_off', 'normal']] — Specifies the rounding rule applied to currency values when the raw amount exceeds the configured precision. Possible values: `round_up` — always rounds the value up. `round_down` — always rounds the value down. `round_off` — rounds to the nearest value. `normal` — no rounding applied.
                    - `precision` (number/int32) — Indicates the number of decimal places retained when storing and displaying currency values for this field, controlling the granularity of monetary amounts.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `multiuserlookup` (object) — Represents the configuration of a multi-user lookup field, which enables associating a record with multiple CRM users through a linking module rather than a single user reference.
                - `linking_details` (object) **REQ** — Contains the configuration of the linking module and its lookup fields that connect the source module to multiple CRM users in a multi-user lookup relationship.
                  - `module` (object) **REQ** — Represents the linking module that intermediates the connection between the source module and the Users module in a multi-user lookup relationship.
                    - `plural_label` (string) **REQ** [maxLen=100] — Contains the plural display name of the linking module used in the multi-user lookup, as shown in navigation and relational panels within the CRM.
                    - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                  - `lookup_field` (object) **REQ** — Represents the lookup field on the linking module that references the source module, establishing the origin side of the multi-user lookup relationship.
                    - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                    - `field_label` (string) **REQ** [maxLen=100] — Contains the display label of the lookup field on the linking module that references the source module, as presented in the CRM interface.
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                  - `connected_lookup_field` (object) **REQ** — Represents the lookup field on the linking module that references the Users module, forming the user-side join in the multi-user lookup relationship.
                    - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                    - `field_label` (string) **REQ** [maxLen=100] — Contains the display label of the lookup field on the linking module that points to the Users module, as presented in the CRM interface.
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                - `record_access` (boolean) **REQ** — Indicates whether the multi-user lookup grants the associated users access to the record being linked, in addition to recording the relationship. Possible values: `true` — linked users gain record-level access; `false` — the relationship is recorded without affecting the users' access to the record.
              - `global_map_dependency` (object) — Represents the global map dependency linked to this field, which governs how the field's available values or behavior are influenced by a shared mapping configuration defined at the organization level. Contains identifying metadata for the associated global map dependency, or is absent when no such dependency applies.
                oneOf:
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the global map dependency.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `custom_field` (boolean) — Indicates whether this field was defined by an administrator or developer beyond the standard module schema, rather than being a built-in system field. Possible values: `true` — the field is user-created and does not belong to the default module definition; `false` — the field is a standard, system-defined field.
              - `lookup` (object) — Represents the lookup configuration that links this field to records in another CRM module, encapsulating the target module reference, the field's API name and display label within that module, and the unique identifier of the lookup relationship.
                oneOf:
                    - `display_label` (object)
                      oneOf:
                          type: string [maxLen=50] — Represents the active display label of the lookup field, shown to users in the CRM interface when the lookup relationship is referenced.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `revalidate_filter_during_edit` (boolean) — Indicates whether the lookup's filter criteria are re-evaluated each time the record is opened in edit mode, ensuring that the selectable records reflect current field values rather than the values at the time the record was first created. Possible values: `true` — filter criteria are reapplied during edit; `false` — filter criteria are applied only at initial field population.
                    - `api_name` (object)
                      oneOf:
                        - `ApiName` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the lookup field
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `module` (object) — Represents the target CRM module that this lookup field references, providing the module's identifying metadata — such as its name and encryption status — required to resolve and navigate the cross-module relationship.
                      - `api_name` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the lookup module
                      - `crypt` (boolean) — Indicates whether data stored in the lookup's target module is encrypted at rest, informing consumers that records retrieved through this lookup relationship may be subject to field-level encryption policies. Possible values: `true` — the target module's data is encrypted; `false` — the target module's data is not encrypted.
                      - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the lookup module
                    - `id` (object) — Represents the unique system-generated identifier for the lookup field definition within the target module. May be null for lookups created implicitly by the system rather than explicitly configured by an administrator.
                      oneOf:
                        - `Id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `query_details` (object) — Contains the query configuration used to filter the selectable records in the lookup dropdown, restricting available options based on field criteria or system-defined query identifiers.
                      oneOf:
                          title: Query Details with Criteria
                          - `query_id` (object) **REQ** — Represents the unique identifier of the custom query used to filter the lookup's selectable records, referencing a predefined query configuration that determines which records appear in the dropdown.
                            oneOf:
                                type: string/int64 [maxLen=30] — Represents the custom query identifier as a string value, referencing a predefined query configuration that filters the lookup's selectable records.
                                type: integer/int64 — Represents the custom query identifier as an integer value, referencing a predefined query configuration that filters the lookup's selectable records.
                          - `criteria` (object) **REQ** — Represents the field-level filter condition applied to the lookup query, defining the field, comparison operator, value, and type of criterion used to narrow the set of records displayed in the lookup.
                            - `comparator` (string) **REQ** [maxLen=50] — Represents the comparison operator applied when evaluating the filter criterion, such as equals, contains, starts with, or greater than, determining how the field value is tested against the specified filter value.
                            - `field` (object) **REQ** — Represents the field used as the left-hand operand in the lookup filter criterion, identifying which field's value is evaluated against the specified comparator and value.
                              - `api_name` (string) [maxLen=100] — Represents the API name of the field used in the lookup filter criterion, which may reference a standard field, a custom field, or a related field accessed through dot notation.
                              - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the field used in the criteria.
                            - `type` (string) **REQ** [maxLen=50] — Indicates whether the filter value is a static literal or a dynamic reference, controlling how the comparison value is resolved at runtime when the lookup list is rendered.
                            - `value` (object) — Represents the value compared against the selected field when evaluating the lookup filter criterion. Can be a string, number, or Boolean depending on the field type and the configured comparator.
                              oneOf:
                                  type: string [maxLen=255] — Represents a string value used as the right-hand operand when evaluating the lookup filter criterion.
                                  type: number — Represents a numeric value used as the right-hand operand when evaluating the lookup filter criterion.
                                  type: boolean — Represents a Boolean value used as the right-hand operand when evaluating the lookup filter criterion.
                                - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                          - `system_query_id` (object) **REQ** — Represents the system-assigned identifier for a platform-managed query that filters the lookup's record list, used when the filter logic is maintained by the CRM system rather than defined by a custom query.
                            oneOf:
                                type: string/int64 [maxLen=30] — Represents the system-assigned query identifier as a string, referencing a platform-managed query that filters the lookup's record list.
                              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                          title: Query Details System Only
                          - `system_query_id` (object) **REQ** — Represents the system-assigned identifier for an alternate platform-managed query variant that filters the lookup's record list in this configuration schema variant.
                            oneOf:
                                type: string/int64 [maxLen=30] — Represents the system-assigned query identifier as a string in the system-query-only variant, referencing a platform-managed filter for the lookup.
                              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `hipaa_compliance` (object)
                oneOf:
                    - `restricted_in_export` (boolean) **REQ** — Indicates whether this field's value is suppressed or masked when records are exported, in accordance with HIPAA data handling requirements. Possible values: `true` — the field is excluded or redacted in exported data sets; `false` — the field value is included in exports without HIPAA-based redaction.
                    - `restricted` (boolean) **REQ** — Indicates whether access to this field's value is restricted under HIPAA compliance rules, limiting visibility to only those users or roles authorized to handle protected health information. Possible values: `true` — the field is treated as restricted PHI and access controls are enforced; `false` — the field is not subject to HIPAA access restrictions.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `convert_mapping` (object) — Contains the cross-module field mapping configuration that governs how this field's value is transferred to corresponding fields in target modules (such as Accounts, Contacts, Deals, Invoices, or Sales Orders) when a record conversion is performed.
                oneOf:
                    title: Leads Field Convert Mapping
                    - `Contacts` (object) **REQ** — Represents the API name of the destination field in the **Contacts** module to which this field's value is mapped during record conversion, or null when no mapping to Contacts is defined.
                      oneOf:
                          type: string [maxLen=100] — Represents the API name of the target field in the **Contacts** module for this field's value during lead-to-Contacts conversion.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `Deals` (object) **REQ** — Represents the API name of the destination field in the **Deals** module to which this field's value is mapped during record conversion, or null when no mapping to Deals is defined.
                      oneOf:
                          type: string [maxLen=100] — Represents the API name of the target field in the **Deals** module for this field's value during lead-to-Deals conversion.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `Accounts` (object) **REQ** — Represents the API name of the destination field in the **Accounts** module to which this field's value is mapped during record conversion, or null when no mapping to Accounts is defined.
                      oneOf:
                          type: string [maxLen=100] — Represents the API name of the target field in the **Accounts** module for this field's value during lead-to-Accounts conversion.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    title: Quotes Field Convert Mapping
                    - `Invoices` (object) **REQ** — Represents the API name of the destination field in the **Invoices** module to which this field's value is mapped during record conversion, or null when no mapping to Invoices is defined.
                      oneOf:
                          type: string [maxLen=100] — Represents the API name of the target field in the **Invoices** module for this field's value during quote-to-Invoices conversion.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `Sales_Orders` (object) **REQ** — Represents the API name of the destination field in the **Sales_Orders** module to which this field's value is mapped during record conversion, or null when no mapping to Sales Orders is defined.
                      oneOf:
                          type: string [maxLen=100] — Represents the API name of the target field in the **Sales_Orders** module for this field's value during quote-to-Sales_Orders conversion.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    title: Sales Orders Field Convert Mapping
                    - `Invoices` (object) **REQ** — Represents the API name of the destination field in the **Invoices** module to which this field's value is mapped under an alternate conversion schema variant, or null when no mapping to Invoices is defined in this context.
                      oneOf:
                          type: string [maxLen=100] — Represents the API name of the target field in the **Invoices** module for this field's value during Sales Order-to-Invoices conversion.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    title: No Convert Mapping
              - `address` (object) — Contains the address sub-field configuration applicable when the field represents a composite address type, such as mailing or billing address, grouping individual components like street, city, state, and country into a structured object.
                oneOf:
                    - `type` (string) **REQ** [maxLen=25] — Represents the classification of the address, distinguishing between address categories such as mailing, billing, or shipping to determine how the composite address field is labeled and used within the module layout.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `rollup_summary` (object) — Represents the rollup summary configuration for this field, defining how aggregated values from related records in a child module are calculated and displayed in the parent record's field.
                oneOf:
                    - `return_type` (string) [maxLen=50] — Indicates the data type of the value produced by the rollup summary calculation, such as integer, decimal, or date, which determines how the computed result is stored and displayed.
                    - `expression` (object) — Contains the expression configuration for the rollup summary calculation, including the aggregation function, the field being summarized, and any filter criteria applied to restrict which related records are included.
                      - `function_parameters` (array of object) [maxItems=100] **REQ** — Contains the list of parameters passed to the rollup aggregation function, specifying which fields or values are used as inputs to the calculation.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the parameter field
                      - `criteria` (object) — Represents the filter conditions applied to limit which related records in the child module are included in the rollup summary calculation.
                        oneOf:
                            - `comparator` (string) **REQ** [maxLen=25] — Represents the comparison operator used in the rollup filter criterion, applied when evaluating whether a related record's field value satisfies the filter condition.
                            - `field` (object) **REQ** — Identifies the field in the child module whose value is tested against the comparator and filter value when determining which related records are included in the rollup.
                              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the child module field used in the rollup filter criterion.
                              - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the criteria field
                            - `type` (string) **REQ** [maxLen=25] — Indicates whether the filter value in the rollup criterion is a static literal or a dynamic reference resolved at runtime.
                            - `value` (string) **REQ** [maxLen=100] — Represents the value compared against the child module field when evaluating the rollup filter criterion.
                          - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                      - `function` (string) **REQ** [maxLen=25] — Represents the aggregation function applied to the child module records when computing the rollup summary, such as SUM, COUNT, MIN, MAX, or AVERAGE.
                    - `based_on_module` (object) — Represents the child module from which related records are aggregated when computing the rollup summary value for this field.
                      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the base module
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the base module
                    - `related_list` (object) — Represents the related list configuration that defines the child module relationship from which records are drawn for the rollup summary calculation.
                      oneOf:
                          - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the related list
                          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the related list
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `rollup_based_on` (string) [maxLen=50] — Indicates the basis of the rollup calculation, specifying whether the aggregation operates on all related records or only on a filtered subset defined by the expression criteria.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `length` (number/int32) — Represents the maximum number of characters or digits permitted for this field's value, defining the storage and input boundary enforced by the CRM when records are saved.
              - `column_name` (string) [maxLen=100] — Represents the underlying database column identifier mapped to this field, used for direct data-layer references and query construction within the CRM storage layer.
              - `display_field` (boolean) — Indicates whether this field is designated as the primary display field for the module, used to represent the record in lookups, related lists, and search results. Possible values: `true` — the field serves as the record's display identifier; `false` — the field is not the primary display field.
              - `pick_list_values_sorted_lexically` (boolean) — Indicates whether the picklist options for this field are automatically sorted in alphabetical order for display, rather than in the administrator-defined sequence order. Possible values: `true` — options are sorted alphabetically; `false` — options appear in the order defined by the administrator.
              - `default_value` (object) — Represents the pre-populated value automatically applied to this field when a new record is saved, serving as a baseline entry that users can override during data entry.
                oneOf:
                    type: string [maxLen=255] — Represents the default string or numeric value pre-populated in this field when a new record is saved.
                    type: boolean — Represents the default Boolean value pre-populated in this field when a new record is saved.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `sortable` (boolean) — Indicates whether records can be sorted by this field's value in list views, reports, and search results. Possible values: `true` — the field is available as a sort key; `false` — the field cannot be used for sorting.
              - `sequence_number` (number/int32) [min=1] — Represents the ordinal position of this field within its containing section, controlling the order in which fields are rendered on record forms. Sequence numbering generally starts from one but may contain gaps.
              - `global_picklist` (object) — Represents the organization-level picklist configuration shared across multiple modules that this field draws its allowed values from. When present, the field's pick options are centrally managed through the referenced global picklist rather than defined locally on the field itself.
                oneOf:
                    - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the global picklist
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the global picklist
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `display_format` (object) — Specifies the presentation pattern applied when rendering the field's value in the UI, such as a date format string, a time pattern, or a number format template controlling separators and symbol placement.
                oneOf:
                    type: string [maxLen=50] — Represents the active display format pattern for this field, such as a date format string or number format template applied when rendering the field's value in the UI.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `history_tracking` (object) — Represents the history tracking configuration for this field, capturing how and for how long changes to the field's value are recorded in the audit trail. Includes details about tracked duration, associated modules, related list linkage, and the specific fields whose changes are followed.
                oneOf:
                    - `related_list_name` (string) [maxLen=100] — Represents the display name of the related list through which the field's historical change records are surfaced on the associated module's detail view, allowing end users to review the audit trail directly within the record context.
                    - `module` (object) — Represents the CRM module with which this field's history tracking is associated, providing the module-level context required to correctly scope, store, and surface field change records in the appropriate audit trail.
                      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the history tracking module
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the history tracking module
                    - `duration_configured_field` (object)
                      oneOf:
                          - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the duration field
                          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the duration field
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `duration_configuration` (string) [maxLen=120] — Contains the settings that govern the time window over which field value changes are retained in the history log, such as the retention period length and applicable time units used to define how far back historical data is preserved.
                    - `followed_fields` (array of object) [maxItems=100] — Contains the collection of fields whose value changes are actively monitored and recorded as part of this field's history tracking configuration, allowing administrators to scope audit trail capture to a defined subset of related fields.
                      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the followed field
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the followed field
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `data_type` (string) [maxLen=50] — Identifies the data category assigned to the field, such as text, integer, decimal, date, Boolean, picklist, or lookup, which governs validation rules, storage format, and applicable UI controls.
              - `formula` (object) — Contains the formula configuration for fields whose values are automatically calculated from expressions referencing other fields or functions, rather than being entered directly by users.
                oneOf:
                    - `return_type` (string) **REQ** [maxLen=25] — Identifies the data type produced by the formula expression, such as string, integer, decimal, date, or Boolean, which determines how the computed value is stored and displayed.
                    - `expression` (string) **REQ** [maxLen=3000] — Contains the formula expression string that defines the calculation logic, composed of function calls, field API name references, and operators that the CRM engine evaluates to produce the field's computed value.
                    - `evaluation_order` (integer/int32) [min=1] — Indicates the relative priority in which this formula field is evaluated when multiple formula fields exist in the same module and share dependencies, ensuring upstream values are resolved before downstream ones.
                    - `sub_return_type` (object) — Represents a secondary classification of the formula's output type, refining the primary return type to indicate a more specific data size or unit. Possible values: `small` — a compact representation of the return type. `medium` — a standard-size representation. `large` — a large-size representation.
                      oneOf:
                          type: string [maxLen=25, enum=['small', 'medium', 'large']] — Represents the active secondary type classification for the formula's return value. Possible values: `small` — a compact representation. `medium` — a standard-size representation. `large` — a large-size representation.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `dynamic` (boolean) **REQ** — Indicates whether the formula is recalculated in real time as dependent field values change, rather than being evaluated only at save time. Possible values: `true` — the formula updates dynamically during record editing; `false` — the formula is evaluated only when the record is saved.
                    - `stop_compute_conditionally` (boolean) **REQ** — Indicates whether the formula evaluation halts when a specified logical condition is met. Possible values: `true` — the formula stops computing once the stop condition expression evaluates to true; `false` — the formula computes to completion regardless of intermediate conditions.
                    - `assume_default` (boolean) — Indicates whether null or missing operand values in the formula expression are treated as zero or an equivalent default, rather than causing the formula result to be null. Possible values: `true` — null operands are substituted with default values; `false` — null operands propagate as null through the calculation.
                    - `stop_compute_expression` (object) **REQ** — Contains the logical expression evaluated at runtime to determine whether formula computation should be interrupted. When the expression resolves to true and stop_compute_conditionally is enabled, further formula processing is skipped and the current interim value is retained.
                      oneOf:
                          type: string [maxLen=3000] — Represents the active logical expression evaluated to determine whether formula computation should be halted before completion.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    additionalProperties: any
                    title: No Formula
              - `static_field` (boolean) — Indicates whether this field is a static layout element with a fixed value that does not accept user input. Possible values: `true` — the field is a static display-only element; `false` — the field accepts dynamic user-entered or system-computed values.
              - `additional_column` (object)
                oneOf:
                    type: string [maxLen=100] — Represents the additional column configuration for the field, specifying display settings when the field appears as an extra column in module list views.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `hipaa_compliance_enabled` (boolean) — Indicates whether HIPAA compliance enforcement is active for this field, determining whether the associated HIPAA access and export restrictions are applied at runtime. Possible values: `true` — HIPAA compliance rules are enforced for this field; `false` — HIPAA compliance is not enforced and the field is treated as non-PHI data.
              - `query_details` (object) — Contains the query configuration applied to filter the selectable records in this field's lookup or dependent logic, using either custom query identifiers or field-level criteria expressions.
                oneOf:
                    - `query_id` (integer/int64) **REQ** — Represents the unique identifier of the custom query used to filter this field's selectable options or lookup results.
                    - `criteria` (object) **REQ** — Represents the field-level filter condition for the query, specifying the field, comparator, type, and value used to narrow down the set of records or options.
                      - `comparator` (string) **REQ** [maxLen=25] — Represents the comparison operator used in the filter criterion, such as equals, contains, or greater than, applied when evaluating whether a record or value satisfies the filter.
                      - `field` (object) **REQ** — Identifies the field whose value is evaluated against the comparator and filter value in the query criteria.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the field used in the criteria.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the field used in the criteria.
                      - `type` (string) **REQ** [maxLen=50] — Indicates whether the comparison value in the filter criterion is a static literal or a dynamic contextual reference resolved at runtime.
                      - `value` (object) — Represents the value compared against the selected field when evaluating the query filter criterion.
                        oneOf:
                            type: string [maxLen=255] — Represents a string value used as the comparison operand in the field-level lookup filter criterion.
                            type: number — Represents a numeric value used as the comparison operand in the field-level lookup filter criterion.
                            type: boolean — Represents a Boolean value used as the comparison operand in the field-level lookup filter criterion.
                          - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `decimal_place` (object)
                oneOf:
                    type: number/int32 — Represents the number of decimal places configured for the field, defining the precision applied when storing and displaying fractional values.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `mass_update` (boolean) — Indicates whether this field can be updated simultaneously across multiple records using the mass update operation. Possible values: `true` — the field is available for mass update; `false` — the field cannot be modified through bulk update actions.
              - `multiselectlookup` (object)
                oneOf:
                    - `linking_details` (object) — Contains the configuration of the intermediary linking module that joins the source and target modules in a multi-select lookup relationship, including the relevant lookup fields on each side.
                      - `module` (object) **REQ** — Represents the intermediary linking module that bridges the source and target modules in a multi-select lookup, storing the join records that implement the many-to-many relationship.
                        - `visibility` (number/int32) **REQ** — Indicates the visibility state of the linking module, controlling whether it appears in the CRM interface and navigation for end users.
                        - `plural_label` (string) **REQ** [maxLen=100] — Contains the plural display name of the linking module, as shown in navigation and relational UI elements within the CRM.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                      - `lookup_field` (object) **REQ** — Represents the lookup field on the linking module that points back toward the source module, establishing the origin side of the multi-select lookup relationship.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                        - `field_label` (string) **REQ** [maxLen=100] — Contains the display label of the lookup field on the linking module that references the source module, as presented in the CRM interface.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                      - `connected_lookup_field` (object) **REQ** — Represents the lookup field on the linking module that points toward the connected (target) module, completing the many-to-many association in the multi-select lookup.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                        - `field_label` (string) **REQ** [maxLen=100] — Contains the display label of the lookup field on the linking module that references the connected target module, as presented in the CRM interface.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                    - `connected_details` (object) — Contains metadata about the target module and its associated layouts and fields that the multi-select lookup field resolves records against.
                      - `field` (object) **REQ** — Represents the specific field in the connected module that is referenced by the multi-select lookup, used to surface a meaningful value from the related record.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                        - `field_label` (string) **REQ** [maxLen=100] — Contains the display label of the referenced field in the connected module, as shown to users when viewing or configuring the multi-select lookup.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                      - `module` (object) **REQ** — Represents the target module to which the multi-select lookup field resolves, providing display and identification attributes for that module.
                        - `plural_label` (string) **REQ** [maxLen=100] — Contains the plural display name of the connected module, typically shown in list views and relationship panels referencing multiple records.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                      - `layouts` (array of object) [maxItems=100] **REQ** — Contains the collection of layouts within the connected module in which the multi-select lookup field is available or rendered.
                        - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                    - `related_list` (object) — Represents the related list configuration associated with the multi-select lookup field, defining how linked records from the target module are displayed within the source record's detail view.
                      - `display_label` (string) **REQ** [maxLen=50] — Contains the label for the related list panel as rendered on the source record's detail page, identifying the collection of linked target-module records.
                      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `auto_number` (object)
                oneOf:
                    - `starting_number_length` (number/int32) — Represents the total digit length of the starting number used in the auto-number sequence, controlling zero-padding and minimum width of generated values.
                    - `prefix` (object)
                      oneOf:
                          type: string [maxLen=10] — Represents the text string prepended to each auto-generated number in the sequence.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `start_number` (object)
                      oneOf:
                          type: number/int32 — Represents the numeric value at which the auto-number sequence begins.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                    - `suffix` (object)
                      oneOf:
                          type: string [maxLen=10] — Represents the text string appended to each auto-generated number in the sequence.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `quick_sequence_number` (string) [maxLen=10] — Represents the ordinal position of this field in the quick-create form layout, determining the display order of fields when users create records through abbreviated entry panels.
              - `category` (number/int32) — Indicates the classification category of the field, used to group fields by their functional role or origin within the module layout, such as standard, custom, or system-defined categories.
              - `blueprint_supported` (boolean) — Indicates whether the field can participate in Blueprint process definitions, enabling it to be referenced in transition conditions and actions within automated workflow stages. Possible values: `true` — the field is eligible for use in Blueprint configurations; `false` — the field cannot be included in Blueprint process logic.
              - `textarea` (object) — Contains the textarea-specific configuration for fields that render as multi-line text input areas, including details about the text area subtype.
                - `type` (string) **REQ** [maxLen=50, enum=['small', 'large', 'rich_text']] — Represents the subtype of the textarea field, distinguishing between multi-line input variants that affect formatting and storage behavior. Possible values: `small` — a compact single-line or short textarea. `large` — a standard multi-line plain text area. `rich_text` — a rich text editor with formatting support.
              - `element_type` (string) [maxLen=50, enum=['field', 'mirror_field']] — Represents the structural element type of this entry in the layout, distinguishing standard data fields from mirror fields. Possible values: `field` — a standard data field that accepts or displays a value. `mirror_field` — a field that reflects a value from a related module through a lookup relationship.
              - `enable_record_category` (boolean) — Indicates if the record category feature is enabled for this picklist field. Only returned when the record category feature is available.
              - `record_category_tracking_field` (object) — Reference to the field used to track record category changes over time in the timeline view. Only present when enable_record_category is true and a tracking field is configured.
                oneOf:
                    - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the tracking field.
                    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the tracking field.
                  - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
              - `enable_transition_for_record_category` (boolean) — Indicates if transitions between record categories are enabled. Only returned when enable_record_category is true.
              - `record_category_values` (array of object) [maxItems=50] — List of record category values defined for this picklist field. Only returned when enable_record_category is true.
                - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the record category.
                - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the record category.
                - `value` (string) **REQ** [maxLen=120] — Display value of the record category.
                - `nature_of_category` (string) **REQ** [enum=['none', 'thumbs_up', 'thumbs_down']] — Nature of the record category indicating sentiment or outcome.
              - `lookup_field` (object) — Represents the source lookup field on which a mirror field is based, identifying the cross-module lookup relationship from which this field's value is derived.
                - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                - `api_name` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
            - `properties` (object)
              oneOf:
                - `SectionProperties` — Represents the additional configuration properties for subform sections, including row-level interaction settings, tooltip configuration, and conditional display preferences.
                  - `reorder_rows` (boolean) — Indicates whether users are permitted to reorder existing rows within the subform section by dragging them to a new position. Possible values: `true` — row reordering is allowed; `false` — rows cannot be reordered.
                  - `bulk_addition` (object)
                    oneOf:
                        - `lookup_field` (object) **REQ** — The lookup field used for bulk addition
                          - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                          - `name` (string) **REQ** [maxLen=100] — Display name of the lookup field
                        - `subform_fields` (object) **REQ**
                          oneOf:
                              type: array of object [maxItems=50]
                                - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                                - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                                - `name` (string) **REQ** [maxLen=100] — Display name of the subform field
                            - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                      - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                  - `tooltip` (object)
                    oneOf:
                        - `name` (string) **REQ** [maxLen=255] — Indicates the delivery mechanism for the section tooltip, such as whether it is rendered as a static label or as a modal help popup.
                        - `value` (string) **REQ** [maxLen=255] — Contains the help text displayed in the section tooltip, providing contextual guidance about the purpose or use of the section.
                      - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                  - `maximum_rows` (number/int32) [min=1] — Indicates the maximum number of rows that can be added to the subform section, controlling how many related records can be embedded in a single parent record's layout.
                  - `preference` (array of object) [maxItems=50] — Contains the conditional display criteria for the section, defining the field conditions that must be satisfied for the section to be shown or for certain section behaviors to be applied.
                    - `comparator` (string) **REQ** [maxLen=50] — Represents the comparison operator applied when evaluating the section preference criterion, such as equals, contains, or is not null.
                    - `field` (object) **REQ** — Identifies the field whose value is evaluated against the comparator and preference value to determine whether the section's conditional display condition is met.
                      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the field used in the criteria.
                      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the field used in the criteria.
                    - `type` (string) **REQ** [maxLen=50] — Indicates whether the comparison value in the preference criterion is a static literal or a dynamic contextual reference resolved at runtime.
                    - `value` (object) **REQ** — Represents the value compared against the selected field when evaluating the section preference criterion, which may be a string, number, or Boolean depending on the field type.
                      oneOf:
                          type: string [maxLen=255] — Represents a string value used as the comparison operand in the section preference criterion.
                          type: number — Represents a numeric value used as the comparison operand in the section preference criterion.
                          type: boolean — Represents a Boolean value used as the comparison operand in the section preference criterion.
                        - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
                - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `display_label` (string) **REQ** [maxLen=100, minLen=1] — Represents the label of the layout as displayed in the CRM interface, shown in layout selection dropdowns and record settings.
          - `show_business_card` (boolean) **REQ** — Indicates whether the business card view is enabled for this layout, allowing a compact summary of key fields to be shown in preview and lookup contexts. Possible values: `true` — business card view is active; `false` — business card view is not enabled.
          - `actions_allowed` (object `LayoutActionsAllowed`) **REQ** — Permissions indicating which operations are allowed on this layout
            schema: `LayoutActionsAllowed`
            - `edit` (boolean) **REQ** — Indicates whether the layout's field arrangement, sections, and configuration can be modified. Possible values: `true` — editing the layout is permitted; `false` — the layout is locked against edits.
            - `rename` (boolean) **REQ** — Indicates whether the layout's display name can be changed. Possible values: `true` — renaming the layout is permitted; `false` — the layout name is locked.
            - `clone` (boolean) **REQ** — Indicates whether the layout can be duplicated to create a new layout with the same field and section configuration. Possible values: `true` — cloning the layout is permitted; `false` — the layout cannot be cloned.
            - `downgrade` (boolean) **REQ** — Indicates whether the layout can be downgraded to a lower-tier configuration or reverted to a previous edition-level feature set. Possible values: `true` — downgrading the layout is permitted; `false` — the layout cannot be downgraded.
            - `delete` (boolean) **REQ** — Indicates whether the layout can be permanently removed from the module configuration. Possible values: `true` — deleting the layout is permitted; `false` — the layout cannot be deleted.
            - `deactivate` (boolean) **REQ** — Indicates whether the layout can be deactivated, preventing it from being assigned to new records while preserving existing associations. Possible values: `true` — deactivating the layout is permitted; `false` — the layout cannot be deactivated.
            - `set_layout_permissions` (boolean) **REQ** — Indicates whether profile-level permission assignments for the layout can be configured. Possible values: `true` — managing layout permissions is permitted; `false` — permission settings cannot be modified for this layout.
          - `modified_time` (object) **REQ**
            oneOf:
                type: string/date-time — Represents the ISO 8601 datetime with timezone offset recording when this layout's configuration was most recently changed.
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the layout
          - `name` (string) **REQ** [maxLen=40, minLen=1] — Represents the internal API name of the layout, used as a programmatic identifier in API operations and automation configurations.
          - `modified_by` (object) **REQ**
            oneOf:
              - `UserReference` — User who last modified the layout
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `generated_type` (string) **REQ** [enum=['system', 'custom']] — Indicates whether this layout originates from automatic system generation or from an administrator's manual configuration. Possible values: `system` — automatically generated by Zoho CRM. `custom` — created manually by an administrator.
          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
          - `total_profiles` (number/int32) — Indicates the total number of CRM profiles associated with this layout, which may exceed the number of profiles included in the current response when has_more_profiles is true.
          - `status` (string) **REQ** [enum=['active', 'inactive', 'downgraded', 'hidden']] — Indicates the current operational status of the layout. Possible values: `active` — the layout is in use and can be assigned to profiles; `inactive` — the layout has been deactivated and is not available for new assignments.
      - `LayoutFieldsResponseSchema` — Represents the response returned when the `fields` query parameter trims each layout to the requested keys. Only `id` is guaranteed - it is returned even when it is not requested - every other key appears only when it was asked for, and keys with no value for a layout are returned as null.
        - `layouts` (array of object) [maxItems=15] **REQ** — Represents the array of layout objects trimmed to the keys requested through the `fields` parameter, ordered by layout name.
          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the layout.
          - `name` (string) [maxLen=40, minLen=1] — Represents the internal API name of the layout.
          - `api_name` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the layout.
          - `display_label` (string) [maxLen=100, minLen=1] — Represents the display label of the layout shown in the CRM interface.
          - `created_time` (object)
            oneOf:
                type: string/date-time — ISO 8601 datetime with timezone offset indicating when the layout was created.
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `modified_time` (object)
            oneOf:
                type: string/date-time — ISO 8601 datetime with timezone offset indicating when the layout was last modified.
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `created_by` (object)
            oneOf:
              - `UserReference` — User who created the layout.
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `modified_by` (object)
            oneOf:
              - `UserReference` — User who last modified the layout.
              - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
          - `status` (string) [enum=['active', 'inactive']] — Represents the current status of the layout.
          - `visible` (boolean) — Indicates whether the layout is visible to users in the CRM interface.
          - `show_business_card` (boolean) — Indicates whether the business card view is enabled for this layout.
          - `generated_type` (string) [enum=['system', 'custom']] — Indicates whether the layout was generated by the system or created by a user.
          - `source` (string) [enum=['crm', 'platform_plugin', 'marketplace_plugin', 'campaign_integration']] — Represents the source from which this layout was created.

- **400**: Bad request response returned when the request contains invalid or missing parameters. [application/json]
    > Represents the error response body returned when a request is rejected due to invalid parameters, missing required inputs, or unsupported operations.
    - `code` (string) **REQ** [enum=[5 values]] — Represents the error classification for the bad request. Possible values: `REQUIRED_PARAM_MISSING` — a required parameter was absent from the request; `INVALID_MODULE` — the specified module does not exist or is not accessible; `INVALID_REQUEST_METHOD` — the HTTP method used is not supported for this endpoint; `PATTERN_NOT_MATCHED` — a parameter value did not conform to the expected format; `NOT_SUPPORTED` — the requested operation is not supported.
    - `details` (object) **REQ** — Contains supplementary information about the bad request error, identifying the specific parameter or condition responsible for the failure.
      - `param_name` (string) [maxLen=100] — Represents the name of the request parameter that triggered the bad request error.
    - `message` (string) **REQ** [maxLen=255] — Represents a plain-language description of the bad request error, suitable for logging or surfacing to an end user.
    - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request. Possible values: `error` — the request was not processed successfully due to a bad request condition.

- **401**: Unauthorized response returned when authentication fails or the provided credentials are invalid or missing. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

- **404**: Not-found response returned when the requested URL does not match any recognised API endpoint pattern. [application/json]
    > Represents the error response body returned when the requested endpoint URL does not match any recognised API route.
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error classification for the not-found condition. Possible values: `INVALID_URL_PATTERN` — the request URL does not match any recognised endpoint pattern.
    - `details` (object) **REQ** — Contains supplementary information about the not-found error, providing additional context about the unrecognised URL.
    - `message` (string) **REQ** [maxLen=255] — Contains a descriptive explanation of why the requested resource could not be found, intended to aid in diagnosing the cause of the error.
    - `status` (string) **REQ** [enum=['error']] — Indicates the outcome classification of the response. Possible values: `error` — the request did not complete successfully and the response body contains error details.

- **500**: Internal server error response returned when an unexpected failure occurs on the server side while processing the request. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

**Scopes:** ZohoCRM.settings.layouts.READ
