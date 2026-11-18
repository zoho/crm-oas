# POST /settings/blueprints/actions/reorder
**Operation:** `reorderBlueprints` — Reorder Blueprints within a module

> To update the display order of Blueprints within a Zoho CRM module, submit a list of Blueprint entries each specifying an ID and the desired sequence_number. The operation accepts up to 100 entries per request and returns the outcome for each Blueprint, indicating whether its position update succeeded.


**Parameters:**
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Specify the name of the service making the API call. Possible values:
automation - Identifies the automation service as the caller.
- `module` (query, string, required) [maxLen=255] {style=form, explode=True}: Specify the API name of the module for which the Blueprint action is to be performed.

**Schemas:**
`BlueprintReorderResult`:
  > Represents the result of a single Blueprint reorder operation, including the result code, status, message, and associated details.
  - `code` (string) [maxLen=255] — Represents the result code indicating the outcome of the reorder operation for this Blueprint.
  - `details` (object `BlueprintReorderResultDetails`) — Represents the details associated with a single Blueprint reorder result, including the unique identifier of the affected Blueprint.
  - `message` (string) [maxLen=255] — Represents the message describing the outcome of the reorder operation for this Blueprint.
  - `status` (string) [maxLen=255] — Represents the status of the reorder operation for this Blueprint, indicating whether it succeeded or failed.
`BlueprintReorderResultDetails`:
  > Represents the details associated with a single Blueprint reorder result, including the unique identifier of the affected Blueprint.
  - `id` (string) [maxLen=255] — Represents the unique identifier of the Blueprint entry.

**Request Body** — application/json `BlueprintOrderUpdateRequest`
> The request body must contain a blueprints array of Blueprint reorder entry objects. Each entry must include the Blueprint ID and the sequence_number representing its new position in the module.

  > Represents the request body for updating the display order of multiple Blueprints. Contains an array of Blueprint reorder entries, each specifying a Blueprint ID and the target sequence number.
  - `blueprints` (array of object `BlueprintReorderEntry`) [maxItems=100] **REQ** — Contains the list of Blueprint entries whose display order is to be updated.
    schema: `BlueprintReorderEntry`
    - `sequence_number` (integer/int32) **REQ** — Represents the new order for the blueprint
    - `id` (string) **REQ** [maxLen=50] — Represents the unique identifier of the Blueprint to be reordered.

**Responses:**

- **200**: Returns the results of the Blueprint reorder operation. Each entry in the blueprints array indicates the reorder outcome for the corresponding Blueprint, including its ID, status, code, and message.
 — Schema: `BlueprintReorderSuccessResponse` [application/json]
    > Represents the success response returned for a Blueprint reorder request, containing an array of per-Blueprint reorder results.
    schema: `BlueprintReorderSuccessResponse`
    - `blueprints` (array of object `BlueprintReorderResult`) [maxItems=50] **REQ** — Contains the list of Blueprint entries reflecting the updated order after a successful reorder operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a mixed-status response when Blueprint reorder entries are processed with varying outcomes. Each entry in the blueprints array independently indicates success or failure for the corresponding Blueprint in the request.
 — Schema: `BlueprintReorderMultiStatusResponse` [application/json]
    > Represents the multi-status response returned for a Blueprint reorder request, containing an array of per-Blueprint reorder results.
    schema: `BlueprintReorderMultiStatusResponse`
    - `blueprints` (array of object `BlueprintReorderResult`) [maxItems=2] — Contains the list of Blueprint reorder results, each indicating the outcome of the reorder operation for an individual Blueprint.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request — The request could not be processed.
**Resolution:** The caller should verify that the required `module` query parameter is present, that the `blueprints` array does not exceed 100 entries, that each entry includes both a valid `id` and a `sequence_number`, and that the specified module name is valid.
 [application/json]
    > Represents a 400 Bad Request error response for the reorderBlueprints operation. Contains one of four error variants: a missing module query parameter error, a data-exceeds-maximum-length error, an invalid module name error, or an array of per-Blueprint validation errors.

    oneOf:
      - `MissingModuleParameterError` — Represents an error response returned when a required query parameter is missing from the request. Includes error code REQUIRED_PARAM_MISSING and the missing parameter name in the details.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned for this response. Possible values:
