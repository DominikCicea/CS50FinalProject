# Dominik's Donuts
#### Video Demo: https://youtu.be/5TKAy1eQR4I
#### Description: Dominik's Donuts is an online shop where you can order donuts, and pay with your card.
----------------------------------------------------------------------------------------------------------------------------------------------------------
Wanna try it yourself? 1) Download ZIP and Extract 2) Open CMD and navigate to the '/CS50FinalProject' folder 3) Type 'flask run' and open the link.

Common newbie Error: "'flask' is not recognized as an internal or external command,
operable program or batch file."

Solution: run 'python -m flask run' in the CMD.
----------------------------------------------------------------------------------------------------------------------------------------------------------
I made this beautiful header image using Canva, and spent some time googling how to make images react when you hover over them using your mouse. The website has a main page, a contact page, and a shopping cart. Everything in the cart is dynamic so when you remove an item, the numbers on the page change. I did that using the Jinja for loops and placeholders. The contact page is a simple form where you can type your name, email, and your message. My main folder contains app.py where I configured the application, project.db where I store information about each donut, and requirements.txt to import flask, requests, etc. My templates folder contains 4 files: layout.html, index.html, contact.html, and cart.html.

layout.html: The layout contains the elements that never change regardless of which page we are on: Header image, Navigation bar, favicon and footer.

index.html: index is the homepage of the website where I showcase 10 donuts and the divs have beautiful on-hover effects. Each donut has an add-to-cart button which triggers an alert saying "Donut added to your cart!"

I added 2 donuts to the background, I used a fixed position and I lowered the opacity so that when we scroll down, the donuts stay in the same position, creating a cool effect.

contact.html: contact is a very simple form that has a Name input, email input, and a message input. The button triggers an alert saying "Message sent!"

cart.html: the cart is a cart and checkout page in one. You can remove an item simply by clicking the X button next to the price of the donut, all digits on the page change depending on how many donuts are in the cart.

The checkout container has 4 inputs for the card details, and below is the subtotal, free shipping, and total price of the order, and the Checkout button which triggers an alert saying "Thank you for your purchase!" The backend of the project is very simple since the only thing I had to do is use SQL tables for the donuts and the cart that hold the donut name, donut image URL, quantity, and price. I think I only used JavaScript for one or two buttons. The project would look much better if I used AJAX but I already started studying Cyber Security and decided that the website is pretty good the way it is.

I really enjoyed creating it, and even though I'm probably not going to be a Web Developer, this was a really cool experience!
