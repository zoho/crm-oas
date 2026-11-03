# DELETE /settings/kiosks/{kioskId}
**Operation:** `deleteKiosk` — Delete a kiosk
> To delete an existing Kiosk from your Zoho CRM organization. The deletion removes the entire Kiosk entry, including all states created within it, along with any related data. You can delete Draft Kiosks, Deactivated Kiosks, and Published Kiosks that are not associated with any supported locations, such as the Home Page, Setup Page, Custom Buttons, or the Record Details View. 

Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk ID.

Available in: Standard, Professional, Enterprise, and Ultimate editions.

**Note:**

You can delete:
   - Draft Kiosks
   - Deactivated Kiosks
   - Published Kiosks that are not associated with any supported locations, such as the Home Page, Setup Page, Custom Buttons, or the Record Details View.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk ID.

**Responses:**

- **200**: Returns the deletion result for the specified kiosk, including the operation status code, a confirmation message, and the ID of the deleted kiosk. — Schema: `KioskDeleteResponse` [application/json]
    > Represents the response returned after deleting a single kiosk, containing one per-item operation result.
    schema: `KioskDeleteResponse`
    - `kiosks` (array of object `KioskDeleteActionResult`) [maxItems=1] — Contains the list of kiosk result objects from the delete operation.
      schema: `KioskDeleteActionResult`
      - `code` (string) [maxLen=255] — Represents the result code of the kiosk delete operation.
      - `details` (object `KioskDeleteResultDetails`) — Represents the identifier of the kiosk deleted in a single delete operation.
        schema: `KioskDeleteResultDetails`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the deleted kiosk.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the kiosk delete operation.
      - `status` (string) [maxLen=255] — Indicates the result status of the kiosk delete operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request could not be completed due to a validation error or a restriction on the operation.
**Resolution:** The kiosk ID in the request path must be valid, or the kiosk must not be associated with any supported locations before deletion. [application/json]
    > Represents the error response schema for a failed delete operation. Contains one of two possible error variants: a not-found error when the specified kiosk ID does not exist (INVALID_DATA), or a not-allowed error when the kiosk is associated with one or more supported locations (NOT_ALLOWED).

    oneOf:
      - `KioskErrorNotFound` — Represents the error response returned when a kiosk with the specified identifier does not exist.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - No kiosk was found with the specified identifier.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the index position within the resource path where the not-found error occurred.
        - `message` (string) **REQ** [enum=['No such Kiosk exists']] — Represents the error message describing the issue. Possible values:
No such Kiosk exists
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
      - `KioskErrorNotAllowedDelete` — Represents the error response returned when a kiosk cannot be deleted because it is active or associated with other components.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code. Possible values:
NOT_ALLOWED - The kiosk cannot be deleted because it is associated with other components.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the index position within the resource path where the delete restriction was encountered.
        - `message` (string) **REQ** [enum=['Kiosk associated other components']] — Represents the error message describing the issue. Possible values:
Kiosk associated other components
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.DELETE
