# POST /settings/blueprints/transitions
**Operation:** `createBlueprintTransitions` — Create Blueprint transitions
> To create one or more Blueprint transitions for an existing Blueprint in your Zoho CRM organization.

**Schemas:**
`ActionLimitExceedsError`:
  > Represents the validation error returned when the configured action count exceeds the permitted limit for the action type (code: INVALID_DATA).
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the action limit is exceeded. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with information about the exceeded action limit, such as the action type, its API name, the configured count, and the allowed limit.
    - `action_type` (string) **REQ** [maxLen=255] — Indicates the type of the action that exceeded the configured limit.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the action that exceeded the configured limit.
    - `limit` (integer/int32) **REQ** — Indicates the maximum number of actions allowed for the transition.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the action in the request that caused the error.
    - `configured_count` (integer/int32) **REQ** — Indicates the number of actions currently configured for the transition.
  - `message` (string) **REQ** [enum=['Action Limit Exceeds']] — Represents the error message returned when the action limit is exceeded. Possible values: **Action Limit Exceeds**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ActionNotBelongingToModuleError`:
  > Represents the error returned when the specified action does not belong to the current module of the transition (code: INVALID_DATA).
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the action does not belong to the module. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level information about the action that does not belong to the current module of the transition.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
  - `message` (string) **REQ** [enum=['The action does not belong to the current module of the transition']] — Represents the error message returned when the action does not belong to the current module of the transition. Possible values: **The action does not belong to the current module of the transition**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ActionNotSupportedForModuleError`:
  > Represents the validation error returned when the specified action type is not supported for the given module (code: INVALID_DATA).
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the action is not supported for the module of the transition. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level information about the action that is not supported for the module of the transition.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
  - `message` (string) **REQ** [enum=['Action Not Supported For Module']] — Represents the error message returned when the action is not supported for the module of the transition. Possible values: **Action Not Supported For Module**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`AdditionalCriteriaGroupFieldReference2`:
  > Field data of the field associated in during field
  - `api_name` (string) [maxLen=100, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — Represents the API name of the field associated with the during input of the transition.
  - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]+$, nullable] — Represents the ID of the field associated with the during input of the transition.
`AutomaticTransitionOwnersNotAllowedError`:
  > Represents the error returned when owners are added to an automatic transition, which is not allowed. Possible values: **NOT_ALLOWED**.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when owners cannot be added to an automatic transition. Possible values: **NOT_ALLOWED**.
  - `details` (object) **REQ** — Contains the error details identifying the field that caused the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
  - `message` (string) **REQ** [enum=['Blueprint transition owners cannot be added to automatic transition']] — Represents the error message returned when owners cannot be added to an automatic transition. Possible values: **Blueprint transition owners cannot be added to automatic transition**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`BlueprintTransitionInvalidDataErrorResponse`:
  > Represents the standardized 400 error payload returned by the Blueprint Transitions API when a transition configuration contains invalid input, such as an invalid sequence number in during inputs. Includes the error status, a stable error code (INVALID_DATA), an error message, and validation details describing the offending fields.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the blueprint transition data fails validation. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that failed validation.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation error.
  - `message` (string) **REQ** [enum=['The given value seems to be invalid']] — Represents the error message returned when the request data for a blueprint transition is invalid. Possible values: **The given value seems to be invalid**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ChecklistItemsLimitExceededError`:
  > Represents the validation error returned when the number of checklist items provided for a checklist field in a blueprint transition exceeds the permitted limit. Contains the error code **DEPENDENT_MISMATCH**, the error message, the response status, and field-level error details, including the maximum permitted number of checklist items.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when the checklist item limit is exceeded. Possible values: **DEPENDENT_MISMATCH**.
  - `details` (object) **REQ** — Contains the error details with field-level validation information about the checklist item limit violation.
    - `dependee` (object) **REQ** — Contains details of the dependent checklist item associated with the checklist item limit validation error.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the dependee field associated with the checklist item limit validation error.
      - `dependee_value` (string) **REQ** [maxLen=255] — Represents the value of the dependee field associated with the checklist item limit validation error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the dependee field that caused the checklist item limit validation error.
    - `maximum_length` (integer/int32) **REQ** — Indicates the maximum permitted number of checklist items whose limit was exceeded.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the checklist field whose item limit was exceeded.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the checklist item limit validation error.
  - `message` (string) **REQ** [enum=['You can provide upto 10 checklist items']] — Represents the error message returned when the checklist item limit is exceeded. Possible values: **You can provide upto 10 checklist items**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ChecklistOptionLengthExceededError`:
  > Represents the validation error returned when the name of a checklist option in a blueprint transition exceeds the allowed character limit. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details, including the maximum number of characters allowed for a checklist option.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the checklist option length is exceeded. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level validation information for the checklist option length error.
    - `maximum_length` (integer/int32) **REQ** — Indicates the maximum number of characters allowed for a checklist option.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the checklist option length validation error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the checklist option that exceeded the allowed character length.
  - `message` (string) **REQ** [enum=['You can provide upto 140 checklists option character limit']] — Represents the error message returned when a checklist option exceeds the allowed character limit. Possible values: **You can provide upto 140 checklists option character limit**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ChecklistTitleLengthExceededError`:
  > Represents the validation error returned when a checklist title in a blueprint transition exceeds the maximum allowed length. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details, including the maximum number of characters allowed for the checklist title.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the checklist title exceeds the allowed length. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level validation information for the checklist title that exceeded the allowed length.
    - `maximum_length` (integer/int32) **REQ** — Indicates the maximum number of characters allowed for the checklist title.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that failed validation.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field in the request that failed validation.
  - `message` (string) **REQ** [enum=['You can provide upto 30 characters.']] — Represents the error message returned when the checklist title exceeds the allowed length. Possible values: **You can provide upto 30 characters.**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ChildParallelTransitionActionsNotAllowedError`:
  > Represents the error returned when after actions are added to a child parallel transition, which is not allowed. Contains the error code **NOT_ALLOWED**, the error message, the response status, and details identifying the disallowed field in the request.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when the operation is not permitted. Possible values: **NOT_ALLOWED**.
  - `details` (object) **REQ** — Contains the error details identifying the field that is not allowed.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the disallowed field.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the disallowed field in the request.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when blueprint transition after actions cannot be added to a child parallel transition. Possible values: **Blueprint transition after actions cannot be added to a child parallel transition**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`CriteriaFieldApiNameInvalidError`:
  > Represents the validation error returned when the API name of a criteria field in a blueprint transition is invalid. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details identifying the invalid criteria field.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the criteria field API name is invalid. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level information about the invalid criteria field API name.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the criteria field that is invalid.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the criteria field whose API name is invalid.
  - `message` (string) **REQ** [enum=['The given api_name seems to be invalid']] — Represents the error message returned when the criteria field API name is invalid. Possible values: **The given api_name seems to be invalid**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`CriteriaGroupCompositeAlternate`:
  > Represents the second alternate form of a composite criteria group, combining conditions and nested groups with a group operator. Contains the comparator used to compare the field value, the group of conditions combined using the group operator, the group operator itself, and the value against which the field value is compared.
  - `comparator` (string) [maxLen=20, nullable] — Represents the comparator of the criteria, used to compare the field value with the specified value.
  - `field` (object `AdditionalCriteriaGroupFieldReference2`) — This denotes the field used in the criteria
  - `value` (string) [maxLen=1000, nullable] — Represents the value against which the field value is compared in the criteria.
  - `group_operator` (string) [maxLen=3, nullable] — Represents the group operator that determines how the conditions in the criteria group are combined.
  - `group` (array of object `CriteriaGroupCompositeAlternate`) [maxItems=2] — Contains the group of conditions that are combined using the group operator in the criteria.
