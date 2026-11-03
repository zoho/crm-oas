# GET /settings/kiosks/{kioskId}/states
**Operation:** `getAllKioskStates` — Get all states of a kiosk
> To retrieve all the states configured in a kiosk in your Zoho CRM organization, along with their transition details and basic metadata such as name, type, and associated fields. Each state represents a screen, action, decision, or GetRecords.

Available in: Standard, Professional, Enterprise, and Ultimate editions.


**Parameters:**
- `include` (query, string, optional) [enum=['configured_properties']]: Specify additional properties to be included in the response for each Kiosk state. By default, the response returns only the basic metadata of each state which includes each state's id, name, and associated_fields.

**Possible values:**

**configured_properties** - Includes the configured_properties key in the response for each state, which holds the list of merge fields and other dynamic references that have been configured within that state. When a state has no such configured properties, the value is returned as null.

- `include_inner_details` (query, string, optional) [enum=['details.type']]: Specify to include additional inner details in the GET response for the kiosk state.
- `kioskId` (path, string, required) [maxLen=255]: Specify the unique identifier of the Kiosk.

**Responses:**

- **200**: Returns the list of all states configured in the specified kiosk, including each state name, type, transitions, and associated fields. — Schema: `GetAllStatesResponse` [application/json]
    > Represents the response for retrieving all states associated with a kiosk. Contains a list of lightweight state entries with their basic metadata.
    schema: `GetAllStatesResponse`
    - `states` (array of object `GETAllStatesItem`) [maxItems=150] **REQ** — The response body contains a JSON object with a states array that lists all the states configured in the specified Kiosk.
      schema: `GETAllStatesItem`
      - `associated_fields` (array of object `GETAssociatedField`) [maxItems=25, nullable] — Represents the state type, indicating whether the state is a screen, decision, action, or get_records state. Below are the possible values for the action state.
**Possible values:**
create_record
quick_create_record
convert
open_record
open_link
add_meeting
schedule_call
assign_owner
add_tags
remove_tags
field_updates
tasks
email_notifications
webhooks

For get_records ,decision , start_state and end_state states, this field is null.

        schema: `GETAssociatedField`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the kiosk state.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the field associated with the kiosk state.
        - `type` (string) [maxLen=255] — Field: type. Present only for screen state associated fields.
      - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk state.
      - `details` (object `GETAllStatesDetails`) — Represents the summary details object returned for a state by the get all states operation. Contains lightweight screen detail properties when available. The structure of this object depends on the state type.
        schema: `GETAllStatesDetails`
        - `screen_details` (object `GETAllStatesScreenDetails`) **REQ** — Represents the summary screen details returned for a screen state by the get all states operation. Contains the width, title, and button alignment.
          schema: `GETAllStatesScreenDetails`
          - `width` (string) **REQ** [maxLen=255, enum=['670px', '1000px']] — Represents the visual width of the kiosk screen container.
**Possible values:**
**670px**
**1000px**

          - `title` (string) **REQ** [maxLen=255] — Represents the display title shown at the top of the kiosk screen.
          - `button_align` (string) **REQ** [maxLen=255, enum=['right_to_left', 'left_to_right', 'center']] — Represents the alignment direction of action buttons within the screen footer.
**Possible values:**

**right_to_left** - Buttons are aligned from right to left.

**left_to_right** - Buttons are aligned from left to right.

**center** - Buttons are aligned to the center.

      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the kiosk state.
      - `type` (string) **REQ** [maxLen=255, enum=['start_state', 'screen', 'get_records', 'end_state', 'action', 'decision']] — Represents the state type, indicating whether the state is a screen, decision, action, or get_records state.
      - `from_transition` (object) — Entry transition details. Null for start states.
        - `name` (string) **REQ** [maxLen=255] — Field: name
        - `id` (string) **REQ** [maxLen=255] — Field: id
      - `configured_properties` (array of object `GETScreenConfiguredProperty`) [maxItems=50, nullable] — Merge fields and dynamic references. Returned only when the include parameter is used.
        schema: `GETScreenConfiguredProperty`
        - `details` (object `GETConfiguredPropertyDetails`) **REQ** — Represents the details of a configured property associated with a kiosk state. Contains the name of the configured property.
          schema: `GETConfiguredPropertyDetails`
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the configured property detail.
          - `component_name` (string) [maxLen=255] — Field: component_name. Associated component reference.
        - `type` (string) **REQ** [maxLen=255, enum=['_merge_field', 'recipients']] — Represents the type of the configured property associated with the screen state.
      - `transitions` (array of object `GETTransition`) [maxItems=25, nullable] — Represents the list of outgoing transitions from the kiosk state.
        schema: `GETTransition`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the outgoing transition.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the outgoing transition.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Returns no content. The specified kiosk contains no states.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains invalid data or parameters.
**Resolution:** A valid kiosk ID must be specified in the request URL, and all query parameter values must be valid. — Schema: `KioskStateErrorResponse` [application/json]
    > Represents the generic error response for kiosk state operations. Contains an error code, error message, and contextual details about the validation failure.
    schema: `KioskStateErrorResponse`
    - `code` (string) **REQ** [enum=[8 values]] — Represents the error category code indicating the type of validation failure.
    - `details` (object) **REQ** — Represents contextual details about the error. The structure varies by error type and may include the affected field path, expected data type, or resource path.
      - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the error.
      - `json_path` (string) [maxLen=1000] — Represents the JSON path pointing to the problematic field in the request body.
      - `expected_data_type` (string) [maxLen=255] — Represents the expected data type when a type mismatch occurs in the request.
      - `maximum_length` (integer/int32) — Represents the maximum allowed length when a field value exceeds the configured limit.
      - `resource_path_index` (integer/int32) — Represents the index in the resource path that is invalid.
      - `permissions` (array of string) [maxItems=100] — Represents the list of required OAuth scopes when access is denied.
        items: [maxLen=255]
      additionalProperties: any
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing what went wrong.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always 'error' for error responses.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.READ
