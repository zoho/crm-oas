# PUT /settings/blueprints/transitions/{transitionId}
**Operation:** `updateBlueprintTransitionById` — Update a Blueprint transition
> To update a single Blueprint transition in Zoho CRM. Prerequisite: Call this API for every transition after Blueprint creation to set the modified_time, which the UI requires to render transitions correctly. Critical behaviors: (1) The **layout** key is required in the request body whenever **during_inputs** are included; omitting it causes INVALID_DATA: Invalid field details with a misleading reference to during_inputs[0]. (2) The **during_inputs** are additive; each PUT call appends new entries rather than replacing them. Remove entries by sending an object with **_delete** set to null, the entry **ID**, and **type** set to "field". (3) The **optional** key must be a Boolean (true/false), not a string; strings return INVALID_DATA: expected Boolean.

**Parameters:**
- `transitionId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+]: Specify the ID of the transition to update.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Represents a custom request header that identifies the Zoho service associated with the request. Possible values: **automation**.

**Schemas:**
`ActionTargetModuleReferenceAlternate`:
  > Related list module data associated in during field
  - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the module for which the transition is created in a blueprint.
  - `id` (string/int64) [maxLen=50, minLen=1, pattern=^[0-9]+$, nullable] — Represents the ID of the module for which the blueprint transition is created.
`AdditionalCriteriaGroupFieldReference2`:
  > field of the criteria
  - `api_name` (string) [maxLen=100, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — Represents the API name of the field associated with the during input of the transition.
  - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]+$, nullable] — Represents the ID of the field associated with the during input of the transition.
`CriteriaGroupCompositeAlternate`:
  > Represents the second alternate form of a composite criteria group, combining conditions and nested groups with a group operator. Contains the comparator used to compare the field value, the group of conditions combined using the group operator, the group operator itself, and the value against which the field value is compared.
  - `comparator` (string) [maxLen=20, nullable] — Represents the comparator of the criteria, used to compare the field value with the specified value.
  - `field` (object `AdditionalCriteriaGroupFieldReference2`) — This denotes the field used in the criteria
  - `value` (string) [maxLen=1000, nullable] — Represents the value against which the field value is compared in the criteria.
  - `group_operator` (string) [maxLen=3, nullable] — Represents the group operator that determines how the conditions in the criteria group are combined.
  - `group` (array of object `CriteriaGroupCompositeAlternate`) [maxItems=2] — Contains the group of conditions that are combined using the group operator in the criteria.
`DuringInputConfiguredFieldAlternate`:
  > Represents the alternate configuration for a during-input sub-field, including the field reference, optional flag, and optional criteria.
  - `optional` (boolean) [nullable] — Indicates whether the field is optional to fill in the during input. Possible values: **true**, **false**.
  - `field` (object `AdditionalCriteriaGroupFieldReference2`) — Field data of the field associated in during field
  - `validation_filter` (object `DuringInputValidationFilterAlternate`) — criteria details for validation
  - `name` (string) [maxLen=100] — Represents the name of the configured field collected as a during input in the transition.
  - `subform_fields` (array of object `DuringInputConfiguredFieldAlternate`) [maxItems=10, nullable] — Contains the fields configured in the during input.
`DuringInputValidationFilterAlternate`:
  > Validation criteria detail for the during field
  - `criteria` (object `TransitionCriteriaExpressionAlternate2`) — Validation criteria specified for the during field associated with the transition
  - `validation_message` (string) [maxLen=100, nullable] — Represents the validation message to be shown in the during field.
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
`TransitionCriteriaExpressionAlternate2`:
  > Validation criteria specified for the during field associated with the transition
  - `comparator` (string) [maxLen=20, nullable] — Represents the comparator used to evaluate the criteria of the blueprint transition.
  - `field` (object `AdditionalCriteriaGroupFieldReference2`) — field of the criteria
  - `value` (string) [maxLen=1000, nullable] — Represents the value of the field to be compared with in the transition criteria.
  - `group_operator` (string) [maxLen=3, nullable] — Represents the group operator applied to the criteria of the blueprint transition.
  - `group` (array of object `CriteriaGroupCompositeAlternate`) [maxItems=1, nullable] — Contains the criteria group to which the transition criteria belong.

**Request Body** — application/json `BlueprintTransitionsUpdateRequestAlternate`
> The request body must contain a **transitions** array with one object that defines the transition configuration to update.
  > Represents the alternate request body containing one or more transition definitions to create or update within the blueprint.
  - `transitions` (array of object `BlueprintTransitionDefinitionAlternate`) [maxItems=1] **REQ** — Contains the list of transitions to update, with each object in the array representing a single transition configuration.
    schema: `BlueprintTransitionDefinitionAlternate`
    - `layout` (object) **REQ** — Represents the layout associated with the transition's module. This property is required when during_inputs is provided; omitting it while providing during_inputs causes a misleading INVALID_DATA error that references the field details of during_inputs[0]. The object must include at least the id and api_name properties.
      - `id` (string/int64) **REQ** [maxLen=50, minLen=1, pattern=^[0-9]{1,19}$] — Represents the ID of the layout associated with the transition's module.
      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents the API name of the layout associated with the transition's module.
      - `name` (string) [maxLen=50] — Represents the display name of the layout associated with the transition's module.
    - `during_inputs` (array of object `TransitionDuringInputEntryAlternate`) [maxItems=50, nullable] — Contains the inputs collected from the user while the transition is executed, such as fields, notes, attachments, tags, checklists, related lists, and kiosk screens. Entries are additive: each PUT call appends new entries to the existing list instead of replacing it. To remove an entry, include the entry with its id and _delete: null. This property requires the layout property in the same request body.
      schema: `TransitionDuringInputEntryAlternate`
      - `validation_filter` (object `DuringInputValidationFilterAlternate`) — Validation criteria detail for the during field
      - `sequence` (integer/int32) [nullable] — Indicates the order of the during-input fields of the transition to be created.
      - `field` (object `AdditionalCriteriaGroupFieldReference2`) — Field data of the field associated in during field
      - `configured_fields` (array of object `DuringInputConfiguredFieldAlternate`) [maxItems=10, nullable] — Contains the fields configured in the during input of the transition.
      - `optional` (boolean) [nullable] — Indicates whether this during-input field is optional. Possible values: **true**, **false**.
      - `type` (string) [maxLen=20, nullable] — Indicates the type of the during-input field configured for the transition to be created.
      - `message` (string) [maxLen=1000, nullable] — Represents the info message displayed in the during input.
      - `title` (string) [maxLen=10, nullable] — Represents the title of the checklist associated with the during-input field.
      - `kiosk` (object `KioskReferenceAlternate1`) — kiosk data associated in during field
        schema: `KioskReferenceAlternate1`
        - `name` (string) [maxLen=10, nullable] — Represents the name of the kiosk associated with the during field.
        - `id` (string) [maxLen=17, nullable] — Represents the ID of the kiosk associated with the during field.
      - `related_list` (object `TransitionRelatedListReferenceAlternate`) — Related list data of the RL associated in the blueprint
        schema: `TransitionRelatedListReferenceAlternate`
        - `layout` (object `RelatedListLayoutReferenceAlternate`) — layout data associated in during field
          schema: `RelatedListLayoutReferenceAlternate`
          - `api_name` (string) [maxLen=8, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — Represents the API name of the related list layout associated in the during field.
          - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]{1,19}$, nullable] — Represents the ID of the related list layout associated in the during field.
        - `name` (string) [maxLen=100, nullable] — Represents the name of the related list associated with the during field.
        - `id` (string) [maxLen=25, nullable] — Represents the ID of the related list associated with the blueprint.
        - `module` (object `ActionTargetModuleReferenceAlternate`) — Related list module data associated in during field
      - `items` (array of object `DuringChecklistItemAlternate`) [maxItems=2, nullable] — Contains the items of the checklist associated with the during-input field.
        schema: `DuringChecklistItemAlternate`
        - `name` (string) [maxLen=6, nullable] — Represents the name of the checklist item associated with the during field of the transition.
        - `sequence` (integer/int32) [nullable] — Represents the sequence of the checklist item associated with the during field of the transition.
        - `optional` (boolean) [nullable] — Indicates whether the checklist item associated with the during field is optional. Possible values: **true**, **false**.
    - `criteria` (object `TransitionCriteriaExpressionAlternate2`) — This denotes the criteria of the transition to be created.
    - `trigger_type` (string) [maxLen=100, enum=['automatic', 'manual'], nullable] — Indicates the trigger type of the transition.

Possible values:
- **automatic** - The transition is executed automatically when its conditions are met, without user action.
- **manual** - The transition is executed manually by a user.
    - `module` (object `ActionTargetModuleReferenceAlternate`) — This denotes the module of the transition to be created
    - `name` (string) [maxLen=50, nullable] — Represents the name of the transition. Transition names must be unique within a blueprint.
    - `description` (string) [maxLen=1000, nullable] — Represents the description of the transition.
    - `transition_type` (string) [maxLen=100, enum=['standalone_transition', 'parallel_transition', 'child_transition'], nullable] — Indicates the type of the transition. Possible values:
**standalone_transition** - A standard transition linking two states of the blueprint.
**parallel_transition** - A transition that runs in parallel with other transitions between the same states.
**child_transition** - A transition that belongs to a child blueprint.
    - `owners` (array of object `TransitionOwnerGroupAlternate`) [maxItems=5, nullable] — Contains the owners of the transition who are allowed to execute it.
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
        - `GeneralOwnerEntryAlternate1` — Represents the owner assignment for the non-referenced owner types of a transition, such as **record_owner**, **team_user**, and **portal_user_type**.
          - `type` (string) **REQ** [maxLen=20, enum=['record_owner', 'team_user', 'portal_user_type']] — Represents the type of the owner of the transition. Possible values: **record_owner**, **team_user**, **portal_user_type**.
          - `resources` (array of object `TransitionOwnerResourceReferenceAlternate`) [maxItems=2, nullable] — Contains the list of owners of the transition who can execute it.
            schema: `TransitionOwnerResourceReferenceAlternate`
            - `id` (string) [maxLen=25, nullable] — Represents the ID of the owner of the transition.
    - `actions` (array of object `TransitionAfterActionEntryAlternate1`) [maxItems=4, nullable] — Contains the list of after actions of the transition to be created. After actions are executed once the record moves from one state to another and include tasks, field updates, tags, and email notifications.
      discriminator: `type`
        field_updates → #/components/schemas/FieldUpdatesActionInputEntry
        tasks → #/components/schemas/TaskActionInputEntry
        functions → #/components/schemas/FunctionActionInputEntry
        email_notifications → #/components/schemas/EmailNotificationActionInputEntry
        webhooks → #/components/schemas/WebhookActionInputEntry
      oneOf:
        - `FieldUpdatesActionInputEntry` — Represents a request payload entry for an after action of the type **field_updates**. Only the ID and name of the field update action are accepted.
          - `id` (string/int64) [maxLen=20, minLen=1, pattern=[0-9]+, nullable] — Represents the ID of the after action associated with the after actions of the transition.
          - `_delete` (null) — Indicates whether the after-action configuration of the transition must be deleted.
          - `type` (string) **REQ** [enum=['field_updates']] — Indicates the type of the after action of the transition. Possible values: **field_updates**.
        - `TaskActionInputEntry` — Represents the request payload entry for an after-action of type tasks on a blueprint transition, identified by its ID.
          - `id` (string/int64) [maxLen=255, minLen=1, pattern=[0-9]+, nullable] — Represents the ID of the after action associated with the transition.
          - `type` (string) **REQ** [enum=['tasks']] — Represents the type of the after action of the transition. Possible values: **tasks**.
          - `_delete` (null) — Indicates whether the after-action configuration must be deleted.
        - `FunctionActionInputEntry` — Represents a request payload entry for an after action of the type **functions**. Only the ID and name of the function action are accepted.
          - `name` (string) [maxLen=255, nullable] — Represents the name of the after action associated with the after actions of the transition.
          - `id` (string/int64) [maxLen=19, minLen=1, pattern=[0-9]+, nullable] — Represents the ID of the after action associated with the after actions of the transition.
          - `type` (string) **REQ** [enum=['functions']] — Indicates the type of the after action of the transition. Possible values: **functions**.
        - `EmailNotificationActionInputEntry` — Represents a request payload entry for an after action of the type **email_notifications**. Only the ID and name of the email notification action are accepted.
          - `name` (string) [maxLen=255, nullable] — Represents the name of the email notification action associated with the after actions of the transition.
          - `id` (string/int64) [maxLen=20, minLen=1, pattern=[0-9]+, nullable] — Represents the ID of the email notification action associated with the after actions of the transition.
          - `type` (string) **REQ** [enum=['email_notifications']] — Indicates the type of the after action of the transition to be created. Possible values: **email_notifications**.
        - `WebhookActionInputEntry` — Represents a request payload entry for an after action of type **webhooks**. Only the id and name properties are accepted for this entry.
          - `name` (string) [maxLen=255, nullable] — Represents the name of the after action associated with the transition.
          - `id` (string/int64) [maxLen=20, minLen=1, pattern=[0-9]+, nullable] — Represents the ID of the after action associated with the transition.
          - `type` (string) **REQ** [enum=['webhooks']] — Indicates the type of the after action of the transition. Possible values: **webhooks**.
        - `GeneralActionEntryAlternate1` — Represents an after action of the transition for non-referenced action types: **add_tags**, **remove_tags**, **sms**, **whatsapp**, **create_record**, **add_meeting**, **schedule_call**, and **convert**.
          - `name` (string) [maxLen=50, nullable] — Represents the name of the after action associated in the after actions of the transition.
          - `details` (object `ActionTagUpdateDetailsAlternate`) — This denotes the details of the actions configured of the transition to be created.
            schema: `ActionTagUpdateDetailsAlternate`
            - `overwrite` (boolean) [nullable] — Indicates whether the tags configured in the after actions of a transition overwrite the existing tags on the record.
            - `module` (object `ActionTargetModuleReferenceAlternate`) — module data associated in after actions of transitions
            - `tags` (array of object `ActionTagDescriptorAlternate`) [maxItems=2, nullable] — Contains the list of tags associated with the after actions of a transition.
              schema: `ActionTagDescriptorAlternate`
              - `color` (string) [maxLen=100, nullable] — Represents the color of the tag configured in the after actions of a transition.
              - `name` (string) [maxLen=7, nullable] — Represents the name of the tag configured in the after actions of a transition.
          - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+, nullable] — Represents the ID of the after action associated with the after actions of the transition.
          - `type` (string) **REQ** [enum=[8 values]] — Represents the type of the after action configured for the transition. Possible values: **add_tags**, **remove_tags**, **sms**, **whatsapp**, **create_record**, **add_meeting**, **schedule_call**, **convert**.
    - `color_code` (string) [maxLen=1000, nullable] — Represents the color code of the transition button, for example, #F27E22.

**Responses:**

- **200**: Created - The API successfully creates or updates the Blueprint transition and returns the per-transition results. — Schema: `BlueprintTransitionsUpdateResponse` [application/json]
    > Represents the response returned when transitions are successfully created or updated, wrapping the per-transition results.
    schema: `BlueprintTransitionsUpdateResponse`
    - `transitions` (array of object `TransitionUpdateStatusEntry`) [maxItems=1] — Contains the list of updated transitions returned in the response, with each object in the array representing a single transition configuration.
      schema: `TransitionUpdateStatusEntry`
      - `code` (string) [maxLen=255] — Represents the error code returned for the transition update status entry.
      - `details` (object `TransitionUpdateItemDetails`) — Contains the response-level details of an updated transition item, including the unique identifier of the updated transition.
        schema: `TransitionUpdateItemDetails`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the updated transition.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the transition update for this status entry.
      - `status` (string) [maxLen=255] — Indicates the processing status of the transition update for this entry.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax.
**Resolution:** The invalid values in the request body must be corrected based on the error details in the response. [application/json]
    > Represents the structure of the error response returned when the request cannot be processed. The response is either a single validation error object or an object that wraps the per-transition errors.
    oneOf:
      - `InvalidEscalationPeriodError` — Represents the error returned when the period value provided in the escalation settings is invalid. The error code is **INVALID_DATA**.
        - `transitions` (array of object) [maxItems=25] **REQ** — Contains the list of error objects, one for each transition that failed validation.
          oneOf:
            - `TransitionTypeInvalidValueError` — Represents the error payload returned when the provided transition type value is invalid, including the API name and JSON path of the field and the values it supports.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the invalid transition type value. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details object with field-level validation information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation error.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Contains the values supported for the field that caused the error.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['the value given is invalid']] — Represents the error message returned when the given value is invalid. Possible values: **the value given is invalid**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `InvalidEscalationPeriodError` — Represents the error returned when the period value provided in the escalation settings is invalid. The error code is **INVALID_DATA**.
            - `TransitionActionsAmbiguityErrorResponse` — Represents the error returned when ambiguity is detected while processing the transition after actions, including the code, message, status, and validation details.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code returned when ambiguity is detected while processing the transition actions. Possible values: **AMBIGUITY_DURING_PROCESSING**.
              - `details` (object) **REQ** — Contains the error details with validation information about the ambiguity detected in the transition actions.
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Contains the list of transition actions that caused the ambiguity, each identified by its API name and JSON path.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the transition action that caused the ambiguity.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the transition action that caused the ambiguity.
              - `message` (string) **REQ** [enum=['Provide proper data']] — Represents the error message returned when ambiguity is detected in the transition actions. Possible values: **Provide proper data**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TransitionFieldMaxLengthError` — Validation error returned when the value of a transition field exceeds the maximum allowed length (code: INVALID_DATA). The error details include the maximum length allowed for the field.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a field value exceeds the maximum allowed length. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level validation information about the field whose value exceeded the maximum allowed length.
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum length allowed for the field whose value failed validation.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field whose value exceeded the maximum allowed length.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field whose value exceeded the maximum allowed length.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned when a field value exceeds the maximum allowed length. Possible values: **Invalid data**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `ChecklistTitleTooLongErrorResponse` — Represents the error response returned when the checklist title of a checklist field in a blueprint transition exceeds the allowed length. Contains the error code, message, response status, and field-level error details, including the maximum number of characters allowed for the checklist title.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the checklist title exceeds the allowed length. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level validation information for the checklist title that exceeded the allowed length.
                - `maximum_length` (integer/int32) **REQ** — Indicates the maximum number of characters allowed for the checklist title.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the checklist field whose title exceeds the allowed length.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the checklist field whose title exceeds the allowed length.
              - `message` (string) **REQ** [enum=['You can provide upto 30 characters.']] — Represents the error message returned when the checklist title exceeds the allowed length. Possible values: **You can provide upto 30 characters.**
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `ChecklistItemLimitExceededErrorResponse` — Represents the error response returned when the number of checklist items provided for a checklist field in a blueprint transition exceeds the allowed limit. Contains the error code, message, response status, and field-level error details, including the maximum number of checklist items permitted.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the checklist item limit exceeded error. Possible values: **DEPENDENT_MISMATCH**.
              - `details` (object) **REQ** — Contains the error details object with field-level validation information.
                - `dependee` (object) **REQ** — Contains the dependee object holding the dependent field information associated with the checklist item error.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the dependee field associated with the checklist item error.
                  - `dependee_value` (string) **REQ** [maxLen=255] — Represents the value of the dependent checklist item associated with the checklist item limit validation error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Contains the JSON path of the dependent checklist item associated with the checklist item limit validation error.
                - `maximum_length` (integer/int32) **REQ** — Indicates the maximum number of checklist items allowed for the checklist field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the checklist item error.
                - `json_path` (string) **REQ** [maxLen=1000] — Contains the JSON path of the checklist field whose item limit was exceeded.
              - `message` (string) **REQ** [enum=['You can provide upto 10 checklist items']] — Contains the error message describing the checklist item limit violation. Possible values: **You can provide upto 10 checklist items**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the status of the response. Possible values: **error**.
            - `ChecklistOptionNameTooLongErrorResponse` — Represents the error response returned when a checklist option name in a blueprint transition exceeds the allowed character limit. Contains the error code, message, response status, and field-level error details, including the maximum number of characters allowed for a checklist option name.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a checklist option name exceeds the allowed character length. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level validation information for the checklist option whose name exceeded the allowed character length.
                - `maximum_length` (integer/int32) **REQ** — Indicates the maximum number of characters allowed for a checklist option name.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the checklist option whose name exceeded the allowed character length.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the checklist option that exceeded the allowed character length.
              - `message` (string) **REQ** [enum=['You can provide upto 140 checklists option character limit']] — Represents the error message returned when a checklist option name exceeds the allowed character limit. Possible values: **You can provide upto 140 checklists option character limit**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TransitionFieldDataTypeError` — Represents the error returned when a value provided for a transition field fails data type validation.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a transition field value fails data type validation. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with validation information for the transition field that failed data type validation.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Indicates the expected data type of the transition field that failed data type validation.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the transition field that failed data type validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the transition field that failed data type validation.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message returned when a transition field value fails data type validation. Possible values: **Invalid data type**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `MandatoryFieldMissingError` — Represents the error returned when a mandatory field is missing from the request. Possible values for code: **MANDATORY_NOT_FOUND**.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a mandatory field is missing from the request. Possible values: **MANDATORY_NOT_FOUND**.
              - `details` (object) **REQ** — Contains the error details object with field-level validation information about the missing mandatory field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the mandatory field that is missing from the request.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the mandatory field that is missing from the request.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message returned when a mandatory field is missing from the request. Possible values: **Required field is missing**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TransitionFieldInvalidValueError` — Validation error returned when the value provided for a transition field is invalid (code: INVALID_DATA). The error details list the values supported by the field.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the transition field value is invalid. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level validation information about the invalid value.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the transition field whose value failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the transition field that contains the invalid value.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Contains the values supported by the transition field, listed when the submitted value is invalid.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned when the transition field value is invalid. Possible values: **Invalid data**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `InvalidValueResponse` — Represents the error response returned when invalid module data is provided during a reorder request. The response includes the error code **INVALID_DATA**, a descriptive message, a status, and validation details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a value in the request is invalid. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details object with field-level validation information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the property that holds the invalid value.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the property that holds the invalid value.
              - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the given ID is invalid. Possible values: **the id given seems to be invalid**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TransitionNameInvalidCharactersError` — Represents the error returned when a transition name contains disallowed characters, including the field-level validation context.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the transition name contains invalid characters. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details object with field-level validation information about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['should not contain special characters']] — Represents the error message returned when the transition name validation fails. Possible values: **should not contain special characters**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `ErrorTriggerTypeUpdateNotAllowed` — Represents the 400 error returned when an attempt is made to update the trigger type of a transition, which is not allowed (error code **NOT_ALLOWED**).
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when the trigger type of the transition cannot be updated. Possible values: **NOT_ALLOWED**.
              - `details` (object) **REQ** — Contains the error details object with field-level validation information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the property associated with the error.
              - `message` (string) **REQ** [enum=['cannot update trigger type']] — Represents the error message returned when the trigger type of the transition cannot be updated. Possible values: **cannot update trigger type**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `ModuleUpdateNotAllowedErrorResponse` — Represents the error returned when an attempt is made to change the module of an existing transition. Possible values for code: **NOT_ALLOWED**.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when the module update is not allowed. Possible values: **NOT_ALLOWED**.
              - `details` (object) **REQ** — Contains the error details with validation information for the rejected module update.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or module associated with the validation error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the attribute that caused the validation error.
              - `message` (string) **REQ** [enum=['cannot update module']] — Represents the error message returned when the module cannot be updated. Possible values: **cannot update module**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `CriteriaNotSupportedForFieldError` — Represents the error response returned when criteria are not supported for the specified field, including the error code, message, status, and field-level details.
              - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code returned when criteria are not supported for the field. Possible values: **NOT_SUPPORTED**.
              - `details` (object) **REQ** — Contains the error details with field-level information about the field for which criteria are not supported.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which criteria are not supported.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field for which criteria are not supported.
              - `message` (string) **REQ** [enum=['criteria not supported for the field']] — Represents the error message returned when criteria are not supported for the field. Possible values: **criteria not supported for the field**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `CriteriaFieldApiNameInvalidError` — Represents the validation error returned when the API name of a criteria field in a blueprint transition is invalid. Contains the error code **INVALID_DATA**, the error message, the response status, and field-level error details identifying the invalid criteria field.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the criteria field API name is invalid. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level information about the invalid criteria field API name.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the criteria field that is invalid.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the criteria field whose API name is invalid.
              - `message` (string) **REQ** [enum=['The given api_name seems to be invalid']] — Represents the error message returned when the criteria field API name is invalid. Possible values: **The given api_name seems to be invalid**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `DuringInputsNotAllowedAutomaticError` — Represents the error returned when during inputs are provided for an automatic transition, which is not allowed (code: NOT_ALLOWED).
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when blueprint transition during fields cannot be added to an automatic transition. Possible values: **NOT_ALLOWED**.
              - `details` (object) **REQ** — Contains the error details with field-level information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field associated with the error.
              - `message` (string) **REQ** [enum=['Blueprint transition during fields cannot be added to automatic transition']] — Represents the error message returned. Possible values: **Blueprint transition during fields cannot be added to automatic transition**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `DuringInputsNotAllowedParallelError` — Represents the error returned when during inputs are provided for a parallel transition, which is not allowed (error code **NOT_ALLOWED**).
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when during inputs are not allowed on a parallel blueprint transition. Possible values: **NOT_ALLOWED**.
              - `details` (object) **REQ** — Contains the error details with field-level information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the transition property that caused the validation error.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when during-input fields cannot be added to a parent parallel transition. Possible values: **Blueprint transition during fields cannot be added to a parent parallel transition**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `ActionNotSupportedForModuleError` — Represents the validation error returned when the specified action type is not supported for the given module (code: INVALID_DATA).
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the action is not supported for the module of the transition. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level information about the action that is not supported for the module of the transition.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['Action Not Supported For Module']] — Represents the error message returned when the action is not supported for the module of the transition. Possible values: **Action Not Supported For Module**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `DuringInputFieldIdInvalidDataError` — Represents the validation error returned when the ID of a during-input field is invalid (code: INVALID_DATA).
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a during-input field ID contains invalid data. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path associated with the error.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned for a during-input field with invalid data. Possible values: **invalid data**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `ActionLimitExceedsError` — Represents the validation error returned when the configured action count exceeds the permitted limit for the action type (code: INVALID_DATA).
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the action limit is exceeded. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with information about the exceeded action limit, such as the action type, its API name, the configured count, and the allowed limit.
                - `action_type` (string) **REQ** [maxLen=255] — Indicates the type of the action that exceeded the configured limit.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the action that exceeded the configured limit.
                - `limit` (integer/int32) **REQ** — Indicates the maximum number of actions allowed for the transition.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the action in the request that caused the error.
                - `configured_count` (integer/int32) **REQ** — Indicates the number of actions currently configured for the transition.
              - `message` (string) **REQ** [enum=['Action Limit Exceeds']] — Represents the error message returned when the action limit is exceeded. Possible values: **Action Limit Exceeds**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TransitionDuringFieldsLimitExceededError` — Represents the error returned when the number of fields configured in the during input of a blueprint transition exceeds the permitted limit.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code returned when the number of fields configured for the transition's during input exceeds the allowed limit. Possible values: **LIMIT_EXCEEDED**.
              - `details` (object) **REQ** — Contains the error details with limit information for the fields that exceed the allowed during-input limit.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error detail.
                - `limit` (integer/int32) **REQ** — Indicates the maximum number of fields allowed in the transition's during input.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the element associated with the error detail.
              - `message` (string) **REQ** [enum=['Blueprint transition during fields limit exceed']] — Represents the error message returned when the transition's during-input field limit is exceeded. Possible values: **Blueprint transition during fields limit exceed**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TransitionFieldInvalidDataError` — Validation error returned when the data provided for a transition field is invalid (code: INVALID_DATA).
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a transition field contains invalid data. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level information for the transition field that contains invalid data.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the transition field that contains invalid data.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the transition field that contains the invalid data.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned when the transition field data is invalid. Possible values: **Invalid data**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TransitionFieldValueInvalidError` — Validation error returned when the value provided for a transition field is invalid (code: INVALID_DATA).
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the given transition field value is invalid. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details object with field-level information about the invalid transition field value.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field whose value is invalid.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field whose value is invalid.
              - `message` (string) **REQ** [enum=['the value given is invalid']] — Represents the error message returned when the given transition field value is invalid. Possible values: **the value given is invalid**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `ActionNotBelongingToModuleError` — Represents the error returned when the specified action does not belong to the current module of the transition (code: INVALID_DATA).
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the action does not belong to the module. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the error details with field-level information about the action that does not belong to the current module of the transition.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['The action does not belong to the current module of the transition']] — Represents the error message returned when the action does not belong to the current module of the transition. Possible values: **The action does not belong to the current module of the transition**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TransitionTypeUpdateNotAllowedError` — Represents the error returned when the transition type cannot be updated to the specified value, with field-level details identifying the field that caused the error.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when the transition type cannot be updated to the specified value. Possible values: **NOT_ALLOWED**.
              - `details` (object) **REQ** — Contains the error details with field-level information about the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['cannot update transition type to the specified value']] — Represents the error message returned when the transition type cannot be updated to the specified value. Possible values: **cannot update transition type to the specified value**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `DuringFieldIdInvalidError` — Represents the validation error returned when the provided during field ID is invalid, including the error code, message, status, and details of the field whose ID is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the given field ID is invalid. Possible values: **INVALID_DATA**.
              - `details` (object) **REQ** — Contains the validation details of the field whose ID is invalid, including the field's API name and JSON path.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field whose ID is invalid.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field whose ID is invalid.
              - `message` (string) **REQ** [enum=['field id given seems to be invalid']] — Contains the error message returned for the validation failure. Possible values: **field id given seems to be invalid**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `DuringInputsWidgetAmbiguityError` — Represents the error returned when during-input fields are configured along with a widget or kiosk, causing an ambiguity during processing (error code **AMBIGUITY_DURING_PROCESSING**).
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code returned when during-input fields are configured along with a widget or kiosk. Possible values: **AMBIGUITY_DURING_PROCESSING**.
              - `details` (object) **REQ** — Contains the error details with validation information about the widget or kiosk ambiguity.
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Contains the list of fields or components that caused the ambiguity during processing.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or component that caused the ambiguity.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field or component that caused the ambiguity.
              - `message` (string) **REQ** [enum=['provide proper data', 'Fields are configured along with widget or kiosk']] — Represents the error message returned when during-input fields are configured along with a widget or kiosk. Possible values:
- **provide proper data**
- **Fields are configured along with widget or kiosk**
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `TeamUserNotAllowedForOrgModule` — Represents the error returned when a team or team-profile user is configured as a transition owner for an organization module, with the error code NOT_ALLOWED.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when a team user is not allowed to access the module. Possible values: **NOT_ALLOWED**.
              - `details` (object) **REQ** — Contains the error details object with field-level information about the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned by the API. Possible values: **team and team_profile type users cannot be configured as transition owners for organization modules**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
            - `ChildParallelTransitionActionsNotAllowedError` — Represents the error returned when after actions are added to a child parallel transition, which is not allowed. Contains the error code **NOT_ALLOWED**, the error message, the response status, and details identifying the disallowed field in the request.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when the operation is not permitted. Possible values: **NOT_ALLOWED**.
              - `details` (object) **REQ** — Contains the error details identifying the field that is not allowed.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the disallowed field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the disallowed field in the request.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when blueprint transition after actions cannot be added to a child parallel transition. Possible values: **Blueprint transition after actions cannot be added to a child parallel transition**.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status of the API call. Possible values: **error**.
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

- **403**: The user does not have permission to perform this action. **Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
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

**Scopes:** ZohoCRM.settings.transitions.UPDATE
