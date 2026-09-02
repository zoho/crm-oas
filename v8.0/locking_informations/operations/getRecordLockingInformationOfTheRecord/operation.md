# GET /{moduleName}/{recordId}/Locking_Information__s
**Operation:** `getRecordLockingInformationOfTheRecord` — Get record locking information
> To retrieve the locking information details of a locked record in your Zoho CRM account, including the user who locked the record, the lock source, reason, and timestamp.

**Parameters:**
- `moduleName` (path, string, required) [maxLen=256]: The API name of the module to which the locked record belongs. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name.
- `recordId` (path, string, required) [maxLen=32]: Specify the unique identifier of the record for which you want to manage the lock.
- `fields` (query, string, optional) [maxLen=2048]: Specify the field API names to include in the response. Accepts comma-separated values. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve the field IDs.

**Responses:**

- **200**: Returns the locking information details of the locked record, including the user who locked it, the lock source, reason, and timestamp. [application/json]
    > Contains the locking information details and pagination metadata for the locked record.
    - `data` (array of object) [maxItems=1] **REQ** — Contains the locking information details of the locked record.
      - `Locked_By__s` (object) — An object containing the details of the user who locked the record. Returns **null** for automatically locked records where no specific user performed the lock.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who locked the record.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who locked the record.
        - `module` (string) [maxLen=255] — Represents the module to which the user who locked the record belongs.
      - `Locked_For__s` (object) — Represents the details of the record that is locked.
        - `module` (object) **REQ** — Represents the details of the module to which the locked record belongs.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module of the locked record.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the module of the locked record.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the locked record.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the locked record.
      - `$field_states` (object) — Represents the field-level lock states of the record. Returns **null** when no field-level locking is applied.
        anyOf:
            type: string [maxLen=255] — Contains the locking information details and pagination metadata for the locked record.
            type: null — Contains the locking information details and pagination metadata for the locked record.
      - `Locked_Reason__s` (string) [maxLen=3000, nullable] — Represents the reason for locking the record. Returns **null** for automatically locked records.
      - `$editable` (boolean) — Indicates whether the locked record is editable by the current user. Possible values: **true** - The record is editable. **false** - The record is not editable.
      - `$sharing_permission` (string) [maxLen=10000] — Represents the sharing permission level of the current user on the locked record.
      - `Lock_Source__s` (string) [maxLen=255, enum=['Manual', 'Both', 'Automatic']] — Indicates the source of the record lock. Possible values: **Manual** - The record was locked manually by a user. **Automatic** - The record was locked automatically by a rule. **Both** - The record has both manual and automatic locks.
      - `Locked_Time__s` (string/date-time) — Represents the timestamp when the record was locked.
      - `Record_Locking_Configuration_Id__s` (string) [maxLen=255] — Represents the unique identifier of the record locking configuration applied to this record.
      - `Record_Locking_Rule_Id__s` (string) [maxLen=255, nullable] — Represents the unique identifier of the record locking rule. Returns **null** for manually locked records.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the locking information record.
      - `Feature_Type__s` (string) [maxLen=255] — Represents the feature type associated with the locking information.
      - `$zia_visions` (object) — Represents Zia Visions data associated with the record. Returns **null** when Zia Visions data is not available.
        anyOf:
            type: string [maxLen=255] — Contains the Zia Visions related information.
            type: null — Null when Zia Visions data is not available.
    - `info` (object) **REQ** — An object containing the pagination details.
      - `per_page` (integer/int32) **REQ** — Represents the number of records displayed per page.
      - `count` (integer/int32) **REQ** — Represents the total number of locking information records returned in the response.
      - `page` (integer/int32) **REQ** — Represents the current page number of the response.
      - `more_records` (boolean) **REQ** — Indicates whether more locking information records are available beyond the current page. Possible values: **true** - More records are available. **false** - No more records are available.
      - `next_page_token` (string) [maxLen=255, nullable] — Represents the token used to fetch the next page of records. Returns **null** when token-based pagination is not in use or no next page exists.
      - `previous_page_token` (string) [maxLen=255, nullable] — Represents the token used to fetch the previous page of records. Returns **null** when token-based pagination is not in use or no previous page exists.
      - `page_token_expiry` (string) [maxLen=255, nullable] — Represents the expiry timestamp of the page token. Returns **null** when token-based pagination is not in use.

- **204**: The record does not have any active locks from the record locking configuration.

- **400**: The request contains invalid or missing parameters. **Resolution:** Verify that the module name, record ID, and field names in the request are valid. [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [enum=['relation not found']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [enum=['the related id given seems to be invalid']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code indicating the action is not allowed.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [enum=['Required Record Locking Configuration is not present']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.

**Scopes:** ZohoCRM.settings.modules.READ
