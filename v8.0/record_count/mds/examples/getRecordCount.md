# Examples: getRecordCount

**GET /{moduleApiName}/actions/count**

## Parameter examples

### `moduleApiName` (path) — Leads

```json
"Leads"
```

### `moduleApiName` (path) — Accounts

```json
"Accounts"
```

### `email` (query) — Example

```json
"p%2Bboyle@abc.com"
```

### `phone` (query) — Example

```json
"9876543210"
```

### `word` (query) — Example

```json
"fin"
```

### `cvid` (query) — Example

```json
"5690xxxx980"
```

### `criteria` (query) — SimpleEquals

Simple equals search (text field)

```json
"(Last_Name:equals:Smith)"
```

### `criteria` (query) — TextStartsWith

Text field with starts_with operator

```json
"(Company:starts_with:Zoho)"
```

### `criteria` (query) — TextNotEqual

Text field with not_equal operator

```json
"(Department:not_equal:Sales)"
```

### `criteria` (query) — TextInOperator

Text field with IN operator

```json
"(Last_Name:in:Smith,Johnson,Williams)"
```

### `criteria` (query) — EmailEquals

Email field with equals operator

```json
"(Email:equals:john@example.com)"
```

### `criteria` (query) — EmailStartsWith

Email field with starts_with operator

```json
"(Email:starts_with:admin)"
```

### `criteria` (query) — PhoneEquals

Phone field with equals operator

```json
"(Phone:equals:9876543210)"
```

### `criteria` (query) — PhoneIn

Phone field with IN operator

```json
"(Mobile:in:9876543210,9876543211,9876543212)"
```

### `criteria` (query) — WebsiteEquals

Website field with equals operator

```json
"(Website:equals:zoho.com)"
```

### `criteria` (query) — WebsiteStartsWith

Website field with starts_with operator

```json
"(Website:starts_with:https)"
```

### `criteria` (query) — TextareaEquals

Textarea field with equals operator

```json
"(Description:equals:Project)"
```

### `criteria` (query) — TextareaStartsWith

Textarea field with starts_with operator

```json
"(Notes:starts_with:Important)"
```

### `criteria` (query) — TextareaNotEqual

Textarea field with not_equal operator

```json
"(Comments:not_equal:Closed)"
```

### `criteria` (query) — IntegerEquals

Integer field with equals operator

```json
"(No_of_Employees:equals:100)"
```

### `criteria` (query) — IntegerGreaterThan

Integer field with greater_than operator

```json
"(No_of_Employees:greater_than:50)"
```

### `criteria` (query) — IntegerGreaterEqual

Integer field with greater_equal operator

```json
"(No_of_Employees:greater_equal:100)"
```

### `criteria` (query) — IntegerLessThan

Integer field with less_than operator

```json
"(No_of_Employees:less_than:500)"
```

### `criteria` (query) — IntegerLessEqual

Integer field with less_equal operator

```json
"(No_of_Employees:less_equal:1000)"
```

### `criteria` (query) — IntegerBetween

Integer field with between operator

```json
"(No_of_Employees:between:100,500)"
```

### `criteria` (query) — IntegerIn

Integer field with IN operator

```json
"(No_of_Employees:in:50,100,200,500)"
```

### `criteria` (query) — IntegerNotEqual

Integer field with not_equal operator

```json
"(No_of_Employees:not_equal:0)"
```

### `criteria` (query) — CurrencyEquals

Currency field with equals operator

```json
"(Annual_Revenue:equals:1000000)"
```

### `criteria` (query) — CurrencyGreaterThan

Currency field with greater_than operator

```json
"(Annual_Revenue:greater_than:500000)"
```

### `criteria` (query) — CurrencyBetween

Currency field with between operator

```json
"(Annual_Revenue:between:100000,1000000)"
```

### `criteria` (query) — CurrencyIn

Currency field with IN operator

```json
"(Annual_Revenue:in:100000,500000,1000000)"
```

### `criteria` (query) — DecimalEquals

Decimal field with equals operator

```json
"(Exchange_Rate:equals:1.25)"
```

### `criteria` (query) — DecimalGreaterEqual

Decimal field with greater_equal operator

```json
"(Exchange_Rate:greater_equal:1.0)"
```

### `criteria` (query) — DecimalBetween

Decimal field with between operator

```json
"(Exchange_Rate:between:1.0,1.5)"
```

### `criteria` (query) — BigIntEquals

BigInt field with equals operator

```json
"(Record_ID:equals:9876543210123)"
```

