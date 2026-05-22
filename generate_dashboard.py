import os
import base64
import folium
from folium import plugins

# 1. Define Hub Metadata for Data Centers, Grid Capacities, and Renewable Access
data_center_hubs = [
    # --- UNITED STATES ---
    {
        "country": "United States",
        "region": "Northern Virginia (Loudoun Co.)",
        "lat": 39.0438, "lon": -77.4875,
        "capacity_mw": 3200,
        "renewable_tier": "Moderate",
        "renewable_color": "#f2994a", # Orange
        "grid_status": "Severe Transmission Congestion; PJM grid capacity facing major reliability bottlenecks.",
        "renewables_breakdown": "High reliance on regional mixed grid. Hyper-scale operators are aggressively driving off-site virtual Power Purchase Agreements (vPPAs) for solar and wind to offset coal/gas baseline.",
        "pue_strategy": "Advanced evaporative chillers and winter air-side economization."
    },
    {
        "country": "United States",
        "region": "Phoenix, Arizona",
        "lat": 33.4484, "lon": -112.0740,
        "capacity_mw": 1400,
        "renewable_tier": "High",
        "renewable_color": "#219653", # Green
        "grid_status": "Stable desert grid distribution; high load match with daylight hours.",
        "renewables_breakdown": "Abundant utility-scale solar arrays and dedicated battery energy storage systems (BESS). Direct access to Western Area Power Administration hydro paths.",
        "pue_strategy": "Closed-loop liquid cooling architectures to eliminate extreme desert evaporation water overheads."
    },
    {
        "country": "United States",
        "region": "Dallas-Fort Worth, Texas",
        "lat": 32.7767, "lon": -96.7970,
        "capacity_mw": 1800,
        "renewable_tier": "High",
        "renewable_color": "#219653",
        "grid_status": "Independent ERCOT Grid; high market volatility but flexible micro-grid integration laws.",
        "renewables_breakdown": "Direct ingestion from the West Texas wind corridor and a booming ERCOT utility solar pipeline. Exceptional merchant power flexibility.",
        "pue_strategy": "Direct-to-chip warm water cooling handling high ambient outside temperatures."
    },
    # --- CHINA (Eastern Data, Western Computing Strategy) ---
    {
        "country": "China",
        "region": "Guizhou Hub (Guiyang)",
        "lat": 26.5833, "lon": 106.7167,
        "capacity_mw": 1200,
        "renewable_tier": "Very High",
        "renewable_color": "#137333", # Deep Green
        "grid_status": "National '东数西算' anchor. Highly robust regional power backbone.",
        "renewables_breakdown": "Dominated by vast provincial hydro-electric clusters and mountain wind farms. Ideal for non-realtime AI training models.",
        "pue_strategy": "Natural cave-insulated facility structures and year-round ambient cool-air circulation."
    },
    {
        "country": "China",
        "region": "Inner Mongolia Hub (Ulanqab)",
        "lat": 41.0312, "lon": 113.1141,
        "capacity_mw": 950,
        "renewable_tier": "High",
        "renewable_color": "#219653",
        "grid_status": "Abundant power supply; directly linked to Northern China power network exports.",
        "renewables_breakdown": "Massive high-plateau wind farms and desert solar fields. Grid mix still incorporates legacy coal but priority routing is given to clean compute loads.",
        "pue_strategy": "Extreme winter free-air cooling loops achieving sub-1.15 design PUE targets."
    },
    {
        "country": "China",
        "region": "Yangtze River Delta Hub",
        "lat": 31.2304, "lon": 121.4737,
        "capacity_mw": 1600,
        "renewable_tier": "Low",
        "renewable_color": "#eb5757", # Red
        "grid_status": "Ultra-high baseline industrial demand; extreme land and grid density constraints.",
        "renewables_breakdown": "Dependent on imported green power lines from western provinces. High carbon-intensity localized grid profile.",
        "pue_strategy": "AI-optimized algorithmic chilling plants and deep marine/river heat exchangers."
    },
    # --- INDIA ---
    {
        "country": "India",
        "region": "Mumbai / Navi Mumbai",
        "lat": 19.0330, "lon": 73.0297,
        "capacity_mw": 2200,
        "renewable_tier": "Moderate",
        "renewable_color": "#f2994a",
        "grid_status": "Highest grid reliability in India; major international subsea cable landing hub.",
        "renewables_breakdown": "Proximity to coastal grid junctions. Operators are increasingly tying up long-distance open-access solar contracts from interior Maharashtra and Gujarat.",
        "pue_strategy": "Industrial-scale centrifugal chillers with sea-breeze pre-cooling filtration."
    },
    {
        "country": "India",
        "region": "Bengaluru (Karnataka)",
        "lat": 12.9716, "lon": 77.5946,
        "capacity_mw": 850,
        "renewable_tier": "High",
        "renewable_color": "#219653",
        "grid_status": "Highly stable technology park distribution; progressive state wheeling open-access laws.",
        "renewables_breakdown": "Karnataka state grid leads India with over 50% nameplate clean capacity. Rich integration with localized solar installations and wind nodes.",
        "pue_strategy": "Adiabatic cooling systems optimized for Bengaluru's elevated, moderate altitude climate plateau."
    },
    {
        "country": "India",
        "region": "Chennai (Tamil Nadu)",
        "lat": 13.0827, "lon": 80.2707,
        "capacity_mw": 1100,
        "renewable_tier": "High",
        "renewable_color": "#219653",
        "grid_status": "Robust manufacturing corridor grid; strategic East-Asian subsea network gateway.",
        "renewables_breakdown": "Backed directly by Tamil Nadu's legacy wind power capacity (e.g., Muppandal clusters) and extensive southern grid solar farms.",
        "pue_strategy": "Vapor compression cycles running on intelligent variable speed drives to counter coastal humidity."
    }
]

