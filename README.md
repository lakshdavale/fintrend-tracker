# 📊 FinTrend Tracker

**FinTrend Tracker** is an intelligent Python tool that tracks what’s trending across:
- 🪙 Crypto (BTC, ETH, DOGE, PEPE...)
- 📈 Stocks (NIFTY, TCS, ADANI, TESLA...)
- 🛢 Commodities (GOLD, OIL, SILVER...)

It uses real-time **news scraping** + **X (Twitter) trends** to calculate a **Trend Score** for each asset.

---

## 🚀 Features

- ✅ Scrapes latest headlines from crypto & finance news sites
- ✅ Tracks Twitter mentions using `snscrape`
- ✅ Matches keywords like BTC, ETH, NIFTY, GOLD, etc.
- ✅ Combines data to show **top trending assets**
- ✅ 100% Open-source and beginner-friendly

---

## 🧠 How Trend Score Works

```text
Trend Score = (News Count × 2) + Tweet Count
