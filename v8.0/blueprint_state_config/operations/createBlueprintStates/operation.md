# POST /settings/blueprints/{blueprintId}/states
**Operation:** `createBlueprintStates` — Create Blueprint States
> To create one or more states for a Blueprint in your Zoho CRM organization.

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Specify the [unique ID of the Blueprint](blueprints.yaml#$.paths./settings/blueprints.get) for which you want to create states.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Specify the Zoho service context for the request. Possible values: **automation** - Targets the automation service.

**Schemas:**
`AutomationActionReferenceUpdateAlternative`:
  > Details of each action configured (Required)
  - `name` (string) [maxLen=100, nullable] — The name of the action configured for the automation trigger.
  - `id` (string) [maxLen=255, pattern=[0-9]+] — The unique identifier of the automation action configured for the trigger.
  additionalProperties: any
`DuplicateStatePicklistError`:
  > Error returned when the provided picklist value is already present.
  - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Error code
  - `details` (object) **REQ** — The error details containing the API name and JSON path of the duplicate picklist state that caused the validation failure.
    - `api_name` (string) **REQ** [maxLen=255] — The API name of the picklist field for which the duplicate state error occurred.
    - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the duplicate picklist field that caused the error.
  - `message` (string) **REQ** [enum=[1 values]] — The error message returned when a duplicate picklist value is detected in the Blueprint. Possible values: There is already a state with the same pick list value used in the blueprint - Indicates that another state in the Blueprint already uses the same picklist value.
  - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates the request resulted in an error.
`InvalidStateIDsError`:
  > Represents the error response returned when one or more of the provided state IDs are invalid.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
  - `details` (object) **REQ** — Represents the details of the validation error, containing an object with the affected record **id**.
    - `id` (string) **REQ** [maxLen=255] — Represents the ID of the invalid state that caused the error.
  - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when an invalid state ID is provided. Possible values: the id given seems to be invalid - The supplied state ID does not correspond to a valid state in Zoho CRM.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
`InvalidValueResponse`:
  > The error response returned when invalid data is provided in a request. Contains the error **code**, **status**, **message**, and validation **details**.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code returned when the request contains invalid data. Possible values: **INVALID_DATA** - The request was rejected because one or more submitted values are invalid.
  - `details` (object) **REQ** — An object containing additional details about the validation error, including the **api_name** and **json_path** of the field that caused the error.
    - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that contains the invalid value.
    - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field in the request body that contains the invalid value.
  - `message` (string) **REQ** [enum=[4 values]] — The error message describing the invalid value encountered. Possible values: the id given seems to be invalid - The provided ID does not match a valid record. the value given is invalid - The supplied field value is not accepted. invalid data - The request contains data that failed validation. Invalid data - The request contains data that failed validation.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
`StateOperationResultItem`:
  > The result of a state operation, including status, code, message, and per-item details.
  - `code` (string) [maxLen=255, enum=['SUCCESS']] — The result code for the operation. Possible values: **SUCCESS** - The operation completed successfully.
  - `details` (object `AutomationActionReferenceUpdateAlternative`) — An automation action reference used in update operations, identified by its **id** and an optional **name**.
  - `message` (string) [maxLen=255] — The message returned for the state operation result.
  - `status` (string) [maxLen=255] — The outcome status of the state operation for the corresponding item.

**Request Body** — application/json `BlueprintStateBatchCreateRequest`
> The request body must contain a **states** array with one object.
  > The batch request payload for creating multiple Blueprint states, containing a **states** array with the state definitions to be created.
  - `states` (array of object `BlueprintStateCreateEntry`) [minItems=1, maxItems=300] **REQ** — The list of Blueprint state objects to be included in the batch create request.
    schema: `BlueprintStateCreateEntry`
    - `process_id` (string) [maxLen=25, pattern=[0-9]+, nullable] — The ID of the Blueprint for which the state is to be created.
    - `state_escalation` (object `StateEscalationPolicyUpdateAlternative`) — Contains details of the state escalation alerts to be configured for the particular state
      schema: `StateEscalationPolicyUpdateAlternative`
      - `period` (string) **REQ** [maxLen=50, enum=['days', 'hours', 'minutes', 'business_days', 'business_hours']] — The time unit for the escalation period. Possible values: **days** - The period is measured in calendar days. **hours** - The period is measured in hours. **minutes** - The period is measured in minutes. **business_days** - The period is measured in business days. **business_hours** - The period is measured in business hours.
      - `value` (integer/int32) **REQ** — The maximum time, in the configured unit, for which a record can remain in the state before escalation.
      - `trigger_details` (array of object `EscalationTriggerConfigurationUpdateAlternative`) [maxItems=3] **REQ** — The list of trigger configurations defined for the state escalation alert.
        schema: `EscalationTriggerConfigurationUpdateAlternative`
        - `period` (string) **REQ** [maxLen=50, enum=['days', 'hours', 'minutes', 'business_days', 'business_hours']] — Represents the unit of time for the escalation trigger period. Possible values: **days** - The period is measured in calendar days. **hours** - The period is measured in hours. **minutes** - The period is measured in minutes. **business_days** - The period is measured in business days. **business_hours** - The period is measured in business hours.
        - `execute_type` (string) **REQ** [maxLen=7, enum=['before', 'on', 'after']] — Represents the execution timing that determines when the escalation actions are triggered. Possible values: **before** - Actions are triggered before the specified escalation event. **on** - Actions are triggered at the time of the specified escalation event. **after** - Actions are triggered after the specified escalation event.
        - `value` (integer/int32) **REQ** — Represents the maximum time duration, in integer units, for which a record can remain in the current state before the escalation is triggered.
        - `actions` (array of object) [maxItems=5] **REQ** — The list of actions configured to trigger during a state escalation alert for the specified execution type.
          oneOf:
            - `EscalationActionSLA` — Represents an escalation action of the SLA type, containing the action type and recipient details for the escalation.
              - `type` (string) **REQ** [maxLen=20, enum=['sla']] — The type of escalation action configured. Possible values: **sla** - Indicates the action is of the SLA escalation type.
              - `details` (object) **REQ** — Represents the details of the SLA escalation action, including the **name** and **escalate_to** recipients.
                - `name` (string) [maxLen=100, nullable] — The name of the SLA escalation action.
                - `escalate_to` (array of object) [maxItems=1] — The list of recipients to whom the SLA escalation is directed.
                  - `type` (string) **REQ** [maxLen=255, enum=['user', 'role', 'group', 'team_user', 'profile']] — The type of recipient to escalate to. Possible values: **user** - A specific CRM user. **role** - A CRM role. **group** - A CRM user group. **team_user** - A member of a team. **profile** - A CRM profile.
                  - `id` (string) **REQ** [maxLen=255] — The unique ID of the escalation recipient.
                additionalProperties: any
              additionalProperties: any
            - `EscalationActionConfigurationUpdateAlternative` — Represents an alternative configuration for an escalation action used during update operations, containing the action **type** and associated **details**.
              - `type` (string) **REQ** [maxLen=20, enum=['circuits', 'whatsapp', 'sms']] — Represents the type of escalation action configured. Possible values: **circuits** - Escalation action delivered through circuits. **whatsapp** - Escalation action delivered through WhatsApp. **sms** - Escalation action delivered through SMS.
              - `details` (object `AutomationActionReferenceUpdateAlternative`) **REQ** — Details of each action configured (Required)
              additionalProperties: any
            - `EscalationActionEmailNotification` — An escalation action of the email notification type, containing the action **type** and its associated **details**.
              - `type` (string) **REQ** [maxLen=20, enum=['email_notifications']] — The type of escalation action. Possible values: **email_notifications** - Indicates that the escalation action sends an email notification.
              - `details` (object) **REQ** — The details of the action configured for the email notification, including the **name** and **id** of the associated entity.
                - `name` (string) [maxLen=100, nullable] — The name of the action configured for the escalation trigger.
                - `id` (string) [maxLen=255, pattern=[0-9]+] — The unique identifier of the automation action configured for the escalation trigger.
                additionalProperties: any
              additionalProperties: any
            - `EscalationActionTask` — An escalation action object used during update operations, containing the action type and associated details.
              - `type` (string) **REQ** [maxLen=20, enum=['tasks']] — The type of escalation action. Possible values: **tasks** - Indicates the action is a task.
              - `details` (object) **REQ** — The details of a configured action, including its **name** and **id**.
                - `name` (string) [maxLen=100, nullable] — The name of the action configured for the escalation trigger.
                - `id` (string) [maxLen=255, pattern=[0-9]+] — The unique identifier of the automation action configured for the escalation trigger.
                additionalProperties: any
              additionalProperties: any
            - `EscalationActionFieldUpdate` — An escalation action configuration used during update operations, containing the action type and its associated details.
              - `type` (string) **REQ** [maxLen=20, enum=['field_updates']] — The type of action configured for the escalation rule. Possible values: **field_updates** - Indicates a field update action.
              - `details` (object) **REQ** — The details of the action configured for the escalation rule, including the field **name** and **id** of the target.
                - `name` (string) [maxLen=100, nullable] — The name of the action configured for the escalation trigger.
                - `id` (string) [maxLen=255, pattern=[0-9]+] — The unique identifier of the automation action configured for the escalation trigger.
                additionalProperties: any
              additionalProperties: any
            - `EscalationActionWebhook` — An escalation action of the webhook type, containing the action type and its associated configuration details.
              - `type` (string) **REQ** [maxLen=20, enum=['webhooks']] — The action type for the escalation configuration. Possible values: **webhooks** - Indicates the action is a webhook notification.
              - `details` (object) **REQ** — The details of the action configured for the escalation, including the action's **name** and **id**.
                - `name` (string) [maxLen=100, nullable] — The name of the action configured for the escalation trigger.
                - `id` (string/int64) [maxLen=255, minLen=1, pattern=[0-9]+] — The unique ID of the automation action configured for the escalation trigger.
                additionalProperties: any
              additionalProperties: any
            - `EscalationActionFunction` — An escalation action configuration, containing the action type and its associated details.
              - `type` (string) **REQ** [maxLen=20, enum=['functions']] — The type of action configured for the escalation. Possible values: **functions** - Indicates the action is a function execution.
              - `details` (object) **REQ** — The details of the action configured for the escalation, including its **name** and **id**.
                - `name` (string) [maxLen=100, nullable] — The name of the action configured for the escalation trigger.
                - `id` (string/int64) [maxLen=255, minLen=1, pattern=[0-9]+] — The unique identifier of the automation action configured for the escalation trigger.
                additionalProperties: any
              additionalProperties: any
    - `pick_list_value` (object `StatePicklistValueIdentifier`) **REQ** — Picklist option value for which the state is configured (Required)
      schema: `StatePicklistValueIdentifier`
      - `actual_value` (string) [maxLen=100, nullable] — The stored value of the picklist option, as saved in the CRM record.
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=[0-9]+] — The unique identifier of the picklist option.
    - `module` (object `BlueprintModuleIdentifier`) **REQ** — Module for which the blueprint state is configured  (Required)
      schema: `BlueprintModuleIdentifier`
      - `api_name` (string) [maxLen=200, nullable] — The API name of the module associated with the Blueprint.
      - `id` (string) **REQ** [maxLen=25, pattern=[0-9]+] — The unique identifier of the CRM module associated with the Blueprint.

