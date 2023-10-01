---
toc: false
comments: true
layout: post
title: Datatypes
description: Data Presentation
type: hacks
courses: { compsci: {week: 5} }
---

<!DOCTYPE html>
<html>
<head>
    <title>Top-Down Scrolling Game</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
        }
        canvas {
            background-color: #000;
            display: block;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas"></canvas>
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        // Set canvas dimensions
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        // Player object
        const player = {
            x: canvas.width / 2,
            y: canvas.height / 2,
            speed: 5,
        };

        // Update player position
        function updatePlayer() {
            if (keys['ArrowUp'] && player.y > 0) {
                player.y -= player.speed;
            }
            if (keys['ArrowDown'] && player.y < canvas.height) {
                player.y += player.speed;
            }
            if (keys['ArrowLeft'] && player.x > 0) {
                player.x -= player.speed;
            }
            if (keys['ArrowRight'] && player.x < canvas.width) {
                player.x += player.speed;
            }
        }

        // Handle keyboard input
        const keys = {};
        window.addEventListener('keydown', (e) => {
            keys[e.key] = true;
        });
        window.addEventListener('keyup', (e) => {
            delete keys[e.key];
        });

        // Game loop
        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Update game objects
            updatePlayer();

            // Draw player
            ctx.fillStyle = '#fff';
            ctx.fillRect(player.x, player.y, 20, 20);

            requestAnimationFrame(gameLoop);
        }

        // Start the game loop
        gameLoop();
    </script>
</body>
</html>
