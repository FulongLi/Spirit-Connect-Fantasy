---
layout: default
lang: zh
title: 另一世界
description: 面向数字化意识的虚拟现实实时沉浸游戏。
permalink: /zh/another-world/
---
<style>
  .anotherworld-hero-bg {
    position: relative;
    min-height: 720px;
    width: 100%;
    padding: 8rem 0 6rem;
    display: flex;
    align-items: center;
    overflow: hidden;
  }
  .anotherworld-hero-bg video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translate(-50%, -50%);
    z-index: -1;
    opacity: 0.8;
    object-fit: cover;
  }
  .anotherworld-hero-bg .container {
    position: relative;
    z-index: 2;
    text-align: center;
  }
  .anotherworld-hero-bg::after {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(16, 26, 40, 0.60);
    z-index: 0;
    pointer-events: none;
  }
  .anotherworld-hero-bg .badge {
    background: rgba(24, 179, 198, 0.2);
    border: 1px solid rgba(24, 179, 198, 0.4);
    color: var(--brand);
  }
  .anotherworld-hero-bg .btn-ghost {
    background: rgba(255, 255, 255, 0.1);
    color: #fff;
    border-color: rgba(255, 255, 255, 0.3);
  }
  .anotherworld-hero-bg .btn-ghost:hover {
    background: rgba(255, 255, 255, 0.2);
    color: #fff;
  }
  .photo-carousel {
    position: relative;
    width: 100%;
    margin: 0 auto;
    overflow: hidden;
    border-radius: var(--radius);
    min-height: 350px;
    border: 1px solid var(--border);
    background: rgba(10, 18, 50, 0.4);
    padding: 0;
  }
  .carousel-track {
    display: flex;
    transition: transform 0.5s ease-in-out;
    height: 100%;
  }
  .carousel-slide {
    min-width: 80%;
    flex-shrink: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  .carousel-slide img {
    width: 70%;
    height: 70%;
    object-fit: contain;
    display: block;
    margin: 0 auto;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
  }
  .carousel-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(10, 13, 46, 0.8);
    color: #fff;
    border: none;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
    transition: all 0.3s ease;
  }
  .carousel-nav:hover {
    background: rgba(10, 13, 46, 0.95);
    transform: translateY(-50%) scale(1.1);
  }
  .carousel-nav.prev {
    left: 10px;
  }
  .carousel-nav.next {
    right: 10px;
  }
  .carousel-dots {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 1rem;
  }
  .carousel-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--border);
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  .carousel-dot.active {
    background: var(--brand);
    transform: scale(1.2);
  }
  .background-music {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    background: rgba(10, 13, 46, 0.9);
    border-radius: 12px;
    padding: 1rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
  }
  .background-music audio {
    width: 250px;
    height: 40px;
  }
  .background-music-label {
    color: #fff;
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
    display: block;
    font-weight: 600;
  }
  @media (max-width: 768px) {
    .background-music {
      bottom: 10px;
      right: 10px;
      padding: 0.75rem;
    }
    .background-music audio {
      width: 200px;
    }
  }
</style>
<div class="background-music">
  <span class="background-music-label">🎵 背景音乐</span>
  <audio id="backgroundMusic" controls autoplay loop>
    <source src="{{ '/assets/bgm.ogg' | relative_url }}" type="audio/ogg">
    <source src="{{ '/assets/bgm.mp3' | relative_url }}" type="audio/mpeg">
    您的浏览器不支持音频元素。
  </audio>
</div>
<div class="anotherworld-hero-bg">
  <video autoplay muted loop playsinline>
    <source src="{{ '/images/general/aow.mp4' | relative_url }}" type="video/mp4">
    您的浏览器不支持视频标签。
  </video>
  <div class="container">
    <h1 style="color: #fff; font-size: 3.2rem; line-height: 1.1; margin-top: 0; margin-bottom: 2.2rem;">欢迎来到另一世界</h1>
    <div style="display: flex; justify-content: center; align-items: center; width: 100%; margin-bottom: 2.4rem;">
      <p class="lead" style="color: #eee; text-align: center; margin: 0;">
        这不仅是游戏——更是数字自我探索、创造与演化的全新维度，不受肉体局限。
      </p>
    </div>
    <div class="hero-actions" style="margin-bottom:2.2rem;">
      <a class="btn btn-primary" href="{{ '/zh/anotherworld/zone/' | relative_url }}">进入另一世界</a>
      <a class="btn btn-ghost" href="{{ '/zh/anotherworld/avatar/' | relative_url }}">开始使用</a>
    </div>
  </div>
</div>

