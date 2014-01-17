Magipack.js
===========

[Magipack.js](https://github.com/keitakun/Magipack.js) is a Javascript code that will help minimize HTTP requests.

One of the issues on HTTP load time usually are the number of requests and the preferred method to minimize HTTP requests are generating image [Spritesheets](https://www.google.com/search?q=spritesheet&oq=spritesheet&aqs=chrome..69i57j69i59j69i60.1687j0j7&sourceid=chrome&espv=210&es_sm=91&ie=UTF-8).

Though, using Spritesheets you end up with some other issues such:

* Can't use different compressions for each image
* Can't use Spritesheets that exceeds 2048x2048 in most browsers
* Hard to use Spritesheets in *IMG* elements
* Needs repositioning *background-position* in CSS when Spritesheets changes

### So what [Magipack.js](https://github.com/keitakun/Magipack.js) does better than Spritesheets?
It loads a single file which is a concatenation of binary data of the files you want and a json file which maps the position and the size of each file.

This way, you can pack up several images with different file formats in a single file without losing compression or metadatas.

The example files and a python script are in the [examples folder](https://github.com/keitakun/Magipack.js/tree/master/examples) so you can easily generate the pack and config file.


Browser compatibility
---------------------
This examples were tested in Chrome 32, IE7, IE8, IE9, IE10, Safari 7, Firefox 25, Safari iOS 7.
There wasn't any large scale testing for this project yet, so if you find any [issue, please report it](https://github.com/keitakun/Magipack.js/issues).

Examples
========

[example1-static.html](http://hellokeita.in/xp/Magipack.js/example1-static.html)

[example2-instance.html](http://hellokeita.in/xp/Magipack.js/example2-instance.html)

[example3-preloadjs.html](http://hellokeita.in/xp/Magipack.js/example3-preloadjs.html)

### Using as static class
```javascript
Magipack.init();
Magipack.onLoadComplete = function()
{
	document.getElementById("i1").src = Magipack.getURI('forkit.gif');
	document.getElementById("i2").src = Magipack.getURI('mario.jpg');
	document.getElementById("i3").src = Magipack.getURI('Smile.png');
	document.getElementById("container").style.backgroundImage = 'url(' + Magipack.getURI('packman_ghost.gif') + ')';
}

Magipack.load('images.pack', 'images.json');
```

### Using as an instance
```javascript
var mp = new Magipack();
mp.onLoadComplete = function()
{
	// Here you can use either the instance you created or `this` scope.
	document.getElementById("i1").src = this.getURI('forkit.gif');
	document.getElementById("i2").src = mp.getURI('mario.jpg');
	document.getElementById("i3").src = mp.getURI('Smile.png');
	document.getElementById("container").style.backgroundImage = 'url(' + mp.getURI('packman_ghost.gif') + ')';
}
mp.load('images.pack', 'images.json');
```

### Using with [Preload.js](http://www.createjs.com/#!/PreloadJS)
``` javascript
var queue = new createjs.LoadQueue();
queue.on("complete", handleComplete, this);
queue.loadManifest([
	{id: "image", src:"images.pack", type: 'binary'},
	{id: "config", src:"images.json"},
]);
function handleComplete() {
	var mp = new Magipack(queue.getResult('image'), queue.getResult('config'));
	document.getElementById("i1").src = mp.getURI('forkit.gif');
	document.getElementById("i2").src = mp.getURI('mario.jpg');
	document.getElementById("i3").src = mp.getURI('Smile.png');
	document.getElementById("container").style.backgroundImage = 'url(' + mp.getURI('packman_ghost.gif') + ')';
}
```

### Packing images with packImages.py
in terminal, if you are in unix system, set permissions to execute script
```
chmod 0755 packImages.py
```

than run it passing the -p argument for the directory
```
./packImages.py -p assets
```

It'll output *images.json* and *images.pack* in the same directory as *packImages.py* script.