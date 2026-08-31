# GET /Leads/{leadId}/__conversion_options
**Operation:** `getLeadConversionOptions` — Lead Conversion Options
> Retrieves available conversion options for a lead including matching contacts, accounts, field mappings, and layout preferences. This endpoint helps determine what conversion paths are available before performing the actual lead conversion.

**Parameters:**
- `leadId` (path, string/int64, required): The unique identifier of the Lead record (int64 as string) for which you want to retrieve conversion options. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the lead record ID.

- `include_inner_details` (query, string, optional) [maxLen=256, minLen=1] {style=form, explode=False}: Fetches additional details of lookup or referenced inner resources within the same API call, avoiding separate dependent requests. Accepts a comma-separated list of inner resource paths starting from the root key of the response (the root key itself must not be included). Supports dot notation and JSONPath-style notation (e.g. $..key.sub_key). Invalid or non-permitted paths are silently ignored.

**Responses:**

- **200**: Successfully retrieved lead conversion options. Returns available contacts, accounts, field mappings, and layout preferences for the specified lead. [application/json]
    > Conversion options response containing available contacts, accounts, and field mappings for lead conversion
    - `__conversion_options` (object) — Container for all conversion option data
      - `module_preference` (object) **REQ** — Represents the preferred module selected for lead conversion. Returns the module API name and ID when a preference exists, or null when no preference is set.
        oneOf:
            - `api_name` (string) **REQ** [maxLen=100] — API name of the preferred module
            - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Unique identifier of the preferred module (int64 as string)
            type: null — No module preference set
      - `Contacts` (object) **REQ** — Represents matching Contact records for the lead. Returns an array when matches exist, or null when no matching contacts are found.
        oneOf:
            type: array of object [maxItems=100]
              - `Full_Name` (string) **REQ** [maxLen=200] — Full name of the contact
              - `Email` (object) **REQ** — Represents the contact email value. Returns the email address when available, or null when the contact has no email value.
                oneOf:
                    type: string/email — Email address of the contact
                    type: null — No email address provided
              - `Layout` (object) — Layout information for the contact record
                - `name` (string) **REQ** [maxLen=100] — Name of the layout
                - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Unique identifier of the layout (int64 as string)
              - `Locked__s` (boolean) **REQ** — Indicates if the contact record is locked
              - `Account_Name` (object) — Represents the account associated with the matched contact. Returns account details when an association exists, or null when no account is linked.
                oneOf:
                    - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Unique identifier of the account (int64 as string)
                    - `name` (string) **REQ** [maxLen=200] — Name of the account
                    - `Locked__s` (boolean) **REQ** — Indicates if the account record is locked
                    type: null — No account associated with this contact
              - `$editable` (boolean) **REQ** — Indicates if the contact record can be edited
              - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Unique identifier of the contact record (int64 as string)
              - `$approval_state` (string) **REQ** [enum=[5 values]] — Current approval state of the contact record
              - `Data_Processing_Basis` (object) **REQ** — Represents the GDPR data processing basis for the matched contact. Returns a basis value when configured, or null when it is not specified.
                oneOf:
                    type: string [maxLen=100] — GDPR data processing basis for the contact
                    type: null — No GDPR data processing basis specified
            type: null — No contacts found matching the lead data
      - `Accounts` (object) **REQ** — Represents matching Account records for the lead. Returns an array when matches exist, or null when no matching accounts are found.
        oneOf:
            type: array of object [maxItems=100]
              - `Phone` (object) **REQ** — Represents the account phone value. Returns a phone number when available, or null when the account has no phone value.
                oneOf:
                    type: string [maxLen=50] — Phone number of the account
                    type: null — No phone number provided
              - `Account_Type` (object) **REQ** — Represents the account type value. Returns the account type when available, or null when the account type is not specified.
                oneOf:
                    type: string [maxLen=100] — Type of the account
                    type: null — No account type specified
              - `Website` (object) **REQ** — Represents the account website value. Returns the website URL when available, or null when the account has no website value.
                oneOf:
                    type: string [maxLen=2000] — Website URL of the account
                    type: null — No website URL provided
              - `Account_Name` (string) **REQ** [maxLen=200] — Name of the account
              - `$editable` (boolean) **REQ** — Indicates if the account record can be edited
              - `Locked__s` (boolean) **REQ** — Indicates if the account record is locked
              - `$approval_state` (string) **REQ** [enum=[5 values]] — Current approval state of the account record
              - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Unique identifier of the account record (int64 as string)
            type: null — No accounts found matching the lead data
      - `preference_field_matched_value` (object) **REQ** — Represents field-level values from the lead that match existing Contact and Account fields. Returns mapped field details when matches exist, or null when no mappings are available.
        oneOf:
            - `Contacts` (object) — Represents Contact field mappings for matched lead values. Returns mapping entries when Contact matches exist, or null when no Contact mappings are available.
              oneOf:
                  type: array of object [maxItems=50]
                    - `field` (object) **REQ** — Details of the field being mapped, including its API name, display label, uniqueness constraint, and ID.
                      - `api_name` (string) **REQ** [maxLen=100] — API name of the field
                      - `field_label` (string) [maxLen=200] — Display label of the field
                      - `unique` (object) — Represents whether the matched Contact field has a uniqueness constraint. Returns a Boolean when uniqueness metadata is available, or null when it is not available.
                        oneOf:
                            type: boolean — Indicates if the field has unique constraint
                            type: null — Field does not have unique constraint information
                      - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Unique identifier of the field (int64 as string)
                    - `matched_lead_value` (string) **REQ** [maxLen=500] — Value from the lead that matches this field
                  type: null — No contact field mappings available
            - `Accounts` (object) — Represents Account field mappings for matched lead values. Returns mapping entries when Account matches exist, or null when no Account mappings are available.
              oneOf:
                  type: array of object [maxItems=50]
                    - `field` (object) **REQ** — Details of the field being mapped, including its API name, display label, uniqueness constraint, and ID.
                      - `api_name` (string) **REQ** [maxLen=100] — API name of the field
                      - `field_label` (string) [maxLen=200] — Display label of the field
                      - `unique` (object) — Indicates whether the matched Account field has a uniqueness constraint. Returns true if the field is unique, false if it is not, or null if the uniqueness metadata is unavailable.
                        oneOf:
                            type: boolean — Indicates if the field has unique constraint
                            type: null — Field does not have unique constraint information
                      - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Unique identifier of the field (int64 as string)
                    - `matched_lead_value` (string) **REQ** [maxLen=500] — Value from the lead that matches this field
                  type: null — No account field mappings available
            type: null — No field mappings available for conversion
      - `modules_with_multiple_layouts` (object) **REQ** — Represents modules that provide multiple layout choices during conversion. Returns module details when available, or null when no module offers multiple layouts.
        oneOf:
            type: array of object [maxItems=20]
              - `api_name` (string) **REQ** [maxLen=100] — API name of the module
              - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Unique identifier of the module (int64 as string)
            type: null — No modules have multiple layout options

- **204**: No conversion options available for this lead. The lead may not have any matching records or predefined conversion paths.

- **400**: Bad request due to invalid lead ID, record approval issues, or record locking conflicts. [application/json]
    > Represents the error response payload returned when the lead conversion options request fails validation or encounters record state restrictions.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_APPROVED', 'RECORD_LOCKED']] — Error code indicating the type of failure
        - `message` (string) **REQ** [maxLen=500] — Human-readable error message describing the issue
        - `status` (string) **REQ** [enum=['error']] — Status of the request
        - `details` (object) **REQ** — Additional error details including resource path information
          - `resource_path_index` (integer/int32) **REQ** — Index of the resource path parameter that caused the error

**Scopes:** ZohoCRM.modules.leads.READ
