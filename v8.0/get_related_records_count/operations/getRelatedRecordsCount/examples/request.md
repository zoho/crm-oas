### `application/json` — BasicCount

Basic related list count without filters

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Contacts",
        "id": "4150868000001038001"
      }
    }
  ]
}
```

### `application/json` — FilteredCount

Count request with field filter and approval status

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Deals",
        "id": "4150868000001038002"
      },
      "params": {
        "approved": true,
        "filters": {
          "comparator": "equal",
          "field": {
            "api_name": "Stage"
          },
          "value": "Closed Won"
        }
      }
    }
  ]
}
```

### `application/json` — MultipleRelatedLists

Count multiple related lists in one request

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Contacts",
        "id": "4150868000001038001"
      }
    },
    {
      "related_list": {
        "api_name": "Deals",
        "id": "4150868000001038002"
      }
    },
    {
      "related_list": {
        "api_name": "Tasks",
        "id": "4150868000001038003"
      }
    }
  ]
}
```

### `application/json` — ConvertedFilter

Count only converted leads in a related list

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Leads",
        "id": "4150868000001038004"
      },
      "params": {
        "converted": true,
        "filters": {
          "comparator": "equal",
          "field": {
            "api_name": "Status"
          },
          "value": "Qualified"
        }
      }
    }
  ]
}
```

### `application/json` — CategoryFilter

Count related records filtered by category type

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Attachments",
        "id": "4150868000001038005"
      },
      "params": {
        "category": "files",
        "filters": {
          "comparator": "equal",
          "field": {
            "api_name": "File_Type"
          },
          "value": "PDF"
        }
      }
    }
  ]
}
```

### `application/json` — ApprovalStateFilter

Count records filtered by approval state

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Quotes",
        "id": "4150868000001038006"
      },
      "params": {
        "approval_state": "approved",
        "filters": {
          "comparator": "equal",
          "field": {
            "api_name": "Quote_Stage"
          },
          "value": "Accepted"
        }
      }
    }
  ]
}
```
