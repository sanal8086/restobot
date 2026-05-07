export const getBrowserFingerprint = () => {
    const {
        userAgent,
        language,
        platform,
        hardwareConcurrency,
        deviceMemory
    } = window.navigator;

    const {
        width,
        height,
        colorDepth,
        pixelDepth
    } = window.screen;

    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

    const getCanvasFingerprint = () => {
        try {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = 200;
            canvas.height = 50;
            
            // Draw a complex pattern with text and emojis
            ctx.textBaseline = "top";
            ctx.font = "14px 'Arial'";
            ctx.textBaseline = "alphabetic";
            ctx.fillStyle = "#f60";
            ctx.fillRect(125, 1, 62, 20);
            ctx.fillStyle = "#069";
            ctx.fillText("RestoBot<canvas>🚀", 2, 15);
            ctx.fillStyle = "rgba(102, 204, 0, 0.7)";
            ctx.fillText("Unique-Identity", 4, 17);
            
            return canvas.toDataURL();
        } catch (e) {
            return "";
        }
    };

    const canvasData = getCanvasFingerprint();

    // Combine properties into a string
    const data = [
        userAgent,
        language,
        platform,
        hardwareConcurrency,
        deviceMemory,
        width,
        height,
        colorDepth,
        pixelDepth,
        timezone,
        canvasData // Adding the graphics engine signature
    ].join('|');

    // Simple hash function (djb2)
    let hash = 5381;
    for (let i = 0; i < data.length; i++) {
        hash = (hash * 33) ^ data.charCodeAt(i);
    }
    
    // Convert to positive hex string
    return (hash >>> 0).toString(16);
};
