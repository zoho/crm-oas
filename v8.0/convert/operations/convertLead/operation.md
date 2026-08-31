# POST /Leads/{leadId}/actions/convert
**Operation:** `convertLead` — Convert a Lead
> Converts a Lead record into Contact, Account, and/or Deal records. Allows configuration of conversion behavior including overwrite settings, notifications, owner assignment, and tag carryover.

**Parameters:**
- `leadId` (path, string/int64, required): Unique identifier of the Lead record to convert. Must be a valid Lead ID that exists in the CRM and has not been previously converted. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the lead ID.

**Schemas:**
`EntityReference`:
  > Reference to a CRM entity with ID and name
  - `name` (string) **REQ** [maxLen=200] — Represents the name of the entity.
  - `id` (string) **REQ** [maxLen=20] — Unique identifier of the entity record (int64 as string)
`ValidationError`:
  > Validation error details
  - `status` (string) **REQ** [enum=['error']] — Error status indicator
  - `code` (string) **REQ** [enum=[7 values]] — Error code identifying the type of validation failure
  - `message` (string) **REQ** [maxLen=500] — Message that explains why the lead conversion request failed validation.
  - `details` (object) **REQ** — Additional error context and affected field information
    - `api_name` (string) [maxLen=100] — API name of the affected field
    - `json_path` (string) [maxLen=200] — JSONPath to the affected field in the request
    - `mapped_field` (string) [maxLen=100] — Name of the field that has a mapping relationship
    - `expected_data_type` (string) [maxLen=50] — Expected data type for the field
    - `maximum_length` (integer/int32) — Maximum allowed length for the field
    additionalProperties: any
`ValidationErrorWrapper`:
  > Wrapper for validation error responses
  - `data` (array of object `ValidationError`) [maxItems=100] **REQ** — Array of validation errors

**Request Body** (required) — application/json `ConversionRequestWrapper`
> Lead conversion configuration including optional Deal creation, owner assignment, notification preferences, and tag carryover settings.
  > Wrapper object containing array of conversion requests
  - `data` (array of object `ConversionRequest`) [maxItems=100] **REQ** — Array of lead conversion configurations
    schema: `ConversionRequest`
    - `overwrite` (boolean) — Determines whether to overwrite the Account Name in a Contact when converting a Lead.
