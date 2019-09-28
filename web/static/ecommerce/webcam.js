'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snap = document.getElementById("snap");
const errorMsgElement = document.querySelector('span#errorMsg');

const constraints = {
  audio: true,
  video: {
    width: 1280, height: 720
  }
};

// Access webcam
async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
  }
}

// Success
function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;
}

// Load init
init();

// Draw image
var context = canvas.getContext('2d');
var data = new FormData();
snap.addEventListener("click", () => {
  context.drawImage(video, 0, 0);
  let image = new Image();
  image.src = canvas.toDataURL('image/png');
  console.log("image captured, sendingnow");
  data.append('img', image);
  $.ajax({
      url : "http://127.0.0.1:8000/api/process/",
      processData : false,
      contentType : false,
      type : 'POST',
      data : data,
  }).done(function(data) {
      // work with data    
      console.log("image processed")         
  });
});
