# GET /settings/recycle_bin/actions/count
**Operation:** `getRecycleBinCounts` — Get recycle-bin record count
> To retrieve the total count of records currently present in the Recycle Bin in your Zoho CRM account. The count reflects every entry across all modules.

**Responses:**

- **200**: Returns the total count of records currently present in the Recycle Bin. [application/json]
    > Represents the response payload containing the total count of records present in the Recycle Bin.
    - `count` (integer/int32) **REQ** — Represents the total number of records currently present in the Recycle Bin.

**Scopes:** ZohoCRM.settings.recycle_bin.READ
