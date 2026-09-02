# DELETE /settings/tags/{id}
**Operation:** `deleteTags` — Delete tag by ID
> To delete a tag by its ID from your Zoho CRM organization.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique ID of the tag.

**Responses:**

- **200**: Returns a success response for a successful tag deletion. The response includes the deleted tag details. — Schema: `DeletetagsResponse200` [application/json]
    > Represents the response body for a successful tag deletion.
    schema: `DeletetagsResponse200`
    - `tags` (array of object `TagsNested1`) [maxItems=1] — Represents an array containing the result of the tag deletion operation.
      schema: `TagsNested1`
      - `code` (string) [maxLen=255] — Represents the operation result code for the tag.
      - `details` (object `DetailsNested`) — Represents the detailed metadata of the tag, including timestamps, the tag name, color code, and the users who created and last modified it.
        schema: `DetailsNested`
        - `created_time` (string/date-time) [maxLen=255] — Represents the creation date and time of the tag.
        - `modified_time` (string/date-time) [maxLen=255] — Represents the last modification date and time of the tag.
        - `name` (string) [maxLen=255] — Represents the name of the tag.
        - `modified_by` (object `ModifiedByNested`) — Represents the user who last modified the tag.
          schema: `ModifiedByNested`
          - `name` (string) [maxLen=255] — Represents the display name of the user who last modified the tag.
          - `id` (string) [maxLen=255] — Represents the unique ID of the user who last modified the tag.
        - `id` (string) [maxLen=255] — Represents the unique ID of the tag.
        - `created_by` (object `CreatedByNested`) — Represents the user who created the tag.
          schema: `CreatedByNested`
          - `name` (string) [maxLen=255] — Represents the display name of the user who created the tag.
          - `id` (string) [maxLen=255] — Represents the unique ID of the user who created the tag.
        - `color_code` (string) [maxLen=255, nullable] — Represents the hex color code assigned to the tag, such as **#FF0000**. The value is null when no color is assigned.
      - `message` (string) [maxLen=255] — Represents the operation result message for the tag.
      - `status` (string) [maxLen=255] — Represents the status of the tag operation.

- **400**: Returns an error response when the request is invalid or the tag is not found.
**Resolution:** Check the error code and verify the tag ID is correct. [application/json]
    > Represents one of the possible error responses returned for a 400 Bad Request.
    oneOf:
      - `InvalidRequestMethodError` — Represents an error response returned when the HTTP request method is not valid for this endpoint.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code **INVALID_REQUEST_METHOD**.
        - `details` (object) **REQ** — Represents the error details object.
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Represents the error message indicating the HTTP method is not valid for this endpoint.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
      - `TagNotFoundError` — Represents an error response returned when the specified tag ID does not exist.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
        - `details` (object) **REQ** — Represents the error details object.
          - `id` (string) **REQ** [maxLen=255] — Represents the ID of the tag that was not found.
        - `message` (string) **REQ** [enum=['tags not found']] — Represents the error message indicating the tag was not found.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
      - `InvalidModuleError` — Represents an error response returned when the specified module name is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code **INVALID_MODULE**.
        - `details` (object) **REQ** — Represents the error details object.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message describing the invalid module name.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

- **403**: Returns an error response when the user does not have permission to delete tags.
**Resolution:** Ensure the access token includes the **ZohoCRM.settings.tags.DELETE** scope. — Schema: `NoTagPermissionError` [application/json]
    > When Tag read permission is not available.
    schema: `NoTagPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code **NO_PERMISSION**.
    - `details` (object) **REQ** — Represents the error details object containing permission information.
      - `permissions` (array of string) [maxItems=25] **REQ** — Represents an array of the required permissions for the operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating insufficient permissions.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

- **404**: Returns an error response when the URL does not match a known endpoint.
**Resolution:** Verify the request URL against the API documentation. — Schema: `InvalidUrlPatternError` [application/json]
    > When a invalid URL Pattern is given
    schema: `InvalidUrlPatternError`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code **INVALID_URL_PATTERN**.
    - `details` (object) **REQ** — Represents the error details object.
    - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] — Represents the error message indicating the URL does not match a known pattern.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.tags.DELETE
