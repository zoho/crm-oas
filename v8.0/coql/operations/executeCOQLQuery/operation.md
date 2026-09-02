# POST /coql
**Operation:** `executeCOQLQuery` — Retrieve records using a COQL query
> To retrieve records from one or more Zoho CRM modules using a COQL SELECT query, with support for cross-module joins, aggregate functions, and flexible filtering.

**Request Body** (required) — application/json
> The request body must contain a **select_query** field with a valid COQL SELECT statement.
  > Represents the request body for the COQL query execution.
  - `select_query` (string) **REQ** [maxLen=2147483647] — Specify the COQL SELECT query to retrieve records. The query must reference module and field API names.
  - `include_meta` (array of string) [minItems=1, maxItems=1] — Specify the list of metadata types to include in the response.
Possible values:
**fields** - Includes field metadata for the SELECT columns in the response.
    items: [enum=['fields']]

**Responses:**

- **200**: Returns the matching records for the COQL query, along with pagination details. [application/json]
    > Represents the response body for a successful COQL query, containing the matching records and pagination metadata.
    - `data` (array of object) [minItems=1, maxItems=200] **REQ** — Represents the list of records returned by the COQL query. Always returned in the response.
    - `info` (object) **REQ** — Represents the pagination metadata for the query result. Always returned in the response.
      - `count` (integer/int32) **REQ** — Represents the number of records returned in the current response. Always returned in the response.
      - `more_records` (boolean) **REQ** — Indicates whether additional records matching the query are available beyond the current page. Always returned in the response.
Possible values:
**true** - More records are available. Use LIMIT and OFFSET to paginate.
**false** - All matching records are included in this response.
    - `fields` (object) — Represents the field metadata for each column specified in the SELECT clause. Keys are field API names and values are field configuration objects. Returned only when **fields** is specified in the **include_meta** request body parameter.

- **204**: Indicates that the COQL query executed successfully but returned no matching records.

- **400**: The COQL query is invalid, contains syntax errors, or references unsupported data. Resolution: Ensure the query uses valid module and field API names, supported operators, and correct COQL syntax. [application/json]
    > Represents one of the possible 400 error responses for the COQL query, each corresponding to a specific error condition.
    oneOf:
        title: SyntaxError
        - `code` (string) **REQ** [enum=['SYNTAX_ERROR']] — Represents the error code for a syntax error in the COQL query. Always returned in the response.
Possible values:
**SYNTAX_ERROR** - A syntax error was detected in the COQL query.
        - `details` (object) **REQ** — Represents the details of the syntax error, including the location or context of the error.
          oneOf:
              - `clause` (string) **REQ** [maxLen=1000] — Represents the COQL clause where the syntax error occurred.
              - `line` (integer/int32) **REQ** — Represents the line number in the query where the syntax error occurred.
              - `column` (integer/int32) **REQ** — Represents the column number in the query where the syntax error occurred.
              - `near` (string) **REQ** [maxLen=1000] — Represents the text fragment near the syntax error location.
              - `operator` (string) **REQ** [maxLen=100] — Represents the unsupported operator used in the COQL query.
              - `near` (string) **REQ** [maxLen=1000] — Represents the text fragment near the syntax error in the query.
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the syntax error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.
        title: LimitExceeded
        - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code for a limit exceeded error. Always returned in the response.
Possible values:
**LIMIT_EXCEEDED** - The query exceeds the permitted limit.
        - `details` (object) **REQ** — Represents additional details about the limit exceeded error.
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the limit exceeded error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.
        title: InvalidQuery
        - `code` (string) **REQ** [enum=['INVALID_QUERY']] — Represents the error code for an invalid query error. Always returned in the response.
