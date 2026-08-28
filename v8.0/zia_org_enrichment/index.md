# Zia organization enrichment

- [OpenAPI specification](zia_org_enrichment.yaml)
- [Trigger organization-level enrichment for a CRM record](mds/submitOrgEnrichmentRequest.md)
  - To submit a request that schedules a Zia organization enrichment job in your Zoho CRM organization. The job runs asynchronously and uses the supplied name, email, or website to retrieve publicly available details such as address, primary contact, industries, and social media handles, and to populate the configured fields of the target module or record.
  - [Examples](mds/examples/submitOrgEnrichmentRequest.md)
- [Get Zia Org Enrichment](mds/getZiaOrgEnrichment.md)
  - To retrieve the paginated list of Zia organization enrichment jobs that have been scheduled in your Zoho CRM organization. Each entry includes the job identifier, current status, creation timestamp, and the user who triggered the job.
  - [Examples](mds/examples/getZiaOrgEnrichment.md)
- [Org Enrichment Details](mds/getOrgEnrichmentById.md)
  - Fetches the enrichment status and enriched organization data for a specific enrichment job using its unique ID. Returns completed, scheduled, or failed enrichment information along with enriched fields such as name, website, email, address, CEO, revenue, employees, social media, and industries.
  - [Examples](mds/examples/getOrgEnrichmentById.md)
