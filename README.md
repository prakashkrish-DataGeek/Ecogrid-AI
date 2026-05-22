# EcoGrid AI v2.0 — Hyper-Scale Data Center Grid & Sustainability Intelligence

**By Prakash Krishnamachari** · Digital, Data & Innovation Leader · 25+ years in asset-heavy infrastructure (Shell, Maersk, TotalEnergies)

[![GitHub Pages](https://img.shields.io/badge/Live-GitHub%20Pages-00C877?style=flat-square)](https://prakashkrish-datageek.github.io/Ecogrid-AI/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

---

## What This Is

A practitioner grade, single-file interactive intelligence platform analyzing **11 hyper-scale AI data center clusters** across the US, China, and India against a six-dimensional constraint matrix:

| Dimension | What It Captures |
|---|---|
| **Renewable Access Score** | 24/7 CFE availability, not just annual percentage claims |
| **Grid Stability** | Interconnect queue depth, substation saturation, redundancy architecture |
| **Water Risk** | Cooling water availability, regulatory trajectory, long-run stress (inverted for scoring) |
| **Policy Clarity** | Permitting timelines, wheeling regulatory stability, sovereignty constraints |
| **Cost Competitiveness** | All-in power cost including wheeling, transmission, and PPA structure |
| **Infrastructure Readiness** | Operator density, substation availability, fiber/connectivity maturity |

Total tracked pipeline: **14.9 GW** across 3 sovereign grids.

---

## What's New in v2.0

### vs. the Original EcoGrid AI

| Feature | v1.0 | v2.0 |
|---|---|---|
| Sites tracked | 8 | 11 (added Rajasthan Solar Zone, Yangtze River Delta expanded, DFW added) |
| Scoring dimensions | 2 (capacity, renewable label) | 6 (composite, weighted) |
| Carbon intensity data | ❌ | ✅ gCO₂/kWh per grid |
| Water stress layer | ❌ | ✅ Indexed 1–5 + regulatory trajectory |
| Policy risk analysis | ❌ | ✅ Per-site PPA and regulatory context |
| Operator landscape | ❌ | ✅ Named operators + MW committed |
| PUE data | Label only | Achieved range + cooling architecture rationale |
| Analytics charts | ❌ | ✅ 4 interactive Chart.js visualizations |
| Practitioner synthesis | ❌ | ✅ Operator-perspective commentary |
| Risk register | ❌ | ✅ 6 structural risks with probability/impact |
| Architecture principles | ❌ | ✅ 6-layer infrastructure framework |
| Dark mode aesthetic | Light Carto map | Full dark-first design with grid texture |
| Map filter controls | ❌ | ✅ Region-based filtering |
| Scoring matrix table | ❌ | ✅ Sortable comparative matrix |

---

## Methodology Notes

### Why Composite Scoring Matters

Most site comparison tools use a single axis—typically renewable percentage or power cost. This obscures the real trade-off structure. A site like Inner Mongolia scores extremely well on cost but has catastrophic water stress and high geopolitical opacity. A single-axis model would recommend it; the composite model appropriately flags it as conditional.

### The Water Stress Scoring (Inverted)

Water risk is scored inversely—a high "water score" means low risk. Phoenix scores 10/100 on water despite excellent solar resources, correctly capturing the structural dealbreaker that evaporative cooling at hyperscale is unsustainable there within a 10-year asset horizon.

### Carbon Intensity vs Renewable Percentage

The analysis uses grid carbon intensity (gCO₂/kWh) rather than stated renewable percentage for two reasons:
1. Annual renewable percentages can be gamed through REC markets without actually decarbonizing
2. Carbon intensity reflects the actual hourly mix including coal backup in intermittent renewable grids

Guizhou's hydro-dominated grid achieves 82 gCO₂/kWh—comparable to France's nuclear grid—while Inner Mongolia's wind-heavy grid still registers 420 gCO₂/kWh due to coal baseload in non-wind hours.

### PUE Target Ranges

PUE (Power Usage Effectiveness) figures represent the credible design target range for new hyperscale facilities at each location, not vendor marketing figures. They account for:
- ASHRAE climate design conditions at each site
- Cooling architecture feasible given water constraints
- GPU rack density assumptions (60–100 kW/rack for AI workloads)

---

## Key Findings

### The Guizhou Paradox
Best energy and PUE profile in the entire analysis (renewable: 96/100, carbon: 82 gCO₂/kWh, PUE: 1.08–1.12). Operationally inaccessible to Western operators due to China's data sovereignty framework. Illustrates the gap between energy economics and operational feasibility.

### The Northern Virginia Trap
Highest infrastructure readiness (95/100) and operator density in the world. Also the most severe grid saturation—PJM interconnect queue exceeds 300 GW against ~20 GW absorption capacity. Operators committing new capacity in 2025–2026 are essentially subsidizing grid upgrades for the broader market.

### The Rajasthan Opportunity
Greenfield, lowest potential PPA cost in the analysis ($22/MWh, ₹1.8–2.4/kWh), highest solar irradiance. Infrastructure readiness: 35/100. The asymmetric opportunity for an operator willing to function as a quasi-utility—owning generation assets and accepting 2027–2028 infrastructure maturity.

### India's PUE Challenge
Mumbai's climate forces PUE of 1.45–1.65, meaning 45–65% overhead energy per unit of IT work. At 2,200 MW of proposed capacity, this implies 990–1,430 MW of cooling and infrastructure power overhead. India's renewable economics are compelling; the cooling physics are the offsetting constraint.

---

## Repository Structure

```
Ecogrid-AI/
│
├── index.html              # Single-file application (deploy this)
├── README.md               # This file
└── LICENSE                 # MIT
```

The entire application is a **single HTML file** with no build process, no npm, no dependencies to install. All libraries (Leaflet, Chart.js) are loaded from CDN.

---

## Deployment — GitHub Pages

### Option A: Direct Upload (Simplest)
1. In your GitHub repository (`prakashkrish-DataGeek/Ecogrid-AI`), click **Add file → Upload files**
2. Upload `index.html` (replace existing)
3. Upload `README.md` (replace existing)
4. Commit directly to `main`
5. Go to **Settings → Pages**, ensure source is set to `Deploy from a branch: main / root`
6. Your site updates at `https://prakashkrish-datageek.github.io/Ecogrid-AI/` within ~60 seconds

### Option B: Git CLI
```bash
git clone https://github.com/prakashkrish-DataGeek/Ecogrid-AI.git
cd Ecogrid-AI

# Replace files
cp /path/to/index.html .
cp /path/to/README.md .

git add -A
git commit -m "EcoGrid AI v2.0 — enhanced multi-dimensional analysis"
git push origin main
```

### Option C: GitHub Desktop
1. Open GitHub Desktop, select the Ecogrid-AI repository
2. Copy the new `index.html` into the local repo folder (replacing the old file)
3. GitHub Desktop will show the changes
4. Write commit message and click **Commit to main** → **Push origin**

---

## Data Sources & Methodology

| Data Category | Sources |
|---|---|
| US Grid Capacity | FERC interconnect queue data, PJM/ERCOT/WECC published studies |
| China Grid Data | National Energy Administration (NEA) reports, State Grid publications |
| India Grid Data | Central Electricity Authority (CEA) annual reports, POSOCO data |
| Renewable Mix | IEA World Energy Statistics 2024, national utility disclosures |
| Carbon Intensity | electricityMaps, National Grid ESO, IEA Electricity Information |
| Water Stress | WRI Aqueduct 4.0 water risk framework |
| Operator Data | Company annual reports, data center news (DCD, Structure Research) |
| PPA Pricing | BloombergNEF PPA tracker, Lawrence Berkeley National Lab reports |
| PUE Benchmarks | Green Grid reports, Uptime Institute Global Survey 2024 |

*Data compiled May 2026. Grid capacity and operator landscape data subject to rapid change; verify against current sources before use in planning decisions.*

---

## Extending This Platform

The site data is a JavaScript array (`SITES`) at the top of the script section in `index.html`. To add new sites:

```javascript
{
  id: 'unique_id',
  name: 'Display Name',
  country: 'US/China/India/etc',
  region: 'us/china/india',          // for map filter
  lat: 00.0000, lng: 00.0000,         // decimal coordinates
  mw: 1000,                           // proposed MW capacity
  renewable: 75,                      // 0-100 score
  stability: 70,                      // 0-100 score
  water: 60,                          // 0-100 score (high = low risk)
  policy: 65,                         // 0-100 score
  cost: 80,                           // 0-100 score (high = cost-competitive)
  infra: 55,                          // 0-100 score
  pue: '1.15–1.25',                  // design target range
  carbonIntensity: 350,               // gCO2/kWh
  powerCost: 45,                      // USD/MWh all-in
  renewableAccess: 'High',            // Very High/High/Moderate/Low
  verdict: 'recommended',             // recommended/conditional/established/latency-only/frontier
  constraints: 'Description...',
  sustainability: 'Cooling architecture...',
  operators: 'Named operators...'
}
```

The map, scoring table, and charts all auto-generate from this data structure.

---

## About the Author

**Prakash Krishnamachari** is a senior digital and data transformation leader with 25+ years of experience across Shell, Maersk, and TotalEnergies E&P Uganda, where he currently serves as Digital, Data & Innovation Manager. He holds an Executive MBA from IIM Bangalore and an M.Tech from IIT Roorkee.

He is pasionate about Data, AI and the infinite possibilities between the two.

- **GitHub**: [github.com/prakashkrish-DataGeek](https://github.com/prakashkrish-DataGeek)
- **Focus**: Geospatial ML, decision intelligence, infrastructure transformation

---

## License

MIT License — see `LICENSE` file. Attribution appreciated.

---

*"The hyperscale energy conversation is dominated by press releases and policy announcements. The actual constraint is always in the last 10 meters — the transformer, the cooling tower, the interconnect agreement."*