### `criteria` (query) — BigIntGreaterThan

BigInt field with greater_than operator

```json
"(Record_ID:greater_than:1000000000000)"
```

### `criteria` (query) — BigIntBetween

BigInt field with between operator

```json
"(Record_ID:between:1000000000000,9999999999999)"
```

### `criteria` (query) — BigIntIn

BigInt field with IN operator

```json
"(Record_ID:in:1234567890123,9876543210123)"
```

### `criteria` (query) — PercentEquals

Percent field with equals operator

```json
"(Discount:equals:10)"
```

### `criteria` (query) — PercentGreaterThan

Percent field with greater_than operator

```json
"(Discount:greater_than:5)"
```

### `criteria` (query) — PercentBetween

Percent field with between operator

```json
"(Discount:between:5,20)"
```

### `criteria` (query) — PercentLessEqual

Percent field with less_equal operator

```json
"(Discount:less_equal:15)"
```

### `criteria` (query) — DateEquals

Date field with equals operator

```json
"(Closing_Date:equals:2024-12-31)"
```

### `criteria` (query) — DateGreaterThan

Date field with greater_than operator

```json
"(Closing_Date:greater_than:2024-01-01)"
```

### `criteria` (query) — DateBetween

Date field with between operator

```json
"(Closing_Date:between:2024-01-01,2024-12-31)"
```

### `criteria` (query) — DateLessThan

Date field with less_than operator

```json
"(Closing_Date:less_than:2024-06-30)"
```

### `criteria` (query) — DateIn

Date field with IN operator

```json
"(Closing_Date:in:2024-01-15,2024-03-15,2024-06-15)"
```

### `criteria` (query) — DateNotEqual

Date field with not_equal operator

```json
"(Closing_Date:not_equal:2024-12-31)"
```

### `criteria` (query) — DateTimeEquals

DateTime field with equals operator

```json
"(Created_Time:equals:2024-12-18T10:30:00+05:30)"
```

### `criteria` (query) — DateTimeGreaterEqual

DateTime field with greater_equal operator

```json
"(Modified_Time:greater_equal:2024-01-01T00:00:00+00:00)"
```

### `criteria` (query) — DateTimeBetween

DateTime field with between operator

```json
"(Created_Time:between:2024-01-01T00:00:00+00:00,2024-12-31T23:59:59+00:00)"
```

### `criteria` (query) — DateTimeLessEqual

DateTime field with less_equal operator

```json
"(Modified_Time:less_equal:2024-06-30T23:59:59+05:30)"
```

### `criteria` (query) — BooleanEquals

Boolean field with equals operator

```json
"(Email_Opt_Out:equals:true)"
```

### `criteria` (query) — BooleanNotEqual

Boolean field with not_equal operator

```json
"(Email_Opt_Out:not_equal:true)"
```

### `criteria` (query) — PicklistEquals

Picklist field with equals operator

```json
"(Lead_Status:equals:Qualified)"
```

### `criteria` (query) — PicklistNotEqual

Picklist field with not_equal operator

```json
"(Lead_Status:not_equal:Converted)"
```

### `criteria` (query) — PicklistIn

Picklist field with IN operator

```json
"(Lead_Status:in:Qualified,Contacted,Working)"
```

### `criteria` (query) — MultiselectPicklistEquals

Multiselectpicklist field with equals operator

```json
"(Interested_Products:equals:CRM)"
```

### `criteria` (query) — MultiselectPicklistStartsWith

Multiselectpicklist field with starts_with operator

```json
"(Tags:starts_with:Priority)"
```

### `criteria` (query) — MultiselectPicklistIn

Multiselectpicklist field with IN operator

```json
"(Interested_Products:in:CRM,Marketing,Sales)"
```

### `criteria` (query) — MultiselectPicklistNotEqual

Multiselectpicklist field with not_equal operator

```json
"(Tags:not_equal:Archived)"
```

### `criteria` (query) — LookupEquals

Lookup field with equals operator

```json
"(Account_Name:equals:Zoho Corporation)"
```

### `criteria` (query) — LookupIn

Lookup field with IN operator

```json
"(Account_Name:in:Zoho Corporation,ABC Inc,XYZ Ltd)"
```

### `criteria` (query) — LookupNotEqual

Lookup field with not_equal operator

```json
"(Account_Name:not_equal:Test Account)"
```

### `criteria` (query) — OwnerEquals

Owner lookup field with equals operator

```json
"(Owner:equals:John Doe)"
```

### `criteria` (query) — OwnerIn

Owner lookup field with IN operator