`CriteriaNotSupportedForFieldError`:
  > Represents the error response returned when criteria are not supported for the specified field, including the error code, message, status, and field-level details.
  - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code returned when criteria are not supported for the field. Possible values: **NOT_SUPPORTED**.
  - `details` (object) **REQ** — Contains the error details with field-level information about the field for which criteria are not supported.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which criteria are not supported.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field for which criteria are not supported.
  - `message` (string) **REQ** [enum=['criteria not supported for the field']] — Represents the error message returned when criteria are not supported for the field. Possible values: **criteria not supported for the field**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`DuringFieldCriteriaExpression`:
  > Validation criteria specified for the during field associated with the transition
  - `comparator` (string) [maxLen=12, nullable] — Represents the comparator used in the criteria.
  - `field` (object `DuringFieldDataReference`) — field of the criteria
  - `value` (string) [maxLen=1000, nullable] — Represents the value of the field to be compared with.
  - `group_operator` (string) [maxLen=3, nullable] — Represents the group operator of the criteria.
  - `group` (array of object `TransitionCriteriaGroupEntry`) [maxItems=1, nullable] — Represents the group of the criteria.
`DuringFieldDataReference`:
  > field of the criteria
  - `api_name` (string) [maxLen=100, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — Represents the API name of the field associated with the during field.
  - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]+$, nullable] — Represents the ID of the field associated with the during field.
`DuringFieldIdDuplicateError`:
  > Represents the validation error returned when a duplicate during field ID is present in the transition, including the error code, message, status, and details of the field that is already present.
  - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when a duplicate field ID is detected in the during input. Possible values: **DUPLICATE_DATA**.
  - `details` (object) **REQ** — Contains the validation details of the during-input field that is already present in the transition, including the field's API name and JSON path.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the during-input field that is already present in the transition.
    - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the during-input field that is already present in the transition.
  - `message` (string) **REQ** [enum=['field already present in during input for the transition']] — Contains the error message returned for the validation failure. Possible values: **field already present in during input for the transition**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`DuringFieldIdInvalidError`:
  > Represents the validation error returned when the provided during field ID is invalid, including the error code, message, status, and details of the field whose ID is invalid.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the given field ID is invalid. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the validation details of the field whose ID is invalid, including the field's API name and JSON path.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field whose ID is invalid.
    - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field whose ID is invalid.
  - `message` (string) **REQ** [enum=['field id given seems to be invalid']] — Contains the error message returned for the validation failure. Possible values: **field id given seems to be invalid**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`DuringFieldValidationFilter`:
  > Validation criteria detail for the during field
  - `criteria` (object `DuringFieldCriteriaExpression`) — Validation criteria specified for the during field associated with the transition
  - `validation_message` (string) [maxLen=100, nullable] — Represents the validation message shown in the during field when the field value fails validation.
`DuringInputConfiguredFieldAlternate`:
  > Represents the alternate configuration for a during-input sub-field, including the field reference, optional flag, and optional criteria.
  - `optional` (boolean) [nullable] — Indicates whether the field is optional to fill in the during input. Possible values: **true**, **false**.
  - `field` (object `AdditionalCriteriaGroupFieldReference2`) — Field data of the field associated in during field
  - `validation_filter` (object `DuringInputValidationFilterAlternate`) — criteria details for validation
  - `name` (string) [maxLen=100] — Represents the name of the configured field collected as a during input in the transition.
  - `subform_fields` (array of object `DuringInputConfiguredFieldAlternate`) [maxItems=10, nullable] — Contains the fields configured in the during input.
`DuringInputFieldIdInvalidDataError`:
  > Represents the validation error returned when the ID of a during-input field is invalid (code: INVALID_DATA).
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a during-input field ID contains invalid data. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level information.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path associated with the error.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned for a during-input field with invalid data. Possible values: **invalid data**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`DuringInputTypeDuplicateError`:
  > Represents the validation error returned when a during-input type is duplicated within the same transition (code: DUPLICATE_DATA).
  - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when more than one entry of the same during-input type is found in the transition. Possible values: **DUPLICATE_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level validation information about the duplicate during-input type.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the during input that caused the duplicate-type error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the during input that caused the duplicate-type error.
  - `message` (string) **REQ** [enum=['Only one type of this during field is allowed to be in the transition']] — Represents the error message describing the duplicate during-input validation failure. Possible values: **Only one type of this during field is allowed to be in the transition**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the request. Possible values: **error**.
`DuringInputValidationFilterAlternate`:
  > criteria details for validation
  - `criteria` (object `TransitionCriteriaExpressionAlternate2`) — Validation criteria specified for the during field associated with the transition
  - `validation_message` (string) [maxLen=100, nullable] — Represents the validation message to be shown in the during field.
`DuringInputsNotAllowedAutomaticError`:
  > Represents the error returned when during inputs are provided for an automatic transition, which is not allowed (code: NOT_ALLOWED).
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when blueprint transition during fields cannot be added to an automatic transition. Possible values: **NOT_ALLOWED**.
  - `details` (object) **REQ** — Contains the error details with field-level information.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field associated with the error.
  - `message` (string) **REQ** [enum=['Blueprint transition during fields cannot be added to automatic transition']] — Represents the error message returned. Possible values: **Blueprint transition during fields cannot be added to automatic transition**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`DuringInputsNotAllowedParallelError`:
  > Represents the error returned when during inputs are provided for a parallel transition, which is not allowed (error code **NOT_ALLOWED**).
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when during inputs are not allowed on a parallel blueprint transition. Possible values: **NOT_ALLOWED**.
  - `details` (object) **REQ** — Contains the error details with field-level information.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the transition property that caused the validation error.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when during-input fields cannot be added to a parent parallel transition. Possible values: **Blueprint transition during fields cannot be added to a parent parallel transition**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`DuringInputsWidgetAmbiguityError`:
  > Represents the error returned when during-input fields are configured along with a widget or kiosk, causing an ambiguity during processing (error code **AMBIGUITY_DURING_PROCESSING**).
  - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code returned when during-input fields are configured along with a widget or kiosk. Possible values: **AMBIGUITY_DURING_PROCESSING**.
  - `details` (object) **REQ** — Contains the error details with validation information about the widget or kiosk ambiguity.
    - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Contains the list of fields or components that caused the ambiguity during processing.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or component that caused the ambiguity.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field or component that caused the ambiguity.
  - `message` (string) **REQ** [enum=['provide proper data', 'Fields are configured along with widget or kiosk']] — Represents the error message returned when during-input fields are configured along with a widget or kiosk. Possible values:
