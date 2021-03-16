// Tensorflow.JS file to test cellSTORM in the browser
// Create local server:  python -m http. server 8000
let model;
let webcam;

// Some parameters
const square_x = 1;
const square_y = 2;
const N_time = 30;
const N_x = 256;
const N_y = 256;
const N_mag = 2;

const webcamElement = document.querySelector('video');
//const webcamElement = document.getElementById('webcam');
webcamElement.width = N_x/2;
webcamElement.height = N_y/2;


// Creating HTML5 canvas elements to display stuff
function createCanvases() {
  const canvas = document.createElement('canvas');
  canvas.width = N_x;
  canvas.height = N_y;
  canvas.id = `output`;
  document.body.appendChild(canvas);
  document.body.appendChild(
    document.createElement('br'),
);
}

// Normalize Data
function normalize(inputmat) {
  const min = inputmat.min();
  const max = inputmat.max();
  inputmat = inputmat.sub(min).div(max.sub(min));
  return inputmat;
}


// Loaded the TensorFlow.js model
// (which was converted from a Keras model.h5)
async function loadModel() {
    model = await tf.loadLayersModel('./converted_model128_30_keras/model.json', strict=false);
    model.summary();
}

// Initializing the application
async function init() {

      //createCanvases();

      // Create an object from Tensorflow.js data API which could capture image
      // from the web camera as Tensor.
      webcam = await tf.data.webcam(webcamElement);

      console.log('Loading Model...');
      await loadModel();
      console.log('Successfully loaded model');

      computeFrames();

}


async function computeFrames() {
  // Initialize model and camera

  let iframe = 0

  // Get the first frame, extract and crop info
  const img = await webcam.capture();
  let img_stack = (img.slice([0, 0, 0], [img.shape[0], img.shape[1], 1]))
  //img_stack = tf.image.cropAndResize(img_stack.expandDims(0), [[0, 0, N_x, N_x]], [0], [N_x, N_y])


  while (true) {

    const img = await webcam.capture();
    const img_gray = (img.slice([0, 0, 0], [img.shape[0], img.shape[1], 1]))

    // concatenate frames
    img_stack = tf.concat([img_stack, img_gray], 2);
    //const result = await model.classify(img);



    if(img_stack.size==(N_x/N_mag*N_y/N_mag*N_time)){
      console.log("Predicting result...");

      img_stack = img_stack.cast('float32');


      // reshape and predict (from Android convention..)
      const img_stack_norm = tf.tidy(() => {
        const max = tf.max(img_stack);
        const min = tf.min(img_stack);
  
        return tf.div(tf.sub(img_stack, min), tf.sub(max, min))
      });


      //img_stack = normalize(img_stack);
      //console.log("stack mean: ");
      //console.log(img_stack.mean())
      /*
      const img_stack_min = tf.min(img_stack);
      img_stack_min.print();
      var img_stack_norm = tf.clone(img_stack);
      img_stack_norm = tf.sub(img_stack_norm, img_stack_min);
      const img_stack_max = tf.max(img_stack_norm);
      img_stack_max.print();
      img_stack_norm = tf.div(img_stack_norm, img_stack_max);
  
      const img_stack_1d = tf.reshape(img_stack_norm,[1,N_x/2*N_y/2*N_time]);
          */
      const myresult = model.predict(img_stack_norm.transpose([2,0,1]).expandDims(0));
      
      const myresult_2d = myresult.reshape([N_x,N_y]);
      //myresult_2d = tf.mul(myresult_2d, 255);

      //img_stack_norm.max().dataSync()
      
      // reshape and predict (from Android convention..)
      const myresult_2d_norm = tf.tidy(() => {
        const max = tf.max(myresult_2d);
        const min = tf.min(myresult_2d);
  
        return tf.div(tf.sub(myresult_2d, min), tf.sub(max, min))
      });

      
      // Display result
      const canvas = document.getElementById(`output`);
      await tf.browser.toPixels(tf.mul(myresult_2d_norm, 1), canvas);
      
      // Free Memory
      myresult.dispose();
      myresult_2d.dispose();
      myresult_2d_norm.dispose();
  
      // append images
      img_stack = img_gray;
    }

    // Dispose the tensor to release the memory.
    img.dispose();

    // Give some breathing room by waiting for the next animation frame to
    // fire.
    await tf.nextFrame();
  }
}

init();

