# Fun with CSS
# Tasks
## 0. Sprite languages
By using this HTML:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>HBTN - 0- Sprite</title>

        <link href="0-styles.css" media="all" rel="stylesheet" type="text/css">
    </head>
    <body>
        <ul>
            <li>HTML<span class="icon i-html"></span></li>
            <li>CSS<span class="icon i-css"></span></li>
            <li>JavaScript<span class="icon i-js"></span></li>
        </ul>
    </body>
</html>
```
And this image file: 0-sprite.png
![image](https://github.com/gillohsylvia/alx-frontend-for-fun/assets/104779232/6a40c344-daa8-44a8-b51d-4fee0a0869ed)


Create `0-styles.css` and generate this layout:

![image](https://github.com/gillohsylvia/alx-frontend-for-fun/assets/104779232/dd3f582d-5b26-4812-942c-9a68e758aff7)


You are not allowed to change the image and the HTML - sprite is cool!

__Repo:__
* GitHub repository: alx-frontend-for-fun
* File: 0-styles.css
  
## 1. Move the (under)line
By using this HTML:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>HBTN - 1- Underline</title>

        <link href="1-styles.css" media="all" rel="stylesheet" type="text/css">
    </head>
    <body>
        <h2>
            Hello <a href="https://www.holbertonschool.com">Holberton!</a>
        </h2>
    </body>
</html>
```
Create `1-styles.css` and generate this layout where the underline is hidden by default and appeared slowly…:

![image](https://github.com/gillohsylvia/alx-frontend-for-fun/assets/104779232/197a5058-2ba7-41a2-9bb2-c87af5a701e8)


You are not allowed to change the HTML

__Repo:__
* GitHub repository: alx-frontend-for-fun
* File: 1-styles.css
  
## 2. Toggle
By using this HTML:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>HBTN - 2- toggle</title>

        <link href="2-styles.css" media="all" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div class="toggle">
            <input type="checkbox" name="toggle" class="toggle-cb" id="toggle-0" checked>
            <label class="toggle-label" for="toggle-0">
                <div class="toggle-inner"></div>
                <div class="toggle-switch"></div>
            </label>
        </div>
    </body>
</html>
```
Create `2-styles.css` and generate this layout where the `<input>` is has this custom toggle layout:

Checked:
![image](https://github.com/gillohsylvia/alx-frontend-for-fun/assets/104779232/150bd9fb-8b21-4fd0-a0ac-80984b47e81c)

Unchecked:

![image](https://github.com/gillohsylvia/alx-frontend-for-fun/assets/104779232/5fdf629b-5566-40b7-bb13-608bf05b3ab2)


You are not allowed to change the HTML

__Repo:__
* GitHub repository: alx-frontend-for-fun
* File: 2-styles.css
  
## 3. Menu
By using this HTML:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>HBTN - 2- toggle</title>

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="3-styles.css" media="all" rel="stylesheet" type="text/css">
    </head>
    <body>

        <nav class="menu">
            <input type="checkbox" href="#" class="menu-open" name="menu-open" id="menu-open"/>
            <label class="menu-open-button" for="menu-open">
                <span class="menu-line menu-line-1"></span>
                <span class="menu-line menu-line-2"></span>
                <span class="menu-line menu-line-3"></span>
            </label>

            <a href="#" class="menu-item"> <i class="fa fa-area-chart"></i> </a>
            <a href="#" class="menu-item"> <i class="fa fa-bar-chart"></i> </a>
            <a href="#" class="menu-item"> <i class="fa fa-line-chart"></i> </a>
            <a href="#" class="menu-item"> <i class="fa fa-pie-chart"></i> </a>
            <a href="#" class="menu-item"> <i class="fa fa-table"></i> </a>
        </nav>

    </body>
</html>
```
Create 3-styles.css and generate this layout/animation:

![image](https://github.com/gillohsylvia/alx-frontend-for-fun/assets/104779232/12f7d9b5-6e5b-4c43-92b1-38f793147a98)


You are not allowed to change the HTML

__Repo:__
* GitHub repository: alx-frontend-for-fun
* File: 3-styles.css
  
Copyright © 2024 ALX, All rights reserved.

