+++
date = '2024-11-05T02:35:09+08:00'
title = 'P4 超搞剛 - Symbolic Link'
+++

# P4 超搞剛 - Symbolic Link

在一般我們使用 P4 當中的 tutorials 文件時，都可以正常使用 `make run` 這個指令，但當我們離開這個資料夾之後，會發現這個 `make run` 這個指令會變得沒有用，原因通常都是:

```bash!=
Makefile:4: ../../utils/Makefile: No such file or directory
make: *** No rule to make target '../../utils/Makefile'.  Stop
```

這個問題代表 MakeFile 找不到，所以無法執行 `make run` ，因此我們要想個辦法。
解決這個問題的辦法之一是利用 symbolic link（符號連結），來建立所需的路徑，讓系統找到目標 `Makefile`，而無需修改現有的專案結構。

## 使用 Symbolic Link 解決 Makefile 缺失問題

透過建立 symbolic link，可以指向現有的 Makefile，並解決「找不到檔案」的問題。這種方法相當靈活，可以在保持原專案目錄結構的情況下修復路徑問題。

### 步驟

1. **確認有效的 Makefile 路徑**：首先，找到一份可用的 Makefile，一般是在專案其他路徑下或相關的資料夾中。

2. **切換到預期目錄**：進入 `make` 指令所期望的目錄，例如 `../../utils/`

3. **建立符號連結**：使用 `ln -s` 指令來建立符號連結，語法如下：

   ```bash
   ln -s /path/to/existing/Makefile Makefile
   ```

   例如，如果你的有效 Makefile 位於 `/home/p4/tutorials/utils`，可以執行以下指令：

   ```bash
   ln -s /path/to/project/utils ../../utils
   ```

4. **確認符號連結**：創建連結後，使用以下指令檢查是否指向正確的 Makefile：

   ```bash
   ls -l ../../utils/Makefile
   ```

   如果有的話，會看到 Linux 回覆一個 `w-r-- 1` ... 或類似的回應，代表 Linux 有找到這個檔案，這樣就可以繼續使用 `make run` 了

5. **額外問題**

   ```bash!=
   - ERROR! While parsing input runtime configuration: file does not exist /home/p4/Desktop/tutorials/basic/build/basic.p4.p4info.txtpb
   Configuring switch s2 using P4Runtime with file pod-topo/s2-runtime.json
   - ERROR! While parsing input runtime configuration: file does not exist /home/p4/Desktop/tutorials/basic/build/basic.p4.p4info.txtpb
   Configuring switch s3 using P4Runtime with file pod-topo/s3-runtime.json
   - ERROR! While parsing input runtime configuration: file does not exist /home/p4/Desktop/tutorials/basic/build/basic.p4.p4info.txtpb
   Configuring switch s4 using P4Runtime with file pod-topo/s4-runtime.json
   - ERROR! While parsing input runtime configuration: file does not exist /home/p4/Desktop/tutorials/basic/build/basic.p4.p4info.txtpb
   ```

   這個問題可能由於檔案名稱或路徑配置錯誤。以下是幾個解決方法來修正這個錯誤：

   1. 檢查並重試編譯參數 (打底下參數就對了，p4 叫啥名字就自己改名)

   ```bash!=
   p4c-bm2-ss --p4v 16 --p4runtime-files build/basic.p4.p4info.txt -o build/basic.json basic.p4
   ```

   2. 更新配置文件使用 `.txt` 格式
      確保所有指向 `p4info` 文件的配置文件都使用 `.txt` 後綴，例如 `pod-topo/s1-runtime.json` 中的路徑更新為 `build/basic.p4.p4info.txt`。

   3. 再次運行 `make run`
      當文件生成後，請再次執行 `make run`，以檢查是否可以順利運行並成功配置交換機。

   這些步驟應該可以解決 `.txtpb` 格式無法識別的問題，並讓編譯器成功生成 `p4runtime` 文件。
