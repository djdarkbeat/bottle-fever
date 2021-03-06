# bottle-fever

A clean-room clone of the Fever RSS aggregator, focusing on providing a compatible API and a simple but scalable feed store and fetcher based on SQLite or Postgres (using the [Peewee](http://peewee.readthedocs.org) ORM) 

# Target Features

* Multi-user support
* Compatible with Reeder apps on iOS and Mac OS X
* URL expansion (i.e., no more junk URLs)
* Grouping of similar items
* Junk filtering (automatic elimination of redundant news items)
* Page extraction from link-only feeds

# Stuff I don't intend to do

* A full-featured web interface (feel free to add your own)

# Related Work

* [Coldsweat](https://github.com/passiomatic/coldsweat), by Andrea Peltrin, is a much nicer, polished solution if you're looking for something like this. And yes, there's a nice web interface in there, too.

# Technical underpinnings

* SQLite database (trivial to replace if you want to scale up, since I use the [Peewee][p] ORM)
* [Bottle][b] web framework
* `gevent` for parallel feed fetching
* Uses Mark Pilgrim's [`feedparser`][fp] as a fallback to HiiDef's [`speedparser`][sp]
* Pick your own HTML parser (`lxml`, `html5lib`, `html.parser`)
* A nice bowl of [BeautifulSoup][bs]


[p]: https://github.com/coleifer/peewee
[b]: http://bottlepy.org
[sp]: https://github.com/hiidef/speedparser
[fp]: https://pypi.python.org/pypi/feedparser/
[bs]: http://www.crummy.com/software/BeautifulSoup/
