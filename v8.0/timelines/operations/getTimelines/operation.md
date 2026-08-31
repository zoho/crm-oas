# GET /{module}/{recordId}/__timeline
**Operation:** `getTimelines` — Get Timelines
> To retrieve a paginated list of timeline entries for a specific record in your Zoho CRM organization. Each timeline entry captures an audited event such as field changes, ownership transfers, workflow actions, Approval Process progressions, Scoring Rule updates, and signal events from extensions.

**Parameters:**
- `module` (path, string, required) [maxLen=255]: Specifies the API name of the CRM module to retrieve timeline entries from. Use the value from the **api_name** field returned by [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html).
- `recordId` (path, string, required) [maxLen=255]: Specifies the unique ID of the CRM record to retrieve timeline entries for.
- `include_inner_details` (query, string, optional) [maxLen=255]: Use this parameter if you want to retrieve additional details about updates made to a record in the `field_history` object of the response.

**Possible Values**

- field_history.data_type :  Gives the data type of the field that was updated.

- `field_history.field_label` : Gives the label details of the fields that were updated.

- field_history.pick_list_values : Represents the list of values available for a picklist field.

- `field_history.enable_colour_code` : Indicates whether colour coding is enabled for the picklist values.

- `done_by.profile` : Provides details of the user's profile who updated the record.

- `done_by.type__s` : Indicates the type of user (for example, portal user or regular user) who modified the record.

- `page_token` (query, string, optional) [maxLen=255]: Specify the **next_page_token** or the **previous_page_token** after you have paginated and retrieved 200 records. Note that you cannot give **per_page** parameter if you give **page_token** in the request.
- `page` (query, integer/int32, optional): Specifies the page number for retrieving timeline entries in paginated results.
- `per_page` (query, integer/int32, optional) [enum=[3]]: Specifies the number of timeline entries to return per page. The value must be **3**.
- `filters` (query, string, optional) [maxLen=255]: **`filters` Parameter**

The `filters` parameter is used to filter responses from the Timeline API based on specific conditions.

