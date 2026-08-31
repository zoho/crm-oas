# POST /settings/automation/field_updates
**Operation:** `createFieldUpdates` — Create Field Update
> Creates a field update action that assigns a static value to a field, triggered by a workflow rule. For single-value fields, use a string for value. For multi-select and multi-user field types, use an array for value (for example, ['Call', 'Advertisement']). update_type (mandatory for multi-select and multi-user fields) specifies how to update the field and is supported only for multi-select fields: overwrite replaces existing values, append adds to existing values. dependent_fields specifies fields affected when the target field changes — primarily used for picklist dependencies, where one field's value controls another's valid options. For example, updating Country to India restricts the dependent State field to Indian states.


**Schemas:**
`FieldDetails`:
  > Target field to be updated. Provide both field.id and field.api_name. If both are present but inconsistent, ambiguity or invalid-data errors can be returned.
  - `ui_type` (integer/int32) — Internal UI type code for the field. Present only in response; not required in requests.
  - `id` (string) **REQ** [maxLen=255] — Unique identifier of the CRM field. Mandatory in create/update payloads.
  - `api_name` (string) **REQ** [maxLen=255] — API name of the CRM field (e.g., Deal_Name, Pipeline, Owner, Layout, Multi_Select_1).
  - `field_label` (string) [maxLen=255] — Display label of the CRM field, as shown in the CRM UI.
  - `data_type` (string) [maxLen=255] — Data type of the CRM field, for example text, picklist, or lookup.

**Request Body** — application/json `CreateFieldUpdateRequest`
> Request body containing the field update configuration to create. Only one field update can be created per request. For dependency-driven fields, include dependent_fields as required: Pipeline -> Stage, Layout -> Pipeline -> Stage (nested), Owner -> user object from Users API.
  > The request body wrapper for creating or updating a field update action. Must contain a field_updates array with exactly one entry.
  - `field_updates` (array of object `FieldUpdateConfigurationForCreate`) [maxItems=1] **REQ** — Array containing one field update configuration object. Exactly one item is allowed per request.
    schema: `FieldUpdateConfigurationForCreate`
    - `name` (string) **REQ** [maxLen=255] — Name of the field update action. Must be unique within the org. This label is displayed in the automation rule configuration UI.
    - `module` (object `ModuleDetails`) **REQ** — The CRM module where this field update should be applied. Specify using the module's unique ID and/or API name (e.g., Deals, Leads, Contacts).
      schema: `ModuleDetails`
      - `singular_label` (string) [maxLen=255] — Singular display label of the module (e.g., Deal, Lead). Present only in responses.
      - `moduleName` (string) [maxLen=255] — Internal module name. Present only in responses.
      - `id` (string) [maxLen=255] — Unique identifier of the CRM module corresponding to api_name.
      - `plural_label` (string) [maxLen=255] — Plural display label of the module (e.g., Deals, Leads). Present only in responses.
      - `api_name` (string) **REQ** [maxLen=255] — CRM module API name used in automation configuration (e.g., Leads, Contacts, Deals).
    - `field` (object `FieldDetails`) **REQ** — Target field to be updated. Provide both field.id and field.api_name. If both are present but inconsistent, ambiguity or invalid-data errors can be returned.
    - `value` (object) **REQ** — The value to assign to the target field when this action is triggered. The type must match the target field's data type  - a mismatch returns DEPENDENT_MISMATCH. Pipeline expects a string value from Pipelines metadata; Layout expects a layout object from Layouts metadata; Owner expects a user object from Users API.
      oneOf:
        - `FieldUpdateStringValue` (string) [maxLen=255] — A string value used for text, single-picklist, date, or Pipeline fields. Picklist and Pipeline values are validated against the field's configured options.
        - `FieldUpdateArrayValue` — An array of string values used for multi-select picklist fields, where each element represents one selected option.
          type: array of string [maxItems=25]
            type: string [maxLen=255] — Individual option value for the multi-select field.
            items: [maxLen=255]
        - `FieldUpdateOwnerValue` — An object value used for Owner or Layout fields, identified by id (a user ID for Owner fields or a layout ID for Layout fields), with an optional name for display.
          - `id` (string) **REQ** [maxLen=255] — Unique identifier of the user to assign as the new owner.
          - `name` (string) [maxLen=255] — Optional display name for readability.
        - `FieldUpdateBooleanValue` (boolean) — A boolean value used for checkbox fields, where true marks the field as checked and false marks it as unchecked.
        - `FieldUpdateNumberValue` (number) — A numeric value used for number, currency, decimal, or percentage fields.
        - `FieldUpdateNullValue` (null) — Null value  - clears/empties the target field, removing any previously set value.
    - `type` (string) **REQ** [maxLen=255, enum=['static']] — Create/update mapping type. Only static is accepted for create/update payloads.
    - `feature_type` (string) [maxLen=255, enum=[8 values]] — The automation feature this field update is associated with. Defaults to 'workflow' if omitted. All enum values are supported for creation via API.
    - `notify` (boolean) [default=False] — Whether to send an email notification to the new owner when the Owner field is updated. Required when the target field is Owner (omitting returns DEPENDENT_FIELD_MISSING). Must not be sent when the target field is not Owner (returns NOT_ALLOWED).
    - `update_type` (string) [maxLen=255, enum=['overwrite', 'append', None], nullable] — Strategy for applying the value. Required for multi-select fields: 'overwrite' replaces all existing values, 'append' adds to them. Omit or pass null for single-value fields.
    - `apply_assignment_threshold` (boolean) [default=False] — Whether to enforce assignment-threshold rules when updating the Owner field. This key is applicable only for Owner updates, and is required only when active owner-assignment thresholds exist for the module. If thresholds are not configured, sending this key can be rejected as not allowed.
    - `dependent_fields` (array of object `DependentFieldsNested`) [maxItems=1, nullable] — Dependent fields that must be set alongside the target field. Required for dependent picklist relationships. Common chains: Pipeline -> Stage, Layout -> Pipeline, and Layout -> Pipeline -> Stage (nested via dependent_fields inside the Pipeline node).
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
    - `related_records` (array of object `RelatedRecordModule`) [maxItems=5, nullable] — Related modules whose open record ownership should also be transferred when the Owner field is updated. Common activity modules (Tasks, Calls, Events) are available for all modules. Additional modules depend on the parent module: Accounts can also include Contacts and Deals; Contacts can also include Deals. Required when the target field is Owner (omitting returns DEPENDENT_FIELD_MISSING). Must not be sent when the target field is not Owner (returns NOT_ALLOWED). Pass null to skip ownership transfer on related records.
      schema: `RelatedRecordModule`
      - `api_name` (string) **REQ** [maxLen=255, enum=['Events', 'Calls', 'Tasks', 'Contacts', 'Deals']] — API name of the related module. Events, Calls, Tasks - open activity records, available for all modules. Contacts - available only when the parent module is Accounts. Deals - available when the parent module is Accounts or Contacts.
      - `id` (string) [maxLen=255] — Unique identifier of the related module. This is the module ID corresponding to the api_name.
    - `related_module` (object `RelatedModuleDetails`) — Related module context when the field update is configured on a related module's records (e.g., updating a field on Contacts related to Accounts). Pass null or omit when not applicable.
      schema: `RelatedModuleDetails`
      - `api_name` (string) [maxLen=255] — CRM related-module API name used in automation configuration (e.g., Notes).
      - `id` (string) [maxLen=255] — Unique identifier of the related CRM module corresponding to api_name.

