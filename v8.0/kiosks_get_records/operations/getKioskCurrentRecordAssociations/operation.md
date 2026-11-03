# GET /settings/kiosks/{kioskId}/current_record/associations
**Operation:** `getKioskCurrentRecordAssociations` — Kiosk CurrentRecords Associations

> To retrieve all associations configured for the current record of the specified kiosk in your Zoho CRM organization.

Use this API to retrieve all the associations configured for the CurrentRecord lookup field in a specific Kiosk. It returns the list of associated resources, including their sequence, name, and ID, that are linked to the CurrentRecord in the Kiosk setup.

**Note:**
  - The response includes all associations defined for the CurrentRecord in the specified Kiosk.
  - Each association may contain one or more resources with details such as sequence number, name, and ID.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=255]: Unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID.
- `include_inner_details` (query, string, optional) [maxLen=500]: Controls additional inner details to include in the response.

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

- **200**: Returns the association data configured for the current record of the specified kiosk, including the list of resources and the type of the association. — Schema: `GetCurrentRecordAssociationsResponse` [application/json]
    > Response containing current record association information.
    schema: `GetCurrentRecordAssociationsResponse`
    - `current_record` (array of object `GETCurrentRecord`) [maxItems=10] **REQ** — Array of current record association data.
      schema: `GETCurrentRecord`
      - `_associations` (array of object `GETAssociation`) [maxItems=1] **REQ** — List of associations for the current record.
        schema: `GETAssociation`
        - `resources` (array of object `GETResource`) [maxItems=25] **REQ** — Resources that use this component.
          schema: `GETResource`
          - `name` (string) **REQ** [maxLen=255] — Name of the resource.
          - `id` (string) **REQ** [maxLen=255] — Unique identifier of the resource.
          - `_details` (object `GETResourceDetails`) **REQ** — Details about the resource type.
            schema: `GETResourceDetails`
            - `type` (string) **REQ** [maxLen=255] — Type of the resource (e.g., 'get_records', 'action').
        - `type` (string) **REQ** [maxLen=255] — Type of association (e.g., 'kiosk_states').
      - `id` (string) **REQ** [maxLen=255] — Current record identifier.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Returned when the kioskId path parameter does not correspond to an existing kiosk in the organization.
**Resolution:** The kioskId path parameter must reference an existing kiosk within the organization. — Schema: `GetRecordErrorResponse` [application/json]
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

**Scopes:** ZohoCRM.settings.kiosks.READ
