# DELETE /Appointments__s
**Operation:** `deleteAppointmentsS` — Delete one or more appointment records

> To delete one or more appointment records in your Zoho CRM organization. Note that this API will not delete any deals created on the completion of the deleted appointments.


**Parameters:**
- `ids` (query, number, optional) [enum=[111115000000147280, 111115000000147230]]: Specify the IDs of the appointment records to delete. Accepts comma-separated record IDs. Use the [Get Appointments API](appointments.yaml#$.paths./Appointments__s.get) to get the IDs.

**Schemas:**
`Delete207SuccessResponse`:
  > Represents a successful deletion result in the multi-Status response, containing the deleted record ID.
  - `code` (string) **REQ** [maxLen=255] — Represents the response code for the delete operation.
  - `details` (object) **REQ** — Represents the details of the deleted appointment record, including the record ID.
    - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the deleted appointment record.
  - `message` (string) **REQ** [maxLen=255] — Represents the message for the record deletion.
  - `status` (string) **REQ** [maxLen=255] — Indicates the status of the record deletion.
`ErrorResponseCore2137699283`:
  > Represents the error when one or more appointment records cannot be deleted.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
  - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
    - `id` (string) **REQ** [maxLen=255] — Represents the ID of the appointment record that could not be processed.
  - `message` (string) **REQ** [enum=['record not deleted']] — Represents the error message describing the validation failure.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status.

**Responses:**

- **200**: Returns a confirmation that all specified appointment records were deleted successfully. Each item in the data array contains the record ID, a SUCCESS code, and a "record deleted" message.
 — Schema: `DeleteappointmentssResponse200` [application/json]
    > Represents the success response for the bulk appointment deletion request.
    schema: `DeleteappointmentssResponse200`
    - `data` (array of object `DataNested1`) [maxItems=3] — Represents the list of deletion result objects for each appointment record in the request.
      schema: `DataNested1`
      - `code` (string) [maxLen=255] — Represents the result code for the operation.
      - `details` (object `DetailsNested`) — Represents the details of an appointment record, including its ID, creation timestamp, and last modification timestamp.
        schema: `DetailsNested`
        - `Modified_Time` (string) [maxLen=120] — Represents the date and time when the appointment record was last modified.
        - `Modified_By` (object `ModifiedByNested`) — Represents the user who last modified the appointment record, including the user ID, full name, and email address.
          schema: `ModifiedByNested`
          - `name` (string) [maxLen=255, nullable] — Represents the full name of the user who last modified the appointment record.
          - `id` (string) [maxLen=255, nullable] — Represents the unique ID of the user who last modified the appointment record.
          - `email` (string/email) [maxLen=33, nullable] — Represents the email address of the user who last modified the appointment record.
        - `Created_Time` (string) [maxLen=120] — Represents the date and time when the appointment record was created.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the appointment record.
        - `Created_By` (object `CreatedByNested`) — Represents the user who created the appointment record, including the user ID, full name, and email address.
          schema: `CreatedByNested`
          - `name` (string) [maxLen=255, nullable] — Represents the full name of the user who created the appointment record.

          - `id` (string) [maxLen=255, nullable] — Represents the unique identifier of the user who created the appointment record.

          - `email` (string/email) [maxLen=33, nullable] — Represents the email address of the user who created the appointment record.

      - `message` (string) [maxLen=255] — Represents the result message for the operation.
      - `status` (string) [maxLen=255] — Indicates the status of the operation.

- **207**: Returns a mixed-status response when the delete operation partially succeeds. Each item in the data array contains either a SUCCESS code with a "record deleted" message or an INVALID_DATA code with a "record not deleted" message, based on the outcome for each individual record.
 [application/json]
    > Represents the Multi-Status response body returned when a bulk deletion request results in a mix of successful and failed appointment deletion attempts.

    - `data` (array of object) [minItems=2, maxItems=200] **REQ** — Represents the list of result objects for each appointment deletion attempt. Each item is either a success confirmation or an error response.

      oneOf:
        - `Delete207SuccessResponse` — Represents a successful deletion result in the multi-Status response, containing the deleted record ID.

- **400**: The request could not be processed due to an invalid appointment ID, an invalid module name, or an unsupported HTTP request method.

**Resolution:** For INVALID_DATA, make a GET Appointments API call and provide a valid appointment ID. For INVALID_REQUEST_METHOD, use only the DELETE method. For INVALID_MODULE, verify that the module API name in the request is correct. [application/json]
    > Represents the error response body for a failed DELETE Appointments request, containing either a list of record-level validation errors or a single request-level error.

    oneOf:
        - `data` (array of object `ErrorResponseCore2137699283`) [maxItems=25] **REQ** — Represents the list of error objects for the appointment records that could not be deleted.

      - `ErrorResponseCore1875045219` — Represents the error when the HTTP request method is not supported.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents the error details object.
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Represents the error message describing the invalid request method.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
      - `ErrorResponseCore1604218709` — Represents the error when the module API name in the request URL is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents the details about the path parameter that caused the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path parameter in the request URL that is invalid.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message describing the invalid module name.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status.

**Scopes:** ZohoCRM.modules.appointments.DELETE
