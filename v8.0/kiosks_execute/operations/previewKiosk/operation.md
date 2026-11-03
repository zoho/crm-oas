# GET /settings/kiosks/{kioskId}/actions/preview
**Operation:** `previewKiosk` — Retrieve the Preview of a Specified Kiosk
> Retrieves the configuration and details of the first screen state for a specified Kiosk in Zoho CRM. This API returns only the first screen data required to render the Kiosk and does not trigger any actions or require user interaction. Supported on Standard, Professional, Enterprise, and Ultimate editions.

**Parameters:**
- `current_record_id` (query, string/int64, optional): Specifies the ID of the record to use as the Current Record context while previewing the Kiosk. The record must belong to the module configured as the Current Record in the Kiosk.
If this parameter is not provided, merge fields that reference the Current Record are not evaluated during the Kiosk preview and will return empty values.

- `invoked_from` (query, string, optional) [enum=['detail_view', 'home_page', 'cscript', 'canvas']]: Specify the context from which the kiosk preview is being invoked.
Possible values:
detail_view - The kiosk is invoked from the CRM record detail view.
home_page - The Kiosk is invoked from the home page.
cscript - The Kiosk is invoked from a Client Script.
canvas - The Kiosk is invoked from a Canvas view.

- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk for which you want to perform the operation.
- `include_inner_details` (query, string, optional) [maxLen=500]: Specify additional inner details to include in the response. Accepts a comma-separated list of dot-notation paths indicating which nested properties should return extended information.

**Responses:**

- **200**: Returns the configuration and initial screen state details of the specified Kiosk, including a kiosk_preview array that contains the kiosk state, its elements, and available transitions. — Schema: `KioskPreviewSuccessResponse` [application/json]
    > Represents the response for a successful kiosk preview, returning the initial executable screen with associated data, transitions, and layout metadata.
    schema: `KioskPreviewSuccessResponse`
    - `kiosk_preview` (array of object `KioskPreviewDetails`) [maxItems=1] **REQ** — Contains the preview details for the initial executable screen, including elements, transitions, data, and layout.
      schema: `KioskPreviewDetails`
      - `executable_info` (object `PreviewExecutableInfo`) **REQ** — Provides the current state and available transitions for the executable context of a kiosk preview.
        schema: `PreviewExecutableInfo`
        - `state` (object `PreviewStateSummary`) **REQ** — Represents a summary of a kiosk state referenced in the preview, including the state ID and display name.
          schema: `PreviewStateSummary`
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk state referenced in the preview.
          - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the kiosk state referenced in the preview.
        - `transitions` (array of object `PreviewTransitionSummary`) [maxItems=1] **REQ** — Specifies the list of transitions available from the current state. Each transition contains the display name, unique ID, prop_name,is_connected_end.
          schema: `PreviewTransitionSummary`
          - `prop_name` (string) **REQ** [maxLen=255, enum=['primary', 'default', 'outlineprimary', 'failure', 'outlineredlight']] — Specifies the type of button displayed on the Kiosk screen. Each button corresponds to a transition path that the user can select from the current screen.
**Possible values:**

**primary** - Displays the button as the primary action on the screen, typically used for actions such as Next, Submit, or Save.

**default** - Displays the button with the standard appearance, suitable for secondary actions.

**outlineprimary** - Displays the button with a primary-colored outline, emphasizing the action without making it the primary button.

**failure** - Displays the button with a solid error-themed style, typically used for destructive or critical actions such as Delete or Reject.

**outlineredlight** - Displays the button with a red outline, typically used for secondary destructive actions such as Cancel, Discard, or Remove.

          - `is_connected_end` (boolean) **REQ** — Indicates whether this transition leads to a connected end state in the kiosk flow.

