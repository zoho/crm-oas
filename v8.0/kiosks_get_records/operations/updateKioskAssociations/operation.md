# PUT /settings/kiosks/{kioskId}/associations
**Operation:** `updateKioskAssociations` — Kiosk Associations
> This API allows you to associate an active Kiosk with the Record Detail View Page of a module. Once associated, the Kiosk will be available within the selected module's Record Detail View Page based on the specified layout.

Use the [Get All Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID. Ensure that the Kiosk is in the active state before associating it.


**Note:**
  - To delete an existing association, include the _delete key with a null value ("_delete": null) in the request. Refer to the Sample input to disassociate a Kiosk from the Record Detail View Page for an example.  Specify the association id to remove the Record Detail View Page association. Use the [Kiosk Associations API](kiosks_get_records.yaml#$.paths./settings/kiosks/associations.get) to retrieve the ID.
  - The maximum number of Kiosk associations allowed per layout depends on your CRM edition:
     - Standard / Professional: 1 association
     - Enterprise: 3 associations
     - Ultimate and above: 5 associations


**Parameters:**
- `kioskId` (path, string, required) [maxLen=255]: Unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID.

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

**Request Body** (required) — application/json `UpdateKioskAssociationsRequest`
  > Request body for updating kiosk associations.
  - `kiosks` (array of object `KioskAssociationPayload`) [maxItems=1] **REQ** — Array of kiosk association configurations.
    schema: `KioskAssociationPayload`
    - `_associations` (array of object `AssociationConfig`) [maxItems=1] **REQ** — Association configurations.
      schema: `AssociationConfig`
      - `type` (string) **REQ** [maxLen=20, enum=['detail_view_page']] — Type of association.
      - `detail_view_page` (array of object `DetailViewPageConfig`) [maxItems=1] **REQ** — Detail view page configurations.
        schema: `DetailViewPageConfig`
        - `layout` (object `LayoutRef`) **REQ** — Layout to associate the kiosk with.
          schema: `LayoutRef`
          - `id` (string) **REQ** [maxLen=19] — Unique identifier of the layout.
        - `name` (string) **REQ** [maxLen=255] — Display name for the association widget on the detail view page.
        - `_delete` (string) [maxLen=255, nullable] — Set to trigger deletion of this association.
        - `module` (object `ModuleRefUpdate`) **REQ** — Module for the detail view page association.
          schema: `ModuleRefUpdate`
          - `name` (string) [maxLen=50, nullable] — Display name of the module.
          - `id` (string) [maxLen=19, nullable] — Unique identifier of the module.
          - `api_name` (string) [maxLen=50, nullable] — API name of the module.
    - `id` (string) **REQ** [maxLen=255] — ID of the kiosk to associate.

**Responses:**

- **200**: Kiosk association updated successfully. — Schema: `UpdateKioskAssociationsResponse` [application/json]
    > Response after successfully updating kiosk associations.
    schema: `UpdateKioskAssociationsResponse`
    - `kiosks` (array of object `KioskOperationResult`) [maxItems=1] — Array of operation results.
      schema: `KioskOperationResult`
      - `code` (string) [maxLen=255] — Result code.
      - `details` (object `OperationResultDetails`) — Details of the operation result.
        schema: `OperationResultDetails`
        - `id` (string) [maxLen=255] — ID of the created, updated, or deleted resource.
      - `message` (string) [maxLen=255] — Human-readable result message.
      - `status` (string) [maxLen=255] — Status of the operation.
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

**Scopes:** ZohoCRM.settings.kiosks.UPDATE
