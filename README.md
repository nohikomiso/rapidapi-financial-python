# 📊 Alpha Vantage RapidAPI (Enhanced)

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[日本語](#-alpha-vantage-rapidapi-enhanced) | [English](#english-version)

---

**RapidAPI 経由で金融データを安定的に取得するための、レート制限への自動適応機能を備えた Python ライブラリ。**

## 🌟 主な特徴

- **レート制限への自動適応**: `X-RateLimit-*` ヘッダーをリアルタイムに監視し、プロバイダーの制限を遵守しながら効率的にリクエスト。
- **インテリジェント・バックオフ**: 429 エラーやボディ内の警告（`Burst pattern detected`等）を検知すると、自動で待機・リトライ。
- **バースト検知回避 (Jitter)**: リクエスト間隔にランダムなゆらぎを加え、機械的なパターンを排除。
- **クォータ（1日上限）管理**: 24時間の上限に達した際、正確な回復時刻を算出し、待機するか例外を投げて終了するかを選択可能。

## 🚀 クイックスタート

### インストール
```bash
uv add "git+https://github.com/nohikomiso/rapidapi-financial-python.git"
```

### 基本的な使い方
```python
from alpha_vantage.fundamentaldata import FundamentalData

# wait_on_quota_exhausted=False にすると、1日の上限到達時にスリープせず例外を投げます
fd = FundamentalData(key='YOUR_RAPIDAPI_KEY', rapidapi=True, wait_on_quota_exhausted=True)
data, meta_data = fd.get_earnings_quarterly('AAPL')
```

---

<div id="english-version"></div>

<details>
<summary><strong>🌐 Click here for English Version</strong></summary>

# 📊 Alpha Vantage RapidAPI (Enhanced)

**A Python library with automatic rate-limit adaptation for stable financial data acquisition via RapidAPI.**

## 🌟 Key Features

- **Automatic Rate-Limit Adaptation**: Monitors `X-RateLimit-*` headers in real-time to ensure efficient requests while respecting provider limits.
- **Intelligent Backoff**: Automatically waits and retries upon detecting 429 errors or in-body warnings (e.g., `Burst pattern detected`).
- **Burst Avoidance (Jitter)**: Adds random fluctuations to request intervals to eliminate mechanical patterns and stay under security filters.
- **Daily Quota Management**: When the 24-hour limit is reached, it calculates the exact recovery time. You can choose to either wait automatically or raise an exception.

## 🚀 Quick Start

### Installation
```bash
uv add "git+https://github.com/nohikomiso/rapidapi-financial-python.git"
```

### Basic Usage
```python
from alpha_vantage.fundamentaldata import FundamentalData

# Set wait_on_quota_exhausted=False to raise an exception instead of sleeping when the daily limit is hit.
fd = FundamentalData(key='YOUR_RAPIDAPI_KEY', rapidapi=True, wait_on_quota_exhausted=True)
data, meta_data = fd.get_earnings_quarterly('AAPL')
```

---

## 🛠️ For Developers

```bash
git clone https://github.com/nohikomiso/rapidapi-financial-python.git
cd rapidapi-financial-python
uv sync
```

## 🙏 Credits
This project is an enhanced version of the excellent [alpha_vantage (v3.0.0)](https://github.com/RomelTorres/alpha_vantage) by **Romel Torres**, with added automatic rate-limiting features for RapidAPI.

## 📄 License
[MIT License](LICENSE) - Copyright (c) 2017 Romel Torres / 2026 nohikomiso

</details>
