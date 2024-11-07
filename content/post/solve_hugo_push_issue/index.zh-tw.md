+++
date = '2024-11-07T18:51:21+08:00'
title = 'Solve hugo push issue'
+++

# 解決 Hugo 部署失敗的問題：本機正常但 GitHub 無法顯示

使用 Hugo 建立靜態網站時，有時可能會遇到這樣的情況：在本機使用 `hugo server` 測試時一切正常，但部署到 GitHub Pages 上後，網站卻出現錯誤或無法正確顯示。本文將說明這個問題的可能原因，並提供簡單的解決方法。

---

## 問題表現方式

- 在本機使用 `hugo server` 指令時，網站可以正常運行，所有內容正確顯示。
- 將網站的內容推送（push）到 GitHub 後，部署的網站卻出現問題：
  - 網頁完全無法出現

---

## 問題原因分析

這種情況可能與 Hugo 在生成靜態網站時未正確清理輸出目錄有關。Hugo 預設會將生成的檔案輸出到 `public` 目錄，如果該目錄中存在殘留的舊檔案，這些檔案可能會被推送到 GitHub，導致部署的網站出現問題。

---

## 解決方法

要解決這個問題，可以嘗試以下步驟：

1. **清理輸出目錄並重新生成網站**
   使用 `hugo --cleanDestinationDir` 指令，這會在生成靜態網站時自動清理輸出目錄，確保僅保留最新的檔案。

   ```bash
   hugo --cleanDestinationDir
   ```

   此指令確保 `public` 目錄中的舊檔案被移除，避免部署過時或衝突的資源。

2. **重新部署到 GitHub**
   在執行清理和重新生成後，將更新後的檔案推送到 GitHub：

   ```bash
   git add .
   git commit -m "Fix deployment issue"
   git push origin main
   ```

3. **檢查部署狀況**
   完成推送後，檢查 GitHub Pages 部署狀態，確認網站是否恢復正常。

---

## 小結

當你遇到 Hugo 部署失敗的情況時，使用 `hugo --cleanDestinationDir` 清理輸出目錄是一個快速有效的解決方案。這能避免舊檔案干擾新內容的部署。如果問題仍然存在，建議檢查 GitHub Pages 的設定或 Hugo 配置檔案，確保兩者的相容性。

希望這篇文章能幫助你順利解決 Hugo 部署的問題，讓你的網站順利上線！🚀
