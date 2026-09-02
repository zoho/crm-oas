# PUT /settings/call_preferences
**Operation:** `updateCallPreferences` — Call Preferences
> To update the Call Preferences configuration for your Zoho CRM organization by enabling or disabling the **From Number** and **To Number** fields on records in the Calls module. A preference cannot be disabled when the corresponding field is marked as mandatory, when it is referenced by a Validation Rule, Layout Rule, Blueprint, or Workflow, or when the organization has an active telephony integration or active calendar booking for calls that depends on it.

**Request Body** (required) — application/json
> The request body must contain a **call_preferences** object that specifies the new visibility setting for the **From Number** field, the **To Number** field, or both.
  > Specify the new visibility setting for the **From Number** field, the **To Number** field, or both.
  - `call_preferences` (object) — Specify the new visibility setting for one or both Call Preferences. Omit a preference from the object to leave its current setting unchanged.
    - `show_from_number` (boolean) — Specify whether the **From Number** field must appear on records in the Calls module. 
**Possible values:**
**true** - Enable the **From Number** field on Call records.
**false** - Disable the **From Number** field and hide it from Call records.
    - `show_to_number` (boolean) — Specify whether the **To Number** field must appear on records in the Calls module. 
**Possible values:**
**true** - Enable the **To Number** field on Call records.
**false** - Disable the **To Number** field and hide it from Call records.

**Responses:**

- **200**: Returns the result of the update action, confirming the Call Preferences update for the Zoho CRM organization. [application/json]
    > Returned when the Call Preferences are successfully updated. Contains a **call_preferences** object that confirms the update outcome.
    - `call_preferences` (object) — Contains the update result for the Call Preferences configuration, including the result code, status, and message.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code of the update action. 
**Possible values:**
**SUCCESS** - Reports successful update of the Call Preferences configuration.
      - `message` (string) **REQ** [maxLen=255] — Describes the update result in plain text so that it can be displayed to the developer.
      - `status` (string) **REQ** [enum=['success']] — Indicates the outcome of the request. 
**Possible values:**
**success** - The request completed successfully.
      - `details` (object) **REQ** — Contains additional information about the update action. This object remains empty for a successful Call Preferences update.

- **400**: The update Call Preferences request is invalid. Resolution: The request payload, the data types of the supplied values, and the eligibility of the targeted fields for disablement must all satisfy the operation's validation rules. [application/json]
    > Returned when the update Call Preferences request fails validation. The response carries one of the per-request error variants, depending on the failure type.
    oneOf:
        - `call_preferences` (object) **REQ** — Contains the per-preference error variant returned when the update Call Preferences request payload fails validation.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
          - `message` (string) **REQ** [maxLen=255] — Error message
          - `status` (string) **REQ** [enum=['error']] — Error Status
          - `details` (object) **REQ** — Error details with validation information
            - `expected_data_type` (string) **REQ** [enum=['boolean']] — Detail field: expected_data_type
            - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
            - `json_path` (string) **REQ** [maxLen=255] — Detail field: json_path
        - `call_preferences` (object) **REQ** — Error details wrapped under call_preferences key
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
          - `message` (string) **REQ** [maxLen=255] — Error message
          - `status` (string) **REQ** [enum=['error']] — Error Status
          - `details` (object) **REQ** — Error details with validation information
            - `api_name` (string) **REQ** [enum=['show_from_number', 'show_to_number']] — Detail field: api_name
            - `json_path` (string) **REQ** [maxLen=255] — Detail field: json_path
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Error code
        - `message` (string) **REQ** [maxLen=255] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error Status
        - `details` (object) **REQ** — Details of the error response

**Scopes:** ZohoCRM.settings.modules.update