**Responses:**

- **201**: Field update action created successfully. — Schema: `PostfieldupdatesResponse201` [application/json]
    > Success response returned when a field update action is created. Contains an array with a single result object indicating the outcome and the server-generated ID of the new field update.
    schema: `PostfieldupdatesResponse201`
    - `field_updates` (array of object `FieldUpdateActionResult`) [maxItems=1] — Array containing the result of the create operation. Always contains exactly one item since only one field update can be created per request.
      schema: `FieldUpdateActionResult`
      - `code` (string) **REQ** [maxLen=255, enum=['SUCCESS', 'NOT_ALLOWED', 'INVALID_DATA']] — Operation result code. 'SUCCESS' for successful operations. In bulk operations (DELETE 207), individual items may return error codes like 'NOT_ALLOWED' or 'INVALID_DATA'.
      - `details` (object `ActionResultDetails`) **REQ** — Details object within an action result, containing the server-generated unique identifier of the created, updated, or deleted field update action.
        schema: `ActionResultDetails`
        - `id` (string) **REQ** [maxLen=255] — Unique identifier of the field update action that was created, updated, or deleted.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the operation outcome.
      - `status` (string) **REQ** [maxLen=255, enum=['success', 'error']] — Overall status of the operation. 'success' for successful operations, 'error' for failed individual items in bulk operations.

