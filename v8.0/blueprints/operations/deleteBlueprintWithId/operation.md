# DELETE /settings/blueprints/{blueprintId}
**Operation:** `deleteBlueprintWithId` — Blueprint
> Delete a specific blueprint by its blueprintId

**Parameters:**
- `blueprintId` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+] {style=simple, explode=False}: Specify the unique ID of the Blueprint to delete. Use the [Get Blueprint by ID](blueprints.yaml#$.paths./settings/blueprints.get) to retrieve the Blueprint ID.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Represents the custom header used to identify the calling service.

**Responses:**

- **200**: OK - Successful response — Schema: `DeleteSingleBlueprintResponse` [application/json]
    > Represents the response returned when the Blueprint is successfully deleted.
    schema: `DeleteSingleBlueprintResponse`
    - `blueprints` (array of object `DeleteBlueprintStatusItem`) [maxItems=1] — Represents the list containing the deletion status of the specified Blueprint.
      schema: `DeleteBlueprintStatusItem`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code indicating the outcome of the Blueprint deletion.

Possible values:
SUCCESS - Indicates that the Blueprint deletion completed successfully.
      - `details` (object `ActionDetails`) **REQ** — Represents the details of the object referenced by the transition action, such as a tag, record, or webhook, depending on the configured action type.
        schema: `ActionDetails`
        - `name` (string) [maxLen=50, nullable] — Represents the name of the object referenced by this action, such as a tag or webhook, depending on the configured action type.
        - `id` (string) [maxLen=255] — Represents the unique ID of the object referenced by this action, such as a tag, record, or webhook, depending on the configured action type.
        additionalProperties: any
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the outcome of the Blueprint deletion.
      - `status` (string) **REQ** [maxLen=255] — Represents the status of the Blueprint deletion operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
      - `RequiredHeaderMissingError` — Represents the error returned when the required X-CRM-ORG header is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_HEADER_MISSING']] — Represents the error code returned by this response.

Possible values:
REQUIRED_HEADER_MISSING - Indicates that one of the expected headers is missing.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `header_name` (string) **REQ** [maxLen=255] — Represents the name of the missing header.
        - `message` (string) **REQ** [enum=['One of the expected headers is missing']] — Represents the error message returned by this response.

Possible values:
One of the expected headers is missing - Indicates that one of the expected headers is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `DeleteInvalidBlueprintIdError` — Represents the error returned when the Blueprint ID provided in the request is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when an invalid Blueprint ID is specified.

Possible values:
INVALID_DATA - Indicates that the provided Blueprint ID is invalid.
        - `details` (object) **REQ** — Represents the details object with validation information about the invalid Blueprint ID.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path that identifies the invalid Blueprint ID.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the provided Blueprint ID is invalid.

Possible values:
the id given seems to be invalid - Indicates that the specified Blueprint ID does not exist or is malformed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Forbidden - The user does not have permission to perform this action. — Schema: `NoPermissionError` [application/json]
    > Represents the error returned when the user does not have permission to perform this action.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned by this response.

Possible values:
NO_PERMISSION - Indicates that the request contains invalid or unexpected data.
    - `details` (object) **REQ** — Represents the details object with validation information about the error.
      - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to perform this action.
        items: [maxLen=100]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message returned by this response.

Possible values:
permission denied - Indicates that permission denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.DELETE