Each filter condition consists of the following components:
- field`
- `comparator`
- `value`

**Supported `field.api_name` Values**
The following values are supported for `field.api_name`:
- `record.module.api_name`
- `source`
- `audited_time`
- `done_by.id`

**`record.module.api_name`**
Use this field to filter timeline details related to the following record types:
- `Notes`
- `Attachments`
- `Tasks`
- `Calls`
- `Events`
- `Emails`

**Allowed Comparators**
- `equal`
- `in`

**Allowed Values**
- `Notes`
- `Attachments`
- `Tasks`
- `Calls`
- `Events`
- `Emails`

**Example: Filter Notes**
```json
{
  "field": {
    "api_name": "record.module.api_name"
  },
  "comparator": "equal",
  "value": "Notes"
}
```
**Example: Filter Notes and Tasks**
```json
{
  "field": {
    "api_name": "record.module.api_name"
  },
  "comparator": "in",
  "value": ["Notes", "Tasks"]
}
```
**`done_by.id`**

Use this field to filter timeline details performed by a specific user.

**Allowed Comparators**

- `equal`
- `in`

**Allowed Values**

- User IDs

**Example**

```json
{
  "field": {
    "api_name": "done_by.id"
  },
  "comparator": "in",
  "value": ["5843104000000424001"]
}
```

**`audited_time`**

Use this field to filter timeline data based on the audit timestamp.

**Allowed Comparator**

- `between`

**Allowed Values**

- Time in ISO 8601 format

**Example: Filter Timeline Details Between Two Dates**

```json
{
  "field": {
    "api_name": "audited_time"
  },
  "comparator": "between",
  "value": [
    "2023-10-25T00:00:00+12:00",
    "2023-10-30T23:59:59+12:00"
  ]
}
```

**`source`**

Use this field to filter timeline data based on its source.

**Allowed Comparators**

- `equal`
- `in`

**Allowed Values**

- `crm_api`
- `mass_delete_via_crm_api`
- `bulkapi`
- `approval_process`
- `assignment_rules`
- `blueprint`
- `mass_update_via_blueprint`
- `orchestration`
- `convert`
- `massconvert`
- `custom_function`
- `macro`
- `crm_ui`
- `mass_update`
- `mass_update_via_scheduler`
- `mass_delete_via_clean_up`
- `bulk_action`
- `change_owner`
- `mass_change_owner_via_scheduler`
- `review_process`
- `scoringrule`
- `wizard`
- `workflow`

**Example: Filter by a Single Source**

```json
{
  "field": {
    "api_name": "source"
  },
  "comparator": "equal",
  "value": "crm_ui"
}
```

**Example: Filter by Multiple Sources**

```json
{
  "field": {
    "api_name": "source"
  },
  "comparator": "in",
  "value": ["crm_api", "crm_ui"]
}
```

---

**Combining Multiple Conditions**

Use `group_operator` and `group` to combine multiple filter conditions.

**Example**

```json
{
  "group_operator": "AND",
  "group": [
    {
      "field": {
        "api_name": "record.module.api_name"
      },
      "comparator": "in",
      "value": ["Notes"]
    },
    {
      "field": {
        "api_name": "source"
      },
      "comparator": "in",
      "value": ["crm_ui", "crm_api"]
    }
  ]
}
```

You can also refer to the sample request for the complete structure.

> **Note:** The value of the `filters` parameter must be URL-encoded before sending the request.

**URL Encoding Example**

The following filter:

```json
{
  "comparator": "between",
  "field": {
    "api_name": "audited_time"
  },
  "value": [
    "2023-06-07T00:00:00+05:30",
    "2023-06-07T12:59:59+05:30"
  ]
}
```

is encoded as:

```text
filters=%7B%22comparator%22%3A%22between%22%2C%22field%22%3A%7B%22api_name%22%3A%22audited_time%22%7D%2C%22value%22%3A%5B%222023-06-07T00%3A00%3A00%2B05%3A30%22%2C%222023-06-07T12%3A59%3A59%2B05%3A30%22%5D%7D
```

You can use the **Encode URL** and **Decode URL** options in the [URL Encoder/Decoder tool](https://www.zoho.com/toolkit/encode-decode.html) to encode or decode this value.

- `sort_by` (query, string, optional) [enum=['audited_time']]: Specifies the field to sort timeline entries by. The only supported value is **audited_time**.
- `sort_order` (query, string, optional) [enum=['asc', 'desc']]: Specifies the sort order for timeline entries. Possible values: **asc**, **desc**.
- `include_timeline_types` (query, string, optional) [maxLen=255]: To include extra types in the "timeline" object. You can get "signals" data through this to get signals-related timeline entries.
- `include` (query, string, optional) [maxLen=255]: Use this parameter if you want to view the details of updates to the record through signals or any other means. The possible values are extension and type. For example, if the record was updated through a signal, then the response will have details of the extension as email insights, while the type of update will be signals.

**Responses:**

- **200**: Returns a paginated list of timeline entries for the specified CRM record. [application/json]
    > Represents the successful response body for the Get Timelines operation.
    - `__timeline` (array of object) [maxItems=200] — Represents an array of timeline entries for the specified CRM record. Each entry captures an audited event with its timestamp, action type, source, and contextual details.
      - `audited_time` (string/date-time) **REQ** — Represents the timestamp at which the action was audited and recorded in the timeline.
      - `action` (string) [enum=[71 values], nullable] — Represents the type of action performed on the record. This field is nullable.
      - `id` (string) [maxLen=255] — Represents the unique ID of the timeline entry.
      - `source` (string) [enum=[127 values]] — Represents the source system or trigger origin of the timeline event.
      - `extension` (object) — Represents the extension details associated with a signal-type timeline entry, including the extension namespace, ID, and signal information.
        - `namespace` (string) [maxLen=255] — Represents the namespace of the extension that generated the signal.
        - `id` (string) [maxLen=255] — Represents the unique ID of the extension that generated the signal.
        - `signal` (object) — Represents the signal details dispatched by the extension.
          - `display_label` (string) [maxLen=255] — Represents the display label shown for the extension signal in the CRM timeline.
          - `action` (string) [maxLen=255] — Represents the action performed by the extension signal.
          - `id` (string) [maxLen=255] — Represents the unique ID of the extension signal.
          - `medium` (string) [maxLen=255] — Represents the medium through which the extension signal was generated.
      - `done_by` (object) — The details of the user who modified the record such as the name, ID, name and ID of that user's profile, and the user type.
        - `name` (string) [maxLen=255] — Represents the name of the user who performed the action.
        - `id` (string) [maxLen=255] — Represents the unique ID of the user who performed the action.
        - `profile` (object) — Represents the user profile associated with the user who performed the action.
          - `name` (string) [maxLen=255] — Represents the name of the user's profile.
          - `id` (string) [maxLen=255] — Represents the unique ID of the user's profile.
        - `type__s` (string) [maxLen=255] — Represents the type of the user who performed the action, such as a standard user, admin, or system user.
      - `related_record` (object) — The name and ID of the parent record which the task, call, or meeting belongs to.
        - `name` (string) [maxLen=255, nullable] — Represents the name of the related CRM record. This field is nullable.
        - `id` (string) [maxLen=255, nullable] — Represents the unique ID of the related CRM record. This field is nullable.
        - `module` (object) — Represents the module information for the related CRM record.
          - `name` (string) [maxLen=255] — Represents the display name of the module containing the related CRM record.
          - `id` (string) [maxLen=255] — Represents the unique ID of the module containing the related CRM record.
          - `api_name` (string) [maxLen=255] — Represents the API name of the module containing the related CRM record.
      - `automation_details` (object) — Represents the automation context associated with the timeline entry, including details about triggered workflows, approval processes, scoring rules, ownership changes, and review processes.
        - `type` (string) [maxLen=255] — Represents the type of automation action that triggered the timeline event, such as a workflow, Approval Process, or Scoring Rule.
        - `rule` (object) — Represents the automation rule that triggered the timeline event.
          - `name` (string) [maxLen=255] — Represents the name of the automation rule.
          - `id` (string) [maxLen=255] — Represents the unique ID of the automation rule.
        - `pathfinder` (object) — Represents the Blueprint process details associated with the timeline entry, including the triggered state and entry or exit flags.
          - `process_entry` (boolean) — Indicates whether the Blueprint process entry action was triggered for this timeline event.
          - `process_exit` (boolean) — Indicates whether the Blueprint process exit action was triggered for this timeline event.
          - `state` (object) — Represents the Blueprint state associated with the timeline event.
            - `trigger_type` (string) [maxLen=255] — Represents the trigger type that caused the Blueprint state to activate.
            - `name` (string) [maxLen=255] — Represents the name of the Blueprint state.
            - `is_last_state` (boolean) — Indicates whether this Blueprint state is the final state in the process.
            - `id` (string) [maxLen=255] — Represents the unique ID of the Blueprint state.
        - `workflow` (object) — Represents the workflow details associated with the timeline entry.
          - `field_update_action` (array of object) [maxItems=50] — Represents an array of field update actions executed by the workflow.
            - `name` (string) [maxLen=255] — Represents the name of the workflow field update action.
            - `id` (string) [maxLen=255] — Represents the unique ID of the workflow field update action.
        - `approval_process` (object) — Represents the Approval Process details associated with the timeline entry.
          - `next_approver` (array of object) [maxItems=50] — Represents an array of the next approvers in the Approval Process sequence.
            - `name` (string) [maxLen=255] — Represents the name of the next approver user.
            - `id` (string) [maxLen=255] — Represents the unique ID of the next approver user.
          - `comments` (string) [maxLen=1000] — Represents the comments added during the Approval Process action.
          - `takeover_reason` (string) [maxLen=255] — Represents the reason provided for the approval task takeover.
          - `current_stage` (integer/int32) — Represents the current stage number of the Approval Process at the time of the timeline event.
          - `takeover_stage` (string) [maxLen=255] — Represents the approval stage at which the takeover occurred.
          - `rejected_details` (object) — Represents the details of the rejection event in the Approval Process.
            - `stage` (object) — Represents the stage transition details at the time of rejection.
              - `from` (string) [maxLen=255] — Represents the approval stage from which the rejection occurred.
              - `to` (string) [maxLen=255] — Represents the approval stage to which the process moved after rejection.
            - `name` (string) [maxLen=255] — Represents the name of the user who rejected the approval request.
            - `id` (string) [maxLen=255] — Represents the unique ID of the user who rejected the approval request.
          - `delegate_details` (object) — Represents the delegation details when the approval task was delegated from one user to another.
            - `from` (object) — Represents the user from whom the approval task was delegated.
              - `name` (string) [maxLen=255] — Represents the name of the user from whom the approval task was delegated.
              - `id` (string) [maxLen=255] — Represents the unique ID of the user from whom the approval task was delegated.
            - `to` (object) — Represents the user to whom the approval task was delegated.
              - `name` (string) [maxLen=255] — Represents the name of the user to whom the approval task was delegated.
              - `id` (string) [maxLen=255] — Represents the unique ID of the user to whom the approval task was delegated.
          - `approver_details` (object) — Represents the details of the approver who acted on the Approval Process.
            - `name` (string) [maxLen=255] — Represents the name of the approver user.
            - `id` (string) [maxLen=255] — Represents the unique ID of the approver user.
        - `assigned_to` (object) — Represents the user to whom the record was assigned by an automation action.
          - `name` (string) [maxLen=255] — Represents the name of the user assigned to the record.
          - `id` (string) [maxLen=255] — Represents the unique ID of the user assigned to the record.
        - `scoring_rule` (object) — Represents the Scoring Rule details associated with the timeline entry, including score changes for positive and negative scoring and touchpoint scoring.
          - `zia_type` (boolean) — Indicates whether the Scoring Rule event was triggered by Zia, the AI assistant in Zoho CRM.
          - `negative_score` (object) — Represents the negative score change recorded for the record by the Scoring Rule.
            - `new` (string) [maxLen=20, nullable] — Represents the new negative score value after the Scoring Rule was applied. This field is nullable.
            - `old` (string) [maxLen=20, nullable] — Represents the previous negative score value before the Scoring Rule was applied. This field is nullable.
          - `positive_score` (object) — Represents the positive score change recorded for the record by the Scoring Rule.
            - `new` (string) [maxLen=20, nullable] — Represents the new positive score value after the Scoring Rule was applied. This field is nullable.
            - `old` (string) [maxLen=20, nullable] — Represents the previous positive score value before the Scoring Rule was applied. This field is nullable.
          - `touch_point` (object) — Represents the touchpoint score details associated with the Scoring Rule event.
            - `negative_score` (object) — Represents the touchpoint negative score change recorded by the Scoring Rule.
              - `new` (string) [maxLen=20, nullable] — Represents the new touchpoint negative score value after the Scoring Rule was applied. This field is nullable.
              - `old` (string) [maxLen=20, nullable] — Represents the previous touchpoint negative score value before the Scoring Rule was applied. This field is nullable.
            - `positive_score` (object) — Represents the touchpoint positive score change recorded by the Scoring Rule.
              - `new` (string) [maxLen=20, nullable] — Represents the new touchpoint positive score value after the Scoring Rule was applied. This field is nullable.
              - `old` (string) [maxLen=20, nullable] — Represents the previous touchpoint positive score value before the Scoring Rule was applied. This field is nullable.
            - `score` (object) — Represents the overall touchpoint score change recorded by the Scoring Rule.
              - `new` (string) [maxLen=20, nullable] — Represents the new overall touchpoint score value after the Scoring Rule was applied. This field is nullable.
              - `old` (string) [maxLen=20, nullable] — Represents the previous overall touchpoint score value before the Scoring Rule was applied. This field is nullable.
        - `owner` (object) — Represents the ownership change details recorded in the timeline entry, including previous and new owner information.
          - `name` (string) [maxLen=255] — Represents the name of the owner user.
          - `id` (string) [maxLen=255] — Represents the unique ID of the owner user.
          - `new` (object) — Represents the new owner assigned to the record after the ownership change.
            - `name` (string) [maxLen=255] — Represents the name of the new owner user.
            - `id` (string) [maxLen=255] — Represents the unique ID of the new owner user.
          - `old` (object) — Represents the previous owner of the record before the ownership change.
            - `name` (string) [maxLen=255] — Represents the name of the previous owner user.
            - `id` (string) [maxLen=255] — Represents the unique ID of the previous owner user.
        - `review_process` (object) — Represents the review process details associated with the timeline entry.
          - `deluge` (object) — Represents the Deluge script associated with the review process event.
            - `name` (string) [maxLen=255] — Represents the name of the Deluge script.
            - `id` (string) [maxLen=255] — Represents the unique ID of the Deluge script.
          - `deactivated_process` (object) — Represents the process that was deactivated as part of the review process event.
            - `name` (string) [maxLen=255] — Represents the name of the deactivated process.
            - `id` (string) [maxLen=255, nullable] — Represents the unique ID of the deactivated process. This field is nullable.
          - `rejection` (object) — Represents the rejection details when the review process was rejected.
            - `reason` (string) [maxLen=255] — Represents the reason provided for the rejection.
            - `comment` (string) [maxLen=255] — Represents the comment provided with the rejection.
        - `group_id` (string/int64) [maxLen=255, nullable] — Automation group ID for subform workflow triggers. Only present when action is 'subform_automation_trigger'.
        - `module` (object) — Module information for subform automation. Only present when action is 'subform_automation_trigger'.
          - `api_name` (string) [maxLen=255] — Module API name
          - `name` (string) [maxLen=255] — Module display name
          - `id` (string/int64) [maxLen=255] — Module ID
      - `record` (object) — Represents the CRM record associated with the timeline entry.
        - `name` (string) [maxLen=255, nullable] — Represents the name of the associated CRM record. This field is nullable.
        - `id` (string) [maxLen=255, nullable] — Represents the unique ID of the associated CRM record. This field is nullable.
        - `count` (string) [maxLen=255, nullable] — Represents the count of records associated with this timeline entry. This field is nullable.
        - `module` (object) **REQ** — Represents the module information for the associated CRM record.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module containing the associated CRM record.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the module containing the associated CRM record.
      - `converted_record` (object) — Represents the details of a converted record associated with the timeline entry.
        - `name` (string) [maxLen=255, nullable] — Represents the name of the converted record. This field is nullable.
        - `id` (string) [maxLen=255, nullable] — Represents the unique ID of the converted record. This field is nullable.
        - `module` (object) — Represents the module information for the converted record.
          - `api_name` (string) [maxLen=255] — Represents the API name of the module containing the converted record.
          - `id` (string) [maxLen=255] — Represents the unique ID of the module containing the converted record.
      - `field_history` (array of object) [maxItems=100, nullable] — **Contains the following details:**

* **api_name** - the API name of the field that was modified. This is available by default in the response.
* **_value** - the old and new values of the field. This is available by default in the response.

The following values are available when you specify the `include_inner_details` parameter:

* **enable_colour_code** - indicates whether color coding is enabled for the picklist field.
* **data_type** - the data type of the field that was modified.
* **pick_list_values** - details of the various values available for the picklist.

        - `data_type` (string) [maxLen=255] — Represents the data type of the field that changed.
        - `enable_colour_code` (boolean) — Indicates whether color coding is enabled for the changed field's values.
        - `pick_list_values` (array of object) [maxItems=200] — Represents an array of picklist options for the changed field, applicable when the field is a picklist type.
          - `display_value` (string) [maxLen=255] — Represents the display text of the picklist option shown in the CRM interface.
          - `sequence_number` (integer/int32) — Represents the sequence number that determines the display order of the picklist option.
          - `reference_value` (string) [maxLen=255] — Represents the reference value of the picklist option, used for lookups and cross-references.
          - `colour_code` (string) [maxLen=255, nullable] — Represents the color code associated with the picklist option. This field is nullable.
          - `actual_value` (string) [maxLen=255] — Represents the actual stored value of the picklist option.
          - `id` (string) [maxLen=255] — Represents the unique ID of the picklist option.
          - `type` (string) [maxLen=255] — Represents the type of the picklist option.
        - `field_label` (string) [maxLen=255] — Represents the display label of the field that changed.
        - `api_name` (string) [maxLen=255] — Represents the API name of the field that changed.
        - `id` (string) [maxLen=255] — Represents the unique ID of the changed field.
        - `_value` (object) — Represents the old and new values for the changed field.
          - `new` (string) [maxLen=255, nullable] — Represents the new value of the field after the change. This field is nullable.
          - `old` (string) [maxLen=255, nullable] — Represents the previous value of the field before the change. This field is nullable.
      - `type` (string) [enum=['timeline', 'signal']] — Represents the type of the timeline entry. Possible values: **timeline** (standard CRM activity), **signal** (event from a Zoho extension).
    - `info` (object) — Represents the pagination metadata for the timeline response.
      - `next_page_token` (string) **REQ** [maxLen=255, nullable] — Represents the token to retrieve the next page of timeline entries. The value is null when no more pages are available.
      - `previous_page_token` (string) **REQ** [maxLen=255, nullable] — Represents the token to retrieve the previous page of timeline entries. The value is null on the first page.
      - `count` (integer/int32) **REQ** — Represents the number of timeline entries returned in the current page.
      - `more_records` (boolean) **REQ** — Indicates whether additional timeline entries are available beyond the current page.
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated results.
      - `per_page` (integer/int32) **REQ** — The number of records you want to fetch per page. You can use this parameter for the first page only. For the subsequent pages, you must use the "page_token" parameter.

- **204**: Returns no content when no timeline entries exist for the specified record.

- **400**: Returns an error response when the request contains invalid parameters or an unrecognized module name.
**Resolution:** Verify the module API name, record ID, and query parameter values before retrying the request. Specify a valid record ID. Refer to [Get Records API](https://www.zoho.com/crm/developer/docs/api/v8/get-records.html) to get the record ID. [application/json]
    > Represents an error response returned when the request fails validation.
    oneOf:
        - `status` (string) [enum=['error']] — Represents the status of the error response. The value is always **error**.
        - `code` (string) [enum=['INVALID_MODULE']] — Represents the error code **INVALID_MODULE**.
        - `message` (string) [enum=['the module name given seems to be invalid']] — Represents the error message describing the invalid module.
        - `details` (object) — Represents the error details for the invalid module error.
          - `resource_path_index` (integer/int32) — Represents the index of the resource path element that caused the invalid module error.
        - `status` (string) [enum=['error']] — Represents the status of the error response. The value is always **error**.
        - `code` (string) [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
        - `message` (string) [maxLen=1000] — Represents the error message describing the invalid data in the request.
        - `details` (object) — Represents the error details for the invalid data error, including the resource path index.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path element that contains the invalid data.
        - `status` (string) [enum=['error']] — Represents the status of the error response. The value is always **error**.
        - `code` (string) [enum=['NOT_SUPPORTED', 'INVALID_DATA', 'PATTERN_NOT_MATCHED']] — Represents the error code. Possible values: **NOT_SUPPORTED**, **INVALID_DATA**, **PATTERN_NOT_MATCHED**.
        - `message` (string) [maxLen=1000] — Represents the error message describing the parameter validation failure.
        - `details` (object) — Represents the error details for the parameter validation error, including the parameter name.
          - `param_name` (string) [maxLen=255] — Represents the name of the parameter that caused the error.
        - `status` (string) [enum=['error']] — Represents the status of the error response. The value is always **error**.
        - `code` (string) [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
        - `message` (string) [maxLen=1000] — Represents the error message describing the required parameter validation failure.
        - `details` (object) — Represents the error details for the required parameter validation error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the required parameter that is missing or invalid.

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.Events.READ, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.Products.READ, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.Custom.READ