**Responses:**

- **201**: Returns the details of the newly created Blueprint state. — Schema: `BlueprintStateCreateResponse` [application/json]
    > The response returned after creating one or more Blueprint states, containing the result details for each state in the **states** array.
    schema: `BlueprintStateCreateResponse`
    - `states` (array of object `StateOperationResultItem`) [maxItems=50] — The list of Blueprint states returned in the create response.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a multi-status response where each item in the array independently indicates success or failure for the corresponding Blueprint state in the request. — Schema: `BlueprintStateCreateMultiStatusResponse` [application/json]
    > A multi-status response for Blueprint state creation requests, where each entry in the **states** array independently indicates success or failure for a corresponding state in the request.
    schema: `BlueprintStateCreateMultiStatusResponse`
    - `states` (array of object) [maxItems=25] — The list of per-state creation results, containing both successful entries and error entries for each state processed in the request.
      oneOf:
        - `StateOperationResultItem` — The result of a state operation, including status, code, message, and per-item details.
        - `DuplicateStatePicklistError` — Error returned when the provided picklist value is already present.
        - `InvalidStateIDsError` — Represents the error response returned when one or more of the provided state IDs are invalid.
        - `InvalidValueResponse` — The error response returned when invalid data is provided in a request. Contains the error **code**, **status**, **message**, and validation **details**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax. **Resolution:** The request body must be reviewed to ensure it contains valid syntax and all required fields. [application/json]
    oneOf:
        - `states` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `MissingActionIDError` — Represents the error returned when a required action ID is absent from state escalation trigger details.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code indicating a mandatory field or value is missing. Possible values: **MANDATORY_NOT_FOUND** - The required action ID was not provided in the request.
              - `details` (object) **REQ** — Represents the details of the validation error, containing the **api_name** and **json_path** of the field for which the action ID is missing.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the action for which the action ID is missing.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request payload for which the action ID is missing.
              - `message` (string) **REQ** [enum=['The required data missing']] — Represents the error message returned when required data is missing. Possible values: The required data missing - Indicates that one or more required fields or parameters were absent in the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
            - `InvalidTriggerTimeError` — Represents the error returned when a trigger time violates SLA constraints.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Represents an object containing additional error context for the invalid trigger time. Contains the **api_name** and **json_path** of the field that caused the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field or parameter associated with the invalid trigger time error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field that contains the invalid trigger time value.
              - `message` (string) **REQ** [enum=["Trigger time should be less than SLA time when execute_type is 'before'"]] — The error message describing the invalid trigger time condition. Possible values: Trigger time should be less than SLA time when execute_type is 'before' - The specified trigger time exceeds the SLA time for a **before** execution type.
              - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates the request resulted in an error.
            - `ErrorResponseCore9` — The error response returned when the transition type provided in the request is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code returned by the API. Possible values: **INVALID_DATA** - The request contains invalid data.
              - `details` (object) **REQ** — An object containing additional context about the error, including the **api_name**, **json_path**, and **supported_values** of the field that caused the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field or parameter that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field in the request that caused the error.
                - `supported_values` (array of string) [maxItems=25] **REQ** — The list of accepted values for the field or parameter that triggered the error.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['the value given is invalid']] — Represents the error message describing the issue. Possible values: the value given is invalid - The request was rejected because an invalid value was provided.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates that the request resulted in an error.
            - `ErrorResponseCore25` — The error response returned when the Blueprint name is missing from the request. Contains the error **code**, **status**, **message**, and **details** properties.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — The error code returned by the server. Possible values: MANDATORY_NOT_FOUND - A required parameter or field is missing from the request.
              - `details` (object) **REQ** — The details of the validation error, including the affected field and its location in the request.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field or parameter associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the specific field in the request payload that caused the error.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the issue. Possible values: required field not found - The request is missing a required field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates that the request resulted in an error.
            - `InvalidEscalationPeriodError` — Error returned when the provided period value in escalation settings is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the escalation period data is invalid. Possible values: **INVALID_DATA** - The escalation period value provided in the request is not valid.
              - `details` (object) **REQ** — Represents the error details for an invalid escalation period, containing the affected field's API name, JSON path, and supported values.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or parameter that contains the invalid escalation period value.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field in the request body that caused the invalid escalation period error.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of valid escalation period values supported by the operation.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned when the escalation period value is invalid. Possible values: invalid data - The provided escalation period data does not meet the required format or constraints.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates that the request resulted in an error.
            - `ErrorResponseCore1` — An error response returned when a request fails due to an invalid core parameter, such as an incorrect module API name associated with a Blueprint. Contains the error **code**, **status**, **message**, and **details** properties.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code returned when the request contains invalid data. Possible values: **INVALID_DATA** - The request data is invalid.
              - `details` (object) **REQ** — An object containing additional context about the error, including the **api_name** and **json_path** of the field that caused the issue.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field or parameter that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the specific field in the request payload that caused the error.
              - `message` (string) **REQ** [enum=['the tabName given seems to be invalid']] — The error message describing the issue encountered during the request. Possible values: the tabName given seems to be invalid - The specified tab name is not recognized as a valid module name.
              - `status` (string) **REQ** [enum=['error']] — The status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `ErrorResponseCore13` — Represents the error response returned when the Blueprint ID provided in the request is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by the server. Possible values: **INVALID_DATA** - The request contains invalid data.
              - `details` (object) **REQ** — Represents an object containing additional context about the error, including the **api_name** and **json_path** of the field that caused the issue.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or parameter associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['the value given seems to be invalid']] — Represents the error message describing the issue encountered. Possible values: the value given seems to be invalid - The value provided in the request is not valid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `ErrorResponseCore28` — Represents the error response returned when the specified criteria update is invalid, containing the error code, status, message, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by the API. Possible values: **INVALID_DATA** - The request contains invalid data.
              - `details` (object) **REQ** — Represents additional details about the error, including the expected data type, the API name of the field that caused the error, and the JSON path to the invalid value.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or parameter associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the specific field in the request that caused the error.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the issue. Possible values: **invalid data** - The request contains invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates that the request resulted in an error.
            - `StateCreationLimitExceededError` — Error indicating the maximum allowed number of states for the blueprint has been reached.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code for this error condition. Possible values: **LIMIT_EXCEEDED** - The allowed creation limit has been exceeded.
              - `details` (object) **REQ** — Represents the error details for the limit exceeded condition, containing the **api_name** and **limit** fields that identify the affected resource and the maximum allowed value.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the resource associated with the state creation limit exceeded error.
                - `limit` (integer/int32) **REQ** — Represents the maximum number of states allowed.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the issue. Possible values: invalid data - The request contains invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `ErrorResponseCore2` — Represents the error response body returned when request data fails validation, containing the error **code**, **status**, **message**, and **details** fields.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by the server. Possible values: **INVALID_DATA** - The request contains invalid data.
              - `details` (object) **REQ** — Represents the details of the validation error, including the expected data type, the API name of the field, and the JSON path of the invalid value.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or parameter associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the specific field in the request payload that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message describing the nature of the failure. Possible values: Invalid data type - The value provided does not match the expected data type for the field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `ErrorResponseCore6` — Represents the error response body returned when the request contains invalid data, including the error **code**, **status**, **message**, and **details** properties.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by the API. Possible values: **INVALID_DATA** - The request contains invalid data.
              - `details` (object) **REQ** — Represents an object containing additional error details, including the **maximum_length**, **api_name**, and **json_path** of the field that failed validation.
                - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for the field that triggered the validation error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or parameter associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the request field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data']] — The error message describing the issue. Possible values: **Invalid data** - The request contains invalid data.
              - `status` (string) **REQ** [enum=['error']] — The status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `ErrorResponseCore26` — Represents the error response returned when the request contains invalid data, including a status code, error code, message, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by the API. Possible values: **INVALID_DATA** - The request contains invalid data.
              - `details` (object) **REQ** — Represents an object containing additional context about the error, including the **regex**, **api_name**, and **json_path** of the field that caused the validation failure.
                - `regex` (string) **REQ** [maxLen=255] — Represents the regular expression pattern associated with the error detail.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or parameter that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the request field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message describing the issue. Possible values: **Invalid data** - The request contains invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `ErrorResponseCore4` — Represents the error response returned when a mandatory request parameter or field is missing.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned by the API. Possible values: **MANDATORY_NOT_FOUND** - A required field or parameter is missing from the request.
              - `details` (object) **REQ** — Represents an object containing additional error context, including the **api_name** and **json_path** of the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or parameter associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message describing the issue. Possible values: Required field is missing - A mandatory field was not included in the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `ErrorResponseCore21` — Represents the error response body returned when the request contains invalid data. The schema includes the **code**, **status**, **message**, and **details** properties that describe the specific validation failure.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by the API. Possible values: **INVALID_DATA** - The request contains invalid data.
              - `details` (object) **REQ** — Represents an object containing additional error context, including the **api_name**, **json_path**, and **supported_values** of the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field or parameter associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field in the request that caused the error.
                - `supported_values` (array of string) [maxItems=25] **REQ** — The list of supported values for the field or parameter that caused the error.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — The error message describing the issue. Possible values: Invalid data - The request contains data that failed validation.
              - `status` (string) **REQ** [enum=['error']] — The status of the response. Possible values: **error** - Indicates that the request resulted in an error.
            - `InvalidValueResponse` — The error response returned when invalid data is provided in a request. Contains the error **code**, **status**, **message**, and validation **details**.
            - `ModuleIdVsApiNameAmbiguityError` — An error response returned when a request value matches both a module ID and a module API name, creating an ambiguity that the server cannot resolve.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — The error code returned when an ambiguity is encountered during processing. Possible values: **AMBIGUITY_DURING_PROCESSING** - The request could not be completed because an ambiguity was detected during processing.
              - `details` (object) **REQ** — The details of the ambiguity error, including information about the source of the conflict.
                - `ambiguity_due_to` (array of object) [maxItems=2] **REQ** — The list of fields that caused the ambiguity between the module ID and the API name.
                  - `api_name` (string) **REQ** [maxLen=255] — The API name of the module that contributes to the ambiguity.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the module ID versus API name ambiguity.
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message returned when the request cannot be processed due to ambiguity. Possible values: Ambiguity while processing the request - The request contains ambiguous module identification that cannot be resolved.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates that the request resulted in an error.
            - `DuplicateStatePicklistError` — Error returned when the provided picklist value is already present.
            - `TriggerDetailsLimitExceededError` — The error response returned when the **trigger_details** array exceeds the maximum allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — The details of the limit-exceeded error, including the **maximum_length**, **api_name**, and **json_path** of the field that triggered the violation.
                - `maximum_length` (integer/int32) **REQ** — The maximum number of detail entries permitted in the request.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the resource associated with the trigger details limit exceeded error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field or parameter that caused the trigger details limit exceeded error.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the issue. Possible values: **invalid data** - The request contains invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates that the request resulted in an error.
            - `SLAMinimumValueError` — Error returned when the SLA value is less than the required minimum of 15 minutes.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation failure. Possible values: **INVALID_DATA** - The submitted data does not meet the required validation criteria.
              - `details` (object) **REQ** — An object containing additional details about the validation error, including the **api_name** and **json_path** of the field that failed validation.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that triggered the SLA minimum value error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field in the request payload that failed the SLA minimum value validation.
              - `message` (string) **REQ** [enum=['SLA need to be at least 15 Minutes']] — The error message returned when the SLA duration does not meet the minimum threshold. Possible values: SLA need to be at least 15 Minutes - The configured SLA duration is below the minimum allowed value of 15 minutes.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates that the request resulted in an error.
            - `BlueprintStateLimitExceededError` — Error returned when the Blueprint state count exceeds the allowed limit.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — The error code returned when a Blueprint state limit is exceeded. Possible values: **LIMIT_EXCEEDED** - The request exceeded the allowed limit for Blueprint states.
              - `details` (object) **REQ** — An object containing additional details about the Blueprint state limit violation, including the **api_name** and **limit** fields.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field or element associated with the Blueprint state limit exceeded error.
                - `limit` (integer/int32) **REQ** — The maximum number of records allowed for the Blueprint state.
              - `message` (string) **REQ** [enum=['Blueprint state limit exceed']] — The error message returned when the Blueprint state limit is exceeded. Possible values: Blueprint state limit exceed - The maximum number of Blueprint states has been reached for the record.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates that the request resulted in an error.
            - `EscalationActionLimitExceededError` — Error returned when the number of actions in a trigger exceeds the allowed limit.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — The error code for this response. Possible values: **LIMIT_EXCEEDED** - The escalation action limit has been exceeded.
              - `details` (object) **REQ** — Represents the details of the escalation action limit violation, including the action type, API name, configured count, and the limit that was exceeded.
                - `action_type` (string) **REQ** [maxLen=255] — Represents the type of action that exceeded the configured escalation limit.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the escalation action limit exceeded error.
                - `limit` (integer/int32) **REQ** — Represents the maximum number of escalation actions allowed.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the escalation action limit exceeded error.
                - `configured_count` (integer/int32) **REQ** — Represents the number of escalation actions currently configured.
              - `message` (string) **REQ** [enum=['Action Limit Exceeds']] — Represents the error message returned when the escalation action limit is exceeded. Possible values: Action Limit Exceeds - Indicates that the number of allowed escalation actions has been exceeded.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `DraftVersionRequiredError` — The error returned when an operation requires a Blueprint to be in draft state, but the Blueprint is not currently in draft state.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Additional details about the error, providing context beyond the primary error message.
              - `message` (string) **REQ** [enum=['Unable to edit, please create a draft version to edit the blueprint.']] — The error message returned when a draft version is required before editing the Blueprint. Possible values: Unable to edit, please create a draft version to edit the blueprint. - Indicates that a draft version must be created before editing the Blueprint.
              - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates the request resulted in an error.
            - `ActionNotBelongToModuleError` — Error returned when the referenced action does not belong to the current module of the blueprint.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the requested action does not belong to the specified module. Possible values: **INVALID_DATA** - The action does not belong to the specified module.
              - `details` (object) **REQ** — Represents the details of the validation error, identifying the action that does not belong to the specified module. Contains the **api_name** and **json_path** of the invalid action.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['The action does not belong to the current module of the blueprint']] — Represents the error message returned when the requested action does not belong to the current module of the blueprint. Possible values: The action does not belong to the current module of the blueprint - Indicates that the specified action is not valid for the blueprint module in the current context.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
            - `TimeTriggerLimitExceededError` — Error returned when the number of time triggers (trigger_details) in a state escalation exceeds the allowed limit.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — The error code for this error condition. Possible values: **LIMIT_EXCEEDED** - The time-trigger limit has been exceeded.
              - `details` (object) **REQ** — The details of the limit exceeded error, including the API name, the configured count, the limit, and the JSON path associated with the violation.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that triggered the time trigger limit exceeded error.
                - `limit` (integer/int32) **REQ** — The maximum allowed number of time triggers.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
                - `configured_count` (integer/int32) **REQ** — The number of time triggers currently configured in the CRM organization.
              - `message` (string) **REQ** [enum=['Timetrigger Limit Exceeds']] — The error message returned when the time trigger limit is exceeded. Possible values: **Timetrigger Limit Exceeds** - The configured time trigger count has reached the allowed limit.
              - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates that the request resulted in an error.
      - `InvalidResourcePathError` — Represents the error response returned when the specified resource path is invalid or malformed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of invalid resource path error. Possible values: **INVALID_DATA** - The request contains invalid data.
        - `details` (object) **REQ** — Represents the error details for an invalid resource path. Contains a **resource_path_index** object with validation information identifying the invalid path.
          - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index of the path segment in the request URL that is invalid.
        - `message` (string) **REQ** [enum=['the process id given seems to be invalid']] — Represents the error message describing the issue. Possible values: the process id given seems to be invalid - The specified process ID does not correspond to a valid resource path.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
      - `ErrorResponseCore15` — Represents the error response returned when a required header is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_HEADER_MISSING']] — Represents the error code returned when a required header is missing from the request. Possible values: **REQUIRED_HEADER_MISSING** - A required header was not included in the request.
        - `details` (object) **REQ** — Represents an object containing additional details about the error, including information about the specific header or field that caused it.
          - `header_name` (string) **REQ** [maxLen=255] — Represents the name of the HTTP request header associated with the error.
        - `message` (string) **REQ** [enum=['One of the expected headers is missing']] — Represents the error message describing the issue. Possible values: One of the expected headers is missing - A required request header was not included in the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to create states for the specified Blueprint. **Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
    > Represents the error response returned when the requesting user lacks permission to perform the operation.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for a permission failure. Possible values: **NO_PERMISSION** - The requesting user does not have permission to perform this action.
    - `details` (object) **REQ** — Represents error details with permission information.
      - `permissions` (array of string) [maxItems=100] **REQ** — Represents the list of permissions required to perform the requested operation.
        items: [enum=['Crm_Implied_Manage_Workflow']]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message returned when permission is denied. Possible values: permission denied - Indicates that the requesting user does not have the required permission to perform this action.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates that the request was not processed successfully.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.states.CREATE
