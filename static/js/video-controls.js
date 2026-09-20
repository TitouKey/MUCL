(function () {
  var ICON_PAUSE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>';
  var ICON_PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';

  var isFr = (document.documentElement.lang || 'en').slice(0, 2) === 'fr';
  var LABEL_PAUSE = isFr ? 'Pause' : 'Pause';
  var LABEL_PLAY = isFr ? 'Lecture' : 'Play';

  var videos = document.querySelectorAll('.crew-video');

  videos.forEach(function (video) {
    var wrap = video.closest('.crew-photo');
    if (!wrap) return;

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'video-pause';
    btn.setAttribute('aria-label', LABEL_PAUSE);
    btn.innerHTML =
      '<span class="video-pause-icon video-pause-icon--pause">' + ICON_PAUSE + '</span>' +
      '<span class="video-pause-icon video-pause-icon--play">' + ICON_PLAY + '</span>';

    var fill = document.createElement('div');
    fill.className = 'video-progress-fill';

    var capsule = document.createElement('div');
    capsule.className = 'video-progress-capsule';
    capsule.appendChild(fill);

    var controls = document.createElement('div');
    controls.className = 'video-controls';
    controls.appendChild(btn);
    controls.appendChild(capsule);
    wrap.appendChild(controls);

    function setPaused(paused) {
      btn.classList.toggle('is-paused', paused);
      btn.setAttribute('aria-label', paused ? LABEL_PLAY : LABEL_PAUSE);
    }

    function updateProgress() {
      var d = video.duration;
      if (isFinite(d) && d > 0) {
        fill.style.width = Math.min(100, (video.currentTime / d) * 100) + '%';
      }
    }

    video.addEventListener('pause', function () { setPaused(true); });
    video.addEventListener('play', function () { setPaused(false); });
    video.addEventListener('loadedmetadata', updateProgress);
    video.addEventListener('timeupdate', updateProgress);
    btn.addEventListener('click', function () {
      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    });

    setPaused(video.paused);
    updateProgress();
  });
})();
