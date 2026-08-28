# Examples: putReorderEntries

**PUT /settings/automation/assignment_rules/{id}/actions/reorder_entries**

## Parameter examples

### `id` (path) — Typical

sample value 1

```json
"123456789"
```

### `id` (path) — LargeId

Maximum long value example

```json
"9223372036854775807"
```

## Request examples

### `application/json` — SamplePutRequest

Sample request body

```json
{
  "assignment_rules": [
    {
      "rule_entries": [
        {
          "id": "543219876547653",
          "sequence_number": 2
        },
        {
          "id": "543219876547654",
          "sequence_number": 5
        },
        {
          "id": "543219876547655",
          "sequence_number": 10
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful Assignment Rule operation

```json
{
  "assignment_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "123456"
      },
      "message": "",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — ErrAssignmentRulesMaxLenExceedsInReqBodyExample

Error response with code INVALID_DATA: invalid data (Field: assignment_rules)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "assignment_rules",
    "json_path": "$.assignment_rules"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — ErrMandatoryRuleEntriesNotFoundInReqBodyExample

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: rule_entries)

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "rule_entries",
        "json_path": "$.assignment_rules[0].rule_entries"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrRuleEntriesExpectedDatatypeMismatchInReqBodyExample

Error response with code INVALID_DATA: Invalid data type (Field: rule_entries)

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "rule_entries",
        "expected_data_type": "jsonarray",
        "json_path": "$.assignment_rules[*].rule_entries"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrRuleEntriesMinLenNotMetInReqBodyExample

Error response with code INVALID_DATA: Invalid data (Field: rule_entries)

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "rule_entries",
        "minimum_length": 1,
        "json_path": "$.assignment_rules[*].rule_entries"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrRuleEntriesMaxLenExceedsInReqBodyExample

Error response with code INVALID_DATA: Invalid data (Field: rule_entries)

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "rule_entries",
        "maximum_length": 200,
        "json_path": "$.assignment_rules[*].rule_entries"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrMandatoryRuleEntryIdNotFoundInReqBodyExample

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: ID)

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrRuleEntryIdExpectedDatatypeMismatchInReqBodyExample

Error response with code INVALID_DATA: Invalid data type (Field: ID)

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.assignment_rules[0].rule_entries[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrMandatoryRuleEntrySequenceNumberNotFoundInReqBodyExample

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: sequence_number)

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "sequence_number",
        "json_path": "$.assignment_rules[0].rule_entries[*].sequence_number"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrRuleEntrySequenceNumberExpectedDatatypeMismatchInReqBodyExample

Error response with code INVALID_DATA: Invalid data type (Field: sequence_number)

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "sequence_number",
        "expected_data_type": "integer",
        "json_path": "$.assignment_rules[0].rule_entries[*].sequence_number"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrInvalidSequenceNumberInReqBodyExample

Error response with code INVALID_DATA: Invalid sequence number (Field: sequence_number)

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "sequence_number",
        "json_path": "$.assignment_rules[0].rule_entries[*].sequence_number"
      },
      "message": "Invalid sequence number",
      "status": "error"
    }
  ]
}
```
