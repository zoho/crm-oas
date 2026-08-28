# Examples: convertLead

**POST /Leads/{leadId}/actions/convert**

## Request examples

### `application/json` — BasicConversion

Basic lead conversion to Contact only

```json
{
  "data": [
    {
      "overwrite": false,
      "notify_lead_owner": true,
      "notify_new_entity_owner": false
    }
  ]
}
```

### `application/json` — ConversionWithDeal

Lead conversion with Deal creation

```json
{
  "data": [
    {
      "overwrite": false,
      "notify_lead_owner": true,
      "notify_new_entity_owner": true,
      "Deals": {
        "Deal_Name": "Enterprise Package Deal",
        "Pipeline": "Standard (Standard)",
        "Stage": "Qualification",
        "Closing_Date": "2025-12-31",
        "Amount": 50000,
        "Probability": 60
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulConversion

Successful lead conversion with Contact only

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Contacts": {
          "name": "John Doe",
          "id": "1643514000006142991"
        },
        "Deals": null,
        "Accounts": null
      },
      "message": "The record has been converted successfully",
      "status": "success"
    }
  ]
}
```

### Status `200` — `application/json` — FullConversion

Complete lead conversion with Contact, Deal, and Account

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Contacts": {
          "name": "John Doe",
          "id": "1643514000006145045"
        },
        "Deals": {
          "name": "Enterprise Deal",
          "id": "1643514000006145051"
        },
        "Accounts": {
          "name": "Acme Corp",
          "id": "1643514000006145040"
        }
      },
      "message": "The record has been converted successfully",
      "status": "success"
    }
  ]
}
```

### Status `202` — `application/json` — ScheduledConversion

Lead conversion scheduled successfully

```json
{
  "data": [
    {
      "code": "SCHEDULED",
      "details": {
        "job_id": "1643514000006145007"
      },
      "message": "Convert lead scheduled successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyConverted

Lead already converted

```json
{
  "code": "ID_ALREADY_CONVERTED",
  "details": {
    "resource_path_index": 1
  },
  "message": "id already converted",
  "status": "error"
}
```

### Status `400` — `application/json` — PipelineStageMismatch

Pipeline doesn't contain the specified Stage

```json
{
  "data": [
    {
      "code": "MAPPING_MISMATCH",
      "details": {
        "mapped_field": "Pipeline",
        "api_name": "Stage",
        "json_path": "$.data[0].Stage"
      },
      "message": "Pipeline doesn't contain the Stage",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NonSubordinateUser

Non subordinate user assigned as record owner

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Owner",
        "json_path": "$.data[0].Owner"
      },
      "message": "Non Subordinate User Found",
      "status": "error"
    }
  ]
}
```
