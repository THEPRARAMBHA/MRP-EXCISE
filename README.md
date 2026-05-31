# MRP Master Calculator — Maharashtra State Excise
## PWA — Progressive Web App

**For State Excise Maharashtra**  
31 Calculators · 7 Categories · Offline Support

---

### 🌐 Live URL
**https://[your-username].github.io/mrp-calculator/**

---

### 📱 Install as App
1. Open the live URL in Chrome on Android
2. Tap "Add to Home Screen" or use the "Install App" prompt
3. App works fully offline after first load

---

### 📁 Repository Structure
```
├── index.html          ← Main PWA app (all-in-one)
├── manifest.json       ← PWA manifest
├── sw.js               ← Service Worker (offline support)
├── icons/
│   ├── icon-72.png
│   ├── icon-96.png
│   ├── icon-128.png
│   ├── icon-144.png
│   ├── icon-152.png
│   ├── icon-192.png
│   ├── icon-384.png
│   ├── icon-512.png
│   └── icon-512-maskable.png   ← For Play Store
└── screenshots/
    └── screen1.png             ← For Play Store listing
```

---

### 🤖 Convert to APK (Play Store)

#### Option A: PWABuilder (Easiest — No coding)
1. Go to **https://www.pwabuilder.com**
2. Enter your GitHub Pages URL
3. Click **Build My PWA**
4. Download **Android APK / AAB**
5. Upload to Play Store

#### Option B: Bubblewrap (Google Official)
```bash
npm install -g @bubblewrap/cli
bubblewrap init --manifest https://[your-url]/manifest.json
bubblewrap build
```

---

### ⚠️ Disclaimer
This app is for **educational purposes only**.  
Not an official government application.

**Contact:** prarambhadigital@gmail.com  
**© 2026 The Prarambha Business Consultancy**
