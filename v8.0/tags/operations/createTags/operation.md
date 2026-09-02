# POST /settings/tags
**Operation:** `createTags` — Tags
> To create tags for a module in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, required) [maxLen=100]: Specify the API name of the module. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.

**Schemas:**
`CreatedByNested`:
  > Represents the user who created the tag.
  - `name` (string) [maxLen=255] — Represents the display name of the user who created the tag.
  - `id` (string) [maxLen=255] — Represents the unique ID of the user who created the tag.
`DetailsNested`:
  > Represents the detailed metadata of the tag, including timestamps, the tag name, color code, and the users who created and last modified it.
  - `created_time` (string/date-time) [maxLen=255] — Represents the creation date and time of the tag.
  - `modified_time` (string/date-time) [maxLen=255] — Represents the last modification date and time of the tag.
  - `name` (string) [maxLen=255] — Represents the name of the tag.
  - `modified_by` (object `ModifiedByNested`) — Represents the user who last modified the tag.
  - `id` (string) [maxLen=255] — Represents the unique ID of the tag.
  - `created_by` (object `CreatedByNested`) — Represents the user who created the tag.
  - `color_code` (string) [maxLen=255, nullable] — Represents the hex color code assigned to the tag, such as **#FF0000**. The value is null when no color is assigned.
`DuplicateTagError`:
  > Represents an error response returned when a tag with the same name already exists in the module.
  - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code **DUPLICATE_DATA**.
  - `details` (object) **REQ** — Represents the error details object containing validation information.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the duplicate data error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that contains the duplicate value.
    - `id` (string) [maxLen=255] — Represents the ID of the duplicate tag record.
  - `message` (string) **REQ** [enum=['duplicate data']] — Represents the error message describing the duplicate data condition.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
`ModifiedByNested`:
  > Represents the user who last modified the tag.
  - `name` (string) [maxLen=255] — Represents the display name of the user who last modified the tag.
  - `id` (string) [maxLen=255] — Represents the unique ID of the user who last modified the tag.

**Request Body** — application/json `PosttagsRequest`
> The request body must contain a **tags** array with one tag object. Each object must include the **name** and an optional **color_code**.
  > Represents the request body schema for the create tag operation.
  - `tags` (array of object `TagsNested`) [maxItems=1] **REQ** — Represents an array of tag objects to create. The array can contain a maximum of one item.
    schema: `TagsNested`
    - `name` (string) **REQ** [maxLen=26] — Specify the name of the tag. The maximum allowed length is 26 characters.
    - `color_code` (string) [maxLen=7, nullable] — Specify the hex color code for the tag, such as **#FF0000**. Set to null to remove the assigned color.
    additionalProperties: any

**Responses:**

- **201**: Returns a success response for a successful tag creation. The response includes the tag details and metadata. — Schema: `PosttagsResponse201` [application/json]
    > Represents the response body for a successful tag creation.
    schema: `PosttagsResponse201`
    - `tags` (array of object `TagsNested1`) [maxItems=20] — Represents an array containing the result of the tag creation operation.
      schema: `TagsNested1`
      - `code` (string) [maxLen=255] — Represents the operation result code for the tag.
      - `details` (object `DetailsNested`) — Represents the detailed metadata of the tag, including timestamps, the tag name, color code, and the users who created and last modified it.
      - `message` (string) [maxLen=255] — Represents the operation result message for the tag.
      - `status` (string) [maxLen=255] — Represents the status of the tag operation.

- **207**: Returns a multi-status response when the request partially succeeds or fails. Each item in the **tags** array indicates whether the operation succeeded or provides the failure reason. [application/json]
    > Represents a multi-status response containing the operation result for each tag in the request.
    - `tags` (array of object) [minItems=2, maxItems=200] **REQ** — Represents an array of tag operation result objects. Each item indicates whether the operation succeeded or contains the failure reason.
      oneOf:
        - `Post207multistatusResponse207` — Represents a single tag operation result item in a multi-status response.
          - `code` (string) [maxLen=255] — Represents the operation result code for the tag item.
          - `details` (object `DetailsNested`) — Represents the detailed metadata of the tag, including timestamps, the tag name, color code, and the users who created and last modified it.
          - `message` (string) [maxLen=255] — Represents the operation result message for the tag item.
          - `status` (string) [maxLen=255] — Represents the operation result status for the tag item.
        - `DuplicateTagError` — Represents an error response returned when a tag with the same name already exists in the module.

