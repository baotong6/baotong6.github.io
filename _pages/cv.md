---
layout: single
title: "Curriculum Vitae"
permalink: /cv/
---

{% include base_path %}

<!-- 下载按钮 -->
<div style="display:flex; justify-content:flex-end; margin-bottom:1em;">
  <a href="{{ '/assets/files/TongCV.pdf' | relative_url }}" target="_blank" 
     style="text-decoration:none; font-weight:bold; color:#fff; background:#007acc; padding:0.5em 1em; border-radius:4px;">
    ⬇ Download CV
  </a>
</div>

<!-- PDF 预览 -->
<div style="width:100%; max-width:900px; margin:0 auto; box-shadow:0 2px 10px rgba(0,0,0,0.1); border-radius:8px; overflow:hidden;">
  <iframe src="{{ '/assets/files/TongCV.pdf' | relative_url }}" 
          style="width:100%; height:calc(100vh - 150px); border:none;" 
          frameborder="0"></iframe>
</div>

<script>
  // 保证iframe高度自适应
  const iframe = document.querySelector("iframe");
  function resizeIframe() {
    const topOffset = document.querySelector('header').offsetHeight + 40; // 留出header +按钮空间
    iframe.style.height = (window.innerHeight - topOffset) + "px";
  }
  window.addEventListener("resize", resizeIframe);
  resizeIframe();
</script>
