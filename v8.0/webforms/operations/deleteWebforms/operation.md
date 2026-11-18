# DELETE /settings/webforms
**Operation:** `deleteWebforms` — Delete webforms by IDs
> To delete multiple webforms from Zoho CRM, specify the IDs of
the webforms to be removed.

**Note:**
- When multiple Webform IDs are passed, if some deletions succeed and others fail, the API responds with **207 Multi-Status**. Check the **status** key in each response item to see the result of each deletion.
- If an invalid or non-existent Webform ID is provided, the deletion fails for that entry. The API returns an error code and message for the specific entry in the response.


**Parameters:**
- `ids` (query, number, required) [enum=[4149211000002945500]]: Specify the comma-separated list of webform IDs for bulk delete or other bulk operations. Use the [Get Webforms API](webforms.yaml#$.paths./settings/webforms.get) to retrieve the webform IDs.
- `trigger_source` (query, string, optional) [enum=['admin_center']]: Specify the source that triggered the webform deletion.
- `module` (query, string, optional) [enum=['Leads']]: Specify the module API name to filter webforms by the target CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Schemas:**
`ErrorResponse`:
  > Represents a generic API error response containing an error code, status, message, and details.
  - `code` (string) **REQ** [enum=[18 values]] — Represents the error code that identifies the type of error returned by the API.
  - `details` (object) **REQ** — Represents additional details providing context about the error, such as the invalid field name or parameter.
  - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the reason for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.
`SuccessResponse`:
  > Represents an API success response, including the status code, message, and additional details.
  - `code` (string) [enum=['SUCCESS']] — Represents the status code of the API response.
  - `details` (object) — Represents additional details about the API response, such as the ID of the created or modified resource.
  - `message` (string) [maxLen=255] — Represents the response message describing the outcome of the operation.
  - `status` (string) [enum=['success']] — Represents the status of the API response. Possible values: success - The operation was successful.

**Responses:**

- **200**: Returns the deletion status for each requested webform. Each item in the response includes a success code, the deleted webform ID, and a confirmation message. — Schema: `DeletewebformsResponse200` [application/json]
    > Returns a successful webform deletion response with per-webform status results.
    schema: `DeletewebformsResponse200`
    - `webforms` (array of object `SuccessResponse`) [maxItems=100] — Contains the list of webform records reflecting the outcome of the delete operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a mixed-status response when the DELETE request includes both valid and invalid webform IDs. Each item in the response indicates either a successful deletion or an error for the corresponding ID. — Schema: `DeletewebformsResponse207` [application/json]
    > Returns a multi-status webform deletion response in which each item independently indicates success or failure.
    schema: `DeletewebformsResponse207`
    - `webforms` (array of object) [maxItems=100] — Contains the list of webform records reflecting the mixed-status outcome of the delete operation, where each entry indicates an individual success or failure result.
      oneOf:
        - `SuccessResponse` — Represents an API success response, including the status code, message, and additional details.
        - `ErrorResponse` — Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains invalid or missing parameters.
**Resolution:** Verify that the `ids` parameter is present and contains valid webform IDs belonging to the specified module, that the `trigger_source` value is valid, and that the module name is correct. [application/json]
    > Represents the error response body for a failed webform DELETE request. Contains either a wrapped object with a webforms array of error objects or a single error object.
    anyOf:
        - `webforms` (array of object `ErrorResponse`) [maxItems=100] **REQ** — Represents the list of error objects returned when one or more webform delete operations fail.
      - `ErrorResponse` — Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.DELETE