- **400**: Returns an error response when the request contains invalid data.
**Resolution:** Check the error code and details to identify and correct the invalid field values. [application/json]
    > Represents one of the possible error responses returned for a 400 Bad Request.
    oneOf:
        - `tags` (array of object) [maxItems=25] **REQ** — Represents an array of error objects for the invalid tag request.
          oneOf:
            - `TagsLicenseLimitExceededError` — Represents an error response returned when the tag creation limit for the module has been reached on the current plan.
              - `code` (string) **REQ** [enum=['LICENSE_LIMIT_EXCEEDED']] — Represents the error code **LICENSE_LIMIT_EXCEEDED**.
              - `details` (object) **REQ** — Represents the error details object.
              - `message` (string) **REQ** [enum=['tags edition limit exceeded']] — Represents the error message indicating the tag limit for the plan has been reached.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `InvalidTagColorCodeError` — Represents an error response returned when the tag color code value is invalid or exceeds the maximum length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
              - `details` (object) **REQ** — Represents the error details object containing validation information.
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the color code field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with the invalid color code.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field with the invalid color code.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid color code.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `TagInvalidDataError` — Represents an error response returned when a field value is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
              - `details` (object) **REQ** — Represents the error details object containing validation information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with the invalid value.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field with the invalid value.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `MandatoryFieldNotFoundError` — Represents an error response returned when a required field is missing from the request body.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code **MANDATORY_NOT_FOUND**.
              - `details` (object) **REQ** — Represents the error details object containing validation information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing mandatory field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing mandatory field.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the missing mandatory field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `DuplicateTagError` — Represents an error response returned when a tag with the same name already exists in the module.
            - `RequiredFieldMissingError` — Represents an error response returned when a required field is absent from the request body.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code **MANDATORY_NOT_FOUND**.
              - `details` (object) **REQ** — Represents the error details object containing validation information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing required field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing required field.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message describing the missing required field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `InvalidDataTypeError` — Represents an error response returned when a field value has an invalid data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
              - `details` (object) **REQ** — Represents the error details object containing validation information.
                - `expected_data_type` (string) [maxLen=255] — Represents the expected data type for the field.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid data type.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field with the invalid data type.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message describing the invalid data type.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `TagFieldMaxLengthError` — Represents an error response returned when a field value exceeds the allowed maximum length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
              - `details` (object) **REQ** — Represents the error details object containing validation information.
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that exceeds the maximum length.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that exceeds the maximum length.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message describing the maximum length violation.
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
      - `RequiredModuleParamError` — Represents an error response returned when the required **module** query parameter is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code **REQUIRED_PARAM_MISSING**.
        - `details` (object) **REQ** — Represents the error details object containing the missing parameter information.
          - `param` (string) **REQ** [maxLen=255] — Represents the name of the missing required parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message indicating the module parameter is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
      - `InvalidRequestMethodError` — Represents an error response returned when the HTTP request method is not valid for this endpoint.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code **INVALID_REQUEST_METHOD**.
        - `details` (object) **REQ** — Represents the error details object.
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Represents the error message indicating the HTTP method is not valid for this endpoint.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

- **403**: Returns an error response when the user does not have permission to create tags.
**Resolution:** Ensure the access token includes the **ZohoCRM.settings.tags.CREATE** scope. — Schema: `NoTagPermissionError` [application/json]
    > When the user does not have sufficient permissions
    schema: `NoTagPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code **NO_PERMISSION**.
    - `details` (object) **REQ** — Represents the error details object containing permission information.
      - `permissions` (array of string) [maxItems=25] **REQ** — Represents an array of the required permissions for the operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating insufficient permissions.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

- **404**: Returns an error response when the URL does not match a known endpoint.
**Resolution:** Verify the request URL against the API documentation. — Schema: `InvalidUrlPatternError` [application/json]
    > When the requested URL pattern is invalid
    schema: `InvalidUrlPatternError`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code **INVALID_URL_PATTERN**.
    - `details` (object) **REQ** — Represents the error details object.
    - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] — Represents the error message indicating the URL does not match a known pattern.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.tags.CREATE
