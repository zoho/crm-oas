# PUT /settings/kiosks/{kioskId}/actions/activate
**Operation:** `activateKiosk` — Activate Kiosk

> To activate a Kiosk that is in draft or inactive state in Zoho CRM. The Kiosk must contain at least one screen before it can be activated. Once activated, the Kiosk becomes active and can be used for data collection. 

Activate a Kiosk after configuring its states and before using the [Execute a Kiosk API](kiosks_execute.yaml#$.paths./settings/kiosks/{kioskId}/actions/execute.post).

A Kiosk can be in one of three states: 

draft - Not yet activated
active - Currently live and in use
inactive Previously active and later deactivated. 

Use the [Get All Kiosks API](kiosks.yaml#$.paths./settings/kiosks) to retrieve the Kiosk ID. You can activate only a Kiosk that is in the draft or inactive state. Use the Get a [Specific Kiosk API](kiosks.yaml#$.paths./settings/kiosks/{kioskId}.get) to check the current status of the Kiosk from the status key in the response. Example: "status": "draft"

**Note:**
- A Kiosk must contain at least **one** screen to be activated.
- Use the [Create a Kiosk State API](kiosks_states.yaml#$.paths./settings/kiosks/{kioskId}/states.post) to configure and add the necessary components before calling the [Activate Kiosk API](kiosks.yaml#$.paths./settings/kiosks/{kioskId}/actions/activate.put).

Availability: Standard, Professional, Enterprise, and Ultimate editions.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk ID.

**Responses:**

- **200**: Returns a confirmation that the Kiosk has been successfully activated, including a SUCCESS code, a confirmation message, and the ID of the activated Kiosk. — Schema: `KioskActivationSuccessResponse` [application/json]
    > Represents the response returned when a kiosk has been successfully activated, including the operation status.
    schema: `KioskActivationSuccessResponse`
    - `kiosks` (object `KioskActivationStatusItem`) — Represents the status of a kiosk activation operation, including the status code, message, and details of the activated kiosk.
      schema: `KioskActivationStatusItem`
      - `code` (string) [maxLen=255] — Represents the status code returned for the kiosk activation operation.
      - `details` (object `KioskActivationItemDetail`) — Represents the identifier of the activated kiosk returned in an activation operation response.
        schema: `KioskActivationItemDetail`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the kiosk activation item detail.
      - `message` (string) [maxLen=255] — Represents the error message describing the issue.
      - `status` (string) [maxLen=255] — Indicates the outcome status of the kiosk activation operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request could not be processed due to a validation error.
**Resolution:** Review the error code in the response body: INVALID_DATA indicates the Kiosk does not exist, ALREADY_ACTIVATED indicates the Kiosk is already active, and NOT_ALLOWED indicates the Kiosk end state was not collected properly. [application/json]
    > Represents one of three possible error responses returned when the Kiosk activation request fails: a Kiosk already active error, an invalid or non-existent Kiosk error, or a not-allowed activation error.
    oneOf:
      - `KioskAlreadyActiveError` — Represents the error response returned when an activation is attempted on a kiosk that is already active.
        - `code` (string) **REQ** [enum=['ALREADY_ACTIVATED']] — Represents the error code. 
Possible values:
ALREADY_ACTIVATED - The kiosk has already been activated and cannot be activated again.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Identifies the zero-based index of the resource path segment associated with the error.
        - `message` (string) **REQ** [enum=['Kiosk already active']] — Represents the error message describing the issue. Possible values: Kiosk already active
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
      - `KioskTestRunInvalidKioskError` — Represents the error response returned when the specified kiosk identifier is invalid for a test run.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. 
Possible values:
INVALID_DATA - The kiosk specified for the test run does not exist.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the index position within the resource path where the invalid kiosk error was encountered.
        - `message` (string) **REQ** [enum=['No such Kiosk exists']] — Represents the error message describing the issue. Possible values:
No such Kiosk exists
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
      - `KioskActivationNotAllowedError` — Represents the error response returned when kiosk activation is not permitted due to configuration constraints, such as an incomplete end state.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code. Possible values:
NOT_ALLOWED - The kiosk activation is not permitted under the current conditions.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the index position within the resource path where the activation error was encountered.
        - `message` (string) **REQ** [enum=['Kiosk end state not collected properly']] — Represents the error message describing the issue. Possible values:
Kiosk end state not collected properly
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.UPDATE
