# GET /{moduleApiName}/actions/count
**Operation:** `getRecordCount` — Module Record Count
> To retrieve the total number of records in a specified Zoho CRM module, optionally filtered by a Custom View or search criteria. The count can be filtered using `cvid` (Custom View ID) or search parameters (`criteria`, `email`, `phone`, or `word`). These two filter groups are mutually exclusive - they cannot be combined in the same request. The `converted` and `approved` parameters apply only to the Leads module. The `type` parameter applies only to the Users module. Note: The record count may take 1-10 minutes to reflect the latest changes in Zoho CRM.

The count can be filtered using `cvid` (Custom View ID) or one of the search parameters (`criteria`, `phone`, `email`, `word`).

**Important Constraint (Zoho Documentation):**

You can only include **either** `cvid` **or** one of the search parameters (`criteria`, `phone`, `email`, `word`) in a single request. Combining `cvid` with any search parameter will result in an `AMBIGUITY_DURING_PROCESSING` error (HTTP 400).

**Tags:** Records

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=5000]: Specify the API name of the module for which you want to retrieve the record count. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `email` (query, string, optional) [maxLen=3000]: Specify an email address to filter the count to records that contain this value in any email field of the specified module. Encode special characters before submitting (for example, use `p%2Bboyle@abc.com` for `p+boyle@abc.com`).
- `phone` (query, string, optional) [maxLen=3000]: Specify a phone number to filter the count to records that contain this value in any phone field of the specified module.
- `word` (query, string, optional) [maxLen=3000]: Specify a search term to filter the count to records that contain this word in any searchable field within the specified module.
- `cvid` (query, string, optional) [maxLen=3000]: Specify the ID of the Custom View from which to retrieve the record count. Refer to the [Get Custom Views](custom_views.yaml#$.paths./settings/custom_views.get) resource for valid values.
- `criteria` (query, string, optional) [maxLen=3000]: Performs search by following the shown criteria: `(({api_name}:{operator}:{value}) and/or ({api_name}:{operator}:{value}))`

Performs a search based on the following format:
`(({field_API_name}:{operator}:{value}) and/or ({field_API_name}:{operator}:{value}))`

Replace `{field_API_name}`, `{operator}`, and `{value}` with the appropriate field API name, condition, and value.

**Key Points:**
- You can search for a maximum of **10 criteria** (with same or different columns)
- The only operator that is supported for **encrypted fields** is `equals`
- When using the `equals` operator in the Search API, it behaves like `contains`, retrieving records that include the specified value

**Single Condition:**
If the condition is `(Company:equals:ABC)`, the response will include records with "ABC" as well as "ABC Inc" in the Company field.

**Multiple Conditions:**
`equals` still behaves like `contains`. For example, `((Company:equals:ABC) and (First_Name:starts_with:M))`, it retrieves records where the "First Name" starts with "M" and the "Company" contains "ABC" (e.g., "ABC" or "ABC Inc.").

**Note:** The above behaviour does not apply to the **picklist field type**.

**IN Operator:**
The `in` operator checks if a field's value matches any value in a given list.
For example, `(Full_Name:in:Patricia,Boyle,Kate)`, it retrieves records where the Full Name is Patricia, Boyle, or Kate.

**Special Character Handling:**
When a single-line field value contains characters such as `{`, `}`, `[`, `]`, `^`, `:`, `-`, `/`, `!`, `?`, `*`, `_`, `@`, space, the Search API returns records with similar-looking values, even if the characters are not an exact match.

For example, if Record A has the field value `sales-team@zoho.com` and Record B has `sales_team@zoho.com`, a search using `equals:sales-team@zoho.com` may return both records.

**Escaping Special Characters:**
When using parentheses `()`, commas `,`, or a backslash `\` as the last character in a search value, follow these steps:
1. Escape special characters using a backslash `\`
2. Encode the value before making the API request. Select the value of the criteria, right-click the value, and choose the EncodeURIComponent option.

**Example 1: Escaping Parentheses and Commas**
- Search term: `((Last_Name:equals:Burns,B) and (First_Name:starts_with:M))`
- Escape the comma `\,`: `((Last_Name:equals:Burns\,B) and (First_Name:starts_with:M))`
- Encode the value: `((Last_Name:equals:Burns%5C%2CB) and (First_Name:starts_with:M))`

**Example 2: Escaping a Backslash at the End**
- Search term: `(Last_Name:equals:K\)`
- Escape the backslash `\\`: `(Last_Name:equals:K\\)`
- Encode the value: `(Last_Name:equals:K%5C%5C)`

**Supported Data Types:**
`picklist`, `owner_lookup`, `user_lookup`, `lookup`, `phone`, `email`, `date`, `datetime`, `text`, `textarea`, `integer`, `currency`, `decimal`, `multiselectpicklist`, `bigint`, `percent`, `formula`, `website`, `boolean`, `double`

**Supported Operators:**
`equals`, `starts_with`, `in`, `not_equal`, `greater_equal`, `greater_than`, `less_equal`, `less_than`, `between`

**Operator Compatibility by Data Type:**

| Data Type | equals | starts_with | in | not_equal | greater_equal | greater_than | less_equal | less_than | between |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **text** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **textarea** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **email** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **phone** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **website** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **picklist** | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **multiselectpicklist** | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **lookup** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **owner_lookup** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **user_lookup** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **boolean** | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **integer** | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **bigint** | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **currency** | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **decimal** | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **double** | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **percent** | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **date** | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **datetime** | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **formula** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Legend:** ✓ = Supported, ✗ = Not Supported

**Note:** Refer to the Zoho CRM API documentation for the most up-to-date operator compatibility information.
- `filters` (query, object, optional): Filter for fetching specific custom views based on criteria
- `include_filters` (query, string, optional) [maxLen=50]: To include inner details of criteria and cross filters
- `cross_filters` (query, string, optional) [maxLen=3000]: Cross filter criteria for related module records
- `converted` (query, string, optional) [enum=['true', 'false', 'both']]: Specify the conversion status to filter the count to lead records. This parameter is supported only for the **Leads** module. Possible values:
**true** - Count only converted leads.
**false** - Count only unconverted leads.
**both** - Count leads regardless of conversion status.
- `approved` (query, string, optional) [enum=['true', 'false', 'both']]: Specify the approval status to filter the count to lead records. This parameter is supported only for the **Leads** module. Possible values:
**true** - Count only approved leads.
**false** - Count only unapproved leads.
**both** - Count leads regardless of approval status.
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve when paginating through results.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of records to include per page.
- `type` (query, string, optional) [enum=[11 values]]: Specify the type of user records to count. This parameter is supported only for the **Users** module. Possible values:
**AllUsers** - All users.
**ActiveUsers** - Active users.
**DeactiveUsers** - Deactivated users.
**ConfirmedUsers** - Confirmed users.
**ConfirmedReportingUsers** - Confirmed users with reporting access.
**NotConfirmedUsers** - Unconfirmed users.
**DeletedUsers** - Deleted users.
**ActiveConfirmedUsers** - Active and confirmed users.
**AdminUsers** - Users with administrator privileges.
**ActiveConfirmedAdmins** - Active, confirmed users with administrator privileges.
**CurrentUser** - The currently authenticated user.

**Schemas:**
`ErrorResponse`:
  > Represents a standard error response returned by the Zoho CRM API when a request fails.
  - `code` (string) [maxLen=64] — Represents the unique error code that identifies the type of failure.
  - `message` (string) [maxLen=512] — Represents the error message describing the reason for the failure.
  - `details` (object) — Represents additional details about the error, which may include the field API name or parameter name associated with the failure.
  - `status` (string) [enum=['error']] — Indicates the response status. Possible values:
**error** - The request resulted in an error.

**Responses:**

- **200**: Successful response containing the total record count. [application/json]
    > Represents the response body containing the total number of records matching the specified filter criteria.
    - `count` (integer/int32) **REQ** — Represents the total number of records matching the specified filter criteria. Always returned in the response.

- **400**: Bad Request - invalid module name, unsupported module, or ambiguous use of parameters. [application/json]
    > Represents the union of possible error response bodies returned for a 400 Bad Request.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Error code indicating invalid request
        - `message` (string) **REQ** [maxLen=1000, const=unable to process your request. please verify whether you have entered proper method name, parameter and parameter values.] — Human-readable error message
        - `details` (object) — Additional error details
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['FIELD_TYPE_UNAVAILABLE']] — Error code indicating invalid request
        - `message` (string) **REQ** [maxLen=1000, enum=['this data type is not found in this module']] — Human-readable error message
        - `details` (object) — Additional error details
        - `status` (string) **REQ** [const=error] — Error status indicator
        - `code` (string) **REQ** [const=NOT_SUPPORTED] — Error code indicating unsupported operation
        - `message` (string) **REQ** [maxLen=1000, enum=[3 values]] — Human-readable error message
        - `details` (object) **REQ** — Additional error details including module information
          - `module` (string) [maxLen=100] — The module that does not support this operation
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['EXPECTED_PARAM_MISSING']] — Error code indicating missing parameters
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `details` (object) **REQ** — Additional error details including missing parameter names
          - `param_names` (array of string) [maxItems=50] **REQ** — List of missing parameter names
            items: [maxLen=100, enum=['criteria', 'email', 'phone', 'word']]
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating invalid module
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `details` (object) **REQ** — Additional error details including resource path information
          - `resource_path_index` (integer/int32) — Index of the invalid resource path segment
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_QUERY']] — Error code indicating invalid query
        - `message` (string) **REQ** [enum=[9 values]] — Human-readable error message describing the query issue
        - `details` (object) **REQ**
          oneOf:
              - `operator` (string) **REQ** [maxLen=50] — The invalid operator used in the query
              - `expected_data_type` (string) **REQ** [maxLen=100] — The expected data type for the field
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `expected_data_type` (string) **REQ** [maxLen=100] — The expected data type for the field
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `value` (string) **REQ** [maxLen=500] — The invalid value provided in the query
              - `operator` (string) **REQ** [maxLen=50] — The invalid operator used in the query
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `details` (string) [maxLen=1000] — Additional details about the error, only Zoho Search team
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `value` (string) **REQ** [maxLen=500] — The invalid value provided in the query
              - `param_name` (string) **REQ** [maxLen=500, enum=['email', 'phone', 'word']] — Name of the parameter causing the error
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid query
        - `message` (string) **REQ** [enum=[11 values]] — Human-readable error message describing the query issue
        - `details` (object) **REQ**
          oneOf:
              - `expected_data_type` (string) **REQ** [maxLen=100] — The expected data type for the field
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `operator` (string) **REQ** [maxLen=50] — The invalid operator used in the query
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `details` (string) [maxLen=1000] — Additional details about the error, only Zoho Search team
              - `reason` (string) **REQ** [maxLen=500] — Detailed reason for the error
              - `value` (string) **REQ** [maxLen=500] — The invalid value provided in the query
              - `param_name` (string) **REQ** [maxLen=500] — Name of the parameter causing the error
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_QUERY']] — Error code indicating invalid query
        - `message` (string) **REQ** [enum=['Only 100 values are allowed in "IN" criteria', 'Invalid query formed']] — Human-readable error message describing the query issue
        - `details` (object) **REQ** — Additional error details including field information
          - `param_name` (string) [maxLen=100] — Name of the parameter causing the error
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['LIMIT_REACHED']] — Error code indicating limit reached
        - `message` (string) **REQ** [enum=['maximum response iteration limit reached']] — Human-readable error message
        - `details` (object) **REQ** — Additional error details including the limit value
          - `limit` (string) **REQ** [enum=['2000']] — Maximum number of records allowed
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['CRITERIA_LIMIT_EXCEEDED']] — Error code indicating criteria limit exceeded
        - `message` (string) **REQ** [enum=['no of criterium that can be given exceed the limit 15']] — Human-readable error message
        - `details` (object) **REQ** — Additional error details
        - `status` (string) [enum=['error']] — Indicates the response is an error.
        - `code` (string) [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code representing ambiguity during request processing.
        - `message` (string) [maxLen=512, enum=[1 values]] — Detailed message describing the ambiguity in the request.
        - `details` (object) — Additional details about the ambiguity.
          - `ambiguity_due_to` (array of object) [maxItems=2] — List of parameters causing ambiguity.
            - `param_name` (string) **REQ** [maxLen=100] — Name of the parameter causing ambiguity.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response is an error.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Error code representing unsupported operation or module.
        - `message` (string) **REQ** [maxLen=512, enum=['api not supported in this version']] — Detailed message describing why the request is not supported.
        - `details` (object) — Additional details including the unsupported module name.
          - `supported_version` (string) [maxLen=100, enum=['v2.1']] — The API version that supports this operation.

- **401**: Unauthorized (e.g., OAUTH_SCOPE_MISMATCH). — Schema: `ErrorResponse` [application/json]
    > Represents a standard error response returned by the Zoho CRM API when a request fails.

- **500**: Internal Server Error — Schema: `ErrorResponse` [application/json]
    > Represents a standard error response returned by the Zoho CRM API when a request fails.

**Scopes:** ZohoCRM.modules.READ, ZohoCRM.modules.Leads.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.Events.READ, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.Products.READ, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.pricebooks.READ, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.salesorders.READ, ZohoCRM.modules.purchaseorders.READ