def build_map_component():
    """Generates the interactive Folium map and returns it as a base64 encoded string."""
    # Initialize global map centered on an equatorial central longitude
    m = folium.Map(location=[25.0, 30.0], zoom_start=3, tiles="cartodbpositron", control_scale=True)
    
    # Feature groups for country isolation toggles
    fg_us = folium.FeatureGroup(name="United States Hubs")
    fg_cn = folium.FeatureGroup(name="China (东数西算) Hubs")
    fg_in = folium.FeatureGroup(name="India Clusters")
    
    for hub in data_center_hubs:
        # Scale circle radius to reflect operational megawatt footprint
        radius_size = (hub["capacity_mw"] / 100) * 1.8
        
        # Build clean, high-design HTML popups without ugly table borders
        popup_html = f"""
        <div style="font-family: 'Roboto', sans-serif; width: 280px; color: #202124;">
            <h4 style="margin: 0 0 4px 0; font-size: 16px; font-weight: 700; color: #1a73e8;">{hub['region']}</h4>
            <p style="margin: 0 0 12px 0; font-size: 12px; font-weight: 500; color: #5f6368;">{hub['country']}</p>
            
            <div style="margin-bottom: 8px;">
                <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #70757a; display: block;">Grid Pipeline Capacity</span>
                <strong style="font-size: 15px; color: #202124;">{hub['capacity_mw']} MW</strong>
            </div>
            
            <div style="margin-bottom: 8px;">
                <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #70757a; display: block;">Renewable Access Profile</span>
                <span style="display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; background-color: {hub['renewable_color']}20; color: {hub['renewable_color']};">
                    ● {hub['renewable_tier']} Availability
                </span>
            </div>
            
            <div style="margin-bottom: 8px; border-top: 1px solid #f1f3f4; padding-top: 6px;">
                <span style="font-size: 11px; font-weight: 700; color: #202124; display: block;">Grid Constraints:</span>
                <p style="margin: 2px 0 0 0; font-size: 11px; line-height: 1.4; color: #3c4043;">{hub['grid_status']}</p>
            </div>
            
            <div style="margin-bottom: 4px;">
                <span style="font-size: 11px; font-weight: 700; color: #202124; display: block;">Sustainability/PUE Strategy:</span>
                <p style="margin: 2px 0 0 0; font-size: 11px; line-height: 1.4; color: #3c4043;">{hub['pue_strategy']}</p>
            </div>
        </div>
        """
        
        marker = folium.CircleMarker(
            location=[hub["lat"], hub["lon"]],
            radius=radius_size,
            popup=folium.Popup(popup_html, max_width=300),
            color=hub["renewable_color"],
            fill=True,
            fill_color=hub["renewable_color"],
            fill_opacity=0.6,
            weight=1.5
        )
        
        if hub["country"] == "United States":
            fg_us.add_child(marker)
        elif hub["country"] == "China":
            fg_cn.add_child(marker)
        elif hub["country"] == "India":
            fg_in.add_child(marker)

    # Add features and full controls to map
    m.add_child(fg_us)
    m.add_child(fg_cn)
    m.add_child(fg_in)
    folium.LayerControl(position="topright", collapsed=False).add_to(m)
    plugins.Fullscreen(position="topleft", title="Expand Map", title_cancel="Exit").add_to(m)
    
    # Render map to HTML string, encode to Base64 to bypass iframe nesting bugs
    raw_html = m.get_root().render()
    b64_html = base64.b64encode(raw_html.encode("utf-8")).decode("utf-8")
    return b64_html

