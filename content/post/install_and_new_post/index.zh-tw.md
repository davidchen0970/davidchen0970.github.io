+++
date = '2025-08-10T09:38:12+08:00'
title = 'Install and create new post'
image = "pawel-czerwinski-OR-7nSsMxWA-unsplash.jpg"
+++

## fedora install 

* 下載和安裝 snap
    ```
    sudo dnf install snapd
    sudo ln -s /var/lib/snapd/snap /snap
    ```
* 重新開啟 terminal 或重新登入

* check snap is installed
    ```
    sudo snap install hello-world
    sudo snap install hugo
    ```

* enable automatic updates
sudo snap refresh --unhold hugo

sudo dnf install hugo

## create new post 

hugo new post/my-new-post/index.zh-tw.md

## build 

```
hugo 
```

這樣就可以了