REQUIRED_PARAM_MISSING - Indicates that a required query parameter was not provided.
        - `details` (object) **REQ** — Contains additional information about the error, including the name of the missing parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the missing parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message returned when a required parameter is missing from the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
      - `ErrorResponseCore27` — Represents an error response returned when the provided data is invalid and exceeds the allowed length. Includes error code INVALID_DATA and the maximum allowed length in the details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for this response. Possible values:
INVALID_DATA - Indicates that the provided data is invalid.
        - `details` (object) **REQ** — Contains additional information about the error, including the affected field name and its JSON path in the request.
          - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field that exceeded the limit.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error in the request payload.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned when the provided data is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
      - `InvalidModuleNameErrorResponse` — Represents an error response returned when the provided module name is invalid. Includes error code INVALID_MODULE and the invalid parameter name in the details.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned for this response. Possible values:
INVALID_MODULE - Indicates that the provided module name is invalid.
        - `details` (object) **REQ** — Contains additional information about the error, including the name of the invalid parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the invalid or missing parameter.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message returned when the provided module name is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
        - `blueprints` (array of object) [maxItems=25] **REQ** — Represents the list of per-Blueprint error objects returned when one or more Blueprint reorder entries fail validation.

          oneOf:
            - `ErrorResponseCore5` — Represents an error response returned when the provided Blueprint ID is invalid. Includes error code INVALID_DATA.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for this response. Possible values:
INVALID_DATA - Indicates that the provided data is invalid.
              - `details` (object) **REQ** — Contains additional information about the error, including the affected field name and its JSON path in the request.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error in the request payload.
              - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the provided Blueprint ID is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
            - `BlueprintReorderInvalidProcessIDErrorResponse` — Represents an error response returned when a Blueprint reorder operation fails due to an invalid or missing process ID.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for this response. Possible values:
MANDATORY_NOT_FOUND - Indicates that a required field was not provided in the request.
              - `details` (object) **REQ** — Contains additional information about the error, including the affected field name and its JSON path in the request.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error in the request payload.
              - `message` (string) **REQ** [enum=['blueprint reorder failed']] — Represents the error message returned when the Blueprint reorder operation fails.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
            - `MissingSequenceNumberErrorResponse` — Represents an error response returned when the mandatory sequence_number field is missing from the reorder request. Includes error code MANDATORY_NOT_FOUND.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for this response. Possible values:
MANDATORY_NOT_FOUND - Indicates that a required field was not provided in the request.
              - `details` (object) **REQ** — Contains additional information about the error, including the affected field name and its JSON path in the request.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error in the request payload.
              - `message` (string) **REQ** [enum=['mandatory field is not given']] — Represents the error message returned when a mandatory field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
            - `InvalidProcessSequenceErrorResponse` — Represents an error response returned when an invalid process sequence is provided in the reorder request. Includes error code INVALID_DATA.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for this response. Possible values:
INVALID_DATA - Indicates that the provided data is invalid.
              - `details` (object) **REQ** — Contains additional information about the error, including the affected field name and its JSON path in the request.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error in the request payload.
              - `message` (string) **REQ** [enum=['Invalid process sequence is given']] — Represents the error message returned when an invalid process sequence is provided.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
            - `ErrorResponseCore4` — Represents an error response returned when a required field is missing from the request. Includes error code MANDATORY_NOT_FOUND.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for this response. Possible values:
MANDATORY_NOT_FOUND - Indicates that a required field was not provided in the request.
              - `details` (object) **REQ** — Contains additional information about the error, including the affected field name and its JSON path in the request.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error in the request payload.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message returned when a required field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
            - `ErrorResponseCore2` — Represents an error response returned when the provided field value does not match the expected data type. Includes error code INVALID_DATA and the expected data type in the details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for this response. Possible values:
INVALID_DATA - Indicates that the provided data is invalid.
              - `details` (object) **REQ** — Contains additional information about the error, including the affected field name and its JSON path in the request.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field that contains invalid data.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error in the request payload.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message returned when the provided value does not match the expected data type for the field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
            - `ErrorResponseCore6` — Represents an error response returned when the provided data exceeds the allowed length. Includes error code INVALID_DATA and the maximum allowed length in the details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for this response. Possible values:
INVALID_DATA - Indicates that the provided data is invalid.
              - `details` (object) **REQ** — Contains additional information about the error, including the affected field name and its JSON path in the request.
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field that exceeded the limit.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error in the request payload.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message returned when the provided data exceeds the allowed length.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates that the request failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.UPDATE
