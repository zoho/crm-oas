# DELETE /settings/blueprints
**Operation:** `deleteBlueprint` — Delete one or more Blueprints
> To delete one or more Blueprints from your Zoho CRM organization. When multiple Blueprint IDs are passed, if some deletions succeed and others fail, the API responds with **207 Multi-Status**. Check the status key in each response item to see the result of each deletion.

**Parameters:**
- `X-ZOHO-SERVICE` (header, string, optional) [enum=['automation']] {style=simple, explode=False}: Represents the custom header used to identify the calling service.
- `ids` (query, array, required) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Represents the comma-separated list (CSV) of up to 100 [unique Blueprint IDs](blueprints.yaml#$.paths./settings/blueprints.get) to filter the results.

**Schemas:**
`ActionDetails`:
  > Represents the details of the object referenced by the transition action, such as a tag, record, or webhook, depending on the configured action type.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the object referenced by this action, such as a tag or webhook, depending on the configured action type.
  - `id` (string) [maxLen=255] — Represents the unique ID of the object referenced by this action, such as a tag, record, or webhook, depending on the configured action type.
  additionalProperties: any
`DeleteBlueprintStatusItem`:
  > Represents an individual Blueprint's deletion status.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code indicating the outcome of the Blueprint deletion.

Possible values:
SUCCESS - Indicates that the Blueprint deletion completed successfully.
  - `details` (object `ActionDetails`) **REQ** — Represents the details of the object referenced by the transition action, such as a tag, record, or webhook, depending on the configured action type.
  - `message` (string) **REQ** [maxLen=255] — Represents the message describing the outcome of the Blueprint deletion.
  - `status` (string) **REQ** [maxLen=255] — Represents the status of the Blueprint deletion operation.

**Responses:**

- **200**: Returns the list of successfully deleted Blueprints with their IDs and confirmation messages. — Schema: `DeleteBlueprintSuccessResponse` [application/json]
    > Represents the response returned when the specified blueprints are successfully deleted.
    schema: `DeleteBlueprintSuccessResponse`
    - `blueprints` (array of object `DeleteBlueprintStatusItem`) [maxItems=2] — Represents the list of blueprints and their deletion status returned in the success response.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a multi-status response containing both successful Blueprint deletions and errors for invalid Blueprint IDs when multiple Blueprints are requested for deletion. — Schema: `DeleteBlueprintPartialResponse` [application/json]
    > Represents the response returned when some of the specified blueprints are not deleted.
    schema: `DeleteBlueprintPartialResponse`
    - `blueprints` (array of object) [maxItems=100] — Represents the list of blueprints and their deletion status returned in a partial success response.
      oneOf:
        - `DeleteBlueprintStatusItem` — Represents an individual Blueprint's deletion status.
        - `InvalidValueResponse` — Represents the error returned when invalid module data is provided during a reorder request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the request contains invalid or unexpected data.
          - `details` (object) **REQ** — Represents the details object with validation information about the error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the invalid field.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message returned when the specified value is invalid.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
        - `DeleteBlueprintIdInvalidError` — Represents the error returned when the Blueprint ID provided in a DELETE request is invalid.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the specified Blueprint ID is invalid.

Possible values:
INVALID_DATA - Indicates that the provided Blueprint ID is invalid.
          - `details` (object) **REQ** — Represents the details object that identifies the invalid Blueprint ID.
            - `id` (string) **REQ** [maxLen=255] — Represents the invalid Blueprint ID value.
          - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the provided Blueprint ID is invalid.

Possible values:
the id given seems to be invalid - Indicates that the specified Blueprint ID does not exist or is malformed.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request — The request cannot be processed due to invalid syntax or missing required parameters.
**Resolution:** Specify a valid Blueprint ID, include all required headers and query parameters, and use the DELETE HTTP method for this endpoint. [application/json]
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
      - `DeleteBlueprintRequiredParamMissingError` — Represents the error returned when the required ids query parameter is missing from the bulk DELETE request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when a required parameter is missing from the delete Blueprint request.

Possible values:
REQUIRED_PARAM_MISSING - Indicates that a required parameter was not provided in the request.
        - `details` (object) **REQ** — Represents the details object identifying the missing required parameter.
          - `param_name` (string) **REQ** [enum=['ids']] — Represents the name of the missing required parameter.

Possible values:
ids - Indicates that the ids parameter was not provided in the request.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message returned when a required parameter is missing from the request.

Possible values:
One of the expected parameter is missing - Indicates that one of the expected request parameters was not provided.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `DeleteBlueprintBulkInvalidIdsErrorResponse` — Represents the bulk delete error response returned when all or some of the specified IDs are invalid.
        - `blueprints` (array of object `DeleteBlueprintBulkInvalidIdErrorItem`) [maxItems=100] **REQ** — Represents the list of per-Blueprint validation errors for the invalid IDs supplied in the bulk DELETE request.
          schema: `DeleteBlueprintBulkInvalidIdErrorItem`
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when an invalid Blueprint ID is provided.

Possible values:
INVALID_DATA - Indicates that the provided Blueprint ID is invalid.
          - `details` (object) **REQ** — Represents the details object that contains the invalid Blueprint ID.
            - `id` (string) **REQ** [maxLen=255] — Represents the ID of the invalid Blueprint.
          - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the provided Blueprint ID is invalid.

Possible values:
the id given seems to be invalid - Indicates that the specified Blueprint ID does not exist or is malformed.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `DeleteBlueprintInvalidDataError` — Represents the error returned when a field value provided in the bulk DELETE request is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the delete Blueprint request contains invalid data.

Possible values:
INVALID_DATA - Indicates that the request contains invalid data.
        - `details` (object) **REQ** — Represents the details object containing the invalid field name and its JSON path.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that contains invalid data.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the invalid field in the request body.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the delete Blueprint request contains invalid data.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Forbidden — The user does not have permission to perform this action.
**Resolution:** The Zoho CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
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
