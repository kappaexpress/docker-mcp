FROM mcr.microsoft.com/playwright

RUN npm install -g @playwright/mcp@latest && npx playwright install chrome

ENTRYPOINT ["npx", "-y", "@playwright/mcp@latest", "--headless"]