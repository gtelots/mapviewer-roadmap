#!/usr/bin/env python3
"""Consolidate tiny feature group files into larger domain files"""

import os
import glob
from collections import defaultdict

def merge_files(source_files, output_file, title):
    """Merge multiple feature group files into one"""
    
    all_features = []
    source_titles = []
    
    for filepath in source_files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract feature rows
        for line in content.split('\n'):
            if line.startswith('|') and 'Feature Group' not in line and 'Feature Name' not in line:
                if '---' not in line and line.count('|') > 3:
                    all_features.append(line)
        
        # Extract source title
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                source_titles.append(line.replace('# ', ''))
                break
    
    if not all_features:
        return 0
    
    # Create consolidated file
    header = """| Feature Group | Feature Name | Short Description | Detailed Description | Why This Feature is Needed | Implementation Phase |
|--------------|--------------|------------|----------------|---------------------------|---------------------|"""
    
    file_content = f"# {title}\n\n"
    file_content += f"> Consolidated from: {', '.join(set(source_titles))}\n\n"
    file_content += header + "\n"
    file_content += "\n".join(all_features) + "\n"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(file_content)
    
    print(f"✅ Created {output_file} ({len(all_features)} features from {len(source_files)} files)")
    
    # Delete source files
    for filepath in source_files:
        if os.path.exists(filepath):
            os.remove(filepath)
    
    return len(all_features)

