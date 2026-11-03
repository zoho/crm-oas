### `application/json` — SamplePutRequest

Update an email notification with merge field, group, and territory recipients

```json
{
  "email_notifications": [
    {
      "name": "Big Deal Alert",
      "from_address": {
        "resource": {
          "id": "6660682000000501001"
        },
        "type": "user"
      },
      "recipients": {
        "to": [
          {
            "details": {
              "api_name": "${!Deals.Created_By}",
              "id": "6660682000000002577"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Owner}",
              "id": "6660682000000002555"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Owner.Reporting_To}",
              "id": "6660682000000256015"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Campaign_Source.Owner}",
              "id": "6660682000000002647"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Campaign_Source.Created_By}",
              "id": "6660682000000002669"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Account_Name.Owner}",
              "id": "6660682000000002421"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Account_Name.Created_By}",
              "id": "6660682000000002453"
            },
            "type": "merge_field"
          },
          {
            "resource": {
              "name": "Patricia Boyle",
              "id": "6660682000000501001"
            },
            "type": "user"
          },
          {
            "details": {
              "api_name": "${!Deals.Contact_Name.Email}",
              "id": "6660682000000002497"
            },
            "type": "merge_field"
          },
          {
            "resource": {
              "name": "UserGroup",
              "id": "6660682000001441002"
            },
            "type": "group"
          },
          {
            "resource": {
              "name": "CEO",
              "id": "6660682000000026005"
            },
            "type": "role_and_subordinate"
          },
          {
            "resource": {
              "name": "Territory_EU",
              "id": "6660682000001453003"
            },
            "type": "territory"
          }
        ]
      },
      "reply_to_address": {
        "resource": {
          "id": "6660682000000501001"
        },
        "type": "user"
      },
      "template": {
        "name": "Big Deal Alert",
        "id": "6660682000000000079"
      }
    }
  ]
}
```
