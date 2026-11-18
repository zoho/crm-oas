# DELETE /settings/webforms/{id}
**Operation:** `deleteWebform` — Delete a webform by ID

> To delete a specific webform from your Zoho CRM organization, send a DELETE request with the webform ID. The webform is permanently removed and the operation cannot be undone.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique [Webform ID](webforms.yaml#$.paths./settings/webforms.get).
- `module` (query, string, required) [enum=['Leads']]: Specify the module API name of the CRM module for which the webform is being created or updated. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Schemas:**
`ErrorResponse`:
  > Represents a generic API error response containing an error code, status, message, and details.
  - `code` (string) **REQ** [enum=[18 values]] — Represents the error code that identifies the type of error returned by the API.
  - `details` (object) **REQ** — Represents additional details providing context about the error, such as the invalid field name or parameter.
  - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the reason for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.

**Responses:**

- **200**: Returns a `webforms` array containing a success object with the status and ID of the deleted webform.
 — Schema: `WebformsSuccessResponse` [application/json]
    > Represents the success response for a webform create or update operation, including the result status for each webform.
    schema: `WebformsSuccessResponse`
    - `webforms` (array of object `SuccessResponse`) [maxItems=1] — Contains the list of webform result objects in the success response.
      schema: `SuccessResponse`
      - `code` (string) [enum=['SUCCESS']] — Represents the status code of the API response.
      - `details` (object) — Represents additional details about the API response, such as the ID of the created or modified resource.
      - `message` (string) [maxLen=255] — Represents the response message describing the outcome of the operation.
      - `status` (string) [enum=['success']] — Represents the status of the API response. Possible values: success - The operation was successful.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request failed due to an invalid or missing parameter, an invalid module name, or a deletion constraint violation.
**Resolution:** The caller must ensure the webform `id` path parameter and `module` query parameter are valid and present, and that the webform is not associated with active records before attempting deletion. — Schema: `ErrorResponse` [application/json]
    > Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The user does not have permission to delete the webform.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `ErrorResponse` [application/json]
    > Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.DELETE