```json
"(Owner:in:John Doe,Jane Smith,Bob Johnson)"
```

### `criteria` (query) — AutonumberEquals

Autonumber field with equals operator

```json
"(Lead_Number:equals:LEAD-10001)"
```

### `criteria` (query) — AutonumberIn

Autonumber field with IN operator

```json
"(Lead_Number:in:LEAD-10001,LEAD-10002,LEAD-10003)"
```

### `criteria` (query) — MultipleConditionsAnd

Multiple conditions with AND logic

```json
"((Company:equals:Zoho) and (Annual_Revenue:greater_than:1000000))"
```

### `criteria` (query) — MultipleConditionsOr

Multiple conditions with OR logic

```json
"((Lead_Status:equals:Qualified) or (Lead_Status:equals:Contacted))"
```

### `criteria` (query) — ComplexNestedConditions

Complex nested conditions with AND/OR

```json
"(((Company:equals:Zoho) and (Annual_Revenue:greater_than:1000000)) or ((Lead_Status:equals:Hot) and (No_of_Employees:greater_than:100)))"
```

### `criteria` (query) — ThreeConditionsAnd

Three conditions with AND

```json
"(((Lead_Status:equals:Qualified) and (Annual_Revenue:greater_than:500000)) and (No_of_Employees:greater_than:50))"
```

### `criteria` (query) — MixedFieldTypes

Mixed field types with AND/OR

```json
"(((Closing_Date:between:2024-01-01,2024-12-31) and (Deal_Amount:greater_than:50000)) or (Priority:equals:High))"
```

### `criteria` (query) — DateRangeCurrentYear

Date range for current year

```json
"(Created_Time:between:2024-01-01,2024-12-31)"
```

### `criteria` (query) — NumericRange

Numeric range with multiple conditions

```json
"((Annual_Revenue:between:100000,1000000) and (No_of_Employees:between:10,500))"
```

### `criteria` (query) — NegativeConditions

Multiple NOT EQUAL conditions

```json
"((Lead_Status:not_equal:Junk) and (Lead_Status:not_equal:Lost))"
```

### `criteria` (query) — MaximumCriteria

Maximum 10 criteria example

```json
"(((Lead_Status:equals:Qualified) and (Annual_Revenue:greater_than:100000)) and ((No_of_Employees:greater_than:10) and (Industry:equals:Technology)) and ((Rating:equals:Hot) and (Email_Opt_Out:equals:false)) and ((Created_Time:greater_than:2024-01-01) and (Lead_Source:equals:Web)) and ((Country:equals:USA) and (State:equals:California)))"
```

### `criteria` (query) — MultipleAnd

Multiple conditions with AND

```json
"((Company:equals:ABC) and (First_Name:starts_with:M))"
```

### `criteria` (query) — MultipleOr

Multiple conditions with OR

```json
"((Last_Name:equals:Smith) or (Last_Name:equals:Johnson))"
```

### `criteria` (query) — InOperator

IN operator for multiple values

```json
"(Full_Name:in:Patricia,Boyle,Kate)"
```

### `criteria` (query) — EscapedComma

Escaped comma in value

```json
"((Last_Name:equals:Burns%5C%2CB) and (First_Name:starts_with:M))"
```

### `criteria` (query) — EscapedBackslash

Escaped backslash at end

```json
"(Last_Name:equals:K%5C%5C)"
```

### `criteria` (query) — Between

Between operator for date range

```json
"(Created_Time:between:2024-01-01,2024-12-31)"
```

### `criteria` (query) — GreaterThan

Greater than operator

```json
"(Annual_Revenue:greater_than:1000000)"
```

### `criteria` (query) — NotEqual

Not equal operator

```json
"(Lead_Status:not_equal:Converted)"
```

### `criteria` (query) — Complex

Complex nested criteria

```json
"(((Company:equals:Zoho) and (First_Name:starts_with:J)) or (Last_Name:equals:Smith))"
```

### `converted` (query) — ConvertedLeads

```json
"true"
```

### `converted` (query) — NonConvertedLeads

```json
"false"
```

### `converted` (query) — BothConvertedAndNonConvertedLeads

```json
"both"
```

### `approved` (query) — ConvertedLeads

```json
"true"
```

### `approved` (query) — NonConvertedLeads

```json
"false"
```

### `approved` (query) — BothConvertedAndNonConvertedLeads

```json
"both"
```

### `page` (query) — Example

```json
1
```

### `per_page` (query) — Example

```json
200
```

### `type` (query) — AllUsers

Get count of all users

