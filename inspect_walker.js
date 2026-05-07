const fs = require('fs');

const buf = fs.readFileSync('c:/Projects/restobot/frontend/public/walking_chef.glb');
const jsonChunkLength = buf.readUInt32LE(12);
const jsonChunk = buf.slice(20, 20 + jsonChunkLength).toString('utf8');
const gltf = JSON.parse(jsonChunk);

console.log('=== ANIMATIONS ===');
(gltf.animations || []).forEach((a, i) => {
  console.log(`[${i}] "${a.name}"`);
});
