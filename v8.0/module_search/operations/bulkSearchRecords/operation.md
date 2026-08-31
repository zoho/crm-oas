# POST /{module}/bulk/search
**Operation:** `bulkSearchRecords` — Bulk Search Records by Criteria, Word, Email, or Phone
> Searches for records in the specified module that match the given search criteria. This API accepts the same search parameters as the GET /{module}/search API, but they are provided in the request body instead of query parameters. Use this API when the search criteria are too long to be passed as query parameters. You must specify at least one of the following search parameters: criteria, email, phone, or word. A maximum of 2,000 records can be retrieved per search, with up to 15 criteria conditions. Newly created or updated records may not appear immediately in the search results due to indexing delays.

**Tags:** Search

**Parameters:**
- `module` (path, string, required) [maxLen=100]: Specify the API name of the module to search within. Refer to [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) to retrieve a list of available modules.
- `approval_state` (query, string, optional) [maxLen=50, enum=[15 values]]: Specify the approval state to filter records by. The search returns only records in the specified approval state.
Possible values: **approval_process_pending**, **webform_invalid**, **review_process_pending**, **webform_invalid_approval**, **zia_vision_validation**, **review_process_rejected**, **webform_unapproved**, **email_parser_waiting**, **approved**, **merge_pending**, **email_parser_rejected**, **zia_vision_rejected**, **zia_vision_pending**, **approval_process_rejected**, **webform_double_optin**.
- `criteria` (query, string, optional) [maxLen=3000]: Specify a criteria string to filter records using field-specific conditions and operators.
Performs a search using the following format:

`(({field_API_name}:{operator}:{value}) and/or ({field_API_name}:{operator}:{value}))`

Replace `{field_API_name}`, `{operator}`, and `{value}` with the
appropriate field API name, condition, and value.
-   You can search using a maximum of 10 criteria, with the same or
    different fields.
-   The only operator supported for encrypted fields is `equals`.

When using the `equals` operator in the Search API, it behaves like
`contains`, retrieving records that include the specified value.
For a single condition, if the condition is:

`(Company:equals:ABC)`

the response includes records with `ABC` as well as `ABC Inc.` in the
`Company` field.
For multiple conditions, `equals` continues to behave like `contains`.

**For example:**
`((Company:equals:ABC) and (First_Name:starts_with:M))`
This retrieves records where:

-   `First_Name` starts with `M`
-   `Company` contains `ABC` (for example, `ABC` or `ABC Inc.`)

** Note**: This behavior does not apply to picklist fields.

The `in` operator checks whether a field value matches any value in a given list.
**For example:**

`(Full_Name:in:Patricia,Boyle,Kate)`

This retrieves records where the `Full_Name` is `Patricia`, `Boyle`, or
`Kate`.

When a single-line field value contains characters such as:

`{ } [ ] ^ : - / ! ? * _ @` or spaces,

the Search API may return records with similar-looking values, even when
the characters are not an exact match.

For example:

-   Record A: `sales-team@zoho.com`
-   Record B: `sales_team@zoho.com`

A search using:

`equals:sales-team@zoho.com`

may return both records.

**Escaping Special Characters**

