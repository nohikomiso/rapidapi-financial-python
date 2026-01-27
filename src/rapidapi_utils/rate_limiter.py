import time
from datetime import datetime, timedelta
from collections import deque
import logging

logger = logging.getLogger(__name__)

class RapidAPIRateLimiter:
    """
    RapidAPIの共通ヘッダーとスライディング・ウィンドウ方式を組み合わせたレート制限管理クラス。
    """
    def __init__(self, max_requests_per_window=5, window_seconds=60, min_interval=13):
        self.max_requests_per_window = max_requests_per_window
        self.window_seconds = window_seconds
        self.min_interval = min_interval
        self.request_times = deque()
        self.last_request_time = None
        self.safety_margin = 5  # 秒

    def wait_before_request(self):
        """リクエストを送信する前に、制限に達していないか確認し必要に応じて待機する"""
        now = datetime.now()

        # 1. 最小間隔のチェック (リクエストの均等分散)
        if self.last_request_time:
            elapsed = (now - self.last_request_time).total_seconds()
            if elapsed < self.min_interval:
                wait_time = self.min_interval - elapsed
                logger.debug(f"Interval wait: {wait_time:.2f}s")
                time.sleep(wait_time)
                now = datetime.now()

        # 2. スライディング・ウィンドウのチェック
        while self.request_times and (now - self.request_times[0]) > timedelta(seconds=self.window_seconds):
            self.request_times.popleft()

        if len(self.request_times) >= self.max_requests_per_window:
            oldest_request = self.request_times[0]
            wait_seconds = (oldest_request + timedelta(seconds=self.window_seconds + self.safety_margin) - now).total_seconds()
            
            if wait_seconds > 0:
                logger.warning(f"Rate limit window full. Waiting {wait_seconds:.2f}s...")
                time.sleep(wait_seconds)
                # 再帰的に再チェック
                self.wait_before_request()
                return

        self.last_request_time = datetime.now()
        self.request_times.append(self.last_request_time)

    def update_from_headers(self, headers, status_code=200):
        """
        レスポンスヘッダーとステータスコードから最新の制限情報を取得し、必要に応じて待機する。
        バックオフ待機が発生した場合は True を返す。
        """
        if status_code == 429:
            wait_time = 65
            logger.warning(f"Status 429 detected. Backing off for {wait_time}s...")
            time.sleep(wait_time)
            self.request_times.clear()
            return True

        remaining = headers.get('x-ratelimit-requests-remaining')
        reset = headers.get('x-ratelimit-requests-reset')

        if remaining is not None:
            remaining = int(remaining)
            if remaining <= 0:
                wait_seconds = int(reset) if reset else 60
                wait_seconds += self.safety_margin
                logger.warning(f"RapidAPI quota exhausted. Waiting {wait_seconds}s for reset...")
                time.sleep(wait_seconds)
                # 待機後はスライディングウィンドウをクリアしてリフレッシュ
                self.request_times.clear()
                return True
        return False