Possible values:
**INVALID_QUERY** - The COQL query is structurally invalid.
        - `details` (object) **REQ** — Represents the details of the invalid query error, including the column, module, alias, operator, or criteria involved.
          oneOf:
              - `column_name` (string) **REQ** [maxLen=150] — Represents the API name of the field with an invalid column reference.
              - `limit` (string) **REQ** [maxLen=150] — Represents the maximum allowed limit for the column in the COQL query, if applicable.
              - `offset` (string) **REQ** [maxLen=150] — The invalid offset value used in the query
              - `column_name` (string) **REQ** [maxLen=150] — Represents the API name of the field with invalid data in the query.
              - `clause` (string) **REQ** [maxLen=150] — Represents the COQL clause associated with the invalid column.
              - `module` (string) **REQ** [maxLen=150] — Represents the API name of the module referenced in an invalid module context.
              - `cvid` (string) **REQ** [maxLen=150] — Represents the invalid Custom View ID referenced in the COQL query.
              - `reason` (string) **REQ** [maxLen=1000] — Represents a description of the reason the operator is invalid for the column.
              - `column_name` (string) **REQ** [maxLen=500] — Represents the API name of the column involved in the invalid operator error.
              - `operator` (string) **REQ** [enum=['>', '<', '>=', '<=', '=', '!=', 'is null', 'is not null']] — Represents the operator that is invalid for the specified column in the COQL query.
Possible values:
**>** - Greater than.
**<** - Less than.
**>=** - Greater than or equal to.
**<=** - Less than or equal to.
**=** - Equal to.
**!=** - Not equal to.
**is null** - Checks if the value is null.
**is not null** - Checks if the value is not null.
              - `column_name` (string) **REQ** [maxLen=150] — Represents the API name of the column with an invalid alias.
              - `alias` (string) **REQ** [maxLen=1000] — Represents the invalid alias name used in the COQL query.
              - `cv_criteria` (boolean) **REQ** — Indicates whether the invalid query involves Custom View criteria.
Possible values:
**true** - Custom View criteria are involved in the error.
**false** - Custom View criteria are not involved.
              - `column_name` (string) **REQ** [maxLen=150] — Represents the API name of the field with invalid criteria in the query.
              - `value` (string) **REQ** [maxLen=500] — Represents the value used in the unsupported criteria that caused the error.
              - `operator` (string) **REQ** [enum=[13 values]] — Represents the operator used in the unsupported criteria.
Possible values:
**=** - Equal to.
**!=** - Not equal to.
**>** - Greater than.
**<** - Less than.
**>=** - Greater than or equal to.
**<=** - Less than or equal to.
**like** - Matches a pattern.
**not like** - Does not match a pattern.
**in** - Matches any value in a list.
**not in** - Does not match any value in a list.
**between** - Matches values within a range.
**is null** - Checks if the value is null.
**is not null** - Checks if the value is not null.
              - `sub_query_sequence` (integer/int32) **REQ** — Represents the sequence number of the subquery that returned incompatible values.
              - `operator` (string) **REQ** [enum=['=', '!=', '>', '<', '>=', '<=']] — Represents the operator that is incompatible with subqueries that return multiple values.
Possible values:
**=** - Equal to.
**!=** - Not equal to.
**>** - Greater than.
**<** - Less than.
**>=** - Greater than or equal to.
**<=** - Less than or equal to.
              - `sub_query_sequence` (integer/int32) **REQ** — Represents the sequence number of the subquery in the COQL query.
              - `column_name` (array of string) [minItems=2, maxItems=500] **REQ** — Represents the list of columns specified in the subquery that caused the error.
                items: [maxLen=150]
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the invalid query error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.
        title: InvalidAlias
        - `code` (string) **REQ** [enum=['INVALID_ALIAS']] — Represents the error code for an invalid alias error. Always returned in the response.
Possible values:
**INVALID_ALIAS** - A column alias in the query is invalid.
        - `details` (object) **REQ** — Represents the details of the invalid alias error.
          - `alias` (string) [enum=['']] — Represents the invalid alias name used in the COQL query.
          - `column_name` (string) [maxLen=150] — Represents the API name of the column with the invalid alias.
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the invalid alias error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.
        title: DuplicateData
        - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for a duplicate data error. Always returned in the response.