Possible values:
true - The transition leads to a connected end state.
false - The transition leads to an intermediate state in the kiosk flow.

          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the transition in the kiosk preview.
          - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the transition in the kiosk preview.
      - `data` (object `PreviewDataSet`) **REQ** — Contains the records retrieved by the data elements configured in the Kiosk. This object uses dynamic keys, where each key is the API name of a data element (for example, a Get Records element). Each key maps to an object containing the retrieved record's display name (name) and unique identifier (id).
        schema: `PreviewDataSet`
        - `GetRecords_1` (array of object `PreviewRecordSummary`) [maxItems=1] **REQ** — Contains the list of record summaries returned by the GetRecords_1 element in the preview screen.
          schema: `PreviewRecordSummary`
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the record summary item in the preview data.
          - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the record summary item in the preview data.
      - `elements` (array of object) [maxItems=2] **REQ** — Contains the list of elements rendered on the kiosk preview screen.
        oneOf:
          - `PreviewElementDataBlock` — Represents a preview element data block that aggregates record retrieval configuration, raw values, record data, and pagination flags for a get record element.
            - `get_record` (object `PreviewGetRecordConfig`) **REQ** — Represents the configuration for a get record element in the preview screen, including selection details, module information, and the list of selected fields.
              schema: `PreviewGetRecordConfig`
              - `selection_details` (object `PreviewSelectionDetails`) **REQ** — Defines the record selection behavior for a get record element in the preview, including the selection type, result type, and record limit.
                schema: `PreviewSelectionDetails`
                - `selection_type` (string) **REQ** [maxLen=255] — Indicates the selection behavior applied to the records returned by the get record element.
                - `result_type` (string) **REQ** [maxLen=255, enum=['single', 'multiple', 'all']] — Indicates the type of result set returned by the get record element, such as all records.
                - `limit` (integer/int32) **REQ** — Indicates the maximum number of records to retrieve in the get record element of the preview.
              - `open_record` (boolean) **REQ** — Indicates whether the record detail view opens when a user selects a record in the preview.

Possible values:
true - The record detail view opens on selection.
false - The record detail view does not open on selection.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the get record element as defined in the kiosk configuration.
              - `module` (object `PreviewModuleInfo`) **REQ** — Describes the CRM module used in the preview get record element, including its display label, API name, internal name, and ID.
                schema: `PreviewModuleInfo`
                - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the CRM module shown to the user in the preview.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module used in the preview get record element.
                - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the CRM module used in the preview get record element.
                - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the CRM module used in the preview get record element.
              - `name` (string) **REQ** [maxLen=255] — Represents the display name of the get record element in the kiosk configuration.
              - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the get record element in the kiosk configuration.
              - `selected_fields` (array of object `PreviewSelectedField`) [maxItems=3] **REQ** — Contains the list of CRM fields configured for display in the get record element of the preview screen.
                schema: `PreviewSelectedField`
                - `ui_type` (integer/int32) **REQ** — Represents the UI type identifier that determines how the selected field is rendered in the preview.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the selected field included in the preview screen.
                - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the selected field as shown in the preview screen.
                - `data_type` (string) **REQ** [maxLen=255] — Represents the data type of the selected field, such as text or ownerlookup.
                - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the selected field definition in the preview screen.
            - `type` (string) **REQ** [maxLen=255] — Indicates the type classification of the preview element data block.
            - `value` (null) **REQ** — Contains the value of the preview element data block, which may be null when the block uses a record retrieval configuration.
            - `get_record_data` (array of object) [maxItems=19] **REQ** — Contains the list of CRM records returned by the get record element in the preview screen.
              oneOf:
                - `PreviewRecordData` — Represents the data returned for a previewed CRM record, including key field values and owner details.
                  - `First_Name` (string) **REQ** [maxLen=255, nullable] — Represents the first name of the contact or lead in the previewed CRM record.
                  - `Company` (string) **REQ** [maxLen=255] — Represents the company name of the previewed CRM record.
                  - `Owner` (object `PreviewOwnerSummary`) **REQ** — Contains information about the owner of the record who initiated this kiosk execution.
                    schema: `PreviewOwnerSummary`
                    - `name` (string) **REQ** [maxLen=255] — Represents the full name of the record owner in the preview.
                    - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the record owner in the preview.
                  - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the previewed CRM record.
            - `more_records` (boolean) **REQ** — Indicates whether additional CRM records are available beyond those returned in the current preview response.

