const https = require('https');
const fs = require('fs');

// Three.js official animated soldier model with walk/run animations
const url = 'https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/gltf/Xbot.glb';
const dest = 'c:/Projects/restobot/frontend/public/walking_chef.glb';

function download(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    https.get(url, (res) => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        file.close();
        fs.unlinkSync(dest);
        return download(res.headers.location, dest).then(resolve).catch(reject);
      }
      res.pipe(file);
      file.on('finish', () => {
        file.close();
        const size = fs.statSync(dest).size;
        console.log('Downloaded:', dest, '(' + (size/1024).toFixed(1) + ' KB)');
        resolve();
      });
    }).on('error', (err) => {
      fs.unlinkSync(dest);
      reject(err);
    });
  });
}

download(url, dest)
  .then(() => console.log('Done!'))
  .catch(err => console.error('Failed:', err.message));
