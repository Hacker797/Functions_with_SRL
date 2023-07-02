# Locator

The `Locator` class is a Python class that takes in a URL string and provides methods to access and manipulate different parts of the URL.

## Usage

To use the `Locator` class, first create an instance by passing in a URL string:

```python
link = Locator('https://www.YouTube/video/share/Gkgprekghrps24332/media/admin')
```

Once you have an instance of the `Locator` class, you can use the following methods to access and manipulate the URL:

- `srl()`: Returns the original URL string.
- `kind()`: Returns the protocol (e.g. 'https') of the URL.
- `location()`: Returns the location (e.g. 'www.YouTube') of the URL.
- `location_parts()`: Returns a list of the parts of the location of the URL.
- `resource()`: Returns the resource (e.g. '/video/share/Gkgprekghrps24332/media/admin') of the URL.
- `resource_parts()`: Returns a list of the parts of the resource of the URL.
- `parent()`: Creates a new `Locator` object without the last part of the resource in the URL¹[1].
- `within(resource_part: str)`: Creates a new `Locator` object with an additional part added to the resource in the URL²[2].

## Example

Here is an example of how to use the `Locator` class:

```python
link = Locator('https://www.YouTube/video/share/Gkgprekghrps24332/media/admin')

print(f"""srl: {link.srl()}
kind: {link.kind()}
location: {link.location()}
location_parts: {link.location_parts()}
resources: {link.resource()}
resources_parts: {link.resource_parts()}
parent: {link.parent().srl()}
check 1: {link.parent().resource_parts()}
within: {link.within('index').srl()}
check 2: {link.within('index').resource_parts()}""")
```

This will output:

```
srl: https://www.YouTube/video/share/Gkgprekghrps24332/media/admin
kind: https
location: www.YouTube
location_parts: ['www', 'YouTube']
resources: /video/share/Gkgprekghrps24332/media/admin
resources_parts: ['', 'video', 'share', 'Gkgprekghrps24332', 'media', 'admin']
parent: https://www.YouTube/video/share/Gkgprekghrps24332/media
check 1: ['', 'video', 'share', 'Gkgprekghrps24332', 'media']
within: https://www.YouTube/video/share/Gkgprekghrps24332/media/admin/index
check 2: ['', 'video', 'share', 'Gkgprekghrps24332', 'media', 'admin', 'index']
```
