# GET /{moduleApiName}/{recordId}/actions/blueprint
**Operation:** `getRecordBlueprintTransition` — Get Blueprint transitions of a record
> To get the next available Blueprint transitions for a record in Zoho CRM, along with the fields available for each transition, the current value of each field, and their validations, if any.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=255]: Specify the API name of the module that contains the record. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `recordId` (path, string, required) [maxLen=255]: Specify the unique ID of the record for which you want to retrieve or execute Blueprint transitions.
- `include_inner_details` (query, boolean, optional): Specify whether to include inner details, such as the column name of the primary field on which the Blueprint is based, inside the **field** object of **process_info**.
Possible values:
true - Includes the inner details in the response.
false - Excludes the inner details from the response.

**Schemas:**
`GETCriteriaDetailsNested`:
  > Represents a criteria group node in the recursive criteria structure of a transition. A group node contains a logical operator and a list of child nodes, where each child is either another nested group or a leaf criterion.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR']] — Represents the logical operator that joins the child nodes of this criteria group.
Possible values:
AND - All child nodes must be satisfied for the group to match.
OR - At least one child node must be satisfied for the group to match.
  - `group` (array of object `GETCriteriaGroupOrCriterionNested`) [maxItems=200] **REQ** — List of child nodes in the criteria group. Each child node is either a nested criteria group or a leaf criterion that compares the value of a field.
    oneOf:
      - `GETCriteriaDetailsNested` — Represents a criteria group node in the recursive criteria structure of a transition. A group node contains a logical operator and a list of child nodes, where each child is either another nested group or a leaf criterion.
      - `GETCriterionNested` — Represents a leaf criterion that compares the value of a field against a target value using a comparator.
        - `comparator` (string) **REQ** [maxLen=50] — Represents the comparison operator applied between the field and the target value, such as equal, not_equal, contains, starts_with, in, or between.
        - `field` (object `GETCriterionFieldNested`) **REQ** — Represents the field reference within a criterion node, identifying the field compared in the criterion by its API name and ID.
          schema: `GETCriterionFieldNested`
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field being compared in the criterion.
          - `id` (string) **REQ** [maxLen=25] — Represents the ID of the field being compared in the criterion.
        - `value` (string) **REQ** [maxLen=4000, nullable] — Represents the target value against which the field is compared. Null for unary comparators such as is_empty.

**Responses:**

- **200**: Returns the next available Blueprint transitions for the record, including the fields available for each transition, the current value of each field, and their validations, if any. — Schema: `GetblueprintResponse200` [application/json]
    > Represents the success response returned for a record's available Blueprint transitions when none of the transitions include during fields.
    schema: `GetblueprintResponse200`
    - `blueprint` (object `GETBlueprintNested`) **REQ** — Represents the Blueprint details of a record, including the transitions currently available in its active Blueprint process.
      schema: `GETBlueprintNested`
      - `process_info` (object `GETProcessInfoNested`) **REQ** — Represents the process information of the Blueprint the record is currently in, including its ID, name, continuity, escalation details, the primary field on which the Blueprint is based, and the field's current value.
        schema: `GETProcessInfoNested`
        - `field_id` (string) **REQ** [maxLen=25] — Primary field ID of which the blueprint is based on.
        - `escalation` (object) **REQ** — Represents the escalation details configured for the Blueprint; null when no escalation is configured.
          oneOf:
            - `GETEscalationNested` — Represents the escalation details for the current Blueprint state, including the number of days configured for the escalation and its status. The value is null when no escalation is configured.
              - `days` (string) **REQ** [maxLen=25] — Represents the number of days configured for the escalation.
              - `status` (string) **REQ** [maxLen=25] — Represents the escalation status of the current Blueprint state.
              type: null — Indicates that no escalation is configured for the Blueprint. The value is always null.
        - `is_continuous` (boolean) — Indicates whether the Blueprint is a continuous Blueprint.
Possible values:
true - The Blueprint is continuous.
false - The Blueprint is not continuous.
        - `api_name` (string) [maxLen=255] — Represents the API name of the primary field on which the Blueprint is based.
        - `continuous` (boolean) **REQ** — Indicates whether the Blueprint is a continuous Blueprint.