- **provide proper data**
- **Fields are configured along with widget or kiosk**
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`InvalidDataError`:
  > Represents a general validation error returned when the request data is invalid. The error code is **INVALID_DATA**.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request data fails validation. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information about the invalid data failure.
    - `maximum_length` (integer/int32) **REQ** — Indicates the maximum permitted length for the field that caused the validation error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation error.
  - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned for the validation failure. Possible values: **Invalid data**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`InvalidDataTypeError`:
  > Represents a validation error returned when one or more request fields contain a value with an invalid data type. The error code is **INVALID_DATA**.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request data fails validation. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information about the invalid data failure.
    - `expected_data_type` (string) **REQ** [maxLen=255] — Indicates the data type expected for the field whose value failed data type validation.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field whose value has an invalid data type.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field whose value has an invalid data type.
  - `message` (string) **REQ** [enum=['Invalid data type']] — Contains the error message returned when a field value has an invalid data type. Possible values: **Invalid data type**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`InvalidDataValidationError`:
  > Represents a validation error returned for generic invalid data conditions during transition processing. The error code is **INVALID_DATA**.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when field data fails validation. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information for the invalid data.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field whose value failed validation.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field whose value failed validation.
    - `supported_values` (array of string) [maxItems=25] **REQ** — Contains the list of values supported for the field whose value failed validation.
      items: [maxLen=255]
  - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned when the data fails validation. Possible values: **Invalid data**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`InvalidEscalationPeriodError`:
  > Represents the error returned when the period value provided in the escalation settings is invalid. The error code is **INVALID_DATA**.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the escalation period is invalid. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level validation information for the invalid escalation period.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field whose value failed validation.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field whose value failed validation.
    - `supported_values` (array of string) [maxItems=25] **REQ** — Contains the values supported by the field that failed validation.
      items: [maxLen=255]
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned when the escalation period is invalid. Possible values: **invalid data**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`InvalidValueResponse`:
  > Represents the error response returned when invalid module data is provided during a reorder request. The response includes the error code **INVALID_DATA**, a descriptive message, a status, and validation details.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a value in the request is invalid. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the property that holds the invalid value.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the property that holds the invalid value.
  - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the given ID is invalid. Possible values: **the id given seems to be invalid**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`InvalidWidgetError`:
  > Represents a validation error returned when the widget provided in during_inputs is invalid. The error code is **INVALID_DATA**.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the widget reference is invalid. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details that identify the invalid widget reference.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid widget.
    - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the invalid widget reference in the request.
    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the ID of the invalid widget.
  - `message` (string) **REQ** [enum=['Invalid widget']] — Represents the error message returned when the widget reference is invalid. Possible values: **Invalid widget**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`KioskIdInvalidError`:
  > Represents the validation error returned when the kiosk ID provided in during_inputs is invalid or inactive. Possible values for code: **INVALID_DATA**.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the kiosk ID is invalid. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details that identify the invalid kiosk reference.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid kiosk reference associated with the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field associated with the error.
    - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the ID of the invalid kiosk associated with the error.
  - `message` (string) **REQ** [enum=['Kiosk ID provided is invalid']] — Represents the error message returned when the provided kiosk ID is invalid. Possible values: **Kiosk ID provided is invalid**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ModuleApiNameInvalidError`:
  > Represents the validation error returned when the provided module API name is invalid. Possible values for code: **INVALID_DATA**.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the module API name is invalid. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with validation information, including the API name and the JSON path of the invalid value.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module identified as invalid.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the property that contains the invalid value.
  - `message` (string) **REQ** [enum=['the value given is invalid']] — Represents the error message returned when the module API name is invalid. Possible values: **the value given is invalid**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ModuleIdentifierAmbiguityError`:
  > Represents the processing error returned when ambiguity is detected between the module ID and API name while creating a transition. Possible values for code: **AMBIGUITY_DURING_PROCESSING**.
  - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code returned when ambiguity is detected during processing. Possible values: **AMBIGUITY_DURING_PROCESSING**.
  - `details` (object) **REQ** — Contains the error details object with validation information about the ambiguity.
    - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Contains the list of identifiers that caused the ambiguity during processing.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module associated with the ambiguity.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field associated with the ambiguity.
  - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message returned for the ambiguity. Possible values: **Ambiguity while processing the request**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ParallelTransitionDependentFieldMissingError`:
  > Represents the error returned when the parallel_transition field is missing while its dependee field, transition_type, is present (error code: DEPENDENT_FIELD_MISSING).
  - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code returned when a dependent field is missing in a parallel transition. Possible values: **DEPENDENT_FIELD_MISSING**.
  - `details` (object) **REQ** — Contains the error details, including the API name and JSON path of the missing field and information about the dependee field it depends on.
    - `dependee` (object) **REQ** — Contains the details of the field that the missing field depends on.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the dependee field.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the dependee field.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that is missing.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing field.
  - `message` (string) **REQ** [enum=['Dependent field is missing']] — Represents the error message returned when a dependent field is missing. Possible values: **Dependent field is missing**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ParallelTransitionIdInvalidError`:
  > Represents the error returned when the specified parallel_transition ID is not associated with any blueprint (error code: INVALID_DATA).
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the specified parallel transition ID is not associated with any blueprint. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level information about the invalid parallel transition ID.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
  - `message` (string) **REQ** [enum=['The specified parallel_transition id is not associated with any blueprint']] — Indicates the error message returned for the failed request. Possible values: **The specified parallel_transition id is not associated with any blueprint**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`ParallelTransitionMandatoryNotFoundError`:
  > Represents the error returned when a required field within parallel_transition is missing from the request (error code: MANDATORY_NOT_FOUND).
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a mandatory property is not found in the request. Possible values: **MANDATORY_NOT_FOUND**.
  - `details` (object) **REQ** — Contains the error details object with field-level information about the missing mandatory property.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the mandatory field that is missing.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the mandatory field that is missing from the parallel transition.
  - `message` (string) **REQ** [enum=['The required data missing']] — Represents the error message returned when required data is missing from the parallel transition. Possible values: **The required data missing**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`PipelineCannotBeEmptyErrorResponse`:
  > Represents the error returned when pipeline details are not provided for a pipeline-enabled module during transition creation (error code: INVALID_DATA).
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the pipeline is empty. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with pipeline field information.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the pipeline field associated with the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the pipeline field associated with the error.
  - `message` (string) **REQ** [enum=['Pipeline cannot be empty']] — Represents the error message returned when the pipeline is empty. Possible values: **Pipeline cannot be empty**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`RelatedListModuleReference`:
  > Related list module data associated in during field
  - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the module of the related list associated in the during field.
  - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]+$, nullable] — Represents the ID of the module of the related list associated in the during field.