# Consolidation mappings
consolidations = [
    # Social & Community (30 files → 1)
    {
        'files': [
            'docs/features/features/community.md',
            'docs/features/features/social.md',
            'docs/features/features/waze-feature.md',
            'docs/features/features/badge.md',
            'docs/features/features/road-reporter.md',
            'docs/features/features/traffic-guardian.md',
            'docs/features/features/community-champion.md',
            'docs/features/features/photo-master.md',
            'docs/features/features/accuracy-expert.md',
            'docs/features/features/local-expert.md',
            'docs/features/features/content-type.md',
            'docs/features/features/traffic-reports.md',
            'docs/features/features/photos.md',
            'docs/features/features/q-a.md',
            'docs/features/features/police-speed-trap-reports.md',
            'docs/features/features/gas-prices.md',
            'docs/features/features/voice-alerts.md',
            'docs/features/features/moods-avatars.md',
            'docs/features/features/verified-traffic-report.md',
            'docs/features/features/verified-incident-report.md',
            'docs/features/features/photo-contribution.md',
            'docs/features/features/q-a-answer-marked-helpful.md',
            'docs/features/features/first-report-of-incident.md',
            'docs/features/features/consecutive-daily-contributions.md',
            'docs/features/features/active-contributors.md',
            'docs/features/features/daily-reports.md',
            'docs/features/features/avg-response-time.md',
        ],
        'output': 'docs/features/features/social-community.md',
        'title': 'Social & Community Features'
    },
    
    # Automotive (25 files → 3)
    {
        'files': [
            'docs/features/verticals/automotive-adas.md',
            'docs/features/verticals/automotive-fleet.md',
        ],
        'output': 'docs/features/verticals/automotive-core.md',
        'title': 'Automotive Core (ADAS & Fleet)'
    },
    {
        'files': [
            'docs/features/verticals/ev.md',
            'docs/features/features/charging-station-api.md',
            'docs/features/features/vn-charging-stations.md',
            'docs/features/features/vinfast.md',
            'docs/features/features/vinfast-integration.md',
            'docs/features/features/vinfast-station-coverage.md',
            'docs/features/verticals/ev-user-adoption.md',
        ],
        'output': 'docs/features/verticals/ev-charging.md',
        'title': 'EV & Charging Infrastructure'
    },
    {
        'files': [
            'docs/features/features/range-calculation.md',
            'docs/features/features/carbon-calculation.md',
            'docs/features/features/carbon-reports-generated.md',
            'docs/features/features/range-prediction-accuracy.md',
            'docs/features/features/range-overlay.md',
            'docs/features/features/vehicle-database.md',
            'docs/features/features/charging-stations-covered.md',
            'docs/features/features/update-frequency.md',
            'docs/features/features/sustainability.md',
            'docs/features/features/partner.md',
            'docs/features/features/petrolimex.md',
            'docs/features/features/shopping-malls.md',
            'docs/features/vietnam/evn-vietnam-electricity.md',
        ],
        'output': 'docs/features/verticals/automotive-metrics.md',
        'title': 'Automotive Metrics & Sustainability'
    },
    
    # AI & ML (12 files → 2)
    {
        'files': [
            'docs/features/features/ai-ml.md',
            'docs/features/features/ml-framework.md',
            'docs/features/features/llm-provider.md',
            'docs/features/features/training-data.md',
            'docs/features/features/infrastructure.md',
        ],
        'output': 'docs/features/features/ai-ml-core.md',
        'title': 'AI & Machine Learning Core'
    },
    {
        'files': [
            'docs/features/features/latency.md',
            'docs/features/features/eta-accuracy.md',
            'docs/features/features/traffic-prediction-accuracy.md',
            'docs/features/features/nlu-intent-recognition.md',
            'docs/features/features/user-satisfaction-ai-features.md',
        ],
        'output': 'docs/features/features/ai-ml-metrics.md',
        'title': 'AI & ML Metrics'
    },
    
    # Data Management (7 files → 2)
    {
        'files': [
            'docs/features/features/data-import.md',
            'docs/features/features/ogc-services.md',
            'docs/features/features/tile-services.md',
        ],
        'output': 'docs/features/features/data-services.md',
        'title': 'Data Services & Standards'
    },
    {
        'files': [
            'docs/features/features/data-management.md',
            'docs/features/features/data-transformation.md',
            'docs/features/features/import-export.md',
        ],
        'output': 'docs/features/features/data-integration.md',
        'title': 'Data Integration & Management'
    },
    
    # GIS Analysis (5 files → 1)
    {
        'files': [
            'docs/features/features/spatial-analysis.md',
            'docs/features/features/network-analysis.md',
            'docs/features/features/topology.md',
            'docs/features/features/geoprocessing.md',
            'docs/features/features/terrain-analysis.md',
            'docs/features/verticals/terrain-elevation.md',
        ],
        'output': 'docs/features/features/gis-analysis.md',
        'title': 'GIS Analysis & Geoprocessing'
    },
    
    # Security (5 files → 2)
    {
        'files': [
            'docs/features/features/security.md',
            'docs/features/features/security-oauth2.md',
        ],
        'output': 'docs/features/features/security-core.md',
        'title': 'Security Core'
    },
    {
        'files': [
            'docs/features/features/admin.md',
            'docs/features/features/configuration.md',
            'docs/features/advanced/security-governance.md',
        ],
        'output': 'docs/features/features/security-admin.md',
        'title': 'Security Administration & Governance'
    },
    
    # Vietnam (8 files → 4)
    {
        'files': [
            'docs/features/vietnam/vietnam-localization.md',
            'docs/features/vietnam/vietnam-culture.md',
        ],
        'output': 'docs/features/vietnam/vietnam-localization.md',
        'title': 'Vietnam Localization & Culture'
    },
    {
        'files': [
            'docs/features/vietnam/vietnam-business.md',
            'docs/features/vietnam/vietnam-smart-city.md',
        ],
        'output': 'docs/features/vietnam/vietnam-business.md',
        'title': 'Vietnam Business & Smart City'
    },
    {
        'files': [
            'docs/features/vietnam/vietnam-transportation.md',
            'docs/features/vietnam/vietnam-weather.md',
        ],
        'output': 'docs/features/vietnam/vietnam-services.md',
        'title': 'Vietnam Transportation & Weather'
    },
    
    # Misc tiny files
    {
        'files': [
            'docs/features/features/metric.md',
            'docs/features/features/requirement.md',
            'docs/features/features/action.md',
            'docs/features/features/feature.md',
        ],
        'output': 'docs/features/features/misc-metadata.md',
        'title': 'Miscellaneous Metadata'
    },
]

print("=" * 80)
print("CONSOLIDATING FEATURE GROUP FILES")
print("=" * 80)

total_created = 0
total_features = 0

for consolidation in consolidations:
    features = merge_files(
        consolidation['files'],
        consolidation['output'],
        consolidation['title']
    )
    if features > 0:
        total_created += 1
        total_features += features

print("\n" + "=" * 80)
print(f"✅ COMPLETE: Created {total_created} consolidated files with {total_features} features")
print("=" * 80)
