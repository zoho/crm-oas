List of Available APIs

```json
{
  "__apis": [
    {
      "path": "/crm/v8/Quotes/{{id}}/actions/send_mail",
      "operation_types": [
        {
          "method": "POST",
          "oauth_scope": "ZohoCRM.send_mail.quotes.CREATE",
          "max_credits": 20,
          "min_credits": 20
        },
        {
          "method": "PUT",
          "oauth_scope": "ZohoCRM.send_mail.quotes.CREATE",
          "max_credits": 20,
          "min_credits": 20
        }
      ]
    },
    {
      "path": "/crm/v8/Accounts/{{id}}/photo",
      "operation_types": [
        {
          "method": "GET",
          "oauth_scope": "ZohoCRM.modules.accounts.READ",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "DELETE",
          "oauth_scope": "ZohoCRM.modules.accounts.DELETE",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "POST",
          "oauth_scope": "ZohoCRM.modules.accounts.CREATE",
          "max_credits": 1,
          "min_credits": 1
        }
      ]
    },
    {
      "path": "/crm/v8/Deals/{{id}}/Attachments",
      "operation_types": [
        {
          "method": "POST",
          "oauth_scope": "ZohoCRM.modules.deals.CREATE",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "GET",
          "oauth_scope": "ZohoCRM.modules.deals.READ",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "PUT",
          "oauth_scope": "ZohoCRM.modules.deals.UPDATE",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "DELETE",
          "oauth_scope": "ZohoCRM.modules.deals.DELETE",
          "max_credits": 1,
          "min_credits": 1
        }
      ]
    }
  ]
}
```