`RequiredFieldMissingError`:
  > Represents the validation error returned when a required field is missing in the request, with the error code MANDATORY_NOT_FOUND.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a mandatory field is missing. Possible values: **MANDATORY_NOT_FOUND**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information about the missing mandatory field.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the mandatory field that is missing.
    - `json_path` (string) **REQ** [maxLen=1000] — Contains the JSON path of the field where the required value is missing.
  - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message returned when a required field is missing. Possible values: **Required field is missing**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TeamUserNotAllowedForOrgModule`:
  > Represents the error returned when a team or team-profile user is configured as a transition owner for an organization module, with the error code NOT_ALLOWED.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when a team user is not allowed to access the module. Possible values: **NOT_ALLOWED**.
  - `details` (object) **REQ** — Contains the error details object with field-level information about the validation failure.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned by the API. Possible values: **team and team_profile type users cannot be configured as transition owners for organization modules**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TransitionActionDetails`:
  > Represents the reference to an action configured for a blueprint transition, identified by its name and ID.
  - `name` (string) [maxLen=11, nullable] — Represents the name of the action of the transition to be created.
  - `id` (string) [maxLen=255, nullable] — Represents the ID of the action of the transition to be created.
`TransitionActionTypeUnsupportedError`:
  > Represents the validation error returned when the specified transition action type is not supported, with the error code INVALID_DATA.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the transition action type is unsupported. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information for the unsupported transition action type.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the validation error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field associated with the validation error.
  - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned when the transition action type is unsupported. Possible values: **Invalid data**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TransitionActionsAmbiguityError`:
  > Represents the error returned when ambiguous or conflicting after-action data is detected in the transition (code: AMBIGUITY_DURING_PROCESSING).
  - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code returned when ambiguity is detected while processing the transition actions. Possible values: **AMBIGUITY_DURING_PROCESSING**.
  - `details` (object) **REQ** — Contains the error details object with validation information about the ambiguity detected while processing the transition actions.
    - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Contains the list of sources that caused ambiguity while processing the transition actions.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the element that caused the ambiguity while processing the transition actions.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the element that caused the ambiguity while processing the transition actions.
  - `message` (string) **REQ** [enum=['Provide proper data']] — Represents the error message returned for the API call. Possible values: **Provide proper data**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TransitionCriteriaExpressionAlternate2`:
  > Validation criteria specified for the during field associated with the transition
  - `comparator` (string) [maxLen=20, nullable] — Represents the comparator used to evaluate the criteria of the blueprint transition.
  - `field` (object `AdditionalCriteriaGroupFieldReference2`) — field of the criteria
  - `value` (string) [maxLen=1000, nullable] — Represents the value of the field to be compared with in the transition criteria.
  - `group_operator` (string) [maxLen=3, nullable] — Represents the group operator applied to the criteria of the blueprint transition.
  - `group` (array of object `CriteriaGroupCompositeAlternate`) [maxItems=1, nullable] — Contains the criteria group to which the transition criteria belong.
`TransitionCriteriaGroupEntry`:
  > Represents a group of criteria within a blueprint transition, combining multiple conditions under a group operator for transition evaluation.
  - `comparator` (string) [maxLen=20, nullable] — Represents the comparator used to evaluate the criteria of the blueprint transition.
  - `field` (object `DuringFieldDataReference`) — This denotes the field used in the criteria
  - `value` (string) [maxLen=1000, nullable] — Represents the value against which the field value is compared in the criteria.
  - `group_operator` (string) [maxLen=3, nullable] — Represents the group operator that combines the criteria entries within a criteria group.
  - `group` (array of object `TransitionCriteriaGroupEntry`) [maxItems=2] — Contains the criteria group to which the transition criteria belong.