Possible values:
true - The Blueprint is continuous.
false - The Blueprint is not continuous.
        - `field_label` (string) **REQ** [maxLen=255] — Denotes the display name of the primary field
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the Blueprint configuration.
        - `column_name` (string) [maxLen=255] — Column name for the primary field
        - `field_value` (string) **REQ** [maxLen=255] — Represents the current value of the Blueprint's primary picklist field.
        - `current_picklist` (object `GETCurrentPicklistNested`) **REQ** — Represents the current state of the Blueprint picklist field for the record, including the value, its ID, and its color code.
          schema: `GETCurrentPicklistNested`
          - `colour_code` (string) **REQ** [maxLen=10, nullable] — Represents the color code of the Blueprint picklist state. Null when no color code is configured for the picklist value.
          - `id` (string) **REQ** [maxLen=25] — Represents the ID of the picklist value.
          - `value` (string) **REQ** [maxLen=255] — Represents the current value of the Blueprint picklist field.
        - `id` (string) **REQ** [maxLen=25] — Represents the ID of the Blueprint the record is currently in.
        - `field_name` (string) **REQ** [maxLen=255] — Field: field_name
      - `transitions` (array of object `GETTransitionsNested`) [maxItems=200] **REQ** — List of transitions currently available for the record in its active Blueprint process. Each transition includes its ID, name, criteria match details, and the fields required to execute it.
        schema: `GETTransitionsNested`
        - `next_transitions` (array of object) [maxItems=200, nullable] — Lists the transitions available to the current user for the record. This key is not present for transitions that are not accessible.
        - `data` (object) — Represents the values of the Blueprint's during fields, including values for fields inside subforms. Not present for non-accessible transitions.
          oneOf:
            - `GETDataNested` (object) — Represents the values of the during fields for a transition. Keys are field API names and values are the field values. For subform during fields, the key is the subform API name and the value is either an array of subform records or an associated module object containing the subform array, such as data.Sales_Order.Ordered_Items.
              type: null — Indicates that the values of the Blueprint's during fields are not included in the response for non-accessible transitions.
        - `type` (string) **REQ** [maxLen=50] — Represents the type of the Blueprint transition.
        - `criteria_message` (string) **REQ** [maxLen=4000, nullable] — Represents the message text for the transition criteria. This value is null when no criteria is configured.
        - `criteria_details` (object) — Represents the criteria structure configured for the transition. This value is null when no criteria is configured.
          oneOf:
            - `GETCriteriaDetailsNested` — Represents a criteria group node in the recursive criteria structure of a transition. A group node contains a logical operator and a list of child nodes, where each child is either another nested group or a leaf criterion.
              type: null — Indicates that no criteria is configured for the transition. The value is always null.
        - `execution_time` (null) **REQ** — Represents the scheduled execution time of an automatic transition.
        - `sequence` (integer/int32) **REQ** — Represents the position of the transition in the Blueprint's transition order.
        - `next_field_value` (string) **REQ** [maxLen=255] — Represents the name of the state the record moves to when the transition is executed.
        - `text_color_code` (string) **REQ** [maxLen=10] — Represents the color code used to render the transition's text in the Blueprint.
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the transition.
        - `criteria_matched` (boolean) **REQ** — Indicates whether the record satisfies the criteria configured for the transition.
Possible values:
true - The record satisfies the transition criteria.
false - The record does not satisfy the transition criteria.
        - `id` (string) **REQ** [maxLen=25] — Represents the unique ID of the Blueprint transition.
        - `parent_transition` (object) **REQ** — Represents the parent transition details for parallel transitions. This value is null when the transition has no parent parallel transition.
          oneOf:
            - `GETParentTransitionNested` — Represents the ID and display name of the parent parallel transition. The value is null when the transition has no parent parallel transition.
              - `name` (string) **REQ** [maxLen=255] — Represents the display name of the parent parallel transition.
              - `id` (string) **REQ** [maxLen=25] — Represents the ID of the parent parallel transition.
              type: null — Indicates that the transition has no parent parallel transition. The value is always null.
        - `state` (string) [enum=['draft', 'open', 'completed']] — Indicates whether the transition is completed for the record.
Possible values:
**draft** - The transition is in draft state.
**open** - The transition is open and not yet completed.
**completed** - The transition is completed.
        - `fields` (array of object) [maxItems=200, nullable] — Represents the metadata of the configured during fields, including details of fields inside subforms used as during fields. Not present for non-accessible transitions.
        - `color_code` (string) **REQ** [maxLen=10] — Represents the color code of the transition.
        - `percent_partial_save` (integer/int32) **REQ** — Represents the percentage of the transition completed for the record.
        - `is_accessible` (boolean) — Indicates whether the transition is accessible to the current user.
