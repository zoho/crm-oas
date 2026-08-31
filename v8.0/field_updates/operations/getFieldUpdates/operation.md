# GET /settings/automation/field_updates
**Operation:** `getFieldUpdates` — Get Field Updates
> Retrieves a paginated list of field update actions. OPTIONAL FILTERS: module (string — filter by module API name), related_module (string — filter by related module API name), feature_type ('workflow'), sort_by, sort_order, page, per_page. Use the Fields metadata API to get field IDs and API names, and the Modules metadata API to get module API names and IDs. Use the [Get Field Updates API](field_updates.yaml#$.paths./settings/automation/field_updates.get) before associating them with workflow rules via the associate action.

**Parameters:**
- `filter` (query, string, optional) [maxLen=10000]: Advanced filter criteria (JSON-encoded string). Supported only: **field.api_name='name'** and **comparator='contains'**. The value field is dynamic.
- `module` (query, string, optional) [maxLen=255]: Filter by CRM module API name. Use module API names from the Zoho CRM Modules API (for example: Leads, Contacts, Deals). Use the [Modules metadata API](modules.yaml#$.paths./settings/modules/.get) to get module API names and IDs.
- `related_module` (query, string, optional) [maxLen=255]: Filter by related module API name. Use related module API names from the Zoho CRM Modules API (for example: Notes). Use the [Modules metadata API](modules.yaml#$.paths./settings/modules.get) to get module API names.
- `feature_type` (query, string, optional) [enum=[12 values]]: Filter field updates by automation feature type.
- `sort_order` (query, string, optional) [enum=['desc', 'asc']]: Sort order for the results based on sort_by. Allowed values: desc, asc.
- `sort_by` (query, string, optional) [enum=['modified_time']] {style=form, explode=True}: Sort field for list response. Default sorting is by created_time; currently supported explicit value is modified_time.
- `include_inner_details` (query, string, optional) [enum=[5 values]] {style=form, explode=True}: Include optional field metadata in the response. `field_label`: UI label, `enable_colour_code`: picklist color-coding flag, `pick_list_values.colour_code`: HEX color per picklist option, `data_type`: field data type, `display_value`: UI-friendly rendered value.
- `page` (query, integer/int32, optional) [min=1, default=1]: Page number (1-based).
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Indicates records per page. Maximum 200.

**Schemas:**
`FieldDetails`:
  > The target CRM field that this action updates.
  - `ui_type` (integer/int32) — Internal UI type code for the field. Present only in response; not required in requests.
  - `id` (string) **REQ** [maxLen=255] — Unique identifier of the CRM field. Mandatory in create/update payloads.
  - `api_name` (string) **REQ** [maxLen=255] — API name of the CRM field (e.g., Deal_Name, Pipeline, Owner, Layout, Multi_Select_1).
  - `field_label` (string) [maxLen=255] — Display label of the CRM field, as shown in the CRM UI.
  - `data_type` (string) [maxLen=255] — Data type of the CRM field, for example text, picklist, or lookup.

**Responses:**

- **200**: Successful response for listing field update actions. Includes configured field update definitions and pagination metadata. — Schema: `FieldUpdatesListResponse` [application/json]
    > Successful response for listing field update actions. Contains an array of field update definitions configured in the org along with pagination metadata.
    schema: `FieldUpdatesListResponse`
    - `field_updates` (array of object `FieldUpdateConfigurationForList`) [maxItems=200] — List of field update actions configured in the org.
      schema: `FieldUpdateConfigurationForList`
      - `created_time` (string) [maxLen=255] — Date-time when this field update action was created.
      - `update_type` (string) [maxLen=255, enum=['overwrite', 'append', None], nullable] — Specifies how the field value should be applied when the target field supports multiple update strategies (e.g., multi-select picklist, Owner). Null when the field type does not support multiple update strategies (e.g., text, single picklist).
      - `lock_status` (object `LockStatus`) — Indicates whether this field update action is locked for edit/delete.
        schema: `LockStatus`
        - `locked` (boolean) — True when the action is locked and cannot be edited or deleted.
      - `apply_assignment_threshold` (boolean) — Whether assignment-threshold rules (record count limits per user) should be enforced when updating the field. Only applicable when the target field is an Owner field and the org has assignment thresholds configured. When true, the system checks whether the new owner has reached their record limit before applying the update. Ignored for non-Owner fields.
      - `editable` (boolean) — Whether the current user can edit this field update action.
      - `module` (object `ModuleDetails`) **REQ** — Primary CRM module on which this field update action is configured.
        schema: `ModuleDetails`
        - `singular_label` (string) [maxLen=255] — Singular display label of the module (e.g., Deal, Lead). Present only in responses.
        - `moduleName` (string) [maxLen=255] — Internal module name. Present only in responses.
        - `id` (string) [maxLen=255] — Unique identifier of the CRM module corresponding to api_name.
        - `plural_label` (string) [maxLen=255] — Plural display label of the module (e.g., Deals, Leads). Present only in responses.
        - `api_name` (string) **REQ** [maxLen=255] — CRM module API name used in automation configuration (e.g., Leads, Contacts, Deals).
      - `related_module` (object `RelatedModuleDetails`) — Related module context when the automation is configured on related records; null when not applicable.
        schema: `RelatedModuleDetails`
        - `api_name` (string) [maxLen=255] — CRM related-module API name used in automation configuration (e.g., Notes).
        - `id` (string) [maxLen=255] — Unique identifier of the related CRM module corresponding to api_name.
      - `deletable` (boolean) — Represents whether the current user can delete this field update action.
      - `source` (string) [maxLen=255] — Source application that created or manages this action (e.g., crm).
      - `type` (string) **REQ** [maxLen=255, enum=['static', 'merge_field']] — Type returned by the API for this field update. Create/update accepts only static; GET responses can include merge_field for pre-existing actions.
      - `created_by` (object `CreatedBy`) — User who created this field update action.
        schema: `CreatedBy`
        - `name` (string) [maxLen=255] — Display name of the user who created the resource.
        - `id` (string) [maxLen=255] — Unique identifier of the user who created the resource.
      - `notify` (boolean) — Whether to send an email notification to the new record owner when the Owner field is updated via this action. Only applicable when the target field is an Owner field. When true, the newly assigned owner receives an email informing them of the ownership change. Ignored for non-Owner fields.
      - `feature_type` (string) [maxLen=255, enum=[8 values]] — Automation feature where this field update action is used.
      - `modified_time` (string) [maxLen=255] — Date-time when this field update action was last modified.
      - `field` (object `FieldDetails`) **REQ** — The target CRM field that this action updates.
      - `dependent_fields` (array of object `DependentFieldsNested`) [maxItems=10, nullable] — Dependent fields that must be set alongside the target field when dependency rules apply. Includes patterns such as Pipeline -> Stage and Layout -> Pipeline -> Stage (nested). Nested dependencies can be represented through dependent_fields within each item. Null when the target field has no dependency rules configured.
        schema: `DependentFieldsNested`
        - `field` (object `FieldDetails`) **REQ** — Specify the API name and ID of the dependent field to be updated.
        - `dependent_fields` (array of object `DependentFieldsNestedLevel2`) [maxItems=10] — Nested dependent fields that must be set when the current dependent field itself has further dependencies.
          schema: `DependentFieldsNestedLevel2`
          - `field` (object `FieldDetails`) **REQ** — Specify the API name and ID of the dependent field to be updated.
          - `dependent_fields` (array of object `DependentFieldsNestedLevel3`) [maxItems=10] — Third-level dependent fields for deeper dependency chains.
            schema: `DependentFieldsNestedLevel3`
            - `field` (object `FieldDetails`) **REQ** — Specify the API name and ID of the dependent field to be updated.
            - `value` (string) **REQ** [maxLen=255] — Contains value of the dependent field.
          - `value` (string) **REQ** [maxLen=255] — Contains value of the dependent field.
        - `value` (string) **REQ** [maxLen=255] — Contains value of the dependent field.
      - `associated` (boolean) — Whether this action is currently linked to any automation rule, approval process, or blueprint.
      - `related_records` (array of object `RelatedRecordModule`) [maxItems=5, nullable] — List of related modules whose record ownership should also be transferred along with the parent record when the Owner field is updated. Only applicable when the target field is an Owner field. Common activity modules (Tasks, Calls, Events) are available for all modules. Additional related modules are available depending on the parent module: Accounts can also include Contacts and Deals; Contacts can also include Deals. Null when the target field is not an Owner field or when no related modules are selected for ownership transfer.
        schema: `RelatedRecordModule`
        - `api_name` (string) **REQ** [maxLen=255, enum=['Events', 'Calls', 'Tasks', 'Contacts', 'Deals']] — API name of the related module. Events, Calls, Tasks - open activity records, available for all modules. Contacts - available only when the parent module is Accounts. Deals - available when the parent module is Accounts or Contacts.
        - `id` (string) [maxLen=255] — Unique identifier of the related module. This is the module ID corresponding to the api_name.
      - `name` (string) **REQ** [maxLen=255] — Display name of the field update action.
      - `modified_by` (object `ModifiedBy`) — User who last modified this field update action.
        schema: `ModifiedBy`
        - `name` (string) [maxLen=255] — Display name of the user who last modified the resource.
        - `id` (string) [maxLen=255] — Unique identifier of the user who last modified the resource.
      - `id` (string) [maxLen=20] — Unique identifier of the field update action.
      - `value` (object) **REQ** — The value configured for the field update. The shape depends on the target field type.
        oneOf:
            type: string [maxLen=255] — A plain text value. Used when the target field is a single-value field such as a text field (e.g., Deal_Name), picklist (e.g., Pipeline, Stage), number, date, or similar scalar field types. Example: "PostTest", "Qualification".
            type: array of string [maxItems=25]
              type: string [maxLen=255] — One selected option value for the multi-select field.
              items: [maxLen=255]
            additionalProperties: any
            type: boolean — A boolean value. Used when the target field is a checkbox or boolean-type field. true enables/checks the field, false disables/unchecks it.
            type: number — A numeric value. Used when the target field is a number, currency, decimal, or percentage field type. Example: 100, 25.5.
            type: null — A null value. Used to clear/empty the target field  - equivalent to choosing 'empty value' in the field update configuration.
      - `parent_module` (object) — Parent module context when the field update is configured on a child module. Null when the field update is on a top-level module.
        - `api_name` (string) [maxLen=255] — API name of the parent CRM module.
        - `id` (string) [maxLen=20] — Unique identifier of the parent CRM module.
    - `info` (object `PaginationInfo`) — Pagination metadata for list responses. Use more_records to determine if additional pages are available.
      schema: `PaginationInfo`
      - `per_page` (integer/int32) — Maximum number of records returned per page (default 200).
      - `count` (integer/int32) — Number of records returned in the current page.
      - `page` (integer/int32) — Current page number (starts at 1).
      - `more_records` (boolean) — True when additional records are available on subsequent pages.

- **204**: No content

- **400**: Returned when a query parameter value is invalid. This includes invalid module names, unsupported feature types, and invalid sort parameters. [application/json]
    oneOf:
      - `InvalidDataParamError` — Returned when a query parameter contains an invalid value. Applies to feature_type, sort_by, sort_order, and similar parameters.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the data provided is invalid
        - `details` (object) **REQ** — Details identifying which parameter caused the error
          - `param_name` (string) [maxLen=255] — The query parameter that has an invalid value
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidModuleError` — Returned when the module query parameter contains a module name that does not exist in the CRM organization.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating the module is invalid
        - `details` (object) **REQ** — Details identifying which parameter caused the error
          - `param_name` (string) [maxLen=255] — The query parameter that has an invalid value
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Indicates that the user does not have the necessary permissions to read all the field update details. — Schema: `FeatureNoPermissionError` [application/json]
    > Indicates that the user does not have the necessary permissions to create a field update action.
    schema: `FeatureNoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code.
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] — Permission that the current user is missing
        items: [maxLen=255]
      - `api_name` (string) [maxLen=255] — API name of the field associated with the permission error.
      - `json_path` (string) [maxLen=1000] — JSON path to the field in the request body
    - `message` (string) **REQ** [enum=[3 values]] — Represents the error message.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status

**Scopes:** ZohoCRM.settings.automation_actions.READ
