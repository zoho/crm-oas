# DELETE /settings/kiosks/{kioskId}/actions/activate
**Operation:** `deactivateKiosk` — Deactivate a Kiosk
> To deactivate an active Kiosk in your Zoho CRM account. Once deactivated, the Kiosk will no longer be accessible for users. Use the [Get All Kiosks API](kiosks.yaml#$.paths./settings/kiosks) to retrieve the Kiosk ID.

**Note**

- A Kiosk must be in the Active (Published) state before it can be deactivated. After deactivation, its status changes to inactive. To make the Kiosk active again, use the [Activate Kiosk API](kiosks.yaml#$.paths./settings/kiosks/{kioskId}/actions/activate.put).
- You cannot deactivate a Kiosk that has existing associations. For example, if the Kiosk is associated with the Record Details View or any other supported component, you must remove those associations before deactivating the Kiosk.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk ID.

**Responses:**

- **200**: Returns a confirmation that the specified kiosk was successfully deactivated in Zoho CRM. The response body contains the kiosk ID, a `SUCCESS` status code, and a confirmation message indicating that the kiosk is now inactive. — Schema: `KioskDeactivationSuccessResponse` [application/json]
    > Represents the response returned when a kiosk has been successfully deactivated, including the operation status.
    schema: `KioskDeactivationSuccessResponse`
    - `kiosks` (object `KioskDeactivationStatusItem`) — Represents the status of a kiosk deactivation operation, including the status code, message, and details of the deactivated kiosk.
      schema: `KioskDeactivationStatusItem`
      - `code` (string) [maxLen=255] — Represents the status code returned for the kiosk deactivation operation.
      - `details` (object `KioskDeactivationItemDetail`) — Represents the identifier of the deactivated kiosk returned in a deactivation operation response.
        schema: `KioskDeactivationItemDetail`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the kiosk deactivation item detail.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the kiosk deactivation operation.
      - `status` (string) [maxLen=255] — Indicates the result status of the kiosk deactivation operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The deactivation request failed due to a client-side error.
**Resolution:** Verify that the kiosk ID is valid (`INVALID_DATA`), that the kiosk has not already been deactivated (`ALREADY_DEACTIVATED`), and that the kiosk has no active associations with other components before attempting deactivation (`NOT_ALLOWED`). [application/json]
    > Represents one of three error conditions returned when the deactivation request cannot be fulfilled: the kiosk ID is invalid (`INVALID_DATA`), the kiosk is already inactive (`ALREADY_DEACTIVATED`), or the kiosk has existing associations with other components that prevent deactivation (`NOT_ALLOWED`).
    oneOf:
      - `KioskTestRunInvalidKioskError` — Represents the error response returned when the specified kiosk identifier is invalid for a test run.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. 
Possible values:
INVALID_DATA - The kiosk specified for the test run does not exist.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the index position within the resource path where the invalid kiosk error was encountered.
        - `message` (string) **REQ** [enum=['No such Kiosk exists']] — Represents the error message describing the issue. Possible values:
No such Kiosk exists
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
      - `KioskDeactivationNotAllowedError` — Represents the error response returned when kiosk deactivation is blocked due to existing associations with other components.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code. Possible values:
NOT_ALLOWED - The kiosk deactivation is not permitted because the kiosk is associated with other components.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the index position within the resource path where the deactivation error was encountered.
        - `message` (string) **REQ** [enum=['Kiosk associated other components']] — Represents the error message describing the issue. Possible values:
Kiosk associated other components
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
      - `KioskAlreadyInactiveError` — Represents the error response returned when a deactivation is attempted on a kiosk that is already inactive.
        - `code` (string) **REQ** [enum=['ALREADY_DEACTIVATED']] — Represents the error code. Possible values:
ALREADY_DEACTIVATED - Indicates the kiosk has already been deactivated.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Identifies the zero-based index of the resource path segment associated with the error.
        - `message` (string) **REQ** [enum=['Kiosk already deactive']] — Represents the error message describing the issue. Possible values:
Kiosk already deactive
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.DELETE
