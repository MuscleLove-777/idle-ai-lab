"""放置ゲーム×AI自動化ラボ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "放置ゲーム×AI自動化ラボ"
BLOG_DESCRIPTION = "BlueStacks・Python・OpenCV・YOLO等で放置ゲームを自動化する技術メディア。エンジニア兼ゲーマー向けに、コード片・規約面の検討・VPS構成までを実践解説。"
BLOG_URL = "https://musclelove-777.github.io/idle-ai-lab/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/idle-ai-lab"

TARGET_CATEGORIES = [
    "PyAutoGUI 周回スクリプト",
    "OpenCV 画像認識",
    "YOLO 物体検出 in ゲーム",
    "BlueStacks マルチアカ運用",
    "VPS / 24時間放置運用",
    "規約・倫理ライン議論",
    "BOT検知回避と対策",
]

THEME = {
    "primary": "#0e2a4a",
    "accent": "#00d4ff",
    "gradient_start": "#0e2a4a",
    "gradient_end": "#00d4ff",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
