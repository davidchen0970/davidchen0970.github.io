// document.addEventListener("DOMContentLoaded", function() {
//   // 找到所有畫廊圖片
//   const galleryImages = document.querySelectorAll('.gallery-image');
  
//   galleryImages.forEach(image => {
//     const img = new Image();
//     img.src = image.src;

//     img.onload = function() {
//       const width = img.width;
//       const height = img.height;

//       // 動態設置圖片的寬高
//       image.style.width = `${width}px`;
//       image.style.height = `${height}px`;
      
//       // 設置自訂屬性
//       image.setAttribute('data-flex-grow', (width * 100) / height);
//       image.setAttribute('data-flex-basis', (width * 240) / height + 'px');
//     };

//     // 處理圖片加載錯誤情況
//     img.onerror = function() {
//       console.error('圖片加載失敗:', image.src);
//     };
//   });
// });


// document.addEventListener("DOMContentLoaded", function() {
//   // 找到所有畫廊圖片
//   const galleryImages = document.querySelectorAll('.gallery-image');

//   galleryImages.forEach(image => {
//     const img = new Image();

//     // 啟用跨域請求
//     img.crossOrigin = 'Anonymous'; // 如果服務器支持 CORS，這將允許跨域請求

//     img.src = image.src;

//     img.onload = function() {
//       const width = img.width;
//       const height = img.height;

//       // 動態設置圖片的寬高
//       image.style.width = `${width}px`;
//       image.style.height = `${height}px`;

//       // 設置自訂屬性
//       image.setAttribute('data-flex-grow', (width * 100) / height);
//       image.setAttribute('data-flex-basis', (width * 240) / height + 'px');
//     };

//     // 處理圖片加載錯誤情況
//     img.onerror = function() {
//       console.error('圖片加載失敗:', image.src);
//     };
//   });
// });

// document.addEventListener("DOMContentLoaded", function() {
//   // 找到所有畫廊圖片
//   const galleryImages = document.querySelectorAll('.gallery-image');

//   // 檢查是否找到了任何圖片
//   // alert(`找到 ${galleryImages.length} 張圖片`);

//   galleryImages.forEach((image, index) => {
//     const img = new Image();

//     // 啟用跨域請求
//     img.crossOrigin = 'Anonymous'; // 如果服務器支持 CORS，這將允許跨域請求

//     img.src = image.src;

//     img.onload = function() {
//       const width = img.width;
//       const height = img.height;

//       // 顯示圖片加載成功
//       // alert(`圖片 ${index + 1} 加載成功：寬度 = ${width}px，高度 = ${height}px`);

//       // 動態設置圖片的寬高
//       image.style.width = `${width}px`;
//       image.style.height = `${height}px`;

//       // 設置自訂屬性
//       image.setAttribute('data-flex-grow', (width * 100) / height);
//       image.setAttribute('data-flex-basis', (width * 240) / height + 'px');
//     };

//     // 處理圖片加載錯誤情況
//     img.onerror = function() {
//       // 顯示圖片加載失敗的訊息
//       // alert(`圖片 ${index + 1} 加載失敗: ${image.src}`);
//     };
//   });
// });

document.addEventListener("DOMContentLoaded", function() {
  // 找到所有畫廊圖片
  const galleryImages = document.querySelectorAll('.gallery-image');
  
  galleryImages.forEach(image => {
    const img = new Image();
    img.src = image.src;

    img.onload = function() {
      const width = img.width;
      const height = img.height;

      // 直接修改圖片的 width 和 height 屬性
      image.setAttribute('width', width);
      image.setAttribute('height', height);
      
      // 設置自訂屬性
      image.setAttribute('data-flex-grow', (width * 100) / height);
      image.setAttribute('data-flex-basis', (width * 240) / height + 'px');
    };

    // 處理圖片加載錯誤情況
    img.onerror = function() {
      console.error('圖片加載失敗:', image.src);
    };
  });
});
