# Examples: executeCOQLQuery

**POST /coql**

## Request examples

### `application/json` — GetLeads

COQL query to retrieve Leads records

```json
{
  "select_query": "select Last_Name, First_Name from Leads where Last_Name = 'Smith'"
}
```

### `application/json` — GetLeadsWithFieldMetadata

COQL query to retrieve Leads records with field metadata

```json
{
  "select_query": "select Last_Name from Leads where Last_Name = 'TestLead'",
  "include_meta": [
    "fields"
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

Successful response with matching records and pagination metadata

```json
{
  "data": [
    {
      "Last_Name": "Smith",
      "First_Name": "John"
    }
  ],
  "info": {
    "count": 1,
    "more_records": false
  }
}
```

### Status `200` — `application/json` — SuccessResponseWithFieldsMeta

Successful response with records and field metadata for SELECT columns

```json
{
  "data": [
    {
      "Last_Name": "TestLead",
      "id": "4413054000000682520"
    }
  ],
  "fields": {
    "Last_Name": {
      "webhook": true,
      "operation_type": {
        "web_update": true,
        "api_create": true,
        "web_create": true,
        "api_update": true
      },
      "colour_code_enabled_by_system": false,
      "field_label": "Last Name",
      "tooltip": null,
      "display_format_properties": null,
      "type": "used",
      "table_name": "CrmLeadDetails",
      "field_read_only": false,
      "required": true,
      "customizable_properties": null,
      "display_label": "Last Name",
      "read_only": false,
      "association_details": null,
      "multi_module_lookup": {},
      "id": "4413054000000000559",
      "created_time": null,
      "filterable": true,
      "visible": true,
      "refer_from_field": null,
      "view_type": {
        "view": false,
        "edit": true,
        "quick_create": true,
        "create": true
      },
      "separator": false,
      "searchable": true,
      "history_tracking_enabled": false,
      "external": null,
      "api_name": "Last_Name",
      "parent_field": null,
      "unique": {},
      "enable_colour_code": false,
      "child_fields": null,
      "pick_list_values": [],
      "system_mandatory": true,
      "virtual_field": false,
      "json_type": "string",
      "crypt": null,
      "range": null,
      "created_source": "default",
      "display_type": -1,
      "ui_type": 127,
      "modified_time": null,
      "public": false,
      "quick_sequence_number": "3",
      "email_parser": {
        "fields_update_supported": false,
        "record_operations_supported": true
      },
      "currency": {},
      "custom_field": false,
      "lookup": {},
      "convert_mapping": {
        "Contacts": "Last_Name",
        "Deals": null,
        "Accounts": null
      },
      "address": null,
      "rollup_summary": {},
      "length": 80,
      "column_name": "LASTNAME",
      "display_field": false,
      "pick_list_values_sorted_lexically": false,
      "default_value": null,
      "sortable": true,
      "layout_associations": [
        {
          "api_name": "Standard__s",
          "name": "Standard",
          "id": "4413054000000095055"
        }
      ],
      "global_picklist": null,
      "display_format": null,
      "history_tracking": null,
      "data_type": "text",
      "lucene_colname": "LASTNAME",
      "generated_type": 1,
      "formula": {},
      "additional_column": null,
      "decimal_place": null,
      "multiselectlookup": {},
      "auto_number": {}
    }
  },
  "info": {
    "count": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — SyntaxErrorInvalidClause

Syntax error response for invalid clause

```json
{
  "code": "SYNTAX_ERROR",
  "details": {
    "clause": "where"
  },
  "message": "missing clause",
  "status": "error"
}
```

### Status `400` — `application/json` — SyntaxErrorLocation

Syntax error response with location details

```json
{
  "code": "SYNTAX_ERROR",
  "details": {
    "line": 1,
    "column": 15,
    "near": "FROM"
  },
  "message": "unexpected token",
  "status": "error"
}
```

### Status `400` — `application/json` — SyntaxErrorOperator

Syntax error response for unsupported operator

```json
{
  "code": "SYNTAX_ERROR",
  "details": {
    "operator": "not"
  },
  "message": "operator not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — SyntaxErrorQueryNotSupported

Syntax error response for unsupported query

```json
{
  "code": "SYNTAX_ERROR",
  "details": {},
  "message": "given coql query not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — SyntaxErrorNear

Syntax error response with near text context

```json
{
  "code": "SYNTAX_ERROR",
  "details": {
    "near": "where"
  },
  "message": "error occured while parsing the query",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQueryInvalidOperator

Invalid query error for invalid operator

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "reason": "invalid operator found",
    "column_name": "First_Name",
    "operator": ">"
  },
  "message": "Invalid query formed",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQueryIsNotNullOperator

Invalid query error with is not null operator

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "reason": "invalid operator found",
    "column_name": "textj8",
    "operator": "is not null"
  },
  "message": "Invalid query formed",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQueryIsNullOperator

Invalid query error with is null operator

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "reason": "invalid operator found",
    "column_name": "textj8",
    "operator": "is null"
  },
  "message": "Invalid query formed",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQueryInvalidAlias

Invalid query error for invalid alias

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "column_name": "First_Name",
    "alias": "Last_Name"
  },
  "message": "column name or property name given in select columns without alias name cannot be an alias name for other select columns",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFound

Mandatory field not found error response

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "select_query"
  },
  "message": "mandatory key not found",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateAlias

Duplicate alias error response

```json
{
  "code": "DUPLICATE_ALIAS",
  "details": {
    "referred_columns": [
      "First_Name",
      "Last_Name"
    ],
    "alias": "Name"
  },
  "message": "same alias cannot refer more than one column",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidAlias

Invalid alias error response

```json
{
  "code": "INVALID_ALIAS",
  "details": {
    "column_name": "First_Name",
    "alias": ""
  },
  "message": "alias name cannot be an empty string",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateData

Duplicate data error response

```json
{
  "code": "DUPLICATE_DATA",
  "details": {
    "column_name": "First_Name"
  },
  "message": "duplicate select column",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateDataAggregate

Duplicate data error with aggregate function

```json
{
  "code": "DUPLICATE_DATA",
  "details": {
    "column_name": "Annual_Revenue",
    "aggregate": "MAX"
  },
  "message": "duplicate aggregate function",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQueryInvalidLimit

Invalid query error for invalid limit

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "limit": "s"
  },
  "message": "limit given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQueryUnsupportedColumn

Invalid query error for unsupported column

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "column_name": "Last_Name"
  },
  "message": "unsupported column",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQueryEmptyDetails

Invalid query error with no additional details

```json
{
  "code": "INVALID_QUERY",
  "details": {},
  "message": "Invalid query formed",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQueryUnsupportedCriteria

Invalid query error for unsupported criteria column

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "cv_criteria": false,
    "column_name": "Participants",
    "value": "${EMPTY}",
    "operator": "!="
  },
  "message": "unsupported column in criteria",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQuerySubQueryOperator

Invalid query error for subquery with incompatible operator

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "sub_query_sequence": 0,
    "operator": ">"
  },
  "message": "subquery return more than one values which is incompatible for the operator",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidQuerySubQueryMultipleColumns

Invalid query error for subquery with multiple columns

```json
{
  "code": "INVALID_QUERY",
  "details": {
    "sub_query_sequence": 0,
    "column_name": [
      "Last_Name",
      "Annual_Revenue"
    ]
  },
  "message": "subquery should contains only one column",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidData

Invalid data error response

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonarray",
    "api_name": "include_meta",
    "json_path": "$.include_meta"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataSupportedValues

Invalid data error with supported values list

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "include_meta",
    "json_path": "$.include_meta[0]",
    "supported_values": [
      "fields"
    ]
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataUnsupportedFunction

Invalid data error for unsupported aggregate function

```json
{
  "code": "INVALID_DATA",
  "details": {
    "reason": "unsupported aggregate function",
    "column": "TestFunction(Last_Name)"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataExpectedTypeWithSupportedValues

Invalid data error with expected type and supported values

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "text",
    "api_name": "include_meta",
    "json_path": "$.include_meta[0]",
    "supported_values": [
      "fields"
    ]
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataLimitZero

Invalid data error for a limit of zero or less

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "limit should be greater than 0",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module error response

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the given module is not supported in api",
  "status": "error"
}
```
