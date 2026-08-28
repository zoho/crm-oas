# DELETE /Services__s/{id}
**Operation:** `deleteServiceById` — Delete a service record by ID
> To delete a service record from your Zoho CRM organization by its unique ID. When a service record is removed, all appointments associated with that service are also removed; however, deals created upon completion of an appointment under the service are not affected.

**Parameters:**
- `id` (path, string, required) [maxLen=100] {style=simple, explode=False}: Specify the unique ID of the service record to be deleted.

**Responses:**

- **200**: Returns the success status code and the ID of the service record after deletion. — Schema: `DeleteservicessResponse200` [application/json]
    > Wrapped response for a service DELETE request. Contains a data array with one status object carrying the success code and the deleted service ID.
    schema: `DeleteservicessResponse200`
    - `data` (array of object `DataNested1`) [maxItems=1] — Represents the per-record status array containing the result for each deleted service record.
      schema: `DataNested1`
      - `code` (string) [maxLen=255] — Represents the operation result code for the service record. 
      - `details` (object `DetailsNested`) — Represents the details as a per-record status item. Carries audit metadata (Modified_Time, Modified_By, Created_Time, Created_By) and the persisted record ID.
        schema: `DetailsNested`
        - `Modified_Time` (string) [maxLen=255] — Represents the timestamp when the service record was last modified.
        - `Modified_By` (object `ModifiedByNested`) — Represents the user who last modified the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
          schema: `ModifiedByNested`
          - `name` (string) [maxLen=255] — Represents the display name of the user who modified the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
          - `id` (string) [maxLen=255] — Represents the unique ID of the user who modified the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `Created_Time` (string) [maxLen=255] — Represents the timestamp when the service record was first saved to the organization.
        - `id` (string) [maxLen=255] — Represents the unique ID of the affected service record.
        - `Created_By` (object `CreatedByNested`) — Represents the user who created the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
          schema: `CreatedByNested`
          - `name` (string) [maxLen=255] — Represents the display name of the user who created the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
          - `id` (string) [maxLen=255] — Represents the unique ID of the user who created the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        additionalProperties: any
      - `message` (string) [maxLen=255] — Represents the result message for the operation result.
      - `status` (string) [maxLen=255] — Represents the status of the operation. 

- **400**: The request failed because the service ID in the request URL is invalid or already deleted, the service ID parameter is missing, or the module name is invalid.

**Resolution:** Verify that the module API name is correct, provide a valid service ID in the request URL, and retry the request.
 [application/json]
    > Represents the bad-request error response for the delete service operation. Contains error variants for invalid service record data, an invalid module name, a missing required parameter, or a general data error.
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
