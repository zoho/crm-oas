# GET /settings/tags
**Operation:** `getTags` — Tags
> To retrieve all tags associated with a module in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, required) [maxLen=100]: Specify the API name of the module. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.
- `include` (query, string, optional) [enum=['type', 'associated_record_count', 'last_accessed_time']]: Specify the additional tag properties to include in the response. Possible values: **type**, **associated_record_count**, **last_accessed_time**.

**Responses:**

- **200**: Returns a list of tags for the specified module, along with pagination and limit details. — Schema: `GettagsResponse200` [application/json]
    > Represents the response body for a successful tag list retrieval.
    schema: `GettagsResponse200`
    - `tags` (array of object `GETTagsNested`) [maxItems=484] **REQ** — Represents an array of tag objects returned for the module.
      schema: `GETTagsNested`
      - `created_time` (string/date-time) **REQ** [maxLen=255] — Represents the creation date and time of the tag.
      - `modified_time` (string/date-time) **REQ** [maxLen=255] — Represents the last modification date and time of the tag.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the tag.
      - `modified_by` (object `GETModifiedByNested`) **REQ** — Represents the user who last modified the tag in the GET response.
        schema: `GETModifiedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who last modified the tag.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who last modified the tag.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the tag.
      - `created_by` (object `GETCreatedByNested`) **REQ** — Represents the user who created the tag in the GET response.
        schema: `GETCreatedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who created the tag.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who created the tag.
      - `color_code` (string) **REQ** [maxLen=255, nullable] — Represents the hex color code assigned to the tag, such as **#FF0000**. The value is null when no color is assigned.
    - `info` (object `GETInfoNested`) **REQ** — Represents pagination and limit information for the tag list response.
      schema: `GETInfoNested`
      - `record_limit` (integer/int32) — Represents the maximum number of records a tag can be applied to.
      - `count` (integer/int32) **REQ** — Represents the total number of tags returned in the response.
      - `allowed_count` (integer/int32) **REQ** — Represents the maximum number of tags allowed for the module in your plan.

- **400**: Returns an error response when the request contains invalid parameters.
**Resolution:** Check the error code and verify the module name is correct. [application/json]
    > Represents one of the possible error responses returned for a 400 Bad Request.
    oneOf:
      - `RequiredModuleParamError` — Represents an error response returned when the required **module** query parameter is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code **REQUIRED_PARAM_MISSING**.
        - `details` (object) **REQ** — Represents the error details object containing the missing parameter information.
          - `param` (string) **REQ** [maxLen=255] — Represents the name of the missing required parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message indicating the module parameter is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
      - `InvalidModuleError` — Represents an error response returned when the specified module name is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code **INVALID_MODULE**.
        - `details` (object) **REQ** — Represents the error details object.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message describing the invalid module name.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
      - `ModuleTagsNotSupportedError` — Represents an error response returned when the specified module does not support tags.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code **INVALID_MODULE**.
        - `details` (object) **REQ** — Represents the error details object.
        - `message` (string) **REQ** [enum=['the given module is not supported for this api']] — Represents the error message indicating the module does not support tags.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
      - `InvalidRequestMethodError` — Represents an error response returned when the HTTP request method is not valid for this endpoint.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code **INVALID_REQUEST_METHOD**.
        - `details` (object) **REQ** — Represents the error details object.
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Represents the error message indicating the HTTP method is not valid for this endpoint.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

- **403**: Returns an error response when the user does not have permission to read tags.
**Resolution:** Ensure the access token includes the **ZohoCRM.settings.tags.READ** scope. — Schema: `NoTagPermissionError` [application/json]
    > When the user does not have sufficient permissions to access the resource
    schema: `NoTagPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code **NO_PERMISSION**.
    - `details` (object) **REQ** — Represents the error details object containing permission information.
      - `permissions` (array of string) [maxItems=25] **REQ** — Represents an array of the required permissions for the operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating insufficient permissions.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

- **404**: Returns an error response when the URL does not match a known endpoint.
**Resolution:** Verify the request URL against the API documentation. — Schema: `InvalidUrlPatternError` [application/json]
    > When the requested resource is not found
    schema: `InvalidUrlPatternError`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code **INVALID_URL_PATTERN**.
    - `details` (object) **REQ** — Represents the error details object.
    - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] — Represents the error message indicating the URL does not match a known pattern.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.tags.READ