`TransitionDuringFieldsLimitExceededError`:
  > Represents the error returned when the number of fields configured in the during input of a blueprint transition exceeds the permitted limit.
  - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code returned when the number of fields configured for the transition's during input exceeds the allowed limit. Possible values: **LIMIT_EXCEEDED**.
  - `details` (object) **REQ** — Contains the error details with limit information for the fields that exceed the allowed during-input limit.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error detail.
    - `limit` (integer/int32) **REQ** — Indicates the maximum number of fields allowed in the transition's during input.
    - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the element associated with the error detail.
  - `message` (string) **REQ** [enum=['Blueprint transition during fields limit exceed']] — Represents the error message returned when the transition's during-input field limit is exceeded. Possible values: **Blueprint transition during fields limit exceed**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TransitionModuleMissingError`:
  > Represents the validation error returned when the required module field is missing in the transition request, identified by the error code **MANDATORY_NOT_FOUND**.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when the mandatory module details are not found in the request. Possible values: **MANDATORY_NOT_FOUND**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information about the missing module.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
  - `message` (string) **REQ** [enum=['required field not found']] — Contains the error message returned when a required field is not found. Possible values: **required field not found**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TransitionOperationResult`:
  > Represents the outcome of processing an individual transition, including the status, code, message, and optional details.
  - `code` (string) [maxLen=255] — Represents the result code returned for the transition operation.
  - `details` (object `TransitionActionDetails`) — Represents the reference to an action configured for a blueprint transition, identified by its name and ID.
  - `message` (string) [maxLen=255] — Represents the message returned for the transition operation, describing its outcome.
  - `status` (string) [maxLen=255] — Indicates the response status of the transition operation.
`TransitionTypeInvalidValueError`:
  > Represents the error payload returned when the provided transition type value is invalid, including the API name and JSON path of the field and the values it supports.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the invalid transition type value. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details object with field-level validation information.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation error.
    - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
    - `supported_values` (array of string) [maxItems=25] **REQ** — Contains the values supported for the field that caused the error.
      items: [maxLen=255]
  - `message` (string) **REQ** [enum=['the value given is invalid']] — Represents the error message returned when the given value is invalid. Possible values: **the value given is invalid**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
`TransitionsFieldInvalidTypeError`:
  > Represents the validation error returned when the transitions property in the request contains a field with an invalid data type. The response carries the error code **INVALID_DATA** along with field-level validation details.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a field in the transition configuration has an invalid data type. Possible values: **INVALID_DATA**.
  - `details` (object) **REQ** — Contains the error details with field-level validation information about the invalid field.
    - `maximum_length` (integer/int32) **REQ** — Indicates the maximum length allowed for the field that failed validation.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with the invalid data type.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field with the invalid data type in the request payload.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned when a field in the transition configuration has an invalid data type. Possible values: **invalid data**.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.

**Request Body** — application/json `TransitionCreateRequestBody`
> The request body must contain a **transitions** array with one object. The object represents the Blueprint transition to be created.
  > Represents the request body for creating one or more blueprint transitions, where each entry carries the full transition definition.
  - `transitions` (array of object `TransitionCreateDefinition`) [maxItems=1] **REQ** — Contains the list of transitions to be created, where each object in the array represents a single transition.
    schema: `TransitionCreateDefinition`
    - `during_inputs` (array of object `TransitionDuringInputEntry`) [maxItems=50, nullable] — Contains the during inputs of the transition to be created, such as fields, notes, attachments, tags, checklists, related lists, and kiosk screens.
      schema: `TransitionDuringInputEntry`
      - `validation_filter` (object `DuringFieldValidationFilter`) — Validation criteria detail for the during field
      - `sequence` (integer/int32) [nullable] — Indicates the order of the during-input fields of the transition to be created.
      - `field` (object `DuringFieldDataReference`) — Field data of the field associated in during field
      - `configured_fields` (array of object `DuringInputConfiguredField`) [maxItems=10, nullable] — Contains the fields configured in the during input.
        schema: `DuringInputConfiguredField`
        - `optional` (boolean) [nullable] — Indicates whether the configured field is optional. Possible values: **true**, **false**.
        - `field` (object `DuringFieldDataReference`) — Field data of the field associated in during field
        - `criteria` (object `DuringFieldCriteriaExpression`) — criteria details for validation
        - `validation_filter` (object `DuringFieldValidationFilter`) — Validation criteria detail for the during field
        - `name` (string) [maxLen=100] — Represents the name of the configured field collected as a during input in the transition.
        - `subform_fields` (array of object `DuringInputConfiguredFieldAlternate`) [maxItems=10, nullable] — Contains the fields configured in the during input of the transition.
      - `optional` (boolean) [nullable] — Indicates whether this during-input field is optional. Only Boolean values are accepted; string values return an INVALID_DATA error. Possible values: **true**, **false**.
      - `type` (string) [maxLen=20, nullable] — Indicates the type of the during-input field configured for the transition to be created.
      - `message` (string) [maxLen=1000, nullable] — Represents the informational message displayed in the during input.
      - `title` (string) [maxLen=10, nullable] — Represents the title of the checklist associated with the during-input field.
      - `kiosk` (object `DuringInputKioskReference`) — kiosk data associated in during field
        schema: `DuringInputKioskReference`
        - `name` (string) [maxLen=10, nullable] — Indicates the kiosk name associated with the during input field.
        - `id` (string) [maxLen=17, nullable] — Indicates the kiosk ID associated with the during input field.
      - `related_list` (object `DuringInputRelatedListEntry`) — Related list data of the RL associated in the blueprint
        schema: `DuringInputRelatedListEntry`
        - `layout` (object `DuringInputLayoutReference`) — layout data associated in during field
          schema: `DuringInputLayoutReference`
          - `api_name` (string) [maxLen=8, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — Represents the API name of the related list layout collected as a during input in the transition.
          - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]{1,19}$, nullable] — Represents the ID of the related list layout collected as a during input in the transition.
        - `name` (string) [maxLen=100, nullable] — Represents the name of the related list collected as a during input in the transition.
        - `id` (string) [maxLen=25, nullable] — Represents the ID of the related list associated with the blueprint transition.
        - `module` (object `RelatedListModuleReference`) — Related list module data associated in during field
      - `items` (array of object `DuringInputChecklistItem`) [maxItems=2, nullable] — Contains the items of the checklist associated with the during-input field.
        schema: `DuringInputChecklistItem`
        - `name` (string) [maxLen=6, nullable] — Represents the name of the checklist item associated with the during field.
        - `sequence` (integer/int32) [nullable] — Represents the sequence of the checklist item associated with the during field.
        - `optional` (boolean) [nullable] — Indicates whether the checklist item is optional. Possible values: **true**, **false**.
    - `criteria` (object `DuringFieldCriteriaExpression`) — This denotes the criteria of the transition to be created.
    - `trigger_type` (string) **REQ** [maxLen=100, enum=['automatic', 'manual']] — Indicates the trigger type of the transition to be created, i.e., whether the transition is executed manually or automatically.
Possible values:
- **automatic**
- **manual**
    - `module` (object `TransitionModuleIdentifier`) **REQ** — This denotes the module of the transition to be created (Required)
      schema: `TransitionModuleIdentifier`
      - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the module for which the transition is created in a blueprint.
      - `id` (string/int64) **REQ** [maxLen=50, minLen=1, pattern=^[0-9]+$] — Represents the ID of the module for which the transition is created.
    - `name` (string) **REQ** [maxLen=50] — Represents the name of the transition to be created. Transition names within a specific blueprint must be unique.
    - `description` (string) [maxLen=1000, nullable] — Represents the description of the transition to be created.
    - `transition_type` (string) **REQ** [maxLen=100, enum=['standalone_transition', 'parallel_transition', 'child_transition']] — Represents the type of the transition to be created.
Possible values:
- **standalone_transition**
- **parallel_transition**
- **child_transition**
    - `owners` (array of object `TransitionOwnerEntry`) [maxItems=5] **REQ** — Contains the owners of the transition to be created who can execute the transition.
      discriminator: `type`
        users → #/components/schemas/UserOwnerEntry
        role → #/components/schemas/RoleOwnerEntry
        group → #/components/schemas/GroupOwnerEntry
      oneOf:
        - `UserOwnerEntry` — Represents the owner assignment of type **users** for a transition. The resources list contains the IDs of the users, roles, or groups permitted to execute the transition.
          - `type` (string) **REQ** [enum=['users']] — Indicates the type of the owner assignment. Possible values: **users**.
          - `resources` (array of object `UserOwnerResource`) [maxItems=10, nullable] — Contains the list of owners of the transition who can execute it.
            schema: `UserOwnerResource`
            - `id` (string) [maxLen=35, nullable] — Represents the ID of the owner of the transition.
        - `RoleOwnerEntry` — Represents the owner assignment of type role for a blueprint transition, with the list of role resources permitted to execute the transition.
          - `type` (string) **REQ** [enum=['role']] — Represents the type of the owner assignment. Possible values: **role**.
          - `resources` (array of object `RoleOwnerResource`) [maxItems=10, nullable] — Contains the list of owners of the transition who can execute it.
            schema: `RoleOwnerResource`
            - `id` (string) [maxLen=35, nullable] — Represents the ID of the owner of the transition.
        - `GroupOwnerEntry` — Represents the owner assignment for the **group** owner type. The resources list contains the user, role, or group IDs that can execute the transition.
          - `type` (string) **REQ** [enum=['group']] — Represents the type of the owner assignment for a group owner of the transition. Possible values: **group**.
          - `resources` (array of object `GroupOwnerResource`) [maxItems=10, nullable] — Contains the list of owners of the transition who can execute it.
            schema: `GroupOwnerResource`
            - `id` (string) [maxLen=35, nullable] — Represents the ID of the owner of the transition to be created.
        - `GeneralOwnerEntry` — Represents the owner assignment of the transition for non-referenced owner types: **record_owner**, **team_user**, and **portal_user_type**.
          - `type` (string) **REQ** [enum=['record_owner', 'team_user', 'portal_user_type']] — Represents the type of the owner assignment for a general owner of the transition. Possible values: **record_owner**, **team_user**, **portal_user_type**.
          - `resources` (array of object `TransitionOwnerResourceEntry`) [maxItems=2, nullable] — Contains the list of owners of the transition who can execute it.
            schema: `TransitionOwnerResourceEntry`
            - `id` (string) [maxLen=25, nullable] — Represents the ID of the owner of the transition.
    - `actions` (array of object `TransitionAfterActionEntry`) [maxItems=4, nullable] — Contains the list of after actions of the transition to be created.
      schema: `TransitionAfterActionEntry`
      - `name` (string) [maxLen=50, nullable] — Represents the name of the after action associated with the after actions of the transition.
      - `details` (object `TransitionAfterActionDetails`) — This denotes the details of the actions configured of the transition to be created.
        schema: `TransitionAfterActionDetails`
        - `overwrite` (boolean) [nullable] — Indicates whether the tags configured in the after actions of the transition overwrite the existing tags on the record. Possible values: **true**, **false**.
        - `module` (object `RelatedListModuleReference`) — module data associated in after actions of transitions
        - `tags` (array of object `TransitionAfterActionTag`) [maxItems=2, nullable] — Contains the tags applied to the record as part of the after actions of the transition.
          schema: `TransitionAfterActionTag`
          - `color` (string) [maxLen=100, nullable] — Represents the color of the tag associated with the after actions of the transition.
          - `name` (string) [maxLen=7, nullable] — Represents the name of the tag associated with the after actions of the transition.
      - `id` (string/int64) [maxLen=19, minLen=1, pattern=[0-9]+, nullable] — Represents the unique ID of the after action associated with the transition.
      - `type` (string) **REQ** [enum=[13 values]] — Represents the type of the after action associated with the transition. Possible values: **field_updates**, **tasks**, **functions**, **email_notifications**, **webhooks**, **add_tags**, **remove_tags**, **sms**, **whatsapp**, **create_record**, **add_meeting**, **schedule_call**, **convert**.
    - `color_code` (string) [maxLen=1000, nullable] — Represents the color code of the transition button to be created. Example: #F27E22.

**Responses:**

- **201**: Returns the result of the successfully created Blueprint transition. — Schema: `BlueprintTransitionsCreateResponse` [application/json]
    > Represents the response returned upon successful creation of transitions, containing the per-transition operation results.
    schema: `BlueprintTransitionsCreateResponse`
    - `transitions` (array of object `TransitionOperationResult`) [maxItems=100] — Contains the creation result of each blueprint transition submitted in the bulk create request.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a multi-status response. Each item in the array independently indicates success or failure for the corresponding transition in the request. — Schema: `PostTransitionsMultiStatusResponse` [application/json]
    > Represents the 207 Multi-Status response returned by POST /settings/blueprints/transitions when a batch of transitions is submitted and some succeed while others fail. Each element in the transitions array is either a success item or one of the known error types.
    schema: `PostTransitionsMultiStatusResponse`
    - `transitions` (array of object) [maxItems=50] **REQ** — Contains the result of each transition in the request. Each item is either a success result or an error result.
      oneOf:
        - `TransitionOperationResult` — Represents the outcome of processing an individual transition, including the status, code, message, and optional details.
        - `TransitionTypeInvalidValueError` — Represents the error payload returned when the provided transition type value is invalid, including the API name and JSON path of the field and the values it supports.
        - `InvalidEscalationPeriodError` — Represents the error returned when the period value provided in the escalation settings is invalid. The error code is **INVALID_DATA**.
        - `ModuleApiNameInvalidError` — Represents the validation error returned when the provided module API name is invalid. Possible values for code: **INVALID_DATA**.
        - `TransitionsFieldInvalidTypeError` — Represents the validation error returned when the transitions property in the request contains a field with an invalid data type. The response carries the error code **INVALID_DATA** along with field-level validation details.
        - `TransitionModuleMissingError` — Represents the validation error returned when the required module field is missing in the transition request, identified by the error code **MANDATORY_NOT_FOUND**.
        - `TransitionActionsAmbiguityError` — Represents the error returned when ambiguous or conflicting after-action data is detected in the transition (code: AMBIGUITY_DURING_PROCESSING).
        - `TransitionActionTypeUnsupportedError` — Represents the validation error returned when the specified transition action type is not supported, with the error code INVALID_DATA.
        - `ChecklistTitleLengthExceededError` — Represents the validation error returned when a checklist title in a blueprint transition exceeds the maximum allowed length. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details, including the maximum number of characters allowed for the checklist title.
        - `ChecklistItemsLimitExceededError` — Represents the validation error returned when the number of checklist items provided for a checklist field in a blueprint transition exceeds the permitted limit. Contains the error code **DEPENDENT_MISMATCH**, the error message, the response status, and field-level error details, including the maximum permitted number of checklist items.
        - `ChecklistOptionLengthExceededError` — Represents the validation error returned when the name of a checklist option in a blueprint transition exceeds the allowed character limit. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details, including the maximum number of characters allowed for a checklist option.
        - `InvalidValueResponse` — Represents the error response returned when invalid module data is provided during a reorder request. The response includes the error code **INVALID_DATA**, a descriptive message, a status, and validation details.
        - `ModuleIdentifierAmbiguityError` — Represents the processing error returned when ambiguity is detected between the module ID and API name while creating a transition. Possible values for code: **AMBIGUITY_DURING_PROCESSING**.
        - `DuringFieldIdInvalidError` — Represents the validation error returned when the provided during field ID is invalid, including the error code, message, status, and details of the field whose ID is invalid.
        - `DuringInputTypeDuplicateError` — Represents the validation error returned when a during-input type is duplicated within the same transition (code: DUPLICATE_DATA).
        - `DuringFieldIdDuplicateError` — Represents the validation error returned when a duplicate during field ID is present in the transition, including the error code, message, status, and details of the field that is already present.
        - `DuringInputsWidgetAmbiguityError` — Represents the error returned when during-input fields are configured along with a widget or kiosk, causing an ambiguity during processing (error code **AMBIGUITY_DURING_PROCESSING**).
        - `RequiredFieldMissingError` — Represents the validation error returned when a required field is missing in the request, with the error code MANDATORY_NOT_FOUND.
        - `InvalidDataTypeError` — Represents a validation error returned when one or more request fields contain a value with an invalid data type. The error code is **INVALID_DATA**.
        - `InvalidDataError` — Represents a general validation error returned when the request data is invalid. The error code is **INVALID_DATA**.
        - `InvalidDataValidationError` — Represents a validation error returned for generic invalid data conditions during transition processing. The error code is **INVALID_DATA**.
        - `BlueprintTransitionInvalidDataErrorResponse` — Represents the standardized 400 error payload returned by the Blueprint Transitions API when a transition configuration contains invalid input, such as an invalid sequence number in during inputs. Includes the error status, a stable error code (INVALID_DATA), an error message, and validation details describing the offending fields.
        - `PipelineCannotBeEmptyErrorResponse` — Represents the error returned when pipeline details are not provided for a pipeline-enabled module during transition creation (error code: INVALID_DATA).
        - `TransitionDuringFieldsLimitExceededError` — Represents the error returned when the number of fields configured in the during input of a blueprint transition exceeds the permitted limit.
        - `CriteriaNotSupportedForFieldError` — Represents the error response returned when criteria are not supported for the specified field, including the error code, message, status, and field-level details.
        - `CriteriaFieldApiNameInvalidError` — Represents the validation error returned when the API name of a criteria field in a blueprint transition is invalid. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details identifying the invalid criteria field.
        - `DuringInputsNotAllowedAutomaticError` — Represents the error returned when during inputs are provided for an automatic transition, which is not allowed (code: NOT_ALLOWED).
        - `DuringInputsNotAllowedParallelError` — Represents the error returned when during inputs are provided for a parallel transition, which is not allowed (error code **NOT_ALLOWED**).
        - `ActionNotSupportedForModuleError` — Represents the validation error returned when the specified action type is not supported for the given module (code: INVALID_DATA).
        - `DuringInputFieldIdInvalidDataError` — Represents the validation error returned when the ID of a during-input field is invalid (code: INVALID_DATA).
        - `ActionLimitExceedsError` — Represents the validation error returned when the configured action count exceeds the permitted limit for the action type (code: INVALID_DATA).
        - `ParallelTransitionIdInvalidError` — Represents the error returned when the specified parallel_transition ID is not associated with any blueprint (error code: INVALID_DATA).
        - `ParallelTransitionDependentFieldMissingError` — Represents the error returned when the parallel_transition field is missing while its dependee field, transition_type, is present (error code: DEPENDENT_FIELD_MISSING).
        - `ParallelTransitionMandatoryNotFoundError` — Represents the error returned when a required field within parallel_transition is missing from the request (error code: MANDATORY_NOT_FOUND).
        - `ActionNotBelongingToModuleError` — Represents the error returned when the specified action does not belong to the current module of the transition (code: INVALID_DATA).
        - `TeamUserNotAllowedForOrgModule` — Represents the error returned when a team or team-profile user is configured as a transition owner for an organization module, with the error code NOT_ALLOWED.
        - `KioskIdInvalidError` — Represents the validation error returned when the kiosk ID provided in during_inputs is invalid or inactive. Possible values for code: **INVALID_DATA**.
        - `InvalidWidgetError` — Represents a validation error returned when the widget provided in during_inputs is invalid. The error code is **INVALID_DATA**.
        - `AutomaticTransitionOwnersNotAllowedError` — Represents the error returned when owners are added to an automatic transition, which is not allowed. Possible values: **NOT_ALLOWED**.
        - `ChildParallelTransitionActionsNotAllowedError` — Represents the error returned when after actions are added to a child parallel transition, which is not allowed. Contains the error code **NOT_ALLOWED**, the error message, the response status, and details identifying the disallowed field in the request.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed because one or more transitions in the request contain invalid data.
**Resolution:** The user must correct the invalid values in the **transitions** array and resend the request. [application/json]
    > Represents the error response returned when one or more transitions in the request fail validation.
    oneOf:
      - `TransitionModuleMissingError` — Represents the validation error returned when the required module field is missing in the transition request, identified by the error code **MANDATORY_NOT_FOUND**.
      - `TransitionsFieldInvalidTypeError` — Represents the validation error returned when the transitions property in the request contains a field with an invalid data type. The response carries the error code **INVALID_DATA** along with field-level validation details.
      - `TransitionTypeInvalidError` — Represents the validation error returned when the provided transition_type value is invalid, including the API name and JSON path of the field and its supported values. Possible values: **INVALID_DATA**.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the transition type is invalid. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Contains the error details object with field-level validation information.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation error.
          - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the validation error.
          - `supported_values` (array of string) [maxItems=25] **REQ** — Contains the supported values for the field that caused the validation error.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned in the response. Possible values: **invalid data**.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
        - `transitions` (array of object) [maxItems=25] **REQ** — Represents an array of error objects. Each object provides the error details for a transition in the request.
          oneOf:
            - `TransitionTypeInvalidValueError` — Represents the error payload returned when the provided transition type value is invalid, including the API name and JSON path of the field and the values it supports.
            - `InvalidEscalationPeriodError` — Represents the error returned when the period value provided in the escalation settings is invalid. The error code is **INVALID_DATA**.
            - `ModuleApiNameInvalidError` — Represents the validation error returned when the provided module API name is invalid. Possible values for code: **INVALID_DATA**.
            - `TransitionsFieldInvalidTypeError` — Represents the validation error returned when the transitions property in the request contains a field with an invalid data type. The response carries the error code **INVALID_DATA** along with field-level validation details.
            - `TransitionModuleMissingError` — Represents the validation error returned when the required module field is missing in the transition request, identified by the error code **MANDATORY_NOT_FOUND**.
            - `TransitionActionsAmbiguityError` — Represents the error returned when ambiguous or conflicting after-action data is detected in the transition (code: AMBIGUITY_DURING_PROCESSING).
            - `TransitionActionTypeUnsupportedError` — Represents the validation error returned when the specified transition action type is not supported, with the error code INVALID_DATA.
            - `ChecklistTitleLengthExceededError` — Represents the validation error returned when a checklist title in a blueprint transition exceeds the maximum allowed length. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details, including the maximum number of characters allowed for the checklist title.
            - `ChecklistItemsLimitExceededError` — Represents the validation error returned when the number of checklist items provided for a checklist field in a blueprint transition exceeds the permitted limit. Contains the error code **DEPENDENT_MISMATCH**, the error message, the response status, and field-level error details, including the maximum permitted number of checklist items.
            - `ChecklistOptionLengthExceededError` — Represents the validation error returned when the name of a checklist option in a blueprint transition exceeds the allowed character limit. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details, including the maximum number of characters allowed for a checklist option.
            - `InvalidValueResponse` — Represents the error response returned when invalid module data is provided during a reorder request. The response includes the error code **INVALID_DATA**, a descriptive message, a status, and validation details.
            - `ModuleIdentifierAmbiguityError` — Represents the processing error returned when ambiguity is detected between the module ID and API name while creating a transition. Possible values for code: **AMBIGUITY_DURING_PROCESSING**.
            - `DuringFieldIdInvalidError` — Represents the validation error returned when the provided during field ID is invalid, including the error code, message, status, and details of the field whose ID is invalid.
            - `DuringInputTypeDuplicateError` — Represents the validation error returned when a during-input type is duplicated within the same transition (code: DUPLICATE_DATA).
            - `DuringFieldIdDuplicateError` — Represents the validation error returned when a duplicate during field ID is present in the transition, including the error code, message, status, and details of the field that is already present.
            - `DuringInputsWidgetAmbiguityError` — Represents the error returned when during-input fields are configured along with a widget or kiosk, causing an ambiguity during processing (error code **AMBIGUITY_DURING_PROCESSING**).
            - `RequiredFieldMissingError` — Represents the validation error returned when a required field is missing in the request, with the error code MANDATORY_NOT_FOUND.
            - `InvalidDataTypeError` — Represents a validation error returned when one or more request fields contain a value with an invalid data type. The error code is **INVALID_DATA**.
            - `InvalidDataError` — Represents a general validation error returned when the request data is invalid. The error code is **INVALID_DATA**.
            - `InvalidDataValidationError` — Represents a validation error returned for generic invalid data conditions during transition processing. The error code is **INVALID_DATA**.
            - `BlueprintTransitionInvalidDataErrorResponse` — Represents the standardized 400 error payload returned by the Blueprint Transitions API when a transition configuration contains invalid input, such as an invalid sequence number in during inputs. Includes the error status, a stable error code (INVALID_DATA), an error message, and validation details describing the offending fields.
            - `PipelineCannotBeEmptyErrorResponse` — Represents the error returned when pipeline details are not provided for a pipeline-enabled module during transition creation (error code: INVALID_DATA).
            - `TransitionDuringFieldsLimitExceededError` — Represents the error returned when the number of fields configured in the during input of a blueprint transition exceeds the permitted limit.
            - `CriteriaNotSupportedForFieldError` — Represents the error response returned when criteria are not supported for the specified field, including the error code, message, status, and field-level details.
            - `CriteriaFieldApiNameInvalidError` — Represents the validation error returned when the API name of a criteria field in a blueprint transition is invalid. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details identifying the invalid criteria field.
            - `DuringInputsNotAllowedAutomaticError` — Represents the error returned when during inputs are provided for an automatic transition, which is not allowed (code: NOT_ALLOWED).
            - `DuringInputsNotAllowedParallelError` — Represents the error returned when during inputs are provided for a parallel transition, which is not allowed (error code **NOT_ALLOWED**).
            - `ActionNotSupportedForModuleError` — Represents the validation error returned when the specified action type is not supported for the given module (code: INVALID_DATA).
            - `DuringInputFieldIdInvalidDataError` — Represents the validation error returned when the ID of a during-input field is invalid (code: INVALID_DATA).
            - `ActionLimitExceedsError` — Represents the validation error returned when the configured action count exceeds the permitted limit for the action type (code: INVALID_DATA).
            - `ParallelTransitionIdInvalidError` — Represents the error returned when the specified parallel_transition ID is not associated with any blueprint (error code: INVALID_DATA).
            - `ParallelTransitionDependentFieldMissingError` — Represents the error returned when the parallel_transition field is missing while its dependee field, transition_type, is present (error code: DEPENDENT_FIELD_MISSING).
            - `ParallelTransitionMandatoryNotFoundError` — Represents the error returned when a required field within parallel_transition is missing from the request (error code: MANDATORY_NOT_FOUND).
            - `ActionNotBelongingToModuleError` — Represents the error returned when the specified action does not belong to the current module of the transition (code: INVALID_DATA).
            - `TeamUserNotAllowedForOrgModule` — Represents the error returned when a team or team-profile user is configured as a transition owner for an organization module, with the error code NOT_ALLOWED.
            - `KioskIdInvalidError` — Represents the validation error returned when the kiosk ID provided in during_inputs is invalid or inactive. Possible values for code: **INVALID_DATA**.
            - `InvalidWidgetError` — Represents a validation error returned when the widget provided in during_inputs is invalid. The error code is **INVALID_DATA**.
            - `AutomaticTransitionOwnersNotAllowedError` — Represents the error returned when owners are added to an automatic transition, which is not allowed. Possible values: **NOT_ALLOWED**.
            - `ChildParallelTransitionActionsNotAllowedError` — Represents the error returned when after actions are added to a child parallel transition, which is not allowed. Contains the error code **NOT_ALLOWED**, the error message, the response status, and details identifying the disallowed field in the request.
            - `ConvertActionCombinationAmbiguityError` — Represents the processing error returned when a convert action is combined with incompatible action types (field_update, tasks, create_tags, or remove_tags) in the same blueprint transition. Contains the error code **AMBIGUITY_DURING_PROCESSING**, the error message, the response status, and details listing the conflicting field paths that caused the ambiguity.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code returned when a convert action is combined with conflicting actions. Possible values: **AMBIGUITY_DURING_PROCESSING**.
              - `details` (object) **REQ** — Contains the error details, including the conflicting field paths that caused the ambiguity.
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Contains the list of fields that caused the ambiguity during processing.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the conflicting field.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the conflicting field.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when the convert action cannot be combined with conflicting actions. Possible values: **convert action cannot be combined with field_update, tasks, create_tags or remove_tags actions for module**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The user does not have permission to create Blueprint transitions.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
    > Represents the error returned when the user does not have the permission required to perform the action. Possible values for code: **NO_PERMISSION**.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the required permission is missing. Possible values: **NO_PERMISSION**.
    - `details` (object) **REQ** — Contains the error details with the list of missing permissions.
      - `permissions` (array of string) [maxItems=25] **REQ** — Contains the list of permissions required to perform the operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message returned when access is denied due to missing permissions. Possible values: **permission denied**.
    - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.transitions.CREATE
