# POST /settings/fields/{fieldId}/actions/replace_pick_list_values
**Operation:** `postReplacePickListValues` — Replace Pick list values
> Replace picklist value

**Parameters:**
- `module` (query, string, required) [maxLen=50, minLen=1] {style=form, explode=True}: Specify the API name of the CRM module that contains the field. Refer to the [Get Modules](modules.json#$.paths./settings/modules.get) resource for valid values.
- `fieldId` (path, string/int64, required) [minLen=1] {style=simple, explode=False}: Specify the unique numeric identifier of the field. Refer to the [Get Fields Metadata](fields.json#$.paths./settings/fields/{fieldId}.get) resource for valid values.

**Request Body** — application/json `PicklistReplaceRequestBody`
> Request body
  > Container for the replace_pick_list_values array, listing one or more instructions to perform picklist value replacements.
  - `replace_pick_list_values` (array of object `PicklistReplaceInstructionItem`) [minItems=1, maxItems=1] **REQ** — Replace picklist value with from and to options (Required)
    schema: `PicklistReplaceInstructionItem`
    - `old_value` (object `PicklistReplaceSourceValue`) **REQ** — The option which is to be replaced (Required)
      - `display_value` (string) [maxLen=120, nullable] — Specify the display value of the option to be replaced
      - `id` (string/int64) [maxLen=20, minLen=13, nullable] — Specify the option id which is to be replaced (Unique)
      anyOf:
    - `new_value` (object `PicklistReplaceTargetValue`) **REQ** — The option to be replaced with the option (Required)
      - `display_value` (string) [maxLen=120, nullable] — Display value of the option
      - `id` (string/int64) [maxLen=20, minLen=13, nullable] — The option id (Unique)
      anyOf:
    - `delete_old_value` (boolean) [nullable] — Boolean value to delete the old_value along with replace

**Responses:**

- **202**: Accepted - Request accepted for processing — Schema: `PicklistReplaceResponse` [application/json]
    > Accepted response indicating picklist replace operations have been scheduled. Returns an array of scheduling results.
    schema: `PicklistReplaceResponse`
    - `replace_pick_list_values` (array of object `PicklistReplaceScheduleResult`) [minItems=1, maxItems=1] **REQ** — Description of the replace option on schedule
      schema: `PicklistReplaceScheduleResult`
      - `code` (string) **REQ** [enum=['SCHEDULED']] — Code of the scheduler response
      - `details` (object `AsyncJobDetails`) **REQ** — Contains the scheduler job identifier for an asynchronous operation that was accepted for processing.
        schema: `AsyncJobDetails`
        - `job_id` (string/int64) **REQ** [maxLen=20, minLen=13] — scheduler jobid
      - `message` (string) **REQ** [enum=['Picklist option replace operation scheduled successfully']] — Message of the scheduled details
      - `status` (string) **REQ** [maxLen=7, minLen=5, enum=['success']] — status on replace operation of the scheduler

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
      - `InvalidFieldIdErrorResponse` — Returned when the provided field ID is invalid for the requested operation. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['The Field Id is Invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidReplacePayloadTypeErrorResponse` — Returned when the replace_pick_list_values payload has an invalid data type or exceeds allowed constraints. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `maximum_length` (integer/int32) **REQ** — Detail field: maximum_length
          - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
          - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
        - `message` (string) **REQ** [enum=['invalid data type replace_pick_list_values object']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
        - `replace_pick_list_values` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `InvalidSourceOptionIdErrorResponse` — Returned when the ID provided in old_value (source option) is invalid. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The id given in old_value is invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidTargetOptionIdErrorResponse` — Returned when the ID provided in new_value (target option) is invalid. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The id given in new_value is invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ReplaceBlockedOptionInUseErrorResponse` — Returned when a replace operation is blocked because the option is used by other features. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `_associations` (array of object) [maxItems=25] **REQ** — Detail field: _associations
                  - `resources` (array of object) [maxItems=25] **REQ** — Nested detail field: resources
                    - `name` (string) **REQ** [maxLen=255] — Nested detail field: name
                    - `id` (string) **REQ** [maxLen=255] — Nested detail field: id
                    - `_details` (object) **REQ** [nullable] — Nested detail field: _details
                  - `type` (string) **REQ** [maxLen=255] — Nested detail field: type
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The picklist option is used in features']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GlobalPicklistOptionReplaceErrorResponse` — Returned when attempting to replace a global picklist option, which is not allowed. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Global picklist option cannot be replaced']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `RestrictedPicklistOptionReplaceErrorResponse` — Returned when attempting to replace a restricted picklist option. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Restricted Option cannot be replaced']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `TargetOptionExpectedFieldMissingErrorResponse` — Returned when required fields for new_value are not provided. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_fields` (array of object) [maxItems=25] **REQ** — Detail field: expected_fields
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['specify atleast one field']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `SourceOptionAmbiguityErrorResponse` — Returned when ambiguity occurs while processing old_value (source option). Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Detail field: ambiguity_due_to
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['ambiguity while processing the old_value']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `TargetOptionAmbiguityErrorResponse` — Returned when ambiguity occurs while processing new_value (target option). Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Detail field: ambiguity_due_to
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['ambiguity while processing the new_value']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `IdenticalSourceAndTargetErrorResponse` — Returned when old_value and new_value reference the same picklist option. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) **REQ** — Detail field: dependee
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['old_value and new_value should not be the same']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `SourceOptionMandatoryErrorResponse` — Returned when old_value is missing in the replace request. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['old_value is mandatory']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `TargetOptionMandatoryErrorResponse` — Returned when new_value is missing in the replace request. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['new_value is mandatory']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidTargetDisplayValueErrorResponse` — Returned when the display_value provided in new_value is invalid. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The display_value given in new_value is invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidDeleteOldValueFlagErrorResponse` — Returned when delete_old_value has an invalid boolean format. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) **REQ** [maxLen=255] — Detail field: expected_data_type
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The delete_old_value boolean field type mismatch']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidSourceOptionObjectErrorResponse` — Returned when old_value is not a valid object or has an unexpected structure. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) **REQ** [maxLen=255] — Detail field: expected_data_type
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['old_value expected data type invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidTargetOptionObjectErrorResponse` — Returned when new_value is not a valid object or has an unexpected structure. Includes error code, message, status, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) **REQ** [maxLen=255] — Detail field: expected_data_type
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['new_value expected data type invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `DeleteOldValueNotAllowedErrorResponse` — Returned when delete_old_value is set to true for a regular picklist field where deletion of old value is not allowed.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details
                - `api_name` (string) **REQ** [maxLen=255] — The field API name
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path of the field
              - `message` (string) **REQ** [enum=['Cannot delete old_value for a picklist field']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidModuleErrorResponse` — Returned when the specified module name is invalid. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `RequiredModuleParameterMissingErrorResponse` — Returned when the required module parameter is missing. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `FeatureNotSupportedErrorResponse` — Returned when the requested feature is not supported by the current license. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['Your License does not support this feature']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidReplacePayloadTypeMinErrorResponse` — Returned when the replace_pick_list_values payload fails minimum length or type validations. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
          - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
          - `minimum_length` (integer/int32) **REQ** — Detail field: minimum_length
        - `message` (string) **REQ** [enum=['invalid data type replace_pick_list_values object']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `MultiselectPicklistReplaceNotAllowedErrorResponse` — Returned when attempting to replace picklist options on a multiselect picklist field, which is not supported.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details
          - `resource_path_index` (integer/int64) **REQ** — Resource path index
        - `message` (string) **REQ** [enum=['PickList option replace not allowed']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Forbidden - The client does not have access rights to the content. — Schema: `PermissionDeniedErrorResponse` [application/json]
    > Returned when the user lacks permission to access the requested picklist resource. Includes error code, message, status, and details.
    schema: `PermissionDeniedErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code.
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] **REQ** — Detail field: permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.fields.UPDATE
