# DELETE /Appointments__s/{appointmentId}
**Operation:** `deleteAppointmentById` — Delete an Appointment by ID

> To delete a single appointment record from your Zoho CRM organization by its unique ID. Note that this operation will not delete any deals created upon completion of the appointment.


**Parameters:**
- `appointmentId` (path, string, required) [maxLen=100]: Specify the unique identifier of the appointment record. Use the [Get Appointments API](appointments.yaml#$.paths./Appointments__s.get) to retrieve all appointment records and obtain the ID of the required appointment record.

**Responses:**

- **200**: Returns a confirmation that the specified appointment record was successfully deleted from Zoho CRM, including the ID of the deleted record.
 — Schema: `DeleteidResponse200` [application/json]
    > Represents the success response for the single appointment deletion request.
    schema: `DeleteidResponse200`
    - `data` (array of object `DataNested1`) [maxItems=1] — Represents the list of deletion result objects for the deleted appointment record.
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

- **400**: The request failed due to an invalid appointment ID, an unsupported HTTP method, or an invalid module name.

**Resolution:** Verify that the appointment ID is correct and has not already been deleted. Use only the DELETE HTTP method and ensure the module name in the request URL is valid.
 [application/json]
    > Represents the error response body for a failed DELETE request to remove a single appointment record. The response conforms to one of several error variants depending on the cause of the failure.

    oneOf:
        - `data` (array of object `ErrorResponseCore2137699283`) [maxItems=25] **REQ** — Represents the list of error objects returned when the DELETE request fails due to an invalid appointment ID or a reference to a record that has already been deleted. 

          schema: `ErrorResponseCore2137699283`
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
          - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
            - `id` (string) **REQ** [maxLen=255] — Represents the ID of the appointment record that could not be processed.
          - `message` (string) **REQ** [enum=['record not deleted']] — Represents the error message describing the validation failure.
          - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
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
      - `ErrorResponseCoreInvalidDataFlat` — Represents the error response returned when the appointment record could not be deleted due to invalid data.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the flat invalid data failure.
        - `details` (object) **REQ** — Represents the error details for the invalid data failure, including the resource path index.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path in the request that triggered the invalid data error.
        - `message` (string) **REQ** [enum=['record not deleted']] — Represents the error message describing the invalid data failure.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status for the invalid data failure.

**Scopes:** ZohoCRM.modules.appointments.DELETE