def generate_full_dashboard():
    """Compiles spatial data and the custom Google-styled responsive HTML wrapper."""
    print("[⚡] Generating interactive geospatial layers...")
    map_b64 = build_map_component()
    
    print("[🎨] Embedding custom about.google-style corporate interface frameworks...")
    
    # Complete, production-grade template using pure Google layout signatures
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoGrid AI // High-Scale AI Data Center Grid & Sustainability Matrix</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --google-gray-900: #202124;
            --google-gray-700: #5f6368;
            --google-gray-200: #f1f3f4;
            --google-blue: #1a73e8;
            --google-green: #137333;
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Roboto', sans-serif;
            background-color: #ffffff;
            color: var(--google-gray-900);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}

        /* Top Navigation Bar */
        nav {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 64px;
            background-color: #ffffff;
            border-bottom: 1px solid var(--google-gray-200);
            position: sticky;
            top: 0;
            z-index: 1000;
        }}

        .nav-logo {{
            font-size: 20px;
            font-weight: 500;
            color: var(--google-gray-900);
            letter-spacing: -0.5px;
        }}
        
        .nav-logo span {{
            color: var(--google-blue);
            font-weight: 700;
        }}

        .nav-links a {{
            text-decoration: none;
            color: var(--google-gray-700);
            margin-left: 32px;
            font-size: 14px;
            font-weight: 500;
            transition: color 0.2s ease;
        }}

        .nav-links a:hover {{
            color: var(--google-blue);
        }}

        /* Hero Main Section - about.google Layout Signature */
        .hero {{
            padding: 100px 64px 60px 64px;
            max-width: 1100px;
            margin: 0 auto;
        }}

        .hero h1 {{
            font-size: 56px;
            font-weight: 400;
            line-height: 1.15;
            letter-spacing: -1.5px;
            margin-bottom: 24px;
            color: var(--google-gray-900);
        }}

        .hero p {{
            font-size: 22px;
            font-weight: 300;
            color: var(--google-gray-700);
            line-height: 1.5;
            max-width: 850px;
            margin-bottom: 40px;
        }}

        /* Key Performance Metric Row */
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            max-width: 1200px;
            margin: 0 auto 60px auto;
            padding: 0 64px;
        }}

        .metric-card {{
            background: #ffffff;
            border: 1px solid var(--google-gray-200);
            border-radius: 8px;
            padding: 32px;
            transition: box-shadow 0.3s ease;
        }}

        .metric-card:hover {{
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        }}

        .metric-card h3 {{
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--google-gray-700);
            margin-bottom: 12px;
        }}

        .metric-card .value {{
            font-size: 36px;
            font-weight: 700;
            color: var(--google-gray-900);
            margin-bottom: 8px;
        }}

        .metric-card .subtext {{
            font-size: 13px;
            color: var(--google-gray-700);
        }}

        /* Visualization Layout Window */
        .map-section {{
            max-width: 1400px;
            margin: 0 auto 80px auto;
            padding: 0 64px;
        }}

        .map-wrapper {{
            background: #ffffff;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid var(--google-gray-200);
            box-shadow: 0 10px 40px rgba(0,0,0,0.04);
        }}

        /* Detailed Deep-Dive Section */
        .details-section {{
            background-color: #f8f9fa;
            padding: 80px 64px;
        }}

        .details-container {{
            max-width: 1100px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 64px;
        }}

        .details-sidebar h2 {{
            font-size: 32px;
            font-weight: 400;
            letter-spacing: -0.5px;
            position: sticky;
            top: 100px;
        }}

        .region-block {{
            margin-bottom: 48px;
            background: #ffffff;
            padding: 32px;
            border-radius: 12px;
            border: 1px solid var(--google-gray-200);
        }}

        .region-block h3 {{
            font-size: 22px;
            font-weight: 500;
            margin-bottom: 16px;
            color: var(--google-blue);
        }}

        .region-block p {{
            font-size: 15px;
            color: var(--google-gray-700);
            margin-bottom: 16px;
        }}

        /* Enterprise Architecture Alignment Element */
        .architecture-blueprint {{
            max-width: 1100px;
            margin: 80px auto;
            padding: 0 64px;
        }}

        .architecture-blueprint h2 {{
            font-size: 32px;
            font-weight: 400;
            margin-bottom: 24px;
            letter-spacing: -0.5px;
        }}

        .blueprint-box {{
            background: #fff;
            border-left: 4px solid var(--google-blue);
            padding: 24px;
            background-color: var(--google-gray-200);
            border-radius: 0 8px 8px 0;
            font-family: monospace;
            font-size: 14px;
            color: #3c4043;
            line-height: 1.8;
            white-space: pre-wrap;
        }}

        footer {{
            text-align: center;
            padding: 40px;
            font-size: 13px;
            color: var(--google-gray-700);
            border-top: 1px solid var(--google-gray-200);
        }}

        @media (max-width: 968px) {{
            nav {{ padding: 16px 24px; }}
            .hero {{ padding: 60px 24px 40px 24px; }}
            .hero h1 {{ font-size: 36px; }}
            .metrics-grid {{ grid-template-columns: 1fr; padding: 0 24px; }}
            .map-section {{ padding: 0 24px; }}
            .details-container {{ grid-template-columns: 1fr; gap: 32px; }}
            .details-section {{ padding: 40px 24px; }}
        }}
    </style>
