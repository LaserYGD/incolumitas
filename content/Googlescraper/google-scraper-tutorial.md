Title: GoogleScraper Tutorial - How to scrape 1000 keywords with Google
Date: 2018-09-05 18:21
Modified: 2018-09-07 18:00
Category: GoogleScraper
Tags: tutorial, GoogleScraper, scraping
Slug: googlescraper-tutorial
Author: Nikolai Tschacher
Summary: Tutorial that teaches how to use GoogleScraper to scrape 1000 keywords with 10 selenium browsers.

In this tutorial we are going to show users how to use [GoogleScraper](https://github.com/NikolaiT/GoogleScraper).

The best way to learn a new tool is to use it in a real world case study. And because GoogleScraper allows you to
query search engines automatically, we are going to scrape 1000 keywords with GoogleScraper.

If you don't want to use this software to scrape data and you want this job to be done for you, you can submit a scrape job
at [scrapeulous.com](https://scrapeulous.com/). Or you can visit the [site that explains scrapeulous.com]({filename}/pages/scrapeulous.md).

Anyways, lets continue...

Let's assume that we want to create a business in the USA. We do not know in which industry yet and we do not know in which
city. Therefore we want to scrape some industries. I will take:

1. coffee shop
2. pizza place
3. burger place
4. sea food restaurant
5. pastry shop
6. shoes repair
7. jeans repair
8. smartphone repair
9. wine shop
10. tea shop

Because we do not now in which city we want to open our shop, we are going to combine the above shop places with the **100 largest cities in the US**. Here I found a [list of the Largest 1000 Cities in America](https://gist.github.com/Miserlou/11500b2345d3fe850c92). This will yield 1000 keyword combinations. You can see the final keyword file here: [keyword file](/data/list.txt).


### Installation of GoogleScraper

First of all you need to install **Python3**. I personally use the [Anaconda Python distribution](https://www.anaconda.com/download/), because it ships with many precompiled scientific packages that I need to use in my everyday work. But you can install Python3 also directly from the [python website](https://www.python.org/downloads/).

Now I assume that you have `python3` installed. In my case I have:

```
$ python3 --version
Python 3.7.0
```

Now you need `pip`, the package manager of python. It usually comes installed with python already. When you have pip, you can install
`virtualenv` with `pip install virtualenv`.

Now that you have virtualenv, go to your project directory and create a virtual environment with `virtualenv env`:

In my case it looks like this:
```
nikolai@nikolai:~/projects/work/google-scraper-tutorial$ virtualenv env
Using base prefix '/home/nikolai/anaconda3'
New python executable in /home/nikolai/projects/work/google-scraper-tutorial/env/bin/python
copying /home/nikolai/anaconda3/bin/python => /home/nikolai/projects/work/google-scraper-tutorial/env/bin/python
Installing setuptools, pip, wheel...done.
```

Now we can activate the virtual environment and install GoogleScraper from the github repository:

```
# Activate environment
nikolai@nikolai:~/projects/work/google-scraper-tutorial$ source env/bin/activate
(env) nikolai@nikolai:~/projects/work/google-scraper-tutorial$

# install GoogleScraper
pip install --ignore-installed git+git://github.com/NikolaiT/GoogleScraper/
```

Now you should be all set. When everything worked smoothely, you should have a similar output to this:

```
$ GoogleScraper --version
0.2.2
```

### Preparation and Scraping Options

We will use the Google search engine soley. We will request 10 results per page and only 1 page for each query.

We are going to use 10 simultaenous browser instances in selenium mode. Therefore each browser needs to scrape 100 keywords.

We are going to use one IP address to test how far we can reach with GoogleScraper with a single IP address.

As output we want a `json` file.

We enable caching such that we don't have to start the scraping process from scratch if something fails.

We will pass all configuration via a configuration file to GoogleScraper. We can create such a configuration file
with the following command:

```
GoogleScraper --view-config > config.py
```

Now the file `config.py` is our configuration file.

In this file set the following variables:

```
google_selenium_search_settings = False

google_selenium_manual_settings = False

do_caching = True

do_sleep = True
```

### The Scraping

Now you are ready to scrape. Enter the following command in your the terminal:

```
GoogleScraper --config-file config.py -m selenium --sel-browser chrome --browser-mode normal --keyword-file list.txt -o results.json -z10
```

This will start 10 browser windows that begin to scrape the keywords in the provided file.

After about 22 minutes of scraping, I got the following [results in a json file](/data/results.json).
As you can see there are 1000 results with 10 results per page and all links and snippets and stuff. You can now
analize this data and make marketing decision based on it.

Here is a short video of how the scraping looks like: [Video of scraping](/data/video-scraping.gif).
