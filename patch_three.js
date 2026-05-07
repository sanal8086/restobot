const fs = require('fs');

// Patch GLTFLoader.js
let gltf = fs.readFileSync('c:/Projects/restobot/frontend/public/GLTFLoader.js', 'utf8');
gltf = gltf.replace("} from 'three';", "} from '/three.module.js';");
gltf = gltf.replace("from '../utils/BufferGeometryUtils.js'", "from '/BufferGeometryUtils.js'");
fs.writeFileSync('c:/Projects/restobot/frontend/public/GLTFLoader.js', gltf);
console.log('GLTFLoader patched');

// Patch BufferGeometryUtils.js
let buf = fs.readFileSync('c:/Projects/restobot/frontend/public/BufferGeometryUtils.js', 'utf8');
buf = buf.replace("} from 'three';", "} from '/three.module.js';");
fs.writeFileSync('c:/Projects/restobot/frontend/public/BufferGeometryUtils.js', buf);
console.log('BufferGeometryUtils patched');

// Verify
const verify = fs.readFileSync('c:/Projects/restobot/frontend/public/GLTFLoader.js', 'utf8');
const idx = verify.indexOf('from ');
console.log('First import:', verify.substring(idx, idx + 60));
