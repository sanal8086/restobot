import React from 'react';

export default function Chef3D({ width = 180, height = 220 }) {
  return (
    <iframe
      src="/chef3d.html"
      style={{
        width,
        height,
        border: 'none',
        background: 'transparent',
        pointerEvents: 'none',
      }}
      scrolling="no"
      title="Chef 3D Model"
    />
  );
}