Possible values:
**DUPLICATE_DATA** - A column or aggregate function is duplicated in the SELECT clause.
        - `details` (object) **REQ** — Represents the details of the duplicate data error, including the field API name or aggregate function that is duplicated.
          oneOf:
              - `column_name` (string) **REQ** [maxLen=150] — Represents the API name of the field that is duplicated in the SELECT clause.
              - `column_name` (string) **REQ** [maxLen=150] — Represents the API name of the field on which the aggregate function is duplicated.
              - `aggregate` (string) **REQ** [enum=['MAX', 'MIN', 'AVG', 'SUM', 'COUNT']] — Represents the duplicate aggregate function used on the same column.
Possible values:
**MAX** - Maximum value.
**MIN** - Minimum value.
**AVG** - Average value.
**SUM** - Sum of values.
**COUNT** - Count of records.
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the duplicate data error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.
        title: DuplicateAlias
        - `code` (string) **REQ** [enum=['DUPLICATE_ALIAS']] — Represents the error code for a duplicate alias error. Always returned in the response.
Possible values:
**DUPLICATE_ALIAS** - An alias in the SELECT clause appears more than once.
        - `details` (object) **REQ** — Represents the details of the duplicate alias error, including the alias and the columns using it.
          - `alias` (string) [maxLen=150] — Represents the alias that appears more than once in the SELECT clause.
          - `referred_columns` (array of string) [minItems=2, maxItems=500] — Represents the list of SELECT columns that use the duplicate alias.
            items: [maxLen=150]
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the duplicate alias error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.
        title: MandatoryNotFound
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for a missing mandatory field error. Always returned in the response.
Possible values:
**MANDATORY_NOT_FOUND** - A mandatory field was not found in the request.
        - `details` (object) **REQ** — Represents the details of the missing mandatory field error.
          - `api_name` (string) **REQ** [maxLen=500] — Represents the API name of the mandatory field that is missing from the request.
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the missing mandatory field. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.
        title: InvalidData
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for an invalid data error. Always returned in the response.
Possible values:
**INVALID_DATA** - The request contains invalid data for one or more fields.
        - `details` (object) **REQ** — Represents the details of the invalid data error, including the affected field and the expected data type.
          oneOf:
              - `expected_data_type` (string) **REQ** [maxLen=100] — Represents the expected data type for the field.
              - `api_name` (string) **REQ** [maxLen=500] — Represents the API name of the field with invalid data.
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field with invalid data.
              - `api_name` (string) **REQ** [maxLen=500] — Represents the API name of the field with invalid data.
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field with invalid data.
              - `supported_values` (array of string) [maxItems=1] **REQ** — Represents the list of supported values for the field.
                items: [enum=['fields']]
              - `reason` (string) **REQ** [maxLen=500] — Represents the reason why the data is invalid.
              - `column` (string) **REQ** [maxLen=500] — Represents the API name of the column using an unsupported aggregate function.
              - `expected_data_type` (string) **REQ** [maxLen=100] — Represents the expected data type for the field.
              - `api_name` (string) **REQ** [maxLen=500] — Represents the API name of the field with invalid data.
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field with invalid data.
              - `supported_values` (array of string) [maxItems=1] **REQ** — Represents the list of supported values for the field.
                items: [enum=['fields']]
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the invalid data error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.
        title: InvalidModule
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for an invalid module error. Always returned in the response.
Possible values:
**INVALID_MODULE** - The module specified in the COQL query does not exist or is inaccessible.
        - `details` (object) **REQ** — Represents the details of the invalid module error.
        - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the invalid module error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always returned in the response.
Possible values:
**error** - The request failed due to an error.

**Scopes:** ZohoCRM.modules.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Leads.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Accounts.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Deals.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Tasks.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Events.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Calls.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Products.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Vendors.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Campaigns.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Cases.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Solutions.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Quotes.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Salesorders.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.coql.READ, ZohoCRM.modules.Custom.READ, ZohoCRM.coql.READ, ZohoCRM.modules.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Leads.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Accounts.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Deals.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Tasks.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Events.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Calls.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Products.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Vendors.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Campaigns.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Cases.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Solutions.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Quotes.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Salesorders.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ, ZohoCRM.modules.Custom.READ, ZohoCRM.coql.READ, ZohoCRM.settings.fields.READ
