# PUT /settings/kiosks/{kioskId}
**Operation:** `updateKiosk` — Update a Kiosk

> To update an existing **draft** Kiosk in Zoho CRM. This API allows you to update the Kiosk's name, description, group API name, and current record module. 

Use the [Get All Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID. You can identify a draft Kiosk using the status key in the response, where the value will be draft.


**Note:**
- You can update **one** Kiosk in a single API call.
- All fields supported in the [Create a Kiosk API](kiosks.yaml#$.paths./settings/kiosks.post) can be updated using this API.
- You can update a Kiosk only when it is in the draft state.

Availability: Standard, Professional, Enterprise, and Ultimate editions.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk ID.

**Schemas:**
`KioskErrorInvalidDataTypeForKiosks`:
  > Represents the error response returned when the kiosks field or its nested fields in the creation payload have invalid data types.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The kiosk request contains a field with an invalid data type.
  - `details` (object) **REQ** — Contains additional details about the error.
    - `maximum_length` (integer/int32) **REQ** — Indicates the maximum allowed length for the field that caused the error.
    - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that caused the data type error.
    - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the data type error.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the issue. Possible values:
invalid data
  - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.

**Request Body** — application/json `KioskEditRequest`
> The request body must contain a kiosks array with one object.
  > Represents the alternate top-level request payload for updating a kiosk, containing a kiosks array with one object.
  - `kiosks` (array of object `KioskEditInput`) [maxItems=1] **REQ** — Contains the details of the kiosk to be updated. Although the field is an array, only one kiosk can be updated per request.
    schema: `KioskEditInput`
    - `name` (string) [maxLen=25, nullable] — Specifies the name of the kiosk. The kiosk name can be at most 25 characters in length.
    - `group_api_name` (string) [maxLen=25, nullable] — Specifies the API name of the kiosk group. The group API name can be at most 25 characters in length.
    - `description` (string) [maxLen=500, nullable] — Specifies the description of the kiosk. The description can indicate the purpose of the kiosk and can be left empty during an update.
    - `id` (string) [maxLen=19, readOnly, nullable] — Specifies the unique identifier of the kiosk to be updated. This field is read-only; any changes to this value are not applied.
    - `current_record_module` (object `KioskCurrentRecordModuleEditInput`) — It is a json object which will contain the details of the current record module being set for the Kiosk. Current record is a designated module from which a specific record will be used for actions inside the Kiosk. For example, if the current record is set as Leads. While running actions or associating a field with current record, the user may have to provide a Lead id during execution. The action/association will be done based on this particular Lead. Current record can be set either in POST or PUT call of kiosks.
      schema: `KioskCurrentRecordModuleEditInput`
      - `api_name` (string) [maxLen=250, nullable] — Specifies the API name of the module to set as the current record. When both identifier and api_name are provided, they must point to the same module.
      - `id` (string) [maxLen=18, nullable] — Specifies the unique identifier of the module to set as the current record. Each module has a unique identifier in Zoho CRM.

**Responses:**

- **200**: Returns the result of the Kiosk update operation, including the status code and the ID of the updated Kiosk. — Schema: `KioskUpdateResponse` [application/json]
    > Represents the response returned after updating a kiosk, containing an array of per-item operation results.
    schema: `KioskUpdateResponse`
    - `kiosks` (array of object `KioskUpdateActionResult`) [maxItems=1] — Contains the list of kiosk result objects from the update operation.
      schema: `KioskUpdateActionResult`
      - `code` (string) [maxLen=255] — Represents the result code of the kiosk update operation.
      - `details` (object `KioskUpdateResultDetails`) — Represents the identifier of the updated kiosk returned as part of the update operation result.
        schema: `KioskUpdateResultDetails`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the updated kiosk.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the kiosk update operation.
      - `status` (string) [maxLen=255] — Indicates the result status of the kiosk update operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains invalid or duplicate data, or a required field is missing.
**Resolution:** Review the request payload and ensure the Kiosk ID is valid, field values do not duplicate existing Kiosk names or API names, and any module ID and API name provided in **current_record_module** refer to the same module. [application/json]
    > Represents the error response body returned for a 400 Bad Request. The response is one of two shapes: a single error object for data type validation failures, or a wrapped kiosks array containing one or more field-level validation errors.
    oneOf:
      - `KioskErrorInvalidDataTypeForKiosks` — Represents the error response returned when the kiosks field or its nested fields in the creation payload have invalid data types.
        - `kiosks` (array of object) [maxItems=25] **REQ** — Represents the list of error objects returned when one or more validation failures occurred during the Kiosk update request.
          oneOf:
            - `KioskErrorInvalidDataValue` — Represents the error response returned when the provided field values do not match the expected format or allowed value set.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The value provided for a field does not meet the expected format or constraints.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Indicates the expected data type for the field that caused the error.
                - `regex` (string) **REQ** [maxLen=255] — Contains the regular expression that defines the expected format for the field.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that contains the invalid value.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the issue. Possible values:
invalid data
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskErrorDuplicateKiosk` — Represents the error response returned when the kiosk name or group API name duplicates an existing kiosk.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code. Possible values:
DUPLICATE_DATA - A kiosk with the same name already exists in the organization.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that contains the duplicate value.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that contains the duplicate value.
              - `message` (string) **REQ** [enum=['Duplicate Kiosk name']] — Represents the error message describing the issue. Possible values:
Duplicate Kiosk name
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskErrorInvalidDataTypeForKiosks` — Represents the error response returned when the kiosks field or its nested fields in the creation payload have invalid data types.
            - `KioskErrorCurrentRecordAmbiguity` — Represents the error response returned when the current record module identifier and api_name reference different modules.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code. Possible values:
AMBIGUITY_DURING_PROCESSING - An ambiguity was encountered while processing the current record module reference.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Contains the list of fields that caused the ambiguity.
                  - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that caused the ambiguity.
                  - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the ambiguity.
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message describing the issue. Possible values:
Ambiguity while processing the request
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskErrorModuleNotFound` — Represents the error response returned when the specified current record module identifier does not correspond to an existing module.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The specified module does not exist in the organization.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that references the missing module.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that references the missing module.
              - `message` (string) **REQ** [enum=["the given module doesn't exist"]] — Represents the error message indicating that the specified module does not exist.
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskErrorInvalidDataType` — Represents the error response returned when the kiosk payload contains fields with invalid data types.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The value provided for a field does not match the expected data type.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Indicates the expected data type for the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that caused the data type error.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the data type error.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message describing the issue. Possible values:
Invalid data type
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
            - `KioskErrorInvalidData` — Represents the error response returned when the kiosk creation payload contains invalid data.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values:
INVALID_DATA - The request contains invalid data.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `maximum_length` (integer/int32) **REQ** — Indicates the maximum allowed length for the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the field that contains the invalid data.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message describing the issue. Possible values:
Invalid data
              - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.UPDATE
