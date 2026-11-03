# GET /settings/kiosks/{kioskId}/get_records/{getRecordId}/associations
**Operation:** `getKioskGetRecordAssociations` — GetRecords Associations
> This API returns all the associations of a specific [GetRecords](https://help.zoho.com/portal/en/kb/crm/customize-crm-account/kiosk/articles/elements-of-a-kiosk#GetRecords) configuration. Associations represent where the configuration is being used, such as:
  - Kiosk states
  - Actions
  - Other dependent elements

This API helps you understand the dependencies of a GetRecords configuration before [modifying](kiosks_states.yaml#$.paths./settings/kiosks/{kioskId}/states/{stateId}.put)  or [deleting](kiosks_states.yaml#$.paths./settings/kiosks/{kioskId}/states/{stateId}.delete) it. 


**Note:** Predefined states, start state and end state, cannot be deleted.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=255]: Unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID.
- `getRecordId` (path, string, required) [maxLen=255]: Unique identifier of the [GetRecord](kiosks_get_records.yaml#$.paths./settings/kiosks/{kioskId}/get_records/{getRecordId}.get) component.
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

- **200**: Returns the association data for the specified get_record component within the kiosk, including the list of resources and the type of each association. — Schema: `GetGetRecordAssociationsResponse` [application/json]
    > Response containing get_record association information.
    schema: `GetGetRecordAssociationsResponse`
    - `get_records` (array of object `GETGetRecordAssociation`) [maxItems=10] **REQ** — Array of get_record association data.
      schema: `GETGetRecordAssociation`
      - `_associations` (array of object `GETAssociation`) [maxItems=10] **REQ** — List of associations for this get_record.
        schema: `GETAssociation`
        - `resources` (array of object `GETResource`) [maxItems=25] **REQ** — Resources that use this component.
          schema: `GETResource`
          - `name` (string) **REQ** [maxLen=255] — Name of the resource.
          - `id` (string) **REQ** [maxLen=255] — Unique identifier of the resource.
          - `_details` (object `GETResourceDetails`) **REQ** — Details about the resource type.
            schema: `GETResourceDetails`
            - `type` (string) **REQ** [maxLen=255] — Type of the resource (e.g., 'get_records', 'action').
        - `type` (string) **REQ** [maxLen=255] — Type of association (e.g., 'kiosk_states').
      - `id` (string) **REQ** [maxLen=19] — Get record identifier.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Returned when the request contains invalid path parameters.
**Resolution:** The kioskId and getRecordId path parameters must reference a valid, existing kiosk and get_record component in the organization. — Schema: `GetRecordErrorResponse` [application/json]
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
