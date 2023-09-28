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
    <title>3D Voxel Raytracer with Perlin Noise</title>
    <style>
        canvas {
            display: block;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <canvas id="voxelCanvas" width="400" height="400"></canvas>

    <script src="noise.js"></script>

    <script>
        const canvas = document.getElementById("voxelCanvas");
        const ctx = canvas.getContext("2d");

        // Voxel grid settings
        const gridSize = 10;
        const voxelSize = canvas.width / gridSize;
        const maxRaySteps = 100; // Maximum raymarching steps
        const voxelColor = "#00f"; // Blue color for the cube

        // Perlin noise settings
        const noise = new Noise(Math.random());
        const noiseScale = 0.05;
        const noiseThreshold = 0.4;

        function drawVoxel(x, y, color) {
            ctx.fillStyle = color;
            ctx.fillRect(x * voxelSize, y * voxelSize, voxelSize, voxelSize);
        }

        function generateWorld() {
            const world = [];
            for (let x = 0; x < gridSize; x++) {
                world[x] = [];
                for (let y = 0; y < gridSize; y++) {
                    const noiseValue = noise.perlin2(x * noiseScale, y * noiseScale);
                    if (noiseValue > noiseThreshold) {
                        world[x][y] = true;
                    } else {
                        world[x][y] = false;
                    }
                }
            }
            return world;
        }

        function raytrace(world, rayOrigin, rayDirection, depth) {
            if (depth > maxRaySteps) {
                return "#000"; // Return black if max ray steps are reached
            }

            const rayX = Math.floor(rayOrigin.x);
            const rayY = Math.floor(rayOrigin.y);

            if (rayX < 0 || rayX >= gridSize || rayY < 0 || rayY >= gridSize) {
                return "#000"; // Return black if the ray is outside the grid
            }

            if (world[rayX][rayY]) {
                // Hit a voxel, so return its color
                return voxelColor;
            }

            // Calculate the next ray position
            const nextRayOrigin = {
                x: rayOrigin.x + rayDirection.x,
                y: rayOrigin.y + rayDirection.y,
            };

            return raytrace(world, nextRayOrigin, rayDirection, depth + 1);
        }

        function render() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            const world = generateWorld();

            for (let x = 0; x < gridSize; x++) {
                for (let y = 0; y < gridSize; y++) {
                    const rayOrigin = { x: x + 0.5, y: y + 0.5 }; // Center of the voxel
                    const rayDirection = { x: 0.0, y: -1.0 }; // Straight down

                    const color = raytrace(world, rayOrigin, rayDirection, 0);
                    drawVoxel(x, y, color);
                }
            }
        }

        render();
    </script>
</body>
</html>
