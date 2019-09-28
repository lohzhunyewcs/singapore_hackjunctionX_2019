"use strict";
class Elem {
    constructor(svg, tag, parent = svg) {
        this.elem = document.createElementNS(svg.namespaceURI, tag);
        parent.appendChild(this.elem);
    }
    attr(name, value) {
        if (typeof value === 'undefined') {
            return this.elem.getAttribute(name);
        }
        this.elem.setAttribute(name, value.toString());
        return this;
    }
    observe(event) {
        return Observable.fromEvent(this.elem, event);
    }
}

const constraints = {
  video: true
};


navigator.mediaDevices.getUserMedia(constraints).
  then((stream) => {video.srcObject = stream});

const captureVideoButton =
  document.querySelector('#screenshot .capture-button');
const screenshotButton = document.querySelector('#snap');
const img = new Image();
const video = document.querySelector('#video');

const canvas = document.querySelector('canvas');

// captureVideoButton.onclick = function() {
//   navigator.mediaDevices.getUserMedia(constraints).
//     then(handleSuccess).catch(handleError);
// };

screenshotButton.onclick = function() {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0);
  // var c = document.getElementById('canvas')
  // var ctx = c.getContext("2d")
  // ctx.beginPath()
  // ctx.rect(0, 0, 150, 100)
  // ctx.stroke()
  // Other browsers will fall back to image/png
  img.src = canvas.toDataURL();
  let data_to_sent ={ 
    'imgBase64': img.src,
 };
 console.log(img.src);
 console.log(`length of b64: ${img.src.length}`)
 console.log(`data_to_sent: ${data_to_sent}`);
  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:8000/api/process/",
    data: data_to_sent['imgBase64']//{'data': data_to_sent}
    fail: function(svg) {
      
    }
  }).done(function(o) {
    console.log('saved')
    // const svg1 = document.createElementNS('rect', )
    // document.getElementById('canvas').getContext('2d').rect(50, 100, 20, 70)
    // document.getElementById('canvas').getContext('2d').lineWidth = 15
    // If you want the file to be visible in the browser 
    // - please modify the callback in javascript. All you
    // need is to return the url to the file, you just saved 
    // and than put the image in your browser.
  }).fail((o  ) =>{
    console.log('fail xD')
    console.log(`o: ${o}`)

    
  })
  
};

function handleSuccess(stream) {
  screenshotButton.disabled = false;
  video.srcObject = stream;
}


// const video = document.getElementById('video');
// const canvas = document.getElementById('canvas');
// const snap = document.getElementById("snap");
// const errorMsgElement = document.querySelector('span#errorMsg');

// const constraints = {
//   audio: true,
//   video: {
//     width: 1280, height: 720
//   }
// };

// // Access webcam
// async function init() {
//   try {
//     const stream = await navigator.mediaDevices.getUserMedia(constraints);
//     handleSuccess(stream);
//   } catch (e) {
//     errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
//   }
// }

// // Success
// function handleSuccess(stream) {
//   window.stream = stream;
//   video.srcObject = stream;
// }

// // Load init
// init();

// // Draw image
// let request = new XMLHttpRequest();
// var context = canvas.getContext('2d');
// var data = new FormData();
// snap.addEventListener("click", () => {
//   context.drawImage(video, 0, 0);
//   // let image = new Image();
//   let image = canvas.toDataURL('image/png');
//   console.log(`image: ${image}`);
//   console.log("image captured, sendingnow");
//   console.log(`data: ${data}`);
//   data.append('img', image);
//   console.log(`data['img']: ${data.get('img')}`);
//   request.open('POST', '/api/process/');
//   request.send(data);
//   return false;
//   // $.ajax({
//   //     url : "http://127.0.0.1:8000/api/process/",
//   //     processData : false,
//   //     contentType : false,
//   //     type : 'POST',
//   //     data : data,
//   // }).done(function(data) {
//   //     // work with data    
//   //     console.log("image processed")         
//   // });
// });
