# GET /settings/fields/{fieldId}
**Operation:** `getFieldsWithID` — Get field metadata by ID
> To retrieve the metadata of a specific custom field in a module in your Zoho CRM account by its field ID.

**Parameters:**
- `module` (query, string, required) [maxLen=30] {style=form, explode=True}: Specify the API name of the module for which you want to retrieve field metadata. For example, the module name 'Leads'.
- `fieldId` (path, string/int64, required): Specify the unique ID of the custom field to retrieve.
- `include` (query, string, optional) [maxLen=50, enum=['allowed_permissions_to_update']] {style=form, explode=True}: Specify whether to include the allowed_permissions JSON object in the response
- `type` (query, string, optional) [maxLen=10, enum=['all', 'unused', 'used']] {style=form, explode=True}: Specify the type of fields to be retrieved. Example: 'used', 'unused', etc.

**Responses:**

- **200**: Returns the metadata for the custom field identified by the specified field ID. [application/json]
    > Represents the response body for the single-field metadata request, containing an array with one field configuration object.
    - `fields` (array of object `FieldSchema`) [maxItems=1] **REQ** — Represents the list of field metadata objects for the specified field, containing one entry.
      schema: `FieldSchema`
      - `mask_details` (object)
        oneOf:
            additionalProperties: any
          - `TypeNull` (null) — Represents the null if no information is available.
      - `associated_module` (object)
        oneOf:
            - `module` (string) **REQ** [maxLen=100] — Represents the name of the module.
            - `id` (string/int64) **REQ** — Id of the resource.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `webhook` (boolean) **REQ** — Indicates whether webhook is enabled for the field.
      - `operation_type` (object) **REQ** — Represents the operation types allowed for the field.
        - `web_update` (boolean) **REQ** — Indicates whether the field can be updated through the web.
        - `api_create` (boolean) **REQ** — Indicates whether the field can be created through the API.
        - `web_create` (boolean) **REQ** — Indicates whether the field can be created through the web.
        - `api_update` (boolean) **REQ** — Indicates whether the field can be updated through the API.
      - `colour_code_enabled_by_system` (boolean) **REQ** — Indicates whether colour coding is enabled for this field by the system.
      - `field_label` (string) **REQ** [maxLen=100] — Represents the display name of the field in the user's preferred language.
      - `tooltip` (object)
        oneOf:
            - `name` (string) **REQ** [maxLen=25] — Represents the it gives the name of the tool tip.
            - `value` (string) **REQ** [maxLen=255] — Represents the text for the tool tip.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `display_format_properties` (object)
        oneOf:
            - `split` (number/int32) — Represents the split value applied to phone number fields, which divides the number into the specified number of segments.
            - `radio_display_type` (string) [maxLen=25] — Represents the display type applied to radio button fields, such as **all** or **vertical**.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `type` (string) **REQ** [maxLen=25] — Represents the type of the field used or unused.
      - `field_read_only` (boolean) **REQ** — Indicates whether the field is always read-only and cannot be edited under any circumstances.
      - `customizable_properties` (object)
        oneOf:
            type: array of string [maxItems=100]
              type: string [maxLen=50] — Represents a customizable property of the field.
              items: [maxLen=50]
          - `TypeNull` (null) — Represents the null if no information is available.
      - `display_label` (string) **REQ** [maxLen=50] — Represents the display label of the field.
      - `read_only` (boolean) **REQ** — Indicates whether the field is read-only for the current user.
      - `association_details` (object) **REQ**
        oneOf:
            - `related_field` (object) **REQ** — Represents the details of the related field.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) **REQ** — Id of the resource.
            - `lookup_field` (object) **REQ** — Represents the details of the lookup field.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) **REQ** — Id of the resource.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `businesscard_supported` (boolean) **REQ** — Indicates whether the field can be added to the business card section.
      - `multi_module_lookup` (object) **REQ**
        oneOf:
            - `display_label` (string) [maxLen=50] — Represents the display label of the multi module lookup.
            - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
            - `modules` (array of object) [maxItems=100] — Represents the list of modules associated with the multi module lookup.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `module_name` (string) **REQ** [maxLen=50] — Represents the name of the module.
              - `id` (string/int64) **REQ** — Id of the resource.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `id` (string/int64) **REQ** — Id of the resource.
      - `created_time` (object)
        oneOf:
            type: string/date-time — Represents the time when the record was created.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `filterable` (boolean) **REQ** — Indicates if the field is filterable.
      - `visible` (boolean) **REQ** — Indicates if the field is visible.
      - `profiles` (array of object) [maxItems=50] **REQ** — Represents the list of profiles associated with the field.
        - `permission_type` (string) **REQ** [maxLen=25] — Represents the type of permission granted.
        - `name` (string) **REQ** [maxLen=60] — Represents the name of the profile.
        - `id` (string/int64) **REQ** — Id of the resource.
      - `view_type` (object) **REQ** — Represents the view type details of the field.
        - `view` (boolean) **REQ** — Indicates if the field is viewable.
        - `edit` (boolean) **REQ** — Indicates if the field is editable.
        - `quick_create` (boolean) **REQ** — Indicates if the field supports quick create.
        - `create` (boolean) **REQ** — Indicates if the field supports create.
      - `separator` (boolean) **REQ** — Indicates if the field is a separator.
      - `searchable` (boolean) **REQ** — Indicates if the field is searchable.
      - `history_tracking_enabled` (boolean) **REQ** — Indicates if history tracking is enabled for the field.
      - `external` (object) **REQ**
        oneOf:
            - `show` (boolean) **REQ** — Indicates if the external field is shown.
            - `type` (string) **REQ** [maxLen=50] — Indicates the type of the external field.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
      - `parent_field` (object)
        oneOf:
            - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
            - `name` (string) **REQ** [maxLen=50] — Represents the name of the parent field.
            - `id` (string/int64) **REQ** — Id of the resource.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `unique` (object) **REQ** — Represents the uniqueness details of the field.
        - `case_sensitive` (boolean) — Indicates if the uniqueness is case sensitive.
      - `enable_colour_code` (boolean) **REQ** — Indicates if colour code is enabled for the field.
      - `child_fields` (object)
        oneOf:
            type: array of object [maxItems=100]
              - `sequence_number` (number/int32) **REQ** — Represents the sequence number of the child field present in the Address field.
              - `field` (object) **REQ** — Represents the details of the child Address field.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `name` (string) **REQ** [maxLen=100] — Represents the name of the child Address field.
                - `id` (string/int64) **REQ** — Id of the resource.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `reference_id` (string) [maxLen=255, pattern=\{\{[a-zA-Z0-9]+\}\}] — Represents the temporary identifier used to reference a screen within the same wizard request payload.
      - `pick_list_values` (object) **REQ**
        oneOf:
            type: array of object [maxItems=100]
              - `display_value` (string) **REQ** [maxLen=120] — Represents the display value of the picklist option shown in the user interface.
              - `sequence_number` (number/int32) **REQ** — Represents the order position of the picklist option in the dropdown list.
              - `reference_value` (string) **REQ** [maxLen=120] — Represents the reference value of the picklist option used by integrations and reports.
              - `colour_code` (string) [maxLen=20] — Represents the colour code associated with the picklist option.
              - `actual_value` (string) **REQ** [maxLen=120] — Represents the actual stored value of the picklist option.
              - `id` (string/int64) **REQ** — Id of the resource.
              - `type` (string) **REQ** [maxLen=50] — Represents whether the picklist option is used or unused in the module.
              - `record_category_value` (object) — Reference to an existing record category value mapped to this picklist option. **At least one identifier must be provided**: `id`, `rid`, or `api_name`. Multiple identifiers can be provided for validation purposes. Server-side validation enforces this requirement.
                - `id` (string/int64) — Unique identifier of the record category value
                - `api_name` (string) [maxLen=255] — API name of the record category value
          - `TypeNull` (null) — Represents the null if no information is available.
      - `enable_record_category` (boolean) — Indicates if the record category feature is enabled for this picklist field. Only returned when the record category feature is available.
      - `record_category_tracking_field` (object) — Reference to the field used to track record category changes over time in the timeline view. Only present when enable_record_category is true and a tracking field is configured.
        oneOf:
            - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the tracking field.
            - `id` (string/int64) **REQ** — Unique identifier of the tracking field.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `enable_transition_for_record_category` (boolean) — Indicates if transitions between record categories are enabled. Only returned when enable_record_category is true.
      - `record_category_values` (array of object) [maxItems=50] — List of record category values defined for this picklist field. Only returned when enable_record_category is true.
        - `id` (string/int64) **REQ** — Unique identifier of the record category.
        - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the record category.
        - `value` (string) **REQ** [maxLen=120] — Display value of the record category.
        - `nature_of_category` (string) **REQ** [enum=['none', 'thumbs_up', 'thumbs_down']] — Nature of the record category indicating sentiment or outcome.
      - `system_mandatory` (boolean) **REQ** — Indicates if the field is system mandatory.
      - `private` (object)
        oneOf:
            - `restricted` (boolean) **REQ** — Indicates if the field is restricted.
            - `type` (string) **REQ** [maxLen=25] — Represents the type of privacy.
            - `export` (boolean) **REQ** — Indicates if the field is exportable.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `virtual_field` (boolean) **REQ** — Indicates if the field is a virtual field.
      - `json_type` (string) [maxLen=25] — Represents the jSON type of the field.
      - `crypt` (object)
        oneOf:
            - `mode` (string) **REQ** [maxLen=25] — Represents the encryption mode used.
            - `encrypt_case` (object)
              oneOf:
                  type: string [maxLen=25] — Represents the details of the encryption case.
                - `TypeNull` (null) — Represents the null if no information is available.
            - `status` (number/int32) **REQ** — Represents the status of the encryption.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `range` (object) **REQ**
        oneOf:
            - `from` (number/double) **REQ** — Represents the starting value of the range.
            - `to` (number/double) **REQ** — Represents the ending value of the range.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `created_source` (string) **REQ** [maxLen=60] — Represents the source from which the field was created.
      - `display_type` (number/int32) **REQ** — Represents the display type of the field.
      - `ui_type` (number/int32) **REQ** — Represents the UI type of the field.
      - `modified_time` (object)
        oneOf:
            type: string/date-time — Represents the time when the record was last modified.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `public` (boolean) **REQ** — Indicates if the field is public.
      - `email_parser` (object) **REQ** — Represents the email parser details of the field.
        - `fields_update_supported` (boolean) **REQ** — Indicates if field updates are supported by email parser.
        - `record_operations_supported` (boolean) **REQ** — Indicates if record operations are supported by email parser.
      - `currency` (object) **REQ**
        oneOf:
            - `rounding_option` (string) [maxLen=25] — Represents the rounding option for the currency.
            - `precision` (number/int32) — Represents the precision of the currency.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `custom_field` (boolean) **REQ** — Indicates if the field is a custom field.
      - `lookup` (object) **REQ**
        oneOf:
            - `display_label` (object)
              oneOf:
                  type: string [maxLen=50] — Display label of the lookup field
                - `TypeNull` (null) — Represents the null if no information is available.
            - `revalidate_filter_during_edit` (boolean) — Indicates if the filter should be revalidated during edit.
            - `api_name` (object)
              oneOf:
                - `ApiName` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `TypeNull` (null) — Represents the null if no information is available.
            - `module` (object) — Represents the module details for the lookup field.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `crypt` (boolean) **REQ** — Indicates if the module is encrypted.
              - `id` (string/int64) **REQ** — Id of the resource.
            - `id` (object)
              oneOf:
                - `Id` (string/int64) — Id of the resource.
                - `TypeNull` (null) — Represents the null if no information is available.
            - `query_details` (object) — Represents the query details for the lookup field.
              - `system_query_id` (object) **REQ**
                oneOf:
                    type: string/int64 [maxLen=30] — Represents the system query ID for the lookup field.
                  - `TypeNull` (null) — Represents the null if no information is available.
              - `query_id` (string/int64) [maxLen=30] — Represents the query ID for the lookup field.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `hipaa_compliance` (object)
        oneOf:
            - `restricted_in_export` (boolean) **REQ** — Indicates if the field is restricted in export.
            - `restricted` (boolean) **REQ** — Indicates if the field is restricted.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `convert_mapping` (object) — Represents the convert mapping details of the field.
        - `Contacts` (object)
          oneOf:
              type: string [maxLen=100] — Represents the mapping details for Contacts field name.
            - `TypeNull` (null) — Represents the null if no information is available.
        - `Deals` (object)
          oneOf:
              type: string [maxLen=100] — Represents the mapping details for Contacts field name.
            - `TypeNull` (null) — Represents the null if no information is available.
        - `Accounts` (object)
          oneOf:
              type: string [maxLen=100] — Represents the mapping details for Contacts field name.
            - `TypeNull` (null) — Represents the null if no information is available.
        - `Invoices` (object)
          oneOf:
              type: string [maxLen=100] — Represents the mapping details for Invoices field name.
            - `TypeNull` (null) — Represents the null if no information is available.
        - `Sales_Orders` (object)
          oneOf:
              type: string [maxLen=100] — Represents the mapping details for Sales Orders field name.
            - `TypeNull` (null) — Represents the null if no information is available.
      - `address` (object)
        oneOf:
            - `type` (string) **REQ** [maxLen=25] — Represents the type of address.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `rollup_summary` (object) **REQ**
        oneOf:
            - `return_type` (string) [maxLen=50] — Represents the return type of the rollup summary.
            - `expression` (object) — Represents the expression details of the rollup summary.
              - `function_parameters` (array of object) [maxItems=100] **REQ** — Represents the list of function parameters for the rollup summary.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `criteria` (object)
                oneOf:
                    - `comparator` (string) **REQ** [maxLen=25] — Represents the comparator used in the criteria.
                    - `field` (object) **REQ** — Represents the details of the field used in the criteria.
                      - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field.
                      - `id` (string/int64) **REQ** — Id of the resource.
                    - `type` (string) **REQ** [maxLen=25] — Represents the type of the criteria.
                    - `value` (string) **REQ** [maxLen=100] — Represents the value used in the criteria.
                  - `TypeNull` (null) — Represents the null if no information is available.
              - `function` (string) **REQ** [maxLen=25] — Represents the function used in the rollup summary.
            - `based_on_module` (object) — Represents the module on which the rollup summary is based.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) **REQ** — Id of the resource.
            - `related_list` (object) — Represents the related list details for the rollup summary.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) **REQ** — Id of the resource.
            - `rollup_based_on` (string) [maxLen=50] — Indicates what the rollup is based on.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `length` (number/int32) — Represents the length of the field.
      - `column_name` (string) [maxLen=100] — Represents the column name of the field.
      - `display_field` (boolean) **REQ** — Indicates if the field is a display field.
      - `pick_list_values_sorted_lexically` (boolean) **REQ** — Indicates whether the picklist values are sorted alphabetically.
      - `sortable` (boolean) **REQ** — Indicates if the field is sortable.
      - `global_picklist` (object)
        oneOf:
            - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
            - `id` (string/int64) **REQ** — Id of the resource.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `display_format` (object)
        oneOf:
            type: string [maxLen=50] — Represents the display format applied to the field value, such as the date or date-time pattern shown in the user interface.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `history_tracking` (object)
        oneOf:
            - `related_list_name` (string) **REQ** [maxLen=100] — Represents the name of the related list for history tracking.
            - `module` (object) **REQ** — Represents the module details for history tracking.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) **REQ** — Id of the resource.
            - `duration_configured_field` (object) **REQ** — Represents the duration configured field details for history tracking.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) **REQ** — Id of the resource.
            - `duration_configuration` (string) **REQ** [maxLen=120] — Represents the duration configuration for history tracking.
            - `followed_fields` (array of object) [maxItems=100] **REQ** — Represents the list of fields being followed for history tracking.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) **REQ** — Id of the resource.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `data_type` (string) **REQ** [maxLen=25] — Represents the data type of the field.
      - `formula` (object) **REQ**
        oneOf:
            - `return_type` (string) [maxLen=50] — Represents the return type of the formula.
            - `sub_return_type` (string) [maxLen=50] — Represents the sub-type of the formula return value, such as the specific string subtype when the return type is a string.
            - `dynamic` (boolean) — Indicates if the formula is dynamic.
            - `stop_compute_conditionally` (boolean) — Indicates if the formula computation should stop conditionally.
            - `assume_default` (boolean) — Indicates if the formula should assume default values.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `additional_column` (object)
        oneOf:
            type: string [maxLen=100] — Represents the additional column of the field.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `hipaa_compliance_enabled` (boolean) — Indicates if HIPAA compliance is enabled for the field.
      - `decimal_place` (object)
        oneOf:
            type: number/int32 — Represents the number of decimal places for the field.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `mass_update` (boolean) **REQ** — Indicates if mass update is enabled for the field.
      - `multiselectlookup` (object)
        oneOf:
            - `linking_details` (object) — Represents the linking details for the multi-module lookup.
              - `module` (object) **REQ** — Represents the module details for the multi-module lookup.
                - `visibility` (number/int32) **REQ** — Represents the visibility of the module.
                - `plural_label` (string) **REQ** [maxLen=50] — Represents the plural label of the module.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `id` (string/int64) **REQ** — Id of the resource.
              - `lookup_field` (object) **REQ** — Represents the lookup field details for the multi-module lookup.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `field_label` (string) **REQ** [maxLen=100] — Represents the field label of the lookup field.
                - `id` (string/int64) **REQ** — Id of the resource.
              - `connected_lookup_field` (object) **REQ** — Represents the connected lookup field details for the multi-module lookup.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `field_label` (string) **REQ** [maxLen=100] — Represents the field label of the connected lookup field.
                - `id` (string/int64) **REQ** — Id of the resource.
            - `connected_details` (object) — Represents the connected details for the multi-module lookup.
              - `field` (object) **REQ** — Represents the field details for the multi-module lookup.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `field_label` (string) **REQ** [maxLen=100] — Represents the field label of the field.
                - `id` (string/int64) **REQ** — Id of the resource.
              - `module` (object) **REQ** — Represents the module details for the multi-module lookup.
                - `plural_label` (string) **REQ** [maxLen=50] — Represents the plural label of the module.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `id` (string/int64) **REQ** — Id of the resource.
              - `layouts` (array of object) [maxItems=100] **REQ** — Represents the list of layouts associated with the multi-module lookup.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `id` (string/int64) **REQ** — Id of the resource.
            - `related_list` (object) — Represents the related list details for the multi-module lookup.
              - `display_label` (string) **REQ** [maxLen=25] — Represents the display label of the related list.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) **REQ** — Id of the resource.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `auto_number` (object) **REQ**
        oneOf:
            - `starting_number_length` (number/int32) — Represents the length of the starting number.
            - `prefix` (object)
              oneOf:
                  type: string [maxLen=25] — Represents the prefix for the auto number.
                - `TypeNull` (null) — Represents the null if no information is available.
            - `start_number` (number/int32) — Represents the starting number for the auto number.
            - `suffix` (object)
              oneOf:
                  type: string [maxLen=25] — Represents the suffix for the auto number.
                - `TypeNull` (null) — Represents the null if no information is available.
          - `TypeNull` (null) — Represents the null if no information is available.
      - `layout_associations` (array of object) [maxItems=100] — Represents the list of layout associations for the field.
        - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the layout.
        - `name` (string) **REQ** [maxLen=25] — Represents the name of the layout.
        - `id` (string/int64) **REQ** — Id of the resource.
      - `quick_sequence_number` (string) [maxLen=10] — Represents the quick sequence number of the field.
      - `blueprint_supported` (boolean) — Indicates whether the field is supported in Blueprint configurations.
      - `textarea` (object) — Represents the textarea field details.
        - `type` (string) **REQ** [maxLen=50] — Represents the type of the textarea.
      - `sharing_properties` (object) — Represents the sharing properties of the field.
        - `scheduler_status` (string) **REQ** [maxLen=50] — Represents the scheduler status for sharing.
        - `share_permission` (string) **REQ** [maxLen=50] — Represents the share permission for the field.
        - `share_preference_enabled` (boolean) **REQ** — Indicates if share preference is enabled.
      - `multiuserlookup` (object) — Represents the multi-user lookup details of the field.
        - `linking_details` (object) **REQ** — Represents the linking details for the multi-user lookup.
          - `module` (object) **REQ** — Represents the module details for the multi-user lookup.
            - `plural_label` (string) **REQ** [maxLen=50] — Represents the plural label of the module.
            - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
            - `id` (string/int64) **REQ** — Id of the resource.
          - `lookup_field` (object) **REQ** — Represents the lookup field details for the multi-user lookup.
            - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
            - `field_label` (string) **REQ** [maxLen=100] — Represents the label of the lookup field.
            - `id` (string/int64) **REQ** — Id of the resource.
          - `connected_lookup_field` (object) **REQ** — Represents the connected lookup field details for the multi-user lookup.
            - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
            - `field_label` (string) **REQ** [maxLen=100] — Represents the label of the connected lookup field.
            - `id` (string/int64) **REQ** — Id of the resource.
        - `record_access` (boolean) **REQ** — Indicates if record access is enabled for the multi-user lookup.
      - `static_field` (boolean) — Indicates if the field is a static field

