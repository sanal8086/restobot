const fs = require('fs');

// Read the GLB file and extract animation names (they're stored as ASCII in the JSON chunk)
const buf = fs.readFileSync('c:/Projects/restobot/frontend/public/walking_chef.glb');

// GLB format: 12-byte header, then chunks. First chunk is JSON.
const jsonChunkLength = buf.readUInt32LE(12);
const jsonChunk = buf.slice(20, 20 + jsonChunkLength).toString('utf8');

const gltf = JSON.parse(jsonChunk);

console.log('=== GLB ANIMATIONS ===');
if (gltf.animations && gltf.animations.length > 0) {
  gltf.animations.forEach((anim, i) => {
    console.log(`[${i}] "${anim.name}" - ${anim.channels?.length || 0} channels`);
  });
} else {
  console.log('NO ANIMATIONS FOUND');
}

console.log('\n=== NODES (skeleton) ===');
(gltf.nodes || []).slice(0, 20).forEach((n, i) => {
  console.log(`[${i}] "${n.name}"`);
});