```json
"AllUsers"
```

### `type` (query) — ActiveUsers

Get count of active users

```json
"ActiveUsers"
```

### `type` (query) — DeactiveUsers

Get count of deactivated users

```json
"DeactiveUsers"
```

### `type` (query) — ConfirmedUsers

Get count of confirmed users

```json
"ConfirmedUsers"
```

### `type` (query) — ConfirmedReportingUsers

Get count of confirmed reporting users

```json
"ConfirmedReportingUsers"
```

### `type` (query) — NotConfirmedUsers

Get count of unconfirmed users

```json
"NotConfirmedUsers"
```

### `type` (query) — DeletedUsers

Get count of deleted users

```json
"DeletedUsers"
```

### `type` (query) — ActiveConfirmedUsers

Get count of active and confirmed users

```json
"ActiveConfirmedUsers"
```

### `type` (query) — AdminUsers

Get count of admin users

```json
"AdminUsers"
```

### `type` (query) — ActiveConfirmedAdmins

Get count of active confirmed admin users

```json
"ActiveConfirmedAdmins"
```

### `type` (query) — CurrentUser

Get current user information

```json
"CurrentUser"
```

## Response examples

### Status `200` — `application/json` — Success

Successful record count response

```json
{
  "count": 42
}
```

### Status `400` — `application/json` — InvalidRequest

Invalid request error

```json
{
  "status": "error",
  "code": "INVALID_REQUEST",
  "message": "unable to process your request. please verify whether you have entered proper method name, parameter and parameter values.",
  "details": {}
}
```

### Status `400` — `application/json` — FieldTypeUnavailable

Field type not found in module

```json
{
  "status": "error",
  "code": "FIELD_TYPE_UNAVAILABLE",
  "message": "this data type is not found in this module",
  "details": {}
}
```

### Status `400` — `application/json` — NotSupported

Module not supported for count

```json
{
  "status": "error",
  "code": "NOT_SUPPORTED",
  "message": "the given module is not supported for count",
  "details": {
    "module": "Module_Name"
  }
}
```

### Status `400` — `application/json` — ModuleNotSupportedForSearch

Module not supported for search

```json
{
  "status": "error",
  "code": "NOT_SUPPORTED",
  "message": "module not suppoted for search",
  "details": {
    "module": "Activities"
  }
}
```

### Status `400` — `application/json` — ExpectedParamMissing

Missing required search parameter

```json
{
  "status": "error",
  "code": "EXPECTED_PARAM_MISSING",
  "message": "one of the expected parameter is missing",
  "details": {
    "param_names": [
      "criteria",
      "email",
      "phone",
      "word"
    ]
  }
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name provided

```json
{
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {
    "resource_path_index": 1
  }
}
```

### Status `400` — `application/json` — InvalidQueryRestrictedField

Restricted field in search criteria

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "Cannot use the restricted field.",
  "details": {
    "reason": "Cannot use the restricted field.",
    "api_name": "Custom_Field_1"
  }
}
```

### Status `400` — `application/json` — InvalidQueryInvalidValue

Invalid value in search criteria

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "invalid value for search",
  "details": {
    "reason": "Please check the value of the field",
    "api_name": "Phone",
    "value": "ABC123"
  }
}
```

### Status `400` — `application/json` — InvalidQueryInvalidOperator

Invalid operator for field type

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "invalid operator found",
  "details": {
    "operator": "greater_than",
    "reason": "The operator is not valid for the field type",
    "api_name": "Email"
  }
}
```

### Status `400` — `application/json` — InvalidQueryDataTypeMismatch

Data type mismatch in search criteria

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "invalid value for search",
  "details": {
    "expected_data_type": "Integer",
    "reason": "invalid value for search",
    "api_name": "Age"
  }
}
```

### Status `400` — `application/json` — InvalidQueryFieldNotAvailable

Field not available for search

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "the field is not available for search",
  "details": {
    "reason": "the field is not available for search",
    "api_name": "Encrypted_Field"
  }
}
```

### Status `400` — `application/json` — InvalidQuerySpecialCharacters

Special characters in search criteria

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "special characters are not allowed",
  "details": {
    "reason": "special characters are not allowed",
    "api_name": "Search_Field"
  }
}
```

### Status `400` — `application/json` — InvalidQueryNoMaskingPermission

No masking permission for searched field

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "no_masking_permission",
  "details": {
    "reason": "no_masking_permission",
    "api_name": "Masked_Field"
  }
}
```

### Status `400` — `application/json` — InvalidQueryMultipleWildcards

