#!/usr/bin/env python3
"""Standardize feature group names"""

import os
import re

# Rename mapping
RENAMES = {
    # Core
    'Core - Search & Geocoding': 'Search and Geocoding',
    'Core - Routing - Outdoor': 'Outdoor Routing',
    'Core - Measurement & Drawing': 'Measurement and Drawing',
    'Core - Sharing & Export': 'Sharing and Export',
    'Core - UI/UX & Accessibility': 'UI/UX and Accessibility',
    'Core - Indoor - Core': 'Indoor Core',
    
    # Foundation
    'Foundation - 3D Tiles Streaming': '3D Tiles Streaming',
    'Foundation - App Shell': 'App Shell',
    'Foundation - Interaction & Identify': 'Interaction and Identify',
    'Foundation - Scene & Camera': 'Scene and Camera',
    
    # Advanced/Expert
    'Advanced - Observability & Diagnostics': 'Advanced Observability and Diagnostics',
    'Advanced - Performance & Reliability': 'Advanced Performance and Reliability',
    'Advanced - Security & Governance': 'Advanced Security and Governance',
    'Advanced - Visualization & Styling': 'Advanced Visualization and Styling',
    'Expert - Enterprise Integrations': 'Expert Enterprise Integrations',
    'Expert - Immersive & AI': 'Expert Immersive and AI',
    'Expert - SDK & Extensibility': 'Expert SDK and Extensibility',
    
    # General (replace & with and, remove emojis)
    '2D Vector & Raster Rendering': '2D Vector and Raster Rendering',
    '3D Scene & 3D Tiles': '3D Scene and 3D Tiles',
    '3D Visualization 🆕': '3D Visualization',
    'Analytics & Reporting': 'Analytics and Reporting',
    'Annotations & Collaboration': 'Annotations and Collaboration',
    'Basemaps & Reference Layers': 'Basemaps and Reference Layers',
    'Camera & Navigation': 'Camera and Navigation',
    'Developer API 🆕': 'Developer API',
    'Drawing & Editing': 'Drawing and Editing',
    'Drone & UAV': 'Drone and UAV',
    'Identify & Query': 'Identify and Query',
    'Navigation & Routing 🆕': 'Navigation and Routing',
    'Observability & Integrations': 'Observability and Integrations',
    'Styling & Theming': 'Styling and Theming',
}

def standardize_file(filepath):
    """Standardize feature group names in a file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Replace in content
    for old_name, new_name in RENAMES.items():
        if old_name in content:
            content = content.replace(old_name, new_name)
            changes.append(f"{old_name} → {new_name}")
    
    # Write back if changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return []

print("=" * 80)
print("STANDARDIZING FEATURE GROUP NAMES")
print("=" * 80)

# Process all feature files
total_changes = 0
files_changed = 0

for folder in ['core', 'foundation', 'features', 'advanced', 'vietnam', 'verticals']:
    folder_path = f'docs/features/{folder}'
    if not os.path.exists(folder_path):
        continue
    
    for file in os.listdir(folder_path):
        if file.endswith('.md') and file != 'README.md':
            filepath = os.path.join(folder_path, file)
            changes = standardize_file(filepath)
            if changes:
                total_changes += len(changes)
                files_changed += 1
                print(f"\n✅ {folder}/{file}:")
                for change in changes:
                    print(f"   {change}")

print("\n" + "=" * 80)
print(f"✅ COMPLETE: {total_changes} renames in {files_changed} files")
print("=" * 80)
