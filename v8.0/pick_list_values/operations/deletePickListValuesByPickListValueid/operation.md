# DELETE /settings/fields/{fieldId}/pick_list_values/{pickListValueId}
**Operation:** `deletePickListValuesByPickListValueid` — Delete a picklist field option
> Delete picklist field option

**Parameters:**
- `module` (query, string, required) [maxLen=50, minLen=1] {style=form, explode=True}: Specify the API name of the CRM module that contains the field. Refer to the [Get Modules](modules.json#$.paths./settings/modules.get) resource for valid values.
- `fieldId` (path, string/int64, required) [minLen=1] {style=simple, explode=False}: Specify the unique numeric identifier of the field. Refer to the [Get Fields Metadata](fields.json#$.paths./settings/fields/{fieldId}.get) resource for valid values.
- `pickListValueId` (path, string/int64, required) [maxLen=255]: Path parameter: pickListValueId

**Responses:**

- **200**: OK - Picklist option deleted successfully — Schema: `DirectPicklistOptionDeletionResponse` [application/json]
    > Success response indicating picklist option has been deleted directly. Returns an array of deletion results.
    schema: `DirectPicklistOptionDeletionResponse`
    - `pick_list_values` (array of object `DirectPicklistOptionDeletionResult`) [minItems=0, maxItems=1] **REQ** — pick list values
      schema: `DirectPicklistOptionDeletionResult`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Picklist option deletion result code
      - `details` (object) **REQ** — Details of the deleted picklist option
        - `id` (string/int64) **REQ** [maxLen=100, minLen=13] — The unique ID of the deleted picklist option
      - `message` (string) **REQ** [enum=['PickList Option deleted successfully']] — Picklist option deletion message
      - `status` (string) **REQ** [maxLen=7, minLen=5, enum=['success']] — Picklist option deletion status

- **202**: Accepted - Request accepted for processing — Schema: `PicklistOptionDeletionResponse` [application/json]
    > Accepted response indicating picklist option deletion has been scheduled. Returns an array of deletion results.
    schema: `PicklistOptionDeletionResponse`
    - `pick_list_values` (array of object `PicklistOptionDeletionResult`) [minItems=0, maxItems=1] **REQ** — pick list values
      schema: `PicklistOptionDeletionResult`
      - `code` (string) **REQ** [enum=['SCHEDULED']] — picklist option deletion code
      - `details` (object `AsyncJobDetails`) **REQ** — Contains the scheduler job identifier for an asynchronous operation that was accepted for processing.
        schema: `AsyncJobDetails`
        - `job_id` (string/int64) **REQ** [maxLen=20, minLen=13] — scheduler jobid
      - `message` (string) **REQ** [enum=['Picklist Option deletion scheduled successfully']] — Picklist option deletion message
      - `status` (string) **REQ** [maxLen=7, minLen=5, enum=['success']] — Picklist option deletion status

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
      - `InvalidPicklistOptionIdErrorResponse` — Returned when the specified picklist option ID does not exist or is invalid. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['pickList option is not available']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidModuleErrorResponse` — Returned when the specified module name is invalid. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidFieldIdForPicklistValuesErrorResponse` — Returned when the provided field ID is invalid for retrieving picklist values. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['The Field Id is Invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `RestrictedPicklistOptionDeletionErrorResponse` — Returned when attempting to delete a restricted picklist option. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['Restricted Option cannot be deleted']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `PicklistOptionInUseErrorResponse` — Returned when the picklist option is used by other features and cannot be modified. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `_associations` (array of object) [maxItems=25] **REQ** — Detail field: _associations
            - `resources` (array of object) [maxItems=25] **REQ** — Nested detail field: resources
              - `name` (string) **REQ** [maxLen=255] — Nested detail field: name
              - `id` (string) **REQ** [maxLen=255] — Nested detail field: id
              - `_details` (object) **REQ** [nullable] — Nested detail field: _details
            - `type` (string) **REQ** [maxLen=255] — Nested detail field: type
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['The picklist option is used in features']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistOptionDeletionErrorResponse` — Returned when attempting to delete a global picklist option, which is not allowed. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['Global picklist option cannot be deleted']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `MinimumPicklistOptionConstraintErrorResponse` — Returned when deletion would leave no options in a layout (must have at least one option). Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=[2 values]] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `MultipleLayoutAssociationDeletionErrorResponse` — Returned when the picklist option exists in multiple layouts and cannot be deleted. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=[1 values]] — Error message
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

- **403**: Forbidden - The client does not have access rights to the content. — Schema: `PermissionDeniedErrorResponse` [application/json]
    > Returned when the user lacks permission to access the requested picklist resource. Includes error code, message, status, and details.
    schema: `PermissionDeniedErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code.
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] **REQ** — Detail field: permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.fields.DELETE
