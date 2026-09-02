# DELETE /Services__s
**Operation:** `deleteServicesS` — Delete one or more service records
> To delete one or more service records from your Zoho CRM organization. All appointments associated with the deleted services are also deleted; however, deals created upon completion of those appointments are not deleted.

**Parameters:**
- `ids` (query, number, optional) [min=1, max=100000000000000000] {style=form, explode=True}: Specify the IDs of the service records to be deleted. Provide them as comma-separated values with a maximum of **100** IDs per request.

**Schemas:**
`CreatedByNested`:
  > Represents the user who created the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `name` (string) [maxLen=255] — Represents the display name of the user who created the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
  - `id` (string) [maxLen=255] — Represents the unique ID of the user who created the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
`DetailsNested`:
  > Represents the details as a per-record status item. Carries audit metadata (Modified_Time, Modified_By, Created_Time, Created_By) and the persisted record ID.
  - `Modified_Time` (string) [maxLen=255] — Represents the timestamp when the service record was last modified.
  - `Modified_By` (object `ModifiedByNested`) — Represents the user who last modified the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `Created_Time` (string) [maxLen=255] — Represents the timestamp when the service record was first saved to the organization.
  - `id` (string) [maxLen=255] — Represents the unique ID of the affected service record.
  - `Created_By` (object `CreatedByNested`) — Represents the user who created the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  additionalProperties: any
`ModifiedByNested`:
  > Represents the user who last modified the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `name` (string) [maxLen=255] — Represents the display name of the user who modified the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
  - `id` (string) [maxLen=255] — Represents the unique ID of the user who modified the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.

**Responses:**

- **200**: Returns the result of a single-record service delete operation. The response body contains a `data` array with one entry that includes the status code `SUCCESS`, the deleted record ID, a confirmation message, and the operation status. — Schema: `DeleteservicessResponse200` [application/json]
    > Wrapped response for a service DELETE request. Contains a data array with one status object carrying the success code and the deleted service ID.
    schema: `DeleteservicessResponse200`
    - `data` (array of object `DataNested1`) [maxItems=1] — Represents the per-record status array containing the result for each deleted service record.
      schema: `DataNested1`
      - `code` (string) [maxLen=255] — Represents the operation result code for the service record. 
      - `details` (object `DetailsNested`) — Represents the details as a per-record status item. Carries audit metadata (Modified_Time, Modified_By, Created_Time, Created_By) and the persisted record ID.
      - `message` (string) [maxLen=255] — Represents the result message for the operation result.
      - `status` (string) [maxLen=255] — Represents the status of the operation. 

- **207**: Returns a multi-status response. Each item in the array independently indicates success or failure for the corresponding service ID in the ids query parameter. [application/json]
    > Wrapped multi-status response for a batch service delete operation. Contains a `data` array (2–200 items) with one entry per service record in the request; each entry independently indicates success or failure for that record.
    - `data` (array of object) [minItems=2, maxItems=200] **REQ** — Represents the per-record status array in the multi-status response. Contains between 2 and 200 entries, each independently indicating success or failure for the corresponding service ID supplied in the `ids` query parameter.

      oneOf:
        - `Post207multistatusResponse207` — Represents a success item in a multi-status response. Carries the success code, message, status, and details for the corresponding service record in the request.
          - `details` (object `DetailsNested`) — Represents the details as a per-record status item. Carries audit metadata (Modified_Time, Modified_By, Created_Time, Created_By) and the persisted record ID.
          - `code` (string) [maxLen=255] — Represents the operation result code for the service record. 
          - `message` (string) [maxLen=255] — Represents the result message for the operation result.
          - `status` (string) [maxLen=255] — Represents the status of the operation. 
        - `InvalidDataMultiStatusError` — Multi-status error item returned when a service record in a bulk operation could not be processed because of invalid data.
          - `code` (string) **REQ** [maxLen=255, enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
          - `details` (object) **REQ** — Represents the details providing validation context for the error.
            - `id` (string) [maxLen=255] — Represents the unique ID of the service record that could not be processed.
            additionalProperties: any
          - `message` (string) **REQ** [maxLen=100] — Represents the error message for the failure.
          - `status` (string) **REQ** [maxLen=100] — Represents the status of the response. 
          additionalProperties: any

- **400**: Returned when the service ID is invalid or already deleted, the `ids` query parameter is missing, or the module name is unrecognized.

**Resolution:** A valid service record ID must be supplied in the `ids` query parameter. The module name must match a recognized API name before retrying the request. [application/json]
    > Bad-request error response for the delete services operation. Returned when the module name is invalid, the `ids` parameter is missing, or one or more service records could not be deleted. The response body conforms to one of: `RecordNotDeletedError`, `InvalidModuleNameError`, `RequiredParamMissingForDeleteError`, or `DataError`.
    oneOf:
      - `RecordNotDeletedError` — Error response returned when a service record referenced in a DELETE request could not be deleted.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment that caused the failure.
        - `message` (string) **REQ** [enum=['record not deleted']] — Represents the error message describing that the service record could not be deleted.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
      - `InvalidModuleNameError` — Error response returned when the module name in the request URL does not match any module in the Zoho CRM organization.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned for the failed request.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment that caused the failure.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message for the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
      - `RequiredParamMissingForDeleteError` — Error response returned when the ids query parameter is missing from a service DELETE request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned for the failed request.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `param` (string) **REQ** [maxLen=255] — Represents the name of the missing query parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message describing that a required parameter is missing from the DELETE request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
      - `DataError` — Standard error response object returned when a request fails. Contains the error code, the message, the status, and a details block identifying the offending field.
        - `code` (string) **REQ** [maxLen=255] — Represents the error code returned when a data validation error occurs.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
          - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message returned when the request fails.
        - `status` (string) **REQ** [maxLen=1000] — Represents the status of the response, indicating that an error occurred.
        additionalProperties: any

**Scopes:** ZohoCRM.modules.services.DELETE
