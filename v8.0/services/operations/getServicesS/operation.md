# GET /Services__s
**Operation:** `getServicesS` — Get services
> To retrieve the list of service records in your Zoho CRM organization that match the specified filter criteria. Supports pagination using either the **page** or **page_token** parameter and can return up to 100,000 services across paginated requests.


**Parameters:**
- `fields` (query, string, required): Specify a comma-separated list of field API names to include in the response. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve the field IDs and API names.
- `cvid` (query, string/int64, optional): Specify the unique ID of the Custom View. Use the [Get Custom Views Metadata API](custom_views.yaml#$.paths./settings/custom_views.get) to retrieve the Custom View IDs.
- `page_token` (query, string, optional) [maxLen=96]: Specify the page token to retrieve records beyond the first 2,000 results. Use the **next_page_token** value from a previous response to access the next page of results.
- `page` (query, integer/int32, optional) [min=1]: Specify the page number to retrieve. Starts at 1.
- `per_page` (query, integer/int32, optional) [min=1, max=200]: Specify the number of records to return per page. Maximum is 200.
- `sort_order` (query, string, optional) [enum=['desc', 'asc']]: Specify the sort order for the records.<br/> <b>Possible values:</b> <br/>desc - Returns records in descending order.<br/> asc - Returns records in ascending order.
- `sort_by` (query, string, optional) [enum=['id', 'Created_Time', 'Modified_Time']]: Specify the field to sort records by.  Possible values:**id** - Sorts by record ID.  **Created_Time** - Sorts by creation timestamp.  **Modified_Time** - Sorts by last modification timestamp.

**Responses:**

- **200**: Returns the list of service records matching the specified filter criteria, up to 200 records per page. Each record includes the full set of service fields. 

The response also contains an **info** object with pagination details such as **per_page**, **page**, **more_records**, and **sort_order**.
 — Schema: `GetservicessResponse200` [application/json]
    > Wrapped response that lists the service records matching the request. Contains a data array with up to 200 service objects, each carrying the full set of service fields.
    schema: `GetservicessResponse200`
    - `data` (array of object `GETDataNested`) [minItems=1, maxItems=200] **REQ** — Represents the array of service records returned by the request.
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

- **400**: The request could not be processed because the module name in the URL is invalid or a required query parameter is missing.

**Resolution:** The module API name in the request URL must reference a valid module, and the required query parameters must be included in the request. [application/json]
    > Contains the error response for a 400 Bad Request on the Get Services endpoint. The schema is one of `InvalidModuleNameError` or `RequiredParamMissingError`, depending on the type of validation failure.

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
