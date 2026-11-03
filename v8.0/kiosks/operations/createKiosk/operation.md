# POST /settings/kiosks
**Operation:** `createKiosk` — Create a Kiosk

> To create a new Kiosk in the draft state in your Zoho CRM organization. After creating the Kiosk, use the [Create a Kiosk State API](kiosks_states.yaml#$.paths./settings/kiosks/{kioskId}/states.post)  to configure screens and then use the [Activate Kiosk API](kiosks.yaml#$.paths./settings/kiosks/{kioskId}/actions/activate.put) to publish it. 

Available in the Standard, Professional, Enterprise, and Ultimate editions.



**Note:**
- Using this API, you can only create a kiosk in a single API call. The created Kiosk will remain in the draft state.
- Refer to the [Compare all features of Zoho CRM editions document](https://www.zoho.com/crm/complete-feature-list.html) to know edition-specific limits for Kiosk creation.


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

**Request Body** — application/json `KioskCreateRequest`
> The request body must contain a kiosks array with one object representing the Kiosk to create.
  > Represents the top-level request payload for creating a kiosk. Contains a kiosks array, with one kiosk object per request.
  - `kiosks` (array of object `KioskCreateInput`) [maxItems=1] **REQ** — Contains the details of the kiosk to be created. Although the field is an array, only one kiosk can be created per request.
    schema: `KioskCreateInput`
    - `current_record_module` (object `KioskCurrentRecordModuleCreateInput`) — It is a json object which will contain the details of the current record module being set for the Kiosk. Current record is a designated module from which a specific record will be used for actions inside the Kiosk. For example, if the current record is set as Leads. While running actions or associating a field with current record, the user may have to provide a Lead id during execution. The action/association will be done based on this particular Lead. 
      schema: `KioskCurrentRecordModuleCreateInput`
      - `api_name` (string) [maxLen=250, nullable] — Specifies the API name of the module to set as the current record. When both identifier and api_name are provided, they must point to the same module.
      - `id` (string) [maxLen=19, nullable] — Specifies the unique identifier of the module to set as the current record. For example, provide the module ID for Leads.
    - `name` (string) **REQ** [maxLen=25] — Specifies the name of the kiosk. The kiosk name can be at most 25 characters in length.
    - `description` (string) [maxLen=500, nullable] — Specifies the description for the kiosk. The description can indicate the purpose of the kiosk and can be left empty during creation.
    - `group_api_name` (string) [maxLen=25, nullable] — Specifies the unique group API name for the kiosk. The group API name should be similar to the kiosk name. Special characters are not allowed.
    - `status` (string) **REQ** [maxLen=5] — Specifies the status of the kiosk. Upon successful creation, the initial status of the kiosk is always draft. Possible values:
draft - The kiosk is in draft state upon creation.

**Responses:**

- **201**: Returns a kiosks array containing one object with the result of the create operation. Each object includes a status, a code, a message, and a details object containing the ID of the newly created Kiosk. — Schema: `KioskCreateResponse` [application/json]
    > Represents the response returned after creating a kiosk, containing an array of per-item operation results.
    schema: `KioskCreateResponse`
    - `kiosks` (array of object `KioskCreateActionResult`) [maxItems=1] — Contains the list of kiosk objects created.
      schema: `KioskCreateActionResult`
      - `code` (string) [maxLen=255] — Represents the result code of the kiosk create operation.
      - `details` (object `KioskCreateResultDetails`) — Represents the identifiers for the created kiosk, such as the kiosk identifier, returned as part of the operation result.
        schema: `KioskCreateResultDetails`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the newly created kiosk.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the kiosk create operation.
      - `status` (string) [maxLen=255] — Indicates the result status of the kiosk create operation.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request — One or more fields in the request failed validation.
**Resolution:** Verify that all mandatory fields are present, that the group API name contains only valid characters, that the status value is valid, that the current_record_module details are correct and unambiguous, and that the name and group API name are not duplicates of an existing Kiosk.
 [application/json]
    > Represents the error response body returned for a 400 Bad Request. Contains one of: a top-level mandatory-field or invalid-data-type error, or a wrapped kiosks array of per-item field-level validation errors.
    oneOf:
      - `KioskErrorMandatoryFieldMissing` — Represents the error response returned when a required field is missing from the kiosk creation payload.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code. Possible values:
MANDATORY_NOT_FOUND - A required field is missing from the kiosk request.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the mandatory field that is missing.
          - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the mandatory field that is missing.
        - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the issue. Possible values:
required field not found
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
      - `KioskErrorInvalidDataTypeForKiosks` — Represents the error response returned when the kiosks field or its nested fields in the creation payload have invalid data types.
        - `kiosks` (array of object) [maxItems=25] **REQ** — Represents the list of per-item error objects returned when one or more kiosk fields fail validation.
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
            - `KioskErrorInvalidApiName` — Represents the error response returned when the group API name provided for the kiosk is invalid or contains unsupported characters.
              - `code` (string) **REQ** [enum=['INVALID_API_NAME']] — Represents the error code. Possible values:
INVALID_API_NAME - The group API name provided for the kiosk is invalid.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the kiosk field that contains the invalid API name.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the field that caused the invalid API name error.
              - `message` (string) **REQ** [enum=['Invalid Kiosk api name']] — Represents the error message indicating an invalid kiosk group API name.
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
            - `KioskErrorMissingRequiredField` — Represents the error response returned when a required field is absent from the kiosk request.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code. Possible values:
MANDATORY_NOT_FOUND - A required field is missing from the request.
              - `details` (object) **REQ** — Contains additional details about the error.
                - `api_name` (string) **REQ** [maxLen=255] — Identifies the API name of the required field that is missing.
                - `json_path` (string) **REQ** [maxLen=1000] — Indicates the JSON path of the required field that is missing.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message describing the issue. Possible values:
Required field is missing
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

**Scopes:** ZohoCRM.settings.kiosks.CREATE