- **400**: Validation error. Returned when one or more request fields are missing, invalid, mismatched with dependencies, or not allowed for the selected field update configuration. [application/json]
    oneOf:
      - `InvalidDataGenericError` — Returned when the field_updates value has an invalid data type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) [maxLen=255] — API name of the field that caused the error.
          - `json_path` (string) [maxLen=1000] — JSON path to the field in the request body.
        - `message` (string) **REQ** [enum=['invalid data', 'the fieldId given seems to be invalid']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Error status
        - `field_updates` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `ModuleIdApiNameAmbiguityError` — Represents module ID and API name do not match the same module.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Module references whose id and api_name values do not match, causing the ambiguity.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the conflicting module reference.
                  - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the conflicting module reference.
              - `message` (string) **REQ** [enum=['The given moduleid seems to be invalid']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `FieldApiAmbiguityError` — Returned when the provided field ID and field API name do not refer to the same CRM field.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Field references whose id and api_name values do not match, causing the ambiguity.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the conflicting field reference.
                  - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the conflicting field reference.
              - `message` (string) **REQ** [enum=['The field api name seems to be invalid']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `UnsupportedKeyNotAllowedError` — Returned when the request contains keys that are not supported for the selected field update configuration.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field that is not supported for this action.
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field in the request body.
              - `message` (string) **REQ** [enum=[3 values]] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `DependentFieldMissingError` — Returned when one or more required dependent fields are missing from the request.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) **REQ** — Identifies the field that requires the missing dependent field.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the field that requires the dependent field.
                  - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field that requires the dependent field.
                - `api_name` (string) **REQ** [maxLen=255] — API name of the missing dependent field.
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the missing dependent field.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `MandatoryFieldMissingError` — Returned when a required field is missing in the request payload.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — API name of the missing required field.
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the missing required field.
              - `message` (string) **REQ** [enum=[9 values]] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidFieldValueTypeError` — Returned when a request field value has an invalid data type for the selected field update configuration.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) **REQ** [maxLen=255] — Expected data type for the field.
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field with the invalid value type.
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field in the request body.
              - `message` (string) **REQ** [maxLen=255] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `FieldLengthExceededError` — Returned when a field value exceeds its maximum allowed length or size constraint.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) **REQ** — The maximum allowed length or size for the field
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field that exceeded the limit
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field in the request body
              - `message` (string) **REQ** [enum=[3 values]] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidDataTypeError` — Returned when a field value type does not match the expected data type for the target field configuration.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field in the request body.
                - `supported_values` (array of string) [maxItems=25] **REQ** — List of values supported for the field.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidDataFieldValidationError` — Returned when the API validates a field value against its domain rules and finds it invalid  - for example, a non-existent module ID, an unknown field API name, or a name containing disallowed characters. Distinguished from data-type validation errors by the context-specific message.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details identifying the invalid field
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field that failed validation
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the invalid field in the request body
              - `message` (string) **REQ** [enum=[6 values]] — Context-specific error message describing the validation failure
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ExpectedFieldMissingError` — Returned when a required nested object (e.g., field) is provided but empty  - at least one identifying property (api_name or id) must be specified.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code.
              - `details` (object) **REQ** — Error details listing the expected fields that were missing
                - `expected_fields` (array of object) [maxItems=10] **REQ** — List of fields where at least one must be provided
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the expected field
                  - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the expected field in the request body
              - `message` (string) **REQ** [maxLen=255] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `DependentMismatchError` — Returned when a field's value is invalid in the context of its dependent field. For example, passing an unsupported type value for the given target field.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code.
              - `details` (object) **REQ** — Error details identifying the mismatched dependency
                - `dependee` (object) **REQ** — The field that the invalid value depends on
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the dependee field
                  - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the dependee field
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field with the invalid value
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field with the invalid value
              - `message` (string) **REQ** [maxLen=255, enum=['Dependent Field is not matching']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Indicates that the user does not have the necessary permissions to create a field update action. [application/json]
    > Error response indicating that the user does not have the necessary permissions to create a field update action.
    - `field_updates` (array of object `FeatureNoPermissionError`) [maxItems=10] **REQ** — List of error responses for each field update action that failed due to insufficient permissions.
      schema: `FeatureNoPermissionError`
      - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code.
      - `details` (object) **REQ** — Error details with validation information
        - `permissions` (array of string) [maxItems=25] — Permission that the current user is missing
          items: [maxLen=255]
        - `api_name` (string) [maxLen=255] — API name of the field associated with the permission error.
        - `json_path` (string) [maxLen=1000] — JSON path to the field in the request body
      - `message` (string) **REQ** [enum=[3 values]] — Represents the error message.
      - `status` (string) **REQ** [enum=['error']] — Represents the error status

**Scopes:** ZohoCRM.settings.automation_actions.CREATE
