# 📊 Alpha Vantage RapidAPI (Enhanced)

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/nohikomiso/rapidapi-financial-python/graphs/commit-activity)

**RapidAPI 経由で金融データを安定的に取得するための、レート制限への自動適応機能を備えた Python ライブラリ。**

---

## 🌟 主な特徴

- **レート制限への自動適応**: `X-RateLimit-*` ヘッダーをリアルタイムに監視し、プロバイダーの制限を遵守しながら効率的にリクエスト。
- **インテリジェント・バックオフ**: 429 エラーやボディ内の警告（`Burst pattern detected`等）を検知すると、API プロバイダーへの過負荷を避けるため自動で安全に待機・リトライ。
- **バースト検知回避 (Jitter)**: リクエスト間隔にランダムなゆらぎを加えることで、機械的な等間隔パターンを排除し、プロバイダー側のセキュリティフィルタ通過率を向上。
- **スライディング・ウィンドウ制御**: クライアント側でもリクエスト間隔を調整し、API サーバーに負荷をかけない均等分散を実現。
- **クォータ（1日上限）管理**: 24時間の上限に達した際、正確な回復時刻を算出し、待機するか例外を投げて終了するかを選択可能。
- **シンプルなシングルパッケージ**: 複雑なサブディレクトリ指定なしで、直ちにプロジェクトへ導入可能。

---

## 📦 含まれるモジュール

このライブラリをインストールすると、以下の2つの機能が利用可能になります。

- **`alpha_vantage`**: オリジナルの `alpha-vantage` ライブラリと互換性を保ちつつ、RapidAPI 用に強化された API ラッパー。
- **`rapidapi_utils`**: 他の RapidAPI にも応用可能な、共通レート制限管理ユーティリティ。

---

## 🚀 クイックスタート

### インストール

プロジェクトのディレクトリで以下のコマンドを実行してください。

```bash
uv add "git+https://github.com/nohikomiso/rapidapi-financial-python.git"
```

### 基本的な使い方

レート制限（無料枠：5回/分など）を気にせず、シンプルに呼び出すだけです。

```python
from alpha_vantage.fundamentaldata import FundamentalData

# ライブラリが裏側で自動的に待機と制限管理を行います
# wait_on_quota_exhausted=False にすると、1日の上限到達時にスリープせず例外を投げます
fd = FundamentalData(key='YOUR_RAPIDAPI_KEY', rapidapi=True, wait_on_quota_exhausted=True)
data, meta_data = fd.get_earnings_quarterly('AAPL')

print(data)
```

---

## 🛠️ 開発者向け情報

```bash
# クローンと依存関係の同期
git clone https://github.com/nohikomiso/rapidapi-financial-python.git
cd rapidapi-financial-python
uv sync
```

---

## 🙏 Credits (謝辞)

このプロジェクトは、**Romel Torres** 氏による素晴らしいライブラリ [alpha_vantage (v3.0.0)](https://github.com/RomelTorres/alpha_vantage) をベースに、RapidAPI 向けの自動制限回避機能を追加した強化版です。

---

## 📄 License

このプロジェクトは [MIT License](LICENSE) のもとで公開されています。
Copyright (c) 2017 Romel Torres / 2026 nohikomiso