Possible values:
true - More records are available and can be retrieved.
false - All available records have been returned in the current response.
          - `PreviewFieldElement` — Represents a field-based element within the kiosk preview screen, including its type classification and current value.
            - `field` (object `PreviewFieldDefinition`) **REQ** — Describes a form or data field in the kiosk preview screen, including its label, API name, data type, UI type, and display constraints.
              schema: `PreviewFieldDefinition`
              - `allow_multiple_upload` (null) **REQ** — Indicates whether the field supports multiple file uploads, when applicable.
              - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the field as shown to the user in the kiosk screen.
              - `length` (integer/int32) **REQ** — Indicates the maximum character length configured for the field.
              - `tooltip` (null) **REQ** — Contains the tooltip text displayed for the field, when applicable.
              - `_merge_field` (string) **REQ** [maxLen=255] — Represents the merge field template reference used to populate the field value from a linked kiosk process flow.
              - `number_separator` (boolean) **REQ** — Indicates whether the field uses a number separator for display.

Possible values:
true - A number separator is applied when displaying the field value.
false - No number separator is applied.
              - `required` (boolean) **REQ** — Indicates whether the field is required in the kiosk screen.

Possible values:
true - The field must be filled in before the user can proceed.
false - The field is optional.
              - `ui_type` (integer/int32) **REQ** — Represents the UI type identifier that determines how the field is rendered in the kiosk screen.
              - `read_only` (boolean) **REQ** — Indicates whether the field is read-only in the kiosk screen.

Possible values:
true - The field is read-only and cannot be edited by the user.
false - The field is editable by the user.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field as defined in the CRM module.
              - `data_type` (string) **REQ** [maxLen=255] — Represents the data type of the field, such as text, integer, or ownerlookup.
              - `currency` (null) **REQ** — Indicates the currency configuration for the field, when applicable to currency-type fields.
              - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the field definition in the kiosk screen.
              - `_pick_list_type` (string) **REQ** [enum=['global_set', 'local', None], nullable] — Indicates the picklist type configuration for the field, when applicable.
              - `decimal_place` (null) **REQ** — Indicates the number of decimal places configured for the field, when applicable to numeric fields.
              - `pick_list_values` (null) **REQ** — Contains the available picklist values for the field, when applicable to picklist field types.
            - `type` (string) **REQ** [maxLen=255] — Indicates the type classification of the field-based element in the preview screen.
            - `value` (string) **REQ** [maxLen=255] — Contains the current value of the field-based element in the preview screen.
      - `width` (string) **REQ** [maxLen=255] — Indicates the display width of the kiosk preview screen.
      - `kiosk` (object `PreviewKioskSummary`) **REQ** — Represents a minimal summary of the kiosk in the preview, including the kiosk name and ID.
        schema: `PreviewKioskSummary`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk associated with the preview.
        - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the kiosk associated with the preview.
      - `title` (string) **REQ** [maxLen=255] — Represents the display title of the kiosk preview screen.
      - `previous_states` (array of object `PreviewPreviousStateSummary`) [maxItems=2] **REQ** — Specifies an array containing the states traversed before the current state in the Kiosk execution flow. The states are listed in the order they were executed, starting from the start state and ending with the state immediately preceding the current state.
        schema: `PreviewPreviousStateSummary`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the previously executed kiosk state.
        - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the previously executed kiosk state.
        - `type` (string) **REQ** [maxLen=255] — Indicates the type classification of the previously executed kiosk state, such as start_state or get_records.
      - `button_align` (string) **REQ** [maxLen=255] — The alignment of action buttons.

**Possible values:**

**right_to_left** - Buttons are aligned from right to left.

**left_to_right** - Buttons are aligned from left to right.

**center** - Buttons are aligned to the center.

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.READ