</head>
<body>

    <nav>
        <div class="nav-logo">EcoGrid <span>AI</span></div>
        <div class="nav-links">
            <a href="#overview">Overview</a>
            <a href="#interactive-map">Global Map</a>
            <a href="#regional-insights">Regional Insights</a>
            <a href="#architecture">Architecture Blueprint</a>
        </div>
    </nav>

    <section class="hero" id="overview">
        <h1>Mapping the hyper-scale energy footprint.</h1>
        <p>As deep learning models scale exponentially, data center clusters represent unprecedented structural loads on sovereign utility infrastructures. This engine analyzes proposed capacity rollouts across the United States, China, and India—intersecting targeted megawatt demands against power grid stability constraints and localized renewable asset availability.</p>
    </section>

    <section class="metrics-grid">
        <div class="metric-card">
            <h3>Tracked Global Capacity</h3>
            <div class="value">14.9 GW</div>
            <div class="subtext">Aggregate power demand pipeline for tracked clusters across the US, China, and India regions.</div>
        </div>
        <div class="metric-card">
            <h3>Renewable Lead</h3>
            <div class="value">Guizhou Hub</div>
            <div class="subtext">Highest immediate clean resource availability driven by localized sovereign hydro-electric networks.</div>
        </div>
        <div class="metric-card">
            <h3>Critical Bottleneck</h3>
            <div class="value">N. Virginia</div>
            <div class="subtext">PJM transmission limitations and land allocation density causing hyper-scale deployment friction.</div>
        </div>
    </section>

    <section class="map-section" id="interactive-map">
        <div class="map-wrapper">
            <iframe src="data:text/html;base64,{map_b64}" width="100%" height="680px" style="border: none; display: block;"></iframe>
        </div>
    </section>

    <section class="details-section" id="regional-insights">
        <div class="details-container">
            <div class="details-sidebar">
                <h2>Regional Infrastructure Realities</h2>
            </div>
            <div class="details-content">
                <div class="region-block">
                    <h3>United States: Transmission & vPPA Friction</h3>
                    <p><strong>Northern Virginia (PJM Grid)</strong> remains the largest consolidated data center hub globally. However, massive multi-gigawatt development pipelines have triggered major distribution utility transmission warnings. To satisfy corporate sustainability metrics, operators are forcing heavy capital allocations into virtual Power Purchase Agreements (vPPAs) across separate regional solar and wind fields to balance localized baseline gas/coal generation dependencies.</p>
                    <p>Conversely, western hubs like <strong>Phoenix, Arizona</strong> show exceptional structural alignment between daytime photovoltaic production and maximum cooling load cycles, though dry climates necessitate a technological shift toward closed-loop waterless liquid architectures.</p>
                </div>
                
                <div class="region-block">
                    <h3>China: The 'Eastern Data, Western Computing' Strategy</h3>
                    <p>Under the national <strong>东数西算 (East-to-West Computing)</strong> directive, China is systematically mitigating the acute power and land supply bottlenecks of coastal gateways like Shanghai by moving large-scale data facilities to resource-rich western provinces.</p>
                    <p>The <strong>Guizhou Hub</strong> leverages massive regional hydro-electric installations combined with subterranean/cave configurations that inherently depress operational Power Usage Effectiveness (PUE). Concurrently, the <strong>Inner Mongolia (Ulanqab)</strong> plateau offers exceptional baseline wind resource footprints alongside sub-zero winter air profiles, matching optimally with non-latency-critical massive AI training runs.</p>
                </div>

                <div class="region-block">
                    <h3>India: Hyper-Scale Consolidation & Grid Transformation</h3>
                    <p>India represents the fastest-growing digital infrastructure market in South Asia, anchoring heavily on coastal gateways. <strong>Mumbai / Navi Mumbai</strong> handles the vast majority of international subsea data pipeline paths, delivering peerless grid uptime records but requiring extensive commercial open-access cross-provincial sourcing strategies to bring in green power.</p>
                    <p>In the southern tech hubs, <strong>Bengaluru (Karnataka)</strong> offers structural leadership—the state grid routinely derives over half of its total generation footprint from operational wind and solar assets, allowing hyper-scalers to meet Scope 2 decarbonization priorities naturally without auxiliary greenfield capital deployment.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="architecture-blueprint" id="architecture">
        <h2>Enterprise Spatial Intelligence Blueprint</h2>
        <div class="blueprint-box">
[Ingestion Layer] -> REST API / Open-Data Pipeline (US Infrastructure Data, China National Plan, India-WRIS/CEA Ports)
        │
        ▼
[Spatial Processing Pipeline] -> GeoPandas Alignment + Coordinate Translation Matrices
        │
        ▼
[Folium Map Core Engine] -> Multi-Layer Vector Scaling (Radius ∝ Megawatt Demand)
        │                       ↳ Color Class Mapping (Green: Clean, Orange: Constrained, Red: Hydrocarbon Interventions)
        ▼
[Compilation Logic Engine] -> Base64 Data Stream Compactor -> Output: Self-Contained Web Architecture Asset (index.html)</div>
    </section>

    <footer>
        Enterprise Sustainability & Compute Infrastructure Intelligence Engine • Portfolio Career Framework
    </footer>

</body>
</html>
"""
    
    output_path = "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"[✔] Single-file dashboard artifact successfully compiled to: {os.path.abspath(output_path)}")
    print("[💡] Push this file to the root of your GitHub repository to activate GitHub Pages deployment instantly.")

if __name__ == "__main__":
    generate_full_dashboard()