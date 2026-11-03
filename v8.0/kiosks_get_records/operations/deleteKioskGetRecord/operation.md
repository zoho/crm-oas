# DELETE /settings/kiosks/{kioskId}/get_records/{getRecordId}
**Operation:** `deleteKioskGetRecord` — Kiosk GetRecord
> To delete a specific [GetRecords](https://help.zoho.com/portal/en/kb/crm/customize-crm-account/kiosk/articles/elements-of-a-kiosk#GetRecords) configuration associated with a Kiosk.
Use the [GetRecords Associations API](kiosks_get_records.yaml#$.paths./settings/kiosks/{kioskId}/get_records/{getRecordId}/associations.get) to identify all associations of the GetRecords configuration. Remove the associations from the respective Kiosk components, and then delete the GetRecords configuration.
Use the [Get All Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID and use the [Kiosk GetRecords API](kiosks_get_records.yaml#$.paths./settings/kiosks/{kioskId}/get_records.get) to retrieve the GetRecords ID.
**Note:**
The response structure is dynamic and depends on the GetRecords configuration. Fields such as criteria, type, and selection_details may vary based on the configured settings.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=255]: Unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID.
- `getRecordId` (path, string, required) [maxLen=255]: Unique identifier of the [GetRecord](kiosks_get_records.yaml#$.paths./settings/kiosks/{kioskId}/get_records/{getRecordId}.get) component.

**Schemas:**
`GetRecordErrorItem`:
  > Individual error item within a batch error response array.
  - `code` (string) **REQ** [enum=[7 values]] — Error category code indicating the type of validation failure.
  - `details` (object) **REQ** — Contextual details about the error. Structure varies by error type.
    - `api_name` (string) [maxLen=255] — API name of the field that caused the error.
    - `json_path` (string) [maxLen=1000] — JSON path pointing to the problematic field in the request body.
    - `expected_data_type` (string) [maxLen=255] — The expected data type when a type mismatch occurs.
    - `maximum_length` (integer/int32) — Maximum allowed length when a value exceeds the limit.
    - `resource_path_index` (integer/int32) — Index in the resource path that is invalid.
    - `supported_values` (array of string) [maxItems=50] — List of supported values when an invalid enum value is provided.
      items: [maxLen=1000]
    additionalProperties: any
  - `message` (string) **REQ** [maxLen=500] — Human-readable error message describing what went wrong.
  - `status` (string) **REQ** [enum=['error']] — Status of the response. Always 'error' for error responses.
  additionalProperties: any

**Responses:**

- **200**: Get record deleted successfully. — Schema: `DeleteGetRecordResponse` [application/json]
    > Response after successfully deleting a get_record component.
    schema: `DeleteGetRecordResponse`
    - `get_records` (array of object `GetRecordOperationResult`) [maxItems=1] — Array of operation results.
      schema: `GetRecordOperationResult`
      - `code` (string) [maxLen=255] — Result code (e.g., 'SUCCESS').
      - `details` (object `OperationResultDetails`) — Details of the operation result.
        schema: `OperationResultDetails`
        - `id` (string) [maxLen=255] — ID of the created, updated, or deleted resource.
      - `message` (string) [maxLen=255] — Human-readable result message.
      - `status` (string) [maxLen=255] — Status of the operation (e.g., 'success').
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Invalid request. — Schema: `GetRecordErrorResponse` [application/json]
    > Unified error response schema for all get_record API errors. Errors may appear at the top level (for path-level errors like invalid kiosk ID) or wrapped in a 'get_records' or 'kiosks' array (for item-level validation errors).
    oneOf:
      - `GetRecordFlatError` — Flat error response for path-level errors such as invalid kiosk or get record ID.
        - `code` (string) **REQ** [enum=[7 values]] — Error category code indicating the type of validation failure.
        - `details` (object) **REQ** — Contextual details about the error. Structure varies by error type.
          - `api_name` (string) [maxLen=255] — API name of the field that caused the error.
          - `json_path` (string) [maxLen=1000] — JSON path pointing to the problematic field in the request body.
          - `expected_data_type` (string) [maxLen=255] — The expected data type when a type mismatch occurs.
          - `maximum_length` (integer/int32) — Maximum allowed length when a value exceeds the limit.
          - `resource_path_index` (integer/int32) — Index in the resource path that is invalid.
          - `supported_values` (array of string) [maxItems=50] — List of supported values when an invalid enum value is provided.
            items: [maxLen=1000]
          additionalProperties: any
        - `message` (string) **REQ** [maxLen=500] — Human-readable error message describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — Status of the response. Always 'error' for error responses.
        additionalProperties: any
      - `GetRecordBatchError` — Batch error response wrapping item-level validation errors in a get_records array.
        - `get_records` (array of object `GetRecordErrorItem`) [maxItems=1] **REQ** — Array of get_record error items.
      - `KioskBatchError` — Batch error response wrapping item-level validation errors in a kiosks array.
        - `kiosks` (array of object `GetRecordErrorItem`) [maxItems=1] **REQ** — Array of kiosk error items.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.DELETE
