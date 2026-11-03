# GET /settings/kiosks/{kioskId}/associations
**Operation:** `getKioskAssociations` — Get Kiosk Associations
> Retrieves all associations configured for a specific Kiosk in Zoho CRM, including the associated resources and, their additional details.

Use the [Get All Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID.

**Note:**
  - The structure of each resource object is mostly consistent, but _details can vary.
  - The sequence_number plays an important role in determining execution or display order.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=255]: Unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID.
- `include_inner_details` (query, string, optional) [maxLen=500]: Controls additional inner details to include in the response.
- `include` (query, string, optional) [maxLen=255]: Specifies additional properties to include in the response.
- `module` (query, string, optional) [maxLen=255]: Filters associations by the specified module API name.

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

- **200**: Returns the association information for the specified kiosk, including detail view page associations. — Schema: `GetKioskAssociationsResponse` [application/json]
    > Response containing kiosk association information including detail view page associations.
    schema: `GetKioskAssociationsResponse`
    - `kiosks` (array of object `GETKioskItem`) [maxItems=1] **REQ** — Array of kiosk association data.
      schema: `GETKioskItem`
      - `_associations` (array of object `GETKioskAssociation`) [maxItems=50] **REQ** — List of associations for this kiosk.
        schema: `GETKioskAssociation`
        - `resources` (null) **REQ** — Resources field (null for detail_view_page type).
        - `type` (string) **REQ** [maxLen=255] — Type of association.
        - `detail_view_page` (array of object `GETDetailViewPage`) [maxItems=50] **REQ** — Detail view page configurations.
          schema: `GETDetailViewPage`
          - `sequence_number` (integer/int32) **REQ** — Display sequence number.
          - `name` (string) **REQ** [maxLen=255] — Name of the detail view page association.
          - `id` (string) **REQ** [maxLen=255] — Unique identifier.
      - `id` (string) **REQ** [maxLen=255] — Kiosk identifier.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The specified kiosk does not exist.
**Resolution:** The **kioskId** path parameter must reference an existing kiosk. — Schema: `GetRecordErrorResponse` [application/json]
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