Multiple wildcards in criteria not allowed

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "More than one wildcard(*) not allowed in a searchword",
  "details": {
    "reason": "More than one wildcard(*) not allowed in a searchword",
    "api_name": "Search_Field"
  }
}
```

### Status `400` — `application/json` — InvalidQueryInvalidParam

Invalid parameter in search criteria

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "Invalid query formed",
  "details": {
    "param_name": "email"
  }
}
```

### Status `400` — `application/json` — InvalidQueryInvalidOperatorForDataType

Operator not supported for data type

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "invalid operator found",
  "details": {
    "operator": "starts_with",
    "api_name": "Annual_Revenue"
  }
}
```

### Status `400` — `application/json` — InvalidDataTimeInvalidValue

Invalid date/time value in criteria

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "invalid value for search",
  "details": {
    "reason": "Please check the value of the field",
    "api_name": "Created_Time",
    "value": "invalid-date"
  }
}
```

### Status `400` — `application/json` — InvalidDateValue

Invalid date value in criteria

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "expected_data_type": "date",
    "reason": "invalid value for search",
    "api_name": "NonDate",
    "value": "asadsa"
  },
  "message": "Invalid query formed",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeMismatch

Data type mismatch in criteria

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "expected_data_type": "datetime",
    "reason": "invalid value for search",
    "api_name": "Modified_Time"
  }
}
```

### Status `400` — `application/json` — InvalidDataInvalidOperator

Invalid data - operator error

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "invalid operator found",
  "details": {
    "operator": "between",
    "reason": "The operator is not valid for the field type",
    "api_name": "Picklist_Field"
  }
}
```

### Status `400` — `application/json` — InvalidDataRestrictedField

Restricted field used in criteria

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "Cannot use the restricted field.",
  "details": {
    "reason": "Cannot use the restricted field.",
    "api_name": "System_Field"
  }
}
```

### Status `400` — `application/json` — InvalidDataSpecialCharacters

Special characters in criteria value

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "special characters are not allowed",
  "details": {
    "reason": "special characters are not allowed",
    "api_name": "Name"
  }
}
```

### Status `400` — `application/json` — InvalidDataMultipleWildcards

Multiple wildcards not allowed in criteria

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "More than one wildcard(*) not allowed in a searchword",
  "details": {
    "reason": "More than one wildcard(*) not allowed in a searchword",
    "api_name": "Company"
  }
}
```

### Status `400` — `application/json` — InvalidDataMinimumLength

Search term below minimum length

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "provide atleast 2 letters for search",
  "details": {
    "param_name": "word"
  }
}
```

### Status `400` — `application/json` — InvalidDataInvalidParam

Invalid data - parameter error

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "param_name": "word"
  }
}
```

### Status `400` — `application/json` — InvalidQueryInOperatorLimit

IN operator value limit exceeded

```json
{
  "status": "error",
  "code": "INVALID_QUERY",
  "message": "Only 100 values are allowed in \"IN\" criteria",
  "details": {
    "api_name": "Lead_Status"
  }
}
```

### Status `400` — `application/json` — LimitReached

Maximum record iteration limit reached

```json
{
  "status": "error",
  "code": "LIMIT_REACHED",
  "message": "maximum response iteration limit reached",
  "details": {
    "limit": "2000"
  }
}
```

### Status `400` — `application/json` — CriteriaLimitExceeded

More than 10 criteria specified

```json
{
  "status": "error",
  "code": "CRITERIA_LIMIT_EXCEEDED",
  "message": "no of criterium that can be given exceed the limit 15",
  "details": {}
}
```

### Status `400` — `application/json` — AmbiguityError

Ambiguous parameters - cvid with criteria

```json
{
  "status": "error",
  "code": "AMBIGUITY_DURING_PROCESSING",
  "message": "Please use either Cvid or Search Params. Combination of both the params is not allowed",
  "details": {
    "ambiguity_due_to": [
      {
        "param_name": "cvid"
      },
      {
        "param_name": "criteria"
      }
    ]
  }
}
```

### Status `400` — `application/json` — NotSupportedVersion

Operation not supported in this API version

```json
{
  "status": "error",
  "code": "API_NOT_SUPPORTED",
  "message": "api not supported in this version",
  "details": {
    "supported_version": "v2.1"
  }
}
```

### Status `401` — `application/json` — ScopeMismatch

OAuth scope mismatch error

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "You do not have the scope required to use this API."
}
```

### Status `500` — `application/json` — INTERNALERROR

Internal server error

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "status": "error"
}
```