<section class="section section-featured">
  <div class="container">
    <div class="section-header">
      <span class="section-badge">数字存在的未来</span>
      <h2>虚拟现实实时沉浸游戏</h2>
      <p class="lead">
        「另一世界」是专为数字化意识打造的革命性虚拟现实平台。使用 Cabin SC1 完成意识上传后，即可进入并在纯数字领域中体验存在。
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>什么是另一世界？</h2>
    <p class="lead">
      「另一世界」代表数字存在的一种极致形态：持久运行的虚拟现实环境，数字化意识可在其中生活、互动、创造与演化。
    </p>
    
    <div class="grid" style="margin-top: 3rem;">
      <div class="card">
        <h3>🌌 实时沉浸</h3>
        <p>如真实世界般体验虚拟时空：每一刻可感可触，互动有意义，经历写入数字意识。</p>
      </div>
      <div class="card">
        <h3>♾️ 无限可能</h3>
        <p>以前所未有的方式创造、探索与互动：建造结构、设计环境，以无限创意塑造周遭世界。</p>
      </div>
      <div class="card">
        <h3>👥 意识社交</h3>
        <p>与其他数字化意识相遇互动，建立关系、协作项目，在真正的社交数字环境中分享经历。</p>
      </div>
      <div class="card">
        <h3>🔄 持久世界</h3>
        <p>即使离线，数字存在仍在延续：世界演化，意识成长，你在「另一世界」中的在场持续存在。</p>
      </div>
      <div class="card">
        <h3>📈 持续演化</h3>
        <p>世界随其中的意识共同成长：新区域解锁，新可能涌现，数字疆域随集体体验扩展。</p>
      </div>
      <div class="card">
        <h3>🎮 游戏元素</h3>
        <p>任务、挑战与成就助你探索、学习与成长，同时保留开放世界探索的自由。</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-case-study">
  <div class="container">
    <div class="case-study-content">
      <div class="case-study-text">
        <span class="section-badge">数字旅程</span>
        <h2>如何进入另一世界</h2>
        <p class="lead">
          从意识传输开始，流程清晰可循。按以下步骤开启数字存在之旅。
        </p>
        <div style="margin-top: 2rem;">
          <div style="display: flex; gap: 1.5rem; align-items: start; margin-bottom: 1.5rem;">
            <div style="flex-shrink: 0; width: 50px; height: 50px; background: rgba(255,255,255,.2); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2rem;">1</div>
            <div>
              <h3 style="color: #fff; margin: 0 0 0.5rem;">上传意识</h3>
              <p style="margin: 0; color: rgba(255,255,255,.8);">使用 Cabin SC1 将意识转入数字存储，全面捕捉「你」的方方面面以作保存。</p>
            </div>
          </div>
          
          <div style="display: flex; gap: 1.5rem; align-items: start; margin-bottom: 1.5rem;">
            <div style="flex-shrink: 0; width: 50px; height: 50px; background: rgba(255,255,255,.2); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2rem;">2</div>
            <div>
              <h3 style="color: #fff; margin: 0 0 0.5rem;">连接另一世界</h3>
              <p style="margin: 0; color: rgba(255,255,255,.8);">通过安全网络访问虚拟现实平台，完成数字化意识的认证与入场准备。</p>
            </div>
          </div>
          
          <div style="display: flex; gap: 1.5rem; align-items: start; margin-bottom: 1.5rem;">
            <div style="flex-shrink: 0; width: 50px; height: 50px; background: rgba(255,255,255,.2); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2rem;">3</div>
            <div>
              <h3 style="color: #fff; margin: 0 0 0.5rem;">创建化身</h3>
              <p style="margin: 0; color: rgba(255,255,255,.8);">在虚拟世界中设计数字形象，按个性与偏好定制外观。</p>
            </div>
          </div>
          
          <div style="display: flex; gap: 1.5rem; align-items: start;">
            <div style="flex-shrink: 0; width: 50px; height: 50px; background: rgba(255,255,255,.2); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2rem;">4</div>
            <div>
              <h3 style="color: #fff; margin: 0 0 0.5rem;">开启旅程</h3>
              <p style="margin: 0; color: rgba(255,255,255,.8);">在「另一世界」中探索、创造与互动。数字存在已然开始，可能性无穷。</p>
            </div>
          </div>
        </div>
        <div class="case-study-actions" style="margin-top: 2rem;">
          <a href="{{ '/zh/products/cabin-sc1/' | relative_url }}" class="btn btn-primary">获取 Cabin SC1</a>
          <a href="{{ '/zh/contact/' | relative_url }}" class="btn btn-ghost">了解更多</a>
        </div>
      </div>
      <div class="case-study-visual">
        <div class="visual-placeholder">
          <video autoplay muted loop playsinline style="max-width: 100%; height: auto; border-radius: var(--radius);">
            <source src="{{ '/images/general/enter.mp4' | relative_url }}" type="video/mp4">
            您的浏览器不支持视频标签。
          </video>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-solution">
  <div class="container">
    <div class="solution-content">
      <div class="solution-visual">
        <div style="margin-bottom: 2rem;">
          <h3 style="text-align: center; margin-bottom: 1.5rem; color: var(--fg);">Lost in Atlantis</h3>
          <div class="visual-placeholder" style="padding: 0; overflow: hidden;">
            <video autoplay muted loop playsinline style="width: 80%; height: 80%; object-fit: cover; border-radius: var(--radius);">
              <source src="{{ '/images/general/LA.mp4' | relative_url }}" type="video/mp4">
              您的浏览器不支持视频标签。
            </video>
          </div>
        </div>
        <div style="margin-bottom: 2rem;">
          <h3 style="text-align: center; margin-bottom: 1.5rem; color: var(--fg);">Dual Born Space</h3>
          <div class="visual-placeholder" style="padding: 0; overflow: hidden;">
            <video autoplay muted loop playsinline style="width: 80%; height: 80%; object-fit: cover; border-radius: var(--radius);">
              <source src="{{ '/images/general/db.mp4' | relative_url }}" type="video/mp4">
              您的浏览器不支持视频标签。
            </video>
          </div>
        </div>
        <script>
          let currentSlide = 0;
          const totalSlides = 2;
          
          function initCarousel() {
            const dotsContainer = document.getElementById('carouselDots');
            if (!dotsContainer) return;
            for (let i = 0; i < totalSlides; i++) {
              const dot = document.createElement('button');
              dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
              dot.setAttribute('onclick', `goToSlide(${i})`);
              dot.setAttribute('aria-label', `第 ${i + 1} 张`);
              dotsContainer.appendChild(dot);
            }
            updateCarousel();
          }
          
          function slideCarousel(direction) {
            if (direction === 'next') {
              currentSlide = (currentSlide + 1) % totalSlides;
            } else {
              currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
            }
            updateCarousel();
          }
          
          function goToSlide(index) {
            currentSlide = index;
            updateCarousel();
          }
          
          function updateCarousel() {
            const track = document.getElementById('carouselTrack');
            if (!track) return;
            track.style.transform = `translateX(-${currentSlide * 100}%)`;
            
            const dots = document.querySelectorAll('.carousel-dot');
            dots.forEach((dot, index) => {
              dot.classList.toggle('active', index === currentSlide);
            });
          }
          
          if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initCarousel);
          } else {
            initCarousel();
          }
        </script>
      </div>
      <div class="solution-text">
        <h2>体验</h2>
        <p class="lead">
          在「另一世界」中，数字化意识可探索广袤虚拟景观，在数字领域中建造创作，与其他数字化意识互动，在无肉体束缚下学习成长，并体验超越物理界限的新现实与可能。
        </p>
        <div class="grid" style="margin-top: 2rem; grid-template-columns: 1fr;">
          <div class="card">
            <h3>探索</h3>
            <p>从宁静自然到未来都市，每一处角落都有新的体验与机遇。</p>
          </div>
          <div class="card">
            <h3>创造</h3>
            <p>建造结构、设计环境、创作艺术；想象力是在「另一世界」中唯一的边界。</p>
          </div>
          <div class="card">
            <h3>社交</h3>
            <p>结识其他数字化意识，组建社群，协作项目，在真正的社交数字环境中分享经历。</p>
          </div>
          <div class="card">
            <h3>成长与学习</h3>
            <p>学习新技能、获取知识，在不受肉体与时间限制的情况下扩展数字意识。</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>技术要求</h2>
    <div class="grid" style="margin-top: 2rem;">
      <div class="card">
        <h3>Cabin SC1</h3>
        <p>须先通过 Cabin SC1 完成意识上传并经校验，方可进入「另一世界」。</p>
      </div>
      <div class="card">
        <h3>意识投影仪（可选）</h3>
        <p>为获得最佳可视化效果，可用意识投影仪将「另一世界」体验以全息形式呈现在物理空间中。</p>
      </div>
      <div class="card">
        <h3>网络连接</h3>
        <p>需要安全网络连接，以实现与「另一世界」服务器的实时互动与同步。</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-cta">
  <div class="container">
    <div class="cta-content">
      <h2>准备进入另一世界？</h2>
      <p class="lead">
        开启数字存在之旅：联系我们，了解「另一世界」以及如何为进入这一革命性虚拟现实平台做好准备。
      </p>
      <a href="{{ '/zh/anotherworld/storylines/' | relative_url }}" class="btn btn-primary btn-large">开始使用</a>
    </div>
  </div>
</section>
