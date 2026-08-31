# GET /settings/related_lists
**Operation:** `getRelatedLists` — Related Lists
> To retrieve the configuration of related list panels for a specific module in your Zoho CRM organization, including display metadata, available record operations, and layout-specific settings.

**Parameters:**
- `module` (query, string, required) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$]: Specify the API name of the CRM module for which to retrieve related lists. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.
- `layout_id` (query, string/int64, optional): Specify the unique identifier of the layout to scope the related lists response. Refer to the [Layouts API](https://www.zoho.com/crm/developer/docs/api/v8/layouts-meta.html) resource for valid values.
- `status` (query, string, optional) [enum=['visible', 'scheduled_for_deletion', 'user_hidden']]: Specify the visibility status to filter related lists. Possible values: **visible**, **scheduled_for_deletion**, **user_hidden**.
- `extra_properties` (query, boolean, optional) [default=False]: Set to **true** to include additional metadata properties for each related list entry beyond the default set. Possible values: **true**, **false**.
- `include_inner_details` (query, string, optional) [maxLen=255, minLen=1]: Specify a comma-separated list of detail keys to embed in each related list object. Controls which nested detail blocks are included in the response.

**Schemas:**
`PickListValue`:
  > Represents a single picklist option, including its display value, stored value, and visual configuration.
  - `display_value` (string) **REQ** [maxLen=255] — Display value shown to the user in the picklist.
  - `sequence_number` (integer/int32) **REQ** — Display sequence position of this picklist value.
  - `reference_value` (string) **REQ** [maxLen=255] — Internal reference value associated with this picklist option.
  - `colour_code` (string) **REQ** [maxLen=7, nullable] — Color code assigned to this picklist value for visual representation.
  - `actual_value` (string) **REQ** [maxLen=255] — Stored value for this picklist option.
  - `id` (string/int64) **REQ** — Unique identifier of the picklist value.
  - `type` (string) **REQ** [enum=['used', 'unused']] — Type classification of the picklist value.
`RelatedListField`:
  > Represents a field configured as a column in a related list view.
  - `sequence_number` (integer/int32) **REQ** — Display order position of the field within the related list.
  - `id` (string/int64) **REQ** — Unique identifier of the field.
  - `api_name` (string) **REQ** [maxLen=100, minLen=1, pattern=^!?[A-Za-z0-9_.]+$] — API name of the field.
  - `field_label` (string) [maxLen=100, minLen=1] — Display label of the field.
  - `ui_type` (integer/int32) — UI type identifier that determines how the field is rendered.
  - `enable_colour_code` (boolean) — Indicates whether color coding is enabled for this field. Possible values: **true**, **false**.
  - `separator` (boolean) — Indicates whether a separator is displayed after this field. Possible values: **true**, **false**.
  - `decimal_place` (integer/int32) [nullable] — Number of decimal places configured for numeric fields.
  - `lookup` (object) — Lookup configuration for the field. Empty object if the field is not a lookup. Returned when include_inner_details contains fields.lookup.
    - `display_label` (string) [maxLen=50] — Display label of the lookup related list.
    - `revalidate_filter_during_edit` (boolean) — Indicates if the filter should be revalidated during edit.
    - `api_name` (string) [maxLen=100] — API name of the lookup related list.
    - `module` (object) — Module details for the lookup field.
      - `api_name` (string) **REQ** [maxLen=100] — API name of the lookup target module.
      - `id` (string/int64) **REQ** — Unique identifier of the lookup target module.
    - `id` (string/int64) — Unique identifier of the lookup field.
    - `query_details` (object) — Query details for the lookup field.
      - `system_query_id` (string/int64) **REQ** [nullable] — System query ID for the lookup field.
  - `formula` (object) — Formula configuration for the field. Empty object if the field is not a formula field. Returned when include_inner_details contains fields.formula.
    - `return_type` (string) [maxLen=50] — The return type of the formula (e.g., text, number).
  - `rollup_summary` (object) — Rollup summary configuration for the field. Empty object if the field is not a rollup summary. Returned when include_inner_details contains fields.rollup_summary.
    - `return_type` (string) [maxLen=50] — The return type of the rollup summary (e.g., integer, number).
  - `pick_list_values` (array of object `PickListValue`) [maxItems=500] — List of picklist values for picklist-type fields in the related list.
  - `mask_details` (object) — Masking configuration for the field. Returned when include_inner_details contains fields.mask_details.
  - `refer_from_field` (object) — Reference field configuration. Returned when include_inner_details contains fields.refer_from_field.
`RelatedListLayoutSpecificProperty`:
  > Represents layout-specific configuration overrides for a related list, including per-layout sequence and visibility.
  - `sequence_number` (string/int32) **REQ** — Display sequence position of this related list in the specified layout.
  - `status` (string) **REQ** [enum=['visible', 'user_hidden', 'scheduled_for_deletion']] — Visibility status of the related list in the specified layout. Possible values: **visible**, **user_hidden**, **scheduled_for_deletion**. 
  - `layout` (object) **REQ** — Layout information for which this property override applies.
    - `name` (string) **REQ** [maxLen=100, minLen=1] — Display name of the layout.
    - `id` (string/int64) **REQ** — Unique identifier of the layout.
`RelatedListModule`:
  > Represents the module associated with a related list, including its API name and unique identifier.
  - `api_name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — API name of the module associated with the related list.
  - `id` (string/int64) **REQ** — Unique identifier of the module.
  - `plural_label` (string) [maxLen=250, minLen=1] — Plural display label of the module.
`RelatedListParentReference`:
  > Represents a reference to a parent related list that this related list depends on for contextual display.
  - `api_name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — API name of the parent related list.
  - `id` (string/int64) **REQ** — Unique identifier of the parent related list.
`RelatedListRecordOperations`:
  > Represents the set of record operations permitted for a related list.
  - `edit` (boolean) **REQ** — Indicates whether the edit operation is allowed on records in the related list. Possible values: **true**, **false**. 
  - `create` (boolean) **REQ** — Indicates whether the create operation is allowed on records in the related list. Possible values: **true**, **false**. 
  - `bulk_edit` (boolean) **REQ** — Indicates whether the bulk edit operation is allowed on records in the related list. Possible values: **true**, **false**. 
  - `delete` (boolean) **REQ** — Indicates whether the delete operation is allowed on records in the related list. Possible values: **true**, **false**. 
  - `disassociate` (boolean) **REQ** — Indicates whether records can be disassociated from the related list. Possible values: **true**, **false**. 
  - `assign` (boolean) **REQ** — Indicates whether the assign operation is allowed on records in the related list. Possible values: **true**, **false**. 

**Responses:**

- **200**: Returns the related list configuration for the specified module, including display metadata, record operation permissions, and layout-specific overrides for each related list. [application/json]
    > Response containing the related list configurations for the specified module.
    - `related_lists` (array of object `RelatedList`) [minItems=1, maxItems=1000] **REQ** — Array of related list configurations for the specified module and layout.
      oneOf:
        - `RelatedListMultiselectLookup` — Configuration metadata for a related list of type multiselectlookup.
          - `id` (string/int64) **REQ** — Specifies the unique identifier of the related list configuration.
          - `sequence_number` (string/int32) **REQ** — Specifies the display sequence position of the related list in the layout.
          - `display_label` (string) **REQ** [maxLen=50, minLen=1] — User-visible label displayed for the related list panel.
          - `api_name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — API name identifier for the related list.
          - `module` (object) **REQ** — Module information for the related list. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for details.
            oneOf:
              - `RelatedListModule` — Represents the module associated with a related list, including its API name and unique identifier.
                type: null — Represents the null state when no module is associated with this related list.
          - `name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_ \-]+$] — Internal name of the related list.
          - `action` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z0-9_]+$, nullable] — Action type supported for adding records to the related list.
          - `href` (string) **REQ** [maxLen=200, minLen=1, nullable] — Relative URL template for navigating to the related list records.
          - `type` (string) **REQ** [enum=['multiselectlookup']] — Relationship type of the related list.
          - `connectedlookupApiName` (string) [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — API name of the connected lookup field for this multiselectlookup related list.
          - `customize_sort` (boolean) **REQ** — Indicates whether the sort configuration for this related list can be customized. Possible values: **true**, **false**. 
          - `customize_fields` (boolean) **REQ** — Indicates whether the field selection for this related list can be customized. Possible values: **true**, **false**. 
          - `customize_display_label` (boolean) **REQ** — Indicates whether the display label of this related list can be customized. Possible values: **true**, **false**. 
          - `status` (string) **REQ** [enum=['visible', 'user_hidden', 'scheduled_for_deletion']] — Visibility status of the related list. Possible values: **visible**, **user_hidden**, **scheduled_for_deletion**. 
          - `visibility` (integer/int32) [min=0] — Numeric visibility flag for the related list.
          - `personality_name` (string) [maxLen=100, minLen=1] — Internal personality identifier associated with this related list configuration.
          - `record_operations` (object `RelatedListRecordOperations`) — Represents the set of record operations permitted for a related list.
          - `connectedmodule` (string) [maxLen=250, minLen=1, pattern=^[A-Za-z0-9_]+$, nullable] — API name of the connected module for this multiselectlookup relationship.
          - `linkingmodule` (string) [maxLen=250, minLen=1, pattern=^[A-Za-z0-9_]+$, nullable] — API name of the linking module that connects the two entities in the multiselectlookup relationship.
          - `parent_related_lists` (array of object `RelatedListParentReference`) [minItems=0, maxItems=4, nullable] — List of parent related list references that this related list depends on for contextual display.
          - `_layout_specific_properties` (array of object `RelatedListLayoutSpecificProperty`) [minItems=0, maxItems=25, nullable] — Layout-specific configuration overrides for this related list, such as per-layout sequence and visibility.
          - `field_enabled` (boolean) — Indicates whether the multiselectlookup field is enabled. Possible values: **true**, **false**.
          - `multiselectlookup` (object `MultiselectLookupConfig`) — Represents the multiselectlookup configuration for a related list, including the lookup field, linking module, and connected module details.
            schema: `MultiselectLookupConfig`
            - `field` (object) **REQ** — Lookup field configuration for the multiselectlookup relationship.
              - `api_name` (string) **REQ** [maxLen=100] — API name of the lookup field.
              - `field_label` (string) **REQ** [maxLen=100] — Display label of the lookup field.
              - `id` (string/int64) **REQ** — Unique identifier of the lookup field.
            - `linking_details` (object) **REQ** — Details of the linking module that connects the two entities in the multiselectlookup.
              - `visibility` (integer/int32) **REQ** — Visibility flag for the linking module relationship.
              - `module` (object) **REQ** — Linking module information for the multiselectlookup relationship.
                - `plural_label` (string) **REQ** [maxLen=100] — Plural display label of the linking module.
                - `api_name` (string) **REQ** [maxLen=100] — API name of the linking module.
                - `id` (string/int64) **REQ** — Unique identifier of the linking module.
              - `lookup_field` (object) **REQ** — Lookup field in the linking module that references the source module.
                - `api_name` (string) **REQ** [maxLen=100] — API name of the lookup field in the linking module that references the source module.
                - `id` (string/int64) **REQ** — Unique identifier of the lookup field in the linking module.
              - `connected_lookup_field` (object) **REQ** — Lookup field in the linking module that references the connected module.
                - `api_name` (string) **REQ** [maxLen=100] — API name of the connected lookup field in the linking module.
                - `id` (string/int64) **REQ** — Unique identifier of the connected lookup field in the linking module.
            - `connected_details` (object) **REQ** — Details of the connected module and field in the multiselectlookup relationship.
              - `field` (object) **REQ** — Field configuration in the connected module for the multiselectlookup relationship.
                - `api_name` (string) **REQ** [maxLen=100] — API name of the field in the connected module.
                - `field_label` (string) **REQ** [maxLen=100] — Display label of the field in the connected module.
                - `id` (string/int64) **REQ** — Unique identifier of the field in the connected module.
              - `module` (object) **REQ** — Connected module information in the multiselectlookup relationship.
                - `plural_label` (string) **REQ** [maxLen=100] — Plural display label of the connected module.
                - `api_name` (string) **REQ** [maxLen=100] — API name of the connected module.
                - `id` (string/int64) **REQ** — Unique identifier of the connected module.
              - `related_list` (object) **REQ** — Related list information in the connected module.
                - `display_label` (string) **REQ** [maxLen=50] — Display label of the related list in the connected module.
                - `api_name` (string) **REQ** [maxLen=100] — API name of the related list in the connected module.
                - `id` (string/int64) **REQ** — Unique identifier of the related list in the connected module.
            - `field_enabled` (boolean) **REQ** — Indicates whether the multiselectlookup field is enabled. Possible values: **true**, **false**. 
          - `sort_by` (object) — Field by which records in this related list are sorted.
            oneOf:
              - `RelatedListMultiselectSortField` — Field metadata used for sorting a multiselectlookup related list. The api_name follows the format ModuleName.FieldApiName (e.g., "Leads.Company") where the left part is the connected module api_name and the right part is the field api_name.
                - `id` (string/int64) **REQ** — Unique identifier of the sort field.
                - `api_name` (string) **REQ** [maxLen=200, minLen=1, pattern=^[A-Za-z0-9_]+(\.[A-Za-z0-9_]+)?$] — API name of the field used for sorting. For multiselectlookup related lists, this is in the format ModuleName.FieldApiName (e.g., "Leads.Company").
                type: null — Represents the null state when no sort field is configured for this related list.
          - `sort_order` (string) [enum=['asc', 'desc', None], nullable] — Sort direction for records in this related list. Possible values: **asc**, **desc**.
          - `fields` (array of object `RelatedListField`) [minItems=0, maxItems=50, nullable] — List of fields configured as columns in the related list view.
        - `RelatedListNonMultiselectLookup` — Configuration metadata for a standard (non-multiselectlookup) related list.
          - `id` (string/int64) **REQ** — Unique identifier of the related list configuration.
          - `sequence_number` (string/int32) **REQ** — Display sequence position of the related list in the layout.
          - `display_label` (string) **REQ** [maxLen=50, minLen=1] — User-visible label displayed for the related list panel.
          - `api_name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — API name identifier for the related list.
          - `module` (object) **REQ** — Module information for the related list. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for details.
            oneOf:
              - `RelatedListModule` — Represents the module associated with a related list, including its API name and unique identifier.
                type: null — Represents the null state when no module is associated with this related list.
          - `name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_ \-]+$] — Internal name of the related list.
          - `action` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z0-9_]+$, nullable] — Action type supported for adding records to the related list.
          - `href` (string) **REQ** [maxLen=200, minLen=1, nullable] — Relative URL template for navigating to the related list records.
          - `type` (string) **REQ** [enum=[8 values]] — Relationship type of the related list.
          - `connectedlookupApiName` (string) [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — API name of the connected lookup field for this related list.
          - `customize_sort` (boolean) **REQ** — Indicates whether the sort configuration for this related list can be customized. Possible values: **true**, **false**. 
          - `customize_fields` (boolean) **REQ** — Indicates whether the field selection for this related list can be customized. Possible values: **true**, **false**. 
          - `customize_display_label` (boolean) **REQ** — Indicates whether the display label of this related list can be customized. Possible values: **true**, **false**. 
          - `status` (string) **REQ** [enum=['visible', 'user_hidden', 'scheduled_for_deletion']] — Visibility status of the related list. Possible values: **visible**, **user_hidden**, **scheduled_for_deletion**. 
          - `visibility` (integer/int32) [min=0] — Numeric visibility flag for the related list.
          - `personality_name` (string) [maxLen=100, minLen=1] — Internal personality identifier associated with this related list configuration.
          - `record_operations` (object `RelatedListRecordOperations`) — Represents the set of record operations permitted for a related list.
          - `connectedmodule` (string) [maxLen=250, minLen=1, pattern=^[A-Za-z0-9_]+$, nullable] — API name of the connected module for this lookup relationship.
          - `linkingmodule` (string) [maxLen=250, minLen=1, pattern=^[A-Za-z0-9_]+$, nullable] — API name of the linking module for this relationship.
          - `parent_related_lists` (array of object `RelatedListParentReference`) [minItems=0, maxItems=4, nullable] — List of parent related list references that this related list depends on.
          - `_layout_specific_properties` (array of object `RelatedListLayoutSpecificProperty`) [minItems=0, maxItems=25, nullable] — Layout-specific configuration overrides for this related list.
          - `sort_by` (object) — Field used for sorting the related list (null if no sorting configured).
            oneOf:
              - `RelatedListSortField` — Represents the field used to sort records in a related list.
                - `id` (string/int64) **REQ** — Unique identifier of the field used for sorting.
                - `api_name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — API name of the field used for sorting.
                type: null — No sorting is applied.
          - `sort_order` (string) [enum=['asc', 'desc', None], nullable] — Sort direction applied to the related list (null if no sorting configured).
          - `fields` (array of object `RelatedListField`) [minItems=0, maxItems=50, nullable] — Fields displayed in the related list (null if not configured).

- **204**: No related lists matched the requested module, layout, or visibility filter.

- **400**: The request contains invalid or missing parameters.
**Resolution:** The **module** parameter must be a valid CRM module API name. The **status** parameter must be one of the supported values. [application/json]
    > Validation error response for the getRelatedLists operation. The error code and details identify the specific failure.
    oneOf:
      - `InvalidDataError` — Error response returned when a field or parameter value fails validation in a related list operation.
        - `status` (string) **REQ** [enum=['error']] — Response status indicating an error occurred. Possible values: **error**. 
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid data was provided. Possible values: **INVALID_DATA**. 
        - `message` (string) **REQ** [enum=[22 values]] — Error message describing the invalid data.
        - `details` (object) **REQ** — Contextual details about the invalid data. The structure varies by error subtype: field-level errors include **api_name** and **json_path**; parameter errors include **param_name**; resource path errors include **resource_path_index**. 
          oneOf:
            - `InvalidDataFieldDetails` — Details for an INVALID_DATA error identifying the specific field and its location in the request.
              - `api_name` (string) **REQ** [maxLen=100] — API name of the field that caused the validation error.
              - `json_path` (string) **REQ** [maxLen=500] — JSON path to the specific field that failed validation.
            - `InvalidDataTypeDetails` — Details for an INVALID_DATA error caused by a data type mismatch, including the expected type.
              - `api_name` (string) **REQ** [maxLen=100] — API name of the field with the data type mismatch.
              - `json_path` (string) **REQ** [maxLen=500] — JSON path to the field with the data type mismatch.
              - `expected_data_type` (string) **REQ** [enum=['integer', 'text', 'boolean', 'jsonarray', 'jsonobject']] — Expected data type for the field. Possible values: **integer**, **text**, **Boolean**, **jsonarray**, **jsonobject**. 
            - `InvalidDataLengthDetails` — Details for an INVALID_DATA error caused by a field value exceeding the maximum allowed length.
              - `api_name` (string) **REQ** [maxLen=100] — API name of the field whose value exceeded the maximum length.
              - `json_path` (string) **REQ** [maxLen=500] — JSON path to the field whose value exceeded the maximum length.
              - `maximum_length` (integer/int32) **REQ** — Maximum allowed length for the field.
            - `InvalidDataParameterDetails` — Details for an INVALID_DATA error on a query or body parameter, identifying the parameter name and supported values.
              - `param_name` (string) **REQ** [enum=[7 values]] — Name of the parameter that failed validation. Possible values: **module**, **status**, **layout_id**, **type**, **extra_properties**, **include_inner_details**, **feature_name**. 
              - `supported_values` (array of string) [maxItems=100] — List of supported values for the parameter.
                items: [maxLen=255]
            - `InvalidDataResourcePathDetails` — Details for an INVALID_DATA error caused by an invalid resource path identifier in the URL.
              - `resource_path_index` (integer/int32) **REQ** — Index of the resource path segment that contains invalid data.
            - `InvalidDataFieldWithSupportedValuesDetails` — Details for an INVALID_DATA error on a constrained field, listing the supported values.
              - `api_name` (string) **REQ** [maxLen=100] — API name of the field with invalid value.
              - `json_path` (string) **REQ** [maxLen=500] — JSON path to the field with invalid value.
              - `supported_values` (object) **REQ** — Supported values for the field, returned either as an array of strings or as a Boolean validation indicator.
                oneOf:
                    type: array of string [maxItems=100]
                      type: string [maxLen=255] — Represents a single supported value for the constrained field.
                      items: [maxLen=255]
                    type: string [maxLen=500] — Represents the supported values as a Boolean validation indicator.
            - `InvalidDataFieldIndexDetails` — Details for an INVALID_DATA error at a specific array index within a field.
              - `api_name` (string) **REQ** [maxLen=100] — API name of the field at the error index.
              - `json_path` (string) **REQ** [maxLen=500] — JSON path to the field at the error index.
              - `index` (integer/int32) **REQ** — Array index at which the validation error occurred.
      - `InvalidModuleError` — Error response returned when the specified module is invalid or not recognized in the CRM organization.
        - `status` (string) **REQ** [enum=['error']] — Response status indicating an error occurred. Possible values: **error**. 
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating the module is invalid. Possible values: **INVALID_MODULE**. 
        - `message` (string) **REQ** [enum=[2 values]] — Error message describing the invalid module.
        - `details` (object) **REQ** — Additional details about the invalid module error.
          - `param_name` (string) **REQ** [enum=['module']] — Name of the parameter that referenced the invalid module. Possible values: **module**. 
      - `MissingModuleParameterError` — Error response returned when the required **module** query parameter is absent from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code indicating the required **module** parameter is missing. Possible values: **REQUIRED_PARAM_MISSING**. 
        - `details` (object) **REQ** — Validation details identifying the missing parameter.
          - `param_name` (string) **REQ** [enum=['module', 'type']] — Name of the missing required parameter. Possible values: **module**. 
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Error message indicating a required parameter is missing. Possible values: **One of the expected parameter is missing**. 
        - `status` (string) **REQ** [enum=['error']] — Response status indicating an error occurred. Possible values: **error**. 
      - `NotSupportedError` — Error response returned when the specified module exists but is not supported by this API.
        - `status` (string) **REQ** [enum=['error']] — Response status indicating an error occurred. Possible values: **error**. 
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code indicating the module is not supported by this API. Possible values: **NOT_SUPPORTED**. 
        - `message` (string) **REQ** [enum=[2 values]] — Error message describing the unsupported module.
        - `details` (object) **REQ** — Additional details about the unsupported module.
          - `param_name` (string) [enum=['module']] — Name of the parameter referencing the unsupported module.

- **401**: The access token is missing, expired, or does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this API. [application/json]
    > Error response returned when authentication fails. Contains the error code, message, and status.
    oneOf:
      - `AuthenticationFailureError` — Error response returned when the OAuth2 access token is missing, expired, or invalid.
        - `code` (string) **REQ** [enum=['INVALID_TOKEN']] — Error code indicating the type of authentication failure. Possible values: **INVALID_TOKEN**. 
        - `details` (object) **REQ** — Additional details about the authentication error.
        - `message` (string) **REQ** [enum=['invalid oauth token']] — Error message describing the authentication failure. Possible values: **invalid OAuth token**. 
        - `status` (string) **REQ** [enum=['error']] — Response status indicating an error occurred. Possible values: **error**. 
      - `OAuthScopeMismatchError` — Error response returned when the access token does not include the required OAuth scope for this API.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code indicating the OAuth scope does not match the required scope. Possible values: **OAUTH_SCOPE_MISMATCH**. 
        - `details` (object) **REQ** — Additional details about the scope mismatch error.
        - `message` (string) **REQ** [enum=['invalid oauth scope to access this URL']] — Error message describing the scope mismatch. Possible values: **invalid OAuth scope to access this URL**. 
        - `status` (string) **REQ** [enum=['error']] — Response status indicating an error occurred. Possible values: **error**. 

**Scopes:** ZohoCRM.settings.related_lists.READ, ZohoCRM.settings.related_lists.ALL, ZohoCRM.settings.ALL
