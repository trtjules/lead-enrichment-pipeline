# lead-enrichment-pipeline
Automated pipeline to enrich a company list with domain and metadata using Clearbit API
# Lead Enrichment Pipeline

## What it does
Takes a raw CSV list of company names and automatically enriches it with domain, 
official name and metadata — using the Clearbit Autocomplete API.

Built to solve a real ops problem: manually researching company info before 
outreach is slow and unscalable. This pipeline does it in seconds.

## Business use case
- Sales & Growth teams working from raw prospect lists
- BDR/SDR workflows where lead data is incomplete
- Any ops context where you need to go from "company name" to actionable data fast

## How to use
1. Prepare a CSV file with a column called `company`
2. Open the script in Google Colab
3. Upload your CSV when prompted
4. Get an enriched CSV output automatically

## Output example
| entreprise | nom_officiel | domaine |
|---|---|---|
| Spotify | Spotify | spotify.com |
| Doctolib | Doctolib | doctolib.fr |
| Spendesk | Spendesk | spendesk.com |

## Limits & next steps
- Clearbit Autocomplete is a free API — accuracy varies on ambiguous names
- V2 : add Hunter.io for email pattern detection
- V2 : add Pappers API for French company legal data (SIRET, size, revenue)
- V2 : plug into a CRM (Notion, Airtable) directly via API