For example, If a Contact is already linked to an Account but the Lead’s Company name is different, enabling this option will update the Contact’s Account to match the Lead’s Company.
**Possible values:**
false (default) : Keeps the existing Account Name in the Contact unchanged.
true : Updates the Contact’s associated Account Name if it differs from the Company name in the Lead.
    - `notify_lead_owner` (boolean) [default=False] — If true, sends email notification to the Lead owner about the conversion. Default is false.
    - `notify_new_entity_owner` (boolean) [default=False] — If true, notifies the owner(s) of newly created Contact, Account, or Deal records. Default is false.
    - `add_to_existing_record` (boolean) — When true, associates the Lead with an existing Account or Contact instead of creating duplicates.
    - `assign_to` (object) — Assigns a record owner for the new Contact and Account after lead conversion. It ensures that the converted lead is assigned to a specific user in Zoho CRM. Use the [Users API](users.yaml#$.paths./users/bulk.get) to retrieve valid User IDs.
      - `id` (string) **REQ** [maxLen=20] — Zoho CRM user ID (int64 as string)
    - `Deals` (object `DealConversion`) — Deal record configuration for lead conversion
      schema: `DealConversion`
      - `Deal_Name` (string) **REQ** [maxLen=120] — Specify the name of the Deal
      - `Campaign_Source` (string) [maxLen=100] — Campaign source associated with this Deal
      - `Amount` (number/double) — Expected revenue amount for the Deal
      - `Contact_Role` (string) [maxLen=50] — Represents the **role** of the Contact in this Deal
      - `Pipeline` (string) **REQ** [maxLen=100] — Indicates the **sales pipeline** for the Deal. Must match an existing pipeline in the CRM.
      - `$move_attachments` (boolean) — If true, moves attachments from the Lead to the Deal
      - `Stage` (string) **REQ** [maxLen=100] — Current stage of the Deal within the specified Pipeline. Must be valid for the chosen Pipeline.
      - `Closing_Date` (string/date) **REQ** — Expected closing date for the Deal (ISO 8601 date format: YYYY-MM-DD)
      - `Type` (string) [maxLen=50] — Type of Deal (e.g., New Business, Existing Business)
      - `Probability` (integer/int32) [min=0, max=100] — Win probability percentage (0-100)
      - `Lead_Source` (string) [maxLen=100] — Source from which the Lead originated
      - `Next_Step` (string) [maxLen=200] — Next action or milestone for the Deal
      - `Description` (string) [maxLen=32000] — Detailed description of the Deal
    - `carry_over_tags` (object) — Configuration for carrying over tags from the Lead to converted records
      - `Contacts` (object) — Tag carryover settings for Contact records.
      - `Accounts` (object) — Tag carryover settings for Account records
      - `Deals` (object) — Tag carryover settings for Deal records

**Responses:**

- **200**: Lead successfully converted. Returns details of created Contact, Account, and Deal records with their IDs and names. — Schema: `ConversionSuccessWrapper` [application/json]
    > Wrapper for successful conversion response
    schema: `ConversionSuccessWrapper`
    - `data` (array of object `ConversionSuccess`) [maxItems=100] **REQ** — Array of conversion results
      schema: `ConversionSuccess`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Status code indicating successful conversion
      - `message` (string) **REQ** [maxLen=500] — Message that summarizes the outcome of the lead conversion request.
      - `status` (string) **REQ** [enum=['success']] — Overall status of the conversion operation
      - `details` (object) **REQ** — Details of created records including their IDs and names.
        - `Contacts` (object `EntityReference`) **REQ** — Reference to a CRM entity with ID and name
        - `Deals` (object) **REQ** — Deal record information, or null if no Deal was created
          oneOf:
            - `EntityReference` — Reference to a CRM entity with ID and name
              type: null — No Deal was created during conversion
        - `Accounts` (object) **REQ** — Account record information, or null if no Account was created
          oneOf:
            - `EntityReference` — Reference to a CRM entity with ID and name
              type: null — No Account was created during conversion

- **202**: Lead conversion request accepted and scheduled for processing, or contains validation errors. [application/json]
    > Represents the response payload for scheduled conversion processing or validation-level errors.
    oneOf:
      - `ConversionScheduledWrapper` — Wrapper for scheduled conversion response
        - `data` (array of object `ConversionScheduled`) [maxItems=1] **REQ** — Array containing the scheduled job information
          schema: `ConversionScheduled`
          - `code` (string) **REQ** [enum=['SCHEDULED']] — Status code indicating conversion was scheduled
          - `message` (string) **REQ** [maxLen=500] — Message that summarizes the scheduling result for the lead conversion request.
          - `status` (string) **REQ** [enum=['success']] — Overall status
          - `details` (object) **REQ** — Job details
            - `job_id` (string) **REQ** [maxLen=20] — Unique job identifier
      - `ValidationErrorWrapper` — Wrapper for validation error responses

- **400**: Bad request due to invalid input data, malformed request, or attempting to convert an already converted Lead. [application/json]
    > Represents the response payload for invalid input or request-level conversion errors.
    oneOf:
      - `ValidationErrorWrapper` — Wrapper for validation error responses
      - `ErrorResponse` — Root-level error response without data wrapper
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
        - `code` (string) **REQ** [enum=[6 values]] — Indicates the error code.
        - `message` (string) **REQ** [maxLen=500] — Error message
        - `details` (object) **REQ** — Error details
          - `resource_path_index` (integer/int32) — Index of the resource path that caused the error.
          - `param_name` (string) [maxLen=100] — Name of the missing or invalid parameter. 
          additionalProperties: any

**Scopes:** ZohoCRM.modules.CREATE
