#!/usr/bin/env python3
"""
Feature Name Translation Script
Translates Vietnamese feature names to English while preserving Vietnamese descriptions
"""

import re
import sys

# Comprehensive translation dictionary
TRANSLATIONS = {
    # Actions
    "Bật/tắt": "Toggle",
    "Bật tắt": "Toggle",
    "Chuyển đổi": "Switch",
    "Chuyển": "Switch",
    "Hiển thị": "Display",
    "Xem": "View",
    "Tìm kiếm": "Search",
    "Tìm": "Find",
    "Chỉnh sửa": "Edit",
    "Sửa": "Edit",
    "Thêm": "Add",
    "Xóa": "Delete",
    "Lưu": "Save",
    "Tải": "Load",
    "Xuất": "Export",
    "Nhập": "Import",
    "Chia sẻ": "Share",
    "Sao chép": "Copy",
    "Chọn": "Select",
    "Phóng to": "Zoom In",
    "Thu nhỏ": "Zoom Out",
    "Xoay": "Rotate",
    "Nghiêng": "Tilt",
    "Di chuyển": "Move",
    "Quản lý": "Manage",
    "Điều khiển": "Control",
    "Cấu hình": "Configure",
    "Cài đặt": "Settings",
    "Tùy chỉnh": "Customize",
    "Đo": "Measure",
    "Vẽ": "Draw",
    "Ghi chú": "Annotate",
    
    # Nouns - Map/Layer
    "Bản đồ": "Map",
    "Layer": "Layer",
    "Lớp": "Layer",
    "Basemap": "Basemap",
    "Bản đồ nền": "Basemap",
    "Style": "Style",
    "Giao diện": "Interface",
    "Chủ đề": "Theme",
    "Màu sắc": "Color",
    "Độ trong suốt": "Opacity",
    "Thứ tự": "Order",
    "Danh mục": "Catalog",
    "Nhóm": "Group",
    "Yêu thích": "Favorites",
    
    # Nouns - 3D/Camera
    "Camera": "Camera",
    "Góc nhìn": "View",
    "3D": "3D",
    "2D": "2D",
    "Mô hình": "Model",
    "Terrain": "Terrain",
    "Địa hình": "Terrain",
    "Ánh sáng": "Lighting",
    "Bóng đổ": "Shadow",
    "Độ cao": "Elevation",
    "Chiều cao": "Height",
    
    # Nouns - Navigation
    "Chỉ đường": "Navigation",
    "Dẫn đường": "Routing",
    "Tuyến đường": "Route",
    "Lộ trình": "Route",
    "Điểm đến": "Destination",
    "Điểm xuất phát": "Origin",
    "Khoảng cách": "Distance",
    "Diện tích": "Area",
    
    # Nouns - Search
    "Địa điểm": "Location",
    "Địa chỉ": "Address",
    "Tọa độ": "Coordinates",
    "POI": "POI",
    "Vị trí": "Position",
    
    # Nouns - Data
    "Dữ liệu": "Data",
    "Thông tin": "Information",
    "Thuộc tính": "Attributes",
    "Metadata": "Metadata",
    "API": "API",
    
    # Nouns - User
    "Người dùng": "User",
    "Tài khoản": "Account",
    "Quyền": "Permission",
    "Nhóm quyền": "Permission Group",
    
    # Features
    "Tính năng": "Feature",
    "Công cụ": "Tool",
    "Bảng điều khiển": "Dashboard",
    "Panel": "Panel",
    "Bảng": "Panel",
    
    # Descriptions
    "Quản lý và điều khiển": "",  # Remove verbose prefix
    "Tính năng": "",  # Remove redundant prefix
    "Điều khiển camera cho": "",  # Remove camera prefix
}

def translate_feature_name(vietnamese_name):
    """Translate a Vietnamese feature name to English"""
    
    # If already in English (contains no Vietnamese chars), return as-is
    if not re.search(r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ]', vietnamese_name, re.IGNORECASE):
        return vietnamese_name.strip()
    
    result = vietnamese_name
    
    # Apply translations
    for vn, en in TRANSLATIONS.items():
        if vn in result:
            result = result.replace(vn, en)
    
    # Clean up
    result = result.strip()
    result = re.sub(r'\s+', ' ', result)  # Remove extra spaces
    result = re.sub(r'^\s*-\s*', '', result)  # Remove leading dash
    
    # If translation failed (still contains Vietnamese), flag it
    if re.search(r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ]', result, re.IGNORECASE):
        return f"[TRANSLATE] {vietnamese_name}"
    
    return result

def translate_file(input_path, output_path=None):
    """Translate feature names in a markdown file"""
    
    if output_path is None:
        output_path = input_path
    
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    translated_lines = []
    stats = {'total': 0, 'translated': 0, 'failed': 0}
    
    for line in lines:
        # Check if this is a feature row (starts with |, not header)
        if line.startswith('|') and 'Feature Group' not in line and 'Feature Name' not in line:
            parts = line.split('|')
            if len(parts) >= 3:
                # Translate only the Feature Name column (index 2)
                original_name = parts[2].strip()
                if original_name and original_name != '---':
                    stats['total'] += 1
                    translated_name = translate_feature_name(original_name)
                    
                    if '[TRANSLATE]' in translated_name:
                        stats['failed'] += 1
                    else:
                        stats['translated'] += 1
                    
                    parts[2] = f" {translated_name} "
                    line = '|'.join(parts)
        
        translated_lines.append(line)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(translated_lines)
    
    return stats

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 translate_features.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file
    
    stats = translate_file(input_file, output_file)
    print(f"Translation complete:")
    print(f"  Total features: {stats['total']}")
    print(f"  Translated: {stats['translated']}")
    print(f"  Failed: {stats['failed']}")
