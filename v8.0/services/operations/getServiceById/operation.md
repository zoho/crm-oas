# GET /Services__s/{id}
**Operation:** `getServiceById` — Retrieve a specific service record by ID

> To retrieve the full details of a single service record from your Zoho CRM organization using its unique ID, including its availability configuration, members, pricing, tax details, and subform data.


**Parameters:**
- `id` (path, string, required) [maxLen=100] {style=simple, explode=False}: Specify the unique ID of the service record to be retrieved, updated, or deleted.

**Responses:**

- **200**: Returns the full details of the requested service record, including its availability configuration, members, owner, pricing, tax, audit timestamps, and currency-formatted values.
 — Schema: `GetServiceByIdResponse200` [application/json]
    > Wrapped response that returns a single service record. Contains a data array with exactly one service object carrying the full set of service fields.
    schema: `GetServiceByIdResponse200`
    - `data` (array of object `GETDataNested`) [minItems=1, maxItems=1] **REQ** — Represents the array containing the requested service record.
      schema: `GETDataNested`
      - `Job_Sheet_Required` (string) **REQ** [maxLen=255, enum=['Yes', 'No']] — Represents whether a job sheet is required for the service. **Possible values**: Yes, No.

      - `Owner` (object `GETOwnerNested`) **REQ** — Represents the owner of the returned service record, identified by name, ID, and email. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        schema: `GETOwnerNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `email` (string) **REQ** [maxLen=255] — Represents the email address of the user.
      - `Description` (string) **REQ** [maxLen=32000, nullable] — Represents the description of the service.
      - `$currency_symbol` (string) [maxLen=255] — Represents the currency symbol used to format monetary fields on the service record.
      - `$field_states` (null) **REQ** — Represents the field-state metadata for the service record.
      - `$photo_id` (null) **REQ** — Represents the photo ID associated with the service record.
      - `Available_Days` (array of object) [maxItems=7] **REQ** — Represents the list of business days on which the service is available.
      - `Tax` (array of object) [maxItems=100] **REQ** — Represents the taxes applied to the service cost.
      - `$sharing_permission` (string) **REQ** [maxLen=255] — Represents the sharing permission level of the current user on the service record.
      - `Unavailable_From` (string) **REQ** [maxLen=255, nullable] — Represents the date and time from which the service is unavailable.
      - `Last_Activity_Time` (string) **REQ** [maxLen=255] — Represents the timestamp of the most recent activity on the service record.
      - `Record_Image` (null) **REQ** — Represents the record image associated with the service.
      - `Modified_By` (object `GETModifiedByNested`) **REQ** — Represents the user who last modified the returned service record, identified by name, ID, and email. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        schema: `GETModifiedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `email` (string) **REQ** [maxLen=255] — Represents the email address of the user.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the service record.
      - `Available_Dates` (array of object) [maxItems=20] **REQ** — Represents the list of dates on which the service is available.
      - `Status` (string) **REQ** [maxLen=255, enum=['Available', 'Temporarily Unavailable', 'Not in Use', 'Scheduled']] — Represents the operational status of the service. 


**Possible values**: Available, Not in Use, Scheduled, Temporarily
Unavailable.

      - `Modified_Time` (string) **REQ** [maxLen=255] — Represents the timestamp when the service record was last modified.
      - `Available_Timings` (array of object `GETAvailableTimingsNested`) [maxItems=3, nullable] **REQ** — Represents the available time windows configured for the service.
        schema: `GETAvailableTimingsNested`
        - `From` (string) **REQ** [maxLen=255] — Represents the start of the availability time window, in HH:MM (24-hour) format.

        - `To` (string) **REQ** [maxLen=255] — Represents the end of the availability time window, in HH:MM (24-hour) format.

      - `Service_Name` (string) **REQ** [maxLen=120] — Represents the name of the service.
      - `Available_From` (string) **REQ** [maxLen=255] — Represents the date from which the service is available.
      - `$data_source_details` (object) — Represents the $data_source_details block on a returned service record. Carries metadata about the data source from which the record originated.
      - `Created_Time` (string) **REQ** [maxLen=255] — Represents the timestamp when the service record was first saved to the organization.
      - `Available_Till` (string) **REQ** [maxLen=255, nullable] — Represents the date until which the service is available.
      - `$editable` (boolean) **REQ** — Indicates whether the current user can edit the service record.
      - `Duration` (integer/int32) **REQ** — Represents the duration of the service, in minutes.
      - `Job_Sheet_Section__s` (null) **REQ** — Represents the job sheet section associated with the service.
      - `Record_Status__s` (string) [maxLen=255] — Represents the system-derived record status of the service.
      - `Price` (integer/int32) **REQ** — Represents the price charged for the service in the organization currency.
      - `$status` (string) **REQ** [maxLen=255] — Represents the internal status identifier of the service record.
      - `Created_By` (object `GETCreatedByNested`) **REQ** — Represents the user who created the returned service record, identified by name, ID, and email. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        schema: `GETCreatedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `email` (string) **REQ** [maxLen=255] — Represents the email address of the user.
      - `Tag` (array of string) [maxItems=100, nullable] **REQ** — Represents the tags associated with the service record. Refer to the [Get tags](tags.yaml#$.paths./settings/tags.get) endpoint for details.
        items: [maxLen=2000]
      - `Availability_Type` (string) **REQ** [maxLen=255] — Represents how the service availability is defined. 


**Possible values**: Specific Day(s), Specific Date Range, Every
Business Days, Specific Date(s).

      - `Members` (array of object `GETMembersNested1`) [maxItems=2] **REQ** — Represents the users who deliver the service. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        schema: `GETMembersNested1`
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the member on the service record. 
        - `Members` (object `GETMembersNested`) **REQ** — Represents a member who delivers the returned service, identified by module, name, and ID. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
          schema: `GETMembersNested`
          - `module` (string) **REQ** [maxLen=255] — Represents the source module of the member. Typically, the Users module.
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who delivers the service. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who delivers the service. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
      - `Location` (string) **REQ** [maxLen=255] — Represents where the service is delivered.


**Possible values**: Client Address, Business Address, Business
Address and Client Address.

      - `Unavailable_Till` (null) **REQ** — Represents the date and time until which the service remains unavailable.
      - `$has_more` (object `GETHasMoreNested`) **REQ** — Indicates whether additional related items exist beyond those included in the response.
        schema: `GETHasMoreNested`
        - `Members` (boolean) **REQ** — Indicates whether more members exist than those included in the current response.
      additionalProperties: any
    additionalProperties: any

- **400**: The request cannot be processed because the module name in the URL is invalid or a required query parameter is missing.

**Resolution:** Ensure the module API name in the request URL references an existing module and that all required query parameters are included in the request.
 [application/json]
    > Error response returned when the module name in the request URL is invalid or a required query parameter is missing from the request. Contains one of: `InvalidModuleNameError` or `RequiredParamMissingError`.

    oneOf:
      - `InvalidModuleNameError` — Error response returned when the module name in the request URL does not match any module in the Zoho CRM organization.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned for the failed request.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment that caused the failure.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message for the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
      - `RequiredParamMissingError` — Error response returned when a required query parameter is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned for the failed request.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the missing query parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message describing that a required query parameter is missing from the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 

**Scopes:** ZohoCRM.modules.services.READ
