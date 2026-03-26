import pandas as pd
import requests
import time
from google.colab import files

# Chargement du fichier CSV
uploaded = files.upload()
filename = list(uploaded.keys())[0]
df = pd.read_csv(filename)
df.columns = df.columns.str.strip()
df = df.rename(columns={df.columns[0]: "entreprise"})
print(f"✅ {len(df)} entreprises chargées")
print(df.head())

# Fonction d'enrichissement
def enrich_company(company_name):
    try:
        url = f"https://autocomplete.clearbit.com/v1/companies/suggest?query={company_name}"
        response = requests.get(url, timeout=5)
        results = response.json()
        if results:
            company = results[0]
            return {
                "entreprise": company_name,
                "nom_officiel": company.get("name", ""),
                "domaine": company.get("domain", ""),
                "logo": company.get("logo", "")
            }
    except Exception:
        pass
    return {
        "entreprise": company_name,
        "nom_officiel": "",
        "domaine": "",
        "logo": ""
    }

# Enrichissement de toutes les entreprises
print("\n🔄 Enrichissement en cours...")
enriched = []
for company in df["entreprise"]:
    result = enrich_company(company)
    enriched.append(result)
    print(f"  ✅ {company} → {result['domaine']}")
    time.sleep(0.5)

# Export du fichier enrichi
df_enriched = pd.DataFrame(enriched)
print("\n✅ Enrichissement terminé !")
print(df_enriched)

df_enriched.to_csv("leads_enriched.csv", index=False)
print("\n📁 Fichier exporté : leads_enriched.csv")
files.download("leads_enriched.csv")
