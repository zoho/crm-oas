# POST /{moduleApiName}/{id}/actions/convert
**Operation:** `convertInventory` — Convert Inventory Record
> To convert an inventory record in your Zoho CRM organization from one module to another. Supported conversion paths are: Quotes to Sales Orders or Invoices, and Sales Orders to Invoices.

**Parameters:**
- `moduleApiName` (path, string, required) [enum=['Quotes', 'Sales_Orders']]: Specify the API name of the source inventory module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module's API name.
- `id` (path, string, required) [maxLen=255]: Specify the unique ID of the source inventory record to convert. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module's ID. 
**Possible values:** Quotes, Sales_Orders.


**Request Body** (required) — application/json
> The request body must contain a data array with one object.
  > Represents the request payload for the inventory record conversion.
  - `data` (array of object) [maxItems=1] — Specify the inventory record conversion details.
    - `convert_to` (array of object) [maxItems=1] **REQ** — Specify the target module details for the conversion.
      - `module` (object) **REQ** — Specify the target inventory module to which the record is to be converted.
        - `api_name` (string) **REQ** [maxLen=50] — Specify the API name of the target inventory module. Possible values: **Invoices**, **Sales_Orders**. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module IDs and API names.
        - `id` (string/int64) **REQ** [maxLen=255] — Unique ID of the target module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID.
      - `carry_over_tags` (boolean) — Specifies whether the tags from the source record are carried over to the converted target record. Must be set to true or omitted; setting this to false returns a NOT_ALLOWED error.

**Responses:**

- **200**: Returns the conversion result, including the unique ID and display name of the converted record in the target module. [application/json]
    > Represents the successful response returned when the inventory record is converted.
    - `data` (array of object) [maxItems=1] — Represents the list of conversion results returned by the operation.
      - `code` (string) [enum=['SUCCESS']] — Represents the result code of the conversion operation. Possible values: **SUCCESS**.
      - `message` (string) [enum=['The record has been converted successfully']] — Represents the message describing the result of the conversion operation.
      - `status` (string) [enum=['success']] — Represents the status of the conversion operation. Possible values: **success**.
      - `details` (object) — Represents the details of the converted record, organized by the target module API name.
        - `Sales_Orders` (object) — Represents the details of the converted Sales Order record.
          - `id` (string) [maxLen=255] — Represents the unique ID of the converted Sales Order record.
          - `name` (string) [maxLen=50] — Represents the display name of the converted Sales Order record.
        - `Invoices` (object) — Represents the details of the converted Invoice record.
          - `id` (string) [maxLen=255] — Represents the unique ID of the converted Invoice record.
          - `name` (string) [maxLen=50] — Represents the display name of the converted Invoice record.

- **400**: Returns a validation error when the request data is invalid or a required field is missing. [application/json]
    > Represents the possible error response shapes returned for validation failures in the conversion request.
    oneOf:
        - `code` (string) **REQ** [maxLen=100, enum=[10 values]] — Represents the error code returned for the validation failure. Possible values: **INVALID_DATA**, **MANDATORY_NOT_FOUND**, **ID_ALREADY_CONVERTED**, **NO_PERMISSION**, **AMBIGUITY_DURING_PROCESSING**, **EXPECTED_FIELD_MISSING**, **INVALID_REQUEST_METHOD**, **NOT_APPROVED**, **NOT_REVIEWED**, **RECORD_LOCKED**. Always returned in the response.
        - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the issue. Always returned in the response.
        - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status of the response. Possible values: **error**. Always returned in the response.
        - `details` (object) **REQ** — Represents additional details about the error, such as the field name, JSON path, or expected data type. Always returned in the response.
        - `data` (array of object) [maxItems=4] **REQ** — Represents the list of validation error details returned for the failed conversion.
          - `code` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error code for the validation failure. Possible values: **AMBIGUITY_DURING_PROCESSING**, **EXPECTED_FIELD_MISSING**, **NOT_ALLOWED**, **INVALID_DATA**, **DUPLICATE_DATA**. Always returned in the response.
          - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the validation issue. Always returned in the response.
          - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status of the response. Possible values: **error**. Always returned in the response.
          - `details` (object) **REQ** — Represents additional details about the validation error, such as the field name, JSON path, or expected data type. Always returned in the response.

- **403**: Returns a permission denied error when the caller lacks access to the source or target inventory module. [application/json]
    > Represents the permission denied response returned when the caller lacks access to the source or target inventory module.
    oneOf:
        - `data` (array of object) [maxItems=4] **REQ** — Represents the list of permission error details returned by the operation.
          - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission failure. Possible values: **NO_PERMISSION**. Always returned in the response.
          - `details` (object) **REQ** — Represents additional details about the permission error, such as the required permissions or the resource path index. Always returned in the response.
          - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the permission denial. Always returned in the response.
          - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status of the response. Possible values: **error**. Always returned in the response.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission failure. Possible values: **NO_PERMISSION**. Always returned in the response.
        - `details` (object) **REQ** — Represents additional details about the permission denial, such as the required permissions. Always returned in the response.
        - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the permission denial. Always returned in the response.
        - `status` (string) **REQ** [maxLen=50, enum=['error']] — Represents the status of the response. Possible values: **error**. Always returned in the response.

**Scopes:** ZohoCRM.modules.Quotes.CREATE, ZohoCRM.modules.SalesOrders.CREATE
