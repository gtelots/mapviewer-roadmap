# Foundation Features
> Advanced features and implementation details for foundation features.

| Feature Group | Feature Name | Short Description | Detailed Description | Why This Feature is Needed | Implementation Phase |
|--------------|--------------|------------|----------------|---------------------------|---------------------|
| 3D Scene & 3D Tiles | 3D Mode Toggle | Chuyển 2D↔3D mượt | Chuyển 2D↔3D mượt | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 3D Scene & 3D Tiles | 3D Tileset Loader | Tải tileset 3D Tiles theo ID/URL | Tải tileset 3D Tiles theo ID/URL | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 3D Scene & 3D Tiles | 3D Feature Picking | Click đối tượng 3D để nhận diện/thông tin | Click đối tượng 3D để nhận diện/thông tin | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 3D Scene & 3D Tiles | 3D Tiles Cache Control | Quản lý cache tile (kích thước, eviction). | Quản lý cache tile (kích thước, eviction). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Core | Deep link boostrap | Khởi tạo trạng thái Viewer từ URL (camera, layers, tools,. | Khởi tạo trạng thái Viewer từ URL (camera, layers, tools,...) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core | Config remote fetch | Lấy cấu hình viewer từ dịch vụ cấu hình (remote config) | Lấy cấu hình viewer từ dịch vụ cấu hình (remote config) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core | Startup State Presets | Áp dụng trạng thái khởi động mặc định: camera, layer, UI | Áp dụng trạng thái khởi động mặc định: camera, layer, UI | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core | State Persistence | Lưu trạng thái gần nhất (chế độ xem vệ tinh, light mode,. | Lưu trạng thái gần nhất (chế độ xem vệ tinh, light mode,...) hoặc đang thao tác -> URL Hash | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core | Feature flags | Bật/tắt tính năng bằng cờ cấu hình | Bật/tắt tính năng bằng cờ cấu hình | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | 3D Tileset Loader | Tính năng 3d tileset loader | Tính năng 3d tileset loader | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | LOD Selection | Tính năng lod selection | Tính năng lod selection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Frustum Culling | Tính năng frustum culling | Tính năng frustum culling | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Occlusion Culling Basic | Tính năng occlusion culling basic | Tính năng occlusion culling basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Cache (Memory) | Tính năng tile cache (memory) | Tính năng tile cache (memory) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Cache (Disk) | Tính năng tile cache (disk) | Tính năng tile cache (disk) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Request Concurrency Limit | Tính năng request concurrency limit | Tính năng request concurrency limit | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Request Priority Queue | Tính năng request priority queue | Tính năng request priority queue | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Progressive Refinement | Tính năng progressive refinement | Tính năng progressive refinement | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Loading Indicator | Tính năng tile loading indicator | Tính năng tile loading indicator | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Bounds Visualization | Tính năng tileset bounds visualization | Tính năng tileset bounds visualization | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Error Handling | Tính năng tile error handling | Tính năng tile error handling | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Retry with Backoff | Tính năng tile retry with backoff | Tính năng tile retry with backoff | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Gzip/Brotli Support | Tính năng gzip/brotli support | Tính năng gzip/brotli support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Draco/meshopt Decode | Tính năng draco/meshopt decode | Tính năng draco/meshopt decode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | KTX2/Basis Texture | Tính năng ktx2/basis texture | Tính năng ktx2/basis texture | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Content Type Support | Tính năng tile content type support | Tính năng tile content type support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Point Cloud Rendering Basic | Tính năng point cloud rendering basic | Tính năng point cloud rendering basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Instanced Models Basic | Tính năng instanced models basic | Tính năng instanced models basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Material Pipeline | Tính năng tile material pipeline | Tính năng tile material pipeline | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Lighting per Tileset | Tính năng lighting per tileset | Tính năng lighting per tileset | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Clipping Planes | Tính năng tileset clipping planes | Tính năng tileset clipping planes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Transforms | Tính năng tileset transforms | Tính năng tileset transforms | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Height Correction | Tính năng tileset height correction | Tính năng tileset height correction | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Shadow Receiver/ കാസter | Tính năng tileset shadow receiver/ കാസter | Tính năng tileset shadow receiver/ കാസter | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Picking Enable | Tính năng tileset picking enable | Tính năng tileset picking enable | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Feature Metadata Support | Tính năng tileset feature metadata support | Tính năng tileset feature metadata support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Style by Metadata | Tính năng tileset style by metadata | Tính năng tileset style by metadata | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Temporal Loading Guard | Tính năng tileset temporal loading guard | Tính năng tileset temporal loading guard | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Unload Policy | Tính năng tile unload policy | Tính năng tile unload policy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Memory Budget Manager | Tính năng memory budget manager | Tính năng memory budget manager | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Request Cancellation | Tính năng tile request cancellation | Tính năng tile request cancellation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | HTTP/2 Friendly Batching | Tính năng http/2 friendly batching | Tính năng http/2 friendly batching | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | CDN Cache Key Strategy | Tính năng cdn cache key strategy | Tính năng cdn cache key strategy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Signed URL Support | Tính năng signed url support | Tính năng signed url support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Multi-Origin Support | Tính năng tileset multi-origin support | Tính năng tileset multi-origin support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Prewarming | Tính năng tileset prewarming | Tính năng tileset prewarming | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Streaming Metrics | Tính năng tileset streaming metrics | Tính năng tileset streaming metrics | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Fallback LOD | Tính năng tileset fallback lod | Tính năng tileset fallback lod | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Versioned Manifest | Tính năng tileset versioned manifest | Tính năng tileset versioned manifest | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Multi-Tileset Orchestrator | Tính năng multi-tileset orchestrator | Tính năng multi-tileset orchestrator | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Dependency Graph | Tính năng tileset dependency graph | Tính năng tileset dependency graph | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Region-of-Interest | Tính năng tileset region-of-interest | Tính năng tileset region-of-interest | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tileset Throttling on Tab Hidden | Tính năng tileset throttling on tab hidden | Tính năng tileset throttling on tab hidden | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Background Decode Worker | Tính năng background decode worker | Tính năng background decode worker | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | GPU Instancing Optimization | Tính năng gpu instancing optimization | Tính năng gpu instancing optimization | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Hotspot Detection | Tính năng tile hotspot detection | Tính năng tile hotspot detection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Integrity Check | Tính năng tile integrity check | Tính năng tile integrity check | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Tile Progressive Texture | Tính năng tile progressive texture | Tính năng tile progressive texture | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - 3D Tiles Streaming | Multi-Resolution Terrain Tiles | Tính năng multi-resolution terrain tiles | Tính năng multi-resolution terrain tiles | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | App Init Config | Tính năng app init config | Tính năng app init config | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Environment Profiles | Tính năng environment profiles | Tính năng environment profiles | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Responsive Layout Engine | Tính năng responsive layout engine | Tính năng responsive layout engine | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | App State Store | Tính năng app state store | Tính năng app state store | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Deep Link Router | Tính năng deep link router | Tính năng deep link router | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Session Persistence | Tính năng session persistence | Tính năng session persistence | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Feature Flags | Tính năng feature flags | Tính năng feature flags | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Theme System | Tính năng theme system | Tính năng theme system | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Keyboard Shortcuts Core | Tính năng keyboard shortcuts core | Tính năng keyboard shortcuts core | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Help & Onboarding | Tính năng help & onboarding | Tính năng help & onboarding | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Error Boundary UI | Tính năng error boundary ui | Tính năng error boundary ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Loading Skeleton | Tính năng loading skeleton | Tính năng loading skeleton | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Network Retry Policy | Tính năng network retry policy | Tính năng network retry policy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Offline Detection | Tính năng offline detection | Tính năng offline detection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Telemetry Consent | Tính năng telemetry consent | Tính năng telemetry consent | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Basic Audit Trail (Client) | Tính năng basic audit trail (client) | Tính năng basic audit trail (client) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Resource Preload | Tính năng resource preload | Tính năng resource preload | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | CDN Asset Support | Tính năng cdn asset support | Tính năng cdn asset support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Multi-Tab Safety | Tính năng multi-tab safety | Tính năng multi-tab safety | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Localization Bootstrap | Tính năng localization bootstrap | Tính năng localization bootstrap | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Date/Time Utilities | Tính năng date/time utilities | Tính năng date/time utilities | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Permission Gate UI | Tính năng permission gate ui | Tính năng permission gate ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Rate Limit Friendly UI | Tính năng rate limit friendly ui | Tính năng rate limit friendly ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Client Cache Control | Tính năng client cache control | Tính năng client cache control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Config Validation | Tính năng config validation | Tính năng config validation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Dependency Health Check | Tính năng dependency health check | Tính năng dependency health check | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Security Headers Readiness | Tính năng bảo mật và kiểm soát truy cập | Tính năng bảo mật và kiểm soát truy cập | Tăng cường bảo mật và tuân thủ quy định | Phase 1 |
| Foundation - App Shell | CORS Preflight Optimizer | Tính năng cors preflight optimizer | Tính năng cors preflight optimizer | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Version Badge & Build Info | Tính năng version badge & build info | Tính năng version badge & build info | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Changelog Notifier | Tính năng changelog notifier | Tính năng changelog notifier | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | API Key Input Modes | Tính năng api key input modes | Tính năng api key input modes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Token Refresh Hook | Tính năng token refresh hook | Tính năng token refresh hook | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Secure Storage Wrapper | Tính năng secure storage wrapper | Tính năng secure storage wrapper | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Content Sanitization | Tính năng content sanitization | Tính năng content sanitization | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Crash Recovery Mode | Tính năng crash recovery mode | Tính năng crash recovery mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Config Override UI UI | Tính năng config override ui ui | Tính năng config override ui ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Startup Performance Budget | Tính năng startup performance budget | Tính năng startup performance budget | Cải thiện hiệu suất và trải nghiệm người dùng | Phase 1 |
| Foundation - App Shell | Accessibility Baseline | Tính năng accessibility baseline | Tính năng accessibility baseline | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Cookie/Storage Policy Banner | Tính năng cookie/storage policy banner | Tính năng cookie/storage policy banner | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - App Shell | Multi-Project Switcher | Tính năng multi-project switcher | Tính năng multi-project switcher | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Click Select Basics | Tính năng click select basics | Tính năng click select basics | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Hover Highlight | Tính năng hover highlight | Tính năng hover highlight | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Properties Panel | Tính năng properties panel | Tính năng properties panel | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Attribute Formatting | Tính năng attribute formatting | Tính năng attribute formatting | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Copy Attribute | Tính năng copy attribute | Tính năng copy attribute | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Feature Locate Button | Tính năng feature locate button | Tính năng feature locate button | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Multi-Select Mode | Tính năng multi-select mode | Tính năng multi-select mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Selection Set Save | Tính năng selection set save | Tính năng selection set save | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Identify Across Layers | Quản lý và điều khiển identify across layers | Quản lý và điều khiển identify across layers | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Interaction & Identify | Pixel/World Tolerance Control | Tính năng pixel/world tolerance control | Tính năng pixel/world tolerance control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Orbit | Điều khiển camera cho camera orbit | Điều khiển camera cho camera orbit | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Pan | Điều khiển camera cho camera pan | Điều khiển camera cho camera pan | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Zoom | Điều khiển camera cho camera zoom | Điều khiển camera cho camera zoom | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Fly-To Position | Tính năng fly-to position | Tính năng fly-to position | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Home View | Tính năng home view | Tính năng home view | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Compass Widget | Tính năng compass widget | Tính năng compass widget | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Pitch Controls | Tính năng pitch controls | Tính năng pitch controls | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Inertia | Điều khiển camera cho camera inertia | Điều khiển camera cho camera inertia | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Collision | Điều khiển camera cho camera collision | Điều khiển camera cho camera collision | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Globe/Plane Mode | Tính năng globe/plane mode | Tính năng globe/plane mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Coordinate Display | Tính năng coordinate display | Tính năng coordinate display | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Scale Bar | Tính năng scale bar | Tính năng scale bar | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Minimap (Optional) | Tính năng minimap (optional) | Tính năng minimap (optional) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | North Lock Option | Tính năng north lock option | Tính năng north lock option | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Bookmarks | Điều khiển camera cho camera bookmarks | Điều khiển camera cho camera bookmarks | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Transition Presets | Điều khiển camera cho camera transition presets | Điều khiển camera cho camera transition presets | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Path Recording | Điều khiển camera cho camera path recording | Điều khiển camera cho camera path recording | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Path Playback | Điều khiển camera cho camera path playback | Điều khiển camera cho camera path playback | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Sync Multi-Views | Điều khiển camera cho camera sync multi-views | Điều khiển camera cho camera sync multi-views | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Split Screen Compare | Tính năng split screen compare | Tính năng split screen compare | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Field of View Control | Tính năng field of view control | Tính năng field of view control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Near/Far Plane Tuning | Tính năng near/far plane tuning | Tính năng near/far plane tuning | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Auto-Exposure (Basic) | Tính năng auto-exposure (basic) | Tính năng auto-exposure (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Frame Rate Cap | Tính năng frame rate cap | Tính năng frame rate cap | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Constraints by Area | Điều khiển camera cho camera constraints by area | Điều khiển camera cho camera constraints by area | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Terrain Exaggeration | Tính năng terrain exaggeration | Tính năng terrain exaggeration | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Terrain Toggle | Tính năng terrain toggle | Tính năng terrain toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Height Reference Modes | Tính năng height reference modes | Tính năng height reference modes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Sun & Time-of-Day Basic | Tính năng sun & time-of-day basic | Tính năng sun & time-of-day basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Shadow Toggle | Tính năng shadow toggle | Tính năng shadow toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Fog Control | Tính năng fog control | Tính năng fog control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Atmosphere Toggle | Tính năng atmosphere toggle | Tính năng atmosphere toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Ground Transparency | Tính năng ground transparency | Tính năng ground transparency | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Reset Orientation | Điều khiển camera cho camera reset orientation | Điều khiển camera cho camera reset orientation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Jump to Coordinates | Tính năng jump to coordinates | Tính năng jump to coordinates | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Speed Control | Điều khiển camera cho camera speed control | Điều khiển camera cho camera speed control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Touch Gesture Support | Tính năng touch gesture support | Tính năng touch gesture support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Double-Click FlyTo | Tính năng double-click flyto | Tính năng double-click flyto | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Focus on Selection | Điều khiển camera cho camera focus on selection | Điều khiển camera cho camera focus on selection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Auto-LOD Targeting | Tính năng auto-lod targeting | Tính năng auto-lod targeting | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Shake Guard | Điều khiển camera cho camera shake guard | Điều khiển camera cho camera shake guard | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | High Precision Mode | Tính năng high precision mode | Tính năng high precision mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Device Pixel Ratio Control | Tính năng device pixel ratio control | Tính năng device pixel ratio control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Screenshot Viewport Safe Area | Tính năng screenshot viewport safe area | Tính năng screenshot viewport safe area | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Presets by Role | Điều khiển camera cho camera presets by role | Điều khiển camera cho camera presets by role | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Kiosk Auto-Rotate | Tính năng kiosk auto-rotate | Tính năng kiosk auto-rotate | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Multi-Monitor Support | Tính năng multi-monitor support | Tính năng multi-monitor support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | VRAM Budget Indicator | Tính năng vram budget indicator | Tính năng vram budget indicator | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Roll Lock | Điều khiển camera cho camera roll lock | Điều khiển camera cho camera roll lock | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Smooth Stop | Điều khiển camera cho camera smooth stop | Điều khiển camera cho camera smooth stop | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Adaptive Input Sensitivity | Tính năng adaptive input sensitivity | Tính năng adaptive input sensitivity | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Teleport Mode | Điều khiển camera cho camera teleport mode | Điều khiển camera cho camera teleport mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Follow Object | Điều khiển camera cho camera follow object | Điều khiển camera cho camera follow object | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera LookAt Lock | Điều khiển camera cho camera lookat lock | Điều khiển camera cho camera lookat lock | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Safe Height Floor | Điều khiển camera cho camera safe height floor | Điều khiển camera cho camera safe height floor | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Navigation History | Điều khiển camera cho camera navigation history | Điều khiển camera cho camera navigation history | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Jump List | Điều khiển camera cho camera jump list | Điều khiển camera cho camera jump list | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Metrics Overlay | Điều khiển camera cho camera metrics overlay | Điều khiển camera cho camera metrics overlay | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera API Surface | Điều khiển camera cho camera api surface | Điều khiển camera cho camera api surface | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Events | Điều khiển camera cho camera events | Điều khiển camera cho camera events | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | View Frustum Debug | Tính năng view frustum debug | Tính năng view frustum debug | Hỗ trợ troubleshooting và phân tích vấn đề | Phase 1 |
| Foundation - Scene & Camera | Ground Clamp Sampling Mode | Tính năng ground clamp sampling mode | Tính năng ground clamp sampling mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Transition Interruptability | Tính năng transition interruptability | Tính năng transition interruptability | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Auto-Focus on Search | Điều khiển camera cho camera auto-focus on search | Điều khiển camera cho camera auto-focus on search | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Precision Cursor Height | Tính năng precision cursor height | Tính năng precision cursor height | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Scene Screenshot Thumbnail | Tính năng scene screenshot thumbnail | Tính năng scene screenshot thumbnail | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Cinematic DOF (Basic) | Tính năng cinematic dof (basic) | Tính năng cinematic dof (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Anti-Aliasing Toggle | Tính năng anti-aliasing toggle | Tính năng anti-aliasing toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Anisotropic Filtering Level | Tính năng anisotropic filtering level | Tính năng anisotropic filtering level | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Screenshot at Resolution | Tính năng screenshot at resolution | Tính năng screenshot at resolution | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Tutorial Mode | Điều khiển camera cho camera tutorial mode | Điều khiển camera cho camera tutorial mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Center-on-Map Click | Tính năng center-on-map click | Tính năng center-on-map click | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Auto-Leveling | Tính năng auto-leveling | Tính năng auto-leveling | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Safe Mode Rendering | Tính năng safe mode rendering | Tính năng safe mode rendering | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Boundary Snap | Điều khiển camera cho camera boundary snap | Điều khiển camera cho camera boundary snap | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Telemetry for Navigation | Tính năng telemetry for navigation | Tính năng telemetry for navigation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Viewport Ruler | Tính năng viewport ruler | Tính năng viewport ruler | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Night Mode Preset | Tính năng night mode preset | Tính năng night mode preset | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | High Contrast Scene Mode | Tính năng high contrast scene mode | Tính năng high contrast scene mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Scene & Camera | Camera Snapshot API | Điều khiển camera cho camera snapshot api | Điều khiển camera cho camera snapshot api | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Observability & Integrations | Webhook Triggers (Optional) | Kích hoạt webhook cho hành động quan trọng (optional). | Kích hoạt webhook cho hành động quan trọng (optional). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Adaptive Quality | Tự điều chỉnh chất lượng theo FPS/năng lực thiết bị. | Tự điều chỉnh chất lượng theo FPS/năng lực thiết bị. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Tile Request Concurrency Control | Giới hạn số request song song tránh nghẽn. | Giới hạn số request song song tránh nghẽn. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Progressive Loading | Tải thô trước, tinh dần để người dùng thấy nhanh. | Tải thô trước, tinh dần để người dùng thấy nhanh. | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Performance & Reliability | Cache Management UI | Xem/xóa cache để xử lý lỗi hiển thị. | Xem/xóa cache để xử lý lỗi hiển thị. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Network Resilience Mode | Chế độ tiết kiệm băng thông khi mạng yếu. | Chế độ tiết kiệm băng thông khi mạng yếu. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Error Boundary U | Màn hình lỗi thân thiện, có nút khôi phục. | Màn hình lỗi thân thiện, có nút khôi phục. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Offline Detection | Phát hiện offline và tạm dừng request hợp lý. | Phát hiện offline và tạm dừng request hợp lý. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Resource Budgeting | Giới hạn RAM, tự evict tile ít dùng. | Giới hạn RAM, tự evict tile ít dùng. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Performance & Reliability | Warm Start | Preload tile quanh điểm xuất phát để mở nhanh. | Preload tile quanh điểm xuất phát để mở nhanh. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Outdoor Routing | Tìm đường ngoài trời giữa A→B | Tìm đường ngoài trời giữa A→B | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Route Profiles | Hồ sơ tuyến: car/bike/walk/accessibility. | Hồ sơ tuyến: car/bike/walk/accessibility. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Avoid Options | Tùy chọn tránh: thu phí/cao tốc/cầu thang/khu hạn chế. | Tùy chọn tránh: thu phí/cao tốc/cầu thang/khu hạn chế. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Multi-Stop Routing | Thêm điểm dừng (via points), tối ưu thứ tự (optional). | Thêm điểm dừng (via points), tối ưu thứ tự (optional). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Routing & Navigation | Turn-by-Turn Steps | Danh sách hướng dẫn từng bước. | Danh sách hướng dẫn từng bước. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | OAuth2 Login (Auth Code + PKCE) | Đăng nhập an toàn theo OAuth2 với PKCE. | Đăng nhập an toàn theo OAuth2 với PKCE. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | Opaque Access Token Storage | Lưu access token dạng opaque an toàn, không “parse token”. | Lưu access token dạng opaque an toàn, không “parse token”. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | Token Revocation on Logout | Logout thì revoke token theo RFC 7009 (nếu bật). | Logout thì revoke token theo RFC 7009 (nếu bật). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | Cross-Tenant Isolation Guards | Ngăn request trộn tenant (đảm bảo isolation). | Ngăn request trộn tenant (đảm bảo isolation). | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Security & Privacy (OAuth2 Opaque Tokens) | PII Redaction in Logs | Loại PII khỏi log/telemetry phía client. | Loại PII khỏi log/telemetry phía client. | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Terrain & Elevation | Elevation Query | Truy vấn độ cao tại điểm người dùng click | Truy vấn độ cao tại điểm người dùng click | Nâng cao trải nghiệm và khả năng sử dụng cho người dùng | Phase 2 |
| Terrain & Elevation | Height Profile Tool | Biểu đồ cao độ theo tuyến (profile) | Biểu đồ cao độ theo tuyến (profile) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Hiển thị bản đồ hình cầu | Tính năng hiển thị bản đồ hình cầu | Tính năng hiển thị bản đồ hình cầu | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Bật, tắt lớp dữ liệu | Bật/ tắt lớp tình trạng kẹt xe, địa điểm (POI) | Bật/ tắt lớp tình trạng kẹt xe, địa điểm (POI) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Custom map button | Nút phóng to, thu nhỏ | Nút phóng to, thu nhỏ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Xoay trục Bắc bản đồ | Tính năng xoay trục bắc bản đồ | Tính năng xoay trục bắc bản đồ | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Vị trí của tôi | Tính năng vị trí của tôi | Tính năng vị trí của tôi | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | Sao chép vị trí | Tính năng sao chép vị trí | Tính năng sao chép vị trí | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Uncategory | None | Chia sẻ địa điểm | Chia sẻ địa điểm | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