- **400**: The request is invalid. Resolution: The **module** query parameter must reference a valid module API name, and the **fieldId** path parameter must reference a valid field ID. — Schema: `BadRequest` [application/json]
    > Represents the standard error response object returned for bad requests.
    schema: `BadRequest`
    - `code` (string) **REQ** [maxLen=50, pattern=^[A-Z_]+$] — Represents the error code identifying the category or type of the bad request failure, expressed as an uppercase underscore-delimited string.
    - `details` (object) **REQ** — Represents additional details about the error, including validation information.
    - `message` (string) **REQ** [maxLen=255] — Represents a descriptive error message conveying the reason for the bad request in a readable format.
    - `status` (string) **REQ** [maxLen=50, pattern=^error$] — Indicates the outcome status of the request, always set to "error" for bad request responses.

- **500**: An unexpected error occurred on the Zoho CRM server while processing the request. Resolution: Contact Zoho CRM support if the issue persists. — Schema: `InternalServerError` [application/json]
    > Represents the internal server error response, including the error code, message, and additional details.
    schema: `InternalServerError`
    - `code` (string) **REQ** [maxLen=50, const=INTERNAL_ERROR] — Represents the error code indicating the type of server-side failure.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the server failure.
    - `details` (object) **REQ** — Represents additional details about the internal server error.
    - `status` (string) **REQ** [maxLen=50, const=error] — Represents the status of the response.

**Scopes:** ZohoCRM.settings.fields.READ
