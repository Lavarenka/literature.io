"use strict"



window.onload = function () {


    const parallax = document.querySelector('.parallax');

    if (parallax) {
        const content = document.querySelector('.parallax__container');
        const fon = document.querySelector('.images-parralax__fon');
        const forest = document.querySelector('.images-parralax__forest');
        const book = document.querySelector('.images-parralax__book');

        //коэффициэнты
        const forFon = 40;
        const forForest = 20;
        const forBook = 10;

        //speed
        const speed = 0.05;

        //переменные
        let positionX = 0, positionY = 0;
        let coordXprocent = 0, coordYprocent = 0;

        function setMouseParallaxStyle() {
            const distX = coordXprocent - positionX;
            const distY = coordYprocent - positionY;

            positionX = positionX + (distX * speed);
            positionY = positionY + (distY * speed);

            // передаем стили
            fon.style.cssText = `transform: translate(${positionX / forFon}%, ${positionY / forFon}%);`;
            forest.style.cssText = `transform: translate(${positionX / forForest}%, ${positionY / forForest}%);`;
            book.style.cssText = `transform: translate(${positionX / forBook}%, ${positionY / forBook}%);`;

            requestAnimationFrame(setMouseParallaxStyle);
        }

        setMouseParallaxStyle();

        parallax.addEventListener("mousemove", function (e) {
            const parallaxWidth = parallax.offsetWidth;
            const parallaxHeight = parallax.offsetHeight;
            //ноль по середине
            const coordX = e.pageX - parallaxWidth / 2;
            const coordY = e.pageY - parallaxHeight / 2;
            //получаем проценты
            coordXprocent = coordX / parallaxWidth * 100;
            coordYprocent = coordY / parallaxHeight * 100;
        });

    }
}

