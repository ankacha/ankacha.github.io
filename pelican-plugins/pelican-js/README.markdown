# pelican-js

pelican-js makes it easy to embed custom JavaScript into individual
Pelican articles and pages.

## How

`git clone https://notabug.org/jorgesumle/pelican-js` in your plugins
folder and add the name of the plugin to your pelicanconf.py file:

```python
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-js'] # You may have more plugins
```

Next, create `js` directory in your `content` directory...

```
website/
├── content
│   ├── js/
│   │   ├── your_custom_script1.js
│   │   └── your_custom_script2.js
│   ├── article1.md
│   └── pages
│       └── about.md
└── pelican.conf.py
```

And then add each resource as a comma-separated file name in the `JS`
tag. You must specify where to place the script inside a parenthesis
after the file name:
- top. Will place the script in the `head` HTML tag
- bottom. Will place the script in the `body` HTML tag

If the location of a script is not specified, it will be place inside
the `<body>` tag.

```
Title: Mejor sin Wordpress
Date: 2017-02-09 18:51
Tags: programación, Wordpress, generador de páginas estáticas, generador de sitios web estáticos, rendimiento, eficiencia, comodidad, desventajas
Category: Desarrollo web
Author: jorgesumle
Slug: mejor-sin-wordpress
JS: your_custom_script1.js (top), your_custom_script2.js (bottom)
```

Finally, in your base template (likely named `base.html`), you need
to add the following in your `<head>` tag...

```
{% if article %}
    {% if article.js %}
        {% for script in article.js %}
            {% if 'top' in script[-7:] %}
                {{ script[:-5]|format(SITEURL) }}
            {% endif %}
        {% endfor %}
    {% endif %}
{% endif %}
```
And the following just before the closing `</body>` tag...
```
{% if article %}
    {% if article.js %}
        {% for script in article.js %}
            {% if 'bottom' in script[-7:] %}
                {{ script[:-8]|format(SITEURL) }}
            {% endif %}
        {% endfor %}
    {% endif %}
{% endif %}
```

So, in the template I use for my blog now looks like the following:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset=utf-8">
    <title>{% block title %} {{SITENAME}} {% endblock %}</title>
    <link rel="stylesheet" href="{{ SITEURL }}/theme/css/style.css" type="text/css">
    {% if article %}
        {% if article.js %}
            {% for script in article.js %}
                {% if 'top' in script[-7:] %}
                    {{ script[:-5]|format(SITEURL) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}
  </head>
  <body>
    <div class=container>
        {% block header %}
            {% include "header.html" %}
        {% endblock %}

        <div class="content">
        {% block content %} {% endblock %}
        </div>

        {% block footer %}
            {% include "footer.html" %}
        {% endblock %}
    </div>
    {% if article %}
        {% if article.js %}
            {% for script in article.js %}
                {% if 'bottom' in script[-7:] %}
                    {{ script[:-8]|format(SITEURL) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}
  </body>
</html>
```

That's it! Run your standard `make html` or `make publish` commands
and your JavaScript files will be copied and ref'd in the right places.

The previous code only works for articles. For most people that's
enough. If you want to enable custom JavaScript in pages too insert the
following code your `<head>` tag...

    {% if page %}
        {% if page.js %}
            {% for script in page.js %}
                {% if 'top' in script[-7:] %}
                    {{ script[:-5]|format(SITEURL) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}

And the following code in the `<body>` tag...

    {% if page %}
        {% if page.js %}
            {% for script in page.js %}
                {% if 'bottom' in script[-7:] %}
                    {{ script[:-8]|format(SITEURL) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}

The final result, which works both for articles and for pages, looks
like this...

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset=utf-8">
    <title>{% block title %} {{SITENAME}} {% endblock %}</title>
    <link rel="stylesheet" href="{{ SITEURL }}/theme/css/style.css" type="text/css">
    {% if article %}
        {% if article.js %}
            {% for script in article.js %}
                {% if 'top' in script[-7:] %}
                    {{ script[:-5]|format(SITEURL) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}
    {% if page %}
        {% if page.js %}
            {% for script in page.js %}
                {% if 'top' in script[-7:] %}
                    {{ script[:-5]|format(SITEURL) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}
  </head>
  <body>
    <div class=container>
        {% block header %}
            {% include "header.html" %}
        {% endblock %}

        <div class="content">
        {% block content %} {% endblock %}
        </div>

        {% block footer %}
            {% include "footer.html" %}
        {% endblock %}
    </div>
    {% if article %}
        {% if article.js %}
            {% for script in article.js %}
                {% if 'bottom' in script[-7:] %}
                    {{ script[:-8]|format(SITEURL) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}
    {% if page %}
        {% if page.js %}
            {% for script in page.js %}
                {% if 'bottom' in script[-7:] %}
                    {{ script[:-8]|format(SITEURL) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}
  </body>
</html>
```
