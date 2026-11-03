# POST /settings/kiosks/{kioskId}/actions/clone
**Operation:** `cloneKiosk` — Clone a Kiosk

> To clone an existing kiosk in Zoho CRM and create a new one from it. Cloning lets you reuse the full structure and configuration of a kiosk — including all its states, transitions, screens, actions, and decisions — without rebuilding it from scratch. The cloned kiosk can be created as an independent, standalone kiosk or as a draft version linked to the source kiosk. This API copies the source kiosk exactly as it is; it does not support modifying the kiosk's configuration during the cloning process. 
To make changes to the cloned Kiosk after it is created, use the [Update a Kiosk State API](kiosks.yaml#$.paths./settings/kiosks/{kioskId}.put).


Available on Standard, Professional, Enterprise, and Ultimate editions.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk ID.
- `delete_kiosk_id` (query, string, optional) [maxLen=19]: ID of the kiosk to delete after cloning (for replace-clone operations).
- `kiosk_clone` (query, string, optional) [maxLen=255]: Indicates the clone mode for the kiosk clone operation.

**Request Body** — application/json `KioskCloneRequest`
> The request body must contain a kiosks array with one object. The object must specify the clone type (standalone or dependent). For a standalone clone, the name and group_api_name fields are also required; description is optional.

  > Represents the request payload for cloning a kiosk, containing the list of kiosk configurations to be created via cloning.
  - `kiosks` (array of object `KioskCloneDetails`) [maxItems=1] **REQ** — Contains the details for the kiosk to be cloned.
    schema: `KioskCloneDetails`
    - `name` (string) [maxLen=50, pattern=[0-9a-zA-Z_\\-\\.\\|\\$\\?\\,\\'\\/\\!\\P{InBasicLatin}\\s]+, nullable] — Specifies the name of the kiosk.
    - `description` (string) [maxLen=500, nullable] — Specifies the description of the kiosk.
    - `type` (string) **REQ** [maxLen=20, enum=['dependent', 'standalone']] — Specifies the type of the cloned kiosk. Possible values:
dependent - The cloned kiosk depends on the source kiosk.
standalone - The cloned kiosk operates independently of the source kiosk.
    - `group_api_name` (string) [maxLen=25, nullable] — Specifies the unique group API name for the kiosk.

**Responses:**

- **200**: The kiosk was cloned successfully. Returns a kiosks object containing the status code, a success message, and the ID of the newly created kiosk.
 — Schema: `KioskCloneSuccessResponse` [application/json]
    > Represents the response returned when a kiosk clone operation completes successfully, including the status information for the cloned kiosk.
    schema: `KioskCloneSuccessResponse`
    - `kiosks` (object `KioskCloneStatus`) — Represents the status of a kiosk clone operation, including the status code, message, and item details.
      schema: `KioskCloneStatus`
      - `code` (string) [maxLen=255] — Represents the status code of the kiosk clone operation.
      - `details` (object `KioskCloneItemDetail`) — Represents the identifiers and related details for a cloned kiosk item returned in a clone operation response.
        schema: `KioskCloneItemDetail`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the kiosk.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the kiosk clone operation.
      - `status` (string) [maxLen=255] — Indicates the result status of the kiosk clone operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Returned when the clone request is rejected due to a missing, invalid, or incomplete input.

**`ID_ALREADY_DELETED`** — No such kiosk exists.
**Resolution:** Specify the ID of an existing kiosk.

**`MANDATORY_NOT_FOUND`** — A required field is missing from the request body.
**Resolution:** Specify values for all required fields.

**`INVALID_DATA`** — The value provided for the type field is not valid.
**Resolution:** Specify a valid type value: `standalone` or `dependent`.

**`DEPENDENT_FIELD_MISSING`** — The name or group_api_name field is required for a standalone clone but was not provided.
**Resolution:** Include the name and group_api_name fields when creating a standalone clone.
 [application/json]
    > Returned when the clone request cannot be processed. Covers two error shapes: a kiosk-not-found error when the specified kiosk ID does not exist, or a wrapped array of field-level and payload-level validation errors when the request body is invalid.

    oneOf:
      - `KioskNotFoundError` — Represents the error response returned when the specified kiosk does not exist or has been deleted, typically during a clone operation.
        - `code` (string) **REQ** [enum=['ID_ALREADY_DELETED']] — Represents the error code. Possible values:
ID_ALREADY_DELETED - The kiosk with the specified identifier has already been deleted.
        - `details` (object) **REQ** — Contains additional details about the error.
        - `message` (string) **REQ** [enum=['No such Kiosk exists']] — Represents the error message describing the issue. Possible values:
No such Kiosk exists
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
        - `kiosks` (array of object) [maxItems=25] **REQ** — Contains one or more error objects returned when the clone request fails validation. Each item identifies the specific field-level or payload-level error that caused the failure.

          oneOf:
            - `KioskCloneMandatoryFieldMissingError` — Represents the error response returned when required data, such as the kiosk name, is missing during a clone operation.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code. Possible values:
MANDATORY_NOT_FOUND - A required field is missing from the kiosk clone request.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the mandatory field that is missing.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the mandatory field that is missing.
              - `message` (string) **REQ** [enum=['Kiosk name is missing']] — Represents the error message describing the issue. Possible values:
Kiosk name is missing
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskCloneTypeInvalidError` — Represents the error response returned when an invalid clone type is provided, such as an unrecognized value for the dependent or standalone option.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The clone type value provided in the request is invalid.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `regex` (string) **REQ** [maxLen=255] — Contains the regular expression that defines the expected format for the field.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the issue. Possible values:
invalid data
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskCloneInvalidDataTypeError` — Represents the error response returned when one or more fields in the clone payload have invalid data types, including the error code, status, message, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - Indicates that the provided data contains an invalid data type.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Indicates the expected data type for the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message describing the issue. Possible values:
Invalid data type
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskCloneInvalidDataError` — Represents the error response returned when the kiosk clone payload contains invalid data, including the error code, message, status, and validation details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The request contains invalid or malformed data.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `maximum_length` (integer/int32) **REQ** — Indicates the maximum allowed length for the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Identifies the JSON path of the field that failed validation.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message describing the issue. Possible values:
Invalid data
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskCloneInvalidPayloadError` — Represents the error response returned when the request payload for cloning a kiosk is invalid, including the error code, message, status, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The request payload contains data that is invalid or does not conform to the expected format.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `regex` (string) **REQ** [maxLen=255] — Contains the regular expression that defines the expected format for the field.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message describing the issue. Possible values:
Invalid data
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskCloneRequiredFieldMissingError` — Represents the error response returned when a required field is not provided for the clone operation, including the error code, message, status, and details.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code. Possible values:
MANDATORY_NOT_FOUND - A required field is missing from the request.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the required field that is missing.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the required field that is missing.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message describing the issue. Possible values:
Required field is missing
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskCloneInvalidRequestError` — Represents the error response returned when the clone request is malformed or contains invalid values, including the error code, message, status, and details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The request data contains an invalid field value.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Contains the list of supported values for the field.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message describing the issue. Possible values:
Invalid data
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskCloneDependentFieldMissingError` — Represents the error response returned when a dependent field required by another field is missing in the clone request.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code indicating that a dependent field is missing during the kiosk clone operation.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `dependee` (object) **REQ** — Contains details about the dependee field that the missing dependent field relies upon.
                  - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the dependee field.
                  - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the dependee field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field involved in the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['Dependent field is missing']] — Represents the error message describing the issue. Possible values:
Dependent field is missing
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.CREATE
