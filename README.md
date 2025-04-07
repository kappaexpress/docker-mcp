# docker imageビルドコマンド
```
docker build -f ./Dockerfile_playwright -t playwright-mcp .
```

# WindowsでのClaude Desktopでのmcpの設定
1. `C:\Users\{ユーザー名}\AppData\Roaming\Claude\claude_desktop_config.json`を開く
2. `claude_desktop_config.json`に以下を追記
```json
{
  "mcpServers": {
    "playwright": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "playwright-mcp"]
    }
  }
}
```
3. `claude_desktop_config.json`を保存
4. Claude Desktopを再起動