Possible values:
true - The transition is accessible to the current user.
false - The transition is not accessible. The response still includes the transition, but omits **next_transitions**, **data**, and **fields**; this supports preview features such as early access.        
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request - The request cannot be processed due to invalid syntax.
**Resolution:** The record ID in the request URL must be valid and the record must be in process. [application/json]
    > Represents the error returned when the Blueprint transitions of a record cannot be retrieved. The response is one of the following error schemas: ErrorRecordNotInProcess, returned when Blueprint transitions are requested for a record that is not in process; ErrorInvalidRecordId, returned when the record ID given in the URL is invalid; ErrorInvalidModule, returned when the module API name given is invalid; or ErrorRecordLocked, returned when the record is locked.
    oneOf:
      - `ErrorRecordNotInProcess` — Represents the error returned when the record is not part of an active Blueprint process.
        - `code` (string) **REQ** [enum=['RECORD_NOT_IN_PROCESS']] — Represents the error code returned when the record is not part of an active Blueprint process.
Possible values:
RECORD_NOT_IN_PROCESS - The record is not associated with an active Blueprint process.
        - `details` (object) **REQ** — Represents additional details of the error that occurred when the record is not part of an active Blueprint process.
        - `message` (string) **REQ** [enum=['record not in process']] — Represents the error message indicating that the record is not part of an active Blueprint process.
Possible values:
record not in process - The specified record is not associated with an active Blueprint process.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed because the record is not part of an active Blueprint process.
      - `ErrorInvalidRecordId` — Represents the error returned when the record ID specified in the request URL is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the record ID in the request URL is invalid.
Possible values:
INVALID_DATA - The record ID specified in the request URL is invalid.
        - `details` (object) **REQ** — Represents additional details about the error, including validation information. This object is empty for this error.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the record ID in the request URL is invalid.
Possible values:
the ID given seems to be invalid - The record ID specified in the request URL is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed because the record ID in the request URL is invalid.
      - `ErrorInvalidModule` — Represents the error returned when the module API name specified in the request URL does not correspond to a valid module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned for this failure, fixed to **INVALID_MODULE** when the module API name given in the request is invalid.
        - `details` (object) **REQ** — Contains additional details about the validation failure, including the index of the request path segment that holds the invalid module name.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the zero-based index of the request path segment that contains the invalid module name.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message returned when the module API name in the request URL is invalid.
Possible values:
the module name given seems to be invalid - The module API name specified in the request URL does not correspond to a valid module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed because the module API name in the request URL is invalid.
      - `ErrorRecordLocked` — Represents the error returned when the requested operation cannot be performed because the record is locked.
        - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Represents the error code returned when the record is locked.
Possible values:
RECORD_LOCKED - The operation cannot be performed because the record is locked.
        - `details` (object) **REQ** — Represents additional details about the record-locking error, including the attempted action and the ID of the locked record.
          - `action` (string) **REQ** [maxLen=255] — Represents the action that was attempted on the locked record.
          - `id` (string) **REQ** [maxLen=255] — Represents the ID of the locked record on which the operation was attempted.
        - `message` (string) **REQ** [enum=['Sorry, you cannot perform this operation as the record is locked.']] — Represents the error message returned when the record is locked.
Possible values:
Sorry, you cannot perform this operation as the record is locked. - The requested operation cannot be completed because the record is locked.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed.
      - `ErrorInvalidRequest` — Represents the error returned when the request body or request parameters are invalid or malformed.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Represents the error code returned when the request body or request parameters are invalid or malformed.
Possible values:
INVALID_REQUEST - The request body or request parameters are invalid or malformed.
        - `details` (object) **REQ** — Represents additional details about the error, including validation information. This object is empty for this error.
        - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when the request body or request parameters are invalid or malformed.
Possible values:
unable to process your request. please verify whether you have entered proper method name, parameter and parameter values. - The request cannot be processed because the method name, parameter, or parameter values are invalid or malformed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed because the request body or request parameters are invalid or malformed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Forbidden - The client does not have access rights to the content.
**Resolution:** The user must be granted the necessary access rights for the record and its Blueprint process. — Schema: `ErrorModuleNotSupported` [application/json]
    > Represents the error response returned when the module specified in the request URL is not supported by this API.
    schema: `ErrorModuleNotSupported`
    - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code that identifies the cause of the failure.

Possible values:
NOT_SUPPORTED - The given module is not supported in the API.
    - `details` (object) **REQ** — Represents additional details about the error, including the index of the request path segment that caused the failure.
      - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index of the request path segment that caused the failure.
    - `message` (string) **REQ** [enum=['the given module is not supported in api']] — Represents the error message that describes the failure.
Possible values:
the given module is not supported in API - The module in the request URL is not supported by this API.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.

Possible values:
error - The request failed because the given module is not supported in the API.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.Events.READ, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.Products.READ, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.Invoices.READ, ZohoCRM.modules.Notes.READ, ZohoCRM.modules.Custom.READ
