+++
date = '2024-11-13T02:44:10+08:00'
title = 'Disable auto-formatting for Hugo templates in VS Code'
categories = [
    "Hugo", "Visual Studio Code"
]
+++

**這篇文章由 AI 自動產生，尚未經過整理**


# 禁用 VS Code 中 Hugo 模板的自動格式化

如果你在使用 Visual Studio Code 時，因為自動格式化功能而失去在 Hugo 模板檔案中精心排列的縮排，感到困擾，那你並不孤單。這裡有一個簡單的指南，可以幫助你停止這種情況，並保留你想要的格式。

---

## 問題

在處理 Hugo 模板時，自動格式化可能會移除縮排，使代碼變得不易閱讀。例如：

### 輸入：
```handlebars
{{ range ... }}
   {{ if .... }}
      {{if ... }}
          <tag></tag>
      {{end}}
   {{end}}
{{end}}
```

### 自動格式化後的輸出：
```handlebars
{{ range ... }}
{{ if .... }}
{{if ... }}
<tag></tag>
{{end}}
{{end}}
{{end}}
```

這種行為會使得複雜的模板變得難以閱讀和維護。為了解決這個問題，你可以專門為 Handlebars 文件禁用自動格式化。

---

## 解決方案

### 在 VS Code 中禁用 Handlebars 的自動格式化

你可以關閉 Handlebars 文件的自動格式化，同時保留對其他檔案類型的自動格式化。

#### 步驟：
1. 打開 VS Code 的設定：
   - 點擊 **檔案 > 偏好設定 > 設定**（或在 Mac 上點擊 **Code > 偏好設定 > 設定**）。
   - 或者，按 `Ctrl + ,`（Windows/Linux）或 `Cmd + ,`（Mac）。
2. 搜尋 `editor.formatOnSave` 並為特定檔案禁用它，通過在 `settings.json` 中加入以下配置：

3. 在 `settings.json` 檔案中加入以下設定：

   ```json
   "[handlebars]": {
     "editor.formatOnSave": false
   }
   ```

   此設定確保對於 `.hbs` 或 `.handlebars` 擴展名的 Handlebars 檔案，會禁用自動格式化。

   ![圖1](/logddd.png)