# Examples: bulkSearchRecords

**POST /{module}/bulk/search**

## Parameter examples

### `module` (path) — Leads

Search within Leads module

```json
"Leads"
```

### `module` (path) — Contacts

Search within Contacts module

```json
"Contacts"
```

### `module` (path) — Accounts

Search within Accounts module

```json
"Accounts"
```

### `approval_state` (query) — Approved

Get only approved records

```json
"approved"
```

### `approval_state` (query) — Pending

Get records pending approval

```json
"approval_process_pending"
```

### `approval_state` (query) — Rejected

Get rejected records

```json
"approval_process_rejected"
```

### `criteria` (query) — SimpleCriteria

Simple equality condition

```json
"(Company:equals:Zylker)"
```

### `criteria` (query) — ComplexCriteria

Multiple conditions with AND operator

```json
"((Company:equals:Zylker) and (Lead_Status:equals:Qualified))"
```

### `criteria` (query) — DateRange

Date range criteria

```json
"((Created_Time:greater_equal:2023-01-01T00:00:00+00:00) and (Created_Time:less_equal:2023-12-31T23:59:59+00:00))"
```

### `criteria` (query) — InOperator

Using IN operator for multiple values

```json
"(Lead_Status:in:Qualified,Contacted,Converted)"
```

### `converted` (query) — OnlyConverted

Get only converted records (e.g., converted leads)

```json
"true"
```

### `converted` (query) — OnlyUnconverted

Get only non-converted records (default)

```json
"false"
```

### `converted` (query) — AllRecords

Get all records regardless of conversion status

```json
"both"
```

### `word` (query) — CompanyName

Search for company name across fields

```json
"Zylker"
```

### `word` (query) — PersonName

Search for person name across fields

```json
"John Doe"
```

### `word` (query) — ProductTerm

Search for product-related terms

```json
"software"
```

### `word` (query) — Phrase

Search for multi-word phrases

```json
"marketing campaign"
```

### `email` (query) — ExactEmail

Search for exact email address

```json
"john.doe@example.com"
```

### `email` (query) — DomainSearch

Search for all emails from a domain

```json
"@company.com"
```

### `email` (query) — PartialEmail

Partial email search (finds john.doe@any-domain.com)

```json
"john.doe"
```

### `phone` (query) — International

International format with country code

```json
"+1-555-123-4567"
```

### `phone` (query) — National

US national format with parentheses

```json
"(555) 123-4567"
```

### `phone` (query) — DigitsOnly

Digits only format

```json
"5551234567"
```

### `phone` (query) — Partial

Partial phone number search

```json
"555-123"
```

### `fields` (query) — BasicFields

Basic contact information fields

```json
"First_Name,Last_Name,Email,Phone"
```

### `fields` (query) — LeadFields

Essential lead tracking fields

```json
"Company,Lead_Status,Lead_Source,Created_Time"
```

### `fields` (query) — AccountFields

Key account information fields

```json
"Account_Name,Industry,Annual_Revenue,Phone"
```

### `fields` (query) — Minimal

Minimal system fields only

```json
"id,Created_Time,Modified_Time"
```

### `page` (query) — FirstPage

First page of results (default)

```json
1
```

### `page` (query) — SecondPage

Second page of results

```json
2
```

### `page` (query) — TenthPage

Jump to tenth page

```json
10
```

### `per_page` (query) — SmallBatch

Small batch for testing or preview

```json
10
```

### `per_page` (query) — MediumBatch

Medium batch for regular processing

```json
50
```

### `per_page` (query) — LargeBatch

Large batch for bulk operations

```json
100
```

### `per_page` (query) — Maximum

Maximum records per page (default)

```json
200
```

### `sort_by` (query) — ById

Sort by record ID (default)

```json
"id"
```

### `sort_by` (query) — ByName

Sort by last name for contacts

```json
"Last_Name"
```

### `sort_by` (query) — ByCompany

Sort by company name

```json
"Company"
```

### `sort_by` (query) — ByCreated

Sort by creation date

```json
"Created_Time"
```

### `sort_by` (query) — ByModified

Sort by last modification date

```json
"Modified_Time"
```

### `sort_order` (query) — Descending

Descending order (newest/highest first, default)

```json
"desc"
```

### `sort_order` (query) — Ascending

Ascending order (oldest/lowest first)

```json
"asc"
```

### `type` (query) — ActiveUsers

Get only active users

```json
"ActiveUsers"
```

### `type` (query) — AdminUsers

Get admin users only

```json
"AdminUsers"
```

### `type` (query) — ConfirmedUsers

Get confirmed users

```json
"ConfirmedUsers"
```

### `type` (query) — AllUsers

Get all users regardless of status

```json
"AllUsers"
```

## Response examples

### Status `200` — `application/json` — LeadBulkSearchResult

Sample lead bulk search result

```json
{
  "data": [
    {
      "id": "<phone_number_or_numberic_id_or_random_id_26>",
      "Owner": {
        "name": "John Smith",
        "id": "<phone_number_or_numberic_id_or_random_id_27>",
        "email": "john.smith@zylker.com"
      },
      "Company": "Zylker",
      "Email": "john.smith@zylker.com",
      "Lead_Status": "Qualified",
      "Created_Time": "2023-01-15T10:30:00+00:00",
      "Modified_Time": "2023-01-20T14:45:00+00:00",
      "Created_By": {
        "name": "John Smith",
        "id": "<phone_number_or_numberic_id_or_random_id_27>"
      },
      "Modified_By": {
        "name": "John Smith",
        "id": "<phone_number_or_numberic_id_or_random_id_27>"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — MissingParameter

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

Invalid module specified

```json
{
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {
    "resource_path_index": 0
  }
}
```

### Status `401` — `application/json` — OauthScopeMismatch

Missing required OAuth scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "Unauthorized",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

Insufficient permissions for module access

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "Permission denied to read",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Invalid API endpoint URL

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```

### Status `429` — `application/json` — RateLimitExceeded

API rate limit exceeded

```json
{
  "code": "RATE_LIMIT_EXCEEDED",
  "details": {},
  "message": "Too many requests. Please try again later.",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalError

Unexpected server error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```

### Status `502` — `application/json` — ServiceUnavailable

Upstream service failure

```json
{
  "code": "SERVICE_UNAVAILABLE",
  "details": {},
  "message": "Service temporarily unavailable",
  "status": "error"
}
```

### Status `503` — `application/json` — MaintenanceMode

Service under maintenance

```json
{
  "code": "SERVICE_UNAVAILABLE",
  "details": {},
  "message": "Service temporarily unavailable for maintenance",
  "status": "error"
}
```
