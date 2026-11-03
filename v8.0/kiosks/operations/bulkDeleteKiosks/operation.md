# DELETE /settings/kiosks
**Operation:** `bulkDeleteKiosks` — Kiosk Deletion
> To delete one or more Kiosks from your Zoho CRM account. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk IDs.

**Note:**

You can delete:
 - Draft Kiosks.
 - Deactivated Kiosks.
 - Published Kiosks that are not associated with any supported locations, such as the Home Page, Setup Page, Custom Buttons, or the Record Details View.

Available in the Standard, Professional, Enterprise, and Ultimate editions.


**Parameters:**
- `ids` (query, string, required) [maxLen=1000]: Comma-separated list of kiosk IDs to delete in bulk.

**Responses:**

- **200**: Returns a per-Kiosk deletion result for each Kiosk ID submitted in the request. Each entry in the kiosks array confirms the deletion status of the corresponding Kiosk, including a result code and the ID of the deleted Kiosk. — Schema: `KioskBulkDeleteResponse` [application/json]
    > Represents the response returned after a bulk kiosk deletion. Contains an array of per-item operation results.
    schema: `KioskBulkDeleteResponse`
    - `kiosks` (array of object `KioskBulkDeleteActionResult`) [maxItems=50] — Contains the list of kiosk result objects.
      schema: `KioskBulkDeleteActionResult`
      - `code` (string) [maxLen=255] — Represents the result code indicating the outcome of the bulk delete action for the kiosk.
      - `details` (object `KioskBulkDeleteResultDetails`) — Represents the identifier of each kiosk deleted in a bulk delete operation.
        schema: `KioskBulkDeleteResultDetails`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the kiosk.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the bulk delete action for the kiosk.
      - `status` (string) [maxLen=255] — Represents the result status of the bulk delete action for the kiosk.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to a missing required parameter, an invalid Kiosk ID, or an attempt to delete a Kiosk that is associated with one or more supported locations. [application/json]
    > Represents one of the possible error responses returned when a bulk Kiosk deletion request fails. The response can indicate a missing required parameter, an invalid Kiosk ID, or an attempt to delete a Kiosk that is associated with one or more supported locations.
    oneOf:
      - `KioskErrorRequiredParamMissing` — Represents the error response returned when the required ids parameter is missing for a bulk kiosk deletion.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code. Possible values:
REQUIRED_PARAM_MISSING - A required query parameter is missing from the request.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `param_name` (string) **REQ** [maxLen=255] — Identifies the name of the required parameter that is missing from the request.
        - `message` (string) **REQ** [enum=['One of the expected param is missing']] — Represents the error message describing the issue. Possible values:
One of the expected param is missing
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
      - `KioskErrorNotFoundBulk` — Represents the error response returned when one or more referenced kiosks do not exist during a bulk operation.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - No kiosk was found with the specified identifier.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the kiosk that was not found.
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
