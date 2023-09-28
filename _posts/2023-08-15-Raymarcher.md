---
toc: false
comments: false
layout: post
title: Raymarcher
description: A complicated raymarch rendering engine
type: tangibles
courses: { compsci: {week: 3} }
---


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raymarcher with Shading</title>
    <style>
        canvas {
            display: block;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <canvas id="raymarchCanvas" width="700" height="700"></canvas>

    <script>
        const canvas = document.getElementById("raymarchCanvas");
        const ctx = canvas.getContext("2d");

        // Raymarching settings
        const maxIterations = 100;
        const epsilon = 0.001;
        const maxDistance = 5.0;

        // Lighting settings
        const lightDirection = { x: 1.0, y: 1.0, z: 1.0 };
        const lightIntensity = 1.0;

        function sceneDistance(point) {
            // Define the scene here (e.g., a sphere)
            const sphereCenter = { x: 0.0, y: 0.0, z: 0.0 };
            const sphereRadius = 1.0;

            const dx = point.x - sphereCenter.x;
            const dy = point.y - sphereCenter.y;
            const dz = point.z - sphereCenter.z;

            return Math.sqrt(dx * dx + dy * dy + dz * dz) - sphereRadius;
        }

        function calculateNormal(point) {
            const d = epsilon * 2.0;
            const normal = {
                x: sceneDistance({ x: point.x + d, y: point.y, z: point.z }) - sceneDistance({ x: point.x - d, y: point.y, z: point.z }),
                y: sceneDistance({ x: point.x, y: point.y + d, z: point.z }) - sceneDistance({ x: point.x, y: point.y - d, z: point.z }),
                z: sceneDistance({ x: point.x, y: point.y, z: point.z + d }) - sceneDistance({ x: point.x, y: point.y, z: point.z - d }),
            };
            const length = Math.sqrt(normal.x * normal.x + normal.y * normal.y + normal.z * normal.z);
            normal.x /= length;
            normal.y /= length;
            normal.z /= length;
            return normal;
        }

        function calculateLighting(normal) {
            const dotProduct = normal.x * lightDirection.x + normal.y * lightDirection.y + normal.z * lightDirection.z;
            return Math.max(dotProduct, 0) * lightIntensity;
        }

        function rayMarch(origin, direction) {
            let distance = 0.0;
            for (let i = 0; i < maxIterations; i++) {
                const point = {
                    x: origin.x + direction.x * distance,
                    y: origin.y + direction.y * distance,
                    z: origin.z + direction.z * distance,
                };

                const dist = sceneDistance(point);
                distance += dist;

                if (dist < epsilon || distance >= maxDistance) {
                    const normal = calculateNormal(point);
                    const lighting = calculateLighting(normal);
                    return lighting;
                }
            }
            return 0.0;
        }

        function render() {
            const imageData = ctx.createImageData(canvas.width, canvas.height);

            const aspectRatio = canvas.width / canvas.height;
            const fov = Math.PI / 2.0;
            const cameraPos = { x: 0.0, y: 0.0, z: -3.0 };

            for (let y = 0; y < canvas.height; y++) {
                for (let x = 0; x < canvas.width; x++) {
                    const u = (2.0 * x - canvas.width) / canvas.width;
                    const v = (2.0 * y - canvas.height) / canvas.height;

                    const direction = {
                        x: Math.tan(fov * 0.5) * u * aspectRatio,
                        y: Math.tan(fov * 0.5) * v,
                        z: 1.0,
                    };

                    const lighting = rayMarch(cameraPos, direction);
                    const color = [255 * lighting, 255 * lighting, 255 * lighting, 255];

                    const pixelIndex = (x + y * canvas.width) * 4;
                    imageData.data[pixelIndex] = color[0];
                    imageData.data[pixelIndex + 1] = color[1];
                    imageData.data[pixelIndex + 2] = color[2];
                    imageData.data[pixelIndex + 3] = color[3];
                }
            }

            ctx.putImageData(imageData, 0, 0);
        }

        render();
    </script>
</body>
</html>
