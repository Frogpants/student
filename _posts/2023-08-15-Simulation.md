---
toc: false
comments: false
layout: post
title: Simulation
description: Basically the survival of CSSE
type: tangibles
courses: { compsci: {week: 4} }
---


<!DOCTYPE html>
<html>
<head>
    <title>Scrolling Platformer</title>
    <style>
        /* Add your CSS styling here */
        /* For simplicity, I'll omit most of the styling */
        body {
            margin: 0;
            overflow: hidden;
        }
        canvas {
            display: block;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="800" height="400"></canvas>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        const player = {
            x: canvas.width / 2,
            y: canvas.height / 2,
            width: 50,
            height: 50,
            speed: 5,
            velocityX: 0,
            velocityY: 0,
            jumping: false,
            gravity: 0.5,
        };
        
        const platforms = [
            { x: 0, y: 370, width: 800, height: 10 },
            { x: 200, y: 270, width: 100, height: 10 },
            { x: 400, y: 220, width: 100, height: 10 },
            // Add more platforms as needed
        ];
        
        let worldOffsetX = canvas.width / 2;
        let worldOffsetY = canvas.height / 2;
        
        function drawPlayer() {
            ctx.fillStyle = 'blue';
            ctx.fillRect(player.x - player.width / 2 - worldOffsetX, player.y - player.height / 2 - worldOffsetY, player.width, player.height);
        }
        
        function drawPlatforms() {
            ctx.fillStyle = 'green';
            platforms.forEach(platform => {
                ctx.fillRect(platform.x - worldOffsetX, platform.y - worldOffsetY, platform.width, platform.height);
            });
        }
        
        function update() {
            // Apply gravity to the player
            player.velocityY += player.gravity;
            
            // Update worldOffsetX and worldOffsetY based on the equations
            worldOffsetX += 0.05 * (player.x - worldOffsetX);
            worldOffsetY += 0.05 * (player.y - worldOffsetY);
            
            // Update player position based on input
            if (player.jumping && !isColliding(player.x, player.y + 1, player.width, player.height)) {
                player.velocityY = -12; // Jumping velocity
            }
        
            player.x += player.velocityX;
            player.y += player.velocityY;
        
            // Check collisions with platforms
            if (isColliding(player.x - worldOffsetX, player.y - worldOffsetY, player.width, player.height)) {
                player.jumping = false;
                player.velocityY = 0;
                player.y = findPlatformY(player.x - worldOffsetX, player.y - worldOffsetY, player.width, player.height) - player.height;
            }
        
            // Draw everything
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawPlatforms();
            drawPlayer();
        
            requestAnimationFrame(update);
        }
        
        // Function to check if the player is colliding with a platform
        function isColliding(x, y, width, height) {
            for (let i = 0; i < platforms.length; i++) {
                const platform = platforms[i];
                if (
                    x < platform.x + platform.width &&
                    x + width > platform.x &&
                    y < platform.y + platform.height &&
                    y + height > platform.y
                ) {
                    return true; // Collided
                }
            }
            return false; // No collision
        }
        
        // Function to find the Y-coordinate of the platform below the player
        function findPlatformY(x, y, width, height) {
            for (let i = 0; i < platforms.length; i++) {
                const platform = platforms[i];
                if (
                    x < platform.x + platform.width &&
                    x + width > platform.x &&
                    y + height <= platform.y + platform.height &&
                    y + height + player.velocityY >= platform.y
                ) {
                    return platform.y + platform.height; // Y-coordinate of the platform
                }
            }
            return canvas.height; // No platform found, return the bottom of the canvas
        }
        
        // Handle player controls
        document.addEventListener('keydown', event => {
            if (event.key === 'ArrowRight') {
                player.velocityX = player.speed;
            } else if (event.key === 'ArrowLeft') {
                player.velocityX = -player.speed;
            } else if (event.key === 'ArrowUp' && !player.jumping) {
                player.jumping = true;
            }
        });
        
        document.addEventListener('keyup', event => {
            if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
                player.velocityX = 0;
            }
        });
        
        update();
    </script>
</body>
</html>
