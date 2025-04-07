from mcp.server.fastmcp import FastMCP
import os
import requests

mcp = FastMCP("google_search")


# ── ツールの定義 ──
@mcp.tool(
    name="google_web_search",
    description="Google検索APIを使用してウェブ検索を実行します。一般的なクエリ、ニュース、記事、オンラインコンテンツに最適です。幅広い情報収集、最近のイベント、または多様なウェブソースが必要な場合に使用してください。リクエストごとに最大20件の結果を表示し、ページネーション用のオフセットを提供します。",
)
def google_search(query: str, count=10, offset=0):
    # パラメータのバリデーション（最大値のチェック）
    count = min(count, 20)
    offset = min(offset, 9)

    # APIキーと検索エンジンID（cx）を環境変数から取得
    api_key = os.environ.get("GOOGLE_API_KEY")
    cx = os.environ.get("GOOGLE_SEARCH_ENGINE_ID")

    # 環境変数が設定されていない場合のエラーチェック
    if not api_key or not cx:
        raise ValueError(
            "環境変数 GOOGLE_API_KEY または GOOGLE_SEARCH_ENGINE_ID が設定されていません"
        )

    # Google Custom Search APIのstartパラメータは1-indexedなので計算する
    start_index = offset * count + 1

    # リクエストURLとパラメータ
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": api_key, "cx": cx, "q": query, "num": count, "start": start_index}

    response = requests.get(url, params=params)
    response.raise_for_status()  # エラーがあれば例外を発生
    return response.json()


# サーバーの起動
if __name__ == "__main__":
    # 標準入出力 (stdio) トランスポートで MCP サーバーを実行
    mcp.run(transport="stdio")