When using parentheses `(` `)`, commas `,`, or a backslash `\` as the
last character in a search value:

1.  Escape special characters using a backslash (`\`).
2.  Encode the value before making the API request.
3.  Select the value of the criteria, right-click the value, and choose
    the `EncodeURIComponent` option.

**Example 1: Escaping Parentheses and Commas**

Search term:

`((Last_Name:equals:Burns,B) and (First_Name:starts_with:M))`

Escape the comma:

`((Last_Name:equals:Burns\,B) and (First_Name:starts_with:M))`

Encode the value:

`((Last_Name:equals:Burns%5C%2CB) and (First_Name:starts_with:M))`

**Example 2: Escaping a Backslash at the End**

Search term:

`(Last_Name:equals:K\)`

Escape the backslash:

`(Last_Name:equals:K\\)`

Encode the value:

`(Last_Name:equals:K%5C%5C)`

**Supported Data Types**

-   `picklist`
-   `owner_lookup`
-   `user_lookup`
-   `lookup`
-   `phone`
-   `email`
-   `date`
-   `datetime`
-   `text`
-   `textarea`
-   `integer`
-   `currency`
-   `decimal`
-   `multiselectpicklist`
-   `bigint`
-   `percent`
-   `formula`
-   `website`
-   `boolean`
-   `double`

**Supported Operators**

-   `equals`
-   `starts_with`
-   `in`
-   `not_equal`
-   `greater_equal`
-   `greater_than`
-   `less_equal`
-   `less_than`
-   `between`

Refer to the following note for operator support by field type.
* **Date, DateTime:** `equals`, `not_equal`, `greater_equal`, `greater_than`, `less_equal`, `less_than`, `between`, `in`
* **Integer, Currency, Decimal:** `equals`, `not_equal`, `greater_equal`, `greater_than`, `less_equal`, `less_than`, `between`, `in`
* **Boolean:** `equals`, `not_equal`
* **textarea:** `equals`, `not_equal`, `starts_with`
* **Lookup (user/owner):** `equals`, `not_equal`, `in`
* **Picklist, Autonumber:** `equals`, `not_equal`, `in`
* **Text, Email, Phone, Website:** `equals`, `not_equal`, `starts_with`, `in`
* **multiselectpicklist:** `equals`, `not_equal`, `in`, `starts_with`
* **bigint:** `equals`, `not_equal`, `greater_than`, `greater_equal`, `less_than`, `less_equal`, `between`, `in`
* **percent:** `equals`, `not_equal`, `greater_than`, `greater_equal`, `less_than`, `less_equal`, `between`, `in`
* **formula:** Operators depend on the formula return type. Check the corresponding data type's supported operators.


- `converted` (query, string, optional) [maxLen=10, enum=['true', 'false', 'both'], default=false]: Specify whether to filter records by their conversion status. Applicable only for the Leads module.
Possible values:
**true** - Returns only converted leads.
**false** - Returns only unconverted leads.
**both** - Returns all leads regardless of conversion status.
Defaults to **false**.
- `word` (query, string, optional) [maxLen=100, minLen=2]: Specify the word or phrase to search for across all searchable text fields in the module. The value must be at least two characters long. Performs a global search with minimum 2 characters required. This is the broadest search method but may be slower than specific field searches.
*Mandatory if criteria, email, and phone are not present.*
- `email` (query, string/string, optional) [maxLen=255]: Specify the email address to search for across all email-type fields in the module. Partial matches are supported and searches multiple email fields simultaneously.  *Mandatory if criteria, phone, and word are not present.*
- `phone` (query, string, optional) [maxLen=50, minLen=3, pattern=^[+]?[0-9\s\-\(\)\.]+$]: Specify the phone number to search for across all phone-type fields in the module. The value must be at least three characters long and may include digits, spaces, hyphens, parentheses, and the plus sign. Supports various phone number formats including international, national, and partial numbers.
*Mandatory if criteria, email, and word are not present.*
- `fields` (query, string, optional) [maxLen=2000]: Specify a comma-separated list of field API names to include in the response. If omitted, the response includes all fields accessible to the current user.
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve for paginated results. The minimum value is 1. Defaults to 1.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of records to return per page. The minimum value is 1, the maximum is 200, and the default is 200.
- `sort_by` (query, string, optional) [maxLen=100, default=id]: Specify the API name of the field to sort the search results by.
- `sort_order` (query, string, optional) [maxLen=10, enum=['asc', 'desc'], default=desc]: Specify the direction in which to sort the results. Defaults to **desc**.
Possible values:
**asc** - Ascending order (A-Z, 1-9).
**desc** - Descending order (Z-A, 9-1).
- `type` (query, string, optional) [maxLen=50, enum=[16 values]]: Specify the user type to filter the search results by.
Possible values: **ActiveAndDeactive**, **CurrentUser**, **DeletedUsers**, **ParentRoleUsers**, **ChildRoleUsers**, **DeactiveUsers**, **NotConfirmedUsers**, **ConfirmedUsers**, **ActiveUsers**, **AdminUsers**, **ActiveConfirmedAdmins**, **ActiveConfirmedUsers**, **DeveloperUsers**, **SubordinateRoleUsers**, **AllUsers**, **AllActiveUsers**.

**Note**

- Only one of the mandatory parameters (`criteria`, `email`, `phone`, or `word`) can be used in a single request.
- If multiple parameters are provided, the API processes them in the following priority order:
   1. `criteria`
   2. `email`
   3. `phone`
   4. `word`
- Only the highest-priority parameter in the request is processed.

- The `page` and `per_page` parameters help retrieve records based on their position in Zoho CRM.
- A single API call can fetch a maximum of 200 records.
- To retrieve more records, adjust the `page` and `per_page` values.

   Example: To fetch 400 records:

   - First API call: `page=1&per_page=200` -> Fetches records 1-200
   - Second API call: `page=2&per_page=200` -> Fetches records 201-400

   By making two API calls, all 400 records can be retrieved.

- The Search API allows you to search for and retrieve a maximum of 2,000 records. If the search exceeds 2,000 records, the API returns a `LIMIT_REACHED` error.

- Values of fields containing sensitive health data are retrieved only when the **Restrict Data Access through API** option in the compliance settings is disabled. If the option is enabled, the field value is returned as `null`. Refer to [HIPAA compliance documentation](https://www.zoho.com/crm/developer/docs/api/v8/hipaa-compliance.html) for more details.

- When you create or edit a record and search for it immediately, you may receive a `204 NO CONTENT` response due to indexing delays. To fetch records without delay, use the [Query API](https://www.zoho.com/crm/developer/docs/api/v8/Get-Records-through-COQL-Query.html).
- The `in` operator supports up to 100 values.
- The `full_name` field contains the concatenated values of the `First Name` and `Last Name` fields.

- `full_name` is a read-only field available only in the `Leads`, `Contacts`, and `Users` modules.

To retrieve subform records that match your search criteria, use the API name of the corresponding subform module.

To retrieve multi-select lookup (MxN) records that match your search criteria, use the API name of the corresponding linking module.

**Schemas:**
`ErrorResponse`:
  > Represents the standard error response structure returned by the API, containing the error code, the message, and the response status.
  - `code` (string) **REQ** [enum=[14 values]] — Represents the error code for the response.
  - `details` (object) **REQ** — Represents additional details about the error, including information about the specific parameter or value that caused the issue.
  - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the reason for the failure.
  - `status` (string) **REQ** [enum=['error'], default=error] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.

**Responses:**

- **200**: Successful response containing the list of records matching the search criteria. [application/json]
    > Successful bulk search response containing matched records and pagination information
    - `data` (array of object) [maxItems=200] **REQ** — Array of records matching the search criteria
      - `id` (string) **REQ** [maxLen=50] — Unique identifier of the record
      - `Owner` (object) — Owner information of the record
        - `name` (string) [maxLen=255] — Name of the record owner
        - `id` (string) [maxLen=50] — Unique identifier of the owner
        - `email` (string/email) — Email address of the owner
      - `Created_Time` (string/date-time) — Timestamp when the record was created
      - `Modified_Time` (string/date-time) — Timestamp when the record was last modified
      - `Created_By` (object) — User who created the record
        - `name` (string) [maxLen=255] — Name of the user who created the record
        - `id` (string) **REQ** [maxLen=50] — Unique identifier of the user who created the record
        - `email` (string/email) — Email address of the user who created the record
      - `Modified_By` (object) — User who last modified the record
        - `name` (string) [maxLen=255] — Name of the user who last modified the record
        - `id` (string) [maxLen=50] — Unique identifier of the user who last modified the record
        - `email` (string/email) — Email address of the user who last modified the record
      additionalProperties: any
    - `info` (object) — Pagination and response metadata
      - `per_page` (integer/int32) — Number of records per page
      - `count` (integer/int32) — Number of records in current response
      - `page` (integer/int32) — Current page number
      - `more_records` (boolean) — Indicates if more records are available
      - `sort_by` (string) [maxLen=100] — Field used for sorting the records
      - `sort_order` (string) [enum=['asc', 'desc']] — Order of sorting the records

- **204**: No Content - The request was successful, but no records matched the search criteria. This may occur due to indexing delays when searching for recently created/modified records.

- **400**: Bad Request - The request could not be processed due to invalid input, missing mandatory parameters, or malformed search criteria. [application/json]
    oneOf:
      - `MissingRequiredParameterErrorResponse` — Missing required parameter error response
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['EXPECTED_PARAM_MISSING']] — Error code indicating missing parameters
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `details` (object) **REQ** — Additional error details including missing parameter names
          - `param_names` (array of string) [maxItems=4] **REQ** — List of missing parameter names
            items: [enum=['criteria', 'email', 'phone', 'word']]
      - `InvalidModuleErrorResponse` — Invalid module error response
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating invalid module
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `details` (object) **REQ** — Additional error details including resource path information
          - `resource_path_index` (integer/int32) **REQ** — Index of the invalid resource path segment

- **401**: Unauthorized - Authentication failed or insufficient OAuth scope permissions. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API, containing the error code, the message, and the response status.

- **403**: Forbidden - User lacks permission to access the requested module or perform the search operation. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API, containing the error code, the message, and the response status.

- **404**: Not Found - The requested URL pattern is invalid or the specified resource does not exist. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API, containing the error code, the message, and the response status.

- **429**: Too Many Requests - Rate limit exceeded. Wait before making additional requests. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API, containing the error code, the message, and the response status.

- **500**: Internal Server Error - An unexpected error occurred on the server. Contact support if the issue persists. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API, containing the error code, the message, and the response status.

- **502**: Bad Gateway - Temporary service dependency failure. The request should be retried. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API, containing the error code, the message, and the response status.

- **503**: Service Unavailable - The service is temporarily unavailable due to maintenance or capacity issues. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API, containing the error code, the message, and the response status.

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.Events.READ, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.Products.READ, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.Invoices.READ, ZohoCRM.modules.Forecasts.READ, ZohoCRM.modules.Activities.READ, ZohoCRM.modules.Notes.READ, ZohoCRM.modules.Attachments.READ, ZohoCRM.modules.custom.READ, ZohoCRM.users.READ, ZohoCRM.modules.READ, ZohoCRM.users.READ
